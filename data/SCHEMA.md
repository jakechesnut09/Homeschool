# Source-data schema

All curriculum content lives in JSON under `data/`. `scripts/build_db.py` compiles it
into the SQLite database `homeschool.db`. Run `python3 scripts/validate.py` after editing.

## Curriculum course files — `data/curriculum/grade_XX/<SUBJECT>.json`

One file per course (one course per subject per grade). `XX` is the two-digit grade (`01`–`12`).

Subject codes:

| Code    | Subject                                   |
|---------|-------------------------------------------|
| ELA     | English Language Arts                     |
| MATH    | Mathematics                               |
| SCI     | Science                                   |
| HSS     | History–Social Science                    |
| VAPA    | Visual & Performing Arts                  |
| PE      | Physical Education                        |
| HEALTH  | Health Education (grade 10: Driver Ed / First Aid) |
| WL      | World Language (Spanish)                  |
| ELEC    | Elective (CS, CTE, Personal Finance …)    |

```jsonc
{
  "grade": 3,
  "subject": "MATH",
  "title": "Mathematics 3",
  "description": "2–4 sentence course overview.",
  "framework": "California Common Core State Standards for Mathematics; 2023 CA Mathematics Framework",
  "minutes_per_day": 60,
  "ag_requirement": null,          // HS only: UC/CSU a–g letter, e.g. "c"
  "credits": null,                 // HS only: e.g. 10 (CA semester-unit convention: 5 per semester)
  "standards": {                   // EVERY code used below must be defined here
    "3.OA.A.1": "Interpret products of whole numbers ..."
  },
  "resources": [                   // free, course-specific resources
    {"name": "Khan Academy – 3rd grade math", "url": "https://www.khanacademy.org/math/cc-third-grade-math", "note": "Video + practice for every unit"}
  ],
  "units": [
    {"number": 1, "title": "Multiplication Concepts", "start_week": 1, "end_week": 4,
     "big_idea": "Multiplication is repeated equal groups.", "standards": ["3.OA.A.1"]}
  ],
  "weeks": [                       // exactly 36, week 1..36, each inside its unit's range
    {
      "week": 1,
      "unit": 1,
      "topic": "Equal groups and arrays",
      "objectives": ["Model multiplication as equal groups", "Write multiplication sentences for arrays"],
      "standards": ["3.OA.A.1"],
      "vocabulary": ["factor", "product", "array"],
      "materials": ["counters", "grid paper"],
      "days": [                    // exactly 5: Mon..Fri
        {"title": "Equal groups", "work": "What the student does today (1–2 concrete sentences: teach, practice, produce)."},
        {"title": "...", "work": "..."},
        {"title": "...", "work": "..."},
        {"title": "...", "work": "..."},
        {"title": "Review & check", "work": "..."}
      ],
      "assessment": "How mastery is checked this week."
    }
  ]
}
```

## Reference files — `data/reference/*.json`

* `resources.json` – free curriculum resources (`name, provider, url, type, subjects[], grade_min, grade_max, cost, description`)
* `funding.json` – grants, funded programs, tax-advantaged accounts, discounts (`name, category, provider, url, eligibility, benefit, how_to_apply, california_notes, last_verified`)
* `paperwork.json` – required / recommended documents (`name, homeschool_option, action (submit|keep_on_file|recommended), frequency, deadline, legal_basis, url, description`)
* `legal_options.json` – the legal ways to homeschool in California (`code, name, description, requirements[], pros[], cons[], legal_basis, url`)

## Teacher's guides — `data/teacher/grade_XX/<SUBJECT>.json`

One file per course, matching `data/curriculum/grade_XX/<SUBJECT>.json` week for week and day for day.

```jsonc
{
  "grade": 3,
  "subject": "MATH",
  "overview": "2–4 sentences for the parent-teacher: how the course is taught, pacing, what to emphasize.",
  "weeks": [                              // exactly 36, matching the curriculum weeks
    {
      "week": 1,
      "prep": "What to gather / read / set up before the week starts.",
      "misconceptions": ["Common mistake and how to correct it"],      // 1–3
      "days": [                           // exactly 5, matching the curriculum days
        {
          "guide": "Step-by-step how to teach today's lesson (2–4 sentences: model, guided practice, independent).",
          "questions": [                  // 1–3 check-for-understanding questions WITH answers
            {"q": "What is 4 × 6? Draw it as an array.", "a": "24 — 4 rows of 6 dots."}
          ]
        }
      ],
      "assessment_key": "Answer key / scoring rubric for the week's assessment, with the actual expected answers."
    }
  ]
}
```
