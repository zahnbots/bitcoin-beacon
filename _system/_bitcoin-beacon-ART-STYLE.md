# The Bitcoin Beacon — House Art Style

Every article image uses this ONE look so the site/brief feels cohesive. Fill the [SCENE] and keep everything else identical.

**STYLE CHANGED 2026-07-06:** painterly golden-hour → **three-color linocut / woodcut engraving** ("heritage broadsheet print"). All heroes from this date forward use the linocut formula below. The old painterly formula is retired.

## The formula prompt
> Vintage newspaper editorial illustration in three-color linocut / woodcut engraving style. Scene: [SCENE — a specific place + a specific human action, grounded in the story]. Black carved linework, warm cream, burnt bitcoin-orange as the single dominant spot color, deep forest-green secondary accents, bold crosshatching, visible ink grain, handmade printmaking texture. FULL-BLEED: the carved artwork fills the ENTIRE frame edge to edge — absolutely no paper margin, no border, no frame, no vignette; the scene extends past all four edges of the image. Heritage broadsheet feel, dignified and warm, one clear subject with strong sense of place. No text, no words, no logos, no watermarks.

**FULL-BLEED IS MANDATORY (added 2026-07-06):** never ship art with a paper margin or framed "print block" composition — the art itself fills the image. If a generation comes back with borders, regenerate.

## Locked house look (don't drift)
- **Medium:** three-color linocut / woodcut engraving print (not photoreal, not painterly, not cartoon, not 3D render).
- **Palette:** warm cream paper ground; black carved linework; bitcoin-orange dominant spot color; forest-green secondary. Consistent across every image.
- **Light/mood:** warm and dignified, sun-ray motifs welcome — never grim, never garish.
- **Composition:** one clear subject with a strong sense of place; leave some calm area for a headline to sit over if needed.
- **Always exclude:** text, words, logos, watermarks, brand marks.
- **Representation:** as below — dignity and place-specificity; avoid stereotyped costume shorthand (e.g., no conical-hat clichés).

## Specs & pipeline
- **Hero:** 16:9. **Cards/thumbs:** 1:1 or 4:5. **Social/OG:** 16:9 or 4:5.
- **Engine:** Higgsfield `generate_image`, model `nano_banana_pro` ONLY (never the lite model). Poll the job, take `results.rawUrl`, embed that URL. (For production, re-host on our own domain/beehiiv.)

## CONSISTENCY RULES (this is why it stays on-brand)
1. **One image per story, reused everywhere.** Generate ONE hero for the lead story and use the SAME file in the newsletter (`{{HERO}}` slot), the website article, and social. Never generate separate art for email vs web — that is the #1 cause of "these don't match."
2. **Always pass a STYLE REFERENCE.** Feed a known-good prior hero as a reference so every new hero inherits the established palette and rendering. A prior generation's job id works directly: pass `medias:[{value:<job_id>, role:"image"}]` (or `media_import_url` a URL first). **Canonical reference: the FULL-BLEED Boracay linocut hero, job `af8df1da-3056-46c7-89bd-25320ef638a4`** (rawUrl hf_20260706_212842_af8df1da…png). This is the single most important lever — do not skip it. NOTE: keep the *style* while changing the *scene/place* — never reuse a place that's under the 5-day topic cooldown.
3. **Quality gate — never ship the first weak output.** Generate 2–3 candidates (`count`), pick the strongest, and REGENERATE if: palette drifts off bitcoin-orange/green/cream, there's any text/watermark/garbled hands/faces, it looks 3D-rendered or cartoonish, or it's oversaturated/neon. When unsure, regenerate.
4. **Same brand across formats.** Newsletter and website share: the `the bitcoin beacon` masthead, the orange/green/cream palette, **Fraunces** headlines, the "Vital Stats" module (three fixed metrics), and the SAME hero art. The newsletter keeps its cream "print edition" texture as personality — everything else matches the site. The linocut art doubles down on the print identity.

## Pre-send consistency checklist
- [ ] Correct masthead lockup — `/assets/masthead-ink.png` on light backgrounds, `/assets/masthead-cream.png` on dark. NEVER use the old 'bitcoin brief' files (bitcoinbeaconlogo.png, 'bitcoin beacon no BG', 'Untitled design.png') — retired 2026-07-06.
- [ ] Lead hero present, house-style, and the SAME image on newsletter + web article.
- [ ] Palette = bitcoin-orange + forest-green + cream. Headlines = Fraunces. Art = linocut formula.
- [ ] "Vital Stats" ribbon present with the fixed three metrics (BTC/USD, block height, hashrate).
- [ ] Sources listed. No text/logos baked into any illustration.

## Human/representation notes
- Depict people with dignity and specificity to the place; avoid stereotype or poverty-as-spectacle. The story is bitcoin as an *upgrade*, and the art should feel aspirational and real.

## Reference images already made (this house look — linocut, 2026-07-06)
- **Boracay beachfront payment, FULL-BLEED (CANONICAL style ref): job af8df1da-3056-46c7-89bd-25320ef638a4 / hf_20260706_212842_af8df1da…png**
- India street market, Buenos Aires bank, Bhutan dzong, US treasury, boardroom, Malawi lightbulb (all FULL-BLEED, 2026-07-06): jobs b946aa9b / f967f758 / 545c53b5 / d23f0733 / 1d4c7c48 / 749b6882
- Retired BORDERED linocut set (jobs 76030a7d / e25301ae / 33fdc63e / 7a121914 / 10a45cbb / 1646d7fb / 418724e6) — do NOT use as style refs; they carry paper borders

### Retired painterly references (do NOT use as style refs anymore)
- São Paulo cane-mill mining (hero): hf_20260704_184749…png
- Nairobi/Kibera market payment (hero): hf_20260704_184750…png
