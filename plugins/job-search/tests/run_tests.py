#!/usr/bin/env python3
"""Regression tests for the job-search scripts. Needs python-docx.

  python3 plugins/job-search/tests/run_tests.py --rules "<Job Applications>/_assets/cv_rules.md"

Everything is synthetic (a fictional Jane Doe): no personal file is read except the rules file,
whose machine-readable checks are exactly what is being tested. Run it after any change to a
script or to the checks block of cv_rules.md. Exit code 1 if a test fails.

What it covers: cv_check.py on an English CV that must pass, an English CV with known violations,
a French CV that must pass (labels, "80 à 90 %", non-breaking spaces), a letter and a text file;
redline.py (tracked, untracked, cut, text split across runs, failure on a bad edit);
docx_dump.py views; to_a4.py; profile_search.py; gate.py (brief, draft, redteam, and that the
templates printed in the three SKILL.md files still carry every heading the gate reads).
"""
import argparse, json, os, subprocess, sys, tempfile
import docx
from docx.shared import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(HERE, "..", "skills")
CHK = os.path.join(SK, "resume-tailor", "scripts", "cv_check.py")
A4 = os.path.join(SK, "resume-tailor", "scripts", "to_a4.py")
SEARCH = os.path.join(SK, "application-brief", "scripts", "profile_search.py")
GATE = os.path.join(SK, "application-brief", "scripts", "gate.py")
RED = os.path.join(SK, "resume-redteam", "scripts", "redline.py")
DUMP = os.path.join(SK, "resume-redteam", "scripts", "docx_dump.py")
results = []


def run(*cmd):
    r = subprocess.run([sys.executable, *cmd], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else "\n       " + detail.strip()[:600]))


def ids(out, level):
    return {l.split("[")[1].split("]")[0] for l in out.splitlines() if l.startswith(level + " [")}


def build_cv(path, a4=True, lang="en", bad=False):
    d = docx.Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = (Emu(7560310), Emu(10692130)) if a4 else (Emu(7772400), Emu(10058400))
    d.add_paragraph("Jane Doe", style="Title")
    h = d.add_paragraph()
    h.add_run("Professional Services Leader").add_break()
    h.add_run("Implementation and master data for enterprise software").add_break()
    h.add_run("Paris | +33 1 00 00 00 00 | jane@example.com")
    d.add_heading("Profile", level=2)
    if lang == "fr":
        d.add_paragraph("Responsable de services professionnels, delivery EMEA piloté depuis Paris. Scripts SQL de contrôle "
                        "écrits personnellement ; estimations de charge et SOW rédigés personnellement. Taux d'utilisation de 80 à 90 % "
                        "sur les projets clients. 50 plateformes remplacées, 90 % mis en production à la date prévue au démarrage du projet.")
    elif bad:
        d.add_paragraph("Executive who ran a department of 110 people and a USD 40M P&L through regional directors — "
                        "certified on Snowflake. 50 replacements, 90% live on the planned date. Utilization of 80-90%.")
    else:
        d.add_paragraph("Professional services leader, with EMEA delivery run from Paris. SQL control scripts written personally; "
                        "effort estimates and SOWs written personally. Utilization of 80-90% on client projects. "
                        "50 platform replacements, 90% live on the date planned at project start.")
    d.add_heading("Areas of Expertise", level=2)
    d.add_paragraph("Master and reference data: data models, feeds, migrations")
    t = d.add_table(rows=2, cols=3)
    for i, v in enumerate(["Services", "Delivery", "Tools"]):
        t.rows[0].cells[i].text = v
        t.rows[1].cells[i].text = "x"
    d.add_heading("Professional Experience", level=2)
    label = {"en": "Client engagements:", "fr": "Exemples de projets clients :"}[lang]
    title = "Acme – Global Director, Sales, Implementation and Support (2019–2024)" if bad else \
            "Acme – Global Director, Sales Engineering, Implementation and Support (2019–2024)"
    for role, n in ((title, 2 if bad else 3), ("Acme – Global Director, Implementation and Support (2007–2018)", 2)):
        rt = d.add_table(rows=1, cols=2)
        rt.rows[0].cells[0].text = role
        rt.rows[0].cells[1].text = "Paris"
        d.add_paragraph("Ran delivery with 5 to 10 direct managers and experts")
        d.add_paragraph("Staffed client projects with internal and subcontracted consultants")
        d.add_paragraph("Context: department of up to 110 people, ~USD 40M P&L")
        d.add_paragraph(label)
        for k in range(n):
            d.add_paragraph("Client %d: programme delivered" % (k + 1))
    d.add_heading("Education", level=2)
    d.add_paragraph("Some School – Master's degree")
    d.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules", required=True, help="path of _assets/cv_rules.md in the Job Applications project")
    a = ap.parse_args()
    tmp = tempfile.mkdtemp(prefix="jobsearch_tests_")
    j = lambda n: os.path.join(tmp, n)
    profile = j("profile.md")
    open(profile, "w", encoding="utf-8").write(
        "# Profile\n\n## Current values (read before printing any figure)\n\n"
        "| Fact | Print as | Never print | Since | Log entry |\n|---|---|---|---|---|\n"
        "| Margin | from 27% to 32% over 24 to 30 months | `to 32% over 3 years` | 2026-11-10 | x |\n\n"
        "## Experience\n- Built things\n\n## Confirmed details from tailoring Q&A (append-only log)\n\n"
        "- **2026-09-01 — SOW:** validated statements of work\n"
        "- **2026-10-23 : Tailoring X :** a produit des **estimations d'effort et des SOW** lui-même ; remplace l'entrée précédente\n"
        "- **2026-08-01 — Other:** nothing relevant\n")
    tags = "non_sales,ps_role,hands_on"
    kw = ["--top-keywords", "EMEA;master data", "--hands-on", "SQL control scripts written personally;SOWs written personally"]

    # --- cv_check
    build_cv(j("CORNET_good_en.docx"))
    rc, out = run(CHK, j("CORNET_good_en.docx"), "--rules", a.rules, "--profile", profile, "--tags", tags, *kw)
    check("cv_check: clean English CV passes", rc == 0 and not ids(out, "FAIL"), out)

    build_cv(j("bad_en.docx"), a4=False, bad=True)
    rc, out = run(CHK, j("bad_en.docx"), "--rules", a.rules, "--profile", profile, "--tags", tags, *kw)
    want = {"R1-filename", "R15-page", "R3-title", "R6-ninety", "R11-emdash", "R14-ceilings", "R18-scale-top",
            "R5-engagements", "R19-hands-on", "top-keywords"}
    got = ids(out, "FAIL")
    check("cv_check: every planted violation is caught", rc == 1 and want <= got, "missing: %s\n%s" % (sorted(want - got), out))
    check("cv_check: 80-90% does not trigger the 90% rule on its own", out.count("[R6-ninety]") == 1, out)

    build_cv(j("CORNET_good_fr.docx"), lang="fr")
    rc, out = run(CHK, j("CORNET_good_fr.docx"), "--rules", a.rules, "--profile", profile, "--tags", tags,
                  "--top-keywords", "EMEA", "--hands-on", "Scripts SQL de contrôle écrits personnellement;SOW rédigés personnellement")
    check("cv_check: clean French CV passes (label, 80 à 90 %, non-breaking spaces)", rc == 0 and not ids(out, "FAIL"), out)

    rc, out = run(CHK, j("CORNET_good_en.docx"), "--rules", a.rules, "--tags", "non_sales")
    check("cv_check: missing role tag is reported", "[level]" in out, out)

    d = docx.Document(); s = d.sections[0]; s.page_width, s.page_height = Emu(7560310), Emu(10692130)
    d.add_paragraph("Dear Sam,"); d.add_paragraph("I have not delivered on Snowflake. I wrote the SQL controls myself.")
    d.save(j("CORNET_letter.docx"))
    rc, out = run(CHK, j("CORNET_letter.docx"), "--rules", a.rules, "--kind", "letter", "--tags", "non_sales,hands_on")
    check("cv_check: a ceiling word in a letter is a WARN, not a FAIL", rc == 0 and "R14-ceilings" in ids(out, "WARN"), out)

    open(j("answers.md"), "w", encoding="utf-8").write("Margin went from 27% to 32% over 3 years.\n")
    rc, out = run(CHK, j("answers.md"), "--rules", a.rules, "--profile", profile, "--kind", "text", "--tags", "hands_on")
    check("cv_check: superseded figure caught in a text file", rc == 1 and "superseded" in ids(out, "FAIL"), out)

    # --- to_a4
    rc, out = run(A4, j("bad_en.docx"), j("bad_a4.docx"))
    sec = docx.Document(j("bad_a4.docx")).sections[0]
    check("to_a4: Letter becomes A4", abs(sec.page_width.twips - 11906) <= 1 and abs(sec.page_height.twips - 16838) <= 1, out)
    rc, out = run(A4, j("bad_a4.docx"), j("bad_a4_again.docx"))
    check("to_a4: A4 input is left unchanged", "already A4" in out, out)

    # --- redline + docx_dump
    d = docx.Document(); p = d.add_paragraph(); p.add_run("Delivered thirty "); p.add_run("platform"); p.add_run(" replacements on time")
    d.add_paragraph("Margin raised over 3 years"); d.add_paragraph("A line to cut entirely"); d.add_paragraph("Another line to drop silently")
    d.save(j("draft.docx"))
    json.dump([{"old": "thirty platform replacements", "new": "30 platform replacements"},
               {"old": "over 3 years", "new": "over 24 to 30 months", "track": False},
               {"cut": "A line to cut"}, {"cut": "Another line to drop", "track": False}], open(j("edits.json"), "w"))
    rc, out = run(RED, j("draft.docx"), j("redline.docx"), j("edits.json"))
    check("redline: all edits applied, 2 tracked and 2 direct", rc == 0 and "4 of 4" in out and "2 corrections written directly" in out, out)
    _, marked = run(DUMP, j("redline.docx"), "--view", "marked")
    _, accepted = run(DUMP, j("redline.docx"))
    _, original = run(DUMP, j("redline.docx"), "--view", "original")
    check("redline: tracked change spans three runs", "[+30 platform replacements+]" in marked and "[-" in marked, marked)
    check("redline: correction is not tracked", "over 24 to 30 months" in marked and "[+over 24" not in marked, marked)
    check("docx_dump: accepted view", "30 platform replacements" in accepted and "A line to cut" not in accepted and "drop silently" not in accepted, accepted)
    check("docx_dump: original view keeps the tracked text", "thirty platform replacements" in original and "A line to cut" in original, original)
    json.dump([{"old": "text that is not in the document", "new": "x"}], open(j("bad.json"), "w"))
    rc, out = run(RED, j("draft.docx"), j("redline2.docx"), j("bad.json"))
    check("redline: an edit that cannot be applied fails the run", rc == 1 and "NOT APPLIED" in out, out)

    # --- profile_search
    rc, out = run(SEARCH, profile, "SOW;statement of work;estimations? d'effort")
    first = [l for l in out.splitlines() if l.startswith("--- line")]
    check("profile_search: finds entries, best match first, flags a superseding entry",
          len(first) == 2 and "2026-10-23" in first[0] and "MAY SUPERSEDE" in first[0], out)

    # --- gate
    g = os.path.join(tmp, "acme-ps-manager")
    os.makedirs(g)
    gp = lambda n: os.path.join(g, n)
    brief = """# Application brief: Acme, PS Manager

## Role
- Role tag: hands_on (\"you will run the projects yourself\")
- cv_check tags: non_sales, ps_role, hands_on
- Language: English

## Requirements and evidence
| # | Requirement | Hard / nice | Coverage | Strongest facts on record (entry date) | First-hand | Open question |
|---|---|---|---|---|---|---|
| 1 | Run delivery | hard | strong | 50 platform replacements (2026-10-15) | yes | |
| 2 | Write SOWs | hard | strong | SOWs written personally (2026-10-23) | yes | |
| 3 | Snowflake certification | nice | blocked | | no | |

## Not claimable
- Snowflake certification: ceiling

## Top-third keywords
- EMEA
- master data

## ATS keywords
EMEA, master data, SOW

## First-hand facts
- SQL control scripts | fragment for cv_check: "SQL control scripts written personally"
- SOWs | fragment for cv_check: "SOWs written personally"

## Questions put to Matt
None: every hard requirement has a fact on record.

## Decisions
| Decision | Source | Where it must show |
|---|---|---|
| Role is hands_on | R18 | header, profile |

## Lessons applied
None: the lessons file has no line for this role family.

## Base file
- File: _assets/master_resume.docx
- Audit: RESULT: 0 FAIL

## Form questions
None: the posting asks none.

## Angle
Delivery lead who writes the SOWs himself.
"""
    open(gp("application_brief.md"), "w", encoding="utf-8").write(brief)
    rc, out = run(GATE, "brief", g)
    check("gate brief: a complete brief passes", rc == 0 and "GATE brief: PASS" in out, out)
    bad_brief = brief.replace("- Role tag: hands_on", "- Role: manager").replace("| 2 | Write SOWs | hard | strong | SOWs written personally (2026-10-23) | yes | |", "| 2 | Write SOWs | hard | partial | | no | |").replace("## Angle\nDelivery lead who writes the SOWs himself.\n", "")
    os.makedirs(gp("bad"))
    open(os.path.join(gp("bad"), "application_brief.md"), "w", encoding="utf-8").write(bad_brief)
    rc, out = run(GATE, "brief", gp("bad"))
    check("gate brief: missing role tag, missing section and a requirement with neither fact nor question fail",
          rc == 1 and "Role tag" in out and "'## Angle' is missing" in out and "requirement 'Write SOWs'" in out, out)
    rc, out = run(GATE, "draft", g)
    check("gate draft: fails before resume-tailor has written its memo", rc == 1 and "tailoring_notes.md does not exist" in out, out)
    open(gp("tailoring_notes.md"), "w", encoding="utf-8").write("""# Tailoring notes

## Check result
cv_check.py --tags non_sales,ps_role,hands_on
RESULT: 0 FAIL, 1 WARN

## Evidence used
| Requirement | Fact on record | CV line |
|---|---|---|
| Run delivery | 50 platform replacements | "50 platform replacements, 90% live on the date planned at project start" |
| Write SOWs | SOWs written personally | not used: reason given |

## Decisions applied
| Decision | CV line that applies it |
|---|---|
| Role is hands_on | "Ran delivery with 5 to 10 direct managers and experts" |
""")
    build_cv(gp("CORNET_Acme_PS-Manager_2026-11-17.docx"))
    rc, out = run(GATE, "draft", g)
    check("gate draft: brief, memo and CV present pass", rc == 0 and "GATE draft: PASS" in out, out)
    open(gp("redteam_notes.md"), "w", encoding="utf-8").write("""# Red-team notes

## Verdict
Borderline.

## Corrections applied directly
None.

## Choices for Matt
| # | Tracked change | Severity | Trade-off | Cause |
|---|---|---|---|---|
| 1 | cut line | Med | shorter | F |

## Questions
| # | Question | State | Answer or reason |
|---|---|---|---|
| 1 | Team size in EMEA? | pending | |

## First-pass count
0 corrections, 1 choice (F: 1)

## Rejected by Matt
""")
    rc, out = run(GATE, "redteam", g)
    check("gate redteam: a question with no state and a missing redline fail",
          rc == 1 and "state is not" in out and "redline" in out, out)
    t = open(gp("redteam_notes.md"), encoding="utf-8").read().replace("| pending | |", "| dropped: answered in the log (2026-10-15) | |")
    open(gp("redteam_notes.md"), "w", encoding="utf-8").write(t)
    build_cv(gp("CORNET_Acme_PS-Manager_2026-11-17_redline.docx"))
    rc, out = run(GATE, "redteam", g)
    check("gate redteam: complete memo and redline pass", rc == 0 and "GATE redteam: PASS" in out, out)

    # --- the templates printed in the skills carry every heading the gate reads
    def heads(skill):
        txt = open(os.path.join(SK, skill, "SKILL.md"), encoding="utf-8").read()
        return {l[3:].split("(key)")[0].strip() for l in txt.splitlines() if l.startswith("## ")}
    want = {"application-brief": ["Role", "Requirements and evidence", "Not claimable", "Top-third keywords", "First-hand facts",
                                  "Questions put to Matt", "Decisions", "Lessons applied", "Base file", "Form questions", "Angle"],
            "resume-tailor": ["Check result", "Evidence used", "Decisions applied"],
            "resume-redteam": ["Verdict", "Corrections applied directly", "Choices for Matt", "Questions", "First-pass count", "Rejected by Matt"]}
    for skill, keys in want.items():
        missing = [k for k in keys if k not in heads(skill)]
        check("template of %s has every heading the gate reads" % skill, not missing, "missing: %s" % missing)
    for skill in sorted(os.listdir(SK)):
        txt = open(os.path.join(SK, skill, "SKILL.md"), encoding="utf-8").read()
        check("%s opens on a step map or a mode map" % skill, "## Step map" in txt[:1800] or "## Mode map" in txt[:1800])
        check("%s has no stale script path" % skill,
              "resume-tailor skill dir>/scripts/profile_search" not in txt and "resume-tailor/scripts/profile_search" not in txt)

    failed = [n for n, ok in results if not ok]
    print("\n%d tests, %d failed" % (len(results), len(failed)))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
