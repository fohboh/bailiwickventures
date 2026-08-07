# bailiwickventures.com

The corporate website for **Bailiwick Ventures, Inc.** — a privately held investment and
operating company. Static, self-contained, no build step required to serve.

## Serving

Every page is a standalone HTML file with its CSS, JavaScript, SVG and images inlined.
Open `index.html` locally, or serve the repository root. Nothing needs compiling.

Published via GitHub Pages from the repository root. `CNAME` points the site at
`bailiwickventures.com`; `.nojekyll` disables Jekyll processing.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home |
| `about.html` | About, org structure, the team, Michael |
| `advisory.html` | Strategic advisory |
| `investing.html` | Investment thesis + For Investors (co-investment, SPV, disclosures) |
| `portfolio.html` | Portfolio, holdings, case studies |
| `studio.html` | Bailiwick Venture Studio |
| `vibe.html` | BailiwickVibe |
| `insights.html` | Themes, public speaking |
| `blog.html` | Blog and archive |
| `book.html` | *The Certified Enterprise* |
| `contact.html` | Start a Conversation |
| `privacy.html` | Privacy policy |
| `404.html` | Not found |
| `thanks.html` | Form confirmation |

## Rebuilding

The HTML is generated, not hand-edited. Edit the Python in `build/`, then:

```bash
cd build
python3 build.py          # regenerates every page
python3 export_brand.py   # regenerates brand/ from the mark
```

- `build/theme.py` — design system, nav, footer, page shell, and the `mark()` logo function
- `build/pages_a.py` — home, about, advisory
- `build/pages_b.py` — investing, portfolio, studio, vibe, insights, contact
- `build/pages_c.py` — blog, book
- `build/pages_d.py` — privacy, 404, thanks

Requires Python 3.11+ and, for `export_brand.py`, Playwright.

## Brand

`brand/` holds the Trajectory mark: 15 SVGs and 39 PNGs, plus a usage README covering
clear space, minimum size, and the two optical weights. Brand color is set in one place —
the `c` default in `mark()`.

## Before this is considered finished

- Blog posts are titles only; the copy still needs migrating, and the FohBoh Learning
  Center posts still need merging in.
- Three case-study slots on the portfolio page are placeholders.
- Book endorsements are drafted but commented out until approved.
- Calder needs a description.
- The contact form needs its one-time FormSubmit confirmation clicked.
- Analytics is not installed.

© 2026 Bailiwick Ventures, Inc.
