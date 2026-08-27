"""Investing, Portfolio, Studio, Vibe, Insights, Contact."""
from pages_a import more

CASES = """
<section class="bord on-warm">
  <div class="shell">
    <p class="eyebrow">Case studies</p>
    <h2 style="max-width:26ch">What the work actually produced.</h2>
    <p class="body" style="margin-top:18px;margin-bottom:clamp(28px,3.4vw,42px);max-width:64ch">Three ventures, three different problems, one method. Each began as a structural diagnosis rather than a product idea &mdash; and in each case the architecture is what made the business possible.</p>

    <div class="grid g3">

      <article class="card" style="border-left:2px solid var(--bronze)">
        <div class="kicker">Case study 01 &middot; Operating company</div>
        <h3>StarBar &middot; SnapCount</h3>
        <p><b>The problem.</b> Periodic inventory is still done on a clipboard and typed in afterward. It is slow, it is error-prone, and because it is unpleasant it gets done late or approximated &mdash; which corrupts every cost metric downstream of it. Beverage shrinkage runs 15&ndash;25% at industry average, and one ounce in five from a keg never generates revenue.</p>
        <p><b>What was architected.</b> SnapCount&trade;: per-shift, voice-driven counting against a locked watchlist. One item at a time, spoken, with tenthing for partial bottles. Mid-shift breakage and transfers are captured with a photo, so the variance math stays clean and custody is never inferred.</p>
        <p><b>What changed.</b> The count stops being a chore performed against the operator and becomes two minutes of talking &mdash; and stops being an estimate. Certification is deterministic: named opening count, named closing count, both inside the shift window, variance within threshold, trust score at or above 85, and no open exception. All six or it is not certified. Every certified event is SHA-256 anchored and publicly verifiable.</p>
        <p><b>The long way round.</b> The first version of this shipped on 17 March 2020 &mdash; the day American dining rooms closed. The product worked; the market disappeared. It was rebuilt on a certification layer that did not exist five years ago, which is why the count is now evidence rather than a number somebody typed in.</p>
        <dl class="meta">
          <div><dt>Role</dt><dd>Majority owned</dd></div>
          <div><dt>Sector</dt><dd>ResTech</dd></div>
          <div><dt>Trust layer</dt><dd>MGE licensee</dd></div>
        </dl>
        <p class="fine" style="margin-top:-4px">StarBar is majority owned by Bailiwick Ventures and partners with FohBoh.ai as a licensee of the Metrics Governance Engine, shipping as a module within FohBoh Sentry&trade;.</p>
        <a class="tlink" href="https://starbar.ai" target="_blank" rel="noopener" style="margin-top:auto">starbar.ai <span class="arrow">&#8599;</span></a>
      </article>
      <article class="card" style="border-left:2px solid var(--cobalt)">
        <div class="kicker">Case study 02 &middot; Certified infrastructure</div>
        <h3>FohBoh.ai</h3>
        <p><b>The problem.</b> A restaurant group runs point-of-sale, inventory, labor, payroll and accounting on separate systems, each producing its own version of &ldquo;sales&rdquo; and &ldquo;cost.&rdquo; Nobody can say which number is authoritative &mdash; and AI trained on those numbers inherits the contradiction.</p>
        <p><b>What was architected.</b> The Metrics Governance Engine: a deterministic certification layer that sits between operational systems and every system of record. Data is sealed on arrival, normalized, reconciled across authoritative sources, scored against trust gates, and issued as a certified operational fact rather than a raw number.</p>
        <p><b>What changed.</b> Certification happens <i>before</i> data reaches the system of record, so neither the source system nor the destination can influence the outcome. Sentry and Cortex are the first applications built on that foundation &mdash; proof that the engine works, not the reason it exists.</p>
        <dl class="meta">
          <div><dt>Role</dt><dd>Founded and architected</dd></div>
          <div><dt>Sector</dt><dd>Restaurant infrastructure</dd></div>
          <div><dt>Status</dt><dd>Operating &middot; raising</dd></div>
        </dl>
        <a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener" style="margin-top:auto">fohboh.ai <span class="arrow">&#8599;</span></a>
      </article>

      <article class="card" style="border-left:2px solid var(--signal)">
        <div class="kicker">Case study 03 &middot; Venture architecture</div>
        <h3>BailiwickQuikFix</h3>
        <p><b>The problem.</b> On-demand home and commercial repair is a $600&nbsp;billion market with no dependable promise attached to it. Response times are estimates, dispatch is manual, and margin leaks everywhere between the customer and the tradesperson.</p>
        <p><b>What was architected.</b> Three applications, a licensed governance engine, and a 60-minute service commitment set by drive-time geofence rather than optimism &mdash; combined with voice and AI into an intelligence stack no competitor has assembled. Six weeks from consequential idea to complete investor package.</p>
        <p><b>What changed.</b> No production backend was ever paid for. The venture was architected, modeled, governed and packaged &mdash; fifteen documents from pitch deck to engineering handoff, and three viable exit paths &mdash; before the expensive part began. That sequencing is the whole argument.</p>
        <dl class="meta">
          <div><dt>Role</dt><dd>Originated in the Studio</dd></div>
          <div><dt>Sector</dt><dd>Home &amp; commercial services</dd></div>
          <div><dt>Status</dt><dd>In development</dd></div>
        </dl>
        <a class="tlink" href="vibe.html" style="margin-top:auto">The method behind it <span class="arrow">&rarr;</span></a>
      </article>


    </div>

    <p class="fine" style="margin-top:clamp(24px,2.8vw,34px);max-width:70ch">Figures shown are from each venture's own modeling and materials. Nothing here is an offer to sell or a solicitation of an offer to buy any security &mdash; see the disclosures on the <a class="tlink" href="investing.html">Investing</a> page.</p>
  </div>
</section>
"""




# --- hoisted disclosure blocks (py3.11: no nested same-quote f-strings) ---
_M1 = more("More on engagement economics", """
      <p>Participation may involve professional fees, fixed project fees, retainers, equity, warrants, direct investment, revenue participation, joint-venture structures, or blended fee-and-equity arrangements.</p>
      <p>The structure depends on the stage, scope, risk, intellectual-property contribution, and level of involvement. We are most valuable where capital alone is insufficient and integrated strategic, operational, financial, and technical judgment is required.</p>""")

_M2 = more("More on the AI-native studio model", """
        <p>The Studio integrates venture architecture, market research, customer discovery, product strategy, business-model design, UX and interface development, AI-assisted software creation, financial modeling, commercial positioning, governance, and capital planning — evolving in parallel rather than in sequence.</p>
        <p><b>We don't ask one AI for the answer.</b> Different models research, challenge, write, reason, code, and test. The Studio uses multiple systems because disagreement is useful: models <i>generate</i> research, requirements, prototypes and code; they <i>challenge</i> with counter-theses, technical alternatives, and risk analysis; and human architects <i>govern</i> — determining what evidence and which decisions become authoritative.</p>
        <p>The objective is no longer to produce more work. It is to reach credible evidence faster.</p>""")

_M3 = more("More on what production actually requires", """
        <p>Security, multi-tenancy, identity, permissions, integrations, testing, observability, infrastructure, deployment, customer onboarding, billing, documentation, support, and go-to-market remain serious engineering and business disciplines. Prototype tools have made software remarkably easy to start; none of them make a product dependable.</p>
        <p><b>Rough carpenter, finish carpenter.</b> The Studio proves the structure can stand. Production makes it ready to occupy. The proof of concept establishes the form — the central idea, the essential workflows, the user experience, the technical feasibility, the customer value, the commercial hypothesis. Production requires precision: architecture that scales, security, reliability, performance, testing, monitoring, deployment, documentation, administration, governance, onboarding, and support.</p>""")

_M4 = more("What we accept", """
        <p>BailiwickVibe may work with products developed through Bailiwick Venture Studio; AI-generated prototypes requiring professional engineering; founder-built MVPs; no-code or low-code products that have outgrown their original architecture; legacy applications requiring modernization; enterprise pilots that must become deployable products; software acquired by investors that requires stabilization or reconstruction; and new products preparing for commercial launch.</p>""")

_V1 = more("More on what production actually requires", """
    <p>Security, multi-tenancy, identity, permissions, integrations, testing, observability, infrastructure, deployment, customer onboarding, billing, documentation, support, and go-to-market remain serious engineering and business disciplines. Prototype tools have made software remarkably easy to start; none of them make a product dependable.</p>
    <p><b>Rough carpentry, finish carpentry.</b> Vibe coding gets the frame up fast — AI writes most of the code and it demos well. Finish carpentry is production-grade architecture, proper security, optimized costs, governance structures, financial modeling, and a real launch strategy. That is what investors fund.</p>""")

_V2 = more("What VIBE accepts", """
    <p>AI-generated prototypes built in Cursor, Claude, Replit or similar; founder-built MVPs; no-code and low-code products that have outgrown their original architecture; ventures developed through Bailiwick Venture Studio; legacy applications requiring modernization; enterprise pilots that must become deployable products; and software acquired by investors that requires stabilization or reconstruction.</p>""")

_M5 = more("More on Certified Intelligence", """
          <p>Michael is the creator of the Certified Intelligence framework and the author of <i>The Certified Enterprise</i>, which explores how organizations can establish trust before AI begins making consequential decisions.</p>
          <p>The commercial expression of that work is FohBoh.ai, which applies deterministic governance and certification to operational data in the restaurant industry — certifying metrics before they reach a system of record, a dashboard, or a model.</p>""")


def investing():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Investing</p>
    <h1>We invest where architecture can change value.</h1>
    <p class="lede">Bailiwick Ventures deploys capital into ventures it has helped design. Our operating experience, architecture capabilities, relationships, and strategic involvement are the reason we invest at all — so we invest where they are already at work.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Conditions</p>
      <h2>One prerequisite, then eight tests.</h2>
      <p class="body" style="margin-top:20px">We do not invest simply because a category is fashionable. We look for situations where a thoughtful change in architecture can materially alter enterprise value — and we look for them inside work we have done ourselves.</p>
    </div>
    <div>
      <div class="gate">
        <div class="lbl">The prerequisite</div>
        <p>The venture must be a Bailiwick Venture Studio portfolio company.</p>
        <p class="sub">We invest behind our own architecture. A venture becomes eligible once it has been through the Studio — framed, architected, built, and validated — because that is the only way we can judge what we are underwriting. Everything below is what we then test.</p>
        <div class="exc">
          <div class="lbl">The one exception</div>
          <p>A very small number of highly selective minority positions. Those still come in <b>through</b> the Studio, not alongside it — the same architecture requirement applies, and nothing is held outside it.</p>
        </div>
      </div>
      <ul class="crit">
        <li>A consequential and commercially meaningful problem.</li>
        <li>A fragmented, inefficient, or structurally outdated market.</li>
        <li>A credible technology or operating-model advantage.</li>
        <li>Clear potential for measurable customer value.</li>
        <li>Defensible intellectual property, data, workflows, or domain expertise.</li>
        <li>A realistic path from validation to recurring revenue.</li>
        <li>Strong alignment between architecture, economics, governance, and capital.</li>
        <li>An opportunity for active ownership to create value beyond capital alone.</li>
      </ul>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Where we look</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Sectors of active interest.</h2>
    <div class="grid g3">
      <div class="card"><h3>Enterprise technology &amp; AI</h3><p>Infrastructure, governance, data trust, and applications where reliability and auditability decide adoption.</p></div>
      <div class="card"><h3>Restaurant &amp; hospitality technology</h3><p>Operational systems, platform strategy, and the infrastructure an industry-wide technology transition requires.</p></div>
      <div class="card"><h3>Food &amp; consumer markets</h3><p>Brands and operating businesses where technology-enabled models change the economics of scale.</p></div>
      <div class="card"><h3>Finance</h3><p>Technology-enabled business models, operating systems, and commercialization in financial services.</p></div>
      <div class="card"><h3>Operational infrastructure</h3><p>The unglamorous systems enterprises depend on, where structural inefficiency is measurable and persistent.</p></div>
      <div class="card"><h3>Technology-enabled transformation</h3><p>Established businesses whose value is limited by architecture rather than by demand.</p></div>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">How we participate</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Five ways we work with a venture.</h2>
    <div class="grid g3">
      <div><h4 style="margin-bottom:10px">Founder partnership</h4><p class="body" style="font-size:14.6px">For founders with domain expertise, customer insight, or a consequential idea.</p></div>
      <div><h4 style="margin-bottom:10px">Enterprise venture</h4><p class="body" style="font-size:14.6px">For companies creating a new strategic product, platform, or business line.</p></div>
      <div><h4 style="margin-bottom:10px">Investor-sponsored venture</h4><p class="body" style="font-size:14.6px">For investors or family offices developing an opportunity before a larger capital commitment.</p></div>
      <div><h4 style="margin-bottom:10px">Studio-originated venture</h4><p class="body" style="font-size:14.6px">For opportunities identified and developed internally by Bailiwick Ventures.</p></div>
      <div><h4 style="margin-bottom:10px">Venture reconstruction</h4><p class="body" style="font-size:14.6px">For companies with valuable technology but incomplete positioning, economics, or architecture.</p></div>
    </div>
    <hr class="rule" style="margin:clamp(34px,4vw,52px) 0 24px">
    {_M1}
  </div>
</section>


<section class="bord on-warm" id="investors">
  <div class="shell">
    <p class="eyebrow">For investors</p>
    <h2 style="max-width:22ch">Invest alongside us, one company at a time.</h2>
    <p class="lede" style="margin-top:20px;margin-bottom:clamp(30px,3.6vw,44px)">Investors can participate directly in individual Bailiwick Venture Studio portfolio companies rather than committing to a blind pool. You see the venture, the architecture behind it, and the evidence it has produced before you decide.</p>

    <div class="grid g2">
      <div class="card">
        <div class="kicker">The default</div>
        <span class="fig">SPV<small>Special purpose vehicle</small></span>
        <p style="margin-bottom:0">Every investment is made through a special purpose vehicle formed for that company. One vehicle, one venture, one decision — and the portfolio company's capitalization table stays clean, which protects its ability to raise the next round.</p>
      </div>
      <div class="card">
        <div class="kicker">The threshold</div>
        <span class="fig">$500,000<small>Minimum for a direct position</small></span>
        <p style="margin-bottom:0">A direct position on the company's cap table is available at $500,000 and above. Below that, participation is through the SPV. There are no exceptions to the threshold — it exists to keep the cap table from becoming the venture's first structural problem.</p>
      </div>
    </div>

    <div style="margin-top:clamp(34px,4vw,52px)">
      <p class="eyebrow">How it works</p>
      <h3 style="max-width:30ch;margin-bottom:18px">We do not send materials on request. We have a conversation first.</h3>
      <p class="body" style="margin-bottom:clamp(24px,3vw,34px)">A short call is the only way either side can judge fit — and it means we know who we are dealing with before anything is shared. You learn how the Studio works and what is open; we learn what you invest in and what you are looking for.</p>

      <div class="phases p3">
        <div class="phase">
          <div class="pn">01</div>
          <h4>A conversation</h4>
          <p>Thirty minutes, direct with Michael. How the Studio works, which companies are open, how participation is structured — and what you are looking for.</p>
        </div>
        <div class="phase">
          <div class="pn">02</div>
          <h4>Qualification</h4>
          <p>We confirm eligibility and record who you are: name, email, and mailing address. Nothing is distributed anonymously, in bulk, or to a list.</p>
        </div>
        <div class="phase">
          <div class="pn">03</div>
          <h4>Materials</h4>
          <p>Company materials and offering documents relevant to the specific opportunity are then sent to you directly.</p>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-top:clamp(26px,3vw,36px)">
        <p class="body" style="margin:0;max-width:46ch">Start with the call. There is no charge and no obligation on either side.</p>
        <a class="btn btn-p" href="https://calendly.com/michael-atkinson" target="_blank" rel="noopener">Contact Us for More Information <span class="arrow">↗</span></a>
      </div>
    </div>

    <div class="legal">
      <h4>Important disclosures</h4>
      <p>Nothing on this page constitutes an offer to sell, or the solicitation of an offer to buy, any security, nor shall there be any sale of securities in any jurisdiction in which such an offer, solicitation, or sale would be unlawful. Any offer or solicitation will be made only by means of definitive offering documents — including a private placement memorandum, operating agreement, and subscription agreement — furnished to qualified prospective investors, and those documents will supersede the information presented here in its entirety.</p>
      <p>Interests in any Bailiwick Venture Studio portfolio company, and in any special purpose vehicle formed to hold such interests, have not been and will not be registered under the U.S. Securities Act of 1933, as amended, or under the securities laws of any state or other jurisdiction. They are offered and sold in reliance on exemptions from registration, including Regulation&nbsp;D, and may be offered only to persons who qualify as accredited investors as defined in Rule&nbsp;501(a). Such interests are restricted securities, are subject to substantial transfer restrictions, and no public market for them exists or is expected to develop.</p>
      <p>Neither the U.S. Securities and Exchange Commission nor any state securities regulator has approved or disapproved of these securities, passed upon the merits of any offering, or determined that the information on this page is accurate or complete. Any representation to the contrary is a criminal offense.</p>
      <p>An investment in an early-stage private company involves a high degree of risk, including the risk of losing the entire amount invested. Such investments are illiquid, are suitable only for investors who are able to bear that risk, and should represent only a portion of a diversified portfolio. Past performance is not indicative of, and provides no guarantee of, future results.</p>
      <p>Statements on this page concerning plans, expectations, projections, or future performance are forward-looking and involve known and unknown risks and uncertainties. Actual results may differ materially from those expressed or implied. Bailiwick Ventures undertakes no obligation to update any forward-looking statement.</p>
      <p>Nothing on this page is investment, legal, accounting, or tax advice. Prospective investors should consult their own advisers before making any investment decision. Bailiwick Ventures, Inc. is not a registered broker-dealer or investment adviser, and participation in any opportunity is at its sole discretion.</p>
    </div>
  </div>
</section>

<section class="bord tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Bring the idea to the Studio first.</h2>
    <p class="body" style="margin:18px auto 0;max-width:52ch">Investment follows architecture, not the other way round.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="studio.html">Visit Bailiwick Venture Studio <span class="arrow">→</span></a>
      <a class="btn btn-s" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


def portfolio():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Portfolio &amp; holdings</p>
    <h1>A connected portfolio of ideas, capabilities, and operating companies.</h1>
    <p class="lede">Bailiwick Ventures owns and supports a portfolio of operating companies, internally developed ventures, intellectual property, and a small number of highly selective minority positions.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <p class="eyebrow" id="fohboh">Operating companies</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Businesses Bailiwick Ventures owns, controls, or co-founded.</h2>
    <div class="grid g3">
      <div class="card" style="grid-column:span 2;border-left:2px solid var(--bronze)">
        <div class="kicker">Studio-born portfolio asset</div>
        <h3 style="font-size:clamp(22px,2.4vw,28px)">FohBoh.ai</h3>
        <p style="max-width:56ch">Certified intelligence infrastructure for enterprise operational data and AI. FohBoh.ai is the first major commercial implementation of Michael Atkinson's work on certified intelligence, deterministic governance, and enterprise trust infrastructure — built for the restaurant industry.</p>
        <p style="margin-bottom:18px"><a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener">fohboh.ai <span class="arrow">↗</span></a></p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Operating / Commercial</dd></div>
          <div><dt>Sector</dt><dd>Enterprise AI / ResTech</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Venture Studio</dd></div>
          <div><dt>Relationship</dt><dd>Operating company / strategic holding</dd></div>
        </dl>
      </div>
      <div class="card" id="kokomo" style="border-left:2px solid var(--bronze)">
        <div class="kicker">Operating company</div>
        <h3>Club Kokomo Spirits</h3>
        <p>Crafted and produced in San Diego, California and founded by Mike Love, co-founder of The Beach Boys, Club Kokomo Spirits focuses on providing consumers with a top-shelf sensory visit to the islands of the Caribbean. Bailiwick Ventures is a co-founder and shareholder.</p>
        <p style="margin-bottom:18px"><a class="tlink" href="https://clubkokomospirits.com" target="_blank" rel="noopener">clubkokomospirits.com <span class="arrow">↗</span></a></p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Operating</dd></div>
          <div><dt>Sector</dt><dd>Spirits / CPG</dd></div>
          <div><dt>Relationship</dt><dd>Co-founder &amp; shareholder</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow" id="ventures">Studio ventures</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Originated or developed through Bailiwick Venture Studio.</h2>
    <div class="grid g3">
      <div class="card" style="border-left:2px solid var(--cobalt)">
        <div class="kicker">Studio venture · In development</div>
        <h3><a href="https://bailiwickquikfix.ai" target="_blank" rel="noopener" style="text-decoration:none;border-bottom:1px solid var(--cobalt)">BailiwickQuikFix.ai <span style="font-size:12px;opacity:.6">↗</span></a></h3>
        <p>On-demand home and commercial repair, built on voice, AI, and a licensed governance engine, with a 60-minute service SLA set by drive-time geofence. Architected end to end in six weeks as the canonical demonstration of the VIBE methodology. <a class="tlink" href="vibe.html">See the case study</a></p>
        <dl class="meta">
          <div><dt>Status</dt><dd>In development</dd></div>
          <div><dt>Sector</dt><dd>Home &amp; commercial services</dd></div>
          <div><dt>Origin</dt><dd>BailiwickVibe</dd></div>
        </dl>
      </div>
      <div class="card" style="border-left:2px solid var(--signal)">
        <div class="kicker">Division property</div>
        <h3>BailiwickVibe.com</h3>
        <p>Venture-In-a-Box Engineering — the production engineering and market-entry division. Live, with the 8-Phase Venture Architecture, the QuikFix case study, and the Vibe Score calculator. <a class="tlink" href="https://bailiwickvibe.com" target="_blank" rel="noopener">Visit ↗</a></p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Live</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Ventures</dd></div>
        </dl>
      </div>
      <div class="card" style="border-left:2px solid var(--bronze)">
        <div class="kicker">Operating company</div>
        <h3><a href="https://starbar.ai" target="_blank" rel="noopener" style="text-decoration:none;border-bottom:1px solid var(--bronze)">StarBar.ai <span style="font-size:12px;opacity:.6">↗</span></a></h3>
        <p>Certified inventory intelligence for restaurants and bars. SnapCount&trade; replaces the clipboard with per-shift voice counting, then certifies the result against six deterministic conditions and anchors it to an immutable ledger. Licensee of FohBoh&rsquo;s Metrics Governance Engine; ships as a module within FohBoh Sentry&trade;.</p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Operating</dd></div>
          <div><dt>Sector</dt><dd>ResTech</dd></div>
          <div><dt>Role</dt><dd>Majority owned</dd></div>
        </dl>
      </div>
      <div class="card" style="border-left:2px solid var(--bronze)">
        <div class="kicker">Operating company</div>
        <h3><a href="https://www.kimellafarms.com" target="_blank" rel="noopener" style="text-decoration:none;border-bottom:1px solid var(--bronze)">Kimella Farms <span style="font-size:12px;opacity:.6">↗</span></a></h3>
        <p>Honest, farm-to-face&trade; skincare and custom blends, handcrafted on the Big Island of Hawaii. At least 95% natural, built on a principle of truth in ingredients.</p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Operating</dd></div>
          <div><dt>Sector</dt><dd>Skincare / CPG</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Ventures</dd></div>
        </dl>
      </div>
      <div class="card" style="border-left:2px solid var(--cobalt)">
        <div class="kicker">Division property</div>
        <h3><a href="https://www.bailiwickventures.com/studio.html" style="text-decoration:none;border-bottom:1px solid var(--cobalt)">Bailiwick Venture Studio</a></h3>
        <p>The venture architecture and development division. Enterprise Venture Architecture applied from consequential idea to usable proof of concept &mdash; six phases, a defined handoff to BailiwickVibe, and Plan&nbsp;A Blueprint as the way in.</p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Live</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Ventures</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow" id="ip">Intellectual property</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Frameworks, methods, and systems owned through Bailiwick.</h2>
    <div class="grid g3">
      <div class="card"><h3>Enterprise Venture Architecture</h3><p>The structural design process applied by Bailiwick Venture Studio to move a venture from diagnosis through capital calibration and execution.</p></div>
      <div class="card"><h3>Certified Intelligence</h3><p>The framework behind <i>The Certified Enterprise</i> — the argument that AI should never be trusted more than the evidence on which it depends.</p></div>
      <div class="card"><h3>The Certified Enterprise</h3><p>The book. <i>Taming Data Anarchy in the AI Era</i> — self-published on Amazon, expected November 2026. <a class="tlink" href="book.html">Read more</a></p></div>
      <div class="card"><h3>Roadmap to Certified</h3><p>The phased certification framework that moves an organization from tribal knowledge to governed logic.</p></div>
      <div class="card"><h3>Published work</h3><p>Essays, frameworks, research, and applied methods developed and held through Bailiwick Ventures. <a class="tlink" href="blog.html">See the writing</a></p></div>
    </div>
  </div>
</section>

{CASES}

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">Categories</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(26px,3vw,40px)">How the portfolio is organized.</h2>
    <div class="grid g4">
      <div><h4 style="margin-bottom:10px">Operating companies</h4><p class="body" style="font-size:14.4px">Businesses Bailiwick Ventures owns, controls, or co-founded and holds shares in.</p></div>
      <div><h4 style="margin-bottom:10px">Studio ventures</h4><p class="body" style="font-size:14.4px">Companies originated or developed through Bailiwick Venture Studio.</p></div>
      <div><h4 style="margin-bottom:10px">Strategic investments</h4><p class="body" style="font-size:14.4px">A very small number of highly selective minority positions — taken through Bailiwick Venture Studio, never alongside it, and held to the same architecture requirement.</p></div>
      <div><h4 style="margin-bottom:10px">Intellectual property</h4><p class="body" style="font-size:14.4px">Frameworks, methods, systems, software, and other proprietary assets owned or managed by Bailiwick.</p></div>
    </div>
  </div>
</section>

<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Owners, founders, and investors: we are open to the right situation.</h2>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
      <a class="btn btn-s" href="investing.html">How We Invest <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


def studio():
    return f"""
<div class="hero" style="background:linear-gradient(180deg,#FFFDF9 0%,#FFFDF9 60%,#F6F3EE 100%)">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow" style="color:var(--cobalt)">Bailiwick Venture Studio · Operating division</p>
    <h1>From consequential idea to usable proof of concept. In 60 days or less.<span style="color:var(--cobalt)">*</span></h1>
    <p class="lede">Bailiwick Venture Studio applies Enterprise Venture Architecture to transform consequential ideas into coherent ventures — integrating strategy, product, technology, economics, governance, commercialization, and capital planning from the beginning.</p>
    <div class="btns">
      <a class="btn btn-p" href="contact.html" style="background:var(--cobalt);border-color:var(--cobalt)">Bring Us an Idea <span class="arrow">→</span></a>
      <a class="btn btn-s" href="#process">Explore the Process <span class="arrow">→</span></a>
      <a class="btn btn-g" href="https://bailiwickventurestudio.com" target="_blank" rel="noopener">Visit the Studio Site <span class="arrow">&#8599;</span></a>
    </div>
    <p class="fine" style="margin-top:22px;max-width:62ch"><span style="color:var(--cobalt)">*</span> The 60-day objective applies to appropriately scoped engagements with available decision-makers, defined access to necessary subject-matter expertise, and timely validation.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">The shift</p>
      <h2>Speed is not the thesis. Coherence is.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:24px">Traditional venture development was slow, sequential, and expensive — research, then strategy, then design, then engineering, then modeling, then market testing, each with handoffs that introduced delay and rework.</p>
      <p class="body">Artificial intelligence has changed the economics and velocity of venture creation. The Studio uses AI to accelerate the work, while experienced human judgment determines what should be built, why it should exist, and what evidence is required before the venture advances.</p>
      {_M2}
    </div>
  </div>
</section>

<section class="bord" id="process">
  <div class="shell">
    <p class="eyebrow">The Bailiwick process</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(28px,3.5vw,44px)">Six phases, run in parallel, not in sequence.</h2>
    <div class="phases">
      <div class="phase"><div class="pn">01</div><h4>Diagnose</h4><p>Is the problem consequential? Market forces, constraints, and structural inefficiency.</p></div>
      <div class="phase"><div class="pn">02</div><h4>Map</h4><p>Where are the risks and asymmetries? Leverage points and structural advantage.</p></div>
      <div class="phase"><div class="pn">03</div><h4>Architect</h4><p>What complete venture should exist? Product, capital structure, and operating model.</p></div>
      <div class="phase"><div class="pn">04</div><h4>Build</h4><p>Can we create a usable proof? Experience, workflows, data model, demonstrable product.</p></div>
      <div class="phase"><div class="pn">05</div><h4>Validate</h4><p>Will customers care enough to act? Technical, product, and commercial evidence.</p></div>
      <div class="phase"><div class="pn">06</div><h4>Prepare</h4><p>Should capital be committed? Production scope, GTM, capital plan, investor narrative.</p></div>
    </div>
    <p class="fine" style="margin-top:18px">Architecture is iterative: stress-testing in phases 04–06 routinely loops back to phase 03.</p>

    <div class="gate" style="margin-top:clamp(32px,4vw,48px);margin-bottom:0">
      <div class="lbl">Where the Studio stops</div>
      <p>The Studio's work ends at the proof.</p>
      <p class="sub">These six phases are pre-proof work: deciding what should exist, designing it as a whole system, and producing enough evidence to justify building it for real. The Studio delivers the venture architecture, a usable proof, the capital plan and investor narrative required to reach the next milestone, and a production blueprint.</p>
      <div class="exc">
        <div class="lbl">What happens next</div>
        <p>Everything after the proof — refactoring for production, governance and IP structure, economic simulation at scale, cap table and control calibration, launch, and investor and acquisition readiness — is <b>BailiwickVibe's 8-Phase Venture Architecture</b>. Same discipline, later stage, and a defined handoff rather than a hazy one. <a class="tlink" href="vibe.html" style="margin-left:4px">See the eight phases <span class="arrow">→</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">What leaves the Studio</p>
    <h2 style="max-width:20ch;margin-bottom:clamp(26px,3vw,42px)">Not just an MVP.</h2>
    <div class="grid g4">
      <div><h4 style="margin-bottom:10px">Venture architecture</h4><p class="body" style="font-size:14.4px">Thesis, market, category, economics, governance, and operating model.</p></div>
      <div><h4 style="margin-bottom:10px">Usable proof</h4><p class="body" style="font-size:14.4px">A product capable of testing the most consequential assumptions.</p></div>
      <div><h4 style="margin-bottom:10px">Capital architecture</h4><p class="body" style="font-size:14.4px">Economics, funding needs, milestones, and investor narrative.</p></div>
      <div><h4 style="margin-bottom:10px">Production blueprint</h4><p class="body" style="font-size:14.4px">The engineering and go-to-market specification for what comes next.</p></div>
    </div>
    <hr class="rule" style="margin:clamp(34px,4vw,52px) 0 26px">
    <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap">
      <p class="body" style="margin:0;max-width:52ch">Ready for production? BailiwickVibe takes over here — production engineering, enterprise readiness, and market entry.</p>
      <a class="btn btn-g" href="vibe.html">Visit BailiwickVibe <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:20ch;margin:0 auto">Have an idea that deserves to be architected?</h2>
    <p class="body" style="margin:18px auto 0;max-width:52ch">Studio work is sold as <b>Plan A — Blueprint</b>: four weeks, fixed price, published. It begins with the Triage.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="plans.html#blueprint" style="background:var(--cobalt);border-color:var(--cobalt)">See Plan A — Blueprint <span class="arrow">→</span></a>
      <a class="btn btn-s" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
    </div>
    <p class="fine" style="margin-top:20px">The Studio publishes its full model, its six phases, its ventures and its
      engagement terms at <a class="tlink" href="https://bailiwickventurestudio.com" target="_blank" rel="noopener">bailiwickventurestudio.com&nbsp;&#8599;</a></p>
  </div>
</section>
"""


def vibe():
    return f"""
<div class="hero" style="background:linear-gradient(180deg,#FFFDF9 0%,#FFFDF9 60%,#F7F2EE 100%)">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow" style="color:var(--signal)">BailiwickVibe · Venture-In-a-Box Engineering</p>
    <h1 style="max-width:15ch">Your AI prototype deserves finish carpentry.</h1>
    <p class="lede">BailiwickVibe takes AI-generated prototypes and vibe-coded experiments and turns them into production-safe, scalable, investable ventures.</p>
    <div class="btns">
      <a class="btn btn-p" href="plans.html" style="background:var(--signal);border-color:var(--signal)">Plans &amp; Pricing <span class="arrow">→</span></a>
      <a class="btn btn-s" href="#method">The 8-Phase Method <span class="arrow">→</span></a>
    </div>
    <div class="tagline" style="color:var(--signal)"><span>From vibe code</span><i style="background:var(--signal)"></i><span>to venture ready</span></div>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">The problem</p>
      <h2>The vibe coding gap.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:26px">AI tools let anyone build a prototype in hours. But there is a canyon between "it works on my machine" and "it is ready for real users and real money."</p>
      <div class="grid g2" style="margin-bottom:8px">
        <div class="card" style="border-left:2px solid var(--line)">
          <h3 style="font-size:19px">Rough carpentry</h3>
          <p style="margin-bottom:0">Vibe coding gets the frame up fast. AI writes 80% of the code. It demos well. But auth is hacked together, data leaks, costs spiral, and it breaks at user&nbsp;#10.</p>
        </div>
        <div class="card" style="border-left:2px solid var(--signal)">
          <h3 style="font-size:19px">Finish carpentry</h3>
          <p style="margin-bottom:0">Production-grade architecture, proper security, optimized costs, governance structures, financial modeling, and a real launch strategy. This is what investors fund.</p>
        </div>
      </div>
      {_V1}
    </div>
  </div>
</section>

<section class="bord" id="method">
  <div class="shell">
    <p class="eyebrow">The method</p>
    <h2 style="max-width:24ch">The 8-Phase Venture Architecture.</h2>
    <p class="body" style="margin-top:18px;margin-bottom:clamp(26px,3vw,36px)">A systematic process that transforms vibe-coded prototypes into production-ready, investable ventures. It does not stop at working software — it ends at a venture someone would fund or buy.</p>

    <div class="gate" style="margin-bottom:clamp(28px,3.5vw,44px);border-color:var(--signal)">
      <div class="lbl" style="color:var(--signal)">Where Vibe starts</div>
      <p>Vibe begins at the prototype, not at the idea.</p>
      <p class="sub">Something has to work first. That prototype may have come out of <a class="tlink" href="studio.html">Bailiwick Venture Studio</a>, or a founder may have built it in Cursor over a weekend — either way, the Studio's job is deciding what should exist and proving it can, and ours starts once it does.</p>
      <div class="exc">
        <div class="lbl">The division of labor</div>
        <p>The Studio runs six pre-proof phases and hands over a venture architecture, a usable proof, and a production blueprint. The eight phases below are post-prototype work. Where the Studio produces a capital plan to reach the next milestone, phase 06 here calibrates cap table, dilution and control through seed. Where the Studio proves the idea, phases 01–04 make it dependable and phases 05–08 make it fundable.</p>
      </div>
    </div>
    <div class="phases p4">
      <div class="phase"><div class="pn">01</div><h4>Structural Diagnostic</h4><p>Audit the prototype through five lenses — architecture, security, data integrity, scalability, deployment readiness — and produce a scored Venture Readiness assessment with prioritized findings.</p></div>
      <div class="phase"><div class="pn">02</div><h4>Risk &amp; Asymmetry Mapping</h4><p>Identify leverage points, single points of failure, and asymmetric opportunities — places where small investments yield outsized returns.</p></div>
      <div class="phase"><div class="pn">03</div><h4>Integrated Venture Design</h4><p>Architect for production. Refactor the codebase. Deliver a migration plan and an engineering handoff any team can continue from.</p></div>
      <div class="phase"><div class="pn">04</div><h4>Governance &amp; IP Architecture</h4><p>Deterministic governance, audit-defensible records, and the IP structure that turns a working product into licensable, transferable, defensible technology.</p></div>
      <div class="phase"><div class="pn">05</div><h4>Economic Simulation</h4><p>Model hosting, inference, and margins at 1×, 10× and 100× scale. ARPU, CAC, LTV and breakeven across three scenarios over 24 months.</p></div>
      <div class="phase"><div class="pn">06</div><h4>Capital &amp; Control Calibration</h4><p>Cap table scenarios from bootstrap through seed. Shareholder governance, minority protections, and decision rights calibrated to the founder's intent.</p></div>
      <div class="phase"><div class="pn">07</div><h4>Go-to-Market &amp; Launch</h4><p>Launch playbook, CI/CD, monitoring, GTM sequence, and a 90-day plan with KPIs and growth scenarios.</p></div>
      <div class="phase"><div class="pn">08</div><h4>Investor &amp; Acquisition Readiness</h4><p>Pitch decks, buyer briefings, data room, demo materials, and exit-path planning — for ventures whose endpoint is a raise, a partnership, or a sale.</p></div>
    </div>
    <p class="fine" style="margin-top:18px">Phases 01 through 06 are the structural work; 07 and 08 are what turn a working product into something fundable.</p>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">VIBE in action</p>
    <div class="split" style="margin-bottom:clamp(28px,3.4vw,40px)">
      <div>
        <h2 style="max-width:16ch">BailiwickQuikFix — built in six weeks.</h2>
      </div>
      <div>
        <p class="body" style="margin-bottom:14px">Three apps, a licensed AI governance engine, and a complete investor package. The canonical example of the VIBE methodology, applied to the $600&nbsp;billion home repair market.</p>
        <p class="body" style="margin-bottom:0"><b>No production backend. That is the point.</b> The venture was architected, modeled, governed and packaged before a line of production infrastructure was paid for.</p>
      </div>
    </div>
    <div class="stats">
      <div><div class="v">Voice + AI + MGE</div><div class="l">Three intelligence layers no competitor has combined.</div></div>
      <div><div class="v">60-minute SLA</div><div class="l">Drive-time geofence — engineered, not guessed.</div></div>
      <div><div class="v">7 verticals</div><div class="l">Restaurants, hotels, property management, apartments and more.</div></div>
      <div><div class="v">86% gross margin</div><div class="l">$19 platform profit on an average $80 job.</div></div>
      <div><div class="v">15 documents</div><div class="l">From pitch deck to engineering handoff — the complete package.</div></div>
      <div><div class="v">3 exit paths</div><div class="l">Sell the IP, raise seed, or partner with an operator.</div></div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-top:clamp(26px,3vw,38px)">
      <p class="body" style="margin:0;max-width:48ch">The full case study, the method in detail, and the Vibe Score calculator live on the BailiwickVibe site.</p>
      <a class="btn btn-g" href="https://bailiwickvibe.com" target="_blank" rel="noopener">See the Case Study <span class="arrow">↗</span></a>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell split">
    <div>
      <p class="eyebrow">What makes it different</p>
      <h2>We begin with the venture, not the specification.</h2>
    </div>
    <div>
      <p class="body" style="margin-bottom:22px">Traditional development firms begin with a specification. BailiwickVibe begins by understanding what customer problem the product solves, how the company creates and captures value, which assumptions have been validated, what evidence customers require, and what milestones investors expect.</p>
      <p class="body">This ensures engineering serves the commercial architecture rather than becoming detached from it — and it is why the method ends at investor and acquisition readiness rather than at deployment.</p>
      {_V2}
    </div>
  </div>
</section>

<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:22ch;margin:0 auto">Have a prototype that has to become dependable?</h2>
    <p class="body" style="margin:18px auto 0;max-width:50ch">Every engagement starts with the Triage — ninety minutes and a written assessment of what you actually have, credited in full against any plan.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="plans.html#triage" style="background:var(--signal);border-color:var(--signal)">Start With the Triage <span class="arrow">→</span></a>
      <a class="btn btn-s" href="plans.html">See All Three Plans <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


def insights():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Insights</p>
    <h1>Ideas we are working through in public.</h1>
    <p class="lede">Writing on enterprise venture architecture, AI governance, operational intelligence, and the systems that decide whether a company can be trusted with its own data.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <p class="eyebrow">Featured thesis</p>
    <div class="split" style="margin-top:8px">
      <div>
        <h2 style="max-width:18ch">AI should never be trusted more than the evidence on which it depends.</h2>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">Michael's work in enterprise AI begins with a distinction most organizations overlook: <b>data records; evidence proves.</b></p>
        <p class="body">As artificial intelligence assumes a greater role in operational and strategic decisions, enterprises will need more than abundant data and increasingly capable models. They will need provenance, reconciliation, governance, deterministic controls, reproducibility, chain of custody, accountability — evidence.</p>
        {_M5}
      </div>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Themes</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(26px,3vw,42px)">The recurring arguments.</h2>
    <div class="grid g3">
      <div class="card"><div class="kicker">Trust</div><h3>Data vs. Evidence</h3><p>Why an abundance of data has not produced an abundance of certainty, and what closes the gap.</p></div>
      <div class="card"><div class="kicker">Governance</div><h3>Governance Before Intelligence</h3><p>Why controls designed after deployment are the most expensive controls an enterprise ever builds.</p></div>
      <div class="card"><div class="kicker">Architecture</div><h3>Architecture Before Acceleration</h3><p>AI can accelerate execution. It cannot compensate for an incoherent thesis or weak economics.</p></div>
      <div class="card"><div class="kicker">Independence</div><h3>Why Systems of Record Cannot Certify Truth</h3><p>The entity that generates a metric cannot also be the authority that certifies it.</p></div>
      <div class="card"><div class="kicker">Venture design</div><h3>Designing Ventures in the Age of AI</h3><p>What changes when research, design, and build compress — and what stubbornly does not.</p></div>
      <div class="card"><div class="kicker">Industry</div><h3>Operational Intelligence</h3><p>What operators actually need from technology, from someone who has run the operation.</p></div>
    </div>
  </div>
</section>

<section class="on-ink" id="speaking">
  <div class="shell">
    <div class="split">
      <div>
        <p class="eyebrow">Public speaking</p>
        <h2>Helping leaders design enterprises worth trusting.</h2>
        <div class="btns" style="margin-top:26px">
          <a class="btn btn-g" href="contact.html#media">Inquire about Speaking <span class="arrow">&rarr;</span></a>
        </div>
      </div>
      <div>
        <p class="lede" style="margin-bottom:22px">Michael speaks about transformative technologies affecting the global restaurant industry &mdash; restaurant automation, voice technology, and the changing nature of customer engagement through integrated data, prescriptive and embedded analytics, and modern data management systems.</p>
        <p class="body">Most recently, alongside the release of <a href="book.html" style="color:var(--warm)"><i>The Certified Enterprise</i></a>, he speaks on enterprise data integrity &mdash; and on the danger of believing that a probabilistic system like an LLM will deliver the trusted insight required to make consequential business decisions.</p>
      </div>
    </div>

    <div class="recog">
      <div class="rq">
        <div class="lbl">Recognition</div>
        <p>Named one of the restaurant industry&rsquo;s most influential restaurant technology experts by <i>Nation&rsquo;s Restaurant News</i>.</p>
        <a class="tlink" href="https://www.nrn.com/people/most-influential-suppliers-and-vendors-country-according-nation-s-restaurant-news-readers" target="_blank" rel="noopener">Read the list <span class="arrow">&#8599;</span></a>
      </div>
      <div>
        <div class="lbl">Signature talks</div>
        <ul class="ticks" style="margin-top:14px">
          <li>AI Needs Evidence, Not More Data</li>
          <li>The Certified Enterprise</li>
          <li>Governance Before Intelligence</li>
          <li>Architecture Before Acceleration</li>
          <li>Designing Ventures in the Age of AI</li>
          <li>Why Systems of Record Cannot Certify Truth</li>
          <li>Trust as Enterprise Infrastructure</li>
        </ul>
      </div>
    </div>

    <hr class="rule" style="margin:clamp(30px,3.6vw,44px) 0 22px">
    <p class="body" style="margin:0;max-width:74ch">For business opportunities, speaking, or venture architecture, contact Michael <a href="contact.html" style="color:var(--warm)">through this website</a> or at <a href="mailto:michael@bailiwickventures.com" style="color:var(--warm)">michael@bailiwickventures.com</a>.</p>
  </div>
</section>

<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Longer-form writing, the Canon, and the journal live on MichaelAtkinson.me.</h2>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-s" href="https://michaelatkinson.me" target="_blank" rel="noopener">Visit MichaelAtkinson.me <span class="arrow">↗</span></a>
    </div>
  </div>
</section>
"""


def contact():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Contact</p>
    <h1>Start a conversation.</h1>
    <p class="lede">Tell us the situation. If Bailiwick is the right partner we will say so quickly — and if we are not, we will usually be able to point you somewhere better.</p>
    <div class="btns">
      <a class="btn btn-p" href="#form">Send a Written Inquiry <span class="arrow">→</span></a>
      <a class="btn btn-s" href="plans.html">Plans &amp; Pricing <span class="arrow">→</span></a>
    </div>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Before you write</p>
      <h2 style="font-size:clamp(21px,2.2vw,26px)">A few notes.</h2>
      <p class="small" style="margin-top:18px">Every inquiry is read by Michael. The more precisely you can describe the situation, the more useful the first conversation will be.</p>
      <p class="small">Writing to us costs nothing and commits you to nothing. Engaging us is priced, published, and starts the same way for everyone.</p>
      <hr class="rule" style="margin:26px 0">
      <p class="eyebrow" style="margin-bottom:10px">Building something?</p>
      <p class="small">Advisory, Studio and BailiwickVibe are professional services and are not sold through a free consultation. The three plans are pre-priced and published, and every one of them begins with the paid Triage.</p>
      <a class="tlink" href="plans.html">See plans &amp; pricing <span class="arrow">→</span></a>
      <hr class="rule" style="margin:26px 0">
      <p class="eyebrow" style="margin-bottom:10px">Investors and partners</p>
      <p class="small">Investment, partnership, co-investment and portfolio conversations are not a service sale — those go straight onto Michael's calendar, no form and no fee.</p>
      <a class="tlink" href="https://calendly.com/michael-atkinson" target="_blank" rel="noopener">calendly.com/michael-atkinson <span class="arrow">↗</span></a>
      <hr class="rule" style="margin:26px 0">
      <p class="eyebrow" id="media" style="margin-bottom:10px">Speaking &amp; media</p>
      <p class="small">For conference, podcast, board briefing, and media inquiries, select <b>Speaking / Media</b> as the nature of your inquiry.</p>
      <hr class="rule" style="margin:26px 0">
      <p class="eyebrow" style="margin-bottom:10px">By email</p>
      <p class="small" style="margin-bottom:6px"><a class="tlink" href="mailto:info@bailiwickventures.com">info@bailiwickventures.com</a></p>
    </div>

    <div>
      <form class="inquiry" id="form" method="POST" action="https://formsubmit.co/michael@bailiwickventures.com" enctype="multipart/form-data">
        <input type="hidden" name="_subject" value="Bailiwick Ventures — new inquiry">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="true">
        <input type="hidden" name="_next" value="https://bailiwickventures.com/thanks.html">
        <input type="text" name="_honey" style="display:none">
        <div class="f2">
          <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization"></div>
          <div class="field"><label for="title">Title</label><input id="title" name="title" type="text" autocomplete="organization-title"></div>
        </div>

        <div class="field"><label for="website">Website</label><input id="website" name="website" type="url" placeholder="https://"></div>

        <div class="field">
          <label for="nature">Nature of inquiry</label>
          <select id="nature" name="nature">
            <option value="">Select one</option>
            <option>Strategic Advisory</option>
            <option>Investment / Partnership</option>
            <option>Plans &amp; Pricing — book the Triage</option>
            <option>Bailiwick Venture Studio</option>
            <option>BailiwickVibe</option>
            <option>Portfolio / Corporate Development</option>
            <option>Speaking / Media</option>
            <option>Other</option>
          </select>
        </div>

        <div class="field">
          <label for="stage">Approximate company stage</label>
          <select id="stage" name="stage">
            <option value="">Select one</option>
            <option>Concept / new venture</option>
            <option>Early revenue</option>
            <option>Growth company</option>
            <option>Established enterprise</option>
            <option>PE-backed</option>
            <option>Investor / fund</option>
          </select>
        </div>

        <div class="field">
          <label for="situation">Briefly describe the situation or opportunity</label>
          <textarea id="situation" name="situation"></textarea>
        </div>

        <div class="field">
          <label for="useful">What would make this conversation useful?</label>
          <textarea id="useful" name="useful" style="min-height:96px"></textarea>
        </div>

        <div class="field">
          <label for="doc">Supporting document or deck <span style="color:#9AA5AF;font-weight:400;text-transform:none;letter-spacing:0">— optional</span></label>
          <input id="doc" name="doc" type="file">
        </div>

        <button class="btn btn-p" type="submit" style="font-family:var(--sans);cursor:pointer">Send Inquiry <span class="arrow">→</span></button>
        <p class="fine" style="margin-top:16px">Submissions are delivered to michael@bailiwickventures.com. The first submission after launch triggers a one-time confirmation email from the form handler — click the link in it once and the form is live.</p>
      </form>
    </div>
  </div>
</section>
"""
