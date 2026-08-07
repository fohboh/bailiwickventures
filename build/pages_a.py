"""Home, About, Advisory."""
from theme import mark

def more(label, inner):
    return (f'<details class="more"><summary>'
            f'<span class="pm"><span>+</span></span>'
            f'<span class="lbl-o">{label}</span><span class="lbl-c">Close</span></summary>'
            f'<div class="inner">{inner}</div></details>')




# --- hoisted disclosure blocks (py3.11: no nested same-quote f-strings) ---
_M1 = more("More on the holding-company model", """
        <p>The company provides the institutional foundation through which new ventures are originated, existing businesses are supported, intellectual property is developed, and capital is allocated. It holds investments and ownership interests, participates in transactions and capital formation, and sponsors its operating divisions.</p>
        <p>Our work is guided by a simple principle: <b>the strongest companies are designed as coherent systems before they are scaled.</b> That means aligning the opportunity, product, operating model, technology, governance, economics, leadership, and capital strategy from the beginning.</p>
        <p>Bailiwick Ventures is not defined by a single industry or product. It invests behind durable theses, experienced operators, differentiated technologies, and business models capable of creating measurable enterprise value.</p>""")

_M2 = more("More on where we look", """
        <p>We are especially interested in enterprise technology, artificial intelligence, restaurant and hospitality technology, food and consumer markets, finance, operational infrastructure, and businesses undergoing technology-enabled transformation.</p>
        <p>We do not invest simply because a category is fashionable. We look for situations where a thoughtful change in architecture can materially alter enterprise value — and where active ownership creates value beyond capital alone.</p>""")

_M3 = more("More on the work", """
        <p>That range has given him a practical understanding of how ideas move through the full enterprise lifecycle: insight, strategy, product, operations, economics, capital, execution, value.</p>
        <p>His work is grounded in the belief that complex problems cannot be solved by optimizing one business function in isolation. Technology must align with the operating model. The operating model must support the customer promise. The economics must support the product. Capital must fund measurable value-creation milestones. Governance must be designed into the system. And the company narrative must accurately explain what the enterprise can prove and deliver.</p>
        <p>Michael is also the creator of the Certified Intelligence framework and the author of <i>The Certified Enterprise</i>, and is the founder of FohBoh.ai — the first major commercial implementation of that work.</p>""")

_M4 = more("More on the discipline", """
      <p>Most specialists work within one layer of a business. A strategist defines the market opportunity. A product leader shapes the offering. A systems architect designs the technology. A CFO builds the financial structure. An investment banker considers valuation and capital. An operator creates the processes required to execute.</p>
      <p>An Enterprise Venture Architect connects all of them. The work begins with a consequential problem and a clear thesis, then translates that thesis into a category, business model, operating system, technology platform, governance framework, commercial strategy, and credible path to capital. The result is not simply a company with a product — it is an enterprise designed as an integrated system.</p>
      <p><b>The distinction.</b> A systems architect designs the technical structure that lets complex systems function. An enterprise systems architect aligns technology, data, applications, and business processes across an organization. An Enterprise Venture Architect operates one level above and across both: systems architecture helps the technology work; enterprise venture architecture helps the entire company work.</p>""")


HERO_MOTIF = """<svg class="hero-motif" viewBox="0 0 400 300" fill="none" aria-hidden="true">
  <g stroke="#12304F" stroke-width="1.6" stroke-linecap="round">
    <path d="M28 268 L96 224 M96 224 L152 252 M96 224 L182 168 M182 168 L248 196
             M182 168 L256 108 M248 196 L330 138 M256 108 L330 138 M256 108 L302 32
             M330 138 L360 56 M360 56 L302 32 M96 224 L112 142 M112 142 L58 92
             M112 142 L182 168"/>
  </g>
  <g fill="#12304F">
    <circle cx="28" cy="268" r="5"/><circle cx="96" cy="224" r="7"/>
    <circle cx="152" cy="252" r="4.5"/><circle cx="182" cy="168" r="7"/>
    <circle cx="248" cy="196" r="5"/><circle cx="256" cy="108" r="7"/>
    <circle cx="330" cy="138" r="5.5"/><circle cx="112" cy="142" r="5"/>
    <circle cx="58" cy="92" r="4.5"/><circle cx="360" cy="56" r="5"/>
    <circle cx="302" cy="32" r="10"/>
  </g>
</svg>"""

LIFECYCLE = """<svg class="lifecycle" viewBox="0 0 1000 200" role="img" aria-label="The venture lifecycle: an idea becomes a thesis, then an architecture, design, proof, validation and capital plan inside Bailiwick Venture Studio, then is hardened, productized and taken to market by BailiwickVibe, reaching growth. Validation iterates back to architecture.">
  <g stroke="#C7D0D9" stroke-width="1" stroke-dasharray="4 5"><path d="M195 26 V186 M645 26 V186"/></g>
  <g font-size="10" font-weight="700" letter-spacing=".18em" fill="#6B8AA6">
    <text x="14" y="22">ORIGINATION</text>
    <text x="211" y="22">BAILIWICK STUDIO</text>
    <text x="661" y="22">BAILIWICKVIBE</text>
  </g>

  <defs><marker id="ah" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M0 0 L8 4 L0 8 Z" fill="#9BA9B6"/></marker></defs>
  <path d="M510 128 C 468 74, 282 74, 240 128" fill="none" stroke="#9BA9B6" stroke-width="1.5"
        stroke-dasharray="5 4" marker-end="url(#ah)"/>
  <text x="375" y="80" font-size="10.5" font-style="italic" fill="#7A858F" text-anchor="middle">iterate</text>

  <g stroke="#12304F" stroke-width="2.6" stroke-linecap="round" fill="none">
    <path d="M60 138 H950"/>
  </g>
  <g fill="#12304F">
    <circle cx="60" cy="138" r="7"/><circle cx="150" cy="138" r="7"/><circle cx="240" cy="138" r="7"/>
    <circle cx="330" cy="138" r="7"/><circle cx="420" cy="138" r="7"/><circle cx="510" cy="138" r="7"/>
    <circle cx="600" cy="138" r="7"/><circle cx="690" cy="138" r="7"/><circle cx="780" cy="138" r="7"/>
    <circle cx="870" cy="138" r="7"/><circle cx="950" cy="138" r="11"/>
  </g>
  <g font-size="11" font-weight="600" fill="#14181D" text-anchor="middle">
    <text x="60" y="172">Idea</text><text x="150" y="172">Thesis</text><text x="240" y="172">Architecture</text>
    <text x="330" y="172">Design</text><text x="420" y="172">Proof</text><text x="510" y="172">Validation</text>
    <text x="600" y="172">Capital plan</text><text x="690" y="172">Harden</text><text x="780" y="172">Productize</text>
    <text x="870" y="172">Market entry</text><text x="950" y="172">Growth</text>
  </g>
</svg>"""


def home(portrait):
    return f"""
<div class="hero">
  {HERO_MOTIF}
  <div class="shell hero-in">
    <p class="eyebrow">Bailiwick Ventures, Inc.</p>
    <h1>We build, own, and advise businesses at inflection points.</h1>
    <p class="lede">A privately held investment and operating company led by Michael&nbsp;L.&nbsp;Atkinson. We invest in, develop, and advise companies where technology, operating complexity, capital, and market transformation intersect.</p>
    <div class="btns">
      <a class="btn btn-p" href="about.html">Explore Bailiwick <span class="arrow">→</span></a>
      <a class="btn btn-s" href="advisory.html">Strategic Advisory <span class="arrow">→</span></a>
    </div>
    <div class="tagline"><span>Capital</span><i></i><span>Architecture</span><i></i><span>Execution</span></div>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">The company</p>
      <h2>An active owner, not a passive holding company.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:26px">Bailiwick Ventures combines investment discipline with operating experience. Our work spans venture creation, strategic advisory, technology commercialization, enterprise architecture, and selective investment.</p>
      <ul class="ticks">
        <li><b>Invest</b> in businesses and intellectual property where active involvement can create disproportionate value.</li>
        <li><b>Advise</b> executives, founders, and investors confronting consequential strategic or capital decisions.</li>
        <li><b>Build</b> new ventures through Bailiwick Venture Studio, and take validated products to production through BailiwickVibe.</li>
      </ul>
      {_M1}
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Our platform</p>
    <h2 style="max-width:20ch;margin-bottom:clamp(30px,4vw,50px)">Four ways Bailiwick creates value.</h2>
    <div class="grid g4">
      <a class="card k-adv" href="advisory.html">
        <div class="swatch"></div>
        <div class="kicker">Counsel</div>
        <h3>Strategic Advisory</h3>
        <p>Michael L. Atkinson advises private equity firms, founders, ResTech companies, finance businesses, and CPG organizations on strategy, technology, commercialization, operations, and capital.</p>
        <span class="tlink">Explore Advisory <span class="arrow">→</span></span>
      </a>
      <a class="card k-studio" href="studio.html">
        <div class="swatch"></div>
        <div class="kicker">Division</div>
        <h3>Bailiwick Venture Studio</h3>
        <p>Our AI-native venture architecture division transforms consequential ideas into validated, fundable ventures — from thesis through usable proof of concept.</p>
        <span class="tlink">Visit the Studio <span class="arrow">→</span></span>
      </a>
      <a class="card k-vibe" href="vibe.html">
        <div class="swatch"></div>
        <div class="kicker">Division</div>
        <h3>BailiwickVibe</h3>
        <p>Venture-In-a-Box Engineering. Our production engineering and market-entry division takes validated prototypes to production, and from production to first customers and first capital.</p>
        <span class="tlink">Visit BailiwickVibe <span class="arrow">→</span></span>
      </a>
      <a class="card" href="portfolio.html">
        <div class="swatch"></div>
        <div class="kicker">Holdings</div>
        <h3>Portfolio</h3>
        <p>Operating companies, studio-developed ventures, strategic investments, and intellectual property owned or supported through Bailiwick Ventures.</p>
        <span class="tlink">View Portfolio <span class="arrow">→</span></span>
      </a>
    </div>
  </div>
</section>

<section class="on-warm bord">
  <div class="shell">
    <p class="eyebrow">The venture lifecycle</p>
    <h2 style="max-width:24ch">One company, end to end.</h2>
    <p class="body" style="margin-top:18px;margin-bottom:clamp(30px,4vw,46px)">An idea becomes a thesis, an architecture, and a proof inside Bailiwick Venture Studio. BailiwickVibe hardens it, productizes it, and takes it to market. Bailiwick Ventures owns, funds, and governs the whole path.</p>
    <div style="border:1px solid var(--line);border-radius:3px;background:var(--warm);padding:clamp(18px,2.4vw,30px);overflow-x:auto">
      {LIFECYCLE}
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell split">
    <div>
      <p class="eyebrow">The investment thesis</p>
      <h2>We prefer complex problems.</h2>
      <p class="body" style="margin-top:22px">Bailiwick is attracted to opportunities where domain expertise, technology, capital, and business architecture must work together.</p>
      <a class="tlink" href="investing.html" style="margin-top:8px">How we invest <span class="arrow">→</span></a>
    </div>
    <div>
      <ul class="ticks" style="margin-bottom:14px">
        <li>Consequential problems with measurable economic value.</li>
        <li>Structural inefficiency or market fragmentation.</li>
        <li>Differentiated technology, operating models, or intellectual property.</li>
      </ul>
      {_M2}
    </div>
  </div>
</section>

<section class="on-warm">
  <div class="shell">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:clamp(28px,3.5vw,44px)">
      <div>
        <p class="eyebrow">Portfolio &amp; holdings</p>
        <h2 style="max-width:22ch">A portfolio of companies, ventures, and intellectual property.</h2>
      </div>
      <a class="tlink" href="portfolio.html">View the full portfolio <span class="arrow">→</span></a>
    </div>
    <div class="grid g3">
      <a class="card" href="portfolio.html#fohboh" style="border-left:2px solid var(--bronze)">
        <div class="kicker">Studio-born portfolio asset</div>
        <h3>FohBoh.ai</h3>
        <p>Certified intelligence infrastructure for enterprise operational data and AI, built for the restaurant industry. Sentry, Cortex and the Metrics Governance Engine.</p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Operating</dd></div>
          <div><dt>Sector</dt><dd>Enterprise AI / ResTech</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Venture Studio</dd></div>
        </dl>
      </a>
      <a class="card" href="portfolio.html#ip">
        <div class="kicker">Intellectual property</div>
        <h3>Frameworks &amp; Methods</h3>
        <p>Proprietary frameworks, methods, and systems developed and owned through Bailiwick Ventures, including Enterprise Venture Architecture.</p>
        <dl class="meta">
          <div><dt>Status</dt><dd>Held &amp; licensed</dd></div>
          <div><dt>Origin</dt><dd>Bailiwick Ventures</dd></div>
        </dl>
      </a>
      <a class="card" href="contact.html">
        <div class="kicker">Open</div>
        <h3>Next Venture</h3>
        <p>We are actively evaluating new ventures, strategic investments, and partnerships where architecture can change value.</p>
        <span class="tlink" style="margin-top:auto">Bring us an opportunity <span class="arrow">→</span></span>
      </a>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell split split-even" style="align-items:center">
    <div class="portrait"><img src="{portrait}" alt="Michael L. Atkinson" width="900" height="900" loading="lazy"></div>
    <div>
      <p class="eyebrow">Michael L. Atkinson</p>
      <h2>Enterprise Venture Architect. Investor. Strategic Advisor.</h2>
      <p class="body" style="margin-top:22px">Michael is a co-founder and the Chief Executive Officer of Bailiwick Ventures. His career spans operations, CFO leadership, investment banking, investing, software and systems architecture, venture creation, and commercialization.</p>
      <p class="body">That experience gives him an unusual ability to examine a business simultaneously through the lenses of enterprise architecture, capital and economics, and execution.</p>
      <div class="btns" style="margin-top:26px">
        <a class="btn btn-s" href="about.html">Meet Michael <span class="arrow">→</span></a>
      </div>
    </div>
  </div>
</section>
"""


ORG_SVG = """
<svg class="org" viewBox="0 0 1000 470" role="img" aria-label="Bailiwick organizational structure: Michael L. Atkinson, Co-founder and CEO, above Bailiwick Ventures, Inc., the parent investment and operating company, which contains the operating divisions Bailiwick Venture Studio and BailiwickVibe and the studio-born portfolio asset FohBoh.ai. MichaelAtkinson.me and Michael L. Atkinson Advisory sit alongside.">
  <defs>
    <style>
      .bx{fill:#FFFDF9;stroke:#12304F;stroke-width:1.4}
      .bx-d{fill:#FFFDF9;stroke:#B9C6D2;stroke-width:1.2;stroke-dasharray:5 4}
      .bx-p{fill:#12304F;stroke:#12304F;stroke-width:1.4}
      .t1{font:600 15px var(--sans);fill:#14181D}
      .t1w{font:600 15px var(--sans);fill:#FFFDF9}
      .t2{font:500 11.5px var(--sans);fill:#6B8AA6}
      .t2w{font:500 11.5px var(--sans);fill:#9FB4C6}
      .t3{font:400 11px var(--sans);fill:#4A5560}
      .ln{stroke:#12304F;stroke-width:1.2;fill:none}
      .ln-d{stroke:#B9C6D2;stroke-width:1.2;fill:none;stroke-dasharray:5 4}
    </style>
  </defs>

  <rect class="bx-p" x="360" y="10" width="280" height="56" rx="3"/>
  <text class="t1w" x="500" y="34" text-anchor="middle">Michael L. Atkinson</text>
  <text class="t2w" x="500" y="52" text-anchor="middle">Co-founder &amp; Chief Executive Officer</text>

  <path class="ln-d" d="M360 38 H150 V112"/>
  <path class="ln-d" d="M640 38 H850 V112"/>
  <path class="ln" d="M500 66 V112"/>

  <rect class="bx-d" x="20" y="112" width="260" height="54" rx="3"/>
  <text class="t1" x="150" y="136" text-anchor="middle">MichaelAtkinson.me</text>
  <text class="t2" x="150" y="153" text-anchor="middle">Executive authority platform</text>

  <rect class="bx-d" x="720" y="112" width="260" height="54" rx="3"/>
  <text class="t1" x="850" y="136" text-anchor="middle">Atkinson Advisory</text>
  <text class="t2" x="850" y="153" text-anchor="middle">Professional services, PE / ResTech / CPG</text>

  <rect class="bx" x="330" y="112" width="340" height="60" rx="3"/>
  <text class="t1" x="500" y="138" text-anchor="middle" style="font-size:17px">Bailiwick Ventures, Inc.</text>
  <text class="t2" x="500" y="157" text-anchor="middle">Parent investment &amp; operating company</text>

  <path class="ln" d="M500 172 V214 M170 214 H830 M170 214 V262 M500 214 V262 M830 214 V262"/>

  <rect class="bx" x="30" y="262" width="280" height="126" rx="3"/>
  <rect x="30" y="262" width="280" height="3" fill="#1F5FD0"/>
  <text class="t1" x="170" y="294" text-anchor="middle" style="font-size:16px">Bailiwick Venture Studio</text>
  <text class="t2" x="170" y="313" text-anchor="middle">Wholly owned operating division</text>
  <line x1="70" y1="330" x2="270" y2="330" stroke="#E0D8CB"/>
  <text class="t3" x="170" y="352" text-anchor="middle">Venture architecture,</text>
  <text class="t3" x="170" y="369" text-anchor="middle">POC / MVP development</text>

  <rect class="bx" x="360" y="262" width="280" height="126" rx="3"/>
  <rect x="360" y="262" width="280" height="3" fill="#E2551F"/>
  <text class="t1" x="500" y="294" text-anchor="middle" style="font-size:16px">BailiwickVibe</text>
  <text class="t2" x="500" y="313" text-anchor="middle">Wholly owned operating division</text>
  <line x1="400" y1="330" x2="600" y2="330" stroke="#E0D8CB"/>
  <text class="t3" x="500" y="352" text-anchor="middle">Production engineering,</text>
  <text class="t3" x="500" y="369" text-anchor="middle">productization &amp; go-to-market</text>

  <rect class="bx" x="690" y="262" width="280" height="126" rx="3"/>
  <rect x="690" y="262" width="280" height="3" fill="#A8763E"/>
  <text class="t1" x="830" y="294" text-anchor="middle" style="font-size:16px">FohBoh.ai</text>
  <text class="t2" x="830" y="313" text-anchor="middle">Studio-born portfolio asset</text>
  <line x1="730" y1="330" x2="930" y2="330" stroke="#E0D8CB"/>
  <text class="t3" x="830" y="352" text-anchor="middle">Commercial implementation of</text>
  <text class="t3" x="830" y="369" text-anchor="middle">certified intelligence</text>

  <line x1="20" y1="418" x2="980" y2="418" stroke="#E0D8CB"/>
  <text class="t3" x="500" y="442" text-anchor="middle" style="font-style:italic">Bailiwick Venture Studio moves ventures from idea to usable proof of concept.</text>
  <text class="t3" x="500" y="460" text-anchor="middle" style="font-style:italic">BailiwickVibe takes validated products from MVP to production and market entry.</text>
</svg>
"""


def about(portrait):
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">About</p>
    <h1>A long-term platform for venture creation and ownership.</h1>
    <p class="lede">Bailiwick Ventures, Inc. is Michael L. Atkinson's privately held investment and operating company. Michael serves as co-founder and Chief Executive Officer, directing the company's strategy, investments, operating divisions, and venture-development priorities.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Approach</p>
      <h2>Architecture before acceleration.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:26px">Bailiwick Ventures reflects a multidisciplinary career across operations, finance, investment banking, investing, enterprise technology, software design, commercialization, and company building. That experience shapes how the company works.</p>
      <ul class="crit">
        <li><b>Architecture before acceleration.</b> Design the system before you scale it.</li>
        <li><b>Evidence before investment.</b> Fund what has been demonstrated, not what has been asserted.</li>
        <li><b>Economics before scale.</b> Unit economics decide whether growth creates or destroys value.</li>
        <li><b>Governance before complexity.</b> Controls are cheaper to design in than to retrofit.</li>
        <li><b>Commercial validation before institutional expansion.</b> Customers first, headcount second.</li>
        <li><b>Active ownership rather than passive participation.</b> Judgment is part of the capital.</li>
      </ul>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">The structure</p>
    <h2 style="max-width:26ch">One parent company. Two operating divisions. Clear boundaries.</h2>
    <p class="body" style="margin-top:20px;margin-bottom:clamp(32px,4vw,48px)">Bailiwick Ventures supports companies throughout their development while preserving clear distinctions between investment, personal advisory, venture creation, and product engineering.</p>
    <div style="border:1px solid var(--line);border-radius:3px;background:var(--warm);padding:clamp(20px,3vw,40px)">
      {ORG_SVG}
    </div>
    <div class="grid g3" style="margin-top:clamp(26px,3vw,38px)">
      <div>
        <h4 style="margin-bottom:10px">Bailiwick Ventures, Inc.</h4>
        <p class="small">The parent investment and operating company. It holds investments and ownership interests, develops and supports new ventures, participates in transactions and capital formation, owns intellectual property, and sponsors its operating divisions.</p>
      </div>
      <div>
        <h4 style="margin-bottom:10px">Bailiwick Venture Studio</h4>
        <p class="small">A wholly owned operating division, not a separate legal entity. The Studio applies Enterprise Venture Architecture to the development, validation, commercialization, and funding of new ventures.</p>
      </div>
      <div>
        <h4 style="margin-bottom:10px">BailiwickVibe</h4>
        <p class="small">A wholly owned operating division carrying validated products through production engineering, enterprise readiness, market entry, and early scale. <a class="tlink" href="https://bailiwickvibe.com" target="_blank" rel="noopener">bailiwickvibe.com ↗</a></p>
      </div>
    </div>
    <div class="grid g3" style="margin-top:clamp(20px,2.4vw,28px)">
      <div>
        <h4 style="margin-bottom:10px">MichaelAtkinson.me</h4>
        <p class="small">Michael's personal authority platform — writing, speaking, and advisory, distinct from the company. <a class="tlink" href="https://michaelatkinson.me" target="_blank" rel="noopener">michaelatkinson.me ↗</a></p>
      </div>
      <div>
        <h4 style="margin-bottom:10px">FohBoh.ai</h4>
        <p class="small">The Studio-born portfolio asset commercializing certified intelligence for the restaurant industry. <a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener">fohboh.ai ↗</a></p>
      </div>
      <div>
        <h4 style="margin-bottom:10px">Atkinson Advisory</h4>
        <p class="small">Professional services delivered by Michael personally to private equity, ResTech, finance and CPG clients. <a class="tlink" href="advisory.html">Advisory</a></p>
      </div>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell split split-even" style="align-items:center">
    <div>
      <p class="eyebrow">Michael L. Atkinson</p>
      <h2>A career built across the systems that make enterprises work.</h2>
      <p class="body" style="margin-top:22px">Michael's career does not fit neatly into one conventional category. He has operated businesses, managed finance, advised transactions, invested capital, designed software, created ventures, developed enterprise frameworks, and built companies.</p>
      {_M3}
      <div class="btns" style="margin-top:26px">
        <a class="btn btn-g" href="advisory.html">Strategic Advisory <span class="arrow">→</span></a>
        <a class="btn btn-g" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
      </div>
    </div>
    <div class="portrait" style="border-color:#274259"><img src="{portrait}" alt="Michael L. Atkinson" width="900" height="900" loading="lazy"></div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">The team</p>
    <h2 style="max-width:26ch">The team is the two divisions.</h2>
    <p class="lede" style="margin-top:20px;margin-bottom:clamp(30px,3.6vw,44px)">Bailiwick does not carry a head office of generalists. Capability lives inside Bailiwick Venture Studio and BailiwickVibe, and is assembled around whichever venture needs it.</p>
    <div class="grid g4">
      <div><h4 style="margin-bottom:10px">Build</h4><p class="body" style="font-size:14.4px">Engineers, AI agent developers, systems architects, and QA managers.</p></div>
      <div><h4 style="margin-bottom:10px">Intelligence</h4><p class="body" style="font-size:14.4px">Data and analytics specialists.</p></div>
      <div><h4 style="margin-bottom:10px">Product</h4><p class="body" style="font-size:14.4px">UI and UX designers, and project managers.</p></div>
      <div><h4 style="margin-bottom:10px">Market</h4><p class="body" style="font-size:14.4px">Go-to-market strategists, sales, and marketing.</p></div>
    </div>
    <div class="grid g2" style="margin-top:clamp(24px,3vw,34px)">
      <div class="card">
        <div class="kicker">Where the people sit</div>
        <h3 style="font-size:19px">Through the divisions and FohBoh.ai</h3>
        <p style="margin-bottom:0">Teams are drawn from <a class="tlink" href="studio.html">Bailiwick Venture Studio</a>, <a class="tlink" href="https://bailiwickvibe.com" target="_blank" rel="noopener">BailiwickVibe</a>, and <a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener">FohBoh.ai</a> — which means a venture gets people who have already shipped certified infrastructure, not a team hired for the occasion.</p>
      </div>
      <div class="card">
        <div class="kicker">Counsel</div>
        <h3 style="font-size:19px">Velawood</h3>
        <p style="margin-bottom:0">General counsel is provided through Velawood, a full-service law firm for startups and early-stage companies, based in Dallas, Texas. <a class="tlink" href="https://velawood.com" target="_blank" rel="noopener">velawood.com <span class="arrow">↗</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="bord on-warm">
  <div class="shell">
    <p class="eyebrow">What an Enterprise Venture Architect does</p>
    <h2 style="max-width:24ch">Most people build products. Some build companies.</h2>
    <p class="lede" style="margin-top:20px">Michael designs the frameworks from which companies can be built — integrating strategy, product, capital formation, governance, operating models, technology architecture, commercialization, and organizational design into a scalable enterprise.</p>
    {_M4}
  </div>
</section>
"""


def advisory():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Strategic advisory</p>
    <h1>Strategic counsel for complex businesses and consequential decisions.</h1>
    <p class="lede">Michael L. Atkinson advises executives, founders, investors, and private equity firms when the problem crosses traditional functional boundaries. His work combines operating experience, finance, investment banking, technology, venture architecture, and commercialization.</p>
    <div class="btns">
      <a class="btn btn-p" href="contact.html">Discuss an Engagement <span class="arrow">→</span></a>
    </div>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <p class="eyebrow">Who engages Michael</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(28px,3.5vw,44px)">Four kinds of client, one kind of problem.</h2>
    <div class="grid g4">
      <div class="card">
        <div class="kicker">01</div>
        <h3>Private Equity</h3>
        <p>Portfolio-company architecture, technology strategy, commercial repositioning, venture assessment, operating-model review, and value-creation planning.</p>
      </div>
      <div class="card">
        <div class="kicker">02</div>
        <h3>Founders &amp; Technology Companies</h3>
        <p>Product-market architecture, positioning, business models, capital formation, go-to-market, and executive decision support.</p>
      </div>
      <div class="card">
        <div class="kicker">03</div>
        <h3>Restaurant &amp; ResTech</h3>
        <p>Operational technology, platform strategy, AI infrastructure, enterprise architecture, and industry transformation.</p>
      </div>
      <div class="card">
        <div class="kicker">04</div>
        <h3>CPG, Finance &amp; Adjacent</h3>
        <p>Technology-enabled business models, operating systems, venture strategy, commercialization, and capital.</p>
      </div>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell split">
    <div>
      <p class="eyebrow">Areas of counsel</p>
      <h2>Judgment, not methodology.</h2>
      <p class="body" style="margin-top:20px">Clients engage Michael for his cross-disciplinary perspective — not for a generic consulting framework applied to an unfamiliar business.</p>
    </div>
    <div>
      <div class="grid g2" style="gap:0 34px">
        <ul class="ticks">
          <li>CEO and founder strategy</li>
          <li>Board and investor advisory</li>
          <li>Enterprise venture architecture</li>
          <li>AI governance and enterprise trust</li>
          <li>Product and platform strategy</li>
          <li>Commercialization and market positioning</li>
        </ul>
        <ul class="ticks">
          <li>Capital formation and transaction strategy</li>
          <li>Business-model and operating-model design</li>
          <li>Restaurant and hospitality technology</li>
          <li>Finance and consumer packaged goods strategy</li>
          <li>Venture assessment and reconstruction</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">Ideal engagements</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(26px,3vw,40px)">When the call is worth making.</h2>
    <div class="grid g3">
      <div><p class="body">A founder has a strong idea but an incomplete venture.</p></div>
      <div><p class="body">A company has built capable technology but lacks a compelling commercial architecture.</p></div>
      <div><p class="body">A private equity firm is evaluating or transforming a portfolio company.</p></div>
      <div><p class="body">An enterprise is deciding how AI should fit into its operating model.</p></div>
      <div><p class="body">A leadership team needs an independent systems-level assessment.</p></div>
      <div><p class="body">A company is preparing for financing, strategic partnership, or a transaction.</p></div>
    </div>
    <hr class="rule" style="margin:clamp(34px,4vw,52px) 0 26px">
    <p class="small" style="color:#8FA1B1;max-width:74ch">Advisory engagements are undertaken through Bailiwick Ventures, Inc. For full venture development, product creation, or multidisciplinary execution, engagements may be undertaken through <a href="studio.html" style="color:var(--warm)">Bailiwick Venture Studio</a>. For production engineering and post-MVP commercialization, work may be undertaken through <a href="vibe.html" style="color:var(--warm)">BailiwickVibe</a>.</p>
  </div>
</section>

<section class="bord on-warm tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:20ch;margin:0 auto">Describe the situation. We will tell you whether we can help.</h2>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""
