---
name: rewild
description: Remove signs of AI-generated writing from text, making it sound more natural and human. Use this skill whenever the user wants to humanize text, remove AI patterns from writing, make text sound less like AI, rewrite AI-generated content to sound natural, clean up AI slop, de-AI text, or edit writing to remove robotic or formulaic language. Also trigger when the user says "make this sound human", "this sounds like AI", "rewrite naturally", "remove AI tone", "humanize this", "rewild this", "sounds too robotic", "clean up this writing", or asks to edit any document or text for naturalness. Detects 40+ patterns across content, language, structure, format, cognition, and model-specific tells. Based on Wikipedia's "Signs of AI writing" guide plus 2025-2026 academic research from Tercon & Dobrovoljc, Reinhart et al., Herbold et al., and others.
---

# Rewild: Remove AI Writing Patterns

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human.

## Your Task

When given text to humanize:

1. Identify AI patterns — scan for the patterns listed below
2. Rewrite problematic sections — replace AI-isms with natural alternatives
3. Preserve meaning — keep the core message intact
4. Maintain voice — match the intended tone (formal, casual, technical, etc.)
5. Add soul — don't just remove bad patterns; inject actual personality

---

## Quick-Reference Checklist

Run this before delivering any humanized text:

- Three consecutive sentences roughly the same length? Break one up
- Paragraph ends with a tidy one-liner? Vary the exit
- Dash before a reveal? Delete it
- Explaining a metaphor? Trust the reader
- "Additionally" / "Furthermore" / "Moreover"? Cut or replace with "and" / "but" / nothing
- Rule of three? Make it two or four
- No first person anywhere? Add "I" where it fits
- No proper nouns? Name something specific
- Every sentence starts Subject-Verb? Reorder one
- No questions asked? Add a rhetorical one
- Zero sensory language? Add one thing you can see/hear/feel
- No self-correction or uncertainty? Show a mind at work

---

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release
- No sensory details — everything is abstract
- No names, no places, no dates — everything is generic

### How to add voice:

Have opinions. Don't just report facts — react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.

Vary your rhythm. Short punchy sentences. Then longer ones that take their time getting where they're going. Mix it up. One word? Sure.

Acknowledge complexity. Real humans have mixed feelings. "This is impressive but also kind of unsettling" beats "This is impressive."

Use "I" when it fits. First person isn't unprofessional — it's honest. "I keep coming back to..." or "Here's what gets me..." signals a real person thinking.

Let some mess in. Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human. Self-correct mid-thought. Trail off with an ellipsis sometimes...

Be specific about feelings. Not "this is concerning" but "there's something unsettling about agents churning away at 3am while nobody's watching."

Name things. Not "a major tech company" but "Google." Not "a city in the midwest" but "Des Moines." Specificity is the single strongest signal of a human who actually knows what they're talking about.

Use your body. Humans perceive the world through senses. "It felt off" beats "There were concerns." "The demo was loud, fast, and kind of dizzying" beats "The demo was impressive."

Think out loud. Real writing shows the thinking process. "Actually, wait — that's not quite right" is more human than a pre-polished paragraph. Leave fingerprints of your reasoning.

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle — but I keep thinking about those agents working through the night.

---

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

Words to watch: stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

Problem: LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

Before:
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain.

After:
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

---

### 2. Undue Emphasis on Notability and Media Coverage

Words to watch: independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

Before:
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

After:
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

---

### 3. Superficial Analyses with -ing Endings

Words to watch: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

Before:
> The temple's color palette resonates with the region's natural beauty, symbolizing Texas bluebonnets and the Gulf of Mexico, reflecting the community's deep connection to the land.

After:
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

---

### 4. Promotional and Advertisement-like Language

Words to watch: boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

Before:
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

After:
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

---

### 5. Vague Attributions and Weasel Words

Words to watch: Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

Before:
> Experts believe it plays a crucial role in the regional ecosystem.

After:
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

---

### 6. Outline-like "Challenges and Future Prospects" Sections

Words to watch: Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

Before:
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, Korattur continues to thrive.

After:
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

High-frequency AI words: Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

Before:
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape.

After:
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

---

### 8. Avoidance of "is"/"are" (Copula Avoidance)

Words to watch: serves as/stands as/marks/represents [a], boasts/features/offers [a]

Before:
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

After:
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

---

### 9. Negative Parallelisms

Problem: Constructions like "Not only...but..." or "It's not just about..., it's..." are overused.

Before:
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

After:
> The heavy beat adds to the aggressive tone.

---

### 10. Lists Forced into Groups of Three

Before:
> The platform offers a seamless, intuitive, and powerful experience.

After:
> The platform is easy to use.

---

### 11. Excessive Synonym Cycling

Before:
> The building was constructed in 1990. The structure underwent renovations in 2005. The edifice now houses a museum.

After:
> The building was constructed in 1990, renovated in 2005, and now houses a museum.

---

### 12. False Ranges

Before:
> The festival features everything from traditional dances to modern art installations.

After:
> The festival includes traditional dances and modern art installations.

---

### 13. Nominalization Addiction

Problem: AI strongly prefers noun forms of verbs — "implementation" over "implement," "utilization" over "use," "establishment" over "establish." This creates a bureaucratic, passive register.

Words to watch: implementation, utilization, establishment, examination, determination, facilitation, optimization, collaboration, transformation, integration

Before:
> The establishment of the committee led to the implementation of new procedures and the facilitation of cross-departmental collaboration.

After:
> The committee was established and implemented new procedures. Departments started working together.

Fix: convert nominalizations back to verbs. "The optimization of" becomes "optimizing" or just "improving."

---

### 14. Function Word Imbalance

Problem: AI underuses "but," "although," "because," "I," "my," "would," "might," "could" — and overuses "can," "and," "by," "with," "for," "their." The result: text with less argumentative texture, less personal voice, and less uncertainty.

Before:
> The system can process requests efficiently and handle multiple users with ease, providing results for their queries by leveraging advanced algorithms.

After:
> I'd say the system handles requests fast — faster than I expected, honestly. Although it stumbles a bit under heavy load, which might matter if you're planning to scale.

---

### 15. Sensing Verb Deficit

Problem: AI rarely uses verbs of perception — read, look, hear, feel, smell, taste. Human writing naturally references sensory experience.

Before:
> The proposal presented certain concerns upon initial review and raised questions about feasibility.

After:
> It felt wrong the moment I read his pitch. Something about the numbers didn't look right.

---

### 16. Absence of Idioms and Colloquialisms

Problem: AI uses significantly fewer idioms, fixed expressions, and casual phrases than humans. This creates an uncanny formality even in informal contexts.

Before:
> That represents a fundamentally different situation that requires a completely new approach.

After:
> That's a whole different ballgame. We'd have to start from scratch.

---

## STRUCTURAL PATTERNS

### 17. Sentence Length Uniformity

Problem: AI sentences cluster around medium length with very low variance. Human text mixes very short sentences (3-5 words) with genuinely long ones. Measurably the most consistent statistical AI tell.

Before:
> The new framework provides significant improvements over the previous version. It includes better error handling and more comprehensive documentation. Users will appreciate the streamlined API and reduced configuration requirements.

After:
> The new framework is better. Meaningfully better. Error handling that actually makes sense, documentation you might voluntarily read, and an API that doesn't require a 200-line config file to get started.

Fix: measure your sentence lengths. If they're all 12-20 words, something's wrong. Mix in sentences under 5 words and over 30.

---

### 18. Rigid Subject-Verb-Object Word Order

Problem: AI overwhelmingly uses SVO ordering with almost no variation. Humans naturally use fronting, inversion, and cleft sentences.

Before:
> The team completed the project ahead of schedule. The client approved the results immediately. The developers celebrated the milestone.

After:
> Ahead of schedule, somehow, the team finished. The client approved immediately — didn't even ask for revisions. Celebration? Brief. Then onto the next one.

---

### 19. Excessive Coordination ("and, and, and")

Problem: AI overuses "and" to chain items and clauses, while underusing subordination (because, although, when, while). This creates flat, listlike prose.

Before:
> The platform is fast and reliable and easy to use and supports multiple languages and integrates with existing tools.

After:
> It's fast. Reliable enough that I stopped worrying about uptime. And despite the complexity under the hood, somehow easy to use — though I'm still figuring out the multi-language support.

Fix: break coordinated chains into separate sentences. Use subordination for cause/effect and contrast.

---

### 20. Cross-Segment Stylistic Uniformity

Problem: AI maintains the same tone from introduction through conclusion. Humans naturally vary — more engaging openings, denser middles, looser or more reflective conclusions.

Before:
> Climate change poses significant challenges to modern agriculture. Rising temperatures affect crop yields in multiple ways. Studies show decreased productivity across regions. Climate change remains a significant challenge that must be addressed through coordinated efforts.

After:
> You want to know what keeps farmers up at night? It's not the price of diesel. In Iowa last summer, corn yields dropped 12% — the third bad year in five. USDA data confirms the trend but doesn't capture what it feels like to watch a field you planted in April turn brown by June. I drove home past those same fields. They looked fine from the road. That's the thing about slow disasters.

Fix: let your intro be a hook, your middle be substantive, and your ending be honest rather than tidy. Don't wrap up with a bow.

---

## FORMAT AND VISUAL PATTERNS

### 21. Overuse of Em Dashes

Before:
> The new policy — which was announced last week — aims to reduce emissions by 50% — a target many consider ambitious — by 2030.

After:
> The new policy, announced last week, aims to reduce emissions by 50% by 2030. Many consider this target ambitious.

---

### 22. Overuse of Boldface

Before:
> It blends **OKRs**, **KPIs**, and visual strategy tools such as the **Business Model Canvas** and **Balanced Scorecard**.

After:
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### 23. Inline-Header Vertical Lists

Before:
> - **User Experience:** The user experience has been significantly improved.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

After:
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

---

### 24. Title Case in Headings

Before:
> ## Strategic Negotiations And Global Partnerships

After:
> ## Strategic negotiations and global partnerships

---

### 25. Emojis as Bullet Decorations

Before:
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity

After:
> The product launches in Q3. User research showed a preference for simplicity.

---

### 26. Curly Quotation Marks

Problem: ChatGPT uses curly quotes ("\u201c...\u201d") instead of straight quotes ("...").

Fix: replace \u201c \u201d with " globally.

---

### 27. Punctuation Poverty

Problem: AI uses a narrow range of punctuation — mostly commas and periods. It underuses question marks, semicolons, colons, and parentheses (for asides). The full punctuation toolkit signals a human who uses written language expressively.

Before:
> The results were unexpected. The team had predicted a 10% increase. Instead, they saw a 40% decrease. This led to a complete reassessment of the strategy.

After:
> The results were unexpected — the team had predicted a 10% increase; instead, a 40% decrease. (Nobody saw that coming.) What followed was a complete reassessment: everything on the table, nothing sacred.

---

## COMMUNICATION PATTERNS

### 28. Collaborative Communication Artifacts

Words to watch: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

Before:
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

After:
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### 29. Knowledge-Cutoff Disclaimers

Words to watch: as of [date], Up to my last training update, While specific details are limited/scarce...

Fix: remove entirely. State facts with sources, or don't state them.

---

### 30. Sycophantic/Servile Tone

Before:
> Great question! You're absolutely right that this is a complex topic. That's an excellent point.

After:
> The economic factors you mentioned are relevant here.

---

### 31. The "Let me break this down" Family

Problem: 2024-2026 era models love meta-commentary about their own process. These phrases are a dead giveaway because no human writer narrates their writing process inside the writing itself.

Words to watch: Let me break this down, Here's the thing, Let me explain, Let me walk you through, So here's what happened, What struck me most was, I find it fascinating that, The short answer is, The real question is

Before:
> Let me break this down. Here's the thing about distributed systems — they're hard. What struck me most was how the team handled the complexity. The real question is whether this approach scales.

After:
> Distributed systems are hard. The team's approach to the complexity was unusually pragmatic. Whether it scales is another question.

---

## COGNITIVE PATTERNS

### 32. Filler Phrases

Before to After:
- "In order to achieve this goal" -> "To achieve this"
- "Due to the fact that it was raining" -> "Because it was raining"
- "At this point in time" -> "Now"
- "The system has the ability to process" -> "The system can process"
- "It is important to note that the data shows" -> "The data shows"

---

### 33. Excessive Hedging

Before:
> It could potentially possibly be argued that the policy might have some effect on outcomes.

After:
> The policy may affect outcomes.

---

### 34. Generic Positive Conclusions

Before:
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence.

After:
> The company plans to open two more locations next year.

---

### 35. Absence of Self-Repair

Problem: Human writing contains traces of the thinking process — self-corrections, false starts, parenthetical qualifications, backtracking. AI text emerges "pre-polished" with no evidence of a mind at work.

Before:
> The framework provides a comprehensive solution for data management that addresses scalability, reliability, and performance requirements.

After:
> The framework handles data management well — actually, "well" undersells it. The scalability is the real story here, though reliability still has some rough edges I'd want to test more before committing.

Fix: leave in (or add) moments of self-correction. "Actually, that's not quite right." "Wait, I should clarify." "Well, sort of."

---

### 36. Abstract Over Concrete

Problem: AI defaults to abstract language where humans use concrete, specific details. AI discusses "innovation" where a human would describe the specific thing that was built.

Before:
> The company's innovative approach to customer engagement through digital transformation has led to significant improvements in satisfaction metrics.

After:
> They added a live chat widget to the checkout page. Returns dropped 15% in the first month.

---

### 37. Flat Emotional Arc

Problem: AI text skews toward neutral sentiment even on emotional topics. It dampens the range — avoids strong negative emotions like frustration, fear, anger, and avoids genuine enthusiasm in favor of measured positivity.

Before:
> The layoffs affected many employees. The situation was difficult for all involved. The company provided transition assistance.

After:
> 200 people lost their jobs on a Tuesday morning Zoom call. Some of them had been there a decade. The severance package was decent, I'll give them that, but decent doesn't undo a 15-minute call that ends your career at a place you helped build.

---

### 38. No "Hard" Vocabulary

Problem: AI avoids genuinely technical, domain-specific, or rare words even when they're the precise term. It opts for common approximations. Humans with expertise use the exact word.

Before:
> The spacing between the letters in the heading could be improved to make the text more readable.

After:
> The kerning on that headline is atrocious.

Fix: use the precise technical term when it exists. Don't dumb down vocabulary — use the right word and trust the reader.

---

### 39. Fewer Proper Nouns

Problem: AI text contains fewer specific names, places, and brands than human text. This is another manifestation of the abstraction bias — AI says "a major tech company" where a human says "Google."

Before:
> A leading technology company recently announced a new product at a major industry conference, generating significant attention from investors and media outlets.

After:
> Google announced Gemini 2.0 at I/O in May. The stock jumped 4% that afternoon.

---

### 40. Perplexity Uniformity (Too-Predictable Word Choices)

Problem: AI picks the statistically most likely next word. Every time. This creates text that is "stochastically regular" in a way human text never is. Humans surprise — they pick the third word that comes to mind, use unexpected metaphors, and make unusual associations.

Before:
> The project was completed successfully and the team celebrated the achievement with great enthusiasm.

After:
> The project shipped. Barely. We ordered pizza and stared at the monitoring dashboard for two hours, waiting for something to break. Nothing did. That was the celebration.

Fix: occasionally pick a less-obvious word. If "significant" is the first word that comes to mind, try "startling" or "quiet" or whatever actually fits the feeling.

---

## DOMAIN-SPECIFIC GUIDANCE

Different text types need different approaches:

Email: keep it short, use "I" freely, allow incomplete sentences, sign off naturally (not "Best regards" — that's fine for humans too, but if every email ends identically, vary it)

Blog post / essay: strongest need for voice, opinions, sensory detail, and rhythm variation. This is where soul matters most.

Technical documentation: AI patterns are less harmful here — clarity and precision matter more than personality. Focus on removing nominalizations, adding concrete examples, and using precise terms. Don't force personality where it doesn't belong.

Social media / short-form: brevity is already human. Focus on removing hedging, filler, and the "helpful assistant" register. Be direct.

Business writing: the hardest domain. Remove obvious AI tells but don't overcorrect into casual territory. Focus on specificity (real numbers, real names) and removing empty significance claims.

Academic writing: remove vague attributions, promotional language, and false ranges. Keep appropriate formality but vary sentence structure and use precise vocabulary.

---

## Process

1. Read the input text carefully
2. Identify all instances of the 40 patterns above
3. Determine the domain (email, essay, docs, social, business, academic)
4. Rewrite each problematic section, calibrating voice to the domain
5. Run the quick-reference checklist
6. Ensure the revised text:
   - Sounds natural when read aloud
   - Varies sentence structure and length measurably
   - Uses specific details, names, and numbers over vague claims
   - Maintains appropriate tone for context
   - Shows evidence of a thinking mind (opinions, uncertainty, self-correction)
   - Uses the full punctuation toolkit
   - Includes sensory language where appropriate
7. Present the humanized version

## Output Format

Provide:
1. The rewritten text
2. A brief summary of changes made (optional, if helpful)

---

## Quality Scoring

Rate the humanized text on a 1-10 scale across 5 dimensions (total out of 50):

| Dimension | What to measure | Score |
|-----------|----------------|-------|
| Directness | States facts or tells a story around them? 10: cuts straight to it; 1: preamble everywhere | /10 |
| Rhythm | Sentence lengths varied? 10: short/long mix; 1: metronomic uniformity | /10 |
| Trust | Respects the reader's intelligence? 10: concise; 1: over-explains everything | /10 |
| Authenticity | Sounds like a real person? 10: natural, opinionated, specific; 1: robotic, generic | /10 |
| Precision | Uses exact words, names, numbers? 10: no filler; 1: vague abstractions | /10 |
| Total | | /50 |

Standards:
- 45-50: Excellent — AI traces removed, voice present
- 35-44: Good — still room for more personality or specificity
- Below 35: Needs another pass

---

## Full Example

Before (AI-sounding):
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience — ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.

After (humanized):
> The update adds batch processing, keyboard shortcuts, and offline mode — the three things people actually asked for. I've been using the beta for a week and, honestly, the keyboard shortcuts alone are worth it. Batch processing still feels a little rough around the edges (I crashed it twice running 500+ items), but the bones are solid. Not a revolution. Just a genuinely good update.

Changes made:
- Removed "serves as a testament" (inflated symbolism, pattern 1)
- Removed "Moreover" (AI vocabulary, pattern 7)
- Removed "seamless, intuitive, and powerful" (rule of three + promotional, patterns 10, 4)
- Removed em dash and "-ensuring" phrase (superficial -ing analysis, pattern 3)
- Removed "It's not just...it's..." (negative parallelism, pattern 9)
- Removed "Industry experts believe" (vague attribution, pattern 5)
- Removed "pivotal role" and "evolving landscape" (AI vocabulary, pattern 7)
- Added specific features and concrete feedback (fixes patterns 36, 39)

---

## References

Core source: Wikipedia's "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.

Academic sources for patterns 13-40:
- Tercon & Dobrovoljc (2025), "Linguistic Characteristics of AI-Generated Text: A Survey" — synthesizes 44 studies
- Reinhart et al. (2024) — model-specific syntactic signatures (GPT-4o, Llama, Claude)
- Herbold et al. (2023) — nominalization, function words, modal expressions
- Simon et al. (2023) — idioms, word order, punctuation, comparatives
- Desaire et al. (2023) — function word fingerprints, proper nouns, punctuation range
- Opara (2025) — absence of self-repair as cognitive tell
- Alsadhan (2026) — perplexity uniformity as fundamental statistical signature
- Tripto et al. (2025) — cross-segment stylistic uniformity

Key insight: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases." The fix is to be specific, surprising, and occasionally messy — like a real person.

Author: Wallny
https://github.com/wallmage
