#!/usr/bin/env python3
"""Validate curriculum JSON files. Usage: validate.py [grade_dir_or_file ...]"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "data" / "curriculum"
SUBJECTS = {"ELA", "MATH", "SCI", "HSS", "VAPA", "PE", "HEALTH", "WL", "ELEC"}

def check(path):
    errs = []
    try:
        c = json.loads(path.read_text())
    except Exception as e:
        return [f"invalid JSON: {e}"]
    for k in ("grade", "subject", "title", "description", "framework", "minutes_per_day",
              "standards", "resources", "units", "weeks"):
        if k not in c:
            errs.append(f"missing key {k}")
    if errs:
        return errs
    if c["subject"] not in SUBJECTS:
        errs.append(f"bad subject {c['subject']}")
    if path.stem != c["subject"]:
        errs.append("file name must equal subject code")
    if path.parent.name != f"grade_{c['grade']:02d}":
        errs.append("grade does not match directory")
    stds = c["standards"]
    units = {u["number"]: u for u in c["units"]}
    for u in c["units"]:
        for s in u.get("standards", []):
            if s not in stds:
                errs.append(f"unit {u['number']}: undefined standard {s}")
    weeks = c["weeks"]
    nums = [w.get("week") for w in weeks]
    if nums != list(range(1, 37)):
        errs.append(f"weeks must be 1..36 in order (got {len(weeks)} weeks)")
    for w in weeks:
        wn = w.get("week")
        u = units.get(w.get("unit"))
        if not u:
            errs.append(f"week {wn}: unknown unit {w.get('unit')}")
        elif not (u["start_week"] <= wn <= u["end_week"]):
            errs.append(f"week {wn}: outside unit {u['number']} range")
        for k in ("topic", "objectives", "standards", "days", "assessment"):
            if not w.get(k):
                errs.append(f"week {wn}: missing/empty {k}")
        for s in w.get("standards", []):
            if s not in stds:
                errs.append(f"week {wn}: undefined standard {s}")
        days = w.get("days", [])
        if len(days) != 5:
            errs.append(f"week {wn}: needs 5 days, has {len(days)}")
        for i, d in enumerate(days):
            if not isinstance(d, dict) or not d.get("title") or not d.get("work"):
                errs.append(f"week {wn} day {i+1}: needs title and work")
    for r in c["resources"]:
        if not r.get("url", "").startswith("http"):
            errs.append(f"resource {r.get('name')}: bad url")
    return errs

def main(args):
    paths = []
    for a in args or [str(ROOT)]:
        p = pathlib.Path(a)
        paths += sorted(p.rglob("*.json")) if p.is_dir() else [p]
    bad = 0
    for p in paths:
        errs = check(p)
        if errs:
            bad += 1
            print(f"FAIL {p}")
            for e in errs[:25]:
                print("   ", e)
        else:
            print(f"ok   {p}")
    print(f"\n{len(paths) - bad}/{len(paths)} files valid")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
