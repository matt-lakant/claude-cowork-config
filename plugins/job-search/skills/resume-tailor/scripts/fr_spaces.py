#!/usr/bin/env python3
"""French typography in a .docx or a text file: non-breaking space before ; : ? ! and inside « ».
Standard library only.

Matt's rule (his preferences, and R22 of cv_rules.md): in any document written in French, the
space before ; : ? ! and inside « » is a non-breaking space (U+00A0), never a plain one. The CVs
he returns from Word carry plain spaces, so a draft built on one of them inherits them, and new
text is right or wrong depending on the run. This script puts the whole file right in one pass.

Usage:  python3 fr_spaces.py <in> <out>      <in> and <out> may be the same path only for a file
                                             this run has just created (a draft, a redline);
                                             never for a file Matt returned.
        python3 fr_spaces.py <in> --count    reports how many spaces are wrong, changes nothing.

In a .docx the text of every run is corrected, tracked insertions included; deleted text is left
as it was. A space at the end of one run followed by the punctuation at the start of the next,
in the same paragraph, is corrected too. Layout, styles and tracked changes are untouched.
"""
import re, sys, zipfile

NB = " "
INNER = [(re.compile(r"(?<=[^\s  ]) (?=[;:?!»])"), NB), (re.compile(r"(?<=«) "), NB)]
WT = re.compile(r"(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)")


def fix_text(t):
    n = 0
    for rx, rep in INNER:
        t, k = rx.subn(rep, t)
        n += k
    return t, n


def fix_xml(xml):
    total = 0
    out = []
    for para in re.split(r"(?<=</w:p>)", xml):
        parts = WT.split(para)                      # [pre, open, text, close, pre, ...]
        idx = list(range(2, len(parts), 4))
        for i in idx:
            parts[i], n = fix_text(parts[i])
            total += n
        for a, b in zip(idx, idx[1:]):             # across two runs of the same paragraph
            if parts[a].endswith(" ") and re.match(r"[;:?!»]", parts[b]):
                parts[a] = parts[a][:-1] + NB
                total += 1
            if re.match(r" [;:?!»]", parts[b]) and parts[a] and not parts[a][-1].isspace():
                parts[b] = NB + parts[b][1:]
                total += 1
            if parts[a].endswith("«") and parts[b].startswith(" "):
                parts[b] = NB + parts[b][1:]
                total += 1
        out.append("".join(parts))
    return "".join(out), total


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    count_only = dst == "--count"
    if src.lower().endswith(".docx"):
        zin = zipfile.ZipFile(src)
        items = [(i, zin.read(i.filename)) for i in zin.infolist()]
        zin.close()
        total, new = 0, []
        for info, data in items:
            if re.match(r"word/(document|header\d*|footer\d*)\.xml$", info.filename):
                xml, n = fix_xml(data.decode("utf-8"))
                total += n
                data = xml.encode("utf-8")
            new.append((info, data))
        if not count_only:
            zout = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
            for info, data in new:
                zout.writestr(info, data)
            zout.close()
    else:
        text, total = fix_text(open(src, encoding="utf-8").read())
        if not count_only:
            open(dst, "w", encoding="utf-8").write(text)
    print("FR_SPACES: %d plain space(s) %s" % (total, "found" if count_only else "replaced by a non-breaking space in %s" % dst))


if __name__ == "__main__":
    main()
