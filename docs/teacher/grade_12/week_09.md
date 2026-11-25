# Teacher's Guide — 12th Grade, Week 9

## English 12 – World & British Literature + Senior Research: Macbeth Acts II–III – murder and guilt

**Prepare:** Read Acts II–III. Select a filmed production (e.g., the 2010 Patrick Stewart PBS version or the 1979 Ian McKellen/Judi Dench version) and preview the banquet scene. Make a motif tracker chart (blood, sleep, darkness).

**Watch for:**
- Treating the Porter scene as irrelevant comedy. It is comic relief that also echoes damnation and equivocation.
- Quotations dropped without commentary. Every quotation needs explanation.
- Assuming Macbeth always hesitates. After Duncan, he plans Banquo's murder alone.

### Day 1 (Monday): The dagger
*Student:* Read II.1–II.2. Analyze the dagger soliloquy and the 'sleep no more' exchange; start a motif tracker for blood, sleep, and darkness.

*How to teach:* Read II.1–II.2. The student starts the motif tracker. Before moving on, have the student answer the check questions below without notes, then compare with the answers and reteach anything missed.

- **Q:** What does the dagger represent?
  **A:** A 'dagger of the mind' — his guilty, overheated imagination drawing him toward murder.
- **Q:** What does Macbeth hear after the murder?
  **A:** A voice crying 'Sleep no more! Macbeth does murder sleep.'

### Day 2 (Tuesday): The porter and discovery
*Student:* Read II.3–II.4. Explain the comic relief of the Porter scene and how unnatural events in nature reflect the murder.

*How to teach:* Read II.3–II.4. Explain comic relief and unnatural events. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** What unnatural events follow Duncan's murder?
  **A:** Darkness by day, an owl killing a falcon, Duncan's horses eating each other.

### Day 3 (Wednesday): Banquo's fear
*Student:* Read III.1–III.2. Compare Macbeth's reasoning for killing Banquo with his earlier hesitation about Duncan; write a paragraph citing two quotations.

*How to teach:* Read III.1–III.2. The student writes a paragraph comparing Macbeth's reasoning. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** Why does Macbeth want Banquo dead?
  **A:** Banquo suspects him, and the witches said Banquo's descendants would be kings — Macbeth's crown is 'fruitless' and his sceptre 'barren.'

### Day 4 (Thursday): The banquet
*Student:* Read III.3–III.6. Watch the banquet scene in one filmed production and discuss how staging the ghost (visible or invisible) changes meaning.

*How to teach:* Read III.3–III.6; watch the banquet scene. Discuss staging the ghost. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** Who escapes the murderers?
  **A:** Fleance, Banquo's son.

### Day 5 (Friday): Motif paragraph
*Student:* Write a 400-word analytical paragraph tracing one motif through Acts I–III with at least four embedded quotations.

*How to teach:* The student writes a 400-word motif paragraph with four quotations. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** Give a blood quotation from Act II.
  **A:** 'Will all great Neptune's ocean wash this blood / Clean from my hand?' (II.2)

**Assessment:** Motif analysis paragraph scored on evidence and commentary.

**Answer key:** Motif paragraph rubric (4 = exemplary, 3 = proficient, 2 = developing, 1 = beginning): 4 = topic sentence claims how the motif develops (e.g., blood shifts from honor to guilt), 4+ quotations with act/scene/line, commentary after each, progression across acts. Proficient: 3+ quotations, clear commentary.

## Precalculus with Statistics: Solving exponential and logarithmic equations; modeling

**Prepare:** Gather a mug, hot (not boiling) water, a kitchen or digital thermometer, and a timer for the cooling lab — supervise hot water. Preview OpenStax 6.6–6.7. Record room temperature before starting.

**Watch for:**
- Taking the log of only one side or of individual terms. Isolate the exponential first, then take the log of both sides.
- Keeping extraneous log solutions. Every answer must make each log's argument positive in the original equation.
- Fitting the cooling data with y = ab^t, which ignores room temperature. Newton's model is T(t) = T_room + (T₀ − T_room)e^(−kt); the curve levels off at room temperature, not 0.

### Day 1 (Monday): Solving equations
*Student:* Solve 12 exponential and logarithmic equations, checking for extraneous solutions.

*How to teach:* Model solving 5e^(2x) = 40: divide, take ln, solve. Then a log equation with a check. The student solves 12 equations. Before moving on, have the student answer the check questions below without notes, then compare with the answers and reteach anything missed.

- **Q:** Solve 5e^(2x) = 40.
  **A:** e^(2x) = 8 → x = ln 8 / 2 ≈ 1.040.
- **Q:** Solve log₂ x + log₂(x − 2) = 3.
  **A:** log₂(x(x − 2)) = 3 → x² − 2x − 8 = 0 → x = 4 or −2. Reject −2 (negative argument). x = 4.

### Day 2 (Tuesday): Half-life and doubling
*Student:* Solve half-life (carbon-14) and doubling-time (population, investment) problems with logarithms.

*How to teach:* Set up A = A₀(1/2)^(t/h) for half-life and solve for t with logs. Do doubling time for continuous growth: t = ln 2 / r. Before moving on, have the student answer the check questions below without notes, then compare with the answers and reteach anything missed.

- **Q:** Carbon-14 has half-life 5730 years. How old is a sample with 30% of its C-14 remaining?
  **A:** 0.3 = (1/2)^(t/5730) → t = 5730·ln 0.3 / ln 0.5 ≈ 9950 years.
- **Q:** How long to double money at 7% compounded continuously?
  **A:** t = ln 2 / 0.07 ≈ 9.9 years.

### Day 3 (Wednesday): Cooling lab
*Student:* Measure the temperature of a cup of hot water every 2 minutes for 30 minutes and record data for Newton's Law of Cooling.

*How to teach:* Pour hot water, insert the thermometer, and record temperature every 2 minutes for 30 minutes along with room temperature. The student keeps a neat data table and notes sources of error.

- **Q:** Predict the shape of the temperature graph and its long-run value.
  **A:** Decreasing quickly at first, then more slowly, leveling off toward room temperature (a horizontal asymptote at T_room).

### Day 4 (Thursday): Fit the model
*Student:* Fit an exponential model to the cooling data in Desmos, interpret parameters, and predict when it reaches 40 °C.

*How to teach:* Enter the data in Desmos and fit T = R + (T₀ − R)e^(−kt) with R fixed at room temperature (or y₁ ~ a·e^(−kx₁) + R). Interpret k and solve for when T = 40 °C.

- **Q:** Room 20 °C, start 90 °C, 60 °C after 10 min. Find k and when it reaches 40 °C.
  **A:** 40 = 70e^(−10k) → k = ln(70/40)/10 ≈ 0.0560 per minute. 20 = 70e^(−0.056t) → t = ln 3.5 / 0.056 ≈ 22.4 minutes.

### Day 5 (Friday): Unit 3 test
*Student:* Take the Unit 3 test on exponential and logarithmic functions.

*How to teach:* Give the Unit 3 test; collect the cooling-lab report. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** Solve 3^(x + 1) = 27.
  **A:** 3^(x + 1) = 3³ → x = 2.

**Assessment:** Unit 3 test and cooling-lab report.

**Answer key:** Unit 3 test sample key: 1) 3^(x+1) = 27 → x = 2. 2) 5e^(2x) = 40 → x ≈ 1.040. 3) log₂x + log₂(x − 2) = 3 → x = 4. 4) 30% C-14 → ≈ 9950 years. 5) Doubling at 7% continuous ≈ 9.9 years. 6) log₅ 20 ≈ 1.861. 7) Graph of log₂(x − 1): VA x = 1, passes (2, 0), (3, 1). Lab report rubric (4 levels): 4 = complete data table, graph, correct Newton model with fitted k and units, prediction for 40 °C, discussion of error sources; 3 = model and prediction correct, minor gaps; 2 = data present but model ignores room temperature or is misinterpreted; 1 = incomplete.

## Earth & Space / Environmental Science: Plate boundaries and California landforms

**Prepare:** Graham crackers, frosting, wax paper. Download the USGS 'latest earthquakes' list (M4.5+ past 30 days). Wallace Creek images (offset ~130 m over ~3,700 years). California geomorphic provinces map.

**Watch for:**
- Thinking the San Andreas is a subduction zone or that California will 'fall into the ocean.' It is a transform boundary; plates slide past horizontally.
- Believing all mountains form from collisions. The Sierra Nevada is a tilted fault block uplifted along its eastern side.
- Assuming earthquakes happen randomly. Most occur along plate boundaries.

### Day 1 (Monday): Boundary models
*Student:* Model divergent, convergent, and transform boundaries with graham crackers on frosting; record landforms each produces.

*How to teach:* On frosting ('asthenosphere'), push crackers apart (divergent: rift/ridge), together (convergent: one dips under — subduction — or they crumple — mountains), and slide past (transform: offset).

- **Q:** Match each boundary to a landform: Mid-Atlantic Ridge, Andes, San Andreas.
  **A:** Mid-Atlantic Ridge — divergent; Andes — convergent (ocean–continent subduction); San Andreas — transform.

### Day 2 (Tuesday): Global patterns
*Student:* Plot the last 30 days of M4.5+ earthquakes from USGS on a world map and outline plate boundaries.

*How to teach:* Plot 30 days of M4.5+ earthquakes on a world map; outline plate boundaries.

- **Q:** Where do earthquakes cluster?
  **A:** Along plate boundaries — especially the Pacific 'Ring of Fire,' mid-ocean ridges, and the Himalayan collision zone.

### Day 3 (Wednesday): San Andreas
*Student:* Study the San Andreas transform fault and measure offset features (e.g., Wallace Creek) to calculate slip rate.

*How to teach:* Study Wallace Creek: the channel is offset ~130 m by the San Andreas over ~3,700 years. Calculate slip rate.

- **Q:** Calculate the slip rate at Wallace Creek.
  **A:** 130 m ÷ 3,700 yr ≈ 0.035 m/yr = 35 mm/yr (about 3.5 cm/yr).

### Day 4 (Thursday): Cascadia & mountains
*Student:* Compare Cascadia subduction (Mt. Shasta, Lassen) with the Sierra Nevada's uplift; map California's landforms by process.

*How to teach:* Compare Cascadia subduction (Gorda/Juan de Fuca Plate under North America; Mt. Shasta, Lassen Peak volcanoes) with Sierra Nevada fault-block uplift; map CA landforms by process.

- **Q:** Why are there volcanoes in far northern California but not along the San Andreas?
  **A:** Northern California sits above the Cascadia subduction zone, where the sinking plate releases water that melts the mantle; the transform San Andreas has no subduction to generate magma.

### Day 5 (Friday): Check
*Student:* Draw an annotated California cross-section from the Pacific to Nevada showing plate processes; take a quiz.

*How to teach:* Student draws an annotated cross-section from the Pacific to Nevada (Pacific Plate, San Andreas, Coast Ranges, Great Valley, Sierra Nevada, Basin and Range); quiz.

- **Q:** What process is stretching Nevada into the Basin and Range?
  **A:** Crustal extension (stretching) producing normal faults with alternating ranges and basins.

**Assessment:** Annotated California cross-section.

**Answer key:** Annotated California cross-section rubric. 4 – Correct west-to-east order (Pacific Plate, San Andreas transform, Coast Ranges/Franciscan, Great Valley, Sierra Nevada batholith/tilted block, eastern Sierra fault, Basin and Range extension), arrows for plate motion, annotations explaining processes, Cascadia noted for northern CA. 3 (proficient) – Correct order and processes. 2 – Some misplacements. 1 – Inaccurate. Quiz key: divergent/convergent/transform; slip ~35 mm/yr; Shasta and Lassen = Cascade volcanoes.

## American Government & Civics (S1) / Economics (S2): Judicial review and federal power

**Prepare:** Open Oyez summaries for Marbury v. Madison (1803), McCulloch v. Maryland (1819), and United States v. Nixon (1974). Print short essays on originalism and living constitutionalism (e.g., National Constitution Center).

**Watch for:**
- Thinking judicial review is written in the Constitution. Marshall inferred it in Marbury.
- Reading McCulloch as letting Congress do anything. It allows implied powers connected to enumerated ones.
- Equating judicial 'activism' with a political side. Both liberal and conservative courts strike down laws.

### Day 1 (Monday): Marbury v. Madison
*Student:* Read excerpts of Marshall's opinion and explain how the Court established judicial review.

*How to teach:* Read Marshall's key lines ('It is emphatically the province and duty of the judicial department to say what the law is'). The student explains the case's logic step by step.

- **Q:** What did Marbury v. Madison establish?
  **A:** Judicial review — courts can strike down laws that conflict with the Constitution; part of the Judiciary Act of 1789 was void.
- **Q:** Why was the ruling politically clever?
  **A:** Marshall denied Marbury his commission (avoiding a clash with Jefferson) while claiming a major power for the Court.

### Day 2 (Tuesday): McCulloch v. Maryland
*Student:* Analyze 'the power to tax involves the power to destroy' and how McCulloch expanded federal power.

*How to teach:* Analyze McCulloch. The student explains both holdings. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** What were McCulloch's two holdings?
  **A:** Congress could create a national bank under the Necessary and Proper Clause (implied powers); Maryland could not tax it, because 'the power to tax involves the power to destroy' and federal law is supreme.

### Day 3 (Wednesday): U.S. v. Nixon
*Student:* Listen to Oyez audio excerpts and explain how the case limited executive privilege.

*How to teach:* Listen to Oyez audio excerpts of Nixon. The student explains limits on executive privilege. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** What did U.S. v. Nixon decide?
  **A:** Unanimously (8–0), that executive privilege is not absolute; Nixon had to turn over the Watergate tapes. He resigned soon after.

### Day 4 (Thursday): Activism vs. restraint
*Student:* Read short essays on judicial philosophy (originalism, living constitution) and apply each to one case.

*How to teach:* Read the philosophy essays; the student applies each to one case. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** Define originalism.
  **A:** Interpreting the Constitution according to its original public meaning when adopted.

### Day 5 (Friday): Check
*Student:* Write a 500-word analysis of how one case strengthened checks and balances.

*How to teach:* The student writes a 500-word case analysis. Before moving on, have the student answer the check question below without notes, then compare with the answer and reteach anything missed.

- **Q:** How did Nixon strengthen checks and balances?
  **A:** It showed no president is above the law and the judiciary can check the executive.

**Assessment:** Case analysis essay.

**Answer key:** Case analysis rubric (4 = exemplary, 3 = proficient, 2 = developing, 1 = beginning): 4 = accurate facts, question, holding, reasoning; clear explanation of effect on checks and balances; evidence from the opinion; 500 words.

## Advanced Art & Portfolio: Painting from life

**Prepare:** Acrylic or oil paints (if oil, use odorless mineral spirits with ventilation or water-mixable oils), canvas or panel, brushes, palette knife. Set up a still life with strong light that stays the same all week (mark object positions with tape).

**Watch for:**
- Starting with details. Work from large shapes to small, dark to light (in oils) or big masses first.
- Overmixing on the canvas, leading to mud. Mix on the palette and place strokes deliberately.
- Glazing in thick paint. Glazes are thin, transparent layers over dry paint.

### Day 1 (Monday): Underpainting
*Student:* Tone a canvas and block in a still life with a monochrome underpainting.

*How to teach:* Tone the canvas with a mid-value wash (e.g., burnt sienna); block in a monochrome underpainting of shapes and shadows.

- **Q:** Why tone the canvas first?
  **A:** It removes the intimidating white and gives a middle value so you can judge lights and darks more accurately.

### Day 2 (Tuesday): Block-in
*Student:* Block in large color shapes, focusing on value relationships.

*How to teach:* Block in large color shapes focusing on value relationships.

- **Q:** What is a block-in?
  **A:** Laying in the large, simplified shapes of color and value before refining.

### Day 3 (Wednesday): Develop
*Student:* Develop forms and edges; use glazing or impasto deliberately.

*How to teach:* Develop forms and edges; use glazing or impasto deliberately.

- **Q:** Define glazing and impasto.
  **A:** Glazing: thin transparent layers over dry paint to modify color. Impasto: thick, textured paint application.

### Day 4 (Thursday): Finish
*Student:* Add final details and highlights.

*How to teach:* Final details and highlights.

- **Q:** Why save highlights for last?
  **A:** They're the lightest, most specific accents; placing them last keeps them clean and crisp.

### Day 5 (Friday): Reflect
*Student:* Write a reflection on your painting process and photograph the work.

*How to teach:* Reflect on process; photograph.

- **Q:** What does 'fat over lean' mean in oil painting?
  **A:** Each upper layer should contain more oil (be more flexible) than the layer beneath it to prevent cracking.

**Assessment:** Observational painting.

**Answer key:** Observational painting rubric. 4 – Accurate drawing and proportions, strong value structure, convincing color and light, intentional edges and paint handling (glazing/impasto), finished surface, reflective process writing. 3 (proficient) – Accurate values and color, finished painting, reflection. 2 – Weak value structure or unfinished. 1 – Incomplete.

## Lifetime Fitness II: Aerobic training principles

**Prepare:** Running shoes, watch. Locate a 400 m track (1 lap) or measure 400 m on a path. Bike or pool for cross-training.

**Watch for:**
- Thinking aerobic and anaerobic systems switch on and off. They work together; intensity and duration change which dominates.
- Running every run fast. Most training should be easy.
- Believing VO2 max can't be improved. Training can raise it, especially in less-trained people.

### Day 1 (Monday): Energy systems
*Student:* Learn aerobic vs. anaerobic systems; do an easy 25-minute run.

*How to teach:* Teach aerobic (with oxygen, long duration) vs. anaerobic (without enough oxygen, short high intensity, causes rapid fatigue). Define VO2 max. Easy 25-minute run.

- **Q:** What is VO2 max?
  **A:** The maximum rate at which the body can take in and use oxygen during intense exercise — a key measure of aerobic fitness.

### Day 2 (Tuesday): Intervals
*Student:* Do 6 × 400 m intervals with 90-second recoveries.

*How to teach:* 6 × 400 m at a hard but controlled effort with 90-second recoveries; record each split.

- **Q:** Which energy system mainly fuels a hard 400 m (about 60–100 s)?
  **A:** Anaerobic glycolysis (with significant aerobic contribution).

### Day 3 (Wednesday): Cross-train
*Student:* Do 30 minutes of cycling or swimming.

*How to teach:* 30 minutes cycling or swimming.

- **Q:** How does cross-training help runners?
  **A:** Builds aerobic fitness with less impact, reducing overuse injury risk.

### Day 4 (Thursday): Tempo
*Student:* Run 20 minutes at comfortably hard tempo pace.

*How to teach:* 20-minute tempo run at 'comfortably hard' (RPE ~7).

- **Q:** What is the purpose of tempo runs?
  **A:** To improve the ability to sustain faster paces by raising the lactate threshold.

### Day 5 (Friday): Plan
*Student:* Write a 5K training plan for the next 4 weeks.

*How to teach:* Write a 4-week 5K plan: 3–4 runs/week (easy, interval/tempo, long), cross-training, strength, rest; increase weekly volume no more than ~10%.

- **Q:** What is the 10% rule?
  **A:** A guideline to increase weekly running volume by no more than about 10% to reduce injury risk.

**Assessment:** 5K training plan.

**Answer key:** 5K training plan rubric. 4 – 4 weeks; includes easy runs, one quality session (intervals or tempo), long run, cross-training, strength, rest; gradual increases (~10%); taper in the final week; target paces from data. 3 (proficient) – Balanced weekly structure with progression and taper. 2 – All hard or no progression. 1 – Incomplete.

## Personal Finance (S1) & College/Career Readiness (S2): Managing debt & student loans

**Prepare:** Open StudentAid.gov loan types page and the Loan Simulator. Build a sample four-debt portfolio (e.g. card A $1,500 at 24%, card B $800 at 18%, car $6,000 at 7%, student loan $10,000 at 5%). Prepare the Unit 3 test.

**Watch for:**
- Thinking all student loans are the same. Subsidized loans don't charge interest while in school (for undergrads with need); unsubsidized loans accrue interest from disbursement.
- Choosing snowball vs. avalanche as right or wrong. Avalanche (highest rate first) saves the most interest; snowball (smallest balance first) gives quick wins that may keep people motivated.
- Thinking student loans go away in bankruptcy. They are very difficult to discharge; default leads to collections, wage garnishment and tax refund seizure.

### Day 1 (Monday): Student loan basics
*Student:* Read the StudentAid.gov loan types page and make a comparison chart of Direct Subsidized, Unsubsidized, PLUS, and private loans.

*How to teach:* Make a chart: Direct Subsidized (undergrad, need-based, government pays interest in school), Direct Unsubsidized (any student, interest accrues), PLUS (parents/grad students, credit check, higher rate), private loans (credit-based, fewer protections).

- **Q:** What's the difference between subsidized and unsubsidized loans?
  **A:** With subsidized loans the government pays the interest while you're in school at least half-time; unsubsidized loans accrue interest from the start.
- **Q:** Why borrow federal before private loans?
  **A:** Federal loans have fixed rates, income-driven repayment, deferment and forgiveness options that private loans usually lack.

### Day 2 (Tuesday): Loan Simulator
*Student:* Use the StudentAid.gov Loan Simulator to estimate monthly payments on $27,000 under standard and income-driven plans.

*How to teach:* Use the Loan Simulator for $27,000 under standard (10-year) and income-driven plans. Example at 6.39%: standard payment ≈ $305/month, total interest ≈ $9,600.

- **Q:** What is the advantage and disadvantage of an income-driven plan?
  **A:** Advantage: lower payments tied to income. Disadvantage: often longer repayment and more total interest.

### Day 3 (Wednesday): Debt strategies
*Student:* Pay down a sample four-debt portfolio using both avalanche and snowball methods in a spreadsheet and compare interest paid.

*How to teach:* Pay down the four-debt portfolio in a spreadsheet using avalanche and snowball with the same monthly total; compare interest paid.

- **Q:** Using avalanche on the sample portfolio, which debt gets extra payments first?
  **A:** Card A at 24% (highest rate).
- **Q:** Using snowball, which first?
  **A:** Card B at $800 (smallest balance).

### Day 4 (Thursday): When debt goes wrong
*Student:* Research collections, default, and wage garnishment, and list three resources (nonprofit credit counseling, CFPB) for help.

*How to teach:* Research collections, default and wage garnishment; list three help resources.

- **Q:** Name two legitimate sources of help with debt.
  **A:** Nonprofit credit counseling agencies (NFCC members), the CFPB, and the loan servicer (for student loan repayment plans).

### Day 5 (Friday): Review & check
*Student:* Unit 3 test on credit reports, credit costs, and debt management.

*How to teach:* Give the Unit 3 test in the key.

- **Q:** Which repayment method saves the most interest?
  **A:** Avalanche (highest interest rate first).

**Assessment:** Unit 3 test and debt-repayment spreadsheet.

**Answer key:** Unit 3 test answers: 1) FICO factors and weights. 2) Utilization calculation. 3) Soft vs. hard inquiry. 4) Negative items stay up to 7 years. 5) APR and grace period definitions. 6) Payday APR 390%. 7) Subsidized vs. unsubsidized loans. 8) Avalanche = highest interest rate first; snowball = smallest balance first. 9) Default on federal student loans = typically 270 days without payment; consequences include wage garnishment and seizure of tax refunds. 10) Nonprofit credit counseling (NFCC member agencies) and CFPB as resources. Mastery 8+/10. Debt spreadsheet: avalanche should show less total interest than snowball on the same monthly budget.
