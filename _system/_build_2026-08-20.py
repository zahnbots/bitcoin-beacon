# -*- coding: utf-8 -*-
import os
BASE = "/sessions/jolly-eloquent-lovelace/mnt/bitcoin beacon/public/stories/2026-08-20"
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"

HEAD_CSS = """<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&display=swap');
  :root{ --ink:#15130f; --muted:#6b6459; --line:#e7e3da; --accent:#e8820c; --paper:#ffffff; --wash:#faf7f1; }
  *{ box-sizing:border-box; }
  body{ margin:0; background:var(--paper); color:var(--ink); font-family:'Inter',system-ui,Arial,sans-serif; line-height:1.6; }
  a{ color:inherit; text-decoration:none; }
  .nav{ position:sticky; top:0; z-index:20; background:rgba(255,255,255,.94); backdrop-filter:blur(6px); border-bottom:1px solid var(--line); }
  .nav .in{ max-width:1120px; margin:0 auto; display:flex; align-items:center; gap:26px; padding:12px 24px; }
  .nav img{ height:56px; }
  .nav .links{ display:flex; gap:20px; font-size:13px; font-weight:600; color:#4a463f; margin-left:6px; }
  .nav .links a:hover{ color:var(--accent); }
  .nav .sub{ background:var(--ink); color:#fff; font-size:12px; font-weight:700; padding:9px 15px; border-radius:999px; }
  .nav .menu-btn{ display:none; background:none; border:0; font-size:22px; line-height:1; cursor:pointer; color:var(--ink); padding:4px 8px; -webkit-tap-highlight-color:transparent; }
  .wrap{ max-width:720px; margin:0 auto; padding:0 24px; }
  .crumb{ max-width:720px; margin:26px auto 0; padding:0 24px; }
  .tag{ display:inline-block; font-size:11px; font-weight:800; letter-spacing:1.4px; text-transform:uppercase; color:#8a5a12; }
  h1.title{ font-family:'Fraunces',Georgia,serif; font-weight:700; font-size:44px; line-height:1.08; letter-spacing:-.5px; margin:10px 0 14px; }
  .standfirst{ font-size:20px; line-height:1.5; color:#3b382f; font-family:'Fraunces',Georgia,serif; font-style:italic; margin:0 0 20px; }
  .meta{ display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; font-size:13px; color:var(--muted); border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:12px 0; margin-bottom:24px; }
  .meta b{ color:var(--ink); font-weight:700; }
  .hero{ max-width:1000px; margin:0 auto 28px; padding:0 24px; }
  .heroart{ height:360px; border-radius:14px; position:relative; overflow:hidden; background:#111; }
  .heroart img{ width:100%; height:100%; object-fit:cover; display:block; }
  .heroart .cap{ position:absolute; left:0; bottom:0; width:100%; padding:14px 18px; font-size:12px; color:#fff; background:linear-gradient(transparent,rgba(0,0,0,.55)); }
  .body{ font-size:18px; }
  .body p{ margin:0 0 18px; }
  .body h2{ font-family:'Fraunces',Georgia,serif; font-size:26px; font-weight:700; margin:34px 0 10px; letter-spacing:-.3px; }
  .body .drop::first-letter{ float:left; font-family:'Fraunces',serif; font-weight:700; font-size:64px; line-height:50px; padding:6px 10px 0 0; color:var(--accent); }
  .pull{ font-family:'Fraunces',Georgia,serif; font-size:26px; line-height:1.3; font-weight:500; color:var(--ink); border-left:4px solid var(--accent); padding:6px 0 6px 20px; margin:26px 0; }
  .sources{ background:var(--wash); border:1px solid var(--line); border-radius:12px; padding:16px 20px; margin:26px 0; font-size:14px; }
  .sources h4{ margin:0 0 8px; font-size:12px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted); }
  .sources ol{ margin:0; padding-left:20px; } .sources li{ margin-bottom:6px; }
  .sources a{ color:var(--accent); text-decoration:underline; word-break:break-word; }
  .note{ font-size:12.5px; color:var(--muted); font-style:italic; border-top:1px solid var(--line); padding-top:14px; margin-top:24px; }
  .subscribe{ max-width:1120px; margin:34px auto; padding:26px 24px; text-align:center; }
  .subscribe .box{ background:var(--ink); color:#fff; border-radius:16px; padding:30px 24px; }
  .subscribe h3{ font-family:'Fraunces',serif; font-size:24px; margin:0 0 8px; }
  .subscribe p{ color:#c9c3b8; margin:0 0 16px; font-size:15px; }
  .subscribe .btn{ display:inline-block; background:var(--accent); color:#fff; font-weight:700; padding:12px 22px; border-radius:999px; font-size:14px; }
  footer{ border-top:1px solid var(--line); padding:26px 24px; text-align:center; color:var(--muted); font-size:12px; }
  @media(max-width:720px){ h1.title{ font-size:32px; } }
  @media(max-width:768px){
    html,body{ max-width:100%; overflow-x:hidden; }
    .nav .in{ flex-wrap:nowrap; gap:8px 10px; padding:10px 14px; }
    .nav .menu-btn{ display:inline-flex; align-items:center; }
    .nav img{ height:34px; }
    .nav .links{ display:none; }
    .nav .sub{ margin-left:auto; padding:8px 12px; white-space:nowrap; }
    .crumb{ margin-top:20px; padding:0 16px; }
    .wrap{ padding:0 16px; }
    h1.title{ font-size:27px; }
    .standfirst{ font-size:17px; }
    .hero{ padding:0 16px; margin-bottom:22px; }
    .heroart{ height:210px; }
    .body{ font-size:16px; }
    .body h2{ font-size:22px; }
    .pull{ font-size:21px; }
  }
  .mast{ background:var(--paper); border-bottom:1px solid var(--line); }
  .mast a{ display:flex; align-items:center; justify-content:center; gap:18px; padding:20px 24px 16px; }
  .mast img{ height:119px; width:119px; border-radius:50%; }
  .mast span{ font-family:'Fraunces',Georgia,serif; font-weight:700; font-size:42px; letter-spacing:-.5px; color:var(--ink); }
  .nav .in{ position:relative; justify-content:center; }
  .nav .sub{ position:absolute; right:24px; top:50%; transform:translateY(-50%); margin-left:0; }
  .nav .menu-btn{ position:absolute; left:14px; top:50%; transform:translateY(-50%); }
  @media(max-width:768px){
    .mast a{ gap:12px; padding:18px 14px 12px; }
    .mast img{ height:64px; width:64px; }
    .mast span{ font-size:24px; letter-spacing:-.3px; }
    .nav{ position:static !important; background:var(--paper) !important; backdrop-filter:none !important; }
    .nav .in{ flex-direction:column !important; align-items:center; padding:12px 14px 16px !important; gap:0 !important; }
    .nav .links{ display:flex !important; flex-direction:row !important; flex-wrap:wrap !important; justify-content:center; overflow:visible !important; gap:9px 18px; padding:0 !important; margin:0; width:100%; font-size:13.5px; position:static !important; box-shadow:none !important; background:transparent !important; border:0 !important; }
    .nav .links a{ white-space:nowrap; border-top:0 !important; padding:0 !important; font-size:13.5px !important; }
    .nav .sub{ display:inline-block !important; position:static !important; transform:none !important; margin:14px auto 0 !important; padding:9px 26px; box-shadow:none !important; font-size:13px; }
    .nav .menu-btn{ display:none !important; }
  }
</style>"""

NAV = """  <div class="mast"><a href="/">
    <img src="/assets/beacon-badge-400.png" alt="The Bitcoin Beacon" width="400" height="400">
    <span>The Bitcoin Beacon</span>
  </a></div>
  <div class="nav"><div class="in">
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    <div class="links"><a href="/archive/on-the-ground.html">On the Ground</a><a href="/archive/money-macro.html">Money &amp; Macro</a><a href="/archive/markets.html">Markets</a><a href="/archive/network-mining.html">Network &amp; Mining</a><a href="/archive/opinion.html">Opinion</a><a href="/archive/policy-nation-states.html">Nation-States</a><a href="/archive.html">Archive</a><a href="/custody/">Custody</a></div>
    <a class="sub" href="#subscribe">Subscribe</a>
  </div></div>
  <script>
  (function(){var b=document.querySelector('.nav .menu-btn');if(b){b.addEventListener('click',function(){var n=b.closest('.nav');var open=n.classList.toggle('open');b.setAttribute('aria-expanded',open?'true':'false');});}})();
  </script>"""

MODAL = """<!-- subscribe modal (site-wide) -->
<style>
.bb-modal{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;background:rgba(21,19,15,.62);padding:20px;}
.bb-modal.open{display:flex;}
.bb-modal .bb-card{background:#faf7f1;border-radius:16px;max-width:620px;width:100%;padding:16px 16px 8px;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.35);}
.bb-modal .bb-x{position:absolute;top:6px;right:12px;background:none;border:0;font-size:28px;color:#6b6459;cursor:pointer;line-height:1;}
.bb-modal iframe{width:100%;height:340px;border:0;border-radius:10px;background:#fff;}
</style>
<div class="bb-modal" id="bb-modal" role="dialog" aria-modal="true" aria-label="Subscribe to The Bitcoin Beacon">
  <div class="bb-card">
    <button class="bb-x" aria-label="Close">&times;</button>
    <iframe data-src="https://subscribe-forms.beehiiv.com/2c9c948c-bcee-4d82-ad46-d31816c72af4" title="Subscribe to The Bitcoin Beacon"></iframe>
  </div>
</div>
<script>
(function(){
  var m=document.getElementById('bb-modal');if(!m)return;
  var f=m.querySelector('iframe');
  function open(e){if(e)e.preventDefault();if(!f.src)f.src=f.getAttribute('data-src');m.classList.add('open');document.body.style.overflow='hidden';}
  function close(){m.classList.remove('open');document.body.style.overflow='';}
  document.addEventListener('click',function(e){
    var a=e.target.closest('a');if(!a)return;
    var h=a.getAttribute('href')||'';
    if(/subscribe\\.html$/.test(h)||h==='#subscribe'){open(e);}
  });
  m.addEventListener('click',function(e){if(e.target===m)close();});
  m.querySelector('.bb-x').addEventListener('click',close);
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();
</script>"""

def page(slug, title, desc, tagcolor, beatlabel, place, readmin, hero, cap, body, sources, note):
    src = "\n".join('        <li>%s</li>' % s for s in sources)
    url = "https://thebitcoinbeacon.com/stories/2026-08-20/" + slug
    img = CF + hero
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#15130f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta property="og:site_name" content="The Bitcoin Beacon">
<meta property="og:type" content="article">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(img)s">
<meta property="og:url" content="%(url)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(img)s">
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "NewsArticle", "headline": "%(title)s", "description": "%(desc)s", "image": ["%(img)s"], "datePublished": "2026-08-20", "dateModified": "2026-08-20", "mainEntityOfPage": "%(url)s", "author": {"@type": "Organization", "name": "The Bitcoin Beacon", "url": "https://thebitcoinbeacon.com"}, "publisher": {"@type": "Organization", "name": "The Bitcoin Beacon", "url": "https://thebitcoinbeacon.com", "logo": {"@type": "ImageObject", "url": "https://thebitcoinbeacon.com/assets/masthead-ink.png"}}}</script>
<title>%(title)s &mdash; The Bitcoin Beacon</title>
%(css)s
</head>
<body>
%(nav)s

  <div class="crumb"><span class="tag" style="color:%(tagcolor)s;">%(beatlabel)s &middot; %(place)s</span></div>
  <div class="wrap">
    <h1 class="title">%(title)s</h1>
    <p class="standfirst">%(standfirst)s</p>
    <div class="meta"><b>By The Bitcoin Beacon</b> &middot; %(placeuc)s &middot; August 20, 2026 &middot; %(readmin)s min read</div>
  </div>
  <div class="hero"><div class="heroart">
    <img src="%(img)s" alt="%(cap)s">
    <div class="cap">%(beatlabel)s &middot; %(cap)s &middot; Illustration: The Bitcoin Beacon</div>
  </div></div>
  <div class="wrap body">

%(body)s

    <div class="sources">
      <h4>Sources</h4>
      <ol>
%(src)s
      </ol>
    </div>
    <p class="note">%(note)s</p>
  </div>
  <div class="subscribe" id="subscribe"><div class="box">
    <h3>The world&rsquo;s bitcoin headlines, in your inbox every morning.</h3>
    <p>Free. Five minutes. No hype.</p>
    <a class="btn" href="/subscribe.html">Subscribe free</a>
  </div></div>

  <footer>THE BITCOIN BEACON &bull; The daily record of Bitcoin's global adoption &bull; Informational only &mdash; not financial advice</footer>

%(modal)s

</body>
</html>
""" % dict(desc=desc, url=url, title=title, img=img, css=HEAD_CSS, nav=NAV, tagcolor=tagcolor,
           beatlabel=beatlabel, place=place, placeuc=place.upper(), standfirst=STANDFIRST[slug],
           readmin=readmin, cap=cap, body=body, src=src, note=note, modal=MODAL)

STANDFIRST = {}

# ---------- Story 2: El Salvador ----------
STANDFIRST["el-salvador-bitcoin-law-five-years"] = "Five years after making bitcoin legal tender, President Nayib Bukele concedes the everyday adoption never came. What is left is a state reserve &mdash; and a lesson."
es_body = """<p class="drop">El Salvador&rsquo;s bet has aged into an admission. Five years after San Salvador became the first government on earth to make bitcoin legal tender, President Nayib Bukele told <em>Time</em> in August that &ldquo;bitcoin did not receive the widespread adoption we expected.&rdquo; It is a striking line from the leader who once put laser eyes on his profile picture and turned a Salvadoran beach town into a global bitcoin pilgrimage.</p>

<p>The numbers behind the concession are blunt. Cryptocurrency settled just <strong>$35.4 million</strong> of the more than <strong>$5 billion</strong> in remittances Salvadorans received in the first half of 2026 &mdash; well under 1% of the flow that keeps many households afloat. Remittances are the use case bitcoin was supposed to transform here, and after five years the transformation is a rounding error.</p>

<h2>From mandate to retreat</h2>
<p>The framework itself has already been walked back. In January 2025, as a condition of a <strong>$1.4 billion</strong> IMF financing package, the government stripped bitcoin of its mandatory legal-tender status. Businesses are no longer required to accept it, taxes must be paid in U.S. dollars, and the state-issued Chivo wallet &mdash; once the on-ramp for millions &mdash; is being wound down. The public sector&rsquo;s direct involvement has been pared back to satisfy the fund.</p>

<p>What survives is the treasury. El Salvador still holds roughly <strong>7,677 BTC</strong>, worth about $480 million after this month&rsquo;s rally, and has kept adding coins even as the consumer program faded. The experiment that began as &ldquo;bitcoin as everyday money&rdquo; has quietly become &ldquo;bitcoin as sovereign reserve asset&rdquo; &mdash; a very different, and far more modest, proposition.</p>

<div class="pull">A government can make a currency legal. It cannot make people prefer it.</div>

<h2>What the experiment actually proved</h2>
<p>The uncharitable reading is that a top-down mandate failed. The fairer one is that it was always the wrong instrument. Legal-tender status compelled merchants to accept bitcoin; it could not manufacture a reason for anyone to spend it when the dollar already circulates freely and most prices are dollar-denominated. Where bitcoin has taken root in El Salvador &mdash; the El Zonte &ldquo;Bitcoin Beach&rdquo; circular economy &mdash; it did so through grassroots education and tourism that predated the 2021 law, not because of it.</p>

<p>Defenders point to what the law seeded regardless: a national bitcoin-education curriculum, tourism and investment attention out of proportion to the country&rsquo;s size, and a reserve now sitting on large paper gains. Those are real. But they are the by-products of a symbolic gamble, not evidence that a decree can bootstrap a currency into daily use.</p>

<p><em>Why it matters: the first country to legislate bitcoin into money has spent five years learning that adoption follows utility, not statute &mdash; a caution for every state now drafting its own bitcoin law.</em></p>"""
es_sources = [
 'news.bitcoin.com &mdash; <a href="https://news.bitcoin.com/5-years-after-the-bitcoin-law-crypto-accounts-for-just-0-7-of-el-salvadors-5b-remittance-market/">Crypto is 0.7% of El Salvador&rsquo;s $5B remittance market (2026)</a>',
 'Bitcoin Magazine &mdash; <a href="https://bitcoinmagazine.com/news/five-years-on-el-salvador-bitcoin">Five Years On, El Salvador Is Still Buying Bitcoin</a>',
 'The Currency Analytics &mdash; <a href="https://thecurrencyanalytics.com/bitcoin/el-salvadors-bitcoin-law-hits-five-years-with-1-remittance-use-and-an-imf-deal-283565">Bitcoin Law Hits Five Years With ~1% Remittance Use and an IMF Deal</a>',
 'Crypto Briefing &mdash; <a href="https://cryptobriefing.com/el-salvador-five-years-bitcoin-legal-tender/">El Salvador reflects on five years of bitcoin as legal tender</a>',
]
es_note = "Figures as reported at the five-year anniversary of El Salvador&rsquo;s Bitcoin Law; reserve size approximate and rising. Informational only &mdash; not financial advice."

# ---------- Story 3: Zhibao ----------
STANDFIRST["zhibao-shanghai-bitcoin-treasury"] = "A Nasdaq-listed insurance broker from a country that bans crypto trading just built a 2,380-coin treasury, importing the Saylor playbook into Chinese finance."
zh_body = """<p class="drop">A Shanghai company just did something that is technically illegal to do in Shanghai. Zhibao Technology, a digital insurance broker based in mainland China, closed a <strong>$154.7 million</strong> private placement funded in bitcoin and now holds a treasury of <strong>2,380 BTC</strong> &mdash; enough to make it the 33rd-largest corporate bitcoin holder in the world, ahead of established names like Core Scientific.</p>

<p>The mechanism is the workaround. China has banned domestic cryptocurrency trading and mining since 2021. Zhibao, however, is listed on the Nasdaq, and the placement was structured through that U.S.-listed entity rather than its mainland operations. The coins sit on a public American exchange&rsquo;s books, one step removed from Beijing&rsquo;s prohibition, funded by investors who paid in bitcoin rather than cash.</p>

<h2>The Saylor template goes global</h2>
<p>The move is the latest export of a playbook written in Virginia. Strategy &mdash; formerly MicroStrategy &mdash; pioneered the idea of a public company turning its balance sheet into a bitcoin-accumulation vehicle, and now holds roughly <strong>844,000 BTC</strong>. Public companies collectively hold more than <strong>1.26 million BTC</strong>, over 6% of the 21 million that will ever exist. Japan&rsquo;s Metaplanet, Europe&rsquo;s H100 Group, and now a Chinese insurance broker have each localized the same structure: raise capital, buy bitcoin, let the treasury become the story.</p>

<div class="pull">The ban stops the trade at home. It does not stop the balance sheet abroad.</div>

<h2>Why it is more than a novelty</h2>
<p>For a Chinese-linked firm, a bitcoin treasury is a statement about where value can be parked outside the reach of domestic capital controls and a depreciating property market. It is also a bet that a Nasdaq listing offers enough regulatory distance to hold the asset safely. That distance is the risk. A treasury built by a mainland-operating company through an offshore shell invites scrutiny from regulators on both sides, and the whole model rides on bitcoin&rsquo;s price staying above the effective cost of the placement.</p>

<p>Like every treasury company, Zhibao now trades partly as a leveraged bet on bitcoin, its shares carrying a premium or discount to the coins it holds. What makes this one notable is the flag on the door. When a firm from the country that outlawed crypto trading becomes a top-35 corporate holder, the treasury model has reached a place its architects probably never mapped.</p>

<p><em>Why it matters: capital finds bitcoin even where the law forbids the trade &mdash; and the corporate-treasury structure is now the vehicle carrying it across borders.</em></p>"""
zh_sources = [
 'Benzinga &mdash; <a href="https://www.benzinga.com/crypto/cryptocurrency/26/08/61292288/nasdaq-chinese-company-bitcoin-treasury-michael-saylor">Nasdaq-Listed Chinese Company Launches $154.7M Bitcoin Treasury</a>',
 'BitcoinTreasuries.NET &mdash; <a href="https://bitcointreasuries.net/">Corporate bitcoin holdings tracker</a>',
 'Bitcoin.com &mdash; <a href="https://www.bitcoin.com/get-started/bitcoin/buying-spending/what-is-a-bitcoin-corporate-treasury/">What is a bitcoin corporate treasury?</a>',
]
zh_note = "Placement and holding figures as reported Aug. 18&ndash;19, 2026. Corporate-treasury totals are approximate and change with new filings. Informational only &mdash; not financial advice."

# ---------- Story 4: Core v32 ----------
STANDFIRST["bitcoin-core-v32-feature-freeze"] = "Bitcoin&rsquo;s reference software stops adding features today, freezing version 32 for a release that reaches users this fall &mdash; a quiet ritual that shows how the network actually changes."
core_body = """<p class="drop">Bitcoin does not have a CEO, a boardroom, or a roadmap anyone can dictate. What it has instead is a release schedule, and today one of its most important dates arrives: <strong>Bitcoin Core version 32 hits its feature freeze</strong>. From this point, no new features go into the release. Maintainers switch to fixing bugs, polishing, and preparing a version the world&rsquo;s bitcoin nodes can run.</p>

<p>The calendar from here is deliberate. Developers split off the 32.x branch, aim to publish a first release candidate (v32.0rc1) around <strong>September 10</strong>, and target a final v32.0 build near <strong>October 10</strong>. Any feature that missed today&rsquo;s cutoff waits for version 33. Critical bug fixes can still land during the run-up to the release candidate; new functionality cannot.</p>

<h2>Governance by tedium</h2>
<p>Bitcoin Core is the dominant implementation of the software that enforces bitcoin&rsquo;s rules, but it is not the network&rsquo;s owner. Nobody is obliged to upgrade. A release becomes real only when node operators and businesses choose to run it, and consensus rules change only when a broad supermajority adopts the same code. That is why the process looks so bureaucratic: it is designed to make change slow, reviewed, and hard to force.</p>

<p>As of mid-August, the v32 milestone showed roughly <strong>17 items open and 79 closed</strong> &mdash; about 82% complete. A couple of pending changes still needed rebasing against the latest code, and a descriptor-wallet fix was targeting an access bug caused by an identifier mismatch. A proposal to allow opt-in unencrypted connections between nodes hit merge conflicts and rebase friction in the final stretch, the kind of unglamorous engineering that determines what ships.</p>

<div class="pull">The point of the freeze is friction: no single hand decides what bitcoin becomes.</div>

<h2>Why a routine release is worth watching</h2>
<p>The conservatism is the feature. Bitcoin secures hundreds of billions of dollars, so its maintainers optimize for not breaking things over shipping fast. Critics argue that Core&rsquo;s dominance is itself a centralizing force &mdash; a debate that has fueled interest in alternative clients like Bitcoin Knots &mdash; but the freeze-and-release cadence is public, auditable, and slow by design. Anyone can read the milestone, the pull requests, and the review comments.</p>

<p>For users, nothing changes the moment the code freezes. The practical questions come later: which features slipped to v33, whether the release candidate surfaces regressions, and how quickly operators upgrade once v32.0 ships in the fall. Watch September 10 for the release candidate &mdash; that is when the theory meets the network.</p>

<p><em>Why it matters: bitcoin changes through a deliberately dull, decentralized process, and the v32 freeze is that process working exactly as intended.</em></p>"""
core_sources = [
 'CryptoSlate &mdash; <a href="https://cryptoslate.com/merge-conflicts-and-unencrypted-traffic-risks-loom-as-bitcoin-core-prepares-to-lock-down-new-node-features-on-thursday/">Bitcoin Core feature freeze nears as rebase issues hit proposal</a>',
 'GitHub &mdash; <a href="https://github.com/bitcoin/bitcoin/issues/35122">Release Schedule for 32.0 (bitcoin/bitcoin #35122)</a>',
 'Coinsbit &mdash; <a href="https://coinsbit.io/news/bitcoin-core-v32-freeze-rebases-wallet-quirks/">Bitcoin Core v32: Freeze Looms &mdash; Rebases, Wallet Quirks &amp; Fee Tweaks</a>',
]
core_note = "Release dates are targets set by Bitcoin Core maintainers and may shift. Informational only &mdash; not financial advice."

# ---------- Story 5: Miners underwater ----------
STANDFIRST["bitcoin-miners-underwater-78000-cost"] = "Even after a 12% rally, the price of a bitcoin sits below what it costs the average public miner to produce one &mdash; and the industry&rsquo;s own stress signals are flashing."
mine_body = """<p class="drop">This week&rsquo;s rally to $72,000 was a relief for almost everyone in bitcoin except the people who make it. By JPMorgan&rsquo;s estimate, the average all-in cost for a publicly traded miner to produce one bitcoin is around <strong>$78,000</strong> &mdash; still above the price even after a 12% jump. Before the rally, with bitcoin near $64,000, the gap was a chasm.</p>

<p>The squeeze is structural. A miner&rsquo;s cost is set mostly by electricity and by network difficulty &mdash; the automatic measure of how hard it is to find a block. Difficulty currently sits at a towering <strong>127.48 trillion</strong>. When more machines compete, each one earns a smaller slice of the fixed daily supply of new coins, so per-coin costs rise even as the hardware improves. Push the price below that cost and the marginal miner bleeds.</p>

<h2>The stress is showing up in the data</h2>
<p>VanEck this month counted <strong>eight of twelve</strong> of its capitulation indicators as active &mdash; the kind of readings that historically cluster near cycle lows, when weaker miners sell reserves, power down rigs, or exit. Public miners have been posting heavy losses and, increasingly, renting their power and buildings to artificial-intelligence tenants that outbid bitcoin for electricity. The pivot keeps the lights on, but it is an admission that mining alone no longer pays at these prices.</p>

<div class="pull">When it costs more to mint a coin than the coin will sell for, something has to give &mdash; usually the miners.</div>

<h2>The number that isn&rsquo;t the whole story</h2>
<p>A $78,000 average hides a wide spread. That figure describes listed U.S. miners carrying debt, hardware depreciation, and corporate overhead. Operators running on genuinely cheap or stranded power &mdash; Ethiopian and Paraguayan hydro, flared gas, curtailed renewables &mdash; produce well below the average and stay profitable through the dip. And bitcoin has a built-in release valve: if enough miners quit, difficulty adjusts downward, lowering costs for those who remain. The next adjustment, due in about two days, is estimated at a modest +0.9%.</p>

<p>So the headline is real but self-correcting. Prolonged sub-cost pricing thins the field, concentrates hashrate among the lowest-cost producers, and historically precedes accumulation rather than collapse &mdash; VanEck itself suggests a bottom could form by November. For now, the arithmetic is stark: the network has never been more expensive to secure, and this week the coin it produces is still worth less than the cost of producing it.</p>

<p><em>Why it matters: miner economics are bitcoin&rsquo;s pressure gauge, and right now the needle is in the red even after the price jumped.</em></p>"""
mine_sources = [
 'Bitcoin News Digest &mdash; <a href="https://bitcoinnewsdigest.substack.com/p/bitcoin-news-digest-august-19-2026">JPMorgan ~$78,000 production cost; difficulty 127.48T (Aug. 19, 2026)</a>',
 'The Block &mdash; <a href="https://www.theblock.co/news/markets/2026-08-18-bitcoin-correction-may-nearing-end-8-capitulation-signals-flashing-vaneck-412130">Bitcoin correction may be nearing end as 8 of 12 capitulation signals flash &mdash; VanEck</a>',
 'mempool.space &mdash; <a href="https://mempool.space/mining">Mining dashboard: difficulty and hashrate (read Aug. 20)</a>',
]
mine_note = "Cost estimate is JPMorgan&rsquo;s average for public miners and varies widely by operator; difficulty and price read live on Aug. 20. Informational only &mdash; not financial advice."

# ---------- Story 6: The Take ----------
STANDFIRST["adoption-built-not-decreed-take"] = "El Salvador wrote bitcoin into law and waited. The last five years say use has to be earned, transaction by transaction &mdash; a lesson the grassroots already knew."
take_body = """<p class="drop">This week bitcoin&rsquo;s price jumped 12% because the U.S. Treasury changed how it buys back bonds. That is worth sitting with, because it is the opposite of everything the coin&rsquo;s adoption story is supposed to be about. The price can be moved by Washington in an afternoon. Adoption cannot &mdash; in either direction &mdash; and El Salvador just spent five years proving it.</p>

<p>San Salvador did the maximal top-down thing: it made bitcoin legal tender, compelled merchants to accept it, and handed out a national wallet. Half a decade later, crypto moves under 1% of the country&rsquo;s remittances and the mandatory-acceptance rule has been repealed. The law could order acceptance. It could not order demand.</p>

<h2>Where adoption actually comes from</h2>
<p>Contrast the mandate with the places the Beacon keeps filing from. A charity in Cusco, Peru, teaching families to save in bitcoin six days a week. Meetup organizers in Bandung, Indonesia, routing around a payments ban with a community mint. Sixteen shops on Isla Mujeres taking Lightning because tourists arrive holding it. El Salvador&rsquo;s own Bitcoin Beach &mdash; the one part of the experiment that stuck &mdash; grew from grassroots education years before the legal-tender law, not because of it.</p>

<p>The common thread is a reason to use bitcoin that beats the alternative: a remittance that lands in seconds instead of days, a savings account that inflation can&rsquo;t quietly drain, a payment a hostile bank can&rsquo;t block. Adoption tracks utility. It shows up merchant by merchant, wallet by wallet, and it is stubbornly indifferent to whether a government blesses it &mdash; bitcoin spread through Nigeria, Argentina and Vietnam in the teeth of official hostility.</p>

<div class="pull">You can legislate acceptance. You cannot legislate a reason to reach for the coin.</div>

<h2>The steelman</h2>
<p>None of this makes El Salvador&rsquo;s law worthless. It seeded a bitcoin curriculum in schools, drew tourism and investment out of all proportion to the country&rsquo;s size, and left the state sitting on a reserve now deep in the green. Top-down and bottom-up can reinforce each other: infrastructure and legitimacy from above, real usage from below. The mistake was expecting the decree to substitute for the demand rather than support it.</p>

<p>So as headlines celebrate a 12% pop engineered in a Treasury press release, keep the two clocks separate. Price is set by whoever holds the marginal dollar this hour. Adoption is set by whoever decides, unprompted, that bitcoin solves a problem they actually have. Watch the second clock. It moves slower, and it is the only one that compounds.</p>

<p><em>Why it matters: the day&rsquo;s rally and El Salvador&rsquo;s retreat tell the same truth &mdash; bitcoin&rsquo;s price is dictated from the top, but its use is built from the ground up.</em></p>"""
take_sources = [
 'The Bitcoin Beacon &mdash; <a href="https://thebitcoinbeacon.com/stories/2026-08-20/el-salvador-bitcoin-law-five-years">El Salvador&rsquo;s Bitcoin Law Turns Five</a>',
 'news.bitcoin.com &mdash; <a href="https://news.bitcoin.com/5-years-after-the-bitcoin-law-crypto-accounts-for-just-0-7-of-el-salvadors-5b-remittance-market/">Crypto is 0.7% of El Salvador&rsquo;s remittance market</a>',
 'The Bitcoin Beacon &mdash; <a href="https://thebitcoinbeacon.com/stories/2026-08-18/peru-motiv-circular-economy">A Peruvian Charity Runs Its Aid on Bitcoin</a>',
]
take_note = "Opinion. Draws on this issue&rsquo;s reporting and prior Beacon dispatches. Informational only &mdash; not financial advice."

pages = [
 ("el-salvador-bitcoin-law-five-years", "El Salvador&rsquo;s Bitcoin Law Turns Five. Bukele Admits It Fell Short.",
  "Five years after making bitcoin legal tender, El Salvador&rsquo;s crypto remittances remain under 1% and Bukele concedes the adoption never came. The reserve is what&rsquo;s left.",
  "#2f6f8f", "Policy &amp; Nation-States", "San Salvador", "5",
  "hf_20260820_101811_6dbfbf28-ed66-4768-bd91-4b5c870c32f9.png",
  "A shopkeeper closing a shutter beside an idle payment kiosk on an El Salvador beach at dusk, three-color linocut",
  es_body, es_sources, es_note),
 ("zhibao-shanghai-bitcoin-treasury", "A Shanghai Insurance Broker Buys $155 Million in Bitcoin",
  "Zhibao, a Shanghai digital-insurance broker, closed a $154.7M placement to build a 2,380-coin treasury &mdash; joining the corporate-treasury playbook from a country that bans crypto trading.",
  "#7a4dd1", "Markets &amp; Institutions", "Shanghai", "5",
  "hf_20260820_102145_6e2f81ae-fb4e-482a-9c91-a3589bc55c01.png",
  "A businesswoman locking a large coin in an iron strongbox before the Shanghai Bund skyline, three-color linocut",
  zh_body, zh_sources, zh_note),
 ("bitcoin-core-v32-feature-freeze", "Bitcoin&rsquo;s Developers Freeze the Code for Version 32",
  "Bitcoin Core hit its v32 feature freeze on Aug. 20, switching from new features to bug fixes ahead of a release candidate around Sept. 10 and a final build near Oct. 10.",
  "#b5601f", "Network &amp; Mining", "Global", "5",
  "hf_20260820_101811_b652efd1-a313-459e-be61-eb28f5c3f558.png",
  "Engineers padlocking a heavy carved printing block over a wall of type, three-color linocut",
  core_body, core_sources, core_note),
 ("bitcoin-miners-underwater-78000-cost", "It Costs $78,000 to Mine a Bitcoin. It Sells for Less.",
  "JPMorgan estimates the average public miner spends about $78,000 to produce a coin &mdash; above the price even after a 12% rally &mdash; as VanEck counts eight of twelve capitulation signals.",
  "#b5601f", "Network &amp; Mining", "Global", "4",
  "hf_20260820_101812_0e9e12eb-483a-49a2-a020-c81f7ec80142.png",
  "A technician studying a sagging gauge in an aisle of bitcoin mining machines, three-color linocut",
  mine_body, mine_sources, mine_note),
 ("adoption-built-not-decreed-take", "Bitcoin Adoption Is Built, Not Decreed",
  "The day&rsquo;s Treasury-driven rally and El Salvador&rsquo;s five-year retreat tell the same truth: bitcoin&rsquo;s price is set from the top, but its use is built from the ground up.",
  "#c0392b", "The Take &middot; Opinion", "Global", "5",
  "hf_20260820_101811_477b36c1-3d08-47c1-b2f7-150c3b25e82d.png",
  "A vendor and customer completing a phone payment at a market while an empty podium stands ignored, three-color linocut",
  take_body, take_sources, take_note),
]

for p in pages:
    slug = p[0]
    html = page(slug, p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])
    with open(os.path.join(BASE, slug + ".html"), "w") as f:
        f.write(html)
    print("wrote", slug, len(html))
print("DONE")
