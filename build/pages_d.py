"""Privacy, 404, and the form thank-you page."""
from pages_a import more

_P1 = more("More on how long we keep things", """
    <p>Inquiry records are kept for as long as there is a live business relationship or a reasonable prospect of one, and then for the period required by our record-keeping and tax obligations. Investor qualification records — including name, email and mailing address — are kept for the life of the relationship and for the retention period our counsel advises for records connected to a securities offering.</p>
    <p>You can ask us to delete your information at any time. Where a legal obligation requires us to keep a record, we will tell you which record and why.</p>""")


def privacy():
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(36px,4vw,60px)">
    <p class="eyebrow">Legal</p>
    <h1 style="max-width:16ch">Privacy policy.</h1>
    <p class="lede">Bailiwick Ventures, Inc. collects very little, uses it for one purpose, and does not sell it. This page explains what we hold, why, and how to have it removed.</p>
    <p class="fine" style="margin-top:20px">Last updated August 2026.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">What we collect</p>
      <h2>Only what you send us.</h2>
    </div>
    <div>
      <p class="body">We do not require an account, and there is nothing to sign up for. Information reaches us in three ways.</p>
      <ul class="crit">
        <li><b>The inquiry form.</b> Name, email address, company, title, website, the nature of your inquiry, your company's approximate stage, your description of the situation, what would make a conversation useful, and any document you choose to attach.</li>
        <li><b>Booking a call.</b> If you book time through our scheduling link, that third-party service collects your name, email address and the details you provide, and shares them with us.</li>
        <li><b>Email.</b> Anything you send to an address on this site.</li>
      </ul>
      <p class="body" style="margin-top:22px"><b>Investor qualification.</b> If you ask about co-investment, we record your name, email address and mailing address before sending materials, and we keep a record of what was sent and when. That is deliberate — we do not distribute offering materials anonymously or in bulk.</p>
      {_P1}
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">How we use it</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Three uses, and nothing else.</h2>
    <div class="grid g3">
      <div class="card"><h3>To reply</h3><p style="margin-bottom:0">To respond to your inquiry, arrange a conversation, and follow up on it.</p></div>
      <div class="card"><h3>To qualify</h3><p style="margin-bottom:0">To confirm eligibility before sending investment materials, and to keep a record of what was sent to whom.</p></div>
      <div class="card"><h3>To keep records</h3><p style="margin-bottom:0">To meet our own record-keeping, contractual, tax and regulatory obligations.</p></div>
    </div>
    <div class="gate" style="margin-top:clamp(28px,3.4vw,40px);margin-bottom:0">
      <div class="lbl">What we do not do</div>
      <p>We do not sell your information, and we do not share it for advertising.</p>
      <p class="sub">We do not run advertising networks, we do not build marketing profiles, and we do not add you to a mailing list because you contacted us. If we ever want to send you something you did not ask for, we will ask first.</p>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell split">
    <div>
      <p class="eyebrow">Who else sees it</p>
      <h2>A short list.</h2>
    </div>
    <div>
      <ul class="ticks">
        <li><b>Service providers</b> who operate this site, deliver our email, host our files, and run our scheduling — acting on our instructions only.</li>
        <li><b>Professional advisers</b> — our counsel, accountants, and auditors — where they need it to advise us.</li>
        <li><b>A counterparty</b> in a transaction, where required and under confidentiality.</li>
        <li><b>A regulator, court or authority</b> where the law requires it.</li>
      </ul>
      <p class="body" style="margin-top:20px">Our operating divisions, Bailiwick Venture Studio and BailiwickVibe, are part of Bailiwick Ventures, Inc. and are covered by this policy.</p>
    </div>
  </div>
</section>

<section class="bord on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Your rights</p>
      <h2>Ask, and we will act.</h2>
      <p class="body" style="margin-top:20px">Depending on where you live you may have rights to access, correct, delete, or restrict our use of your information, to receive a copy of it, and to object to certain uses. We honor these requests regardless of where you live.</p>
    </div>
    <div>
      <ul class="ticks">
        <li>Ask what we hold about you.</li>
        <li>Ask us to correct it.</li>
        <li>Ask us to delete it.</li>
        <li>Ask us to stop using it for a particular purpose.</li>
        <li>Ask for a copy in a portable format.</li>
        <li>Withdraw consent where our use rests on consent.</li>
      </ul>
      <p class="body" style="margin-top:20px">Write to <a class="tlink" href="mailto:info@bailiwickventures.com">info@bailiwickventures.com</a> and we will respond. We will not charge you for asking, and we will not treat you differently for having asked.</p>
      <p class="body"><b>California residents:</b> we do not sell or share personal information as those terms are defined by the CCPA, and we have not done so in the preceding twelve months.</p>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Cookies, security, and the rest</p>
    <div class="grid g3" style="margin-top:6px">
      <div><h4 style="margin-bottom:10px">Cookies</h4><p class="body" style="font-size:14.4px">This site sets no advertising or tracking cookies. If we add analytics we will say so here and give you a way to opt out before it runs.</p></div>
      <div><h4 style="margin-bottom:10px">Security</h4><p class="body" style="font-size:14.4px">We use reasonable technical and organizational measures to protect what you send us. No method of transmission over the internet is completely secure, and we will not pretend otherwise.</p></div>
      <div><h4 style="margin-bottom:10px">Children</h4><p class="body" style="font-size:14.4px">This site is intended for business use by adults. We do not knowingly collect information from anyone under 18.</p></div>
      <div><h4 style="margin-bottom:10px">Where data is held</h4><p class="body" style="font-size:14.4px">We operate from the United States, and information you send may be processed there. If you contact us from outside the US, you are sending it to the US.</p></div>
      <div><h4 style="margin-bottom:10px">Links out</h4><p class="body" style="font-size:14.4px">This site links to other sites, including our portfolio companies. Their privacy practices are their own.</p></div>
      <div><h4 style="margin-bottom:10px">Changes</h4><p class="body" style="font-size:14.4px">If we change this policy we will update the date at the top. Material changes will be flagged on this page.</p></div>
    </div>
  </div>
</section>

<section class="on-ink tight">
  <div class="shell">
    <p class="eyebrow">Two things worth stating plainly</p>
    <div class="grid g2">
      <div>
        <h3 style="margin-bottom:12px">We are not a broker-dealer.</h3>
        <p class="body">Bailiwick Ventures, Inc. is not a registered broker-dealer or investment adviser. Nothing on this site is an offer to sell or a solicitation of an offer to buy any security, and nothing here is investment, legal, or tax advice. Any offering is made only through definitive documents furnished to investors who qualify. See the disclosures on the <a href="investing.html" style="color:var(--warm)">Investing</a> page.</p>
      </div>
      <div>
        <h3 style="margin-bottom:12px">Contact</h3>
        <p class="body">Bailiwick Ventures, Inc.<br>
        <a href="mailto:info@bailiwickventures.com" style="color:var(--warm)">info@bailiwickventures.com</a></p>
        <p class="body">Questions about this policy, or a request about your information, should go to that address and will reach a person.</p>
      </div>
    </div>
    <hr class="rule" style="margin:clamp(30px,3.5vw,44px) 0 22px">
    <p class="fine" style="color:#8195A6;max-width:80ch">This policy is written to be read. It is a plain-language business privacy policy covering professional services and private investment activity, and it has not been reviewed by counsel. Have Velawood read it alongside the investor disclosures before launch.</p>
  </div>
</section>
"""


def notfound():
    return """
<div class="hero" style="border-bottom:none">
  <div class="shell hero-in" style="padding-top:clamp(70px,10vw,150px);padding-bottom:clamp(60px,8vw,120px)">
    <div class="split split-even" style="align-items:center">
      <div>
        <p class="eyebrow">Error 404</p>
        <h1 style="max-width:14ch">This page is outside our bailiwick.</h1>
        <p class="lede" style="margin-top:22px">The address you followed does not exist, or it moved. Nothing is broken on your end — the link was pointing somewhere we do not keep anything.</p>
        <div class="btns">
          <a class="btn btn-p" href="index.html">Back to the beginning <span class="arrow">&rarr;</span></a>
          <a class="btn btn-s" href="contact.html">Tell us what you were after <span class="arrow">&rarr;</span></a>
        </div>
      </div>
      <div>
        <svg viewBox="0 0 400 300" fill="none" aria-hidden="true" style="width:100%;max-width:420px;margin:0 auto;opacity:.5">
          <g stroke="#12304F" stroke-width="2" stroke-linecap="round">
            <path d="M40 250 L120 200 M120 200 L200 150"/>
            <path d="M200 150 L280 100" stroke-dasharray="6 9" opacity=".45"/>
            <path d="M120 200 L180 245" opacity=".55"/>
          </g>
          <g fill="#12304F">
            <circle cx="40" cy="250" r="9"/><circle cx="120" cy="200" r="9"/><circle cx="200" cy="150" r="9"/>
            <circle cx="180" cy="245" r="7" opacity=".55"/>
          </g>
          <g stroke="#A8763E" stroke-width="2.4" stroke-linecap="round">
            <path d="M296 84 L328 116 M328 84 L296 116"/>
          </g>
          <text x="200" y="290" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif"
                font-size="11" letter-spacing="2.4" fill="#6B8AA6">THE LAST NODE IS MISSING</text>
        </svg>
      </div>
    </div>
  </div>
</div>

<section class="bord on-warm tight">
  <div class="shell">
    <p class="eyebrow">Try one of these instead</p>
    <div class="grid g4" style="margin-top:6px">
      <a class="card" href="about.html"><h3 style="font-size:19px">About</h3><p style="margin-bottom:0">Who Bailiwick is and how it is structured.</p></a>
      <a class="card" href="investing.html"><h3 style="font-size:19px">Investing</h3><p style="margin-bottom:0">How we invest, and how to co-invest.</p></a>
      <a class="card" href="portfolio.html"><h3 style="font-size:19px">Portfolio</h3><p style="margin-bottom:0">What we own, built, and co-founded.</p></a>
      <a class="card" href="book.html"><h3 style="font-size:19px">The Book</h3><p style="margin-bottom:0"><i>The Certified Enterprise</i>, out November 2026.</p></a>
    </div>
  </div>
</section>
"""


def thanks():
    return """
<div class="hero" style="border-bottom:none">
  <div class="shell hero-in" style="padding-top:clamp(70px,10vw,150px);padding-bottom:clamp(60px,8vw,120px);text-align:center">
    <svg width="58" height="58" viewBox="0 0 64 64" aria-hidden="true" style="margin:0 auto 26px">
      <g stroke="#12304F" stroke-width="3.5" stroke-linecap="round" fill="none">
        <path d="M10 52 L30 38 M30 38 L52 14 M30 38 L50 50"/></g>
      <g fill="#12304F"><circle cx="10" cy="52" r="7"/><circle cx="30" cy="38" r="7"/>
        <circle cx="52" cy="14" r="9"/><circle cx="50" cy="50" r="5.5"/></g>
    </svg>
    <p class="eyebrow">Received</p>
    <h1 style="max-width:18ch;margin:0 auto">Thank you. It reached a person.</h1>
    <p class="lede" style="margin:22px auto 0">Every inquiry is read by Michael, not routed to a queue. You will hear back directly.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="https://calendly.com/michael-atkinson" target="_blank" rel="noopener">Put time on the calendar <span class="arrow">&#8599;</span></a>
      <a class="btn btn-s" href="index.html">Back to the site <span class="arrow">&rarr;</span></a>
    </div>
  </div>
</div>
"""
