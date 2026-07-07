# The Bitcoin Beacon — Folder & Cataloging System

## Folders
- **_system/** — the operating docs: `_bitcoin-beacon-CHARTER.md` (rules), `_bitcoin-beacon-MEMORY.md` (no-repeat ledger), `_bitcoin-beacon-TEMPLATE.html` (issue skeleton), `_bitcoin-beacon-ART-STYLE.md` (house art), `catalog.csv` (the index), this README.
- **issues/** — the daily newsletter editions: `bitcoin-beacon-newspaper-YYYY-MM-DD.html` (+ optional .pdf). These are the EMAIL; they go to beehiiv (not part of the static web root).
- **public/** — THE WEBSITE = the static deploy root (Cloudflare Pages serves this folder):
  - `index.html` (home), `brand-kit.html`
  - `stories/YYYY-MM-DD/slug.html` — article pages grouped by day (7-10/day). Maps 1:1 to that day's issue; mirrors clean URLs (`/stories/2026-07-04/slug`). Date lives in the folder; file is just the slug.
  - `assets/` — logos/images.
- **assets/** — logos and images.
- **archive/** — superseded drafts and one-offs (kept, not deleted).

## Naming conventions
- **Issues: one subfolder per day** — `issues/YYYY-MM-DD/` containing:
  - `bitcoin-beacon-newspaper-YYYY-MM-DD.html` — the designed archival issue (print to PDF from the browser if a PDF is wanted)
  - `bitcoin-beacon-paste-YYYY-MM-DD.html` — the beehiiv paste version (settings box + red line + semantic-only content; copy format EXACTLY from issues/2026-07-06/)
  - `art-YYYY-MM-DD.html` — all of the day's heroes with save links (lead = beehiiv thumbnail)
- **Story:** `public/stories/YYYY-MM-DD/slug.html` — the day-folder holds all 7-10 of that day's stories; the file is just the topic slug (e.g., `nairobi-tando-40m`). The catalog + folder both carry the date.

## The catalog (catalog.csv) — the index of everything
One row per story. Columns:
`date, issue, slug, title, beat, place, tags, sources, url, status`
- **date** — day it ran (YYYY-MM-DD).
- **issue** — the newspaper file it appeared in.
- **slug / url** — the article's filename / path.
- **beat** — section (see vocab below).
- **place** — dateline location.
- **tags** — semicolon-separated topics/entities for search (e.g., `lightning; m-pesa; africa`).
- **sources** — semicolon-separated source domains for that story.
- **status** — draft / published.

Open it in Excel/Sheets to filter by beat, place, tag, or date. To find "everything we've run on Africa," filter `tags` for `africa`; to find a story's day, read the `date` (or the filename).

## Beat vocabulary (keep consistent)
`on-the-ground` · `money-macro` · `markets` · `policy-nation-states` · `network-mining` · `opinion`

## Two ledgers, two jobs
- **MEMORY.md** = prose "have we covered this?" guard (prevents repeats). Read first each day.
- **catalog.csv** = structured, searchable index for retrieval and the website archive/tag pages.
Every new story: append a row to `catalog.csv` AND log it in `MEMORY.md`.

## North star (read this before every decision)
Grow free subscribers until the list supports **paid sponsorships**. Every page, email, and image serves that: every artifact carries a subscribe path (`/subscribe.html`), every page has share-ready OG tags (shares are the growth loop), and the archive + sitemap keep the back catalog indexable (search is the compounding channel). When choosing between options, pick the one that gains or keeps subscribers.

## Daily flow
Read _system docs (**including _bitcoin-beacon-VOICE.md — headline test + mandatory 25% cut pass on all copy**) → gather → filter vs MEMORY (and the 5-day topic cooldown via catalog) → build issue in `issues/` from TEMPLATE → write each story to `public/stories/YYYY-MM-DD/slug.html` **with the head template below** → refresh `public/index.html` with today's stories → **append today's stories to `public/archive.html`** (right beat section, newest first) → **append today's clean URLs to `public/sitemap.xml`** (lastmod = today) → append rows to `catalog.csv` + MEMORY → try beehiiv draft via `save_post` (skip gracefully if plan-gated; tell Matt to paste + send) → present. Newsletter story ↔ website page = 1:1; use the SAME hero image in both.

## Story page head template (REQUIRED on every new page)
Insert directly after the viewport meta. Placeholders: TITLE, DESC (the standfirst, plain text, ~150 chars), DATE (YYYY-MM-DD), SLUG, HERO_URL.

```html
<meta name="description" content="DESC">
<link rel="canonical" href="https://thebitcoinbeacon.com/stories/DATE/SLUG">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#15130f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta property="og:site_name" content="The Bitcoin Beacon">
<meta property="og:type" content="article">
<meta property="og:title" content="TITLE">
<meta property="og:description" content="DESC">
<meta property="og:image" content="HERO_URL">
<meta property="og:url" content="https://thebitcoinbeacon.com/stories/DATE/SLUG">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="TITLE">
<meta name="twitter:description" content="DESC">
<meta name="twitter:image" content="HERO_URL">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"NewsArticle","headline":"TITLE","description":"DESC","image":["HERO_URL"],"datePublished":"DATE","dateModified":"DATE","mainEntityOfPage":"https://thebitcoinbeacon.com/stories/DATE/SLUG","author":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com"},"publisher":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com","logo":{"@type":"ImageObject","url":"https://thebitcoinbeacon.com/assets/bitcoinbeaconlogo.png"}}}</script>
```

Page conventions: **two-tier header** — a `.mast` block (lighthouse badge + "The Bitcoin Beacon" in Fraunces, centered, its own line) ABOVE the sticky `.nav` row (links centered, Subscribe pill right). Copy the `.mast` block, nav block, and the "two-tier masthead" CSS verbatim from any existing story page. Nav links = `/archive.html#on-the-ground|#money-macro|#markets|#network-mining|#opinion|#policy-nation-states`; ALL subscribe CTAs → `/subscribe.html` (opens the site modal); home links = `/` (never `../../index.html`); homepage card images get `loading="lazy" decoding="async" width height`; homepage hero gets `fetchpriority="high"`. Brand mark: the lighthouse linocut badge (job 6100b7c7, `hf_20260706_174039_6100b7c7…_min.webp`) — replaced the plain bitcoin-B on 2026-07-06.

## Site upkeep files (owned by the daily run)
- `public/archive.html` — the full back catalog by beat. Append each new story `<li>` under its beat's `<ul>`, newest first.
- `public/sitemap.xml` — append `<url><loc>https://thebitcoinbeacon.com/stories/DATE/SLUG</loc><lastmod>DATE</lastmod></url>` per story before `</urlset>`.
- `public/subscribe.html` — fallback subscribe page with the beehiiv form embedded inline.
- **Subscribe modal (site-wide):** every page carries a `bb-modal` block before `</body>` (beehiiv form `2c9c948c-bcee-4d82-ad46-d31816c72af4` in an overlay). Clicks on any link to `subscribe.html` or `#subscribe` open the modal instead of navigating — subscribing never leaves the page. NEW story pages MUST include this block — copy it verbatim from any existing story page.
- `public/robots.txt` — has the Sitemap line; don't remove.

## Deploy (AUTOMATIC since 2026-07-07)
`public/` is the web root. Hosting: **Cloudflare Pages** project `bitcoin-beacon`, git-connected to **github.com/zahnbots/bitcoin-beacon** (private), production branch `main`, build command none, build output dir = `public`, serving **thebitcoinbeacon.com** (+ bitcoin-beacon.pages.dev preview). Pipeline: the 6:00 AM daily run edits this folder → a **launchd job at 6:45 AM** (`_system/auto-push.sh` via `~/Library/LaunchAgents/com.bitcoinbeacon.autopush.plist`, log at /tmp/bitcoinbeacon-push.log) commits & pushes → Cloudflare auto-deploys in ~1 min. NO manual deploy step. The daily run itself cannot push (sandbox has no github.com egress) — the launchd job owns that; if a push is needed sooner, run `_system/auto-push.sh` manually or push from GitHub Desktop/Terminal. The old drag-drop Worker project `young-tooth-3a08` is retired (kept as fallback; safe to delete after a few clean days). www.thebitcoinbeacon.com still needs a DNS record + 301 redirect to the apex (one-time fix in the dashboard). Newsletter/subscribers: **beehiiv** (email links point to live `https://thebitcoinbeacon.com/stories/...` URLs; beehiiv write-API is plan-gated on the current plan — issue HTML is drafted locally and pasted, or upgrade the beehiiv plan to unlock `save_post` automation).
