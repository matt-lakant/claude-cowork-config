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

### No local installs (Matt's rule, 2026-09-22)

**Nothing is ever installed on Matt's machine for this step, and no `pip install` runs
there.** Rendering and conversion happen in the **cloud workspace**, with the tools it ships
with: Playwright + Chromium (`/opt/pw-browsers`) and `pdfplumber`. The files then go into the
application folder with `device_commit_files`. If either tool is missing from the cloud
workspace, stop and tell Matt; do not install anything, anywhere, to work around it.

The helper is `scripts/jd_capture.py` in this skill's directory (the base directory shown
when the skill loads; if unknown, `find ~/.claude -path '*opportunity-intake/scripts/jd_capture.py'`).
Below, `$JD` is that path and `$W` a working folder in the scratchpad, e.g. `$W=<scratchpad>/jd/<slug>`.

```text
python3 $JD sum <card.html>                           # code points + checksum, to match the browser
python3 $JD pdf <card.html> <header.json> <out.pdf>   # Chromium renders the card to A4
python3 $JD md  <posting.pdf> <out.md> [<url>]        # pdfplumber rebuilds headings, bullets, paragraphs
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

**d. Write the card and header in the cloud workspace, and prove the copy is exact.** With
`Write`, save the HTML verbatim to `$W/card.html` and the header to `$W/header.json`:

```json
{"title": "<Role title>", "company": "<Company>",
 "meta": {"Company": "<Company>", "Location": "<location> (<work mode>, <contract type>)",
          "Source": "https://www.linkedin.com/jobs/view/<id>/",
          "Retrieved": "<YYYY-MM-DD> (<posting age; application notes if shown>)"}}
```

Run `python3 $JD sum $W/card.html`. Both numbers must equal the `codepoints` and `checksum`
from step c. **A mismatch means the HTML was altered in transit: rewrite `card.html` and
check again. Never render an unverified card.** Close the tab once it matches.

**e. Render, then extract:**

```bash
python3 $JD pdf "$W/card.html" "$W/header.json" "$W/<Company>_JobPost_<Role>.pdf"
python3 $JD md  "$W/<Company>_JobPost_<Role>.pdf" "$W/job_description.md" "<LinkedIn URL>"
```

A4, 2 cm margins, the title as H1, the header block, then LinkedIn's own formatting of the
card, with page numbers. Checked 2026-09-22 against the Kyndryl posting: checksum matched
on the first try, 3 pages, clean markdown. Then deliver (below).

### Route B — PDF → `job_description.md`

- **Attached in chat:** it is already in the cloud workspace uploads. Copy it to
  `$W/<Company>_JobPost_<Role>.pdf`.
- **Already in the application folder with no `.md`:** stage it with `device_stage_files`
  (the conversion tool exists only in the cloud workspace, which is a valid reason to stage).

Then `python3 $JD md "<the PDF>" "$W/job_description.md" "<source URL, if known>"`. Printed
browser PDFs carry a print timestamp and the page title as their first line; leave it, it
dates the capture. A scanned PDF with no text layer fails with a message: ask Matt to paste
the posting instead.

### Route C — text or another website

Write `job_description.md` directly into the folder with `device_bash` (no tool needed): `#
<Role> — <Company>`, the header bullets (`Company`, `Location`, `Source`, `Retrieved`), then
`## About the job` with the text verbatim. No PDF.

### Deliver, verify, log

1. Copy the new files (the PDF for routes A and B-attached, and `job_description.md`) to
   `/mnt/user-data/outputs/<slug>/` and send each with `SendUserFile`: that is the
   clickable card Matt's standing rule requires, and it returns the `file_uuid`.
2. Write each into `applications/<slug>/` with `device_commit_files` using that `fileUuid`.
3. **Verify on Matt's machine:** `md5sum` each file in the folder with `device_bash` and
   compare with the cloud copy. `device_commit_files` has reported success for writes that
   never landed (2026-09-10); a mismatch means commit again.
4. `job_description.md` must end on the posting's last line. If it stops at the header, the
   card had not loaded in route A: scroll and extract again. Do not ship it.
5. **Verbatim, original language:** no summary, no reordering, no translation.
6. Add a Timeline line to `notes.md`: `<YYYY-MM-DD> — posting captured (<PDF filename>)`.

**Re-capture of a changed posting:** never overwrite. Save
`<Company>_JobPost_<Role>_<YYYY-MM-DD>.pdf` and `job_description_<YYYY-MM-DD>.md`, and note the
change in `notes.md`. Downstream skills then read the most recent dated `.md`. A changed
posting is information.

**Older folders:** a `job_description.md` with no PDF is complete; a posting PDF with no
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
- **Never install anything on Matt's machine** for the posting capture. Rendering and
  conversion run in the cloud workspace with its preinstalled tools only.
- **Do not stall on the routing table.** This skill is the front door, not a gate. Open
  the opportunity in one line and continue to the real work in the same turn.
