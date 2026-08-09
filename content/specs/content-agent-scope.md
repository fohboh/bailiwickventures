# Scope — Bailiwick Content Pipeline Agent

**Internal build. Working name: PRESS.**
Prepared for Michael L. Atkinson · Draft for review · August 2026

---

## 1. The decision being automated

Publishing an essay across three destinations currently costs 60–90 minutes of manual work per piece: building the site page, reformatting for Substack, setting the canonical, writing a LinkedIn post, and remembering the sequence. None of that is judgment. All of it is repetitive, error-prone, and the reason essays sit unpublished.

**What is *not* being automated:** the decision to publish, the argument itself, and anything the system cannot substantiate.

The agent produces three finished artifacts and stops. A human reads them and clicks publish. That boundary is the design, not a limitation to be engineered away later.

---

## 2. Scope

**In scope**

- Ingest a finished essay in markdown with frontmatter.
- Generate and deploy the site page (primary version).
- Generate a Substack-ready version with canonical pointing to the site.
- Draft a LinkedIn post plus a first-comment link.
- Run the trust gate and the corpus checks described in §4.
- Present all outputs for approval in one review.

**Explicitly out of scope**

- Writing essays from a topic prompt. The agent formats, checks and distributes; it does not originate arguments.
- Publishing to Substack or LinkedIn without a human click.
- Scheduling, drip campaigns, audience segmentation, analytics.
- Any destination beyond the three named. X, Medium and newsletters are deferred until the first three are boring.

---

## 3. The workflow

Five stages. Authority is stated at each one, because "who is allowed to decide this" is the question that makes or breaks an agent.

### Stage 01 — Ingest
**Authority: agent, full.**
Reads `content/essays/<slug>.md`. Validates frontmatter: title, subtitle, date, topic, and a `sources:` block. Rejects the piece if frontmatter is incomplete. Computes word count and read time.

*Fails closed.* A malformed file stops the run with a specific error, never a guess at intent.

### Stage 02 — Verify
**Authority: agent proposes, human resolves.**
The trust gate (§4) runs here. Every factual claim, figure and attribution is checked against its declared source and against the existing corpus. Output is a findings list, each item classified **blocking** or **advisory**.

*Blocking findings stop the pipeline.* The agent does not proceed to generation with an unsubstantiated number in the text.

### Stage 03 — Generate
**Authority: agent, full — within a fixed template.**
Produces three artifacts:

- **Site page.** Through the existing Python build, so it inherits the design system automatically. No bespoke HTML.
- **Substack version.** Markdown shaped to the editor's shortcut syntax, with title, subtitle, and the canonical URL recorded for the post settings.
- **LinkedIn post.** 3–5 sentences making one point from the essay, in the author's voice, plus a separate first-comment line carrying the link. Never the full text.

### Stage 04 — Review
**Authority: human, exclusive.**
A single screen: the rendered site page, the Substack draft, the LinkedIn text, and the findings from Stage 02 including advisories that did not block. Michael approves, edits, or rejects.

*This stage cannot be skipped or defaulted.* No timeout auto-approves.

### Stage 05 — Distribute
**Authority: split, deliberately.**

| Destination | Mechanism | Who commits |
|---|---|---|
| Site | Git commit → Vercel deploy | **Agent**, on approval |
| Substack | Browser automation fills a **draft** | **Human** clicks publish |
| LinkedIn | Text prepared, staged | **Human** posts |

The site is the only destination the agent commits to directly, because it is ours, reversible in one commit, and carries the canonical.

---

## 4. The trust gate

The reason this is a Bailiwick tool and not a script.

An essay does not pass to generation unless:

1. **Every figure traces to a source.** Any number in the text must map to an entry in the frontmatter `sources:` block or be tagged `own-analysis`. An untraceable statistic is a blocking finding.
2. **Every attributed claim resolves.** Quotes and "according to" statements must carry a resolvable source. Broken or unreachable links block.
3. **No contradiction with the published corpus.** The essay is checked against the 21 pieces already on the site and the book manuscript positions. A direct contradiction blocks; a tension is advisory and surfaced for a human call.
4. **No unintended repetition.** Substantial overlap with an existing piece is advisory, with the overlapping piece named.
5. **Voice check.** Drift from the corpus baseline — sentence length, hedging density, jargon load — is advisory only. Voice is never a blocking condition; that judgment is the author's.

**Gate output is a record, not a vibe.** Each run writes a signed findings file kept with the essay: what was checked, what passed, what was waived and by whom. Over time that becomes an audit trail for your own published claims — which is the argument you make to clients, applied to yourself.

---

## 5. Architecture

Deliberately thin. Four components, no new infrastructure.

- **Pipeline runner** — Python, sits beside the existing `build/` system, reuses `posts.py` and `theme.py`. No parallel rendering path.
- **Verifier** — the trust gate. Deterministic checks (link resolution, figure-to-source mapping, corpus diff) run first and independently. Only the judgment-shaped checks (contradiction, overlap) use a model, and only *after* the deterministic layer has passed.
- **Corpus index** — the 21 published pieces plus book positions, indexed once, refreshed on publish.
- **Distributors** — three adapters behind one interface: `git` (real), `substack` (browser), `linkedin` (prepare-only). Each fails independently; a broken Substack adapter must not block the site publish.

**Ordering is not incidental.** Deterministic checks before probabilistic ones, same as MGE. A model is never the thing that decides whether a number is real.

---

## 6. What it will not do

- Publish anything to a third-party platform without a human click.
- Invent, embellish or "improve" a claim.
- Proceed past a blocking finding, including on a rerun, without an explicit recorded waiver.
- Post the full essay text to LinkedIn.
- Touch any destination not listed in §2.

---

## 7. Acceptance criteria

The build is done when, for a new essay dropped into `content/essays/`:

1. A malformed frontmatter file is rejected with a specific, actionable error.
2. An essay containing an untraceable figure is blocked, and the finding names the figure and the line.
3. An essay overlapping a published piece produces an advisory naming that piece.
4. The site page renders identically to a hand-built one — same design system, no drift.
5. The Substack draft appears in the account with title, subtitle, correct heading structure, and canonical recorded.
6. The LinkedIn text and first-comment link are produced and are not the full essay.
7. Nothing publishes to Substack or LinkedIn without a human click.
8. A failure in any distributor leaves the others unaffected.
9. Every run leaves a findings record beside the essay.

---

## 8. Build phases

Sequenced so value lands before the brittle parts.

**Phase 1 — Site pipeline and gate.** Ingest, verify, generate site page, commit. Useful on its own; this is where most of the manual hour goes.

**Phase 2 — Corpus index and contradiction checks.** The part that makes it a Bailiwick tool rather than a formatter.

**Phase 3 — Substack adapter.** Browser automation to draft. Expect maintenance.

**Phase 4 — LinkedIn preparation.** Text generation only. No automation against LinkedIn.

Phases 1 and 2 are the product. Phases 3 and 4 are convenience and should be treated as disposable.

---

## 9. Risks

- **Platform brittleness.** Substack and LinkedIn offer no API and change their editors without notice. Adapters must fail loudly and never block the site publish.
- **Scope creep toward autonomy.** The pressure to remove the review step will be constant and should be refused. The review step is the product's integrity.
- **Corpus staleness.** An index that drifts produces false confidence, which is worse than no checking. Refresh on every publish.
- **Voice flattening.** Model-drafted LinkedIn copy will trend generic. Treat drafts as raw material.
- **Gate theatre.** A trust gate that only ever passes is decoration. Track the block rate; if nothing is ever blocked, the checks are too loose.

---

## 10. Decisions — resolved

All five were settled on 9 August 2026. Phase 1 is unblocked.

1. **Waiver authority — Michael only.** A blocking finding can be waived, but by no one else, and every waiver is written into the findings record with its reason attached. A waiver is a signed act, not a dismissed dialog.
2. **Publish-to-site — the agent commits directly on approval.** No review branch. The site is ours and a bad publish is one revert away; a branch step would buy nothing and cost the speed the pipeline exists for.
3. **Canonical — confirmed available.** The Substack version carries the full text with the canonical URL pointed at the site page, so the site is the primary version and search engines are told so explicitly.
4. **Corpus boundary — Bailiwick material only.** The contradiction index covers the essays, blog and book positions published under Bailiwick. FohBoh.ai Learning Center content sits deliberately outside it: the two voices are allowed to differ, and an index that blurred them would manufacture contradictions that are not real.
5. **Failure notification — Slack and email.** Blocking findings go to both. Slack for the interrupt, email for the record. A finding that surfaces only in a terminal nobody is watching is the same as no finding at all.

**What this settles about the design.** Three of the five concentrate authority in one named person rather than distributing it, which is the right shape for a system whose whole claim is that a human stands behind what gets published. The agent moves fast where speed is free — formatting, checking, drafting, committing to our own property — and stops dead where judgment is required. That boundary does not move as the tool matures.

---

*Everything here is governed. One thing is declared.*
