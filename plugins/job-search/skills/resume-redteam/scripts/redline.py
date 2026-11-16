#!/usr/bin/env python3
"""Apply a reviewer's edits to a .docx as Word tracked changes. Needs python-docx (lxml).

Usage:
  python3 redline.py <draft.docx> <redline.docx> <edits.json> [--author Recruiter]

<redline.docx> must be a new path: the draft is never overwritten.

edits.json is a list. Each entry is one of:
  {"old": "<text copied verbatim from the document>", "new": "<replacement>"}
        replace OLD by NEW. An empty "new" deletes OLD. OLD may span several runs of the same
        paragraph (python-docx users: it need not sit in one run), but not a line break, a
        hyperlink or text that an earlier edit of this run inserted.
  {"cut": "<first words of a paragraph>"}
        delete the whole paragraph, paragraph mark included. The prefix must identify one
        paragraph only.

Edits are applied in list order. Give OLD enough words to be unique; when it occurs several
times the first occurrence is taken and a warning is printed.

The script prints one line per edit that could not be applied and exits with code 1 if there is
any: a redline with silently missing edits is worse than no redline. It then re-reads the result
with every change accepted and checks that each NEW string is there.
"""
import copy, datetime, json, sys
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
IGNORED = {qn("w:proofErr"), qn("w:bookmarkStart"), qn("w:bookmarkEnd")}


class Redliner:
    def __init__(self, document, author):
        self.d = document
        self.author = author
        self.date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        ids = [int(e.get(qn("w:id"))) for tag in ("w:ins", "w:del") for e in document.element.iter(qn(tag))
               if (e.get(qn("w:id")) or "").isdigit()]
        self.next_id = max(ids + [899]) + 1

    def mark(self, tag):
        e = OxmlElement(tag)
        e.set(qn("w:id"), str(self.next_id)); self.next_id += 1
        e.set(qn("w:author"), self.author)
        e.set(qn("w:date"), self.date)
        return e

    @staticmethod
    def is_plain(r):
        """A run that holds only text (and its formatting)."""
        return r.tag == qn("w:r") and all(c.tag in (qn("w:rPr"), qn("w:t")) for c in r) and r.find(qn("w:t")) is not None

    @staticmethod
    def run_text(r):
        return "".join(t.text or "" for t in r.findall(qn("w:t")))

    @staticmethod
    def make_run(rpr, text, deleted=False):
        r = OxmlElement("w:r")
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        t = OxmlElement("w:delText" if deleted else "w:t")
        t.text = text
        t.set(XML_SPACE, "preserve")
        r.append(t)
        return r

    def groups(self, p):
        """Maximal sequences of plain runs that are direct children of the paragraph."""
        out, cur = [], []
        for ch in p:
            if self.is_plain(ch):
                cur.append(ch)
            elif ch.tag in IGNORED:
                continue
            else:
                if cur:
                    out.append(cur)
                cur = []
        if cur:
            out.append(cur)
        return out

    def paragraphs(self):
        return list(self.d.element.body.iter(qn("w:p")))

    def count(self, old):
        return sum("".join(self.run_text(r) for r in g).count(old) for p in self.paragraphs() for g in self.groups(p))

    def replace(self, old, new):
        for p in self.paragraphs():
            for g in self.groups(p):
                text = "".join(self.run_text(r) for r in g)
                i = text.find(old)
                if i < 0:
                    continue
                j, pos, covered, first_rpr = i + len(old), 0, [], None
                for r in g:
                    t = self.run_text(r)
                    a, b = pos, pos + len(t)
                    pos = b
                    if b <= i or a >= j:
                        continue
                    rpr = r.find(qn("w:rPr"))
                    if first_rpr is None:
                        first_rpr = rpr
                    head, mid, tail = t[:max(i - a, 0)], t[max(i - a, 0):min(j, b) - a], t[min(j, b) - a:]
                    if head:
                        r.addprevious(self.make_run(rpr, head))
                    dr = self.make_run(rpr, mid, deleted=True)
                    r.addprevious(dr)
                    covered.append(dr)
                    if tail:
                        r.addprevious(self.make_run(rpr, tail))
                    p.remove(r)
                dele = self.mark("w:del")
                covered[0].addprevious(dele)
                for dr in covered:
                    dele.append(dr)
                if new:
                    ins = self.mark("w:ins")
                    ins.append(self.make_run(first_rpr, new))
                    dele.addnext(ins)
                return True
        return False

    def cut(self, prefix):
        hits = [p for p in self.paragraphs() if accepted_text(p).startswith(prefix)]
        if len(hits) != 1:
            return "prefix matches %d paragraphs" % len(hits)
        p = hits[0]
        runs = [ch for ch in p if ch.tag == qn("w:r")]
        if not runs:
            return "paragraph has no direct run (already edited?)"
        dele = self.mark("w:del")
        runs[0].addprevious(dele)
        for r in runs:
            for t in r.findall(qn("w:t")):
                t.tag = qn("w:delText")
            dele.append(r)
        ppr = p.find(qn("w:pPr"))
        if ppr is None:
            ppr = OxmlElement("w:pPr"); p.insert(0, ppr)
        rpr = ppr.find(qn("w:rPr"))
        if rpr is None:
            rpr = OxmlElement("w:rPr"); ppr.append(rpr)
        rpr.append(self.mark("w:del"))
        return None


def accepted_text(p):
    return "".join(t.text or "" for t in p.iter(qn("w:t")))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    author = "Recruiter"
    if "--author" in sys.argv:
        author = sys.argv[sys.argv.index("--author") + 1]
        args.remove(author)
    if len(args) != 3 or args[0] == args[1]:
        sys.exit(__doc__)
    src, out, edits_path = args
    edits = json.load(open(edits_path, encoding="utf-8"))
    d = docx.Document(src)
    rl = Redliner(d, author)
    failed, applied = [], 0
    for k, e in enumerate(edits, 1):
        if "cut" in e:
            err = rl.cut(e["cut"])
            if err:
                failed.append((k, "CUT " + e["cut"][:60], err))
            else:
                applied += 1
            continue
        old, new = e["old"], e.get("new", "")
        n = rl.count(old)
        if n == 0:
            failed.append((k, old[:60], "OLD not found (check it is verbatim, in one paragraph, and not inside an earlier insertion)"))
            continue
        if n > 1:
            print("WARN edit %d: OLD occurs %d times, first occurrence taken | %s" % (k, n, old[:60]))
        rl.replace(old, new)
        applied += 1
    d.save(out)
    # verification on the saved file, every change accepted
    full = "\n".join(accepted_text(p) for p in docx.Document(out).element.body.iter(qn("w:p")))
    for k, e in enumerate(edits, 1):
        if e.get("new") and all(f[0] != k for f in failed) and e["new"] not in full:
            failed.append((k, e["new"][:60], "NEW not found in the saved file"))
    for k, what, why in failed:
        print("NOT APPLIED edit %d: %s | %s" % (k, what, why))
    print("RESULT: %d of %d edits applied, author %s, saved to %s" % (applied, len(edits), author, out))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
