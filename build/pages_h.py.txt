"""Company & Investor Overview (overview.html) — Oct 2026.

Public overview and portfolio reference. The PDFs live in
/downloads/ and are the only public downloads; the v7 ZIP is an
implementation package and is never linked.
"""

OV_PDF = "/downloads/bailiwick-ventures-overview.pdf"

_DOC = """<svg width="26" height="32" viewBox="0 0 26 32" fill="none" aria-hidden="true">
  <path d="M2 2h15l7 7v21H2z" stroke="#12304F" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M17 2v7h7" stroke="#12304F" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M7 16h12M7 21h12M7 26h8" stroke="#A8763E" stroke-width="1.5" stroke-linecap="round"/>
</svg>"""


def overview():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Company &amp; Investor Overview</p>
    <h1 style="max-width:20ch">The venture model, and the opportunity in front of it.</h1>
    <p class="lede">An overview of the venture model and a look at FohBoh.ai, a Bailiwick portfolio company.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <div class="grid g2">
      <article class="card dl-card">
        {_DOC}
        <div class="kicker">PDF &middot; 2 pages</div>
        <h2 class="dl-h">Bailiwick Ventures Overview</h2>
        <p>How Bailiwick funds, architects, and develops ventures in six stages: BV pre-seed, the Studio, Vibe builds, MVP ready, the Seed round, and GTM. It explains where outside investors participate, and that participation is in the selected venture rather than in Bailiwick Ventures or its divisions.</p>
        <a class="btn btn-p" href="{OV_PDF}" target="_blank" rel="noopener" style="margin-top:auto">Download the overview (PDF)</a>
      </article>
      <article class="card dl-card">
        {_DOC}
        <div class="kicker">Portfolio company</div>
        <h2 class="dl-h">FohBoh.ai</h2>
        <p>Certified intelligence infrastructure, with restaurant operations as its first configured sector. MGE is in production. Sentry is production-ready.</p>
        <a class="btn btn-p" href="portfolio.html#fohboh">View FohBoh.ai in the portfolio <span class="arrow" aria-hidden="true">→</span></a>
      </article>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell split">
    <div>
      <p class="eyebrow">Bailiwick Ventures</p>
      <h2>Start with a conversation.</h2>
    </div>
    <div>
      <p class="lede">Learn how Bailiwick builds ventures, works with operators, and develops strategic relationships.</p>
      <div class="btns" style="margin-top:26px"><a class="btn btn-p" href="contact.html">Contact Bailiwick</a></div>
      <p class="fine" style="margin-top:28px;max-width:62ch">Nothing on this page is an offer to sell or a solicitation of an offer to buy any security; see the disclosures on the <a class="tlink" href="investing.html#investors" style="font-size:12.5px">Investing</a> page.</p>
    </div>
  </div>
</section>
"""
