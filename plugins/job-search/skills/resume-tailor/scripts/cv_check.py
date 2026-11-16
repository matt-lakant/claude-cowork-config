#!/usr/bin/env python3
"""Mechanical pre-delivery check of a CV, a letter or a text piece against Matt's standing rules.

Standard library only. Reads the document as it would look with every tracked change
accepted (inserted text kept, deleted text dropped), so it works on a draft and on a redline.

Usage:
  python3 cv_check.py <file> --rules <_assets/cv_rules.md> [--profile <_assets/candidate_profile.md>]
                      [--kind cv|letter|text] [--tags non_sales,non_finance,ps_role]
                      [--top-keywords "a;b;c"]

  <file>     a .docx (CV or letter) or a .md / .txt file (message, form answers, interview prep)
  --kind     cv (default), letter (cover letter .docx) or text (anything else Matt sends or says:
             recruiter message, form answer, interview answers). A check that carries
             "kinds": ["cv"] in the rules only runs for that kind; "level_by_kind" lets a check
             be a FAIL on a CV and a WARN elsewhere (a letter may name a tool Matt has not used,
             because gaps are handled there; a CV may not). Layout checks (header, page, file
             name, client engagements) are skipped for a text file.

  --rules    file holding the fenced block  ```json cv-checks ... ```  (the machine-readable rules)
  --profile  candidate_profile.md; the "Never print" column of its "Current values" table is
             turned into forbidden strings (superseded figures and wordings)
  --tags     conditions that apply to this posting; a check with "when": ["non_sales"] only
             runs when that tag is passed. Checks with no "when" always run.
  --top-keywords  "EMEA;master data;professional services": words of the job title and core
             nouns of the posting that must appear above the skills matrix (header, profile,
             areas of expertise), where a six-second skim stops. One FAIL per missing keyword.

Exit code 1 when at least one FAIL is reported. WARN lines never fail the run: they are judged
by the model and listed in the memo.
"""
import argparse, json, os, re, sys, zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def par_text(p):
    """Text of a paragraph with tracked changes accepted; line breaks become \\n."""
    out = []
    for el in p.iter():
        if el.tag == W + "t":
            out.append(el.text or "")
        elif el.tag == W + "br":
            out.append("\n")
    return "".join(out)


def par_style(p):
    st = p.find(W + "pPr/" + W + "pStyle")
    return st.get(W + "val") if st is not None else ""


def load_blocks(path):
    """Body content in document order: ('p', text, style) and ('tbl', [cell texts])."""
    if not path.lower().endswith(".docx"):
        return [("p", l, "") for l in open(path, encoding="utf-8").read().splitlines()]
    root = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml"))
    body = root.find(W + "body")
    blocks = []
    for ch in body:
        if ch.tag == W + "p":
            blocks.append(("p", par_text(ch), par_style(ch)))
        elif ch.tag == W + "tbl":
            blocks.append(("tbl", [par_text(p) for p in ch.iter(W + "p")], ""))
    return blocks


def page_size(path):
    """(width, height) in twips of the first section, or None."""
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    m = re.search(r"<w:pgSz[^>]*>", xml)
    if not m:
        return None
    w, h = re.search(r'w:w="(\d+)"', m.group(0)), re.search(r'w:h="(\d+)"', m.group(0))
    return (int(w.group(1)), int(h.group(1))) if w and h else None


def load_checks(rules_path):
    src = open(rules_path, encoding="utf-8").read()
    m = re.search(r"```json cv-checks\s*\n(.*?)\n```", src, re.S)
    if not m:
        sys.exit("cv_check: no ```json cv-checks block found in " + rules_path)
    return json.loads(m.group(1))


def load_never_print(profile_path):
    """Backticked strings in the 'Never print' column of the Current values table."""
    out = []
    lines = open(profile_path, encoding="utf-8").read().splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("## Current values"))
    except StopIteration:
        return None
    col = None
    for l in lines[start + 1:]:
        if l.startswith("## "):
            break
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if col is None:
            if "Never print" in cells:
                col = cells.index("Never print")
            continue
        if col < len(cells):
            for s in re.findall(r"`([^`]+)`", cells[col]):
                out.append((s, cells[0]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--rules", required=True)
    ap.add_argument("--profile")
    ap.add_argument("--tags", default="")
    ap.add_argument("--top-keywords", default="")
    ap.add_argument("--kind", default="cv", choices=["cv", "letter", "text"])
    a = ap.parse_args()
    tags = {t.strip() for t in a.tags.split(",") if t.strip()}
    is_docx = a.docx.lower().endswith(".docx")
    blocks = load_blocks(a.docx)
    lines = []
    for kind, content, _ in blocks:
        for t in ([content] if kind == "p" else content):
            lines.extend(x for x in t.split("\n") if x.strip())
    results = []  # (level, id, message)

    def add(level, cid, msg):
        results.append((level, cid, msg))

    def excerpt(line, m):
        s, e = max(0, m.start() - 40), min(len(line), m.end() + 40)
        return "..." + line[s:e] + "..."

    for c in load_checks(a.rules):
        when = c.get("when")
        if when and not (set(when) & tags):
            continue
        if c.get("kinds") and a.kind not in c["kinds"]:
            continue
        if not is_docx and c["type"] in ("header", "page", "filename", "engagements"):
            continue
        level = c.get("level_by_kind", {}).get(a.kind, c.get("level", "FAIL")).upper()
        flags = 0 if c.get("case") else re.I
        kind = c["type"]
        if kind == "forbid":
            rx = re.compile(c["pattern"], flags)
            for l in lines:
                m = rx.search(l)
                if m:
                    add(level, c["id"], c.get("message", "") + " | " + excerpt(l, m))
        elif kind == "require_if":
            if any(re.search(c["if"], l, flags) for l in lines):
                rx = re.compile(c["pattern"], flags)
                for l in lines:
                    if re.search(c["if"], l, flags) and not rx.search(l):
                        add(level, c["id"], c.get("message", "") + " | " + l[:120])
        elif kind == "header":
            # first non-empty paragraph after the name: every visual line must fit on one line
            ps = [b for b in blocks if b[0] == "p" and b[1].strip()]
            if len(ps) > 1:
                hl = [x for x in ps[1][1].split("\n") if x.strip()]
                if len(hl) > c.get("max_lines", 99):
                    add(level, c["id"], "header has %d lines, max %d" % (len(hl), c["max_lines"]))
                for x in hl:
                    if len(x) > c.get("max_line_chars", 95):
                        add(level, c["id"], "header line of %d characters may wrap: %s" % (len(x), x))
        elif kind == "engagements":
            label = re.compile(c["label"], re.I)
            counts, i = [], 0
            while i < len(blocks):
                k, t, st = blocks[i]
                if k == "p" and label.match(t.strip()):
                    n, j = 0, i + 1
                    while j < len(blocks) and blocks[j][0] == "p" and not blocks[j][2].lower().startswith("heading") \
                            and not label.match(blocks[j][1].strip()):
                        if blocks[j][1].strip():
                            n += 1
                        j += 1
                    counts.append(n)
                    i = j
                else:
                    i += 1
            if counts != c["expected"]:
                add(level, c["id"], "%s: found %s, expected %s" % (c.get("message", "client engagements per role"), counts, c["expected"]))
        elif kind == "page":
            size = page_size(a.docx)
            if size != (c["width"], c["height"]):
                add(level, c["id"], "%s: page is %s twips, expected (%d, %d). Run to_a4.py" % (c.get("message", "page size"), size, c["width"], c["height"]))
        elif kind == "filename":
            if not re.match(c["pattern"], os.path.basename(a.docx)):
                add(level, c["id"], c.get("message", "") + " | " + os.path.basename(a.docx))
        else:
            add("WARN", c.get("id", "?"), "unknown check type " + kind)

    kws = [k.strip() for k in a.top_keywords.split(";") if k.strip()]
    if kws:
        top = []
        for kind, content, _ in blocks:
            if kind == "tbl":
                break
            top.append(content)
        top_text = " ".join(top).lower()
        for k in kws:
            if k.lower() not in top_text:
                add("FAIL", "top-keywords", "'%s' is absent above the skills matrix (header, profile, areas of expertise)" % k)

    if a.profile:
        never = load_never_print(a.profile)
        if never is None:
            add("WARN", "current-values", "no '## Current values' table found in the profile: figures were not checked")
        else:
            for s, fact in never:
                for l in lines:
                    i = l.lower().find(s.lower())
                    if i >= 0:
                        add("FAIL", "superseded", "'%s' is superseded (Current values: %s) | ...%s..." % (s, fact, l[max(0, i - 40):i + len(s) + 40]))

    words = sum(len(l.split()) for l in lines)
    fails = [r for r in results if r[0] == "FAIL"]
    for level, cid, msg in sorted(results):
        print("%s [%s] %s" % (level, cid, msg))
    print("INFO kind=%s words=%d (all tracked changes accepted) tags=%s" % (a.kind, words, ",".join(sorted(tags)) or "none"))
    print("RESULT: %d FAIL, %d WARN" % (len(fails), len(results) - len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
