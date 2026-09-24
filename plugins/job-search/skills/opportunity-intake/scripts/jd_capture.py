"""jd_capture.py: posting card (LinkedIn "About the job", Collective.work mission) -> posting PDF -> job_description.md

Runs in the CLOUD WORKSPACE with its preinstalled tools only (Playwright + Chromium,
pdfplumber). Nothing is installed, nothing runs on Matt's machine.

  python3 jd_capture.py sum <card.html>                            # code points + checksum, to match the browser
  python3 jd_capture.py pdf <card.html> <header.json> <out.pdf>    # render the card with Chromium
  python3 jd_capture.py md  <posting.pdf> <out.md> [<source-url>]  # extract the PDF to markdown
"""
import html, json, re, sys


def checksum(path):
    s = open(path, encoding="utf-8").read().rstrip("\n")
    return len(s), sum(ord(c) for c in s)


CSS = """
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #111; }
h1 { font-size: 17pt; margin: 0 0 .3em; }
h2 { font-size: 13.5pt; margin: 1.1em 0 .4em; }
ul.meta { list-style: none; padding: 0; margin: 0 0 1em; font-size: 9pt; color: #333; }
ul.meta li::before { content: none; }
ul { list-style: none; margin: .2em 0 .6em 0; padding-left: 1.1em; }
li { margin: .15em 0; text-indent: -1.1em; }
li::before { content: "\\2022\\00a0\\00a0"; }   /* bullet as real text, so it survives extraction */
ol { list-style: none; margin: .2em 0 .6em 0; padding-left: 1.6em; counter-reset: n; }
ol > li { counter-increment: n; text-indent: -1.6em; }
ol > li::before { content: counter(n) ".\\00a0\\00a0"; }   /* number as real text, no bullet */
a { color: #0a66c2; text-decoration: none; }
"""


def render_pdf(card, header, out):
    """Chromium prints the card exactly as a browser lays it out."""
    from playwright.sync_api import sync_playwright
    h = json.load(open(header, encoding="utf-8"))
    esc = lambda s: html.escape(s or "")
    meta = "".join(f"<li><b>{esc(k)}:</b> {esc(v)}</li>" for k, v in h.get("meta", {}).items() if v)
    doc = (f'<!doctype html><html><head><meta charset="utf-8">'
           f'<title>{esc(h["title"])} — {esc(h["company"])}</title><style>{CSS}</style></head><body>'
           f'<h1>{esc(h["title"])} — {esc(h["company"])}</h1><ul class="meta">{meta}</ul>'
           f'{open(card, encoding="utf-8").read()}</body></html>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(doc, wait_until="load")
        pg.pdf(path=out, format="A4", print_background=True,
               margin={"top": "2cm", "bottom": "2cm", "left": "2cm", "right": "2cm"},
               display_header_footer=True, header_template="<span></span>",
               footer_template='<div style="font-size:8px;width:100%;text-align:right;'
                               'padding-right:2cm;color:#666"><span class="pageNumber"></span> / '
                               '<span class="totalPages"></span></div>')
        b.close()


NUM = re.compile(r"^(\d+)\.\s+")                                    # "1.  text" from an <ol>
META = re.compile(r"^(Company|Location|Source|Retrieved|Application):\s*(.*)$")   # header block written by render_pdf


def to_md(pdf, out, url=None):
    """Rebuild headings, bullets and paragraphs from font size, weight and spacing."""
    import pdfplumber
    lines = []
    with pdfplumber.open(pdf) as doc:
        for page in doc.pages:
            body_bottom = page.height - 50          # drop footers (page numbers, print stamps)
            for ln in page.extract_text_lines(return_chars=True, keep_blank_chars=True):
                if ln["top"] > body_bottom or not ln["text"].strip():
                    continue
                chars = [c for c in ln["chars"] if c["text"].strip()]
                size = max(c["size"] for c in chars)
                bold = sum("Bold" in c["fontname"] for c in chars) / len(chars) > 0.9
                lines.append({"t": ln["text"].strip(), "size": size, "bold": bold,
                              "top": ln["top"], "bottom": ln["bottom"], "x": ln["x0"], "page": page.page_number})
    if not lines:
        raise SystemExit("no text in PDF (scanned image?): ask Matt to paste the posting")
    body = sorted(l["size"] for l in lines)[len(lines) // 2]   # median = body text size
    blocks, prev = [], None
    for l in lines:
        t = l["t"]
        if l["size"] >= body * 1.5:
            kind = "#"
        elif l["size"] >= body * 1.2:
            kind = "##"
        elif l["bold"] and len(t) < 90 and not t.startswith("•"):
            kind = "###"
        elif t.startswith("•"):
            kind, t = "-", t.lstrip("•  ").strip()
        elif NUM.match(t):
            kind, t = "n", NUM.sub(r"\1. ", t, count=1)        # numbered item from an <ol>
        elif META.match(t):
            kind = "meta"
        else:
            kind = "p"
        gap = (l["top"] - prev["bottom"]) if prev and prev["page"] == l["page"] else 99
        cont = (prev and kind == "p" and blocks and blocks[-1][0] in ("p", "-", "n")
                and gap < l["size"] * 0.6)                       # wrapped line of the same block
        if cont:
            blocks[-1][1] += " " + t
        elif kind == "###" and blocks and blocks[-1][0] == "###" and gap < l["size"] * 0.6:
            blocks[-1][1] += " " + t
        else:
            blocks.append([kind, t])
        prev = l
    md = []
    for kind, t in blocks:
        if kind == "meta":
            m = META.match(t)
            md.append(f"- **{m.group(1)}:** {m.group(2)}")
        elif kind in ("#", "##", "###"):
            md.append(f"{kind} {t}")
        elif kind == "-":
            md.append(f"- {t}")
        elif kind == "n":
            md.append(t)
        else:
            md.append(t)
    text = "\n\n".join(md)
    text = re.sub(r"\n\n(?=- |\d+\. )", "\n", text)                    # tight lists
    text = re.sub(r"(?m)^((?:- |\d+\. ).*)\n(?!- |\d+\. )", r"\1\n\n", text)
    text = re.sub(r"(?m)^(#.*)\n(?=- |\d+\. )", r"\1\n\n", text)     # blank line between a heading and its list
    if url and url not in text:
        text = f"- **Source:** {url}\n\n" + text
    open(out, "w", encoding="utf-8").write(re.sub(r"\n{3,}", "\n\n", text).strip() + "\n")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sum":
        print(*checksum(sys.argv[2]))
    elif cmd == "pdf":
        render_pdf(*sys.argv[2:5]); print("wrote", sys.argv[4])
    elif cmd == "md":
        to_md(*sys.argv[2:5]); print("wrote", sys.argv[3])
