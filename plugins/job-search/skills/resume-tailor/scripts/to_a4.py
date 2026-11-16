#!/usr/bin/env python3
"""Set a .docx to A4 without moving a line break. Standard library only.

Matt's CV template and every CV tailored before 2026-11-16 were US Letter (12240 x 15840 twips).
A4 is 334 twips narrower, and the template's tables are fixed at the Letter text width, so the
side margins are reduced by 167 twips each: the text width, the tables and the line breaks stay
as they were, and only the page gets taller.

Usage:  python3 to_a4.py <in.docx> <out.docx>
<out.docx> must be a different path: Office files are never overwritten (make the backup or the
new version first, then write to the name you need). A file already in A4 is copied unchanged.
"""
import re, sys, zipfile

A4_W, A4_H, LETTER_W = 11906, 16838, 12240


def convert(xml):
    changed = False

    def page(m):
        nonlocal changed
        tag = m.group(0)
        w = int(re.search(r'w:w="(\d+)"', tag).group(1))
        if 'w:orient="landscape"' in tag or w == A4_W:
            return tag
        changed = True
        tag = re.sub(r'w:w="\d+"', 'w:w="%d"' % A4_W, tag)
        return re.sub(r'w:h="\d+"', 'w:h="%d"' % A4_H, tag)

    was_letter = ('w:w="%d"' % LETTER_W) in "".join(re.findall(r"<w:pgSz[^>]*>", xml))
    xml = re.sub(r"<w:pgSz[^>]*>", page, xml)
    if changed and was_letter:
        half = (LETTER_W - A4_W) // 2

        def margins(m):
            tag = m.group(0)
            for side in ("left", "right"):
                v = int(re.search(r'w:%s="(\d+)"' % side, tag).group(1))
                tag = re.sub(r'w:%s="\d+"' % side, 'w:%s="%d"' % (side, max(v - half, 567)), tag)
            return tag

        xml = re.sub(r"<w:pgMar[^>]*>", margins, xml)
    return xml, changed


def main():
    if len(sys.argv) != 3 or sys.argv[1] == sys.argv[2]:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        changed = False
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                xml, changed = convert(data.decode("utf-8"))
                data = xml.encode("utf-8")
            zout.writestr(item, data)
    print("converted to A4" if changed else "already A4, copied unchanged")


if __name__ == "__main__":
    main()
