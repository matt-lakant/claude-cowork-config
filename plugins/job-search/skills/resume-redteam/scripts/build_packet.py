#!/usr/bin/env python3
"""Build the red-team reviewer's packet: a folder of primary sources, copied by this script.

  python3 build_packet.py --kind cv --app <applications/<slug>> --assets <project>/_assets \
      --identity "<vault>/Notes/Matt Cornet.md" --doc <CV .docx> --out <new folder>
  python3 build_packet.py --kind letter ... --doc <letter .docx> --cv <final CV .docx> \
      --extra voice=<file> --extra motivations=<file> [--extra forms=<file>] --out <new folder>

Why a script: the reviewer must judge the document without the drafter's reasoning. A packet
assembled by hand is assembled by the context that wrote the document, and what it pastes,
trims or summarizes carries its angle. Here every file is copied or cut by rule, so the only
things the drafting context adds are the paths it passes. Standard library only.

What goes in the packet (and nothing else):
  00_READ_ME.md             what each file is; the reviewer starts here
  01_job_description.md     most recent job_description*.md, minus any fit or coverage section
  02_company_overview.md    minus "Positioning implications for Matt" (drafting advice)
  03_cv.txt                 the CV as text (docx_dump.py, tracked changes accepted)
  04_letter.txt             the letter as text (--kind letter)
  05_truth_ceilings.md      "Framing guardrails" and "Technology and scope ceilings" of the identity note
  06_current_values.md      the Current values table of candidate_profile.md
  07_cv_rules.md            Part 1 of cv_rules.md (the whole file if no "Part 1" heading is found)
  record/                   candidate_profile.md, profile_log.md, facts/ (copies, for grep)
  extra_<name>.<ext>        --extra files, copied byte for byte

--out must be a folder that does not exist yet (or is empty) and sits OUTSIDE the project
folder: the reviewer is never given the project path. The manifest (packet file, source, size,
sha256) is printed and saved beside the packet as <out>.manifest.md, not inside it, because the
sources are paths the reviewer must not learn. Paste it into the red-team notes.

Exit code 1 names what is missing. A packet is never written partially: fix and run again.
"""
import argparse, glob, hashlib, os, re, shutil, subprocess, sys

FORBIDDEN = ("application_brief", "tailoring_notes", "fit_report", "cover_letter_notes",
             "redteam_notes", "cl_redteam_notes", "notes")
JD_STRIP = r"^(requirement coverage|coverage matrix|fit (matrix|score|analysis|report|summary|check)|fit$)"


def read(p):
    return open(p, encoding="utf-8").read()


def heading(line):
    """(level, title) for a markdown heading or a bold label on its own line; else None."""
    m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
    if m:
        return len(m.group(1)), m.group(2).strip()
    m = re.match(r"^\s*(?:[-*]\s+)?\*\*(.+?)\*\*\s*:?\s*$", line) or re.match(r"^\s*(?:[-*]\s+)?\*\*(.+?):\*\*", line)
    if m:
        return 7, m.group(1).strip().rstrip(":")
    return None


def span(lines, pattern):
    """(start, end) of the first section whose title matches pattern, or None."""
    for i, l in enumerate(lines):
        h = heading(l)
        if h and re.search(pattern, h[1], re.I):
            for j in range(i + 1, len(lines)):
                g = heading(lines[j])
                if g and (g[0] <= h[0] or (h[0] == 7 and g[0] <= 7)):
                    return i, j
            return i, len(lines)
    return None


def cut(text, pattern):
    """Text without every section matching pattern, and the titles removed."""
    lines, gone = text.splitlines(), []
    while True:
        s = span(lines, pattern)
        if not s:
            break
        gone.append(heading(lines[s[0]])[1])
        del lines[s[0]:s[1]]
    return "\n".join(lines).rstrip() + "\n", gone


def take(text, pattern):
    lines = text.splitlines()
    s = span(lines, pattern)
    return None if not s else "\n".join(lines[s[0]:s[1]]).rstrip() + "\n"


def latest_jd(app):
    dated = sorted(glob.glob(os.path.join(app, "job_description_*.md")))
    plain = os.path.join(app, "job_description.md")
    return dated[-1] if dated else (plain if os.path.exists(plain) else None)


def dump(docx_path):
    here = os.path.dirname(os.path.abspath(__file__))
    r = subprocess.run([sys.executable, os.path.join(here, "docx_dump.py"), docx_path], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 and r.stdout.strip() else None


def inside(path, folder):
    path, folder = os.path.realpath(path), os.path.realpath(folder)
    return path == folder or path.startswith(folder + os.sep)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", required=True, choices=["cv", "letter"])
    ap.add_argument("--app", required=True)
    ap.add_argument("--assets", required=True)
    ap.add_argument("--identity", required=True)
    ap.add_argument("--doc", required=True)
    ap.add_argument("--cv")
    ap.add_argument("--extra", action="append", default=[])
    ap.add_argument("--strip", action="append", default=[], help="one more job-description heading to remove")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    miss, notes, files = [], [], []      # files: (packet name, source, text or None for a copy)

    project = os.path.dirname(os.path.realpath(a.assets))
    if inside(a.out, project) or inside(a.out, a.app):
        miss.append("--out is inside the project folder: the packet goes in the session's scratch space")
    if os.path.isdir(a.out) and os.listdir(a.out):
        miss.append("--out exists and is not empty: give a new folder, never reuse a packet")

    jd = latest_jd(a.app)
    if not jd:
        miss.append("no job_description*.md in %s: opportunity-intake Step 3b creates it" % a.app)
    else:
        text, gone = cut(read(jd), "|".join([JD_STRIP] + [re.escape(s) for s in a.strip]))
        if gone:
            notes.append("job description: removed section(s) %s" % ", ".join("'%s'" % g for g in gone))
        notes.append("job description headings kept: %s" % (", ".join(h[1] for h in map(heading, text.splitlines()) if h and h[0] < 7) or "none"))
        files.append(("01_job_description.md", jd, text))

    co = os.path.join(a.app, "company_overview.md")
    if not os.path.exists(co):
        miss.append("company_overview.md is missing: run company-overview")
    else:
        text, gone = cut(read(co), r"^positioning implications")
        if not gone:
            notes.append("company overview: no 'Positioning implications' section found, file copied whole. Check it holds no drafting advice")
        files.append(("02_company_overview.md", co, text))

    cv = a.doc if a.kind == "cv" else a.cv
    if a.kind == "letter" and not a.cv:
        miss.append("--cv is required with --kind letter: the final CV Matt returned")
    for name, path in (("03_cv.txt", cv),) + ((("04_letter.txt", a.doc),) if a.kind == "letter" else ()):
        if not path:
            continue
        if not os.path.exists(path):
            miss.append("%s does not exist" % path)
            continue
        text = dump(path)
        if not text:
            miss.append("docx_dump.py printed nothing for %s" % path)
        else:
            files.append((name, path, text))

    if not os.path.exists(a.identity):
        miss.append("identity note not found: %s (connect the vault; no fallback)" % a.identity)
    else:
        idt = read(a.identity)
        ceil = take(idt, r"^technology and scope ceilings")
        guard = take(idt, r"^framing guardrails")
        if not ceil:
            miss.append("no 'Technology and scope ceilings' section in the identity note")
        else:
            if not guard:
                notes.append("identity note: no 'Framing guardrails' section, ceilings only")
            files.append(("05_truth_ceilings.md", a.identity, (guard or "") + ("\n" if guard else "") + ceil))

    prof = os.path.join(a.assets, "candidate_profile.md")
    if not os.path.exists(prof):
        miss.append("candidate_profile.md is missing from %s" % a.assets)
    else:
        cur = take(read(prof), r"^current values")
        if not cur:
            miss.append("no '## Current values' section in candidate_profile.md")
        else:
            files.append(("06_current_values.md", prof, cur))
        files.append((os.path.join("record", "candidate_profile.md"), prof, None))
    log = os.path.join(a.assets, "profile_log.md")
    if os.path.exists(log):
        files.append((os.path.join("record", "profile_log.md"), log, None))
    else:
        miss.append("profile_log.md is missing from %s" % a.assets)
    for f in sorted(glob.glob(os.path.join(a.assets, "facts", "*.md"))):
        files.append((os.path.join("record", "facts", os.path.basename(f)), f, None))

    rules = os.path.join(a.assets, "cv_rules.md")
    if not os.path.exists(rules):
        miss.append("cv_rules.md is missing from %s" % a.assets)
    else:
        p1 = take(read(rules), r"\bpart\s*1\b")
        if not p1:
            notes.append("cv_rules.md: no 'Part 1' heading, file copied whole")
        files.append(("07_cv_rules.md", rules, p1 or read(rules)))

    extras = []
    for e in a.extra:
        name, _, path = e.partition("=")
        base = os.path.splitext(os.path.basename(path))[0].lower()
        if not name or not path or not re.match(r"^[a-z0-9_]+$", name):
            miss.append("--extra %s: write it as name=path, name in lowercase letters, digits and _" % e)
        elif not os.path.exists(path):
            miss.append("--extra %s: file not found" % e)
        elif any(base == f or base.startswith(f + "_") for f in FORBIDDEN):
            miss.append("--extra %s: %s is a drafting or review note and never goes to the reviewer" % (e, os.path.basename(path)))
        else:
            extras.append(("extra_%s%s" % (name, os.path.splitext(path)[1] or ".md"), path, None))
    files += extras

    if miss:
        print("PACKET: NOT BUILT")
        for m in miss:
            print(" - " + m)
        sys.exit(1)

    os.makedirs(os.path.join(a.out, "record", "facts"), exist_ok=True)
    doc_name = "04_letter.txt" if a.kind == "letter" else "03_cv.txt"
    about = {
        "01_job_description.md": "the posting",
        "02_company_overview.md": "research on the company",
        "03_cv.txt": "the CV under review" if a.kind == "cv" else "the final CV, as sent",
        "04_letter.txt": "the cover letter under review",
        "05_truth_ceilings.md": "the hard limit of what the candidate may claim",
        "06_current_values.md": "the current wording of each figure",
        "07_cv_rules.md": "the candidate's standing rules: constraints, do not propose against them",
    }
    readme = ["# Reviewer's packet", "",
              "Document under review: `%s`. Read every numbered file from first line to last." % doc_name,
              "`record/` is the candidate's record: read `record/candidate_profile.md` in full, then grep",
              "`record/profile_log.md` (dated, append-only: the LATEST entry wins) or read the matching sheet",
              "in `record/facts/` for each claim you check. Cite the date and line of each entry.", "",
              "Read nothing outside this folder, and write nothing.", "",
              "| File | What it is |", "|---|---|"]
    rows = []
    for name, src, text in files:
        dst = os.path.join(a.out, name)
        if text is None:
            shutil.copyfile(src, dst)
        else:
            open(dst, "w", encoding="utf-8").write(text)
        b = open(dst, "rb").read()
        rows.append((name.replace(os.sep, "/"), src, len(b), hashlib.sha256(b).hexdigest()[:12]))
        if not name.startswith("record"):
            label = about.get(name) or "%s, copied as is" % name[6:].rsplit(".", 1)[0].replace("_", " ")
            readme.append("| `%s` | %s |" % (name, label))
    readme.append("| `record/` | candidate_profile.md, profile_log.md, facts/ |")
    open(os.path.join(a.out, "00_READ_ME.md"), "w", encoding="utf-8").write("\n".join(readme) + "\n")

    man = ["| Packet file | Source | Bytes | sha256 |", "|---|---|---|---|"]
    man += ["| %s | %s | %d | %s |" % r for r in rows]
    man += ["", "Notes:"] + [" - " + n for n in (notes or ["none"])]
    out = os.path.realpath(a.out)
    open(out.rstrip(os.sep) + ".manifest.md", "w", encoding="utf-8").write("\n".join(man) + "\n")
    print("PACKET: BUILT  %s  (%d files)" % (out, len(rows) + 1))
    print("\n".join(man))


if __name__ == "__main__":
    main()
