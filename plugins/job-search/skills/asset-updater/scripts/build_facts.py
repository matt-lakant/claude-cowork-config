#!/usr/bin/env python3
"""Build the fact sheets by theme from the append-only log. Standard library only.

  python3 build_facts.py <_assets folder> [--check]

Reads   <_assets>/profile_log.md         the dated log, one entry per "- **YYYY-MM-DD ..." line
        <_assets>/facts/themes.json      the themes: name, description, and the patterns that sort
                                         an item into them (personal data: it lives in the project,
                                         never in the plugin)
Writes  <_assets>/facts/<theme>.md       one sheet per theme
        <_assets>/facts/INDEX.md         the list of sheets with their counts

The sheets are views, not a second store. Nothing is typed into them: a fact is added or corrected
in the log, then this script is run again. An entry that bundles several numbered points, "(1) ...
(2) ...", is split into one line per point, each carrying the date and title of its entry.

An item goes to the first theme, in the order of themes.json, whose "title" pattern matches the
entry title or whose "text" pattern matches the item. Items matching nothing go to "unsorted".
An entry whose title matches "bundle_title" (the answers given for one application, which cover
many subjects) is sorted on the text of each point only, unless the theme sets "title_always".

Status. An entry marked as replaced or corrected (an inline "⛔", or a closing "*(⛔ STATUS ...)*"
note) is not silently dropped: its items go to the section "Replaced or corrected" at the bottom
of the sheet, with the note, so a reader sees both the old statement and what replaced it. When
the note names "point (k)", only that point is moved.

--check  writes nothing; exits 1 if the sheets on disk differ from what the log would produce
         (the log was edited and the sheets were not rebuilt).
"""
import json, os, re, sys

ENTRY = re.compile(r"^(?:- )?\*\*(\d{4}-\d\d-\d\d)")
STATUS = re.compile(r"\*\(⛔ STATUS [^:]*: (.*?)\)\*\s*$", re.S)


def entries(path):
    out, cur, started = [], None, False
    for n, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if ENTRY.match(line):
            cur = {"line": n, "text": line}
            out.append(cur)
        elif cur is not None and line.strip() and not line.startswith(">") and not line.startswith("#"):
            cur["text"] += "\n" + line
    for e in out:
        t = e["text"]
        e["date"] = ENTRY.match(t).group(1)
        m = re.match(r"^(?:- )?\*\*(.*?)\*\*", t, re.S)
        head = m.group(1) if m else t[:120]
        e["title"] = re.sub(r"\s+", " ", re.sub(r"^\d{4}-\d\d-\d\d\s*", "", head)).strip(" :—–-")[:110]
        e["body"] = t[m.end():].strip() if m else t
        s = STATUS.search(e["body"])
        e["note"] = s.group(1).strip() if s else ""
        if s:
            e["body"] = e["body"][:s.start()].strip()
    return out


def split_items(body):
    """Split on sequential markers (1) (2) ... or (a) (b) ...; a marker inside a phrase such as
    'point (2)' is not a split."""
    for seq in ([str(i) for i in range(1, 15)], list("abcdefghij")):
        pos, start = [], 0
        for k in seq:
            m = None
            for cand in re.finditer(r"\(%s\)\s" % re.escape(k), body[start:]):
                before = body[max(0, start + cand.start() - 9):start + cand.start()].lower()
                if re.search(r"(points?|entrée|entry|item)\s*$", before):
                    continue
                m = cand
                break
            if not m:
                break
            pos.append((k, start + m.start(), start + m.end()))
            start = start + m.end()
        if len(pos) >= 2:
            items = []
            lead = body[:pos[0][1]].strip()
            for i, (k, a, b) in enumerate(pos):
                end = pos[i + 1][1] if i + 1 < len(pos) else len(body)
                items.append((k, (body[b:end]).strip()))
            return lead, items
    return "", [("", body)]


def clean(t):
    return re.sub(r"\s+", " ", t).strip()


def build(assets):
    log = os.path.join(assets, "profile_log.md")
    cfg = json.load(open(os.path.join(assets, "facts", "themes.json"), encoding="utf-8"))
    themes = cfg["themes"]
    bundle = re.compile(cfg["bundle_title"], re.I) if cfg.get("bundle_title") else None
    for t in themes:
        t["_title"] = re.compile(t["title"], re.I) if t.get("title") else None
        t["_text"] = re.compile(t["text"], re.I) if t.get("text") else None
    sheets = {t["name"]: {"cur": [], "old": []} for t in themes}
    sheets["unsorted"] = {"cur": [], "old": []}
    ents = entries(log)
    for e in ents:
        lead, items = split_items(e["body"])
        named = set(re.findall(r"point \((\w+)\)", e["note"]))
        for k, text in items:
            text = clean(text)
            if not text:
                continue
            full = (clean(lead) + " " + text) if lead and len(lead) < 160 else text
            theme = "unsorted"
            is_bundle = bool(bundle and bundle.search(e["title"]))
            for t in themes:
                by_title = t["_title"] and (not is_bundle or t.get("title_always")) and t["_title"].search(e["title"])
                if by_title or (t["_text"] and t["_text"].search(text)):
                    theme = t["name"]
                    break
            old = "⛔" in text or (e["note"] and (not named or k in named))
            ref = "%s · %s%s" % (e["date"], e["title"], (" · (%s)" % k) if k else "")
            line = "- [%s] %s" % (ref, full)
            if old and e["note"] and "⛔" not in text:
                line += " **→ %s**" % e["note"]
            sheets[theme]["old" if old else "cur"].append((e["date"], e["line"], line))
    out = {}
    desc = {t["name"]: t.get("description", "") for t in themes}
    desc["unsorted"] = "Items no theme pattern matched. Read them when a search comes back thin, and add a pattern to themes.json when a group of them belongs together."
    index = ["# Fact sheets", "",
             "Generated by `build_facts.py` from `../profile_log.md`. Do not edit these files: add or correct a fact in the log, then rebuild.",
             "Figures are printed as worded in the Current values table of `../candidate_profile.md`, which wins over any line here.", "",
             "| Sheet | What it holds | Current items | Replaced or corrected |", "|---|---|---|---|"]
    for name in list(sheets):
        s = sheets[name]
        if not s["cur"] and not s["old"]:
            continue
        body = ["# Facts: %s" % name.replace("_", " "), "",
                "> %s" % desc[name],
                "> Generated from `../profile_log.md` (%d entries, last dated %s). Do not edit: correct the log and rebuild. Each line starts with the date and title of its log entry." % (len(ents), max(e["date"] for e in ents)),
                "", "## Current (most recent first)", ""]
        body += [l for _, _, l in sorted(s["cur"], key=lambda x: (x[0], x[1]), reverse=True)] or ["None."]
        if s["old"]:
            body += ["", "## Replaced or corrected (do not use without reading the correction)", ""]
            body += [l for _, _, l in sorted(s["old"], key=lambda x: (x[0], x[1]), reverse=True)]
        out[name + ".md"] = "\n".join(body) + "\n"
        index.append("| [%s](%s.md) | %s | %d | %d |" % (name, name, desc[name], len(s["cur"]), len(s["old"])))
    out["INDEX.md"] = "\n".join(index) + "\n"
    return out, len(ents)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    assets = args[0]
    out, n = build(assets)
    fdir = os.path.join(assets, "facts")
    if "--check" in sys.argv:
        stale = [f for f, c in out.items()
                 if not os.path.exists(os.path.join(fdir, f)) or open(os.path.join(fdir, f), encoding="utf-8").read() != c]
        print("FACTS: %s" % ("up to date" if not stale else "STALE (%s): run build_facts.py" % ", ".join(sorted(stale))))
        sys.exit(1 if stale else 0)
    for f, c in out.items():
        open(os.path.join(fdir, f), "w", encoding="utf-8").write(c)
    total = sum(c.count("\n- [") for f, c in out.items() if f != "INDEX.md")
    print("FACTS: %d entries, %d items, %d sheets written to %s" % (n, total, len(out) - 1, fdir))


if __name__ == "__main__":
    main()
