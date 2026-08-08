---
title: "We Don't Build One Big Agent"
subtitle: "Task-specific beats one-size-fits-all, and the reasons are structural."
date: "August 8, 2026"
source: ""
series: ""
---

Every few weeks someone asks us to build "an AI agent for the business." Singular. One system, pointed at everything, answering whatever gets asked.

We don't build that. Not because it's difficult — because it's the wrong shape.

## What narrow actually looks like

In our own ventures, every agent is deliberately small. FohBoh Sentry recovers money restaurants are owed, and it does that through separate modules that barely resemble each other. One reconciles delivery-service settlements against point-of-sale orders. Another reconciles merchant processor statements against deposits. A third, in beta, tests franchise royalty calculations against the disclosure document. The delivery module carries 83 rules. The merchant module carries 107. They overlap almost nowhere, because a delivery aggregator's fee schedule and an interchange table have nothing in common except that both are used to take money from an operator.

FohBoh Cortex is different again. It answers operational questions in voice and text, but it reconciles nothing. It reads what the Metrics Governance Engine has already certified and explains it. Narrowing its job that severely is what makes its answers defensible.

BailiwickQuikFix runs field applications over a licensed governance engine for a wholly different operating problem.

None of these could be merged into one agent without making all of them worse.

## Four reasons narrow wins

**A narrow agent can be tested.** When the job is "find fee variances in a settlement file," you can write down what correct means and check it. When the job is "help with the business," you cannot, and so you never find out that it is wrong.

**A narrow agent fails visibly.** This is the one that matters most. A general-purpose agent producing a wrong answer sounds exactly like one producing a right answer. A scoped agent has a defined output with defined bounds, and a violation shows up as a violation.

**Constraints are cheap to encode when the job is small.** A hundred rules about merchant fees is a tractable body of knowledge. A hundred rules about everything a restaurant company does is a rewrite of the company.

**Domain expertise has somewhere to land.** Which is the next point, and the largest one.

## Standards are inputs, not documentation

Two kinds of standards govern an agent, and clients routinely underestimate both.

**Brand standards** determine what the agent is permitted to say: voice, register, the claims it must never make, the questions it must escalate rather than answer. An agent talking to your franchisees is speaking as you.

**Business standards** determine what the agent is permitted to conclude: which formula is authoritative, which denominator is approved, which source of record wins a disagreement, what variance threshold requires a human. These are the same questions a governance engine asks, and they have real answers inside a company — usually undocumented, usually held by three people.

Both change. Fee structures change quarterly, brand positions change with leadership, thresholds tighten as an operator learns what its own numbers look like. So standards get built as reviewed configuration on a cadence, never as prose buried in a prompt where no one can audit it. An agent is not finished at handover. It is instrumented at handover.

## Domain expertise is the prerequisite

Someone on the build has to already know that a promotional adjustment and a chargeback are different things, that a comp is not a discount, that food cost percentage means three different numbers depending on who is asking. Without that, you get an agent that is fluent, fast, and confidently wrong — which costs more than having built nothing.

And underneath all of it: no agent we build touches uncertified data. Trust layer first, then the agent. In that order, permanently.
