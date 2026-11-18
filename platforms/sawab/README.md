# Sawab · صواب: math practice studios

Live site: https://sawabmath.pages.dev (Cloudflare Pages project `sawabmath`, Direct Upload).

Four studios, each with a hub, a **Mock exam** and **Guided practice**:

| Studio | Path | Bank | Notes |
|---|---|---|---|
| SAT Aceit | `/sat/` | 2,673 items | Adaptive two-module mock, Desmos, international contexts only |
| SAAT Lab | `/saat/` | 435 guided items | No calculator, Saudi context kept |
| GAT Atelier | `/gat/` | 463 guided items | ETEC blueprint, Saudi context kept |
| AP Precalc Studio | `/ap/` | 413 MCQ, 24 FRQ | All 44 topics of Units 1–3, lessons from the Precalc Book |

## Contents

- `sawab_site.zip`: the full deployable site (as live on 18 Nov 2026). The Desmos API key is replaced by `REPLACE_DESMOS_KEY` in `sat/mock/index.html` and `sat/guided/index.html`; put the real key back before deploying.
- `build/`: build and test scripts.
  - `build_v2.py`: builds the four guided-practice pages and hubs from the mock banks (`DESMOS_API_KEY` environment variable for SAT).
  - `guided.js`, `guided.css`: the guided-practice engine (worked example, hinted "Your turn" twin, independent block, mastery gate at 80%).
  - `desmos_steps.py`: per-question Desmos walkthroughs for SAT (sympy-verified).
  - `twins.py`, `sat_traps.py`: authored twin items (SAAT, GAT, AP) and per-option trap notes.
  - `proctor.js`, `inject_proctor.py`: fullscreen and leave-the-page warnings for the SAAT, GAT and AP mocks.
  - `localize_sat.py`: keeps SAT international (replaces Saudi places, SAR and names in the SAT bank).
  - `polish.py`: injects icons, web-app manifest, share-preview tags and the offline service worker into every page. Run it after every build.
  - `audit.py`, `test_gp.py`, `shots.py`: page audit (desktop and phone), end-to-end guided-practice test, local CDN stubs.
  - `ap/`: AP Precalculus expansion (lessons 1.1–1.7 and 3.1–3.15 from the book, parametric MCQ generators with named traps, figures). `expand.py` writes them into `ap/mock/index.html`.

## Rebuild and deploy

1. Unzip `sawab_site.zip` into `site/`; the scripts expect `/home/claude/v2/site` (edit the paths at the top of each script if needed).
2. `python3 ap/expand.py` (AP data), then `DESMOS_API_KEY=... python3 build_v2.py` (several minutes, SAT is slowest).
3. `python3 polish.py`, then test: serve `site/` on port 8765, run `python3 audit.py` and `python3 test_gp.py`.
4. Zip the whole `site/` folder and upload it in Cloudflare: Workers & Pages › sawabmath › Create deployment. A deployment replaces the whole site, so always upload everything.

## House rules

- SAT and AP Precalculus stay international; SAAT and GAT keep the Saudi context.
- Every wrong option names the trap behind it; all mathematics in LaTeX (KaTeX).
- Guided practice: the worked example and "Your turn" share the same idea and trick.
- No per-topic question counts on the pages.
