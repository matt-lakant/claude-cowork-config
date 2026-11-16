#!/usr/bin/env python3
"""Find what is on record for a requirement in candidate_profile.md. Standard library only.

The profile's Q&A log is append-only, several hundred kilobytes, mostly in French, and holds most
of the facts that make a CV specific. Nobody reads it in full, so the facts get found late, by the
reviewer. This script is the search to run BEFORE drafting, once per requirement of the posting.

Usage:
  python3 profile_search.py <candidate_profile.md> "<term>;<term>;..." [--max 8] [--width 260]

  terms   words or phrases for ONE requirement, separated by ";". Give the posting's word, its
          French equivalent and the synonyms Matt would use: "SOW;statement of work;cahier des
          charges;chiffrage;estimation". A term is a case-insensitive regular expression, so
          "utili[sz]ation" and "sous-trait|subcontract" work. An entry matches if any term does;
          entries matching more terms come first, then the most recent.

Output, one block per entry: line number, date of the entry, its title, the terms found, and the
text around each match. "LATER ENTRY MAY SUPERSEDE" is printed when the entry itself says it
replaces or corrects something: read the dates before using a figure, and prefer the Current values
table at the top of the profile when the figure has a row there.
"""
import re, sys

DATE = re.compile(r"(20\d\d-\d\d-\d\d)")
SUPERSEDE = re.compile(r"remplace|supersed|corrige|prévaut|annule|replaces|lève", re.I)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    def opt(name, default):
        if name in sys.argv:
            v = sys.argv[sys.argv.index(name) + 1]
            if v in args:
                args.remove(v)
            return int(v)
        return default
    mx, width = opt("--max", 8), opt("--width", 260)
    if len(args) != 2:
        sys.exit(__doc__)
    path, terms = args[0], [t.strip() for t in args[1].split(";") if t.strip()]
    rxs = [(t, re.compile(t, re.I)) for t in terms]
    hits = []
    section = ""
    for n, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if line.startswith("#"):
            section = line.lstrip("# ").strip()
            continue
        if not line.strip() or line.startswith("|---"):
            continue
        found = [(t, [m.start() for m in rx.finditer(line)]) for t, rx in rxs]
        found = [(t, pos) for t, pos in found if pos]
        if not found:
            continue
        d = DATE.search(line[:60])
        title = re.sub(r"[*`]", "", line[:110]).strip("- ").split(":**")[0][:100]
        hits.append((len(found), d.group(1) if d else "", n, section, title, found, line))
    hits.sort(key=lambda h: (-h[0], h[1] == "", [-ord(c) for c in h[1]]))
    print("%d entries match %s; showing %d" % (len(hits), terms, min(mx, len(hits))))
    for count, date, n, section, title, found, line in hits[:mx]:
        flag = "  [LATER ENTRY MAY SUPERSEDE: check dates]" if SUPERSEDE.search(line) else ""
        print("\n--- line %d | %s | %s%s" % (n, date or "undated (" + section[:40] + ")", title, flag))
        print("    terms: " + ", ".join(t for t, _ in found))
        shown = []
        for t, pos in found:
            for p in pos[:2]:
                if any(abs(p - q) < width for q in shown):
                    continue
                shown.append(p)
                a, b = max(0, p - width // 2), min(len(line), p + width // 2)
                print("    ..." + line[a:b].replace("\n", " ") + "...")


if __name__ == "__main__":
    main()
