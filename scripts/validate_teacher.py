#!/usr/bin/env python3
"""Validate teacher's guide files against the matching curriculum files.
Usage: validate_teacher.py [dir_or_file ...]   (default: data/teacher)"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "data"

def check(p):
    errs = []
    try:
        t = json.loads(p.read_text())
    except Exception as e:
        return [f"invalid JSON: {e}"]
    cur = ROOT / "curriculum" / p.parent.name / p.name
    if not cur.exists():
        return [f"no matching curriculum file {cur}"]
    c = json.loads(cur.read_text())
    if t.get("grade") != c["grade"] or t.get("subject") != c["subject"]:
        errs.append("grade/subject mismatch with curriculum file")
    if not t.get("overview"):
        errs.append("missing overview")
    weeks = t.get("weeks", [])
    if [w.get("week") for w in weeks] != list(range(1, 37)):
        errs.append(f"weeks must be 1..36 in order (got {len(weeks)})")
    for w in weeks:
        wn = w.get("week")
        for k in ("prep", "assessment_key"):
            if not w.get(k):
                errs.append(f"week {wn}: missing {k}")
        if not w.get("misconceptions"):
            errs.append(f"week {wn}: missing misconceptions")
        days = w.get("days", [])
        if len(days) != 5:
            errs.append(f"week {wn}: needs 5 days, has {len(days)}")
        for i, d in enumerate(days, 1):
            if not d.get("guide"):
                errs.append(f"week {wn} day {i}: missing guide")
            qs = d.get("questions") or []
            if not qs:
                errs.append(f"week {wn} day {i}: needs at least one question")
            for q in qs:
                if not q.get("q") or not q.get("a"):
                    errs.append(f"week {wn} day {i}: question needs q and a")
    return errs

def main(args):
    paths = []
    for a in args or [str(ROOT / "teacher")]:
        p = pathlib.Path(a)
        paths += sorted(p.rglob("*.json")) if p.is_dir() else [p]
    bad = 0
    for p in paths:
        e = check(p)
        if e:
            bad += 1
            print(f"FAIL {p}")
            for x in e[:25]:
                print("   ", x)
        else:
            print(f"ok   {p}")
    print(f"\n{len(paths) - bad}/{len(paths)} files valid")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
