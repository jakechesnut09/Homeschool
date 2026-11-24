# California Homeschool Curriculum Database (Grades 1–12)

A complete, standards-aligned homeschool curriculum for **1st through 12th grade**, built on
**California content standards**. It includes:

- **Day-by-day lesson plans** for every subject. Each grade has a 36-week year, and every week has
  5 school days (180 days, more than the 175 days used by CA public schools).
- **Free online resources**, both general ones and ones attached to each course.
- **Grants, funding programs and financial aid** available to California homeschoolers.
- **Legal paperwork:** what to file, what to keep on file, and the legal basis for each, for every
  legal way to homeschool in California.

**At a glance:** 90 courses · 830 units · 3,240 weekly plans · 16,200 daily lessons · 3,067 CA standards referenced · 315 free resources · 26 funding programs · 26 paperwork items.

Everything is in one SQLite file, **`homeschool.db`**. The same plans are also exported as
readable Markdown in **[`docs/plans/`](docs/plans/README.md)**, so you can browse them on GitHub without any software.

> **Not legal or tax advice.** The paperwork and funding data was checked against official sources
> in November 2026 (see `last_verified`), but laws and programs change. Confirm details with the
> [CDE Private Schools office](https://www.cde.ca.gov/sp/ps/), your charter or PSP, or a tax adviser.

---

## Quick start

No installation is needed beyond Python 3.

```bash
# Print a full week (all subjects, Monday–Friday) for a grade
python3 scripts/plan.py week --grade 3 --week 5

# A single day's checklist
python3 scripts/plan.py day --grade 3 --week 5 --day 2

# Course overview: units, weekly topics, free resources, standards
python3 scripts/plan.py course --grade 9 --subject MATH

# Full-text search across every lesson
python3 scripts/plan.py search "fractions"
python3 scripts/plan.py search "gold rush" --grade 4

# Legal paperwork, funding and resources
python3 scripts/plan.py paperwork --option PSA      # PSA | PSP | CHARTER | TUTOR | DISTRICT_IS
python3 scripts/plan.py funding
python3 scripts/plan.py resources --grade 6 --subject SCI

# Regenerate the Markdown in docs/plans/
python3 scripts/plan.py export
```

You can also open `homeschool.db` in a SQLite viewer such as [DB Browser for SQLite](https://sqlitebrowser.org/)
(free) or [Datasette](https://datasette.io/).

## Web app

`web/` is a browsable version of the whole curriculum: grades → courses → units → weeks → days, plus
search, paperwork, funding and resources. Every page links back to its source files in this repository.

```bash
python3 scripts/build_web.py            # regenerate web/data/*.json and web/index.html
cd web && python3 -m http.server 8000   # open http://localhost:8000
```

### Publishing it as a public website (GitHub Pages)

The workflow in `.github/workflows/pages.yml` rebuilds the app and publishes `web/` every time `main`
changes. One-time setup:

1. GitHub Pages needs either a **public repository** or a paid GitHub plan (Pro, Team or Enterprise)
   for a private one. To make this repository public: **Settings → General → Danger Zone → Change
   visibility**.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
3. Run the workflow once: **Actions → Deploy web app to GitHub Pages → Run workflow** (or push to `main`).

The site will be at **https://jakechesnut09.github.io/Homeschool/**. The app's "on GitHub" buttons
point at the repository's `main` branch, so visitors can open them only if the repository is public.

## What each grade covers

Every course runs 36 weeks, organized into units. Each week has a topic, objectives, CA standards,
vocabulary, materials and an assessment, plus five daily lessons.

| Grade | Courses |
|---|---|
| 1 | ELA · Math · Science (NGSS) · HSS: *A Child's Place in Time and Space* · Art & Music · PE · Health |
| 2 | ELA · Math · Science · HSS: *People Who Make a Difference* · Art & Music · PE · Health |
| 3 | ELA · Math · Science · HSS: *Continuity and Change* · Art & Music · PE · Health |
| 4 | ELA · Math · Science · HSS: *California, A Changing State* · Art & Music · PE · Health |
| 5 | ELA · Math · Science · HSS: *U.S. History, Making a New Nation* · Art & Music · PE · Health |
| 6 | ELA · Math · Integrated Science · HSS: *Ancient Civilizations* · VAPA · PE · Health |
| 7 | ELA · Math · Integrated Science · HSS: *Medieval & Early Modern Times* · VAPA · PE · Health · Spanish 1A |
| 8 | ELA · Math · Integrated Science · HSS: *U.S. History, Growth and Conflict* · VAPA · PE · Health · Spanish 1B |
| 9 | English 9 · Algebra I · Biology (The Living Earth) · World Geography / Ethnic Studies · Spanish II · Visual Art I · PE · Health & Wellness |
| 10 | English 10 · Geometry · Chemistry in the Earth System · Modern World History · Spanish III · Music & Media Arts · PE · Driver Ed / First Aid & CPR · Computer Science Principles |
| 11 | English 11 (American Lit) · Algebra II · Physics of the Universe · U.S. History · Spanish IV · Theatre · Lifetime Fitness · Intro to Engineering Design (CTE) |
| 12 | English 12 + Senior Research · Precalculus with Statistics · Earth/Space & Environmental Science · Government (S1) / Economics (S2) · Advanced Art & Portfolio · Lifetime Fitness II · Personal Finance / College & Career Readiness |

The subjects cover the branches of study in **CA Education Code §51210** (grades 1–6) and
**§51220** (grades 7–12). The high school sequence meets or exceeds the CA public-school
graduation requirements in Ed Code §51225.3 and the **UC/CSU a–g** subject pattern. It provides:

- 4 years of English
- 4 years of math (Algebra I through Precalculus)
- 4 years of lab science
- 4 years of social science (geography and ethnic studies, world history, U.S. history,
  government and economics)
- 3 years of Spanish in high school, after Spanish I in grades 7–8
- 4 years of arts
- PE every year

Each high school course in the database records its a–g area and credits. Home-based private
schools set their own graduation requirements, so these are guidelines rather than mandates.

### Standards used

| Subject | California standards / framework |
|---|---|
| ELA | CA Common Core State Standards for ELA/Literacy; 2014 ELA/ELD Framework |
| Math | CA CCSS for Mathematics; 2023 CA Mathematics Framework |
| Science | CA Next Generation Science Standards; 2016 CA Science Framework (integrated middle school; *Living Earth / Chemistry in the Earth System / Physics of the Universe* in high school) |
| History–Social Science | CA HSS Content Standards; 2016 HSS Framework; 2021 Ethnic Studies Model Curriculum |
| Visual & Performing Arts | 2019 CA Arts Standards (visual arts, music, theatre, dance, media arts) |
| PE | CA Physical Education Model Content Standards |
| Health | 2008 CA Health Education Content Standards |
| World Language | 2019 CA World Languages Standards |
| Electives | CA K-12 Computer Science Standards; CA CTE Model Curriculum Standards; personal finance (AB 2927 topics) |

Some standard codes are shortened or prefixed so they stay unique in the database: Health `H-…`,
PE `PE-…`, World Language `WL-…`, Government `GOV-12.x` and Economics `ECON-12.x`. For PE and
Health, the codes follow the structure of the official documents and the descriptions are
paraphrases. Check the official text when exact wording matters.

## Homeschooling legally in California

The `legal_options` table compares the five legal routes:

1. **Private School Affidavit (PSA):** run your own home-based private school.
2. **Private School Satellite Program (PSP)**
3. **Charter school independent study:** these programs often come with instructional funds.
4. **Credentialed private tutor**
5. **District independent study**

The `paperwork` table lists every document to **submit**, **keep on file**, or keep as
**recommended** practice, with the deadline and the Education Code or Health & Safety Code
section behind it. Highlights:

- **PSA:** file online with CDE each year. The legal window is **Oct 1–15**; the online system is
  open Aug 1–Jun 30 so families who start mid-year can file when they begin.
- **Keep on file:**
  - attendance register
  - courses of study
  - faculty names, addresses and qualifications
  - immunization records or exemption status (home-based private schools are exempt under
    H&S §120335(f))
  - transcripts and diploma records

The `funding_programs` table covers:

- charter school instructional funds
- HSLDA / Homeschool Foundation grants
- the 2025 federal 529 expansion, including California's non-conformity
- Coverdell ESAs
- the federal tax-credit scholarship starting in 2027 (California's opt-in status)
- community college dual enrollment fee waivers
- park passes and museum/library passes
- educator discounts
- Cal Grant and FAFSA / CA Dream Act eligibility for homeschool graduates

## Database layout

| Table / view | Contents |
|---|---|
| `grades`, `subjects` | 12 grades; 9 subject codes (ELA, MATH, SCI, HSS, WL, VAPA, PE, HEALTH, ELEC) with their Ed Code basis |
| `courses` | One course per subject per grade: description, framework, minutes/day, a–g area, credits |
| `units` | Units within each course and the weeks they span |
| `weekly_plans` | 36 per course: topic, objectives, vocabulary, materials, assessment, quarter and semester |
| `daily_lessons` | 5 per week: day name, school day (1–180), lesson title, the student's work, minutes |
| `standards` + `unit_standards`, `weekly_plan_standards` | CA standard codes and descriptions, linked to units and weeks |
| `resources`, `resource_subjects`, `course_resources` | Free resources: general ones and course-specific ones |
| `legal_options`, `paperwork`, `funding_programs` | Legal and financial reference data |
| `lesson_search` | Full-text (FTS5) index of all lessons |
| `v_daily_plan` | One row per subject per day, ready to print as a schedule |
| `v_weekly_overview` | Weekly topics with the standards they cover |
| `v_course_catalog`, `v_hs_course_plan`, `v_daily_minutes` | Course catalog, high school transcript plan, daily instructional minutes |

### Example queries

```sql
-- Monday of week 1 for a 5th grader
SELECT course, lesson_title, work, minutes
FROM v_daily_plan WHERE grade = 5 AND week = 1 AND day = 1 ORDER BY subject_order;

-- Which weeks of 8th grade math cover standard 8.EE.C.8?
SELECT w.week, w.topic FROM weekly_plans w
JOIN weekly_plan_standards ws ON ws.weekly_plan_id = w.id
JOIN standards s ON s.id = ws.standard_id
JOIN courses c ON c.id = w.course_id
WHERE c.grade = 8 AND c.subject_code = 'MATH' AND s.code = '8.EE.C.8';

-- Courses for a high school transcript
SELECT * FROM v_hs_course_plan;

-- Free science resources suitable for a 4th grader
SELECT r.name, r.url FROM resources r JOIN resource_subjects rs ON rs.resource_id = r.id
WHERE rs.subject_code IN ('SCI','ALL') AND coalesce(r.grade_min,1) <= 4 AND coalesce(r.grade_max,12) >= 4;
```

## Editing the curriculum

The database is generated from human-editable JSON. Do not edit `homeschool.db` directly.

```
data/
  curriculum/grade_01 … grade_12/<SUBJECT>.json   # one file per course (units, weeks, days)
  reference/resources.json  funding.json  paperwork.json  legal_options.json
  SCHEMA.md        # JSON format
  COURSE_PLAN.md   # course list and standards conventions per grade
scripts/
  validate.py      # checks: 36 weeks, 5 days each, all standard codes defined
  build_db.py      # JSON → homeschool.db
  plan.py          # CLI viewer, search, Markdown export
  build_web.py     # JSON → web/data for the web app
web/
  app.html         # the web app (edit this)
  index.html       # generated full page for static hosting
  data/            # generated JSON
```

After editing, run:

```bash
python3 scripts/validate.py && python3 scripts/build_db.py && python3 scripts/plan.py export && python3 scripts/build_web.py
```

## Tips for using the plans

- **Pacing:** daily minutes are typical classroom estimates. One-on-one instruction usually takes
  less time.
- **Adjusting:** skip, combine or stretch weeks as needed. The weekly assessment tells you whether
  the student is ready to move on.
- **Records:** printing `plan.py week` output each week and checking off the lessons gives you
  both an attendance record and a course-of-study record for your files.
- **Mature content:**
  - Some high school literature and history lessons deal with mature themes (war, the Holocaust,
    slavery), so preview them first.
  - The grade 7–9 health courses include sexual health content aligned to the CA Healthy Youth
    Act. That content is the parent's choice; skip or replace those days as you see fit.
- **Links:** resource links were checked in November 2026. A few major sites (Library of Congress,
  Smithsonian Learning Lab, Project Gutenberg) block automated link checks but work in a browser.
