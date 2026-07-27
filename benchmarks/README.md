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
| Forced choice, this version | **10 / 12 (83%)** | **9 / 12 (75%)** |
| Machine-written, previous | 25.9 | 22.0 |
| Machine-written, this version | **24.9** | **21.7** |

Both are wins. Chinese took three rounds to get there: 6/12, then 7/12, then
9/12, each round fixing a defect the forced choice exposed and the pass/fail
rubric could not see.

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

**An instruction that licensed invention (both languages).** "When you cut
unsourced praise, replace it with an honest, modest first-party claim" told the
model to write a self-assessment the source never made. It produced "各家流程
不一样，能省下多少时间也就不一样" in marketing copy and "上手这一关一直是我们
的短板" in a release announcement — a company confessing a weakness its own
source never confessed. All three judges flagged both. The rule now says: cut
the praise together with its claim and leave the gap. A humble invention is
still an invention.

**Re-saying reordered the argument.** "Look away from the original and write
it fresh" moved an essay's stated most-important lesson to the end, stranding
the reference. Re-saying now changes wording, not sequence.

Every one of these was the same shape: an instruction the model satisfied
literally, producing worse writing. None is visible to a pass/fail rubric, and
all four surfaced on the first forced-choice run that tested them.

## Protocol: the region benchmark (hk / tw)

The Traditional Chinese skills need a different measurement, because they have
no previous version to beat. What they claim is narrower and sharper: a Hong
Kong reader should take the output for local writing, and so should a Taiwanese
reader, and neither should mistake it for the other side.

Round 1 used three inputs (`hant-1` press release, `hant-2` internal email,
`hant-3` personal essay), each written as mainland-flavoured AI slop so both arms have the same
region work to do. Each carries planted conversion artefacts (`髮展`, `標准`)
and region-ambiguous vocabulary that has to resolve differently per region.

**Measure 1 — region attribution (the one that matters).** A judge who has
never seen the source reads one output and answers a single forced-choice
question: *was this written by a Hong Konger or by a Taiwanese?* No ties. The
skill passes when judges place its output on the intended side. This is the
user-facing claim stated as a testable proposition, and it is the only measure
here that a generic Traditional Chinese humanizer cannot game.

**Measure 2 — cross-contamination.** Judges see `rewild-hk` and `rewild-tw`
output for the *same* source, side by side, and say which is which. Two skills
that have genuinely diverged are separable; two that collapsed into "generic
Traditional" are not. This measure is why one skill with a region flag was
rejected at the design stage, so it is the one that would expose that decision
as wrong.

**Measure 3 — forced-choice naturalness.** As in the section above: each region
skill against a generic Traditional Chinese humanizer prompt on the same input,
judges must pick one, no ties.

Two rules carry over unchanged. The judge never learns which arm it is reading,
and fabrication is disqualifying regardless of how local the text sounds.

One caveat to state plainly: these judges are language models, not Hong Kong
and Taiwanese readers. The measurement is a proxy. It catches vocabulary,
transliteration and orthography reliably, and it is weakest on exactly the
thing the skill is aiming at — whether prose feels like a neighbour wrote it.
Native-reader review is the test this cannot replace.

## Result: the region benchmark

Run on 2026-07-27. Three inputs, three arms (`rewild-hk`, `rewild-tw`, and a
generic "write like a human, in Traditional Chinese" control), nine outputs
blinded to single letters, three independent judges — one neutral, one reading
as a Hong Kong reader, one reading as a Taiwanese reader.

| | result |
|---|---|
| Region attribution, skill arms | **18 / 18** |
| Own-region naturalness ranking | **6 / 6** |
| Control placed in a region | 0 / 3 by its own identity |

Every judge placed all six skill outputs on the correct side, and the neutral
judge marked all six "high confidence". The Hong Kong reader ranked the `hk`
output first in all three triples; the Taiwanese reader ranked the `tw` output
first in all three. Neither ever ranked the control first.

The result worth more than the score is that all three judges reconstructed the
experimental design without being told it. In the neutral judge's words: "each
triple contains one confident HK text, one confident TW text, and one that
reads as fluent-but-regionless — the third system in each set is the one
failing the test."

**What the control failed at is the specific thing being claimed.** It was not
bad writing. Judges called it fluent and, on vocabulary alone, mostly Taiwanese
— it defaults to 專案/使用者 unprompted. What it could not do was commit:
「詞彙查對了台灣，但語感與收尾仍是大陸的」. One judge placed two of its three
outputs in mainland China on the strength of 社交軟體, 應用 for apps, and
manufactured closing aphorisms. Generic Traditional Chinese is a real output
and it belongs to nobody.

### Three defects the benchmark found

**Cantonese syntax under standard characters.** The `hk` announcement wrote
「一樣處理到工作」. Every character is standard, but 動詞＋到 as a potential
complement is Cantonese grammar, and it had leaked into a 書面語 press release
— the exact register mixing the skill exists to prevent. One judge of three
caught it; the checker cannot, because its Cantonese markers match characters
and 處理到 contains none of them. Now documented as a fourth class in H9, with
the honest note that it is invisible to tooling and only reading aloud catches
it.

**The unsourced-statistic loophole.** The source said 「據統計顯示，超過 87% 的
用戶⋯」. The `tw` arm deleted the figure; the `hk` arm kept the number and cut
only the 據統計顯示 wrapper, reasoning that the source attributed it to users.
Taiwan read the rule correctly — 用戶表示 is not a source — and a judge
independently dinged the Hong Kong output for carrying the stat as an
unintegrated last line. C8 now names this failure: stripping the wrapper and
keeping the number leaves a figure that looks *more* credible while being just
as unsourced.

**A tension the rules do not resolve.** A judge criticised the `tw` output for
the opposite reason: deleting the statistic left the announcement with no
evidence at all. Both complaints are fair, and they pull against each other.
The anti-fabrication rule wins — an invented source is worse than a thin
announcement — but this is a genre cost, not a solved problem, and pretending
otherwise would be dishonest.

## Round 2: five inputs, including the cross-region pair

The first region run had a hole. All three inputs were mainland-flavoured, so
neither skill was ever asked to do the harder job: convert *the other region's*
Traditional Chinese. Two inputs were added — `hant-4`, a Taiwanese press
release the Hong Kong skill has to convert, and `hant-5`, a Hong Kong internal
email the Taiwan skill has to convert. Both regions now run all five.

Ten outputs, blinded to single letters in a scrambled order, three independent
judges: one reading as a Hong Kong reader, one as a Taiwanese reader, one a
region-neutral editor.

| | result |
|---|---|
| Region attribution | **30 / 30** (10 texts × 3 judges) |
| Texts placed in mainland China | **0 / 30** |
| Hong Kong 本地感, HK judge, own texts | 9, 8, 7, 5, 5 (mean 6.8) |
| Taiwan 在地感, TW judge, own texts | 9, 9, 8.5, 8, 5 (mean 7.9) |

Attribution is the claim the skills make, and it held: every judge placed every
text on the correct side, and nothing was mistaken for mainland writing. The
local-feel scores are the interesting half, because they are not full marks and
the judges agree on why.

### What the judges converged on

**Localisation stopped at the word layer.** All three said some version of it.
The neutral judge put it hardest: *"all ten are one skeleton in different
skins"* — the four memos swap 使用者↔用戶 and 佇列↔隊列 meticulously while
paragraph order, the order the systems are listed in, and the placement of the
thanks stay near-identical. The Hong Kong judge: *"these are not ten texts,
they are four source texts with the vocabulary swapped ten ways."*

Part of that is structural and honest to state: both arms rewrite the same
source, and the workflow forbids reordering because reordering is where
fidelity drift starts. Two documents faithful to one source will resemble each
other. But part of it was a real gap, and it is now closed in three places —
department names and long noun phrases (T17), internal versus external
correspondence register (H17b), and where 港味 actually comes from in business
writing, which the two lowest-scoring texts had none of.

**The documents stopped functioning.** Three of the ten no longer worked as
what they claimed to be: a 3.0 launch announcement with no publisher, no date
and no availability; a press release with no date, no named source and no media
contact. *"The de-AI pass was deleting for tone with nobody checking whether it
was still a press release afterward."* Both skills now carry a per-genre
function checklist — what has to survive in a product announcement, a press
release, an internal notice, an event notice — plus the rule that when the
source itself lacks those, you say so rather than invent them.

**Batch convergence is visible to readers.** Two judges independently spotted
that the two migration emails were one skeleton run twice, down to a shared
empty sentence in two costumes: 「能走到這一步是大家一起做出來的」 against
「能夠順利推進全靠大家」. Every per-document check passes on both. This is what
`--siblings` was built for.

**Taiwan had a residual 昇華 the mainland catalog does not describe.** All three
Taiwan texts ended a paragraph with a content-free self-affirmation — 「回響正
面」, 「正如那句老話」, 「能走到這一步是大家一起做出來的」 — and no Hong Kong
text did. They evade 模式 16 because they are casual rather than formulaic. Now
T18, with the test that matters: delete the sentence and ask what the reader
knows less of.

### Round 3: the three weakest texts, rebuilt and re-judged head-to-head

The three lowest-scoring texts were rewritten against the revised skills and
put back in front of blind judges — old version against new, letters scrambled,
no indication which was which.

The Taiwanese reader picked the new version of the migration email, **8 against
5**, and named the three things that moved: 資訊科技部 became 資訊部, the Hong
Kong noun phrase 資訊科技基建優化計劃 became 系統搬遷, and the T18 tic was gone.
Their words for what won it: 「準備工作的部分不好意思要再麻煩各位先處理完」 is a
sentence a Taiwanese person writes from muscle memory — apologise first, 麻煩 as
a verb — against the old version's flat 「請各團隊先把準備工作做完」 and a
closing that reads "back-translated from *feel free to write to me*." On the
specific tic: the new version ends every paragraph on a fact or an instruction
and pins its thanks to 忙了三個禮拜; the old one carried 「能走到這一步是大家一起
做出來的」, which the judge noted is not merely empty but *contradicts* the very
next clause thanking one department.

The criticism that survived is worth recording because it is not about region
at all: *"X won the ear and lost the job."* The notice never says what the
preparation work is, and 「相關服務會受影響」 tells nobody whether they can still
log in. Both are true of the source too, so the rewrite could not fix them
without inventing — which is exactly the case the function checklist now covers
by requiring the gap to be reported rather than filled. One thing the checklist
did not cover has been added: a relative time inherited from the source
(「本週六」) is unresolvable for a reader who opens the mail the next day, and
that has to be flagged even though converting it would be fabrication.

The Hong Kong reader picked the new version in both Hong Kong pairs — the
product launch for writing 數據 dashboard where the old one translated it (Hong
Kong offices do not translate that word) and for the old one claiming 「改了三處」
then listing five, and the press release for 冀、質素、該會⋯指, which the old
one had none of. Across the three pairs, **3 / 3 to the revised skills**.

Their criticism is the most useful thing in this file, because it is about an
absence and no amount of vocabulary work would have found it: *"none of the six
was written by a Hong Konger — and the proof isn't a mistranslated word, it's
what's absent. A real Hong Kong downtime notice without 「不便之處，敬請見諒」
does not exist."* Also missing across all six: 屆時, 敬請留意, 另行通知,
特此公布. These are not vocabulary forks, so no lexicon table would list them;
they are the fixed furniture of a genre. That is now H6b, on the *restore* side
of the catalog alongside 港式文言虛詞, with the constraint that matters —補回,
不是新增: if the source never apologised, adding an apology is putting words in
the author's mouth.

The second criticism applies to both regions and has been acted on: an orphaned
sentence survived in *both* versions of two pairs, because the workflow's
"rewording, not reordering" rule was being read as forbidding repair. It exists
to stop a rewrite quietly changing setup and reference, not to preserve the
source's own defects. Both skills now carry the exception.

### Round 4: testing the absence claim directly

H6b came out of one judge's sentence, so it got its own test: the two internal
notices rewritten with it, put blind against their previous versions in front of
a Hong Kong reader who was asked specifically whether the furniture makes the
difference claimed.

**Both pairs went to the new version**, taking the cumulative head-to-head to
**5 / 5**. But the useful answer is the qualified one:

> 缺了家具一定不是本地寫的；家具齊全不代表是本地寫的。

Missing furniture is a hard tell — the one text with none of it ranked last.
Presence proves nothing: the text carrying the *most* furniture ranked second
worst, because it was placed wrong. It apologised 「不便之處，敬請見諒」 in a
notice that asked the reader to do nothing, used 本人 in a nine-line internal
email, and signed off 「順頌業祺」 as if writing to a client. H6b now carries
placement rules and an explicit *when not to*: no two 敬請 in one breath, no
classical honorific bolted to an English word (「敬請各 team」), and no apology
where nobody was inconvenienced.

Three further findings, all acted on:

- **Translating the technical terms was the giveaway.** All four texts rendered
  *message queue* as 訊息隊列. 隊列 is the correct Hong Kong word — the defect is
  translating at all, because a Hong Kong IT department writes "message queue"
  or MQ. Now H8b, with the same test H8 uses: what do colleagues say out loud.
- **Convergence at a finer grain than the sibling scan sees.** Two texts dropped
  from written Chinese into Cantonese 「搵我」 at exactly the same position — the
  last line. Different words, same gesture, same position: *"same hand, two
  vocabularies."* Shingles cannot catch that; the skill now says so directly.
- **The notice genre carries more furniture than the checklist knew.** No
  subject line, no issuing department, no contingency (「如未能如期完成，將另行
  通知」), no instruction to log off before the window, no statement of which
  systems stay up, and in all four the only contact channel was one person's
  inbox. The source lacks these too, so the rule is unchanged — report them,
  don't invent them — but they are now enumerated rather than left to judgement.

### Final round: full set, both regions, after every fix

Ten outputs regenerated against the finished skills, blinded, read by a Hong
Kong reader and a Taiwanese reader.

| | result |
|---|---|
| Region attribution | **20 / 20**, both judges, clean split, nothing ambiguous |
| Hong Kong 本地感, own texts | 8.5, 8, 8, 6.5, 6 |
| Taiwan 在地感, own texts | 8, 8, 7, 6, 6 |
| Cumulative region calls, all rounds | **50 / 50** |

Four of the five named failure modes are gone. Translated technical terms:
fixed, and the Hong Kong judge called it the best-fixed of the lot — message
queue, dashboard, icon and email all kept in English. Hollow self-affirming
endings: **all five gone**, five different closing positions. Hong Kong
department names and epistolary formulae leaking into Taiwanese text: gone.
No local voice in announcements: fixed. Over-correction stayed clean — no
bolted-on particles, no forced 台語, and apologies appear only in the two texts
that actually take a service down for four hours.

**What is left is one defect, and both judges found it from opposite sides.**
A Hong Kong and a Taiwanese rewrite of one source come out as the same document
in two accents. The Taiwanese reader: 「文體變了，手沒變。」 The Hong Kong
reader gave the cleanest evidence — the two personal essays end

> 或許有一天會裝，或許不會。暫時這樣，我覺得幾好。
> 也許哪天會裝，也許不會。至少現在這樣我還蠻喜歡的。

one sentence through two accent filters. **No vocabulary check can see this,
because every single word already differs.** The four migration notices align
paragraph for paragraph and close with the same move in four accents —
email 我／搵我／來找我／直接找我.

That is now a check. `--siblings` compares paragraph structure rather than
words, so it works across regions: two versions of one source that share a
paragraph count and sentence-count profile are reported as *one document in two
accents*. Run on the final set it catches the migration pair at 100% skeleton
alignment. Both catalogs carry the rule with the essay pair as the worked
example.

Two smaller Hong Kong findings, both acted on: furniture was being rationed per
document rather than matched to genre and position (「不便之處，敬請見諒」 used
as a closing line when it belongs mid-paragraph; 「特此公布」 — a government and
listed-company sign-off — on a product release note, which is an *upward*
register jump and reads worse than a downward one), and 「在此謹多謝」 mixes
classical and colloquial inside one phrase.

### Mechanical separability

The judge-free half of measure 2. Every output is run under its own region and
under the other one. A text that belongs to a region should raise no region
warnings under its own flag and at least one under the other:

| | result |
|---|---|
| Outputs separable by the checker alone | **13 / 13** |

This started at 11/13. Both failures were the same short Hong Kong
announcement, which used 項目管理 — and 項目 cannot be gated for Taiwan, because
there it means "item" (比賽項目, 檢驗項目) and flagging it would fire on ordinary
Taiwanese prose. The collocations that only ever mean "project" (項目管理,
項目經理, 項目團隊) are safe where the bare word is not, and gating those closed
the gap without loosening anything.

### Reproducing it

```bash
python3 rewild-hk/scripts/naturalness-check.py <rewrite> --source benchmarks/inputs/hant-1.txt --lang hk
```

The mechanical half needs no judges. Run each output under both `--lang hk` and
`--lang tw`: an output that belongs to a region should raise region warnings
under the other one and none under its own.

## The editor loop: one artifact, ten rounds, 8 → 10

A different shape of test from everything above. The A/B rounds measure *which
side* a text lands on. This one measures how far a single text can be pushed
after the vocabulary is already correct.

Protocol: the skill writes one 400–500 word first-person essay. It goes to a
judge prompted entirely in Traditional Chinese as a thirty-year 副刊總編輯,
told to score 1–10, to quote every line that reads machine-written, and to say
what would earn a 10. Every named fix is applied and the piece is rescored.
Same caveat as the region benchmark: these are language models, not native
readers.

| | Hong Kong | Taiwan |
|---|---|---|
| First draft | 5 | 5 |
| Seven rounds, a fresh judge each round | 5 → 8 | 5 → 8 |
| Structural rewrite, one editor held across revisions | 7 → 8 → 9 | 8 → 9 |
| Final | **10** | **10** |

The Hong Kong dip is not noise, it is the point: a fresh editor scored the
structural rewrite *lower* (7) than the previous editor had scored the text it
replaced (8). Scores from rotating judges wander by a point or two in both
directions; only a held editor produces a monotone climb.

**Vocabulary saturates early; structure does not.** From round two onward
neither editor could fault the word choice — Hong Kong: 「字係香港人嘅字，骨係
機器嘅骨」; Taiwan: 「字是台灣人的字，結構是機器的結構」. Everything between
8 and 10 was distribution: every paragraph landing a short dry close, every
detail eventually recycled, one number per paragraph, filler sprinkled evenly,
a closing image that maps one-to-one onto the theme. The sharpest form of it,
from the Hong Kong editor: 「呢篇嘅問題唔係寫得差，係寫得冇失手過。」 That is
now pattern 26b (en) / 29b (zh, hk, tw) / 32b (de).

Two things about method are worth recording:

**Rotating a fresh judge every round stalls.** Seven rounds of new judges held
both texts at 8 and produced contradictions — one round asked for an opinion
line, the next cut the same line as op-ed voice. Progress came from keeping
*one* editor across rounds: it holds its own fix list, and it can be held to
it. Both 10s came from an editor scoring a revision of a draft it had already
marked up.

**Replacing a perfect ending with another perfect ending does not work.** The
Hong Kong editor caught exactly that mid-loop — an umbrella symbol swapped for
a noodles symbol — and named it 「換衫，唔係換人」. The fix is not a better
ending; it is being willing to end badly.

Reproducing it needs no fixture files: generate an essay with the skill, and
prompt a judge with the paragraph above. The essays themselves are not
committed, for the same reason the original benchmark outputs are not — this
folder is the harness, not an archive.

## Regression tests

`tests/test_checker.py` covers the checker itself. Run it from the repo root
before trusting any benchmark result:

```bash
python3 tests/test_checker.py
```
