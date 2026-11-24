#!/usr/bin/env python3
"""Print or export lesson plans from homeschool.db as Markdown.

Examples:
  python3 scripts/plan.py week  --grade 3 --week 5          # one week, all subjects, day by day
  python3 scripts/plan.py day   --grade 3 --week 5 --day 2  # a single day's checklist
  python3 scripts/plan.py course --grade 9 --subject MATH   # course scope & sequence
  python3 scripts/plan.py teacher --grade 3 --week 5 [--subject MATH]  # teacher's guide with answers
  python3 scripts/plan.py search "photosynthesis"           # full-text search of lessons
  python3 scripts/plan.py paperwork [--option PSA]          # required documents
  python3 scripts/plan.py funding                           # grants / funding programs
  python3 scripts/plan.py resources [--grade 4] [--subject SCI]
  python3 scripts/plan.py export --out docs/plans           # write every week of every grade to Markdown
"""
import argparse
import pathlib
import signal
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "homeschool.db"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def connect():
    if not DB.exists():
        sys.exit("homeschool.db not found — run: python3 scripts/build_db.py")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def week_md(con, grade, week, only_day=None):
    g = con.execute("SELECT * FROM grades WHERE grade=?", (grade,)).fetchone()
    out = [f"# {g['name']} — Week {week} (Quarter {(week - 1) // 9 + 1})", ""]
    overview = con.execute("SELECT * FROM v_weekly_overview WHERE grade=? AND week=? "
                           "ORDER BY (SELECT sort_order FROM subjects WHERE code=subject_code)",
                           (grade, week)).fetchall()
    if only_day is None:
        out += ["## Week at a glance", "", "| Subject | Unit | Topic | Standards |", "|---|---|---|---|"]
        for o in overview:
            out.append(f"| {o['course']} | {o['unit'] or ''} | {o['topic']} | {o['standards'] or ''} |")
        out.append("")
    days = [only_day] if only_day else range(1, 6)
    for d in days:
        rows = con.execute("SELECT * FROM v_daily_plan WHERE grade=? AND week=? AND day=? "
                           "ORDER BY subject_order", (grade, week, d)).fetchall()
        total = sum(r["minutes"] or 0 for r in rows)
        out += [f"## Day {d} — {DAYS[d - 1]} (school day {(week - 1) * 5 + d}, ~{total} min)", ""]
        for r in rows:
            out.append(f"- [ ] **{r['course']}** — *{r['lesson_title']}* ({r['minutes']} min): {r['work']}")
        out.append("")
    if only_day is None:
        out += ["## Objectives, materials & assessment", ""]
        for o in overview:
            out.append(f"### {o['course']}: {o['topic']}")
            if o["objectives"]:
                out += [f"- Objective: {x}" for x in o["objectives"].split("\n")]
            if o["vocabulary"]:
                out.append(f"- Vocabulary: {o['vocabulary']}")
            if o["materials"]:
                out.append(f"- Materials: {o['materials']}")
            out.append(f"- Assessment: {o['assessment']}")
            out.append("")
    return "\n".join(out)


def course_md(con, grade, subject):
    c = con.execute("SELECT * FROM courses WHERE grade=? AND subject_code=?", (grade, subject)).fetchone()
    if not c:
        sys.exit("course not found")
    out = [f"# {c['title']} (Grade {grade})", "", c["description"] or "", "",
           f"*Framework:* {c['framework']}  ", f"*Time:* {c['minutes_per_day']} min/day"]
    if c["ag_requirement"]:
        out.append(f"*UC/CSU a–g:* {c['ag_requirement']} · *Credits:* {c['credits']}")
    out += ["", "## Units", ""]
    for u in con.execute("SELECT * FROM units WHERE course_id=? ORDER BY number", (c["id"],)):
        out.append(f"### Unit {u['number']}: {u['title']} (weeks {u['start_week']}–{u['end_week']})")
        out.append(f"{u['big_idea'] or ''}\n")
        for w in con.execute("SELECT week, topic FROM weekly_plans WHERE unit_id=? ORDER BY week", (u["id"],)):
            out.append(f"- Week {w['week']}: {w['topic']}")
        out.append("")
    out += ["## Free resources", ""]
    for r in con.execute("SELECT r.name, r.url, cr.note FROM course_resources cr JOIN resources r "
                         "ON r.id=cr.resource_id WHERE cr.course_id=?", (c["id"],)):
        out.append(f"- [{r['name']}]({r['url']}) {('— ' + r['note']) if r['note'] else ''}")
    out += ["", "## Standards", ""]
    for s in con.execute("SELECT code, description FROM standards WHERE grade=? AND subject_code=? "
                         "ORDER BY code", (grade, subject)):
        out.append(f"- **{s['code']}** {s['description']}")
    return "\n".join(out)


def teacher_md(con, grade, week, subject=None):
    g = con.execute("SELECT * FROM grades WHERE grade=?", (grade,)).fetchone()
    q = ("SELECT c.id, c.title, c.subject_code, w.id AS wid, w.topic, w.assessment, tw.prep, tw.misconceptions,"
         " tw.assessment_key FROM weekly_plans w JOIN courses c ON c.id=w.course_id"
         " JOIN subjects s ON s.code=c.subject_code LEFT JOIN teacher_weeks tw ON tw.weekly_plan_id=w.id"
         " WHERE c.grade=? AND w.week=?")
    args = [grade, week]
    if subject:
        q += " AND c.subject_code=?"; args.append(subject.upper())
    out = [f"# Teacher's Guide — {g['name']}, Week {week}", ""]
    for c in con.execute(q + " ORDER BY s.sort_order", args).fetchall():
        out += [f"## {c['title']}: {c['topic']}", ""]
        if c["prep"]:
            out += [f"**Prepare:** {c['prep']}", ""]
        if c["misconceptions"]:
            out += ["**Watch for:**"] + [f"- {m}" for m in c["misconceptions"].split("\n")] + [""]
        for d in con.execute("SELECT d.id, d.day, d.day_name, d.title, d.work, td.guide FROM daily_lessons d"
                             " LEFT JOIN teacher_days td ON td.daily_lesson_id=d.id"
                             " WHERE d.weekly_plan_id=? ORDER BY d.day", (c["wid"],)):
            out += [f"### Day {d['day']} ({d['day_name']}): {d['title']}", f"*Student:* {d['work']}", ""]
            if d["guide"]:
                out += [f"*How to teach:* {d['guide']}", ""]
            for qa in con.execute("SELECT question, answer FROM teacher_questions WHERE daily_lesson_id=? ORDER BY seq", (d["id"],)):
                out += [f"- **Q:** {qa['question']}", f"  **A:** {qa['answer']}"]
            out.append("")
        out += [f"**Assessment:** {c['assessment']}", ""]
        if c["assessment_key"]:
            out += [f"**Answer key:** {c['assessment_key']}", ""]
    return "\n".join(out)


def main():
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # allow piping into head
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("week"); p.add_argument("--grade", type=int, required=True); p.add_argument("--week", type=int, required=True)
    p = sub.add_parser("day"); p.add_argument("--grade", type=int, required=True); p.add_argument("--week", type=int, required=True); p.add_argument("--day", type=int, required=True)
    p = sub.add_parser("course"); p.add_argument("--grade", type=int, required=True); p.add_argument("--subject", required=True)
    p = sub.add_parser("teacher"); p.add_argument("--grade", type=int, required=True); p.add_argument("--week", type=int, required=True); p.add_argument("--subject")
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--grade", type=int)
    p = sub.add_parser("paperwork"); p.add_argument("--option")
    sub.add_parser("funding")
    p = sub.add_parser("resources"); p.add_argument("--grade", type=int); p.add_argument("--subject")
    p = sub.add_parser("export"); p.add_argument("--out", default=str(ROOT / "docs" / "plans"))
    a = ap.parse_args()
    con = connect()

    if a.cmd == "week":
        print(week_md(con, a.grade, a.week))
    elif a.cmd == "day":
        print(week_md(con, a.grade, a.week, a.day))
    elif a.cmd == "teacher":
        print(teacher_md(con, a.grade, a.week, a.subject))
    elif a.cmd == "course":
        print(course_md(con, a.grade, a.subject.upper()))
    elif a.cmd == "search":
        q = "SELECT grade, subject_code, week, day, course, title, work FROM lesson_search WHERE lesson_search MATCH ?"
        args = [a.query]
        if a.grade:
            q += " AND grade = ?"; args.append(a.grade)
        for r in con.execute(q + " ORDER BY rank LIMIT 50", args):
            print(f"G{r['grade']} W{r['week']} D{r['day']} {r['course']}: {r['title']} — {r['work']}")
    elif a.cmd == "paperwork":
        q, args = "SELECT * FROM paperwork", []
        if a.option:
            q += " WHERE homeschool_option LIKE ? OR homeschool_option LIKE '%ALL%'"; args = [f"%{a.option.upper()}%"]
        for r in con.execute(q + " ORDER BY CASE action WHEN 'submit' THEN 0 WHEN 'keep_on_file' THEN 1 ELSE 2 END, name", args):
            print(f"[{r['action']}] {r['name']} ({r['homeschool_option']}) — {r['deadline'] or r['frequency'] or ''}\n"
                  f"    {r['description']}\n    Basis: {r['legal_basis'] or '-'}  {r['url'] or ''}\n")
    elif a.cmd == "funding":
        for r in con.execute("SELECT * FROM funding_programs ORDER BY category, name"):
            print(f"[{r['category']}] {r['name']} — {r['provider'] or ''}\n    Benefit: {r['benefit']}\n"
                  f"    Eligibility: {r['eligibility']}\n    {r['url'] or ''}\n")
    elif a.cmd == "resources":
        q, args = "SELECT DISTINCT r.* FROM resources r LEFT JOIN resource_subjects rs ON rs.resource_id=r.id WHERE 1=1", []
        if a.grade:
            q += " AND (r.grade_min IS NULL OR r.grade_min <= ?) AND (r.grade_max IS NULL OR r.grade_max >= ?)"; args += [a.grade, a.grade]
        if a.subject:
            q += " AND rs.subject_code IN (?, 'ALL')"; args.append(a.subject.upper())
        for r in con.execute(q + " ORDER BY r.name", args):
            print(f"{r['name']} — {r['url']}\n    {r['description'] or ''}")
    elif a.cmd == "export":
        out = pathlib.Path(a.out)
        n = 0
        for g in con.execute("SELECT grade FROM grades ORDER BY grade").fetchall():
            gd = out / f"grade_{g['grade']:02d}"
            gd.mkdir(parents=True, exist_ok=True)
            for subj in con.execute("SELECT subject_code FROM courses WHERE grade=?", (g["grade"],)).fetchall():
                (gd / f"course_{subj['subject_code']}.md").write_text(course_md(con, g["grade"], subj["subject_code"]))
            for wk in range(1, 37):
                (gd / f"week_{wk:02d}.md").write_text(week_md(con, g["grade"], wk))
                n += 1
        tdir = out.parent / "teacher"
        if con.execute("SELECT count(*) FROM teacher_weeks").fetchone()[0]:
            for g in con.execute("SELECT grade FROM grades ORDER BY grade").fetchall():
                gd = tdir / f"grade_{g['grade']:02d}"
                gd.mkdir(parents=True, exist_ok=True)
                for wk in range(1, 37):
                    (gd / f"week_{wk:02d}.md").write_text(teacher_md(con, g["grade"], wk))
            print(f"Wrote teacher's guides to {tdir}")
        print(f"Wrote {n} weekly plans to {out}")


if __name__ == "__main__":
    main()
