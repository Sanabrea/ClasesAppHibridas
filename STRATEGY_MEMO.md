# The Armory Storefront Strategy Memo

## Executive summary

The Armory is ten months in, with 12 tools and roughly 120 studios having installed at least one of them. On the surface, leadership’s instinct to “double down on installs” makes sense: tools like ArcaneArt top the install charts and create the impression of broad success. But when separating reach from value—activation, week‑4 retention, engagement, satisfaction, and cost—a different picture emerges.

Two tools stand out as true winners: EchoVoice and BugHound. They combine high activation, strong week‑4 retention, high deploys per active studio, excellent CSAT, and reasonable infra and support cost, and they are described by studios as part of their core workflow. By contrast, ArcaneArt leads in installs but underperforms on retention, engagement, and operational efficiency, while several art and narrative tools show signs of low fit and declining usage.

This memo recommends a shift in the storefront’s north-star from “total installs” to “monthly engaged studios” (studios performing a minimum number of AI-powered deploys in the last 30 days), supported by activation, retention, deploy depth, CSAT, and cost per engaged studio. It proposes an adoption plan centered on EchoVoice and BugHound, clear launch/invest/sunset criteria, a RICE-based roadmap for the next two quarters that prioritizes platform friction reducers and proven winners, explicit stakeholder messaging, and a reusable intake-to-launch lifecycle.

---

## 1. Storefront diagnosis & success metrics

### 1.1 What looks like it’s working vs. what is actually working

At first glance, ArcaneArt is the flagship: 95 studios have installed it, the highest reach in the catalog. However, only 28 are active in the last 30 days, week‑4 retention is 22 %, and active studios perform just 6 deploys per month on average. ArcaneArt generates 140 support tickets per month, has a relatively low CSAT of 2.9 out of 5, and carries the highest infra cost in the catalog at 4,200 USD per month. Feedback from studios describes it as slow, unstable, and responsible for broken asset pipelines, to the point that some teams have stopped trusting it for production use and largely abandoned it despite early installs.

EchoVoice, by contrast, has lower raw reach at 42 installs, but 38 of those studios are active in the last 30 days, with week‑4 retention of 81 % and 34 deploys per active studio per month. It generates only 9 tickets in the same period, has a CSAT of 4.7, and costs 1,100 USD per month in infra. Multiple studios report using EchoVoice every sprint and on every build, and explicitly credit it with saving weeks of placeholder VO work, while asking mainly for more languages and better discovery.

BugHound, still in beta, shows a similarly strong profile: 18 installs, 16 active studios, 78 % week‑4 retention, and the highest deploys per active studio at 41 per month. It has just 6 tickets, a CSAT of 4.6, and infra cost of 500 USD per month. Studios say it is already part of their workflow and request a CI integration so it can run on every pull request, signaling strong pull from advanced users.

Several tools exhibit the opposite pattern: moderate installs but weak retention and engagement, combined with concerning qualitative feedback. MotionMage has 22 installs but only 4 active studios, week‑4 retention of 18 %, 3 deploys per active studio, 19 monthly tickets, CSAT 3.1, and an infra cost of 1,500 USD per month; at least one studio reports that it broke after an update, prompting them to move to an external tool and not return. TileMancer has 31 installs and 6 active studios (19 % retention, 4 deploys per active studio), 28 tickets, and 800 USD per month in infra, with feedback indicating that it never fit their level style and was abandoned. QuestGen shows 14 installs and only 2 active studios (12 % retention, 2 deploys per active studio), 8 tickets, CSAT 2.8, and 400 USD monthly infra, with studios calling it “abandoned” and complaining about low-quality, slow outputs.

LoreWeaver, PixelForge, ScriptSmith, SoundScape, BalanceBot, and VoxModeler occupy a middle band: installs and active studios grow over time, retention sits in the 41–70 % range, and deploys per active studio are moderate, with CSAT in the mid‑3 to low‑4 range and infra costs between 300 and 1,300 USD per month. ScriptSmith is described as “fine and reliable, nothing exciting” and used occasionally, which suggests it is stable but not a must‑have.

### 1.2 Winners, misleaders, and cuts

Based on the combination of reach, activation, retention, engagement, satisfaction, and cost, the tools fall into three clear categories:

- **Real winners (invest / graduate):**
  - EchoVoice (T02) – high activation and retention, heavy usage, high CSAT, strong qualitative love, and clear asks for expansion.
  - BugHound (T05, beta) – high engagement and retention in a short time, strong workflow integration, and obvious next steps (CI, GA).
  - LoreWeaver (T03) – steady growth, solid retention (64 %), and CSAT 4.2, with narrative/lore depth as a known need.

- **Headline misleader:**
  - ArcaneArt (T01) – highest installs, but weak retention and engagement, heavy support and infra burn, and eroded trust in production workflows.

- **Likely sunset candidates:**
  - MotionMage (T08) – low and declining active usage, poor retention and engagement, costly infra, and feedback of breakage and permanent churn to external alternatives.
  - QuestGen (T12) – very low active usage and retention, poor perceived quality and speed, low CSAT, and limited reach.
  - TileMancer (T10) – marginal active usage, poor fit with some studios’ level styles, and signs of abandonment, though with somewhat higher reach than QuestGen.

### 1.3 Proposed north-star metric and supporting KPIs

Leadership’s current focus on “total installs” is understandable but misaligned with actual value creation in the storefront. Installs are a useful top-of-funnel signal of awareness and trial but do not capture whether studios are using tools in production, deriving sustained value, or incurring hidden costs.

A more appropriate **north-star metric** for The Armory is:

> **Monthly engaged studios**: Number of studios that perform at least a threshold number of AI-powered deploys (e.g., 5 or more) in the last 30 days across one or more tools in The Armory.

This metric implicitly encodes activation (studios reach first use), retention (they come back within 30 days), and engagement depth (they perform multiple deploys), and it correlates with the real operational value that studios describe for tools like EchoVoice and BugHound.

Supporting **leading metrics** would be:

- **Activation rate per tool**: active_studios_30d / studios_installed.
- **Week‑4 retention**: retention_week4_pct per tool, monitored over time.
- **Deploys per active studio**: deploys_per_active_studio_mo, especially for tools positioned as part of build pipelines.
- **Setup friction proxy**: time from install to first deploy, approximated via patterns in usage-monthly data and explicit measurement going forward.

Key **lagging/support metrics**:

- **CSAT per tool**: csat_1to5, trended.
- **Support tickets per active studio**: support_tickets_30d / active_studios_30d, highlighting tools that generate disproportionate operational load.
- **Infra cost per engaged studio**: infra_cost_usd_mo / engaged studios per tool.

This KPI stack aligns investment with tools that create sustained, production-level value while exposing tools whose apparent success is driven purely by installs.

---

## 2. Adoption plan: where and how to grow

The adoption plan focuses on the two clearest winners—EchoVoice and BugHound—because they already demonstrate strong pull and clear asks that, if addressed, can compound their impact.

### 2.1 EchoVoice (T02)

EchoVoice has 42 installs and 38 active studios, with 81 % week‑4 retention and 34 deploys per active studio. Studios report using it every sprint and on every build, citing large time savings, and specifically ask for two things: better discovery and broader language and accent support.

**Key blockers from install → recurring use:**

- Studios may not discover EchoVoice early; one studio explicitly notes they “found it by accident,” suggesting the storefront is not surfacing it effectively despite its impact.
- Language coverage limits its value for global player bases, constraining adoption depth in non-English markets.

**Concrete moves:**

- **Discovery and positioning:**
  - Feature EchoVoice in a “Recommended for production pipelines” and/or “Most adopted VO tools” section on the storefront home.
  - Add category filters and badges that highlight it as “High retention” and “High CSAT,” making it stand out against less proven tools.

- **Onboarding and packaging:**
  - Provide a “VO in 15 minutes” quick-start path for common engines, with ready-to-use sample projects and CI snippets.
  - Offer presets for popular genres (e.g., dark fantasy, sci-fi, casual) to reduce time-to-first-acceptable-output.

- **Feature investment (aligned with R02):**
  - Implement multi-language and accent support as a roadmap priority, as requested by seven studios and the EchoVoice team.
  - Use this expansion as the anchor for a targeted campaign to studios with global audiences.

### 2.2 BugHound (T05)

BugHound has 18 installs and 16 active studios after only three months, with 78 % week‑4 retention, the highest deploys per active studio (41), and strong feedback that it catches regressions missed by manual QA.

**Key blockers from install → recurring use:**

- It is still in beta, and some studios may hesitate to rely on it in CI/CD pipelines without a GA designation.
- Lack of built-in CI integration means teams must manually wire it into their workflows, adding friction.

**Concrete moves:**

- **GA graduation and CI integration (R03):**
  - Promote BugHound from beta to GA, signaling stability, once minimal quality and reliability criteria are met.
  - Ship first-class CI/CD integrations (e.g., GitHub Actions, GitLab CI, Jenkins) to align with the explicit studio request for “runs on every PR.”

- **Onboarding and packaging:**
  - Provide templates for common QA flows (smoke tests, regression suites, cross-platform checks) to showcase value quickly.
  - Highlight “teams like yours” case studies based on studios already integrating it deeply.

- **Discovery and positioning:**
  - Position BugHound within a “Production quality” or “CI-ready tools” slice of the storefront, so it surfaces alongside EchoVoice as a core pipeline component.

---

## 3. Readiness: launch, invest, sunset

### 3.1 Criteria

To simplify decisions, every tool is evaluated on three axes:

- **Launch / graduate:**  
  - Stable technical performance (no recurrent breakage reports or severe regressions).
  - Week‑4 retention above ~60 % and a non-trivial number of active studios (e.g., 10+).
  - Deploys per active studio indicating recurring use (e.g., 10+ per month for tools meant to be in active pipelines).
  - CSAT ≥ 4.0 and manageable tickets per active studio.

- **Invest:**  
  - Evidence of strong product–market fit (e.g., high deploys per active, strong qualitative pull), but with clear gaps (e.g., missing integrations, language support).
  - Reasonable infra cost relative to value.

- **Sunset (or freeze & re-evaluate):**  
  - Low and/or declining active usage, poor retention, and weak deploy depth, especially when combined with negative qualitative feedback.
  - Disproportionate infra or support cost per active or per engaged studio.

### 3.2 Recommended calls

**Graduate from beta:**

- **BugHound (T05):** Meets the bar for GA once CI integration and a small set of reliability fixes are delivered, given its 78 % retention, 41 deploys per active studio, strong feedback, and reasonable infra/support profile.

**Double down (invest):**

- **EchoVoice (T02):** Already a core tool for many teams; invest in multi-language support and discovery to fully leverage its adoption potential.
- **BugHound (T05):** As above, graduation plus CI is the main investment, as captured by R03.
- **Platform capabilities R01 and R04:** Shared deploy/auth SDK and search/discovery revamp (detailed in the roadmap) are investments that improve activation and adoption across the entire catalog.

**Sunset (make the unglamorous call):**

- **MotionMage (T08):** With 22 installs, 4 active studios, 18 % retention, 3 deploys per active studio, 19 monthly tickets, CSAT 3.1, and 1,500 USD per month in infra cost, plus explicit feedback that it broke after an update and caused a migration to external tools, MotionMage is a clear candidate for sunset.  
  - **Rough savings:** Immediate infra cost reduction of 1,500 USD per month and elimination of 19 tickets per month that can be reallocated to higher-value tools.  
  - Migration support should be provided to the few remaining active studios, but the low base makes this manageable.

**Monitor for potential cuts / reframe:**

- **QuestGen (T12):** 14 installs, 2 active studios, 12 % retention, 2 deploys per active, CSAT 2.8, infra 400 USD per month, and feedback that it feels abandoned and low quality.
- **TileMancer (T10):** 31 installs, 6 active studios, 19 % retention, 4 deploys per active, 28 tickets, and 800 USD per month infra, with feedback that it never fit some level styles.  

For both, set explicit thresholds (e.g., raise retention and deploy depth to specified levels over the next two quarters) or plan a second-wave sunset if improvement does not materialize.

---

## 4. Roadmap and prioritization (next 2 quarters)

### 4.1 RICE framework and scores

Using the backlog data, a simple RICE model is applied:  

RICE = (Reach × Impact × Confidence) / Effort

Where confidence is the given percentage converted to a 0–1 range.

| ID  | Item (short)                                             | Type                | Reach | Impact | Conf | Effort (pw) | Approx. RICE |
|-----|----------------------------------------------------------|---------------------|-------|--------|------|-------------|--------------|
| R01 | Shared deploy + auth SDK                                 | Platform capability | 120   | 2.0    | 0.8  | 6           | ≈ 32.0       |
| R02 | EchoVoice multi-language + accents                       | Tool investment     | 42    | 2.0    | 0.9  | 4           | ≈ 18.9       |
| R03 | BugHound GA + CI/CD integration                          | Tool investment     | 60    | 2.0    | 0.7  | 5           | ≈ 16.8       |
| R04 | Storefront search & discovery revamp                     | Platform capability | 120   | 1.0    | 0.7  | 5           | ≈ 16.8       |
| R08 | Per-studio usage analytics dashboard                     | Platform capability | 120   | 0.5    | 0.8  | 4           | ≈ 12.0       |
| R05 | ArcaneArt reliability + performance overhaul             | Tool investment     | 95    | 1.0    | 0.6  | 7           | ≈ 8.1        |
| R06 | New tool: ShaderSmith (AI shader generation)             | New tool            | 35    | 1.0    | 0.5  | 8           | ≈ 2.2        |
| R09 | New tool: CutsceneDirector (AI cinematic generation)     | New tool            | 25    | 2.0    | 0.4  | 10          | ≈ 2.0        |
| R07 | Bespoke Hollow Crown lore fine-tune (Twin Hearth only)   | New tool            | 1     | 3.0    | 0.8  | 8           | ≈ 0.3        |

This ranking places shared platform capabilities and investments in proven winners (EchoVoice and BugHound) clearly above new, unproven tools and bespoke work for a single studio.

### 4.2 Q3–Q4 roadmap (high-level)

**Q3 – Fix friction and amplify proven winners**

Focus for the first quarter is reducing setup and discovery friction across the catalog and amplifying tools that already demonstrate strong value:

- **R01 – Shared deploy + auth SDK (high priority):**  
  - Goal: move from per-tool setup and login to a true one-click install → activate flow, addressing the #1 churn driver between install and first deploy.  
  - Outcome: higher activation rate and lower time-to-first-deploy for every tool in the Armory.

- **R02 – EchoVoice multi-language + accents (high priority):**  
  - Goal: unlock EchoVoice for global player bases based on explicit studio demand.  
  - Outcome: deeper adoption in existing studios and increased attractiveness for new ones.

- **R03 – BugHound GA + CI/CD integration (begin implementation):**  
  - Goal: solidify BugHound as a first-class CI-ready QA tool and graduate it from beta.  
  - Outcome: more studios comfortable relying on it in production pipelines.

- **Sunset MotionMage (T08) and freeze new ArcaneArt installs (guardrail):**  
  - Goal: stop the bleeding from a low-value, high-cost tool (MotionMage) and prevent further expansion of ArcaneArt until its reliability path is clear.

**Q4 – Scale discoverability and visibility, deepen telemetry**

Second quarter builds on the friction reductions and tool investments:

- **R03 – Complete BugHound GA + CI/CD integration:**  
  - Target: GA announcement, CI templates, and adoption push to studios currently on waitlists.

- **R04 – Storefront search & discovery revamp (filters, “new”, recommendations):**  
  - Goal: address feedback that the storefront is “just a wall of cards” and that studios cannot tell what is new or relevant for them.  
  - Outcome: better matching between studio needs and tools, particularly benefitting newer or more specialized tools.

- **R08 – Per-studio usage analytics dashboard (as capacity allows):**  
  - Goal: provide studios and internal teams with visibility into usage and adoption, supporting more data-driven decisions.

- **R07 – Hollow Crown lore fine-tune: discovery and scoping (limited):**  
  - Goal: run a structured discovery with Twin Hearth to define data requirements, model behavior, and integration points, while being transparent that this is a high-effort, single-account initiative.  
  - Outcome: a grounded decision on whether and how to proceed in subsequent quarters, given the trade-offs.

New tools such as ShaderSmith and CutsceneDirector (R06 and R09) remain deprioritized in the next two quarters: their RICE scores are low relative to platform improvements and investments in proven winners, and leadership’s immediate bottleneck is adoption and engagement, not catalog expansion.

---

## 5. Stakeholder alignment

### 5.1 Leadership: reframing “double down on installs”

> Subject: The Armory – shifting from installs to engaged AI workflows  
>    
> Today, total installs paint an incomplete—and sometimes misleading—picture of what’s working in The Armory. Tools like ArcaneArt top the install charts but show low week‑4 retention, shallow engagement, heavy support load, and the highest infra cost in the catalog. Meanwhile, EchoVoice and BugHound have fewer installs but much higher activation, retention, and deploy depth, with excellent CSAT and tight integration into studio workflows. To align investment with real value, I recommend shifting our north-star from “total installs” to “monthly engaged studios” (studios performing at least X AI-powered deploys in the last 30 days), supported by activation rate, week‑4 retention, deploys per active studio, CSAT, and infra/support per engaged studio. This gives us a clear, data-backed way to double down on what truly moves the needle for studios and for Mythril.

### 5.2 Twin Hearth Studios: handling the loudest request

> Subject: Hollow Crown lore model – where it sits on the roadmap  
>    
> Thank you for the clear feedback on needing a model that really understands Hollow Crown’s lore. You’ve called this your top ask, and we treat it as such. Over the next two quarters, our primary focus is on reducing friction across The Armory—making it truly one-click to go from install to first deploy—and doubling down on the tools your team already uses every sprint, like EchoVoice and BugHound. The bespoke Hollow Crown lore fine-tune is on the roadmap as a targeted initiative: in Q3 we’ll run discovery on data, behavior, and integration, and in Q4 we’ll aim for a scoped beta if the technical and business trade-offs are sound. I want to be transparent that this is a high-effort investment for a single account with limited reuse, so we’re sequencing it after the highest-impact changes for all studios, while still making sure your request is clearly acknowledged and planned.

---

## 6. Intake-to-launch process

To ensure future tools and investments are handled consistently, The Armory should operate with a lightweight but explicit intake-to-launch lifecycle:

1. **Intake:**  
   - Capture all requests (new tools, tool investments, platform capabilities) via a standard template that includes problem statement, type, reach estimate, expected impact, confidence, effort estimate, and source.

2. **Triage and categorization:**  
   - Quickly filter out items that are clearly out of scope or misaligned with the north-star, and categorize the rest as tool, investment, or platform capability.  

3. **Prioritization (RICE + strategy):**  
   - For the remaining items, compute RICE using the agreed reach, impact, confidence, and effort, and then check the ranking against the north-star and supporting KPIs.  
   - Promote high-RICE, high-strategy-fit items to the next quarter’s candidate list; mark others as backlog or “parking lot.”

4. **Discovery:**  
   - For the top candidates, run focused discovery with a small number of studios (including those behind the request, when applicable) to validate the problem, refine scope, and define success metrics.  

5. **Build and launch:**  
   - Implement in increments (e.g., internal alpha → closed beta → GA), with clear acceptance criteria, documentation, and onboarding paths.  
   - For platform capabilities, ship with example integrations and tooling that make it easy for tool teams and studios to adopt them.

6. **Measurement and iteration:**  
   - Track activation, retention, deploys per active studio, CSAT, and support load for the new capability or tool, and compare against the success criteria defined in discovery.  
   - Iterate where metrics are below target, or expand promotion when they are above.

7. **Sunset gate:**  
   - At regular intervals (e.g., twice per year), evaluate each tool against the sunset criteria: low and/or declining active usage, poor retention, shallow engagement, negative feedback, and high cost per engaged studio.  
   - For tools that clearly miss the bar, plan a structured sunset: freeze new installs, support migrations, and decommission infra, freeing capacity for higher-impact work.

This process keeps the storefront aligned with its north-star, prevents one-off requests from bypassing prioritization, and gives leadership and studios a predictable way to understand how decisions are made.

---

This memo provides a defensible, data-backed plan that reorients The Armory from vanity installs towards engaged, production-grade AI workflows, while maintaining clear communication with leadership and key studios.
