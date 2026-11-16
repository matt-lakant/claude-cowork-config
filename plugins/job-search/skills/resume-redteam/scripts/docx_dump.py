#!/usr/bin/env python3
"""Print the text of a .docx in document order, tables included. Standard library only.

Usage:  python3 docx_dump.py <file.docx> [--view accepted|original|marked]

  accepted  (default) the text with every tracked change accepted: what the reader gets
  original  the text with every tracked change rejected: the draft before the redline
  marked    both, deletions as [-text-] and insertions as [+text+]

Paragraphs print as  P<n>: text  and table cells as  T<n> r<row>c<col>: text . Line breaks inside a
paragraph print as " / ". Use it to give a reviewer the CV or letter as text, to copy OLD strings
verbatim for redline.py, and to read a redline without opening Word. python-docx's
paragraph.text is not a substitute: it skips text inside tracked insertions.
"""
import sys, zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def text(p, view):
    out = []

    def walk(el, state):
        for ch in el:
            st = state
            if ch.tag == W + "ins":
                st = "ins"
            elif ch.tag == W + "del":
                st = "del"
            if ch.tag == W + "t":
                if view == "original" and state == "ins":
                    continue
                out.append("[+%s+]" % ch.text if (view == "marked" and state == "ins") else (ch.text or ""))
            elif ch.tag == W + "delText":
                if view == "accepted":
                    continue
                out.append("[-%s-]" % ch.text if view == "marked" else (ch.text or ""))
            elif ch.tag == W + "br":
                out.append(" / ")
            else:
                walk(ch, st)

    walk(p, None)
    return "".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    view = sys.argv[sys.argv.index("--view") + 1] if "--view" in sys.argv else "accepted"
    if view in args:
        args.remove(view)
    if len(args) != 1 or view not in ("accepted", "original", "marked"):
        sys.exit(__doc__)
    body = ET.fromstring(zipfile.ZipFile(args[0]).read("word/document.xml")).find(W + "body")
    n = 0
    for ch in body:
        if ch.tag == W + "p":
            t = text(ch, view)
            if t.strip():
                print("P%d: %s" % (n, t))
            n += 1
        elif ch.tag == W + "tbl":
            for r, row in enumerate(ch.findall(W + "tr")):
                for c, cell in enumerate(row.findall(W + "tc")):
                    t = " / ".join(x for x in (text(p, view) for p in cell.iter(W + "p")) if x.strip())
                    if t.strip():
                        print("T%d r%dc%d: %s" % (n, r, c, t))
            n += 1


if __name__ == "__main__":
    main()
