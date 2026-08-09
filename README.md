# bailiwickventures.com

The corporate website for **Bailiwick Ventures, Inc.** — a privately held investment and operating company. Static, self-contained, no build step required to serve.

## Serving

Every page is a standalone HTML file with its CSS, JavaScript, SVG and images inlined. Open `index.html` locally, or serve the repository root. Nothing needs compiling.

Deployed on **Vercel** from this repository's root, on every push to `main`. `CNAME` points the site at bailiwickventures.com; `.nojekyll` is a leftover from the earlier GitHub Pages setup and is harmless.

## Pages

38 pages in total: 16 built from page modules, 22 generated from markdown in `content/`.

| File | Purpose |
|---|---|
| `index.html` | Home |
| `about.html` | About, org structure, the flywheel, Michael |
| `advisory.html` | Strategic advisory |
| `applied-ai.html` | Applied AI & Agent Engineering — client service line |
| `investing.html` | Investment thesis + For Investors (co-investment, SPV, disclosures) |
| `portfolio.html` | Portfolio, holdings, three case studies |
| `studio.html` | Bailiwick Venture Studio |
| `vibe.html` | BailiwickVibe |
| `insights.html` | Themes, public speaking |
| `blog.html` | Blog and archive |
| `book.html` | The Certified Enterprise |
| `pre-order.html` | Book pre-order |
| `contact.html` | Start a Conversation |
| `privacy.html` | Privacy policy |
| `404.html` | Not found |
| `thanks.html` | Form confirmation |

Plus one page per post: 2 site-native essays, 6 Substack essays hosted here as the primary version, and 14 rescued legacy blog posts.

## Rebuilding

The HTML is generated, not hand-edited. Edit the Python in `build/`, then:

```
cd build
python3 build.py            # regenerates every page and sitemap.xml
python3 export_brand.py     # regenerates brand/ from the mark
python3 export_logos.py     # regenerates the logo kit
```

- `build/theme.py` — design system, nav, footer, page shell, and the `mark()` logo function
- `build/pages_a.py` — home, about, advisory
- `build/pages_b.py` — investing, portfolio, studio, vibe, insights, contact
- `build/pages_c.py` — blog, book
- `build/pages_d.py` — privacy, 404, thanks, pre-order
- `build/pages_e.py` — applied AI
- `build/posts.py` — loads and renders everything under `content/`
- `build/flywheel.py` — the flywheel diagram on `about.html`

Requires Python 3.11+ and, for the export scripts, Playwright.

## Content

Markdown sources live in `content/`, and every published page is generated from them:

- `content/essays/` — written for this site
- `content/substack/` — captured verbatim from Substack; hosted here as the primary version with attribution
- `content/blog/` — the 14 rescued legacy posts
- `content/specs/` — internal build specs (not published)
- `content/drafts/` — unpublished material, including endorsement drafts that are **not approved and must not ship**

## Brand

`brand/` holds the Trajectory mark: 15 SVGs and 39 PNGs, a one-color `mono/` set for print and embroidery, and a usage README covering clear space, minimum size and the two optical weights.

Two colors are set in one place, in `mark()` in `theme.py`: the navy `c` default and the `accent` on the terminal node (vermilion, `#E2551F`). Passing `accent=None` returns the one-color mark.

## Open items

- Book endorsements are drafted in `content/drafts/` and unapproved. Nothing appears on the site.
- The contact form needs its one-time FormSubmit confirmation clicked.
- Analytics is not installed.
- The flywheel graphic predates the vermilion decision and still uses bronze for the return arc.

---

© 2026 Bailiwick Ventures, Inc.
