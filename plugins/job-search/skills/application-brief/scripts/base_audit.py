#!/usr/bin/env python3
"""List the CVs that can serve as a base, with their state against today's rules. Standard library
only (it calls cv_check.py and docx_dump.py, which ship with the plugin).

  python3 base_audit.py <project root> [--write] [--since YYYY-MM-DD]

A base is the .docx that resume-tailor edits in place. It is layout and phrasing Matt validated,
so the candidates are the CVs he returned himself (file name containing "final", letters excluded),
plus _assets/master_resume.docx as the fallback. For each one the script reports the language, the
word count, and the number of FAIL lines of cv_check.py when the CV is read as a leadership CV and
as a hands_on CV, with the rule identifiers. Page size (R15) is listed apart: it is fixed by
to_a4.py on the working copy and says nothing about the content. The hands_on count never includes
R19 (first-hand facts above the matrix), which needs the posting.

Without --write the table is printed. With --write it is saved as <project>/_assets/cv_bases.md,
below a section "Notes" that is kept as it is from one run to the next (it is where Matt or a
skill records which base to prefer for a role family). Run it after each CV Matt returns.
"""
import collections, datetime, glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "..", "..", "resume-tailor", "scripts", "cv_check.py")
DUMP = os.path.join(HERE, "..", "..", "resume-redteam", "scripts", "docx_dump.py")


def run(*cmd):
    return subprocess.run([sys.executable, *cmd], capture_output=True, text=True).stdout


def audit(path, rules, profile):
    txt = run(DUMP, path)
    fr = len(re.findall(r"\b(les|des|une|et|avec|pour)\b", txt))
    en = len(re.findall(r"\b(the|and|with|for|of)\b", txt))
    out = {}
    words = "?"
    for tag in ("leadership", "hands_on"):
        o = run(CHK, path, "--rules", rules, "--profile", profile, "--tags", tag)
        ids = [l.split("[")[1].split("]")[0] for l in o.splitlines() if l.startswith("FAIL [")]
        ids = [i for i in ids if i not in ("R1-filename", "R19-hands-on")]
        out[tag] = collections.Counter(ids)
        m = re.search(r"words=(\d+)", o)
        words = m.group(1) if m else words
    a4 = "R15-page" not in out["leadership"]
    for t in out:
        out[t].pop("R15-page", None)
    return ("FR" if fr > en else "EN"), words, a4, out


def fmt(c):
    return "0" if not c else "%d (%s)" % (sum(c.values()), ", ".join("%s×%d" % (k, v) if v > 1 else k for k, v in sorted(c.items())))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    since = ""
    if "--since" in sys.argv:
        since = sys.argv[sys.argv.index("--since") + 1]
        args.remove(since)
    if len(args) != 1:
        sys.exit(__doc__)
    root = args[0]
    rules = os.path.join(root, "_assets", "cv_rules.md")
    profile = os.path.join(root, "_assets", "candidate_profile.md")
    files = [f for f in glob.glob(os.path.join(root, "applications", "*", "*.docx"))
             if re.search(r"final", os.path.basename(f), re.I) and not re.search(r"lettre|letter|cover|redline", os.path.basename(f), re.I)]
    rows = []
    for f in files:
        m = re.search(r"(20\d\d-\d\d-\d\d)", os.path.basename(f))
        date = m.group(1) if m else ""
        if since and date < since:
            continue
        lang, words, a4, res = audit(f, rules, profile)
        rows.append((date, lang, os.path.relpath(f, root).replace(os.sep, "/"), words, a4, res))
    rows.sort(key=lambda r: r[0], reverse=True)
    master = os.path.join(root, "_assets", "master_resume.docx")
    if os.path.exists(master):
        lang, words, a4, res = audit(master, rules, profile)
        rows.append(("fallback", lang, "_assets/master_resume.docx", words, a4, res))
    lines = ["| Date | Lang | File | Words | A4 | FAIL as leadership | FAIL as hands_on |", "|---|---|---|---|---|---|---|"]
    for date, lang, rel, words, a4, res in rows:
        lines.append("| %s | %s | `%s` | %s | %s | %s | %s |" % (date, lang, rel, words, "yes" if a4 else "no", fmt(res["leadership"]), fmt(res["hands_on"])))
    table = "\n".join(lines)
    if "--write" not in sys.argv:
        print(table)
        return
    out = os.path.join(root, "_assets", "cv_bases.md")
    notes = "## Notes\n\nNone yet.\n"
    if os.path.exists(out):
        old = open(out, encoding="utf-8").read()
        if "## Notes" in old:
            notes = old[old.index("## Notes"):old.index("## Candidates")] if "## Candidates" in old else notes
    head = ("# Base CVs\n\n"
            "> The CVs Matt returned himself, with their state against today's rules. `application-brief` Step 7 picks the base here: the most recent "
            "file in the posting's language, for the nearest role family and the same role tag, with the fewest FAIL lines. Every FAIL is a line "
            "`resume-tailor` rewrites. A base gives layout and phrasing, never figures: those come from the Current values table.\n"
            "> The table is generated by `base_audit.py` (last run %s); the Notes section is kept by hand and survives each run.\n\n" % datetime.date.today().isoformat())
    open(out, "w", encoding="utf-8").write(head + notes.rstrip("\n") + "\n\n## Candidates\n\n" + table + "\n")
    print("BASES: %d candidates written to %s" % (len(rows), out))


if __name__ == "__main__":
    main()
