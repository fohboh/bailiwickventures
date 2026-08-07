"""Blog and Book — drafted content with clearly marked blanks."""
from pages_a import more

_B1 = more("More on the problem", """
    <p>Modern multi-unit businesses are paralysed by a hidden dysfunction. They have invested in best-in-class systems for point-of-sale, inventory, labor, and finance, but these systems operate as isolated kingdoms. Each produces its own conflicting version of core metrics like "sales," "cost," and "labor."</p>
    <p>Leaders waste time reconciling numbers instead of making decisions. AI initiatives fail, fed on contradictory data. This is the costly reality for any business with a complex operational stack.</p>""")

_B2 = more("More on who should read it", """
    <p>The book is written for the person who has to sign off on a number, not the person who computes it. It starts in restaurants — the industry where the author spent three decades and where the dysfunction is most visible — but the argument holds for any business running a complex operational stack.</p>""")

TOFILL = '<span class="tofill">to fill</span>'
DRAFT = '<span class="tofill">draft</span>'

# The legacy bailiwickventures.com/certified-enterprise-book page, reproduced
# in full inside a chevron disclosure so nothing links out to the old site.
LEGACY_BOOK = """
<section class="bord on-warm" id="fullpage">
  <div class="shell">
    <p class="eyebrow">The full book page</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(20px,2.4vw,28px)">Everything from the original announcement.</h2>
    <p class="body" style="margin-top:-8px;margin-bottom:clamp(22px,2.6vw,32px);max-width:62ch">The book page that lived on the previous Bailiwick Ventures site, brought across in full. Nothing links out to it any more &mdash; it is here.</p>

    <details class="reveal">
      <summary>
        <span class="rl">The Certified Enterprise &mdash; the full book page</span>
        <span class="rn">The universal problem, the author, and what publishes in November</span>
        <span class="chev"><svg width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true"><path d="M1 1.5L6 6.5L11 1.5" stroke="#12304F" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </summary>
      <div class="rbody">

        <p class="eyebrow">The universal problem</p>
        <h3 style="font-size:clamp(21px,2.3vw,28px);margin-bottom:16px">The Data Civil War</h3>
        <p class="pull" style="margin-top:0;margin-bottom:26px">&ldquo;The next billion-dollar restaurant advantage won&rsquo;t be more AI &mdash; it will be knowing which numbers to believe.&rdquo;</p>
        <p class="body">Modern multi-unit businesses are paralyzed by a hidden dysfunction. They have invested in best-in-class systems for point-of-sale, inventory, labor, and finance, but these systems operate as isolated kingdoms. Each produces its own conflicting version of core metrics like &ldquo;sales,&rdquo; &ldquo;cost,&rdquo; and &ldquo;labor.&rdquo;</p>
        <p class="body">Leaders waste time reconciling numbers instead of making decisions. AI initiatives fail, fed on contradictory data. This is the costly reality for any business with a complex operational stack. <i>The Certified Enterprise</i> introduces and defines the alternative: an organization that has ended its internal data civil war and now competes on trusted intelligence.</p>

        <hr class="rule" style="margin:clamp(26px,3vw,38px) 0">

        <p class="eyebrow">About the author</p>
        <h3 style="font-size:clamp(21px,2.3vw,28px);margin-bottom:16px">Michael L. Atkinson</h3>
        <p class="body">Michael L. Atkinson is the Chief Executive Officer of Bailiwick Ventures and a three-decade veteran of the restaurant-technology collision. A founder, operator, investor, entrepreneur and innovator, he has built companies to solve the chaos he has managed firsthand. Most recently he founded FohBoh.ai, a native Gen&nbsp;AI operating system for the global restaurant industry.</p>
        <p class="body">This book provides the blueprint he wished he had had: a practical guide to replacing data chaos with certified truth &mdash; the only foundation for a future-proof business.</p>

        <hr class="rule" style="margin:clamp(26px,3vw,38px) 0">

        <p class="eyebrow">Coming soon</p>
        <p class="body" style="max-width:60ch">Expected November 2026, self-published on Amazon in hardcover and paperback. Pre-orders are open now.</p>
        <p class="pull" style="margin-top:20px;margin-bottom:24px">The future of AI in restaurants will not be defined by who builds the best model. It will be defined by who controls the integrity of the data those models rely on.</p>
        <div class="btns" style="margin-top:0">
          <a class="btn btn-p" href="https://www.bailiwickventures.com/pre-order" target="_blank" rel="noopener">Pre-Order <span class="arrow">&#8599;</span></a>
          <a class="btn btn-s" href="contact.html">Bulk or speaking <span class="arrow">&rarr;</span></a>
        </div>

      </div>
    </details>
  </div>
</section>
"""


def book(cover):
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <div class="split split-even" style="align-items:center">
      <div>
        <p class="eyebrow">The book</p>
        <h1 style="max-width:14ch">The Certified Enterprise</h1>
        <p class="lede" style="margin-top:18px;font-style:italic;color:var(--navy)">Taming Data Anarchy in the AI Era</p>
        <p class="lede" style="margin-top:20px">A new competitive paradigm for organizations that have ended their internal data civil war and now compete on trusted intelligence. In an age of analytic abundance, the ultimate advantage is not more data, but certified truth.</p>
        <p class="pull">&ldquo;The next billion-dollar restaurant advantage won't be more AI — it will be knowing which numbers to believe.&rdquo;</p>
        <div class="btns">
          <a class="btn btn-p" href="https://www.bailiwickventures.com/pre-order" target="_blank" rel="noopener">Pre-Order <span class="arrow">↗</span></a>
          <a class="btn btn-s" href="#fullpage">Read the full book page <span class="arrow">↓</span></a>
        </div>
        <p class="fine" style="margin-top:20px">By Michael L. Atkinson · Self-published on Amazon · Expected November 2026 · Hardcover and paperback</p>
      </div>
      <div>
        <img class="jacket" src="{cover}" alt="The Certified Enterprise, by Michael L. Atkinson — hardcover" width="760" height="897" loading="eager">
      </div>
    </div>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">The universal problem</p>
      <h2>The Data Civil War.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:24px">Best-in-class systems for point-of-sale, inventory, labor and finance, each operating as an isolated kingdom, each producing its own conflicting version of "sales," "cost" and "labor."</p>
      <p class="body">Leaders waste time reconciling numbers instead of making decisions. AI initiatives fail, fed on contradictory data. The book introduces and defines the alternative: <b>The Certified Enterprise</b> — an organization that has ended its internal data civil war and now competes on trusted intelligence.</p>
      {_B1}
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Inside the book</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(28px,3.5vw,44px)">What it covers.</h2>
    <p class="body" style="margin-top:-14px;margin-bottom:clamp(28px,3.4vw,40px)">Three parts, twelve chapters, an epilogue, and four appendices.</p>
    <div class="grid g3">
      <div class="card">
        <div class="kicker">Part I</div>
        <h3>The Problem of Truth</h3>
        <ul class="toc">
          <li><span class="cn">1</span><span class="ct">The Hidden Architecture of Chaos</span></li>
          <li><span class="cn">2</span><span class="ct">The Illusion of Clean Data</span></li>
          <li><span class="cn">3</span><span class="ct">The AI Mirage</span></li>
          <li><span class="cn">4</span><span class="ct">Why Restaurants Break AI Faster</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="kicker">Part II</div>
        <h3>The Truth Layer</h3>
        <ul class="toc">
          <li><span class="cn">5</span><span class="ct">Introducing the Truth Layer</span></li>
          <li><span class="cn">6</span><span class="ct">The Trust Score Playbook</span></li>
          <li><span class="cn">7</span><span class="ct">The Cognitive Layer</span></li>
          <li><span class="cn">8</span><span class="ct">Truth Guardians</span></li>
          <li><span class="cn sub">8.1</span><span class="ct">The 90-Day MGE Implementation Playbook</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="kicker">Part III</div>
        <h3>The Competitive Advantage</h3>
        <ul class="toc">
          <li><span class="cn">9</span><span class="ct">Competing on Truth</span></li>
          <li><span class="cn sub">9.1</span><span class="ct">The Economics of Truth</span></li>
          <li><span class="cn sub">9.2</span><span class="ct">Architecting the Governed Stack</span></li>
          <li><span class="cn">10</span><span class="ct">The Real Cost of Truth, Cost of Indecisions (CID)</span></li>
          <li><span class="cn">11</span><span class="ct">The Future Is Certified</span></li>
          <li><span class="cn">12</span><span class="ct">The Truth Advantage in the Market</span></li>
          <li><span class="cn">—</span><span class="ct">The Truth Renaissance</span></li>
        </ul>
      </div>
    </div>

    <div class="tail">
      <div>
        <div class="kicker">Epilogue</div>
        <h4>Your Next Chapter: A Leader&rsquo;s Manifesto</h4>
      </div>
      <div>
        <div class="kicker">Appendices</div>
        <ul class="appx">
          <li><span class="ax">A</span>The Truth Renaissance Glossary</li>
          <li><span class="ax">C</span>The KPI Reconciliation Matrix</li>
          <li><span class="ax">D</span>The Trust Score Framework</li>
          <li><span class="ax">F</span>The Comprehensive Glossary</li>
        </ul>
      </div>
    </div>
  </section>

<section class="on-ink">
  <div class="shell split">
    <div>
      <p class="eyebrow">Who it is for</p>
      <h2>Anyone who has to sign off on a number.</h2>
    </div>
    <div>
      <ul class="ticks">
        <li>Executives deciding how AI should fit into their operating model.</li>
        <li>Boards and audit committees asking what the numbers actually rest on.</li>
        <li>CFOs, controllers, and operators living with reconciliation by hand.</li>
        <li>Investors evaluating whether a company's reported metrics can be defended.</li>
        <li>Technology leaders building data, analytics, and AI platforms.</li>
        <li>Founders creating infrastructure in industries where trust is the constraint.</li>
      </ul>
      {_B2}
    </div>
  </div>
</section>

<!-- EARLY PRAISE — hidden until real endorsements are approved.
     Three drafts (Sebes / Zat / Kadleck) are preserved below. To restore,
     delete this comment wrapper. -->
<!--
<section class="bord on-warm">
  <div class="shell">
    <p class="eyebrow">Early praise</p>
    <h2 style="max-width:20ch;margin-bottom:clamp(22px,2.6vw,32px)">What readers are saying.</h2>

    <details class="reveal">
      <summary>
        <span class="rl">Read the early praise</span>
        <span class="rn">Three perspectives — operator, technologist, data science</span>
        <span class="chev"><svg width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true"><path d="M1 1.5L6 6.5L11 1.5" stroke="#12304F" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </summary>
      <div class="rbody">
        <div class="grid g3">
          <blockquote class="card quote">
            <span class="unapproved">Draft &middot; not yet approved</span>
            <p>Every multi-unit operator I know has lived this. You walk into a Monday meeting with three numbers for the same week and spend the first twenty minutes arguing about which one is real. Atkinson names the problem precisely and, more usefully, shows what has to change structurally before any of it gets better.</p>
            <cite>Christopher Sebes &middot; Industry Advisor &middot; ResTech CEO</cite>
          </blockquote>
          <blockquote class="card quote">
            <span class="unapproved">Draft &middot; not yet approved</span>
            <p>We have spent a decade connecting systems that were never designed to agree with one another. This book makes the case that integration was never the hard part &mdash; reconciliation and governance were. It should be required reading for anyone shipping software into a restaurant back office.</p>
            <cite>Sam Zat &middot; Executive Chairman &middot; Founder, Craftable</cite>
          </blockquote>
          <blockquote class="card quote">
            <span class="unapproved">Draft &middot; not yet approved</span>
            <p>Models do not fail because the math is wrong. They fail because the inputs were never reconciled and nobody could say which definition of a metric was authoritative. Atkinson gives that problem a name, a structure, and a remedy &mdash; without hiding behind the technology.</p>
            <cite>Jan Kadleck &middot; Founder &amp; CEO, MBI.ai</cite>
          </blockquote>
        </div>
        <p class="fine" style="margin-top:22px;margin-bottom:0">These are drafts written to show the shape and length of a usable endorsement. Nothing here has been said or approved by the people named. Send each one their quote, get it back in their own words, then remove this note and the draft markers.</p>
      </div>
    </details>
  </div>
</section>
-->

<section class="bord">
  <div class="shell split">
    <div>
      <p class="eyebrow">About the author</p>
      <h2 style="font-size:clamp(22px,2.4vw,30px)">Michael L. Atkinson</h2>
    </div>
    <div>
      <p class="body">Michael L. Atkinson, Chief Executive Officer of Bailiwick Ventures, is a three-decade veteran of the restaurant-tech collision. A founder, operator, investor, entrepreneur and innovator, he has built companies to solve the chaos he has managed firsthand. Most recently he founded FohBoh.ai, a native Gen&nbsp;AI operating system for the global restaurant industry.</p>
      <p class="body"><i>The Certified Enterprise</i> provides the blueprint he wished he had had: a practical guide to replacing data chaos with certified truth — the only foundation for a future-proof business.</p>
      <a class="tlink" href="about.html">More about Michael <span class="arrow">→</span></a>
    </div>
  </div>
</section>

{LEGACY_BOOK}

<section class="bord tight">
  <div class="shell">
    <p class="eyebrow">Publication</p>
    <div class="grid g4" style="margin-top:6px">
      <div><h4 style="margin-bottom:8px">Publisher</h4><p class="small">Self-published on Amazon.</p></div>
      <div><h4 style="margin-bottom:8px">Expected</h4><p class="small">November 2026.</p></div>
      <div><h4 style="margin-bottom:8px">Formats</h4><p class="small">Hardcover and paperback.</p></div>
      <div><h4 style="margin-bottom:8px">Links</h4>
        <p class="small" style="margin-bottom:8px"><a class="tlink" href="https://www.bailiwickventures.com/pre-order" target="_blank" rel="noopener">Pre-order <span class="arrow">↗</span></a></p>
        <p class="small" style="margin-bottom:0"><a class="tlink" href="#fullpage">Full book page <span class="arrow">↓</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="on-ink tight" id="notify">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:22ch;margin:0 auto">Be told when it publishes.</h2>
    <p class="body" style="margin:18px auto 0;max-width:54ch">Pre-order now, or subscribe on Substack for the announcement and for the essays the book grew out of.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-g" href="https://www.bailiwickventures.com/pre-order" target="_blank" rel="noopener">Pre-Order <span class="arrow">↗</span></a>
      <a class="btn btn-g" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Subscribe on Substack <span class="arrow">↗</span></a>
      <a class="btn btn-g" href="contact.html">Bulk or Speaking <span class="arrow">→</span></a>
    </div>
    <p class="pull" style="margin:clamp(34px,4vw,50px) auto 0;color:var(--warm);border-color:var(--bronze-lt);text-align:left">The future of AI in restaurants will not be defined by who builds the best model. It will be defined by who controls the integrity of the data those models rely on.</p>
  </div>
</section>
"""


POSTS = [
    ("Featured", "Why systems of record cannot certify truth",
     "The entity that generates a metric cannot also be the authority that certifies it. The argument, and what it means for every company that has bought a system of record expecting an answer.",
     "Independence", True),
    ("Essay", "Data records. Evidence proves.",
     "Two words most organizations treat as synonyms, and the gap between them that decides what a decision is actually worth.",
     "Trust", False),
    ("Essay", "AI needs evidence, not more data",
     "Abundant data and capable models have not produced certainty. What the missing layer looks like, and why it has to be deterministic.",
     "Enterprise AI", False),
    ("Essay", "Architecture before acceleration",
     "AI can now build the wrong product faster than ever. Why speed makes venture architecture more important, not less.",
     "Venture design", False),
    ("Field notes", "What forty years in restaurants taught me about enterprise software",
     "Operators do not want dashboards. They want to know whether the number is right. A view from the floor.",
     "Operations", False),
    ("Essay", "Governance before intelligence",
     "Controls designed after deployment are the most expensive controls an enterprise ever builds. A case for designing them in.",
     "Governance", False),
]


def _post_card(kind, title, dek, topic, featured):
    span = ' style="grid-column:span 2"' if featured else ''
    size = ' style="font-size:clamp(22px,2.4vw,29px)"' if featured else ''
    return f"""<article class="card post"{span}>
        <div class="kicker">{kind} · {topic}</div>
        <h3{size}>{title}</h3>
        <p>{dek}</p>
        <div class="postmeta">
          <span class="tofill">to write</span>
          <span class="pdate">Date {TOFILL}</span>
        </div>
      </article>"""


def blog():
    cards = "\n      ".join(_post_card(*p) for p in POSTS)
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Blog</p>
    <h1>Working notes on trust, architecture, and building companies.</h1>
    <p class="lede">Shorter and more frequent than the Insights essays: arguments in progress, things learned in the middle of a build, and the occasional disagreement with the industry.</p>
    <div class="btns">
      <a class="btn btn-p" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Subscribe on Substack <span class="arrow">↗</span></a>
      <a class="btn btn-s" href="insights.html">Longer essays <span class="arrow">→</span></a>
    </div>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:clamp(24px,3vw,38px)">
      <div>
        <p class="eyebrow" style="margin-bottom:10px">Recent</p>
        <h2 style="max-width:18ch">Latest posts.</h2>
      </div>
      <p class="fine" style="margin:0;max-width:40ch">Six confirmed posts. Summaries are my draft — edit freely. Dates fill in as they publish.</p>
    </div>
    <div class="grid g3">
      {cards}
    </div>
  </div>
</section>


<section class="bord on-warm">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(20px,2.4vw,30px)">
      <div>
        <p class="eyebrow">Archive</p>
        <h2 style="max-width:20ch">Published earlier.</h2>
      </div>
      <div>
        <p class="body" style="margin:0">Fourteen posts already live on the current Bailiwick Ventures site. They migrate across as-is when the new site goes up — the list below is the inventory. Each title still links to the live version until the copy is moved.</p>
      </div>
    </div>
    <div class="arch">
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">The Impact of Data Inconsistency on Business Performance</span><span class="tg">Metrics governance ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Why AI Is Useless Without Data Integrity</span><span class="tg">Restaurant AI ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">The Trust Imperative: Why Metric Governance is the Foundation of FohBoh.ai</span><span class="tg">Trust ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Bolt-On AI vs. Native AI: Why It Matters for Restaurants</span><span class="tg">Gen AI ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Why You Can't Just Connect Your POS to ChatGPT</span><span class="tg">LLM ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Why Evaluating Your Restaurant's Tech-Stack Health is Essential Right Now</span><span class="tg">ResTech ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Restaurant Digital Transformation and Performance Improvement</span><span class="tg">Data management ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Leveraging AI for Optimal Workforce Management in the Restaurant Industry</span><span class="tg">Workforce ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">How Software Companies Master Go-To-Market Strategies</span><span class="tg">GTM ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Unlocking Success: The Vital Role of Technology in Restaurant Back-of-House Management</span><span class="tg">Operations ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Revolutionizing Inventory Management in Hospitality</span><span class="tg">Inventory ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Revolutionizing Restaurant Operations: AI-Driven Procurement Marketplaces</span><span class="tg">Procurement ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">The Rising Value of Voice Technology and Embedded Voice Apps</span><span class="tg">VoiceTech ↗</span></a>
        <a href="https://www.bailiwickventures.com/blog" target="_blank" rel="noopener"><span class="t">Embracing Technology: A Recipe for Success in the Modern Restaurant Industry</span><span class="tg">ResTech ↗</span></a>
    </div>
    <div class="gate" style="margin-top:clamp(26px,3vw,36px);margin-bottom:0">
      <div class="lbl">Second source — not yet merged</div>
      <p>The FohBoh.ai Learning Center still needs to be folded in.</p>
      <p class="sub">Its posts sit behind categories — Research, Store-Level Stories, Above-Store Intel, Guides, Restaurant AI — and the page renders client-side, so I could not read the list. Grant fohboh.ai in the browser extension, or paste the titles, and I will merge both sources into one list and strip any duplicates. <span class="tofill">to fill</span></p>
    </div>
    <p class="fine" style="margin-top:20px">Further writing appears on <a class="tlink" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Substack</a> and <a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener">FohBoh.ai</a>.</p>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Topics</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(22px,2.6vw,34px)">What gets written about here.</h2>
    <div class="tagrow">
      <span class="tag">Certified Intelligence</span>
      <span class="tag">Data vs. Evidence</span>
      <span class="tag">Enterprise AI governance</span>
      <span class="tag">Deterministic systems</span>
      <span class="tag">Venture architecture</span>
      <span class="tag">Capital &amp; commercialization</span>
      <span class="tag">Restaurant technology</span>
      <span class="tag">Operational intelligence</span>
      <span class="tag">Leadership &amp; enterprise design</span>
    </div>
  </div>
</section>

<section class="on-ink tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">The essays publish first on Substack.</h2>
    <p class="body" style="margin:18px auto 0;max-width:54ch">Subscribe there and they arrive by email. Everything of lasting value is collected here and in <a href="insights.html" style="color:var(--warm)">Insights</a>.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-g" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Subscribe on Substack <span class="arrow">↗</span></a>
      <a class="btn btn-g" href="book.html">The Book <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""
