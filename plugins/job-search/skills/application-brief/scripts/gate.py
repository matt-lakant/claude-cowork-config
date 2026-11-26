#!/usr/bin/env python3
"""Check that a stage of the application pipeline left its outputs. Standard library only.

  python3 gate.py brief   <applications/<slug> folder> [--suffix _label]
  python3 gate.py draft   <applications/<slug> folder> [--suffix _label]
  python3 gate.py redteam <applications/<slug> folder> [--suffix _label]

A stage is not finished because the model believes it is: it is finished when its file holds
what the next stage needs. Each skill runs its gate as its last step, and the next skill runs
the previous gate as its first step. Exit code 1 lists what is missing; fix it and run again.

  brief    application_brief.md   written by application-brief, read by resume-tailor and cover-letter
  draft    tailoring_notes.md and the CORNET_*.docx   written by resume-tailor, read by resume-redteam
  redteam  redteam_notes.md and the *_redline*.docx   written by resume-redteam

Section headings are keys and stay in English whatever the language of the posting. --suffix reads
the files of a comparison run (application_brief_label.md and so on); the CV and the redline
must then carry the label in their file name too.
"""
import glob, os, re, sys


def sections(path):
    out, cur = {}, None
    for line in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def find(secs, key):
    for k, v in secs.items():
        if k.lower().startswith(key.lower()):
            return v
    return None


def rows(text):
    """Data rows of the first markdown table in a section, as lists of cells."""
    out = []
    for l in (text or "").splitlines():
        if l.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", l):
            out.append([c.strip() for c in l.strip().strip("|").split("|")])
    return out[1:]


def items(text):
    return [l for l in (text or "").splitlines() if re.match(r"^\s*([-*]|\d+\.)\s+\S", l)]


def is_none(text):
    return bool(re.match(r"^\s*(none|aucun|aucune|n/a)\b", (text or "").strip(), re.I))


def gate_brief(folder, suf, miss):
    p = os.path.join(folder, "application_brief%s.md" % suf)
    if not os.path.exists(p):
        miss.append("application_brief%s.md does not exist: run application-brief" % suf)
        return
    s = sections(p)
    need = ["Role", "Requirements and evidence", "Not claimable", "Top-third keywords", "First-hand facts",
            "Questions put to Matt", "Decisions", "Lessons applied", "Base file", "Form questions", "Angle"]
    for k in need:
        v = find(s, k)
        if v is None:
            miss.append("section '## %s' is missing" % k)
        elif not v:
            miss.append("section '## %s' is empty (write 'None' with the reason if there is nothing)" % k)
    role = find(s, "Role") or ""
    tag = re.search(r"Role tag:\W*(hands_on|leadership)\b", role)
    if not tag:
        miss.append("Role: no line 'Role tag: hands_on' or 'Role tag: leadership'")
    if "cv_check tags:" not in role:
        miss.append("Role: no line 'cv_check tags: ...'")
    req = rows(find(s, "Requirements and evidence"))
    if len(req) < 3:
        miss.append("Requirements and evidence: fewer than 3 requirement rows")
    for r in req:
        r = r + [""] * 7
        name, facts, question = r[1], r[4], r[6]
        coverage = r[3].lower()
        if not facts and not question and "blocked" not in coverage and "gap" not in coverage:
            miss.append("requirement '%s': no fact on record, no question to Matt, and not marked blocked or gap" % name[:50])
    if len(items(find(s, "Top-third keywords"))) < 2:
        miss.append("Top-third keywords: fewer than 2 keywords listed")
    fh = find(s, "First-hand facts")
    if tag and tag.group(1) == "hands_on" and len(items(fh)) < 2:
        miss.append("First-hand facts: a hands_on role needs at least 2, listed as bullets")
    q = find(s, "Questions put to Matt")
    if q and not rows(q) and not is_none(q):
        miss.append("Questions put to Matt: neither a table of questions nor 'None' with the reason")
    for r in rows(q):
        if len(r) < 3 or not r[2]:
            miss.append("question '%s' has no answer recorded" % (r[1][:50] if len(r) > 1 else "?"))
        elif len(r) < 4 or not re.search(r"20\d\d-\d\d-\d\d", r[3]):
            miss.append("question '%s': the answer has no date of its entry in profile_log.md (log it, then write the date)" % r[1][:50])
    dec = rows(find(s, "Decisions"))
    if not dec:
        miss.append("Decisions: no row (the role tag and the triggered rules of cv_rules.md are standing rows)")
    for r in dec:
        if len(r) < 3 or not r[2]:
            miss.append("decision '%s' does not say where it must show" % r[0][:50])
    base = find(s, "Base file") or ""
    if ".docx" not in base:
        miss.append("Base file: no .docx named")
    if not re.search(r"audit", base, re.I):
        miss.append("Base file: no audit result (cv_check on the base)")


def gate_draft(folder, suf, miss):
    gate_brief(folder, suf, miss)
    p = os.path.join(folder, "tailoring_notes%s.md" % suf)
    if not os.path.exists(p):
        miss.append("tailoring_notes%s.md does not exist: run resume-tailor" % suf)
        return
    s = sections(p)
    chk = find(s, "Check result")
    if chk is None:
        miss.append("tailoring_notes: section '## Check result' is missing")
    else:
        if not re.search(r"RESULT:\s*0 FAIL", chk):
            miss.append("Check result: no 'RESULT: 0 FAIL' line from cv_check.py (paste its last lines)")
        if not re.search(r"hands_on|leadership", chk):
            miss.append("Check result: the tags passed to cv_check.py are not shown, or carry no role tag")
    ev = find(s, "Evidence used")
    if ev is None:
        miss.append("tailoring_notes: section '## Evidence used' is missing")
    else:
        er = rows(ev)
        if not er:
            miss.append("Evidence used: no row")
        for r in er:
            if len(r) < 3 or not r[2]:
                miss.append("evidence '%s': no CV line quoted and no 'not used: reason'" % r[0][:50])
    da = find(s, "Decisions applied")
    if da is None:
        miss.append("tailoring_notes: section '## Decisions applied' is missing")
    else:
        for r in rows(da):
            if len(r) < 2 or not r[1]:
                miss.append("decision '%s': no CV line quoted" % r[0][:50])
        if not rows(da):
            miss.append("Decisions applied: no row")
    cvs = [f for f in glob.glob(os.path.join(folder, "CORNET_*.docx"))
           if not re.search(r"redline|Lettre|Letter|Cover", os.path.basename(f), re.I) and suf in os.path.basename(f)]
    if not cvs:
        miss.append("no CORNET_*%s*.docx CV in the folder" % suf)


def gate_redteam(folder, suf, miss):
    p = os.path.join(folder, "redteam_notes%s.md" % suf)
    if not os.path.exists(p):
        miss.append("redteam_notes%s.md does not exist: run resume-redteam" % suf)
        return
    s = sections(p)
    for k in ["Verdict", "Corrections applied directly", "Choices for Matt", "Questions", "First-pass count",
              "Reviewer independence", "Rejected by Matt"]:
        v = find(s, k)
        if v is None:
            miss.append("redteam_notes: section '## %s' is missing" % k)
        elif not v and k != "Rejected by Matt":
            miss.append("redteam_notes: section '## %s' is empty (write 'None' if there is nothing)" % k)
    fp = find(s, "First-pass count") or ""
    if fp and not re.search(r"\d", fp):
        miss.append("First-pass count: no number of corrections and choices")
    ri = find(s, "Reviewer independence") or ""
    if ri and not re.search(r"^\s*[-*]?\s*\**Deviations\**\s*:\s*\S", ri, re.I | re.M):
        miss.append("Reviewer independence: no 'Deviations:' line (write 'Deviations: None' when the reviewer was a new agent that read only the packet)")
    for r in rows(find(s, "Questions")):
        if len(r) < 3 or not re.search(r"asked|dropped|open", r[2], re.I):
            miss.append("question '%s': state is not 'asked', 'dropped: reason' or 'open'" % (r[1][:50] if len(r) > 1 else "?"))
    if not [f for f in glob.glob(os.path.join(folder, "CORNET_*redline*.docx")) if suf in os.path.basename(f)]:
        miss.append("no CORNET_*%s*redline*.docx in the folder" % suf)


def project_checks(folder, miss):
    """Rules that hold for the folder and the project whatever the stage."""
    for f in glob.glob(os.path.join(folder, "CORNET_*.pdf")):
        miss.append("a PDF of a CV or a letter is in the folder (%s): Matt makes his own from Word; move it to _assets/archive/" % os.path.basename(f))
    assets = os.path.join(os.path.abspath(folder), "..", "..", "_assets")
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "asset-updater", "scripts", "build_facts.py")
    if os.path.exists(os.path.join(assets, "facts", "themes.json")) and os.path.exists(script):
        import subprocess
        r = subprocess.run([sys.executable, script, assets, "--check"], capture_output=True, text=True)
        if r.returncode != 0:
            miss.append("the fact sheets are older than profile_log.md: run build_facts.py on _assets")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    suf = ""
    if "--suffix" in sys.argv:
        suf = sys.argv[sys.argv.index("--suffix") + 1]
        args.remove(suf)
    if len(args) != 2 or args[0] not in ("brief", "draft", "redteam"):
        sys.exit(__doc__)
    stage, folder = args
    miss = []
    {"brief": gate_brief, "draft": gate_draft, "redteam": gate_redteam}[stage](folder, suf, miss)
    project_checks(folder, miss)
    for m in miss:
        print("MISSING " + m)
    print("GATE %s: %s" % (stage, "PASS" if not miss else "%d item(s) missing" % len(miss)))
    sys.exit(1 if miss else 0)


if __name__ == "__main__":
    main()
