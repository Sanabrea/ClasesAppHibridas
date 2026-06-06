# PM_AI_WORKFLOW

## Overview

This assessment explicitly encourages an AI‑first approach, so I treated AI as a core collaborator throughout the exercise rather than as an afterthought. My goal was to use AI to accelerate the mechanical parts (data parsing, first‑draft writing) while keeping product judgment, prioritization, and trade‑off decisions firmly in the human loop.

Concretely, I used an LLM-based assistant to help with:

- Summarizing and cross‑referencing the CSVs (`tools`, `usage-monthly`, `intake-backlog`, `studio-feedback`).  
- Identifying patterns (e.g., “headline winners” vs. “real winners”) and proposing candidate north-star metrics.  
- Drafting a first version of the strategy memo structure and some wording.  

I kept the interpretation of the data, the final calls (winners, cuts, roadmap) and all numerical checks under my own control, validating AI suggestions against the raw CSVs.

---

## AI tools and how I used them

### 1. Data comprehension and exploration

I pasted the contents of `tools.csv`, `usage-monthly.csv`, `intake-backlog.csv`, and `studio-feedback.csv` into an AI assistant and asked it to:

- Highlight tools with the best combination of installs, active studios, week‑4 retention, deploys per active studio, CSAT, tickets, and infra cost.  
- Flag any tools where “headline reach” (installs) diverged from actual value (activation, retention, engagement).  
- Summarize studio feedback by tool and platform theme.  

This gave me a fast “shape of the data” view: EchoVoice and BugHound clearly stood out as winners, while ArcaneArt, MotionMage, TileMancer, and QuestGen looked problematic when combining metrics and quotes.

### 2. Prioritization and roadmap framing

Using `intake-backlog.csv`, I asked the assistant to:

- Compute and compare approximate RICE scores for each request (converting confidence from percentage to 0–1).  
- Suggest a logical grouping of items into Q3 vs. Q4 based on RICE and strategic fit (platform vs. tool vs. bespoke).  

I then re‑checked the math myself and adjusted the roadmap to make sure platform capabilities (R01, R04) and investments in proven winners (R02, R03) came before new, unproven tools (R06, R09) or bespoke items (R07).

### 3. Drafting and editing the strategy memo

Once I had my own conclusions (winners, misleading tool, sunset candidate, north-star, roadmap), I used the AI assistant as a writing partner:

- I shared an outline of the memo sections, plus my bullet‑point conclusions per section.  
- I asked it to generate well‑structured paragraphs and stakeholder messages in a Head‑of‑Product‑ready tone.  

From there, I edited the text to make sure it sounded like me, tightened any over‑confident claims, and checked that every statement could be traced back to the data.

---

## Workflow / prompt I’m proud of

The workflow that was most effective was a “data + intent + guardrails” prompt I used to align the assistant with the assessment’s expectations. A simplified version:

> “Here is the content of `tools.csv`, `usage-monthly.csv`, `intake-backlog.csv`, and `studio-feedback.csv`.  \
> The context: Mythril’s Armory is a storefront for AI dev tools. Leadership wants to ‘double down on installs’, but the brief says that installs can be misleading.  \
> 1) Identify which tools are the real winners vs. headline misleaders, using activation, week‑4 retention, deploys per active, CSAT, tickets, and infra cost.  \
> 2) Propose a north-star metric for the storefront that reflects value, not just reach.  \
> 3) Suggest a RICE-based ordering of the backlog items and a high-level 2‑quarter roadmap.  \
> Do not invent data; only use what’s in the CSVs. Be explicit about trade-offs and assumptions.”

This worked well because:

- It anchored the assistant on the same “reach vs. value” framing that the assessment itself uses.  
- It forced the model to cite concrete metrics (e.g., EchoVoice’s retention vs. ArcaneArt’s support load) instead of staying at a generic level.  
- It asked for structure (winners, north-star, RICE, roadmap) that directly mapped to the six required deliverables, which reduced rework.  

The output wasn’t copy‑paste ready, but it gave me a strong first pass that I could refine.

---

## Where AI was wrong or misleading (and how I caught it)

One example where the AI was directionally useful but technically off:

- In an early iteration, the assistant loosely treated the `active_studios_30d` values in `usage-monthly.csv` as if they might be incremental changes, rather than snapshots per month, and it briefly implied a stronger “churn” narrative than the data actually supported.  
- To verify this, I manually scanned the CSV and cross‑checked against `tools.csv`:  
  - The `cumulative_installs` column clearly grows over time (e.g., ArcaneArt 18 → 95), while `active_studios_30d` fluctuates within a smaller band (e.g., 12 → 31 → 28), indicating snapshots, not deltas.  
  - When combined with week‑4 retention and the latest active count from `tools.csv`, the trend still supports a story of softening engagement—but not a full collapse.  

I corrected the narrative in the memo to say that ArcaneArt’s active usage “peaks and then softens while installs continue to climb,” rather than overstating churn. This is a good example of why AI suggestions are helpful, but raw data and PM judgment must stay in control of the final story.

A similar pattern happened with the backlog: the assistant initially pushed the bespoke Hollow Crown lore fine‑tune (R07) higher than I was comfortable with, given its impact is concentrated in one studio. I re‑applied the RICE formula, noted its extremely low reach (1) and high effort (8 person‑weeks), and consciously deprioritized it behind platform work (R01, R04) and investments in EchoVoice and BugHound, while still acknowledging it in the stakeholder section.

---

## Reflections on AI-first product work

This assessment is a good example of how an AI‑first PM can and should work:

- Use AI to compress the time from raw data to structured hypotheses—especially when dealing with messy CSVs and qualitative feedback.  
- Keep model outputs as inputs, not as ground truth: check numbers, re‑do the math, and challenge any conclusion that doesn’t survive a quick spreadsheet or sanity‑check.  
- Leverage AI for drafting and refinement so more time goes into framing the problem, making trade‑offs, and communicating decisions clearly to leadership and studios.  

In other words, AI accelerated the work, but it did not replace the core responsibilities of the product role: deciding what matters, in what order, and why.
