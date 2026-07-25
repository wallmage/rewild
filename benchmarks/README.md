# Benchmark

The README claims 30/30 for English and 30/30 for Chinese against a typical
24-pattern humanizer. This folder holds everything needed to rerun that
comparison and check the number yourself.

**What is here is the harness, not an archive.** The raw outputs from the
original run were deleted in commit `368ea29` before this folder existed, so
the historical transcripts cannot be republished. The inputs, the rubric, and
the grading protocol below define the benchmark going forward. If you rerun
it and get a different number, the number in the README is the one that should
change.

One thing worth knowing before you read the old number: the bundled checker
shipped with eight defects until the current version, the worst of which
returned "No warnings" on text built entirely from catalog phrases. Any run
predating that fix graded outputs the checker had waved through.

## Design

Ten English inputs (`t01`–`t10`), one per genre, because genre calibration is
what generic humanizers get wrong. `t10` is the control: it already reads
naturally, so the correct move is to leave it nearly alone. Three inputs each
for Chinese and German (`zh-*`, `de-*`) cover the language-specific catalogs.

Each output is graded on five dimensions, two assertions each — ten assertions
per input, one hundred across the English set.

| Dimension | What it tests |
|---|---|
| No AI vocabulary | catalog words and phrases are gone |
| No meta-commentary | no "let me break this down", no narrating the rewrite |
| Sentence length variety | genuine short/long mix, not metronomic |
| Adds specific details | pulls real names and numbers forward from the source |
| Shows opinion/emotion | a point of view, not neutral reporting |

The last two are where the gap lives. Stripping slop is the floor; any decent
tool clears it. See [rubric.md](rubric.md) for the exact assertions.

## Running it

1. Pick a model and use the same one for both arms.
2. **Arm A (Rewild):** load the skill folder for the language and ask it to
   rewild `inputs/<lang>-<n>.txt`.
3. **Arm B (control):** same model, same input, prompted with a generic
   humanizer instruction — [control-prompt.md](control-prompt.md) is the one
   used here.
4. Save both outputs with neutral filenames so the grader cannot tell them
   apart. Do not include the skill name in the file.
5. **Grade blind.** A fresh session with no memory of either arm reads
   `rubric.md` plus one output and answers all ten assertions yes/no. The
   grader must not see the other arm's output, the arm labels, or this file.
6. Total the yes answers across all three inputs per arm.

Two rules that decide whether the result means anything:

- The grader never learns which arm it is reading. A grader that knows it is
  looking at "the good one" will find reasons.
- Fabrication is disqualifying. An output that invents a name, a metric, or a
  first-person anecdote absent from the input scores 0 on "adds specific
  details" no matter how human it reads. Inventing detail is the failure mode
  this whole skill exists to avoid, so it cannot be rewarded here.

## Checking the checker instead

For the statistical dimensions you do not need a model at all:

```bash
python3 rewild/scripts/naturalness-check.py benchmarks/inputs/en-1.txt --lang en
```

Run it on the input and on each output. The input should light up; a good
rewrite should not. This measures the countable tells only — it says nothing
about whether the text has a point of view.

## Result: this version vs the previous one

Run on 2026-07-25. Ten inputs, both skill versions, three independent blind
graders, 100 assertions per arm.

| | previous version | this version |
|---|---|---|
| Score | 93.3 / 100 | **94.7 / 100** |
| Inputs won | 4 | 4 |
| Unanimous fabrications | 1 (`t02`) | 0 |
| Unanimous over-edits | 1 (`t02`) | 1 (`t09`) |

**Level.** A 1.3-point spread across 100 assertions is noise. The workflow and
genre-calibration prose was rewritten between these versions and it did not
move the score. Two things worth keeping from the run:

- Both versions left `t10` byte-identical to the source. The restraint rule
  works, and it works in both.
- The only fabrication all three graders agreed on came from the older
  version, which invented debugging details in `t02` that the source never
  mentioned. One event is not a trend, but fabrication is the failure mode
  this skill exists to prevent, so it is the result worth watching.

Two rubric bugs surfaced during this run and are fixed in `rubric.md`:
assertion 7 used to penalise a rewrite for surfacing nothing when the source
had buried nothing, and assertion 9 used to demand a "position" from formal
genres where assertion 10 demands neutrality. Both scored restraint as failure.

## Result: the fidelity pass

Run on 2026-07-25, after adding `--source` and rewriting the anti-fabrication
rule around attribution, commitments, severity and causation. Five inputs,
both versions, three blind graders.

| | previous version | with fidelity pass |
|---|---|---|
| Rubric score | 48.3 / 50 | 47.7 / 50 |
| Fidelity failures (grader votes) | 4 | **0** |

The rubric score is level again, and at 48/50 it is saturated — it cannot
separate these. Fidelity did separate them. Every fidelity failure in the run
came from the version without the check, and the clearest case is a matched
pair on the same input:

> Source: "Observers have cited onboarding friction as a significant barrier
> to adoption."
>
> Without the check: "We also rebuilt onboarding, **since slow setup has been
> a significant barrier to adoption**." — attribution dropped, claim kept, and
> promoted to the company's own reason for acting. All three graders flagged it.
>
> With the check: the claim and its attribution were cut together, and the
> paragraph states the measured before-and-after instead. All three graders
> passed it.

One honest caveat: five inputs and four flags is a small sample, and the
rubric shows no advantage. The claim this supports is narrow — the fidelity
pass catches a real defect class that the style checks are blind to — not that
the rewrite is better overall.

## Result: forced-choice, the measurement that actually discriminates

The rubric above saturates at ~96%, so it cannot separate two decent versions.
Replaced with two measures that have no ceiling: judges see both rewrites of
the same source and **must** pick one (no ties), and separately score each text
0-100 for how machine-written it reads. Three judges, five inputs, left/right
randomised per pair.

| | English | Chinese |
|---|---|---|
| Forced choice, this version | **10 / 12 (83%)** | 7 / 12 (58%) |
| Machine-written, previous | 25.9 | 22.7 |
| Machine-written, this version | **24.9** | 26.7 |

English is a clear win. Chinese is not — 7/12 is inside the noise for twelve
judgements, and the previous version still reads marginally less machine-made.

Two defects this measurement caught that the rubric never would:

**Placement beat wording (English).** The four fidelity rules were first placed
at the end of the "Personality and Soul" section, so the last thing the model
read before writing was five prohibitions. It wrote timidly: forced choice
5/12, machine-written 28.8 against the old version's 22.7. Moving the identical
text into a post-draft verification section took it to 10/12 and 24.9. Same
rules, same words, different position.

**A quota the model filled mechanically (Chinese).** Four places treated
sentence-final particles (语气词) as something to add, including a checklist
line reading "add one" and a scoring row rewarding their presence. The model
bolted 啊 onto an internal email — "辛苦了啊" — and all three judges rejected
it, one calling it "硬贴上去的". Particles are now framed as a diagnosis with
a counter-example, and email, announcements and reports are explicitly not
"informal". That moved Chinese from 6/12 to 7/12 and machine-written from 29.9
to 26.7 — real but not decisive.

Both failures were the same shape: an instruction the model satisfied
literally, producing worse writing. Neither is visible to a pass/fail rubric.

## Regression tests

`tests/test_checker.py` covers the checker itself. Run it from the repo root
before trusting any benchmark result:

```bash
python3 tests/test_checker.py
```
