# Brief for authoring one grade's teacher's guides

Repository: /home/user/Homeschool. Read data/SCHEMA.md (section "Teacher's guides") for the exact format.

For EVERY course file in data/curriculum/grade_XX/, write the matching teacher's guide at
data/teacher/grade_XX/<SUBJECT>.json. Read each curriculum file and follow it week by week and day by
day: the guide for week N day D must teach exactly the lesson in curriculum week N day D.

Audience: a parent teaching at home, often without a teaching background. Be concrete.
- "guide": how to run the lesson — what to say/model, what the child does, how to check. 2–4 sentences.
- "questions": 1–3 check-for-understanding questions per day WITH correct, specific answers.
  Math: real problems with worked answers. ELA: text-dependent questions with model answers that
  cite the named text (if a text is long, ask about well-known events/themes you are sure of; never
  invent plot details). Science: predictions/explanations with the expected scientific answer.
  HSS: factual and analytical questions with accurate answers. Spanish: prompts with the correct
  Spanish. PE/Health/VAPA: cue checks, safety and concept questions with answers.
- "misconceptions": 1–3 common errors for the week and how to correct them.
- "assessment_key": the answer key or rubric for that week's curriculum "assessment" — give actual
  answers (e.g. "1) 24 2) 35 …" for a quiz you specify, or a 3–4 level rubric with what a proficient
  answer contains for writing/projects).
- "prep": materials to gather and anything to read or preview first (and parental-preview notes for
  sensitive health or mature literature content).
Accuracy matters more than length: every answer must be correct.

Method: generate with a Python script in your scratchpad (one course at a time, write the JSON file,
then move on). Validate with: python3 scripts/validate_teacher.py data/teacher/grade_XX
Do NOT edit data/curriculum or any other grade, do not commit. Final reply: one short paragraph.
