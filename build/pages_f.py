"""Plans & Pricing — the three pre-priced engagements and the paid Triage.

Plan A (Blueprint) is Studio work; Plan B (Buildout) is Vibe phases 01-04;
Plan C (Venture) adds Vibe phases 05-08. The page is framed by the client's own
situation rather than by division, because clients do not know which division
they belong to. Division colors are preserved: cobalt = Studio, vermilion = Vibe.

Every price on this page appears exactly once as a constant below. Nothing is
restated in prose — if a number changes, it changes here and nowhere else.
"""

TRIAGE = "$2,500"
A_PRICE = "$25,000"
B_PRICE = "$85,000"
C_PRICE = "$250,000"
C_EQUITY = "3–6%"
FLOOR = "$25,000"
CREDIT_DAYS = "30 days"
CONCURRENT = "four"


# ---------------------------------------------------------------- helpers

def _faq(q, a):
    return f"""<details class="more"><summary><span class="pm"><span>+</span><span class="mn">&minus;</span></span><span>{q}</span></summary><div class="inner">{a}</div></details>"""


def _faq_group(title, items):
    body = "".join(_faq(q, a) for q, a in items)
    return f"""<div>
      <h4 style="margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid var(--line)">{title}</h4>
      {body}
    </div>"""


# ---------------------------------------------------------------- page

PAGE_CSS = """
<style>
/* Page-scoped corrections to the shared design system.
   Two combinations are used here for the first time on the site and are not
   covered by theme.py; both should migrate into theme.py at the next full
   rebuild, at which point this block can be deleted.

   1. A bare .phases grid inside .on-ink kept its light card background while
      .on-ink recolored the heading and body text to light — white on cream.
   2. .gate .exc p b is pinned to --ink, which on a navy .on-ink section
      renders near-black on near-black. */
.on-ink .phases{background:#274259;border-color:#274259}
.on-ink .phase{background:#0F2942}
.on-ink .phase h4{color:var(--warm)}
.on-ink .phase .pn{color:var(--bronze-lt)}
.on-ink .phase p{color:#AEBDCA}
.on-ink .gate .exc p b{color:var(--warm)}
.on-ink .gate .exc .lbl{color:#8FA1B1}
/* the fig caption runs long on this page; let it breathe rather than collide */
.fig small{line-height:1.5}
/* 3. theme.py's details.more hides every span inside .pm when open, which for a
      question-and-answer list leaves an empty box instead of a minus. The FAQ
      keeps its question visible when open, so it needs the toggle to swap
      rather than vanish. */
details.more>summary .pm .mn{display:none}
details.more[open]>summary .pm .mn{display:inline}
#faq details.more{margin-top:0;border-bottom:1px solid var(--line)}
#faq details.more>summary{padding:13px 0;align-items:flex-start;gap:10px}
#faq details.more .inner{margin-bottom:14px}
</style>
"""


def plans():
    return PAGE_CSS + f"""
<div class="hero" style="background:linear-gradient(180deg,#FFFDF9 0%,#FFFDF9 58%,#F6F2EC 100%)">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Plans &amp; pricing &middot; Studio and BailiwickVibe</p>
    <h1 style="max-width:16ch">Three ways to start. All of them priced.</h1>
    <p class="lede">Most firms make you sit through discovery before they will tell you what anything costs. We publish the number. You arrive knowing what you are buying, and we arrive knowing you are serious.</p>
    <div class="btns">
      <a class="btn btn-p" href="#triage">Start With the Triage &mdash; {TRIAGE} <span class="arrow">&rarr;</span></a>
      <a class="btn btn-s" href="#plans">Compare the Three Plans <span class="arrow">&rarr;</span></a>
    </div>
    <div class="tagline"><span>Blueprint</span><i></i><span>Buildout</span><i></i><span>Venture</span></div>
  </div>
</div>

<!-- ---------------------------------------------------------------- triage -->
<section class="on-ink" id="triage">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(30px,3.6vw,44px)">
      <div>
        <p class="eyebrow">The front door</p>
        <h2 style="max-width:14ch">The Triage.</h2>
        <span class="fig" style="margin-top:22px">{TRIAGE}<small>Credited in full &middot; 5 business days</small></span>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">There is one way into any of the three plans, and this is it. Ninety minutes with Michael, then a written assessment of what you actually have and what it would take to make it real.</p>
        <p class="body" style="margin-bottom:22px">It is paid because unpaid diagnostics get treated as free consulting, and because the memo is worth more than most people pay for a month of advice. The entire fee is credited against any plan booked within {CREDIT_DAYS} of delivery.</p>
        <p class="pull">If the honest answer is that you should not build this, the memo says so. That is a finished deliverable, not a failed sale.</p>
      </div>
    </div>

    <div class="grid g2" style="gap:clamp(20px,3vw,44px)">
      <div>
        <div class="eyebrow">What you bring</div>
        <ul class="ticks">
          <li>Whatever exists &mdash; a document, a repository, a prototype URL, a deck, or nothing but the problem.</li>
          <li>Read access to the code and data if there is code and data.</li>
          <li>The person who can actually decide. One call, not a committee tour.</li>
          <li>An honest account of what has already been tried and what it cost.</li>
        </ul>
      </div>
      <div>
        <div class="eyebrow">What you leave with</div>
        <ul class="ticks">
          <li><b>Findings &amp; Path</b> &mdash; a written memo, typically five to seven pages, inside five business days.</li>
          <li>An unsentimental read of what you have, including the parts that only look finished.</li>
          <li>The three or four things most likely to kill it, ranked.</li>
          <li>Which plan fits, why the other two do not, and an indicative cost and elapsed time.</li>
          <li>What we would do in your position if you never hired us.</li>
        </ul>
      </div>
    </div>

    <div class="gate" style="margin-top:clamp(32px,4vw,48px);margin-bottom:0">
      <div class="lbl">The minimum</div>
      <p>We do not open a plan below {FLOOR}.</p>
      <p class="sub">Below that number there is no version of this work that is honest about what it can deliver, so we do not sell one. If your budget is under the floor, take the Triage anyway and use the memo yourself &mdash; that is a legitimate outcome and we will write it that way.</p>
      <div class="exc">
        <div class="lbl">And no free diagnostics</div>
        <p>Scoping calls, prototype reviews, architecture opinions and &ldquo;can I pick your brain&rdquo; all resolve to the same place: <b>the Triage</b>. One fee, one memo, credited if you proceed.</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- chooser -->
<section class="bord" id="plans">
  <div class="shell">
    <p class="eyebrow">Which one are you?</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(26px,3vw,40px)">Pick the sentence that sounds like your situation.</h2>
    <div class="grid g3">

      <a class="card" href="#blueprint" style="border-top:3px solid var(--cobalt)">
        <div class="kicker" style="color:var(--cobalt)">Plan A &middot; Blueprint</div>
        <h3 style="margin-bottom:14px">&ldquo;I have an idea, and no idea how to start.&rdquo;</h3>
        <p>There is a real problem you keep running into and a real business hiding in it. There is no code, no spec, and no defensible answer yet to what it costs or whether it works.</p>
        <span class="fig" style="font-size:clamp(24px,2.6vw,32px);margin-bottom:0">{A_PRICE}<small>4 weeks &middot; fixed</small></span>
        <span class="tlink" style="margin-top:18px">What Blueprint delivers <span class="arrow">&rarr;</span></span>
      </a>

      <a class="card" href="#buildout" style="border-top:3px solid var(--signal)">
        <div class="kicker" style="color:var(--signal)">Plan B &middot; Buildout</div>
        <h3 style="margin-bottom:14px">&ldquo;I built a proof of concept. It demos well and I do not trust it.&rdquo;</h3>
        <p>Claude, Cursor, Replit or a weekend of nerve got something working. It falls over at user ten, the auth is improvised, and nobody can tell you what it costs at scale.</p>
        <span class="fig" style="font-size:clamp(24px,2.6vw,32px);margin-bottom:0">{B_PRICE}<small>10&ndash;14 weeks &middot; fixed</small></span>
        <span class="tlink" style="margin-top:18px">What Buildout delivers <span class="arrow">&rarr;</span></span>
      </a>

      <a class="card" href="#venture" style="border-top:3px solid var(--bronze)">
        <div class="kicker" style="color:var(--bronze)">Plan C &middot; Venture</div>
        <h3 style="margin-bottom:14px">&ldquo;I want a company, not a project.&rdquo;</h3>
        <p>Everything above, plus the entity, the economics, the launch, and an investor package built to survive diligence. You want us materially inside the business, not adjacent to it.</p>
        <span class="fig" style="font-size:clamp(24px,2.6vw,32px);margin-bottom:0">From {C_PRICE}<small>6&ndash;9 months &middot; plus {C_EQUITY} equity</small></span>
        <span class="tlink" style="margin-top:18px">What Venture delivers <span class="arrow">&rarr;</span></span>
      </a>

    </div>
    <p class="fine" style="margin-top:20px;max-width:74ch">Between two of them? That is the ordinary case, and it is what the Triage decides. We would rather move you down a plan than sell you up one, every time.</p>
  </div>
</section>

<!-- ---------------------------------------------------------------- plan A -->
<section class="on-warm bord" id="blueprint">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(28px,3.4vw,42px)">
      <div>
        <p class="eyebrow" style="color:var(--cobalt)">Plan A</p>
        <h2>Blueprint.</h2>
        <span class="fig" style="margin-top:20px;color:var(--cobalt)">{A_PRICE}<small>4 weeks &middot; fixed &middot; 60 / 40</small></span>
        <p class="small" style="margin-top:18px">Run by <a class="tlink" href="studio.html">Bailiwick Venture Studio</a> &mdash; the first three phases of its six-phase process, plus a build specification.</p>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">Blueprint answers the question that stops most founders before they start: <i>what exactly am I building, and is it worth building?</i> You end the month with a venture designed as a whole system and a specification precise enough that a competent engineer &mdash; or a competent engineer paired with AI &mdash; can begin on the Monday.</p>
        <p class="body">No code is written. That is deliberate. Building before this work is done is how people spend forty thousand dollars discovering that the thing they built was not the business.</p>
      </div>
    </div>

    <p class="eyebrow" style="margin-bottom:14px">What Blueprint delivers &mdash; eight named deliverables</p>
    <div class="phases p4">
      <div class="phase"><div class="pn">01</div><h4>Venture architecture</h4><p>Thesis, customer, category, and the value exchange. What this is, and the adjacent things it is deliberately not.</p></div>
      <div class="phase"><div class="pn">02</div><h4>Risk &amp; asymmetry map</h4><p>What kills it, ranked. Where a small investment produces a disproportionate result. Which assumption to test first.</p></div>
      <div class="phase"><div class="pn">03</div><h4>Unit economics</h4><p>A working model, not a slide. Cost to serve, price, margin, and the honest breakeven. Including AI inference cost.</p></div>
      <div class="phase"><div class="pn">04</div><h4>Product definition</h4><p>The workflows, the data model, and the ruthless first cut of what does not get built in version one.</p></div>
      <div class="phase"><div class="pn">05</div><h4>Build specification</h4><p>Scoped work, architecture direction, stack recommendation, and acceptance criteria. Executable by us or by anyone else.</p></div>
      <div class="phase"><div class="pn">06</div><h4>Capital shape</h4><p>What reaching proof costs, what it should be funded with, and whether it needs outside money at all.</p></div>
      <div class="phase"><div class="pn">07</div><h4>Walkthrough</h4><p>A recorded 60-minute session on the whole package, with your engineers or advisors in the room if you want them.</p></div>
      <div class="phase"><div class="pn">08</div><h4>Thirty days after</h4><p>Email access to Michael for thirty days following delivery, for the questions that only surface once you start.</p></div>
    </div>

    <div class="gate" style="margin-top:clamp(28px,3.4vw,42px);margin-bottom:0;border-color:var(--cobalt)">
      <div class="lbl" style="color:var(--cobalt)">Not included in Blueprint</div>
      <p>Working software, visual design, and anything investor-facing.</p>
      <p class="sub">No code, no design comps, no prototype, no pitch deck, no incorporation, no fundraising. Blueprint produces the decision and the specification. Building it is Plan&nbsp;B; funding it is Plan&nbsp;C.</p>
      <div class="exc">
        <div class="lbl">Payment</div>
        <p><b>60% at signature, 40% on delivery.</b> Fixed at signature for the named scope. Blueprint credits in full against Plan&nbsp;B or Plan&nbsp;C started within ninety days &mdash; the specification is the input to both, so you never pay for the same discovery twice.</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- plan B -->
<section class="bord" id="buildout">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(28px,3.4vw,42px)">
      <div>
        <p class="eyebrow" style="color:var(--signal)">Plan B</p>
        <h2>Buildout.</h2>
        <span class="fig" style="margin-top:20px;color:var(--signal)">{B_PRICE}<small>10&ndash;14 weeks &middot; fixed &middot; 40 / 30 / 30</small></span>
        <p class="small" style="margin-top:18px">Run by <a class="tlink" href="vibe.html">BailiwickVibe</a> &mdash; phases 01 through 04 of its eight-phase method, carried through to a deployed system.</p>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">A prototype that demos is not a product. Buildout is the finish carpentry: the same idea, rebuilt on foundations that hold when real users, real data and real money arrive &mdash; and documented so that no single person, us included, is load-bearing.</p>
        <p class="body">We keep what works. Refactoring is surgical and confined to the core path; we are not here to rewrite your prototype for the pleasure of rewriting it.</p>
      </div>
    </div>

    <p class="eyebrow" style="margin-bottom:14px">What Buildout delivers &mdash; eight named deliverables</p>
    <div class="phases p4">
      <div class="phase"><div class="pn">01</div><h4>Structural diagnostic</h4><p>Five lenses &mdash; architecture, security, data integrity, scalability, deployment readiness &mdash; scored, with findings ranked by consequence.</p></div>
      <div class="phase"><div class="pn">02</div><h4>Production architecture</h4><p>The target design, the migration path, and the refactor itself across the core path. Agreed in writing before code moves.</p></div>
      <div class="phase"><div class="pn">03</div><h4>Security &amp; data integrity</h4><p>Authentication, secret handling, tenancy isolation, PII treatment, and an audit trail that survives being asked about.</p></div>
      <div class="phase"><div class="pn">04</div><h4>Scale &amp; cost</h4><p>Behavior and unit cost at 1&times;, 10&times; and 100&times;, with AI inference governed rather than hoped about.</p></div>
      <div class="phase"><div class="pn">05</div><h4>Governance &amp; IP</h4><p>The structure that turns working software into technology that can be licensed, transferred, diligenced and defended.</p></div>
      <div class="phase"><div class="pn">06</div><h4>Deployment</h4><p>CI/CD, environments, monitoring, alerting, and a runbook written for whoever is holding the pager at 3 a.m.</p></div>
      <div class="phase"><div class="pn">07</div><h4>Engineering handoff</h4><p>Documentation any competent team can continue from. Delivered as a named artifact, not as goodwill.</p></div>
      <div class="phase"><div class="pn">08</div><h4>Thirty days live</h4><p>Post-deployment support for thirty days: defect resolution against the acceptance criteria, at our cost.</p></div>
    </div>

    <div class="gate" style="margin-top:clamp(28px,3.4vw,42px);margin-bottom:0;border-color:var(--signal)">
      <div class="lbl" style="color:var(--signal)">Not included in Buildout</div>
      <p>New features, new platforms, and certifications we cannot issue.</p>
      <p class="sub">Net-new feature development beyond the agreed core path, native mobile applications unless separately scoped, and formal certification audits. We architect toward SOC&nbsp;2 and comparable regimes; the audit itself belongs to an accredited third party and is billed by them, not by us. Fundraising materials and go-to-market are Plan&nbsp;C.</p>
      <div class="exc">
        <div class="lbl">Payment</div>
        <p><b>40% at signature, 30% at architecture sign-off, 30% at deployment acceptance.</b> Fixed at signature for the named scope. If the diagnostic finds the prototype is materially worse than the Triage could see, we stop, re-price in writing, and you decide &mdash; we do not spend your budget quietly.</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- plan C -->
<section class="on-ink" id="venture">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(28px,3.4vw,42px)">
      <div>
        <p class="eyebrow">Plan C</p>
        <h2>Venture.</h2>
        <span class="fig" style="margin-top:20px">From {C_PRICE}<small>6&ndash;9 months &middot; staged &middot; plus {C_EQUITY} equity</small></span>
        <p class="small" style="margin-top:18px">Studio and <a class="tlink" href="vibe.html">BailiwickVibe</a> together &mdash; whatever of Plans A and B applies, plus phases 05 through 08 of the Vibe method.</p>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">Plan C is for the founder who does not want a vendor. It is the whole arc: architect it, build it properly, incorporate it, price it, launch it, and put an investor package in front of the market that holds up under diligence &mdash; with Michael in the room for the conversations that matter. Your company, your team, your cap table; we are alongside it, not inside it.</p>
        <p class="body" style="margin-bottom:0">The cash number is lower than the work is worth, and the equity is why. It is still a <b>fixed fee for the work</b> &mdash; payable whether or not a financing ever happens &mdash; and the equity percentage is negotiated and agreed before the engagement begins. Neither number moves with what you raise.</p>
      </div>
    </div>

    <p class="eyebrow" style="margin-bottom:14px">What Venture delivers &mdash; eight named deliverables</p>
    <div class="phases p4">
      <div class="phase"><div class="pn">01</div><h4>Everything applicable</h4><p>Whatever of Blueprint and Buildout your situation needs, run as one continuous engagement rather than three purchases.</p></div>
      <div class="phase"><div class="pn">02</div><h4>Economic simulation</h4><p>ARPU, CAC, LTV, payback and breakeven across three scenarios over twenty-four months, built as a model an investor can open and interrogate.</p></div>
      <div class="phase"><div class="pn">03</div><h4>Entity &amp; cap table</h4><p>Formation, founder vesting, option pool, minority protections, and decision rights calibrated to what you actually want to control.</p></div>
      <div class="phase"><div class="pn">04</div><h4>IP consolidation</h4><p>Every asset assigned to the company, cleanly, with the contractor and AI-authorship gaps closed before a diligence lawyer finds them.</p></div>
      <div class="phase"><div class="pn">05</div><h4>Go-to-market</h4><p>Positioning, pricing, channel, and a named sequence for the first hundred customers. A ninety-day launch plan with KPIs attached.</p></div>
      <div class="phase"><div class="pn">06</div><h4>Investor package</h4><p>Deck, model, data room, and diligence readiness &mdash; assembled to answer questions before they are asked.</p></div>
      <div class="phase"><div class="pn">07</div><h4>Michael in the room</h4><p>Investor meetings and partner conversations, as an advisor with equity in the outcome rather than a consultant on the sideline.</p></div>
      <div class="phase"><div class="pn">08</div><h4>A seat, if you want one</h4><p>Board observer or advisor seat through the raise. A perspective at the table, never a control position.</p></div>
    </div>

    <div class="gate" style="margin-top:clamp(28px,3.4vw,42px);margin-bottom:0">
      <div class="lbl">What Plan C is not</div>
      <p>It is not a guarantee of funding, and we are not your banker.</p>
      <p class="sub">No one can promise a raise, and anyone who does is selling something else. We build the case; the market decides. Bailiwick Ventures is not a broker-dealer, does not place securities, and takes <b>no compensation of any kind that is contingent on, or measured by, a financing</b> &mdash; no success fee, no percentage of proceeds, no finder's fee, no warrant tied to a round. The cash fee is fixed, is earned by the work, and is payable whether or not you ever raise a dollar.</p>
      <div class="exc">
        <div class="lbl">The equity, plainly</div>
        <p><b>{C_EQUITY} common stock, or advisor warrants where a cap table already exists.</b> The percentage is negotiated and fixed in writing <i>before</i> the engagement begins &mdash; never left to the end, never adjusted by the outcome. It vests on a time schedule across the engagement and is documented in the engagement agreement. Cash is a fixed fee, staged monthly against named milestones. If you never raise, the fee was still earned and the equity still stands &mdash; that was the risk we both took.</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- honesty -->
<section class="bord on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Fit</p>
      <h2>When not to hire us.</h2>
      <p class="small" style="margin-top:18px">Published because the Triage will tell you anyway, and it is cheaper for both of us if you read it first.</p>
    </div>
    <div>
      <ol class="crit">
        <li><b>You need hands, not architecture.</b> If what you want is a contractor at an hourly rate to execute a plan you already have, a good agency will serve you better and cost less.</li>
        <li><b>You want the decision validated.</b> If it has already been made and the assignment is agreement, we are the wrong purchase. We will say what we find.</li>
        <li><b>Your plan budget is under {FLOOR}.</b> Take the Triage, keep the memo, and go build. That is a real answer, not a brush-off.</li>
        <li><b>You are in a regulated category without counsel.</b> Payments, health, alcohol, lending, childcare: engage a lawyer before you engage us, not after.</li>
        <li><b>You need someone in the org chart.</b> We are not fractional executives, not interim staff, and not recruiters. If the gap is a person rather than a scope, hire the person &mdash; ideally someone you have already worked with.</li>
        <li><b>You need it in three weeks.</b> Blueprint is four, Buildout is ten at the fastest, and compressing either produces the thing you were trying to escape.</li>
      </ol>
      <p class="fine" style="margin-top:22px">We run {CONCURRENT} engagements at a time. When those are full, the Triage still runs and the plan is scheduled &mdash; we do not take work we cannot staff.</p>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- FAQ -->
<section class="bord" id="faq">
  <div class="shell">
    <p class="eyebrow">The granular version</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(28px,3.4vw,44px)">Questions we would ask if we were buying this.</h2>

    <div class="grid g2" style="gap:clamp(26px,3.4vw,52px)">

      {_faq_group("Choosing a plan", [
        ("I am between two plans. What happens?",
         "<p>That is the ordinary case and it is what the Triage resolves. The memo names one plan and explains why the other does not fit. Our bias is downward: an oversold engagement produces a client who never refers anyone, and referrals are the entire business.</p>"),
        ("Can I do Plan A now and Plan B later?",
         f"<p>Yes, and it is the most common path. Blueprint&rsquo;s build specification is Buildout&rsquo;s input, so nothing is repeated. Blueprint credits in full against Plan&nbsp;B or Plan&nbsp;C begun within ninety days of delivery &mdash; you never pay twice for the same discovery.</p>"),
        ("What if the Triage says none of them fit?",
         "<p>Then the memo says that, in writing, with the reasoning. You keep the document. Roughly speaking, if we cannot see a path we will not invent one to fill a slot in the calendar.</p>"),
        ("I already have engineers. Does that change anything?",
         "<p>For Blueprint and Buildout, no &mdash; we work alongside internal teams routinely, and the engineering handoff is designed for exactly that. Plan&nbsp;C assumes we are materially inside the company, so it is a conversation about roles before it is a conversation about price.</p>"),
        ("Do you work outside the United States?",
         "<p>Yes, in English, on a workable timezone overlap. Entity formation and cap table work under Plan&nbsp;C is US-centric; outside the US we coordinate with your local counsel rather than pretending to be it.</p>"),
      ])}

      {_faq_group("Scope and change control", [
        ("What counts as a change order?",
         "<p>Anything not named in the engagement schedule. Every plan ships with a schedule listing deliverables by name and by acceptance condition, so the boundary is a document rather than a memory. Changes are priced and agreed <i>before</i> the work starts &mdash; never discovered on an invoice.</p>"),
        ("Who decides when a phase is finished?",
         "<p>The acceptance condition in the schedule, and your written acceptance against it. If a deliverable does not meet its stated condition, we fix it at our cost. If it does and you want something more, that is a change order.</p>"),
        ("My thinking will change during the engagement. Is that a problem?",
         "<p>In Blueprint it is expected &mdash; changing your mind is what the month is for. In Buildout it depends on whether the change is direction or foundation. Direction is usually absorbable; foundation is a re-price. We will tell you which one you are proposing on the day you propose it.</p>"),
        ("What if my prototype turns out to be worse than it looked?",
         "<p>The Triage exists to find that before you sign. If it emerges later anyway, we stop, put the finding and a revised price in writing, and you decide whether to continue. We do not spend a budget quietly and present the problem at the end.</p>"),
        ("Can we pause?",
         "<p>Once, for up to sixty days, at a phase boundary. Beyond that the engagement closes and re-opens at current pricing, because holding a team idle is a cost somebody pays.</p>"),
      ])}

      {_faq_group("Who does the work", [
        ("Is Michael personally involved, or is this a brochure?",
         "<p>Personally involved in every engagement: the architecture, the judgment calls, the Triage memo, and the client relationship. He is not the person writing every line of code, and any firm that tells you their founder is should be asked how many clients they have.</p>"),
        ("Who writes the code?",
         "<p>A small senior team working with AI pair-programming under human architecture review. Nothing is offshored, nothing is body-shopped, and no junior is left unsupervised on your foundation. The tools are modern; the review discipline is not.</p>"),
        ("How many engagements do you run at once?",
         f"<p>{CONCURRENT.capitalize()}. It is a real constraint rather than a scarcity tactic &mdash; the work depends on senior attention, and senior attention does not divide indefinitely. When the slots are full, the Triage still runs and your plan is scheduled with a start date.</p>"),
        ("Are you a fractional CTO, CFO, or interim executive?",
         "<p>No. We are not fractional staff and we do not take operating roles or titles inside your company. An engagement is a defined scope with named deliverables and an end date; Plan&nbsp;C adds a board observer or advisor seat, which is a seat, not a job. If what you need is someone in the org chart, you need to hire that person, and we will say so.</p>"),
        ("What happens if you disappear?",
         "<p>Every plan ships an engineering handoff written so another competent team can continue without us. It is a named deliverable with an acceptance condition, not a courtesy. Key-person risk is a thing we remove, not a thing we sell.</p>"),
      ])}

      {_faq_group("Ownership and intellectual property", [
        ("Who owns what you build?",
         "<p>You do, on final payment: code, data model, documentation, models, specifications, and the deliverables in full. Assignment is written into the engagement agreement rather than left to be argued about later.</p>"),
        ("What about your frameworks and methods?",
         "<p>Those remain ours. On payment in full you receive a perpetual license to use anything of ours embedded in your deliverables, for the life of the venture. What you do not receive is the right to resell the method itself as a service.</p>"),
        ("Do you reuse our work with other clients?",
         "<p>Never anything client-specific &mdash; not your code, your data, your model, your positioning, or your name. Generic engineering patterns and our own internal libraries travel, as they do at every firm; your business does not.</p>"),
        ("Is FohBoh technology involved, and who benefits if it is?",
         "<p>Only where a venture genuinely needs certified, audit-defensible metrics. FohBoh.ai is a separate company in which Bailiwick Ventures holds an interest, so any use of its technology is a related-party arrangement: it is disclosed to you before it is proposed, licensed and priced separately by FohBoh, and never a condition of working with us. If a competing product fits better, we will say so.</p>"),
        ("Will you sign our NDA?",
         "<p>Yes, a mutual one, before the Triage. We will not sign non-competes that would bar us from an entire sector, and we will tell you plainly if we are already working in an adjacent space.</p>"),
      ])}

      {_faq_group("Money", [
        ("Is the Triage fee genuinely credited?",
         f"<p>In full, against any plan booked within {CREDIT_DAYS} of the memo&rsquo;s delivery. One Triage, one credit. There is no clawback, no partial credit, and no small print reducing it.</p>"),
        ("What are the payment schedules?",
         f"<p><b>Blueprint</b> &mdash; 60% at signature, 40% on delivery. <b>Buildout</b> &mdash; 40% at signature, 30% at architecture sign-off, 30% at deployment acceptance. <b>Venture</b> &mdash; staged monthly against named milestones, with the equity documented at the start. Invoices are net 15.</p>"),
        ("Can either of us stop?",
         "<p>Yes, in writing, at a stage boundary. You pay for work completed to that point, and everything delivered and paid for is yours to keep and to use. There is no termination penalty in either direction and no exit fee.</p>"),
        ("Do you give refunds?",
         "<p>We do not refund completed work that met its acceptance condition. We do repair, at our own cost, any deliverable that did not. Those are different questions and we treat them differently.</p>"),
        ("What about expenses?",
         "<p>Travel and third-party costs &mdash; hosting, licenses, audits, data &mdash; are billed at cost with receipts, and anything above $500 is approved by you first. We do not mark up pass-throughs.</p>"),
        ("Do the published prices ever move?",
         "<p>Blueprint and Buildout are fixed at signature for the named scope; for that scope, the number on this page is the number on the agreement. Published pricing may change for future engagements, and it never changes retroactively for a signed one.</p>"),
      ])}

      {_faq_group("Plan C and the equity", [
        ("Why take equity at all?",
         "<p>Because Plan&nbsp;C is us carrying venture risk with you over six to nine months, and a pure-cash price for that work would exceed what almost any founder can pay at this stage. Equity is what makes the cash number reachable. It also means we are wrong at the same time you are.</p>"),
        ("How much, and what class?",
         f"<p>{C_EQUITY} of common stock, or advisor warrants where a cap table already exists and issuing common would be disruptive. The exact figure is set by scope and cash mix at the start of the engagement, not negotiated at the end of it.</p>"),
        ("How does it vest?",
         "<p>On a time schedule across the engagement, written into the agreement. There is no acceleration tied to a financing, a sale, or any other transaction &mdash; vesting is a function of time served, nothing else. If we stop early, unvested equity does not vest, the same discipline you would apply to a founder.</p>"),
        ("Do you take a percentage of what we raise?",
         "<p>No, in every form the question can take: no success fee, no finder&rsquo;s fee, no percentage of proceeds, no warrant tied to a round, no bonus on a close. Bailiwick Ventures is not a broker-dealer and does not place securities. Our compensation is a <b>fixed cash fee for the work</b> plus an equity percentage <b>negotiated before the engagement starts</b>. Both are set before anyone knows what you will raise, and neither changes afterward.</p>"),
        ("Do you guarantee we will get funded?",
         "<p>No, and neither can anyone else. We build the strongest honest case for the venture and stand behind it in the room. Whether the market says yes is the market&rsquo;s decision, and a firm that promises otherwise is describing a service it cannot deliver.</p>"),
        ("Will you build our team, or help us hire?",
         "<p>We are not recruiters and we do not staff your company. We will make introductions where we know someone worth knowing, and we will help you think about what a role actually needs before you open it &mdash; but the hiring is yours to do and yours to own.</p>"),
        ("Any advice on how we should build the team, then?",
         "<p>One piece, strongly: hire people you have already worked with. A team assembled from strangers in the weeks before a raise is a diligence problem, not an achievement &mdash; investors read it as unproven, and they are usually right. Founders who have shipped something difficult together carry evidence that no r&eacute;sum&eacute; provides. Start there, and fill the genuine gaps afterward.</p>"),
        ("Do you take a board seat?",
         "<p>An observer or advisor seat through the raise, if you want one. Not a control position, not a blocking right, and not a permanent fixture &mdash; the seat is there to be useful during the period we are inside the business.</p>"),
        ("Would Bailiwick also invest?",
         "<p>Occasionally, and separately. Any investment is a distinct decision on ordinary terms alongside other investors, documented apart from the engagement. Being a client creates no obligation on us to invest, and an investment creates no discount on the work.</p>"),
      ])}

      {_faq_group("Timing and what we need from you", [
        ("When can you start?",
         "<p>The Triage typically within two weeks of payment; the memo within five business days of the session. Plan start depends on the slots &mdash; we will give you a real date at Triage rather than an encouraging one.</p>"),
        ("What do you need from us to hit the timeline?",
         "<p>A decision-maker who responds inside two business days, access to systems and data on day one rather than week three, and one person empowered to say yes. Those three things account for most of the difference between a plan that lands on schedule and one that does not.</p>"),
        ("What actually causes overruns?",
         "<p>In order: slow client decisions, missing access to data or systems, and changes to the foundation rather than the surface. Technical surprises are a distant fourth, because the Triage and the diagnostic are built to find them early.</p>"),
        ("What do you not do at any price?",
         "<p>Staff augmentation, hourly work, fixed-bid responses to RFPs, taking over management of an existing engineering team, recruiting or placing staff, fractional or interim executive roles, and building anything we would have to be dishonest to sell. Also: engagements that skip the Triage, and free work of any description.</p>"),
      ])}

    </div>

    <div class="legal">
      <h4>Notes on this page</h4>
      <p>Prices shown are for engagements contracted with Bailiwick Ventures,&nbsp;Inc. and are quoted in US dollars, exclusive of applicable taxes and of third-party pass-through costs. Blueprint and Buildout are fixed-price for the scope named in the engagement schedule; Plan&nbsp;C pricing begins at the figure shown and is set by scope. Published pricing may change for future engagements and never changes retroactively for a signed one.</p>
      <p>Nothing on this page is an offer of securities, investment advice, legal advice, or tax advice. Bailiwick Ventures,&nbsp;Inc. is not a registered broker-dealer or investment adviser, does not place securities, and accepts no transaction-based compensation in connection with any financing. Cash fees under every plan are fixed fees for services rendered and are not contingent on, reduced by, or measured against the outcome of any financing. Equity compensation under Plan&nbsp;C is consideration for services, negotiated and fixed in writing before the engagement begins, vesting on a time schedule, and documented in the engagement agreement; it carries no acceleration or adjustment tied to a financing or other transaction. Bailiwick Ventures does not recruit, place, or supply personnel, and does not accept operating or interim executive roles in client companies. Founders should engage their own counsel on entity, securities, and tax matters.</p>
      <p>Bailiwick Ventures,&nbsp;Inc. holds an interest in FohBoh.ai. Where FohBoh technology is proposed as part of a client solution, that relationship is disclosed in advance and the technology is licensed and priced separately by FohBoh.ai. It is never a condition of engagement.</p>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------------- CTA -->
<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:22ch;margin:0 auto">Every plan starts the same way.</h2>
    <p class="body" style="margin:18px auto 0;max-width:52ch">Ninety minutes, a written assessment of what you actually have, and a straight answer about which plan fits &mdash; credited in full if you proceed.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="contact.html">Book the Triage &mdash; {TRIAGE} <span class="arrow">&rarr;</span></a>
      <a class="btn btn-s" href="#faq">Read the Detail <span class="arrow">&rarr;</span></a>
    </div>
    <p class="fine" style="margin-top:18px">Select <b>Plans &amp; Pricing</b> as the nature of your inquiry, and tell us which sentence sounded like you.</p>
  </div>
</section>
"""
