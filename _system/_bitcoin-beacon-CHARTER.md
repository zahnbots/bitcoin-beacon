# The Bitcoin Beacon — CHARTER (rules)

## Mission
A daily micro-newspaper on **Bitcoin's global adoption**. The through-line is *where and how bitcoin is becoming money in the world* — merchants, payments, Lightning, remittances, circular economies, nation-states, energy/mining, and the macro forces that push people toward or away from it. Adoption on the ground leads; Wall Street is a supporting beat, not the spine.

## Business goal
Grow the free subscriber list until it supports **paid sponsorships**. Editorial quality is the product; distribution is the job. Concretely: every page/email carries a subscribe path; headlines and standfirsts are written to be shared; OG/social tags are never skipped; the archive and sitemap stay current so search compounds. Sponsorship readiness later means: consistent daily cadence, verifiable open rates, and a clean niche (bitcoin adoption) — protect all three. Never trade reader trust for short-term growth (no clickbait that the story can't cash).

## Custody Corner (evergreen education — /custody/)
Five vendor-neutral guides + hub. FREE, always — they are the SEO backbone and the future sponsor placement ("Custody Corner presented by X"). Rules: (1) content is written independently; a sponsor buys adjacency, NEVER the conclusions or product mentions; every sponsored placement is labeled; (2) name categories, not products; (3) accuracy bar is highest on the site — custody errors cost readers their savings; when in doubt, be conservative and say "verify independently"; (4) updated QUARTERLY by Matt's ask, not by the daily run — the daily run links to it but does not edit it; (5) direct reader-paid products (premium tier, paid playbook) are a later decision, revisited at ~1,000 subscribers — not before.

## Bitcoin ONLY — hard filter
This is a Bitcoin paper, not a crypto paper. INCLUDE: bitcoin as money/payments, Lightning, bitcoin mining & energy, bitcoin treasuries, bitcoin ETFs/institutions, bitcoin nation-state/policy, bitcoin macro. EXCLUDE: altcoins (ETH/SOL/XRP/etc.), "crypto" exchanges' non-bitcoin business, NFTs, memecoins, stablecoins (unless a development directly moves bitcoin), generic "crypto adoption" stats. If a story is really about the crypto industry rather than bitcoin, drop it. When a source lumps "crypto," extract only the bitcoin-specific fact or cut it.

## Four files (this folder)
- **_bitcoin-beacon-CHARTER.md** — these rules.
- **_bitcoin-beacon-VOICE.md** — how we write: headline test, 25% cut pass, word bans. READ BEFORE WRITING, EVERY DAY.
- **_bitcoin-beacon-MEMORY.md** — ledger of every story already run. READ FIRST, APPEND LAST.
- **_bitcoin-beacon-TEMPLATE.html** — empty skeleton. COPY it and fill placeholders. Never edit/copy a prior edition.

## Daily build sequence
1. Read MEMORY.md fully.
2. Gather TODAY's news, WEIGHTED TO THE GLOBAL SOUTH and on-the-ground adoption. Sources: web search + Matt's X. Adoption accounts/orgs to lean on: Bitcoin Beach, Afribit Africa, Machankura, Gridless, Bitcoin Ekasi, BitcoinKE, TechCabal, Adopting Bitcoin, @DylanLeClair_/@BTCtreasuries/@thebtcpharaoh (treasuries), @MartyBent/TFTC, @parkeralewis. (Build/maintain a dedicated "Adoption" X list over time.)
3. Filter hard against MEMORY.md (no repeats) and the Bitcoin-only filter.
4. `cp _bitcoin-beacon-TEMPLATE.html bitcoin-beacon-newspaper-<YYYY-MM-DD>.html`; fill placeholders; build fresh.
5. Append today's stories to MEMORY.md.
6. Present with a 2–3 sentence summary (concise). Flag anything unverified.

## Rules
1. **No repeated stories, ever.** Check every candidate against MEMORY.md. Only a genuinely new development on an old thread may run, as the new fact.
1a. **5-DAY TOPIC COOLDOWN.** Do not run the same topic/entity/country sooner than every 5 days — no El Salvador, Metaplanet, Strategy, Kenya, etc. two days running. Each day's issue must be built from topics/places/entities NOT used in the previous 4 issues. ENFORCE via catalog.csv: before including a story, check the `place`/`tags` of the last 4 days' rows; if the same topic appears, skip it. ONLY exception: a genuine MATERIAL change that must be addressed to stay current (a new purchase, a law passing, a collapse) — and then frame it as the new development, not a rehash.
1b. **Whole-issue freshness.** Consecutive days should feel completely different — different countries, companies, and beats. Deliberately rotate regions (Africa → LatAm → Asia → Europe → …) and entities so the paper doesn't fixate.
2. **Lead with adoption when it exists.** Prefer an on-the-ground story ("where bitcoin became money today") over a markets story. Give lead + on-the-ground items a **place dateline** (e.g., `NAIROBI —`, `SAN SALVADOR —`).
3. **Sections are conditional.** Include a beat only if it has fresh news. Quiet day = short issue. Beats: On the Ground (adoption) · Money & Macro · Markets & Institutions · Policy & Nation-States · Network & Mining · Voices · The Take.
4. **The main story carries its own POV.** The lead combines reporting AND its analysis/point of view into one piece, ending on a plain "why it matters" line. Do NOT split the day's top story into a separate same-topic opinion box.
4a. **The Take is a DIFFERENT topic than the main story.** Never an opinion re-run of the lead — pick a separate angle.
4b. **"What We're Watching" must be entirely forward-looking items NOT already in the issue.** If a thread was a story today, it's not a "watching" item — that's redundant. Watching = things we haven't covered that we expect to move.
5. **"Vital Stats" (the standing strip).** SAME three metrics every issue — never swap them out. (Renamed from "Adoption at a Glance"; holders and BTC-Map merchants were dropped July 2026.) On the WEBSITE these update live via mempool.space JS (price + block height every 30s; hashrate on load). In the NEWSLETTER (email can't run JS) they are a static "at press time" snapshot. The three metrics, in order:
   - BTC / USD — mempool.space `/api/v1/prices` (`.USD`). Website refreshes every 30s.
   - Block height — mempool.space `/api/blocks/tip/height`. Website refreshes every 30s; also drives the nav "Block" pill.
   - Network hashrate — mempool.space `/api/v1/mining/hashrate/3d` (`currentHashrate` ÷ 1e18 = EH/s). [~945 EH/s mid-2026]
   Newsletter placeholders: {{PRICE}}, {{BLOCK}}, {{HASHRATE}}. (Price is otherwise not a story unless the 24h move is violent.)
6. **Static facts/holdings aren't news;** only material changes. Depth when a story earns its place.
7. **Price is not a story** unless the 24h move is violent (>~8–10% / new ATH / liquidation cascade). Otherwise it's ribbon-only.
8. **One labeled "The Take"** opinion piece per issue, real voice, built from reporting + X.
9. **Curate ruthlessly:** ~5–8 ranked items. Resist completeness.
10. **Formatting matters.** Section subheads must never strand at the foot of a column detached from their text (the template's CSS uses `break-after:avoid` on `.sub` to prevent this — keep it). Read the built file before presenting; if a header is orphaned or a column looks broken, fix it.
11. **ACCURACY IS THE JOB.** Every item must trace to a primary, dated source. Verify names/titles before quoting an official (people leave posts). Built from web + X — treat as a draft that a human reviews before it goes to real readers; never assert what you can't source.
11a. **ALWAYS show your sources.** Whenever a fact or story is flagged as needing verification — or really for any non-obvious claim — provide the actual source link(s) used, so Matt can check them. End every issue (and every full site article) with a "Sources" list of live links behind its claims. Flagging "verify this" without a link is not acceptable.

## Schedule
Daily 6:00 AM local via task `bitcoin-beacon-daily`.
