"""Turn the rescued legacy blog markdown into site pages.

Reads content/blog/*.md, emits one page per post, and builds the archive list
that blog.html renders.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "blog"

# slug -> (filename stem used on the site, topic tag shown in the archive)
META = {
    "01": ("the-impact-of-data-inconsistency-on-business-performance", "Metrics governance"),
    "02": ("why-ai-is-useless-without-data-integrity", "Restaurant AI"),
    "03": ("the-trust-imperative-metric-governance", "Trust"),
    "04": ("bolt-on-ai-vs-native-ai", "Gen AI"),
    "05": ("why-you-cant-just-connect-your-pos-to-chatgpt", "LLM"),
    "06": ("evaluating-your-restaurants-tech-stack-health", "ResTech"),
    "07": ("restaurant-digital-transformation-data-management", "Data management"),
    "08": ("leveraging-ai-for-workforce-management", "Workforce"),
    "09": ("how-software-companies-master-go-to-market", "GTM"),
    "10": ("technology-in-restaurant-back-of-house", "Operations"),
    "11": ("revolutionizing-inventory-management-in-hospitality", "Inventory"),
    "12": ("ai-driven-procurement-marketplaces", "Procurement"),
    "13": ("the-rising-value-of-voice-technology", "VoiceTech"),
    "14": ("embracing-technology-modern-restaurant-industry", "ResTech"),
}


def _inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               r'<a class="tlink" href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def _blocks(md):
    """Split markdown into (kind, payload) blocks."""
    out, buf, mode = [], [], None

    def flush():
        nonlocal buf, mode
        if buf:
            out.append((mode, buf))
        buf, mode = [], None

    for raw in md.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if re.match(r"^#{1,6}\s", line):
            flush()
            lvl = len(line) - len(line.lstrip("#"))
            out.append(("h", (lvl, line.lstrip("#").strip())))
            continue
        m_ul = re.match(r"^[-*]\s+(.*)", line)
        m_ol = re.match(r"^\d+[.)]\s+(.*)", line)
        if m_ul:
            if mode != "ul":
                flush()
                mode = "ul"
            buf.append(m_ul.group(1))
            continue
        if m_ol:
            if mode != "ol":
                flush()
                mode = "ol"
            buf.append(m_ol.group(1))
            continue
        if mode in ("ul", "ol"):
            buf[-1] += " " + line.strip()
            continue
        if mode != "p":
            flush()
            mode = "p"
        buf.append(line.strip())
    flush()

    # Blank lines between list items split them into separate blocks, which would
    # restart numbering at 1 for every item. Merge adjacent lists of the same kind.
    merged = []
    for kind, payload in out:
        if (merged and kind in ("ul", "ol") and merged[-1][0] == kind):
            merged[-1][1].extend(payload)
        else:
            merged.append((kind, list(payload) if kind in ("ul", "ol", "p") else payload))
    return merged


def _norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def md_to_html(md, title=""):
    parts = []
    tnorm = _norm(title)
    first = True
    for kind, payload in _blocks(md):
        if kind == "h":
            lvl, text = payload
            hn = _norm(text)
            # skip any heading that restates the page title
            if tnorm and (hn == tnorm or hn.startswith(tnorm) or tnorm.startswith(hn)):
                continue
            parts.append(f"<h3>{_inline(text)}</h3>")
        elif kind == "ul":
            items = "".join(f"<li>{_inline(i)}</li>" for i in payload)
            parts.append(f'<ul class="ticks">{items}</ul>')
        elif kind == "ol":
            items = "".join(f"<li>{_inline(i)}</li>" for i in payload)
            parts.append(f'<ol class="ord">{items}</ol>')
        else:
            txt = " ".join(payload)
            bare = txt.strip()
            # a short, fully-bold opening line is the post's standfirst
            if first and len(bare) < 120 and re.fullmatch(r"\*\*.+\*\*|\.\.\..*|[^*]{0,120}", bare) and (
                    bare.startswith("**") or bare.startswith("...")):
                parts.append(f'<p class="lede" style="margin-bottom:26px">{_inline(bare.strip("*"))}</p>')
                first = False
                continue
            parts.append(f'<p class="body">{_inline(txt)}</p>')
        first = False
    return "\n      ".join(parts)


def load():
    """Return a list of post dicts, in numeric order."""
    posts = []
    for f in sorted(SRC.glob("*.md")):
        num = f.name[:2]
        if num not in META:
            continue
        text = f.read_text(encoding="utf-8")
        fm, body = "", text
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if m:
            fm, body = m.group(1), m.group(2)
        title = re.search(r'title:\s*"(.*)"', fm)
        source = re.search(r'source:\s*"(.*)"', fm)
        slug, topic = META[num]
        words = len(body.split())
        posts.append({
            "num": num,
            "slug": slug,
            "topic": topic,
            "title": title.group(1) if title else f.stem,
            "source": source.group(1) if source else "",
            "body": body.strip(),
            "words": words,
            "mins": max(2, round(words / 220)),
        })
    return posts


def page_body(p):
    article = md_to_html(p["body"], p["title"])
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(30px,3.4vw,48px)">
    <p class="eyebrow">Blog &middot; {html.escape(p['topic'])}</p>
    <h1 style="max-width:20ch">{html.escape(p['title'])}</h1>
    <p class="fine" style="margin-top:22px">By Michael L. Atkinson &middot; {p['mins']} min read</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <div class="article">
      {article}
    </div>
  </div>
</section>

<section class="on-ink tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Keep reading.</h2>
    <p class="body" style="margin:18px auto 0;max-width:54ch">More on trust, architecture, and the systems that decide whether a company can rely on its own numbers.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-g" href="blog.html">All posts <span class="arrow">&rarr;</span></a>
      <a class="btn btn-g" href="book.html">The Book <span class="arrow">&rarr;</span></a>
      <a class="btn btn-g" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Substack <span class="arrow">&#8599;</span></a>
    </div>
  </div>
</section>
"""


def archive_html(posts):
    rows = []
    for p in posts:
        rows.append(
            f'<a href="{p["slug"]}.html"><span class="t">{html.escape(p["title"])}</span>'
            f'<span class="tg">{html.escape(p["topic"])} &rarr;</span></a>')
    return "\n        ".join(rows)


# --- Substack essays, hosted here as the primary version -------------------
SUB_SRC = ROOT / "content" / "substack"

SUB_META = {
    "s01": ("systems-of-record-were-never-designed-to-certify-truth", "Independence"),
    "s02": ("your-ai-isnt-wrong-your-data-is", "Enterprise AI"),
    "s03": ("the-trust-crisis-in-enterprise-ai", "Trust"),
    "s04": ("the-intelligent-enterprise-is-a-certified-enterprise", "Governance"),
    "s05": ("the-invisible-force-behind-every-technology-revolution", "Technology"),
    "s06": ("in-data-we-trust", "Metrics governance"),
}


def load_sub():
    out = []
    for f in sorted(SUB_SRC.glob("*.md")):
        key = f.name[:3]
        if key not in SUB_META:
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        fm, body = (m.group(1), m.group(2)) if m else ("", text)

        def field(name):
            g = re.search(rf'{name}:\s*"(.*)"', fm)
            return g.group(1) if g else ""

        slug, topic = SUB_META[key]
        words = len(body.split())
        out.append({
            "key": key, "slug": slug, "topic": topic,
            "title": field("title"), "subtitle": field("subtitle"),
            "date": field("date"), "source": field("source"),
            "series": field("series"),
            "body": body.strip(), "words": words,
            "mins": max(2, round(words / 220)),
        })
    return out


def sub_page_body(p):
    article = md_to_html(p["body"], p["title"])
    banner = mark_banner() if p.get("banner") else ""
    attribution = ""
    if p.get("source"):
        attribution = (
            '<hr class="rule" style="margin:clamp(34px,4vw,50px) 0 20px">'
            f'<p class="fine" style="margin-bottom:0">First published on Substack on '
            f'{html.escape(p["date"])}. <a class="tlink" href="{p["source"]}" target="_blank" '
            f'rel="noopener">Read the original <span class="arrow">&#8599;</span></a> &middot; '
            '<a class="tlink" href="https://substack.com/@michaellatkinson1" target="_blank" '
            'rel="noopener">Subscribe <span class="arrow">&#8599;</span></a></p>')
    sub = (f'<p class="lede" style="margin-top:18px">{html.escape(p["subtitle"])}</p>'
           if p["subtitle"] else "")
    series = (f'<p class="fine" style="margin-top:16px;margin-bottom:0">{html.escape(p["series"])}</p>'
              if p["series"] else "")
    return f"""
<div class="hero">
  <div class="shell hero-in" style="padding-bottom:clamp(30px,3.4vw,48px)">
    <p class="eyebrow">Blog &middot; {html.escape(p['topic'])}</p>
    <h1 style="max-width:22ch">{html.escape(p['title'])}</h1>
    {sub}
    <p class="fine" style="margin-top:22px">By Michael L. Atkinson &middot; {html.escape(p['date'])} &middot; {p['mins']} min read</p>
    {series}
  </div>
</div>

<section class="on-warm">
  <div class="shell">
    <div class="article">
      {banner}{article}
      {attribution}
    </div>
  </div>
</section>

<section class="on-ink tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Keep reading.</h2>
    <p class="body" style="margin:18px auto 0;max-width:54ch">More on trust, architecture, and the systems that decide whether a company can rely on its own numbers.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-g" href="blog.html">All posts <span class="arrow">&rarr;</span></a>
      <a class="btn btn-g" href="book.html">The Book <span class="arrow">&rarr;</span></a>
      <a class="btn btn-g" href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener">Substack <span class="arrow">&#8599;</span></a>
    </div>
  </div>
</section>
"""


def sub_cards(posts):
    cards = []
    for i, p in enumerate(posts):        # s01 is the newest
        span = ' style="grid-column:span 2"' if i == 0 else ''
        size = ' style="font-size:clamp(22px,2.4vw,29px)"' if i == 0 else ''
        dek = html.escape(p["subtitle"] or p["title"])
        cards.append(f"""<a class="card post" href="{p['slug']}.html"{span}>
        <div class="kicker">Essay &middot; {html.escape(p['topic'])}</div>
        <h3{size}>{html.escape(p['title'])}</h3>
        <p>{dek}</p>
        <div class="postmeta">
          <span class="pdate">{html.escape(p['date'])}</span>
          <span class="pdate">{p['mins']} min read</span>
        </div>
      </a>""")
    return "\n      ".join(cards)


# --- Essays written for this site (no Substack origin) ---------------------
NATIVE_SRC = ROOT / "content" / "essays"

NATIVE_META = {
    "n01": ("one-node-is-vermilion", "Brand & method"),
    "n02": ("we-dont-build-one-big-agent", "Applied AI"),
}

# The mark, drawn large, as the article's header image.
def mark_banner():
    from theme import LINKS, NODES, VERMILION
    navy = "#12304F"
    r = (7.0, 7.0, 9.0, 5.5)
    circles = "".join(
        f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{VERMILION if i == 2 else navy}"/>'
        for i, ((x, y), rr) in enumerate(zip(NODES, r)))
    return (
        '<div style="background:var(--warm);border:1px solid var(--line);border-radius:3px;'
        'padding:clamp(44px,6vw,86px);display:flex;justify-content:center;'
        'margin-bottom:clamp(30px,3.6vw,46px)">'
        '<svg width="180" height="180" viewBox="0 0 64 64" role="img" '
        'aria-label="The Bailiwick mark: four nodes climbing left to right with one branch. '
        'The oversized terminal node is vermilion; everything else is navy.">'
        f'<g stroke="{navy}" stroke-width="3.5" stroke-linecap="round" fill="none">'
        f'<path d="{LINKS}"/></g>{circles}</svg></div>')


def load_native():
    out = []
    for f in sorted(NATIVE_SRC.glob("*.md")):
        key = f.name[:3]
        if key not in NATIVE_META:
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        fm, body = (m.group(1), m.group(2)) if m else ("", text)

        def field(name):
            g = re.search(rf'{name}:\s*"(.*)"', fm)
            return g.group(1) if g else ""

        slug, topic = NATIVE_META[key]
        words = len(body.split())
        out.append({
            "key": key, "slug": slug, "topic": topic,
            "title": field("title"), "subtitle": field("subtitle"),
            "date": field("date"), "source": "", "series": "",
            "body": body.strip(), "words": words,
            "mins": max(2, round(words / 220)), "banner": key == "n01",
        })
    return list(reversed(out))   # newest first
