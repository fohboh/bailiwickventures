import base64, os, sys, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme import page
import pages_a as A
import pages_b as B
import pages_c as C
import pages_d as D

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
OUT.mkdir(exist_ok=True)

def datauri(p):
    return "data:image/jpeg;base64," + base64.b64encode((ROOT / p).read_bytes()).decode()

PORTRAIT = datauri("assets/michael-sm.jpg")
PORTRAIT_LG = datauri("assets/michael.jpg")

def datauri_webp(p):
    return "data:image/webp;base64," + base64.b64encode((ROOT / p).read_bytes()).decode()

BOOK_3D = datauri_webp("assets/book-3d.webp")

S = "Bailiwick Ventures, Inc."

PAGES = [
 ("index.html", f"{S} — Capital. Architecture. Execution.",
  "A privately held investment and operating company led by Enterprise Venture Architect Michael L. Atkinson. We build, own, and advise businesses at inflection points.",
  "index.html", A.home(PORTRAIT_LG)),

 ("about.html", f"About — {S}",
  "Bailiwick Ventures is a long-term platform for venture creation and ownership: one parent company, two operating divisions, and clear boundaries between investment, advisory, venture creation, and product engineering.",
  "about.html", A.about(PORTRAIT_LG)),

 ("advisory.html", f"Strategic Advisory — {S}",
  "Michael L. Atkinson advises executives, founders, investors, and private equity firms when the problem crosses traditional functional boundaries.",
  "advisory.html", A.advisory()),

 ("investing.html", f"Investing — {S}",
  "Bailiwick Ventures invests where architecture can change value: the conditions we look for, the sectors we follow, and the ways we participate.",
  "investing.html", B.investing()),

 ("portfolio.html", f"Portfolio & Holdings — {S}",
  "Operating companies, studio-developed ventures, strategic investments, and intellectual property owned or supported through Bailiwick Ventures.",
  "portfolio.html", B.portfolio()),

 ("studio.html", "Bailiwick Venture Studio — Venture Architecture & Development",
  "Bailiwick Venture Studio is the AI-native venture architecture division of Bailiwick Ventures: from consequential idea to usable proof of concept in 60 days or less.",
  "studio.html", B.studio()),

 ("vibe.html", "BailiwickVibe — Production Engineering & Market Entry",
  "BailiwickVibe takes validated prototypes and MVPs through the hard transition to production: engineering, security, scalability, productization, deployment, and go-to-market.",
  "vibe.html", B.vibe()),

 ("insights.html", f"Insights — {S}",
  "Writing on enterprise venture architecture, AI governance, operational intelligence, and the systems that decide whether a company can be trusted with its own data.",
  "insights.html", B.insights()),

 ("contact.html", f"Start a Conversation — {S}",
  "Tell us the situation. Advisory, investment and partnership, Bailiwick Venture Studio, BailiwickVibe, corporate development, speaking and media.",
  "contact.html", B.contact()),

 ("blog.html", f"Blog — {S}",
  "Working notes on trust, architecture, and building companies: shorter and more frequent than the Insights essays.",
  "blog.html", C.blog()),

 ("book.html", "The Certified Enterprise — Michael L. Atkinson",
  "The Certified Enterprise: Taming Data Anarchy in the AI Era. Artificial intelligence is only as reliable as the evidence it consumes.",
  "book.html", C.book(BOOK_3D)),

 ("privacy.html", f"Privacy Policy — {S}",
  "What Bailiwick Ventures collects, why, who else sees it, and how to have it removed. We do not sell your information.",
  "privacy.html", D.privacy()),

 ("404.html", f"Page not found — {S}",
  "That page is outside our bailiwick.",
  "404.html", D.notfound()),

 ("thanks.html", f"Thank you — {S}",
  "Your inquiry reached us.",
  "thanks.html", D.thanks()),
]

for fn, title, desc, active, body in PAGES:
    (OUT / fn).write_text(page(title, desc, active, body), encoding="utf-8")
    print(f"{fn:18} {len((OUT/fn).read_bytes())/1024:7.1f} KB")

print("\nwrote", len(PAGES), "pages to", OUT)
