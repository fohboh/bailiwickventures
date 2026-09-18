"""The Production Gate — where the BailiwickVibe 8-phase method stops being
advice and becomes evidence.

Two of the eight phases end at a gate rather than a review. Gate 1
(Readiness-Certified) is the five-lens Venture Readiness score from phase 01,
scored by rule and sealed; it is Buildout's first deliverable. Gate 2
(Traction-Certified) measures the 90-day actuals against the phase 05 model
and seals the finding; it lives in Venture (phases 05-08).

Prices and the Triage URL are imported from pages_f so that nothing is
restated here. The funnel graphic is drawn as inline SVG in the site palette;
vermilion marks a gate, steel marks a hand-off.
"""

from pages_f import TRIAGE, FLOOR, TRIAGE_URL, CREDIT_DAYS

# ---------------------------------------------------------------- graphic

_F = 'font-family="Inter,Helvetica,Arial,sans-serif"'
_SER = "font-family=\"'Source Serif 4',Georgia,serif\""

def _box(x, y, w, h, fill="#FFFDF9", stroke="#E0D8CB", sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def _t(x, y, txt, size=12.5, fill="#14181D", w="", anchor="", ff=_F, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ''
    wt = f' font-weight="{w}"' if w else ''
    return f'<text x="{x}" y="{y}"{a} {ff} font-size="{size}"{wt} fill="{fill}"{extra}>{txt}</text>'

def _head(x, y, w, label, sub):
    return (_box(x, y, w, 40, "#12304F", "#12304F")
            + _t(x + 14, y + 25, sub, 11, "#9FB3C8", "700", extra=' letter-spacing="1.5"')
            + _t(x + w - 14, y + 25, label, 14, "#fff", "700", "end"))

def _band(y, label):
    lw = len(label) * 8.4 + 30
    return (_t(40, y, label, 12, "#6B8AA6", "700", extra=' letter-spacing="2"')
            + f'<line x1="{40 + lw}" y1="{y - 4}" x2="1010" y2="{y - 4}" stroke="#E0D8CB"/>')

def _card(x, y, w, title, lines, fill="#F6F2EC", stroke="#E0D8CB", sw=1):
    o = _box(x, y, w, 26 + 18 * len(lines) + 12, fill, stroke, sw) + _t(x + 12, y + 20, title, 12.5, "#14181D", "700")
    for i, l in enumerate(lines):
        o += _t(x + 12, y + 40 + 18 * i, l, 12.5, "#4A5560")
    return o

def _v(x, y1, y2, color="#6B8AA6", arrow=False, sw=1.5):
    m = ' marker-end="url(#pg-ahv)"' if (arrow and color == "#E2551F") else (' marker-end="url(#pg-ah)"' if arrow else '')
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{m}/>'

def _h(x1, x2, y):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#6B8AA6" stroke-width="1.5"/>'

def _gate(y, n, title, big, small):
    return (_box(150, y, 700, 86, "#FFFDF9", "#E2551F", 2.5)
            + _t(172, y + 25, f"GATE {n} · {title}", 11, "#E2551F", "700", extra=' letter-spacing="2"')
            + _t(172, y + 49, big, 19, "#14181D", "600", ff=_SER)
            + _t(172, y + 71, small, 12.5, "#4A5560"))

def _svg():
    o = []
    o.append(_t(530, 44, "The Production Gate", 30, "#14181D", "600", "middle", _SER))
    o.append(_t(530, 70, "WHERE THE 8-PHASE VENTURE ARCHITECTURE STOPS BEING ADVICE AND BECOMES EVIDENCE", 13, "#4A5560", anchor="middle", extra=' letter-spacing="2.5"'))

    o.append(_band(118, "PHASES 01–02 · DIAGNOSE THE PROTOTYPE"))
    o.append(_head(150, 134, 320, "Structural Diagnostic", "01")); o.append(_head(590, 134, 320, "Risk & Asymmetry Mapping", "02"))
    o.append(_card(150, 190, 320, "Five lenses, one scored assessment", ["Architecture · Security", "Data integrity · Scalability", "Deployment readiness", "Prioritized findings — including “don’t build this”"]))
    o.append(_card(590, 190, 320, "Where the frame will fail, and where it pays", ["Single points of failure", "Leverage points", "Asymmetric bets — small spend, outsized return", "Baseline the numbers the venture must move"]))
    o.append(_v(310, 300, 340)); o.append(_v(750, 300, 340)); o.append(_h(310, 750, 340)); o.append(_v(530, 340, 362, "#E2551F", True, 2))
    o.append(_gate(366, 1, "READINESS-CERTIFIED", "No refactor starts on a score nobody can reproduce.", "Scored by rule across five lenses · findings sealed SHA-256 · same prototype, same score, every time"))

    o.append(_v(530, 452, 486, "#E2551F", True, 2))
    o.append(_band(482, "PHASES 03–06 · ARCHITECT THE VENTURE"))
    o.append(_head(60, 498, 300, "Integrated Venture Design", "03")); o.append(_head(380, 498, 300, "Governance & IP", "04")); o.append(_head(700, 498, 300, "Economics & Capital", "05–06"))
    o.append(_card(60, 554, 300, "Finish carpentry", ["Production architecture · refactor", "Migration plan", "Engineering handoff any team can continue"]))
    o.append(_card(380, 554, 300, "The mechanism behind both gates", ["Deterministic governance — rules, not opinions", "Audit-defensible records from day one", "IP that is licensable, transferable, defensible"], "#F6F2EC", "#12304F", 1.5))
    o.append(_card(700, 554, 300, "The model the venture will be held to", ["Hosting, inference, margin at 1× · 10× · 100×", "ARPU · CAC · LTV · breakeven, 24 months", "Cap table bootstrap → seed · decision rights"]))
    o.append(_v(210, 646, 680)); o.append(_v(530, 646, 680)); o.append(_v(850, 646, 680)); o.append(_h(210, 850, 680)); o.append(_v(530, 680, 712, arrow=True))
    o.append(_t(546, 702, "handoff complete → launch", 11.5, "#4A5560"))

    o.append(_band(742, "PHASES 07–08 · PROVE IT"))
    o.append(_head(150, 758, 320, "Go-to-Market & Launch", "07")); o.append(_head(590, 758, 320, "Investor & Acquisition Readiness", "08"))
    o.append(_card(150, 814, 320, "Ship it, watch it", ["Launch playbook · CI/CD · monitoring", "90-day plan with KPIs", "Growth scenarios, tracked against the model"]))
    o.append(_card(590, 814, 320, "The package a buyer or investor opens", ["Pitch deck · buyer briefings · demo materials", "Data room", "Exit path: raise, partner, or sell"]))
    o.append(_v(310, 906, 940)); o.append(_v(750, 906, 940)); o.append(_h(310, 750, 940)); o.append(_v(530, 940, 962, "#E2551F", True, 2))
    o.append(_gate(966, 2, "TRACTION-CERTIFIED", "The 90-day numbers are measured against the model, then sealed.", "Actual vs. modeled ARPU, CAC, margin · narrative sealed SHA-256 · reproducible from the data room"))
    o.append('<path d="M850,1009 H1010 V546 H850 V551" fill="none" stroke="#6B8AA6" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#pg-ah)"/>')
    o.append(_t(1034, 780, "misses → back to the model → re-forecast → the data room carries the corrected record", 11.5, "#4A5560", anchor="middle", extra=' transform="rotate(-90 1034 780)"'))
    o.append(_v(530, 1052, 1084, arrow=True))
    o.append(_box(250, 1088, 560, 44, "#F6F2EC")); o.append(_t(530, 1108, "Venture ready — with a record", 13, "#14181D", "700", "middle")); o.append(_t(530, 1124, "Sealed readiness score · certified traction · a data room that reproduces both", 11.5, "#4A5560", anchor="middle"))
    o.append(_t(40, 1166, "BAILIWICKVIBE · bailiwickventures.com/vibe.html", 11, "#6B8AA6", extra=' letter-spacing="1.5"'))
    o.append(_t(1040, 1166, "Vermilion marks a certification gate. Grey marks a hand-off.", 11, "#6B8AA6", anchor="end"))

    defs = ('<defs>'
            '<marker id="pg-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6B8AA6"/></marker>'
            '<marker id="pg-ahv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#E2551F"/></marker>'
            '</defs>')
    aria = ("The Production Gate inside the 8-Phase Venture Architecture: phases 01 and 02 diagnose the prototype and lead to Gate 1, "
            "Readiness-Certified; phases 03 to 06 architect the venture and lead to launch; phases 07 and 08 launch and package it and "
            "lead to Gate 2, Traction-Certified, with misses fed back to the economic model.")
    return (f'<svg viewBox="0 0 1060 1180" role="img" aria-label="{aria}" style="display:block;width:100%;max-width:1000px;height:auto;margin:0 auto">'
            + defs + "".join(o) + '</svg>')


# ---------------------------------------------------------------- page

_CSS = """
<style>
.pg-fig{background:var(--warm);border:1px solid var(--line);border-radius:3px;padding:clamp(16px,2.4vw,28px) clamp(10px,1.6vw,18px) 10px;overflow-x:auto;margin:0}
.pg-fig figcaption{font-size:13.5px;line-height:1.55;color:var(--body);padding:12px 8px 4px;max-width:80ch}
.pg-cmp{width:100%;border-collapse:collapse;font-size:15px;line-height:1.55}
.pg-cmp th{text-align:left;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--body);font-weight:700;padding:0 16px 10px 0;border-bottom:1px solid var(--line)}
.pg-cmp td{vertical-align:top;padding:14px 16px 14px 0;border-bottom:1px solid var(--line);color:var(--body)}
.pg-cmp td:first-child{font-weight:600;color:var(--ink);width:20%}
.pg-cmp td.us{color:var(--ink)}
.pg-cmp td.us b{color:var(--signal);font-weight:600}
.pg-opts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 20px}
.pg-opt{border:1px solid var(--line);background:var(--warm);border-radius:3px;padding:14px 16px;font-size:14.5px;line-height:1.5;color:var(--body)}
.pg-opt b{display:block;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--signal);margin-bottom:3px}
@media (max-width:760px){.pg-opts{grid-template-columns:1fr}.pg-cmp{display:block;overflow-x:auto}.pg-cmp td:first-child{width:auto}}
</style>
"""


def production_gate():
    return f"""{_CSS}
<div class="hero" style="background:linear-gradient(180deg,#FFFDF9 0%,#FFFDF9 60%,#F7F2EE 100%)">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow" style="color:var(--signal)">BailiwickVibe &middot; The Production Gate</p>
    <h1 style="max-width:16ch">A prototype passes a demo. A venture passes a gate.</h1>
    <p class="lede">The 8-Phase Venture Architecture takes a vibe-coded prototype to production-safe, scalable and investable. Two of those phases end at a gate instead of a review: a rule-based check with a sealed record of what passed, what failed, and why. This page shows where the gates sit and what they change.</p>
    <div class="btns">
      <a class="btn btn-p" href="{TRIAGE_URL}" target="_blank" rel="noopener" style="background:var(--signal);border-color:var(--signal)">Schedule the Triage &mdash; {TRIAGE} <span class="arrow">&#8599;</span></a>
      <a class="btn btn-s" href="vibe.html#method">The 8-Phase Method <span class="arrow">&rarr;</span></a>
    </div>
    <div class="tagline" style="color:var(--signal)"><span>A review is an opinion</span><i style="background:var(--signal)"></i><span>A gate is a record</span></div>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Why a gate, not a review</p>
      <h2>Two moments where opinion becomes a record.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:22px">A review is an opinion held by the people who built the thing, or who want it funded. It varies with the reviewer, the day, and how badly someone needs the answer to be yes.</p>
      <p class="body">A gate is a rule-based check whose result is sealed and reproducible. An investor, an acquirer, or the next engineering team can verify it without taking anyone&rsquo;s word &mdash; ours included. The method has eight phases; two of them end this way, and they are the two moments a diligence team asks about first.</p>
    </div>
  </div>
</section>

<section class="bord" id="funnel">
  <div class="shell">
    <p class="eyebrow">The method, with its gates</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(22px,2.6vw,32px)">Eight phases, two certification gates.</h2>
    <figure class="pg-fig">
      {_svg()}
      <figcaption>The two vermilion boxes are the difference. Every phase in this figure appears on the <a class="tlink" href="vibe.html#method">Method</a>. The gates are where a sealed, rule-based record replaces a judgment call: once after the diagnostic, once after the first ninety days live.</figcaption>
    </figure>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <div class="phases p3">
      <div class="phase"><div class="pn">PHASES 01&ndash;02</div><h4>Diagnose the prototype</h4><p>The Structural Diagnostic audits the prototype through five lenses &mdash; architecture, security, data integrity, scalability, deployment readiness. Risk &amp; Asymmetry Mapping finds the single points of failure and the places where a small investment yields an outsized return, and baselines the numbers the venture will have to move. If the honest finding is <i>don&rsquo;t build this</i>, the memo says so.</p></div>
      <div class="phase"><div class="pn">PHASES 03&ndash;06</div><h4>Architect the venture</h4><p>Integrated Venture Design is the finish carpentry: production architecture, the refactor, a migration plan, an engineering handoff any team can continue from. Governance &amp; IP Architecture is the mechanism behind both gates &mdash; deterministic governance and audit-defensible records. Economic Simulation and Capital &amp; Control Calibration produce the model the venture is held to at 1&times;, 10&times; and 100&times;.</p></div>
      <div class="phase"><div class="pn">PHASES 07&ndash;08</div><h4>Prove it</h4><p>Go-to-Market &amp; Launch ships it with CI/CD, monitoring, and a 90-day plan with KPIs tracked against the phase 05 model. Investor &amp; Acquisition Readiness assembles the package a buyer or investor opens. Misses go back into the model, the forecast is corrected, and the data room carries the corrected record rather than the original promise.</p></div>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">What makes it a gate</p>
    <div class="grid g2" style="margin-top:8px">
      <div class="gate" style="border-color:var(--signal);margin:0">
        <div class="lbl" style="color:var(--signal)">Gate 1 &middot; after the diagnostic</div>
        <p>Readiness-Certified.</p>
        <p class="sub">The usual version of this step is a senior developer reading the code and giving an opinion. Ours scores the prototype by rule across the five lenses, so the same prototype scores the same way twice, and the findings are hashed the moment they are written. The refactor starts from a number that can be reproduced, not a feeling. It is also the honest exit: a prototype that fails the gate gets the memo that says so, and the founder keeps the money they would have spent building on it.</p>
        <div class="exc">
          <div class="lbl">Where it lives</div>
          <p>The five-lens scored assessment is <b>Buildout&rsquo;s first deliverable</b>. The Triage is an experienced read that decides which plan fits; the gate is days of work inside the plan.</p>
        </div>
      </div>
      <div class="gate" style="border-color:var(--signal);margin:0">
        <div class="lbl" style="color:var(--signal)">Gate 2 &middot; after the first ninety days</div>
        <p>Traction-Certified.</p>
        <p class="sub">The usual version of this step is a screenshot of a dashboard on slide nine. Ours measures the 90-day actuals against the ARPU, CAC and margin the phase 05 model predicted, writes the findings into a narrative, and seals it. An investor or acquirer can reproduce the traction claim from the data room without trusting the founder&rsquo;s slide. That is what makes a venture investable rather than merely live.</p>
        <div class="exc">
          <div class="lbl">Where it lives</div>
          <p>Phases 05 through 08 are <b>Venture</b> work. The model is built in phase 05; the gate closes after the phase 07 launch plan has run for ninety days.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Side by side</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(22px,2.6vw,32px)">The usual path from prototype to launch, and where the Gate departs from it.</h2>
    <table class="pg-cmp">
      <thead><tr><th>Step</th><th>The usual path</th><th>The Production Gate</th></tr></thead>
      <tbody>
        <tr><td>Readiness</td><td>A senior developer&rsquo;s opinion after reading the code.</td><td class="us"><b>Scored by rule</b> across five lenses, findings sealed, reproducible.</td></tr>
        <tr><td>Governance</td><td>Added later, if ever &mdash; usually when a buyer asks.</td><td class="us"><b>Designed in phase 04.</b> Records are audit-defensible from the first commit after the refactor.</td></tr>
        <tr><td>Economics</td><td>A spreadsheet the founder built the night before the pitch.</td><td class="us"><b>Modeled at 1&times;, 10&times;, 100&times;</b> in phase 05 and used as the baseline the venture is measured against.</td></tr>
        <tr><td>Traction</td><td>A dashboard screenshot on slide nine.</td><td class="us"><b>Actuals vs. the model,</b> sealed, reproducible from the data room.</td></tr>
        <tr><td>Who vouches</td><td>The founder.</td><td class="us"><b>The record.</b> The team, the advisor or the agency can change without the evidence changing.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="bord on-warm">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(24px,3vw,36px)">
      <div>
        <p class="eyebrow">VIBE in action</p>
        <h2>The gates already ran once.</h2>
      </div>
      <div>
        <p class="body" style="margin-bottom:0">BailiwickQuikFix is the canonical example of the method &mdash; and of the record it leaves behind. Three apps, a licensed AI governance engine, and a complete investor package, architected, modeled, governed and packaged before a line of production infrastructure was paid for.</p>
      </div>
    </div>
    <div class="stats">
      <div><div class="v">6 weeks</div><div class="l">From vibe-coded prototype to a complete venture package.</div></div>
      <div><div class="v">15 documents</div><div class="l">From pitch deck to engineering handoff, each the output of a numbered phase. The data room is the Gate 2 record, not a marketing folder.</div></div>
      <div><div class="v">3 exit paths</div><div class="l">Sell the IP, raise seed, or partner with an operator &mdash; kept open by the same sealed record.</div></div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-top:clamp(22px,2.6vw,32px)">
      <p class="fine" style="margin:0;max-width:64ch"><b style="color:var(--ink)">Evidence policy.</b> The figures on this page are our own, from the QuikFix build. We do not publish industry statistics we cannot trace to a named source and date, and we do not publish illustrative numbers dressed as results.</p>
      <a class="btn btn-s" href="https://bailiwickvibe.com" target="_blank" rel="noopener">See the Case Study <span class="arrow">&#8599;</span></a>
    </div>
  </div>
</section>

<section class="bord" id="stuck">
  <div class="shell split">
    <div>
      <p class="eyebrow">Start here</p>
      <h2>Where does your prototype get stuck?</h2>
      <p class="small" style="margin-top:18px">Pick the stage. It is the first question the Triage asks, and the answer decides which plan we recommend.</p>
    </div>
    <div>
      <div class="pg-opts">
        <div class="pg-opt"><b>Structure</b>It demos well and breaks at user&nbsp;#10.</div>
        <div class="pg-opt"><b>Governance</b>There is no record an investor could audit.</div>
        <div class="pg-opt"><b>Economics</b>Nobody knows what it costs at 10&times; the users.</div>
        <div class="pg-opt"><b>Traction</b>It&rsquo;s live, and you can&rsquo;t prove it moved a number.</div>
      </div>
      <div class="btns">
        <a class="btn btn-p" href="{TRIAGE_URL}" target="_blank" rel="noopener" style="background:var(--signal);border-color:var(--signal)">Schedule the Triage &mdash; {TRIAGE} <span class="arrow">&#8599;</span></a>
        <a class="btn btn-s" href="plans.html">See All Three Plans <span class="arrow">&rarr;</span></a>
      </div>
      <p class="fine" style="margin-top:16px;max-width:70ch">Ninety minutes with Michael, a written Findings &amp; Path memo, credited in full against any plan booked within {CREDIT_DAYS}. No plan below {FLOOR}; compensation is never contingent on a financing.</p>
    </div>
  </div>
</section>
"""
