---
name: opportunity-intake
description: "The front door of the job-search pipeline. Opens an opportunity: confirms its name, creates its folder under applications/, starts its notes file, and routes to the right next skill. Use whenever a named company, recruiter, hiring manager, agency contact, mission or role enters the conversation and anything at all is going to come out of it — a LinkedIn thread, a call to prepare, a freelance enquiry, a targeting note, a spontaneous application — and before any other job-search skill writes a file. Every other job-search skill calls this first."
---

# Opportunity Intake

## What this skill does

Opens an opportunity and gives it a home before any work happens:

1. Confirms the opportunity name.
2. Creates `applications/<slug>/` if it does not exist.
3. Starts `applications/<slug>/notes.md` if it does not exist.
4. Routes to the skill that should actually do the work.

It exists because the pipeline's entry point was implicit. When no other skill
fired — a LinkedIn thread, a call to prepare, a mission enquiry — deliverables got
written wherever the session happened to be, and the opportunity lost its file history.
Observed repeatedly in September 2026: seven opportunity files loose in the project root.

## When this runs

- **First, in every other job-search skill.** They all point here.
- **On its own**, whenever a named company, recruiter, hiring manager, agency contact,
  mission or role enters the conversation and a file is going to come out of it.

Trigger on the **subject**, not the verb. *"Prépare-moi pour l'appel avec Nick de
Masento"* opens an opportunity even though nobody said *interview*, *resume* or *apply*.
So does a targeting note, a LinkedIn message to a named person at a named company, a
freelance mission brief, or a spontaneous candidature. Nothing has to have been applied
to yet — a first call is an opportunity.

Work that is genuinely **not** tied to one opportunity — a market sweep, a list of open
roles across several companies, a review of Matt's own LinkedIn profile — does not open
one. See *Non-opportunity outputs* below.

## Precondition — the project folder must be connected

> Paths in this skill are relative to the **Job Applications project root** — the folder
> holding `applications/`, `_assets/` and `applications_tracker.md`.

1. Run `ls $HOME/mnt/` and look for `Job Applications`.
2. If it is not there, call `device_request_folder_access` on
   `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications`.
3. If that fails, **stop and tell Matt**. Do not fall back to another connected folder,
   to the `claude-cowork-config` repo, or to chat-only delivery. A deliverable with no
   folder is a deliverable that gets lost.

## Step 1 — Confirm the opportunity name

Check whether Matt has already named it in this conversation.

- If yes: use it.
- If no: ask — *"Quel est le nom de cette opportunité ?"* (FR) or *"What is the name of
  this opportunity?"* (EN) — and wait for the answer before writing anything.

Once confirmed, display this reminder as a blockquote at the top of the response:

> 📝 **Renommer cette conversation en :** "[OpportunityName]"

## Step 2 — Resolve the slug

Format: `applications/<company>-<role-slug>/`, kebab-case, ASCII, no accents
(`mister-ia-consultant-freelance`, `masento-freelance-manufacturing`).

**List `applications/` and compare before creating anything.** If a folder for the same
company and a similar role already exists, reuse it — do not create a near-duplicate. If
two existing folders could both fit, ask Matt rather than guessing. A genuinely different
or re-posted role at the same company gets its own folder with a distinguishing suffix;
record the relationship in `notes.md`.

## Step 3 — Create the folder and the notes file

```bash
mkdir -p "$HOME/mnt/Job Applications/applications/<slug>"
```

If `notes.md` does not exist yet, create it with this skeleton and fill what is known.
Leave a field blank rather than inventing it.

```markdown
# <Opportunity name>

| | |
|---|---|
| Company | |
| Role / mission | |
| Source | LinkedIn / recruiter / job board / referral / spontaneous |
| Contacts | name, title, how reached |
| Opened | <YYYY-MM-DD> |
| Status | first contact |

## What we know

## Open questions

## Timeline
- <YYYY-MM-DD> — opened
```

State the resolved path once, in one line, then get on with the real work. No ceremony.

## Step 3b — Get the posting into `job_description.md`

**`job_description.md` is the one file every downstream skill reads** for the posting
(`job-fit-analyzer`, `resume-tailor`, `resume-redteam`, `interview-prep`, the re-post
check). The posting PDF is the archived copy of the posting as it read on the day; nothing
analyzes from it. Run this step whenever a skill needs the posting and
`applications/<slug>/job_description.md` does not exist yet.

| Input | Route |
|---|---|
| LinkedIn link, no posting PDF | **A.** Web page → `<Company>_JobPost_<Role>.pdf` → `job_description.md` |
| A posting PDF (attached in chat, or already in the folder with no `.md`) | **B.** PDF → `job_description.md` |
| Pasted text, or a non-LinkedIn URL | **C.** Write `job_description.md` directly, no PDF |

A posting PDF is `*_JobPost_*.pdf`, `job_description.pdf` in older folders, or any other
`.pdf` in the folder that is the posting rather than one of Matt's `CORNET_*` files. If one
exists, it counts as provided: use route B, never re-capture over it.

**Filename:** `<Company>_JobPost_<Role>.pdf` (e.g. `Kyndryl_JobPost_DirectorConsultPartner.pdf`).
`<Company>` is the company name without spaces or accents, `<Role>` the role title in
PascalCase without spaces, punctuation or accents.

**Tooling on Matt's machine** (all work runs there through `device_bash`, straight into the
application folder; nothing goes through the cloud workspace):

```bash
python3 -c "import weasyprint, pymupdf4llm" 2>/dev/null || pip install --user weasyprint pymupdf4llm
```

Then write the helper to `$HOME/scratch/` (outside `mnt/`, so it never lands in Matt's folders):

```bash
mkdir -p "$HOME/scratch" && cat > "$HOME/scratch/jd_capture.py" <<'PY_EOF'
"""jd_capture.py: LinkedIn "About the job" card -> posting PDF -> job_description.md

  python3 jd_capture.py pdf  <card.html> <header.json> <out.pdf>   # render the card as captured
  python3 jd_capture.py md   <posting.pdf> <out.md> [<source-url>]  # extract the PDF to markdown
  python3 jd_capture.py sum  <card.html>                            # codepoints + checksum, to match the browser
"""
import html, json, sys

def checksum(path):
    s = open(path, encoding="utf-8").read().rstrip("\n")
    return len(s), sum(ord(c) for c in s)

def render_pdf(card, header, out):
    import weasyprint
    h = json.load(open(header, encoding="utf-8"))
    e = lambda k: html.escape(h.get(k, ""))
    meta = "".join(f"<li><b>{html.escape(k)}:</b> {html.escape(v)}</li>"
                   for k, v in h.get("meta", {}).items() if v)
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>{e('title')} — {e('company')}</title>
<style>
 @page {{ size: A4; margin: 2cm; @bottom-right {{ content: counter(page) " / " counter(pages); font-size: 8pt; color: #666; }} }}
 body {{ font-family: "DejaVu Sans", sans-serif; font-size: 10pt; line-height: 1.45; color: #111; }}
 h1 {{ font-size: 16pt; margin: 0 0 .3em; }}
 h2 {{ font-size: 13pt; margin: 1.2em 0 .4em; }}
 .meta {{ list-style: none; padding: 0; margin: 0 0 1em; color: #333; font-size: 9pt; }}
 ul {{ margin: .2em 0 .6em 1.2em; padding: 0; }} li {{ margin: .15em 0; }}
 a {{ color: #0a66c2; text-decoration: none; }}
</style></head><body>
<h1>{e('title')} — {e('company')}</h1><ul class="meta">{meta}</ul>
{open(card, encoding='utf-8').read()}
</body></html>"""
    weasyprint.HTML(string=doc).write_pdf(out)

def to_md(pdf, out, url=None):
    import pymupdf4llm
    import re
    md = pymupdf4llm.to_markdown(pdf)
    md = re.sub(r"(?m)^\s*\d+ / \d+[ \t]*$", "", md)                 # page footers
    md = re.sub(r"(?m)^(#+) \*\*(.+?)\*\*[ \t]*$", r"\1 \2", md)       # "## **X**" -> "## X"
    md = re.sub(r"(?m)^(\*\*[^*\n]+:\*\*.*?)[ \t]*$",                   # header meta run -> one bullet per field
                lambda m: "\n".join("- " + f.strip() for f in re.split(r"(?=\*\*[^*]+:\*\*)", m.group(1)) if f.strip()), md)
    md = re.sub(r"[ \t]+$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    if url and url not in md:
        md = f"- **Source:** {url}\n\n" + md
    open(out, "w", encoding="utf-8").write(md.strip() + "\n")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sum":   print(*checksum(sys.argv[2]))
    elif cmd == "pdf": render_pdf(*sys.argv[2:5]); print("wrote", sys.argv[4])
    elif cmd == "md":  to_md(*sys.argv[2:5]); print("wrote", sys.argv[3])
PY_EOF
```

### Route A — LinkedIn link: PDF from the web page

**a. Load the card.** Never use server-side web fetch: the job URL and the guest endpoint
(`linkedin.com/jobs-guest/jobs/api/jobPosting/<id>`) both return empty. With Claude in
Chrome, open a new tab on `https://www.linkedin.com/jobs/view/<id>/` (a `currentJobId=<id>`
search URL resolves to the same view URL). The description is lazy-loaded and a JavaScript
scroll does **not** trigger it: use the `computer` tool's `scroll` action, 10 ticks down,
twice. If Chrome is not connected, ask Matt to attach a PDF of the posting (route B) or
paste it (route C). Never rebuild a posting from search results.

**b. Read the header.** With `get_page_text` *before* step c (step c replaces the page),
note title, company, location, work mode, contract type, posting age and "responses managed
off LinkedIn" if shown.

**c. Extract the card's own HTML.** Run this with `javascript_tool`. It finds the "About
the job" card (EN or FR heading) by its text, since LinkedIn's class names are obfuscated,
strips LinkedIn's markup down to headings, paragraphs, lists, bold, italics and links, drops
the "… more" toggle, and replaces the page with that HTML shown as text. It returns a
code-point count and checksum.

```javascript
// Run in the LinkedIn job tab AFTER scrolling (see 1a). Replaces the page with the cleaned
// "About the job" HTML as plain text, so get_page_text returns it in full.
const re = /^(About the job|À propos de l.offre d.emploi|Description du poste)$/i;
const h = [...document.querySelectorAll('h1,h2,h3,h4')].find(e => re.test(e.textContent.trim()));
if (!h) throw new Error('About the job card not rendered yet: scroll again');
let c = h; while (c && c.innerText.length < 800) c = c.parentElement;
const k = c.cloneNode(true);
k.querySelectorAll('button,svg,img,script,style,[aria-hidden="true"]').forEach(e => e.remove());
const KEEP = new Set(['H1','H2','H3','H4','P','UL','OL','LI','STRONG','B','EM','I','A','BR']);
(function clean(n) { [...n.children].forEach(ch => { clean(ch);
  if (!KEEP.has(ch.tagName)) ch.replaceWith(...ch.childNodes);
  else [...ch.attributes].forEach(a => { if (!(ch.tagName === 'A' && a.name === 'href')) ch.removeAttribute(a.name); });
}); })(k);
const html = k.innerHTML.replace(/<p>\s*<\/p>/g, '').replace(/\s*\n\s*/g, '\n')
  .replace(/(<br>|<\/p>|<\/li>|<\/h\d>|<\/ul>|<\/ol>)/g, '$1\n').trim();
const cps = [...html];
document.body.innerHTML = ''; const pre = document.createElement('pre'); pre.textContent = html; document.body.appendChild(pre);
({ codepoints: cps.length, checksum: cps.reduce((s, ch) => s + ch.codePointAt(0), 0) })
```

Then `get_page_text` returns the full HTML. (`javascript_tool` output is cut at about 1 000
characters, which is why the HTML goes through the page rather than the return value.) Only
the card is kept: "About the company", the hiring team, salary insights and similar jobs are
not the posting.

**d. Write the card and header to Matt's machine, and prove the copy is exact.** In one
`device_bash` call, write the HTML verbatim to `$HOME/scratch/jd/card.html` (quoted heredoc,
`<<'CARD_EOF'`) and the header to `$HOME/scratch/jd/header.json`:

```json
{"title": "<Role title>", "company": "<Company>",
 "meta": {"Company": "<Company>", "Location": "<location> (<work mode>, <contract type>)",
          "Source": "https://www.linkedin.com/jobs/view/<id>/",
          "Retrieved": "<YYYY-MM-DD> (<posting age; application notes if shown>)"}}
```

Run `python3 "$HOME/scratch/jd_capture.py" sum "$HOME/scratch/jd/card.html"`. Both numbers
must equal the `codepoints` and `checksum` from step c. **A mismatch means the HTML was
altered in transit: rewrite `card.html` and check again. Never render an unverified card.**
Close the tab once it matches.

**e. Render the PDF** into the application folder:

```bash
cd "$HOME/mnt/Job Applications/applications/<slug>" && \
  python3 "$HOME/scratch/jd_capture.py" pdf "$HOME/scratch/jd/card.html" "$HOME/scratch/jd/header.json" \
    "<Company>_JobPost_<Role>.pdf"
```

A4, 2 cm margins, the title as H1, the header block, then LinkedIn's own formatting of the
card, with page numbers. Checked 2026-09-22 against the Kyndryl posting: 3 pages, checksum
matched on the first try.

Then continue with route B on that PDF.

### Route B — PDF → `job_description.md`

```bash
cd "$HOME/mnt/Job Applications/applications/<slug>" && \
  python3 "$HOME/scratch/jd_capture.py" md "<posting>.pdf" job_description.md "<source URL, if known>"
```

`pymupdf4llm` rebuilds headings and bullets from the PDF; the helper removes page footers
and puts the header fields one per line. For a PDF Matt attached in chat, first save it
into the application folder under the `_JobPost_` name (copy it from the chat upload to
`/mnt/user-data/outputs/` in the cloud workspace, then write it into the folder with
`device_commit_files`), then run this. Printed browser PDFs carry a print
timestamp and the page title as their first lines; leave them, they date the capture.

### Route C — text or another website

Write `job_description.md` directly in the same shape: `# <Role> — <Company>`, the header
bullets (`Company`, `Location`, `Source`, `Retrieved`), then `## About the job` with the text
verbatim. No PDF.

### Check, deliver, log

- `job_description.md` must end on the posting's last line. If it stops at the header, the
  card had not loaded in route A: scroll and extract again. Do not ship it.
- **Verbatim, original language:** no summary, no reordering, no translation.
- Surface the PDF (routes A and B) as a clickable card with `SendUserFile` (stage it
  first), per the standing rule that the folder copy alone is not delivery.
- Add a Timeline line to `notes.md`: `<YYYY-MM-DD> — posting captured (<PDF filename>)`.
- **Re-capture of a changed posting:** never overwrite. Save
  `<Company>_JobPost_<Role>_<YYYY-MM-DD>.pdf` and `job_description_<YYYY-MM-DD>.md`, and note
  the change in `notes.md`. Downstream skills then read the most recent dated `.md`. A
  changed posting is information.
- **Older folders:** a `job_description.md` with no PDF is complete; a posting PDF with no
  `.md` gets route B the first time a skill needs it.

## Step 4 — Route

Hand off to the skill that does the work. Run it in the same turn — do not stop and ask
Matt what he wants next when the request already says.

| What Matt is asking for | Next skill |
|---|---|
| A name or a contact, no posting yet | `company-overview`, then come back |
| "Should I apply?", a posting to triage | Step 3b (posting → `job_description.md`), then `job-fit-analyzer` |
| A resume or cover letter for this role | Step 3b (posting → `job_description.md`), then `resume-tailor` then `resume-redteam` (mandatory gate) |
| A call, screen or interview to prepare | `interview-prep` |
| A message to a recruiter or hiring manager | `recruiter-followup` |
| An offer on the table | `offer-negotiator` |
| Nothing yet, just capture it | stay here; `notes.md` is the deliverable |

Whatever runs, `application-tracker` owns the row in `applications_tracker.md`. Creating
the folder is **not** logging the application — the row is the record, the folder is not.

## Step 5 — Pin the folder for the session

Every file produced for this opportunity from here on goes inside that folder, whatever
skill produces it: call preps, company overviews, tailored resumes, cover letters,
LinkedIn messages, correspondence, notes. Subfolders (`interview_prep/`,
`correspondence/`, `negotiation/`) follow the owning skill's own convention.

Per Matt's standing preference, every file is **also** surfaced as a clickable card with
`SendUserFile`. The card and the folder are both required; the card alone is not delivery.

## Non-opportunity outputs

Market sweeps, multi-company role lists, and reviews of Matt's own profile or assets go to:

```
_research/<topic>_<YYYY-MM-DD>.md
```

Create `_research/` if it does not exist. These do not open an opportunity and they do
not belong in the project root either.

## Hard rules

- **Never write an opportunity-scoped file to the project root.** If the slug is unknown,
  ask. If the folder is missing, create it. If it cannot be created, stop and say so.
- **The "project folders are kept flat, no subfolders" preference does not apply to
  Job Applications.** This project is an explicit exception: `applications/<slug>/`,
  `_assets/`, `_research/`. When the flat rule and this skill conflict, this skill wins.
- **Do not wait for a formal application.** A first call, a recruiter DM or an
  exploratory coffee opens an opportunity. The folder is cheap; the lost history is not.
- **Do not rename or move existing application folders** without asking. The tracker's
  `Folder` column points at them.
- **Every posting lands in `job_description.md` before any analysis** (Step 3b). A LinkedIn
  link becomes `<Company>_JobPost_<Role>.pdf` first, generated from the web page, and the
  `.md` is extracted from that PDF. Never analyze or tailor from a browser read that was not saved.
- **Do not stall on the routing table.** This skill is the front door, not a gate. Open
  the opportunity in one line and continue to the real work in the same turn.
