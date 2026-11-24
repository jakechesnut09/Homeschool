#!/usr/bin/env python3
"""Compile the JSON source data in data/ into the SQLite database homeschool.db.

Usage:  python3 scripts/build_db.py [--out homeschool.db]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

GRADES = {
    1: ("Elementary", "A Child's Place in Time and Space"),
    2: ("Elementary", "People Who Make a Difference"),
    3: ("Elementary", "Continuity and Change"),
    4: ("Elementary", "California: A Changing State"),
    5: ("Elementary", "United States History and Geography: Making a New Nation"),
    6: ("Middle", "World History and Geography: Ancient Civilizations"),
    7: ("Middle", "World History and Geography: Medieval and Early Modern Times"),
    8: ("Middle", "United States History and Geography: Growth and Conflict"),
    9: ("High", "World Geography & Ethnic Studies"),
    10: ("High", "World History, Culture, and Geography: The Modern World"),
    11: ("High", "United States History and Geography: Continuity and Change in the Twentieth Century"),
    12: ("High", "Principles of American Democracy and Economics"),
}

SUBJECTS = [
    ("ELA", "English Language Arts", "Ed Code 51210(a)(1) / 51220(a)", 1),
    ("MATH", "Mathematics", "Ed Code 51210(a)(2) / 51220(f)", 2),
    ("SCI", "Science", "Ed Code 51210(a)(4) / 51220(e)", 3),
    ("HSS", "History–Social Science", "Ed Code 51210(a)(3) / 51220(b)", 4),
    ("WL", "World Language (Spanish)", "Ed Code 51220(c) — grades 7–12", 5),
    ("VAPA", "Visual & Performing Arts", "Ed Code 51210(a)(5) / 51220(g)", 6),
    ("PE", "Physical Education", "Ed Code 51210(a)(7) / 51220(d); 51222", 7),
    ("HEALTH", "Health Education", "Ed Code 51210(a)(6) / 51220(h)(i) (driver ed)", 8),
    ("ELEC", "Elective / Career Technical Education", "Ed Code 51220(h)(j)", 9),
]

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);

CREATE TABLE grades (
  grade        INTEGER PRIMARY KEY,
  name         TEXT NOT NULL,
  band         TEXT NOT NULL,          -- Elementary / Middle / High
  hss_theme    TEXT
);

CREATE TABLE subjects (
  code         TEXT PRIMARY KEY,
  name         TEXT NOT NULL,
  ca_basis     TEXT,                    -- CA Education Code basis for the subject
  sort_order   INTEGER
);

CREATE TABLE courses (
  id              INTEGER PRIMARY KEY,
  grade           INTEGER NOT NULL REFERENCES grades(grade),
  subject_code    TEXT NOT NULL REFERENCES subjects(code),
  title           TEXT NOT NULL,
  description     TEXT,
  framework       TEXT,
  minutes_per_day INTEGER,
  ag_requirement  TEXT,                -- UC/CSU a-g area (high school)
  credits         REAL,                -- high school semester units
  UNIQUE (grade, subject_code)
);

CREATE TABLE standards (
  id           INTEGER PRIMARY KEY,
  subject_code TEXT NOT NULL REFERENCES subjects(code),
  grade        INTEGER NOT NULL,
  code         TEXT NOT NULL,
  description  TEXT,
  UNIQUE (subject_code, grade, code)
);

CREATE TABLE units (
  id          INTEGER PRIMARY KEY,
  course_id   INTEGER NOT NULL REFERENCES courses(id),
  number      INTEGER NOT NULL,
  title       TEXT NOT NULL,
  start_week  INTEGER NOT NULL,
  end_week    INTEGER NOT NULL,
  big_idea    TEXT,
  UNIQUE (course_id, number)
);

CREATE TABLE unit_standards (
  unit_id     INTEGER REFERENCES units(id),
  standard_id INTEGER REFERENCES standards(id),
  PRIMARY KEY (unit_id, standard_id)
);

CREATE TABLE weekly_plans (
  id          INTEGER PRIMARY KEY,
  course_id   INTEGER NOT NULL REFERENCES courses(id),
  unit_id     INTEGER REFERENCES units(id),
  week        INTEGER NOT NULL CHECK (week BETWEEN 1 AND 36),
  quarter     INTEGER NOT NULL,
  semester    INTEGER NOT NULL,
  topic       TEXT NOT NULL,
  objectives  TEXT,          -- newline-separated
  vocabulary  TEXT,          -- comma-separated
  materials   TEXT,          -- comma-separated
  assessment  TEXT,
  UNIQUE (course_id, week)
);

CREATE TABLE weekly_plan_standards (
  weekly_plan_id INTEGER REFERENCES weekly_plans(id),
  standard_id    INTEGER REFERENCES standards(id),
  PRIMARY KEY (weekly_plan_id, standard_id)
);

CREATE TABLE daily_lessons (
  id             INTEGER PRIMARY KEY,
  weekly_plan_id INTEGER NOT NULL REFERENCES weekly_plans(id),
  course_id      INTEGER NOT NULL REFERENCES courses(id),
  grade          INTEGER NOT NULL,
  subject_code   TEXT NOT NULL,
  week           INTEGER NOT NULL,
  day            INTEGER NOT NULL CHECK (day BETWEEN 1 AND 5),
  day_name       TEXT NOT NULL,
  school_day     INTEGER NOT NULL,     -- 1..180
  title          TEXT NOT NULL,
  work           TEXT NOT NULL,
  minutes        INTEGER,
  UNIQUE (course_id, week, day)
);
CREATE INDEX idx_daily_grade_week ON daily_lessons (grade, week, day);

CREATE TABLE resources (
  id          INTEGER PRIMARY KEY,
  name        TEXT NOT NULL,
  provider    TEXT,
  url         TEXT NOT NULL UNIQUE,
  type        TEXT,
  cost        TEXT,
  grade_min   INTEGER,
  grade_max   INTEGER,
  description TEXT
);

CREATE TABLE resource_subjects (
  resource_id  INTEGER REFERENCES resources(id),
  subject_code TEXT,
  PRIMARY KEY (resource_id, subject_code)
);

CREATE TABLE course_resources (
  course_id   INTEGER REFERENCES courses(id),
  resource_id INTEGER REFERENCES resources(id),
  note        TEXT,
  PRIMARY KEY (course_id, resource_id)
);

CREATE TABLE legal_options (
  code         TEXT PRIMARY KEY,
  name         TEXT NOT NULL,
  description  TEXT,
  requirements TEXT,   -- newline-separated
  pros         TEXT,
  cons         TEXT,
  legal_basis  TEXT,
  url          TEXT
);

CREATE TABLE paperwork (
  id               INTEGER PRIMARY KEY,
  name             TEXT NOT NULL,
  homeschool_option TEXT,     -- PSA / PSP / CHARTER / TUTOR / DISTRICT_IS / ALL
  action           TEXT,      -- submit / keep_on_file / recommended
  frequency        TEXT,
  deadline         TEXT,
  legal_basis      TEXT,
  url              TEXT,
  description      TEXT
);

CREATE TABLE funding_programs (
  id               INTEGER PRIMARY KEY,
  name             TEXT NOT NULL,
  category         TEXT,
  provider         TEXT,
  url              TEXT,
  eligibility      TEXT,
  benefit          TEXT,
  how_to_apply     TEXT,
  california_notes TEXT,
  last_verified    TEXT
);

CREATE VIRTUAL TABLE lesson_search USING fts5(
  grade UNINDEXED, subject_code UNINDEXED, week UNINDEXED, day UNINDEXED,
  course, topic, title, work, tokenize = 'porter'
);

-- ---------- Convenience views ----------
CREATE VIEW v_daily_plan AS
SELECT d.grade, d.week, d.day, d.day_name, d.school_day,
       s.sort_order AS subject_order, d.subject_code, c.title AS course,
       u.title AS unit, w.topic AS week_topic,
       d.title AS lesson_title, d.work, d.minutes
FROM daily_lessons d
JOIN courses c       ON c.id = d.course_id
JOIN subjects s      ON s.code = d.subject_code
JOIN weekly_plans w  ON w.id = d.weekly_plan_id
LEFT JOIN units u    ON u.id = w.unit_id;

CREATE VIEW v_weekly_overview AS
SELECT c.grade, w.week, w.quarter, w.semester, c.subject_code, c.title AS course,
       u.title AS unit, w.topic, w.objectives, w.vocabulary, w.materials, w.assessment,
       (SELECT group_concat(st.code, ', ') FROM weekly_plan_standards ws
          JOIN standards st ON st.id = ws.standard_id WHERE ws.weekly_plan_id = w.id) AS standards
FROM weekly_plans w
JOIN courses c    ON c.id = w.course_id
LEFT JOIN units u ON u.id = w.unit_id;

CREATE VIEW v_course_catalog AS
SELECT c.grade, g.band, c.subject_code, c.title, c.minutes_per_day,
       c.minutes_per_day * 5 AS minutes_per_week, c.ag_requirement, c.credits,
       (SELECT count(*) FROM units u WHERE u.course_id = c.id) AS units,
       c.framework, c.description
FROM courses c JOIN grades g ON g.grade = c.grade;

CREATE VIEW v_daily_minutes AS
SELECT grade, week, day, day_name, sum(minutes) AS total_minutes, count(*) AS subjects
FROM daily_lessons GROUP BY grade, week, day;

CREATE VIEW v_hs_course_plan AS
SELECT grade, subject_code, title, ag_requirement, credits
FROM courses WHERE grade >= 9 ORDER BY grade, subject_code;
"""


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def joinl(v, sep):
    if v is None:
        return None
    if isinstance(v, list):
        return sep.join(str(x) for x in v)
    return str(v)


def upsert_resource(cur, r, grade=None, subject=None):
    url = r["url"].strip()
    row = cur.execute("SELECT id FROM resources WHERE url = ?", (url,)).fetchone()
    if row:
        rid = row[0]
        if grade is not None:  # widen grade span for course-level resources
            cur.execute("UPDATE resources SET grade_min = min(coalesce(grade_min, ?), ?),"
                        " grade_max = max(coalesce(grade_max, ?), ?) WHERE id = ?",
                        (grade, grade, grade, grade, rid))
    else:
        cur.execute(
            "INSERT INTO resources (name, provider, url, type, cost, grade_min, grade_max, description)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (r.get("name"), r.get("provider"), url, r.get("type"), r.get("cost", "free"),
             r.get("grade_min", grade), r.get("grade_max", grade),
             r.get("description") or r.get("note")))
        rid = cur.lastrowid
    subs = r.get("subjects") or ([subject] if subject else [])
    for s in subs:
        cur.execute("INSERT OR IGNORE INTO resource_subjects VALUES (?, ?)", (rid, s))
    return rid


def build(out):
    if out.exists():
        out.unlink()
    con = sqlite3.connect(out)
    cur = con.cursor()
    cur.executescript(SCHEMA)

    for g, (band, theme) in GRADES.items():
        name = {1: "1st Grade", 2: "2nd Grade", 3: "3rd Grade"}.get(g, f"{g}th Grade")
        cur.execute("INSERT INTO grades VALUES (?,?,?,?)", (g, name, band, theme))
    cur.executemany("INSERT INTO subjects VALUES (?,?,?,?)", SUBJECTS)

    # Reference data first so course resources can merge with the master list.
    ref = DATA / "reference"
    if (ref / "resources.json").exists():
        for r in load_json(ref / "resources.json"):
            upsert_resource(cur, r)
    if (ref / "legal_options.json").exists():
        for o in load_json(ref / "legal_options.json"):
            cur.execute("INSERT INTO legal_options VALUES (?,?,?,?,?,?,?,?)",
                        (o["code"], o["name"], o.get("description"),
                         joinl(o.get("requirements"), "\n"), joinl(o.get("pros"), "\n"),
                         joinl(o.get("cons"), "\n"), o.get("legal_basis"), o.get("url")))
    if (ref / "paperwork.json").exists():
        for p in load_json(ref / "paperwork.json"):
            cur.execute("INSERT INTO paperwork (name, homeschool_option, action, frequency, deadline,"
                        " legal_basis, url, description) VALUES (?,?,?,?,?,?,?,?)",
                        (p["name"], joinl(p.get("homeschool_option"), ", "), p.get("action"),
                         p.get("frequency"), p.get("deadline"), p.get("legal_basis"),
                         p.get("url"), p.get("description")))
    if (ref / "funding.json").exists():
        for f in load_json(ref / "funding.json"):
            cur.execute("INSERT INTO funding_programs (name, category, provider, url, eligibility, benefit,"
                        " how_to_apply, california_notes, last_verified) VALUES (?,?,?,?,?,?,?,?,?)",
                        (f["name"], f.get("category"), f.get("provider"), f.get("url"),
                         f.get("eligibility"), f.get("benefit"), f.get("how_to_apply"),
                         f.get("california_notes"), f.get("last_verified")))

    course_files = sorted((DATA / "curriculum").glob("grade_*/*.json"))
    counts = {"courses": 0, "weeks": 0, "lessons": 0}
    for path in course_files:
        c = load_json(path)
        g, subj = c["grade"], c["subject"]
        cur.execute("INSERT INTO courses (grade, subject_code, title, description, framework,"
                    " minutes_per_day, ag_requirement, credits) VALUES (?,?,?,?,?,?,?,?)",
                    (g, subj, c["title"], c.get("description"), c.get("framework"),
                     c.get("minutes_per_day"), c.get("ag_requirement"), c.get("credits")))
        cid = cur.lastrowid
        counts["courses"] += 1

        std_ids = {}
        for code, desc in c.get("standards", {}).items():
            cur.execute("INSERT OR IGNORE INTO standards (subject_code, grade, code, description)"
                        " VALUES (?,?,?,?)", (subj, g, code, desc))
            std_ids[code] = cur.execute(
                "SELECT id FROM standards WHERE subject_code=? AND grade=? AND code=?",
                (subj, g, code)).fetchone()[0]

        for r in c.get("resources", []):
            rid = upsert_resource(cur, r, grade=g, subject=subj)
            cur.execute("INSERT OR IGNORE INTO course_resources VALUES (?,?,?)",
                        (cid, rid, r.get("note")))

        unit_ids = {}
        for u in c.get("units", []):
            cur.execute("INSERT INTO units (course_id, number, title, start_week, end_week, big_idea)"
                        " VALUES (?,?,?,?,?,?)",
                        (cid, u["number"], u["title"], u["start_week"], u["end_week"], u.get("big_idea")))
            unit_ids[u["number"]] = cur.lastrowid
            for s in u.get("standards", []):
                if s in std_ids:
                    cur.execute("INSERT OR IGNORE INTO unit_standards VALUES (?,?)",
                                (unit_ids[u["number"]], std_ids[s]))

        for w in c.get("weeks", []):
            wk = w["week"]
            cur.execute("INSERT INTO weekly_plans (course_id, unit_id, week, quarter, semester, topic,"
                        " objectives, vocabulary, materials, assessment) VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (cid, unit_ids.get(w.get("unit")), wk, (wk - 1) // 9 + 1, 1 if wk <= 18 else 2,
                         w["topic"], joinl(w.get("objectives"), "\n"), joinl(w.get("vocabulary"), ", "),
                         joinl(w.get("materials"), ", "), w.get("assessment")))
            wid = cur.lastrowid
            counts["weeks"] += 1
            for s in w.get("standards", []):
                if s in std_ids:
                    cur.execute("INSERT OR IGNORE INTO weekly_plan_standards VALUES (?,?)", (wid, std_ids[s]))
            for i, d in enumerate(w.get("days", [])[:5], start=1):
                cur.execute("INSERT INTO daily_lessons (weekly_plan_id, course_id, grade, subject_code, week,"
                            " day, day_name, school_day, title, work, minutes) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                            (wid, cid, g, subj, wk, i, DAY_NAMES[i - 1], (wk - 1) * 5 + i,
                             d["title"], d["work"], d.get("minutes", c.get("minutes_per_day"))))
                cur.execute("INSERT INTO lesson_search (grade, subject_code, week, day, course, topic, title, work)"
                            " VALUES (?,?,?,?,?,?,?,?)",
                            (g, subj, wk, i, c["title"], w["topic"], d["title"], d["work"]))
                counts["lessons"] += 1

    meta = {
        "name": "California Homeschool Curriculum Database (Grades 1–12)",
        "standards_basis": "California content standards (CA CCSS ELA & Math, CA NGSS, HSS, 2019 Arts, PE, Health, World Languages, CS)",
        "school_year": "36 weeks x 5 days = 180 instructional days",
        "built_from": "data/ (see data/SCHEMA.md)",
        **{k: str(v) for k, v in counts.items()},
    }
    cur.executemany("INSERT INTO meta VALUES (?,?)", meta.items())
    con.commit()
    cur.execute("VACUUM")
    con.close()
    return counts, len(course_files)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(ROOT / "homeschool.db"))
    args = ap.parse_args()
    counts, n = build(pathlib.Path(args.out))
    print(f"Built {args.out}: {counts['courses']} courses, {counts['weeks']} weekly plans, "
          f"{counts['lessons']} daily lessons (from {n} course files)")


if __name__ == "__main__":
    sys.exit(main())
