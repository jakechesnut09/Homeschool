# Brief for authoring one grade of curriculum

Repository: /home/user/Homeschool (a California homeschool curriculum database).
Read first: data/SCHEMA.md (exact JSON format) and data/COURSE_PLAN.md (which courses your grade has,
and the CA standards/frameworks + code formats to use).

Your job: write ONE JSON file per course for your grade at data/curriculum/grade_XX/<SUBJECT>.json.

Requirements:
- 36 weeks per course, every week has exactly 5 days (Mon–Fri), each day with a short "title" and a
  concrete "work" field (1–2 sentences of what the student actually does: the lesson, the practice,
  the product — name the specific text, skill, experiment, problem type, drill or project).
  Day 5 normally reviews/assesses the week. Never write filler like "continue practicing".
- Sequence follows a realistic CA public-school scope & sequence for that grade; cover ALL the
  grade's major CA standards across the year. Units: roughly 6–12 per course.
- Use real CA standard codes in the format given in COURSE_PLAN.md. Every code used in units/weeks
  must be defined in the file's "standards" object with a short paraphrase.
- ELA: name actual public-domain or widely available texts (library), weave reading, writing,
  phonics/word study (grades 1–3), grammar, speaking & listening through each week.
- Science: include hands-on investigations with household materials. HSS: include primary sources.
- PE/Health/VAPA can have shorter daily work but still 5 days per week.
- "resources": 3–6 FREE resources for the course with stable URLs (prefer top-level or course-level
  pages: Khan Academy, CK-12, PhET, NASA, Smithsonian Learning Lab, Library of Congress, National
  Archives/DocsTeach, Calisphere, Project Gutenberg, ReadWorks, CommonLit, Open Up Resources /
  Illustrative Mathematics, OpenStax, Mystery Science free lessons, GoNoodle, PBS LearningMedia,
  Duolingo, Code.org, etc.). Do not invent deep URLs you are not sure of; you may verify with
  `curl -s -o /dev/null -w "%{http_code}" -L <url>`.
- Write each course file separately (one Write per file) to keep files manageable. Use compact JSON
  (2-space indent is fine).
- After writing, run: python3 scripts/validate.py data/curriculum/grade_XX  and fix every failure.
- Do NOT touch other grades' directories, do not create other files, do not git commit.
- Final reply: one short paragraph — files written, validation result, anything notable. No file dumps.
