# -*- coding: utf-8 -*-
import os, html

BASE = "/sessions/loving-hopeful-curie/mnt/bitcoin beacon"
DATE = "2026-08-15"
DATE_LONG = "August 15, 2026"
DATE_STRAP = "Saturday, August 15, 2026"
HB = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"
SITE = "https://thebitcoinbeacon.com"

# Vital stats read this run (River price @ 11:45 UTC; mempool block+hashrate)
VS_PRICE = "$62,972"
VS_BLOCK = "962,568"
VS_HASH  = "~900 EH/s"
VS_PRICE_RAW = "62972"   # for index initial
VS_BLOCK_RAW = "962,568"
VS_HASH_RAW  = "900 EH/s"
VS_LABEL = "as of 11:45 UTC"

BEAT_COLOR = {
    "on-the-ground":"#127a5b","money-macro":"#8a5a12","markets":"#7a4dd1",
    "policy-nation-states":"#2f6f8f","network-mining":"#b5601f","opinion":"#c0392b",
}
BEAT_LABEL = {
    "on-the-ground":"On the Ground","money-macro":"Money &amp; Macro","markets":"Markets &amp; Institutions",
    "policy-nation-states":"Policy &amp; Nation-States","network-mining":"Network &amp; Mining","opinion":"Opinion",
}

def U(slug): return "%s/stories/%s/%s" % (SITE, DATE, slug)

# ---- HEAD + HEADER + MODAL (copied verbatim from existing story page) ----
HEAD_CSS = r"""<style>
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

HEADER_HTML = r"""  <div class="mast"><a href="/">
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

MODAL_HTML = r"""<!-- subscribe modal (site-wide) -->
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
    if(/subscribe\.html$/.test(h)||h==='#subscribe'){open(e);}
  });
  m.addEventListener('click',function(e){if(e.target===m)close();});
  m.querySelector('.bb-x').addEventListener('click',close);
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();
</script>"""

def story_page(s):
    color = BEAT_COLOR[s["beat"]]
    label = BEAT_LABEL[s["beat"]]
    url = U(s["slug"])
    hero = s["hero"]
    desc = s["ogdesc"]
    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
      '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
      '<meta name="description" content="%s">\n'
      '<link rel="canonical" href="%s">\n'
      '<link rel="icon" href="/favicon.ico" sizes="any">\n'
      '<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">\n'
      '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
      '<meta name="theme-color" content="#15130f">\n'
      '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
      '<meta property="og:site_name" content="The Bitcoin Beacon">\n'
      '<meta property="og:type" content="article">\n'
      '<meta property="og:title" content="%s">\n'
      '<meta property="og:description" content="%s">\n'
      '<meta property="og:image" content="%s">\n'
      '<meta property="og:url" content="%s">\n'
      '<meta name="twitter:card" content="summary_large_image">\n'
      '<meta name="twitter:title" content="%s">\n'
      '<meta name="twitter:description" content="%s">\n'
      '<meta name="twitter:image" content="%s">\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"NewsArticle","headline":"%s","description":"%s","image":["%s"],"datePublished":"%s","dateModified":"%s","mainEntityOfPage":"%s","author":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com"},"publisher":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com","logo":{"@type":"ImageObject","url":"https://thebitcoinbeacon.com/assets/masthead-ink.png"}}}</script>\n'
      '<title>%s &mdash; The Bitcoin Beacon</title>\n'
      % (desc, url, s["title_plain"], desc, hero, url, s["title_plain"], desc, hero,
         s["title_plain"], desc, hero, DATE, DATE, url, s["title_plain"]))
    doc = (head + HEAD_CSS + "\n</head>\n<body>\n" + HEADER_HTML + "\n\n"
      '  <div class="crumb"><span class="tag" style="color:%s;">%s &middot; %s</span></div>\n' % (color, label, s["place_disp"]) +
      '  <div class="wrap">\n'
      '    <h1 class="title">%s</h1>\n' % s["title"] +
      '    <p class="standfirst">%s</p>\n' % s["standfirst"] +
      '    <div class="meta"><b>By The Bitcoin Beacon</b> &middot; %s &middot; %s &middot; %s</div>\n' % (s["dateline"], DATE_LONG, s["read"]) +
      '  </div>\n'
      '  <div class="hero"><div class="heroart">\n'
      '    <img src="%s" alt="%s">\n' % (hero, s["alt"]) +
      '    <div class="cap">%s &middot; Illustration: The Bitcoin Beacon</div>\n' % label +
      '  </div></div>\n'
      '  <div class="wrap body">\n\n' + s["body"] + "\n" +
      '    <div class="subscribe" id="subscribe"><div class="box">\n'
      '    <h3>The world&rsquo;s bitcoin headlines, in your inbox every morning.</h3>\n'
      '    <p>Free. Five minutes. No hype.</p>\n'
      '    <a class="btn" href="/subscribe.html">Subscribe free</a>\n'
      '  </div></div>\n'
      '  </div>\n'
      '  <footer>THE BITCOIN BEACON &bull; The daily record of Bitcoin\'s global adoption &bull; Informational only &mdash; not financial advice</footer>\n\n'
      + MODAL_HTML + "\n\n</body>\n</html>\n")
    return doc

# ============ CONTENT ============
STORIES = []

# ---- 1. LEAD ----
STORIES.append({
"slug":"lightning-africa-payroll","beat":"on-the-ground",
"title":"Lightning Now Pays Salaries Across Africa",
"title_plain":"Lightning Now Pays Salaries Across Africa",
"standfirst":"Bitcoin&rsquo;s payment layer has quietly become a payroll and remittance rail from Lagos to Nairobi &mdash; reaching feature phones, and mostly through apps that hide the bitcoin entirely.",
"ogdesc":"Bitcoin's Lightning Network has become a payroll and remittance rail across 23 African countries, reaching even feature phones, largely through custodial apps.",
"place_disp":"Lagos","dateline":"LAGOS","read":"7 min read",
"hero":HB+"hf_20260815_115243_e7df8eac-fdc3-4064-be97-7ec569a51db1.png",
"alt":"A Lagos market vendor accepts a mobile phone payment at her produce stall, three-color linocut",
"body":r"""<p class="drop">The fastest-growing use of Bitcoin&rsquo;s Lightning Network in 2026 is not speculation, and it is not tipping. It is payroll. Bitnob, a Nigerian-founded payments company, now runs Lightning-based salary payments for remote workers across 23 African countries, and the volume it moves has grown 340% in a year, according to a June assessment from the wallet-infrastructure firm Spark.</p>

<p>The mechanics are deliberately dull. An employer abroad pays in dollars; the money crosses borders as bitcoin over Lightning &mdash; settling in seconds for a fraction of a cent &mdash; and lands with a worker as local currency. The recipient often never sees a bitcoin balance at all. Bitcoin is the wire, not the destination.</p>

<h2>Reaching the phones that can&rsquo;t reach the internet</h2>
<p>The harder problem in African payments is not fees; it is hardware. Most bitcoin apps assume a smartphone and a data plan. Machankura removed that assumption. It lets people send and receive Lightning payments over USSD and SMS &mdash; the menu-driven codes that work on a $15 feature phone with no internet &mdash; across Ghana, Kenya, Malawi, Nigeria, South Africa and Uganda. A user dials a short code, navigates a text menu, and moves value that settles on the same network a Wall Street desk uses.</p>

<h2>Kenya turned every mobile-money number into a bitcoin address</h2>
<p>The most aggressive experiment is in Kenya. Since May, the payments app Tando has made every mobile number connected to M-Pesa &mdash; roughly 40 million of them &mdash; automatically reachable as a Lightning address in the form number@bitcoin.co.ke. A sender anywhere in the world can pay that address in bitcoin; Tando converts it to M-Pesa credit the recipient spends at a shop counter, with no fee on Tando&rsquo;s side. Bitcoin becomes the settlement layer under Africa&rsquo;s dominant mobile-money system without asking the user to learn a single new habit.</p>

<h2>The network is growing and shrinking at once</h2>
<p>Zoom out and Lightning looks paradoxical. Public capacity sat near 4,898 BTC across 41,080 channels in May, and monthly volume crossed $1.17 billion last November &mdash; up 266% year over year, with about 12 million transactions a month. Yet the number of public nodes has fallen to 17,438, down from a 2022 peak near 20,700. More money is moving over fewer independent machines.</p>

<p>That is the shape of the African rollout too. Bitnob, Machankura and Tando are custodial or heavily abstracted: they hold keys, manage channels and hide the plumbing so an ordinary person never confronts it. Convenience is the product. The network is consolidating around service providers, not spreading node by node.</p>

<div class="pull">Bitcoin is winning Africa as a wire, not as a wallet people hold themselves.</div>

<h2>The trade-off nobody advertises</h2>
<p>For a worker paid in a currency that lost a third of its value, a custodial Lightning wallet that holds dollars for a week and settles instantly is a genuine upgrade. But it is an upgrade with a counterparty. The same abstraction that onboards millions also reintroduces the intermediary bitcoin was built to remove &mdash; a company that can freeze an account, get hacked, or be leaned on by a regulator. The Kenyan grandmother reachable at her phone number is not running a node; she is trusting Tando.</p>

<p>That is not a reason to dismiss the progress. It is the reason to watch what comes next: whether these rails stay custodial funnels, or whether the people they onboard ever take hold of their own keys. Adoption is real. Sovereignty is still optional.</p>

<p><em>Why it matters: bitcoin is becoming everyday money across Africa as a payment rail, not as savings people control &mdash; and it is arriving through apps that hide the coin.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Spark &mdash; <a href="https://www.spark.money/research/lightning-network-2026-state">State of the Lightning Network in 2026</a> (Jun. 3, 2026)</li>
        <li>TechCabal &mdash; <a href="https://techcabal.com/2026/03/04/machankuras-solution-for-crypto-transactions/">Machankura is putting Bitcoin on Africa&rsquo;s most basic phones</a></li>
        <li>Forbes &mdash; <a href="https://www.forbes.com/sites/digital-assets/2026/06/26/tando-is-unlocking-spending-bitcoin-for-40-million-kenyans/">Tando Is Unlocking Spending Bitcoin For 40 Million Kenyans</a></li>
        <li>mempool.space &mdash; <a href="https://mempool.space/lightning">Lightning Network dashboard</a></li>
      </ol>
    </div>
    <p class="note">Figures (23 countries and 340% year-over-year Bitnob growth; Lightning capacity, node count and volume; ~40 million M-Pesa numbers reachable via Tando) are from the cited Spark, TechCabal, Forbes and mempool.space sources. Informational only &mdash; not financial advice.</p>
"""})

# ---- 2. MARKETS ----
STORIES.append({
"slug":"msci-index-exclusion-strategy-metaplanet","beat":"markets",
"title":"MSCI Moves to Drop Strategy and Metaplanet",
"title_plain":"MSCI Moves to Drop Strategy and Metaplanet",
"standfirst":"A proposed index rule would strip the two largest corporate bitcoin holders from MSCI&rsquo;s global benchmarks &mdash; forcing the passive funds that track them to sell.",
"ogdesc":"MSCI has proposed excluding non-operating companies from its global indexes, a rule that simulations show would delete Strategy and Metaplanet and trigger passive outflows.",
"place_disp":"New York","dateline":"NEW YORK","read":"6 min read",
"hero":HB+"hf_20260815_115247_71a1f099-1236-48bb-b91c-fd536f192ad7.png",
"alt":"A lone figure on the steps of a columned Wall Street institution beneath a quotation board with a falling arrow, three-color linocut",
"body":r"""<p class="drop">On August 14, MSCI &mdash; the index provider whose benchmarks guide trillions of dollars in passive money &mdash; proposed a rule that could evict the biggest corporate bitcoin holders from its global stock indexes. The consultation targets what MSCI calls &ldquo;non-operating companies,&rdquo; and by its own simulation the two names that fall out are Strategy and Metaplanet.</p>

<p>The screen is mechanical. A company qualifies as an operating business only if its operating assets exceed 50% of total assets; it must also pass a set of five financial ratios, and failing at least four renders it ineligible. Run against May 2026 data, that test deletes Strategy, Metaplanet and the uranium holder Yellow Cake from the MSCI ACWI IMI, and puts SharpLink, Center Laboratories and Lydia Holding on a watchlist.</p>

<h2>Why an index rule moves real money</h2>
<p>Membership in a benchmark like ACWI is not cosmetic. Index and passive funds are required to hold what the index holds, so inclusion pulls in automatic, price-insensitive buyers &mdash; and exclusion forces them to sell, regardless of what they think of bitcoin. For Strategy, whose shares have traded as a leveraged proxy for its coin pile, a deletion means index funds dumping stock into the market on a fixed date. Analysts framing the proposal put the potential passive outflows in the billions.</p>

<h2>The hidden pillar of the treasury trade</h2>
<p>This exposes something the bitcoin-treasury boom rarely says out loud. Part of the demand for these stocks came not from investors choosing bitcoin, but from passive vehicles mechanically buying an index constituent. Strip the index membership and you remove a buyer that was never there for the thesis. It is the same fragility the Beacon flagged when Strategy began selling coins to defend its own preferred stock: the financial machinery wrapped around the bitcoin has demands the bitcoin itself does not.</p>

<div class="pull">Index funds bought the stock because it was in the index &mdash; not because they wanted bitcoin.</div>

<h2>Strategy pushes back</h2>
<p>Strategy responded the same day, arguing that MSCI should &ldquo;measure markets, not dictate corporate assets&rdquo; &mdash; that an index provider&rsquo;s job is to reflect what public companies are, not to penalize a balance-sheet choice. There is a steelman on MSCI&rsquo;s side too: a firm whose assets are almost entirely bitcoin, funded by convertible debt and share issuance, is arguably not an operating company at all, and a global-equity index is not supposed to be a bitcoin fund in disguise. This is the second attempt; an October 2025 version was deferred after industry pushback.</p>

<h2>What happens next</h2>
<p>The timeline is the story to watch. Feedback runs through the end of September, MSCI publishes final methodology on October 16, and the index review where deletions are actually decided is set for November 11. Between now and then, every treasury company built on the assumption that public markets would keep buying its stock has a reason to be nervous.</p>

<p><em>Why it matters: index inclusion was a quiet source of demand for bitcoin-treasury stocks, and MSCI is proposing to switch it off.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>The Block &mdash; <a href="https://www.theblock.co/news/business/2026-08-14-strategy-metaplanet-msci-index-proposal-411809">Strategy, Metaplanet could face MSCI index removal under new proposal</a> (Aug. 14, 2026)</li>
        <li>CoinDesk &mdash; <a href="https://www.coindesk.com/markets/2026/08/14/bitcoin-holders-strategy-and-metaplanet-face-stock-index-exclusion-under-msci-s-new-proposal">Strategy and Metaplanet face stock-index exclusion under MSCI&rsquo;s new proposal</a></li>
        <li>Cryptobriefing &mdash; <a href="https://cryptobriefing.com/msci-strategy-metaplanet-index-removal/">MSCI could remove Strategy and Metaplanet from indexes in November</a></li>
        <li>Bitcoin Magazine &mdash; <a href="https://bitcoinmagazine.com/news/strategy-slams-msci-possible-index-removal">Strategy Bites Back After MSCI Announces Index Removal</a></li>
      </ol>
    </div>
    <p class="note">The 50%-operating-assets screen, the five-ratio test, the simulated deletions (Strategy, Metaplanet, Yellow Cake) and the Sept./Oct. 16/Nov. 11 timeline are from the cited reports on MSCI&rsquo;s August 2026 consultation. Informational only &mdash; not financial advice.</p>
"""})

# ---- 3. NETWORK & MINING ----
STORIES.append({
"slug":"trezor-shipmonk-data-breach","beat":"network-mining",
"title":"A Shipping Partner Leaked 13,689 Trezor Owners&rsquo; Addresses",
"title_plain":"A Shipping Partner Leaked 13,689 Trezor Owners' Addresses",
"standfirst":"The wallets stayed safe. The customer list &mdash; names, homes and phone numbers of people who own bitcoin &mdash; did not.",
"ogdesc":"A breach at Trezor's fulfillment partner ShipMonk exposed order data for 13,689 hardware-wallet customers, most including names and home addresses.",
"place_disp":"Prague","dateline":"PRAGUE","read":"5 min read",
"hero":HB+"hf_20260815_114919_923c816b-d346-44a8-9b64-1afcb8b9208b.png",
"alt":"A parcel warehouse with an opened box revealing a hardware device beneath a looming padlock, three-color linocut",
"body":r"""<p class="drop">On August 13, the hardware-wallet maker Trezor disclosed a data breach &mdash; not of its own systems, but of a shipping partner. The Czech company said order data for 13,689 customers who received deliveries in the 90 days before August 8 had been exposed through a breach at its fulfillment provider, ShipMonk. Trezor&rsquo;s own infrastructure, its device firmware and customers&rsquo; private keys were untouched.</p>

<p>The exposed records split two ways: 11,742 included names, email addresses, phone numbers and shipping addresses; another 1,947 included names, cities and emails. Affected customers spanned the US, the UK, Sweden, Colombia, Brazil, Italy and Portugal.</p>

<h2>The seed phrase was never the weak point here</h2>
<p>No coins moved, and Trezor was quick to stress that no coins could move from this leak alone. But that framing understates the threat. A list of names paired with home addresses, filtered to people who just bought a bitcoin hardware wallet, is a targeting document. It tells an attacker exactly who holds bitcoin and where they sleep.</p>

<div class="pull">A hardware-wallet customer list is, by definition, a list of people worth robbing.</div>

<p>The immediate danger is phishing: convincing emails or texts impersonating Trezor support, urging a &ldquo;security update&rdquo; that asks for a recovery phrase. The slower, uglier danger is physical &mdash; the so-called &ldquo;$5 wrench&rdquo; attack, where the threat is not a hacker but a person at the door. Self-custody defends against remote theft brilliantly and against a home invasion not at all.</p>

<h2>A bad summer for hardware</h2>
<p>The leak lands in a rough stretch for the category. Earlier in August, a firmware flaw tied to Coldcard wallets was linked to bitcoin thefts running into the tens of millions, draining funds from more than a thousand addresses. The two incidents are unrelated in cause &mdash; one a supply-chain data leak, the other a device vulnerability &mdash; but together they puncture the idea that buying a hardware wallet ends the security conversation.</p>

<h2>What owners should do</h2>
<p>Treat any message referencing a recent Trezor order as hostile until proven otherwise; the attackers now know real order details, which makes their lures more convincing. Never enter a recovery phrase anywhere but the device itself. And weigh the quieter lesson: privacy around a purchase &mdash; where it shipped, under what name &mdash; is part of the security model, and it lives with vendors and their contractors, outside the owner&rsquo;s control.</p>

<p><em>Why it matters: the hardest part of holding your own bitcoin is no longer the cryptography &mdash; it is the metadata other companies keep about you.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Bitcoin Magazine &mdash; <a href="https://bitcoinmagazine.com/news/trezor-data-breach-leaks-customer-info">Data Breach At Trezor Leaks Info On Nearly 14,000 Bitcoin Wallet Users</a></li>
        <li>CryptoRank &mdash; <a href="https://cryptorank.io/news/feed/d093c-trezor-data-breach-leaks-customer-info">Trezor data breach leaks customer info</a></li>
        <li>The Hacker News &mdash; <a href="https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html">Coldcard Hardware Wallet Flaw Linked to Bitcoin Theft</a> (context)</li>
      </ol>
    </div>
    <p class="note">The 13,689 figure, the record split (11,742 with addresses; 1,947 with cities), the affected countries and the ShipMonk attribution are from Trezor&rsquo;s August 13, 2026 disclosure as reported by the cited sources. The Coldcard incident is a separate, earlier event included for context. Informational only &mdash; not financial advice. This touches on physical safety; treat unsolicited &ldquo;support&rdquo; contact with caution.</p>
"""})

# ---- 4. POLICY ----
STORIES.append({
"slug":"el-salvador-keeps-buying-2027-election","beat":"policy-nation-states",
"title":"El Salvador Keeps Buying Bitcoin as Rivals Vow to Stop",
"title_plain":"El Salvador Keeps Buying Bitcoin as Rivals Vow to Stop",
"standfirst":"Five years in, the reserve is near 7,730 coins and still growing daily &mdash; but the 2027 campaign has turned it into a political target.",
"ogdesc":"El Salvador keeps buying bitcoin daily, lifting its reserve toward 7,730 BTC, even as 2027 opposition candidates vow to reverse a policy the IMF already curbed.",
"place_disp":"San Salvador","dateline":"SAN SALVADOR","read":"6 min read",
"hero":HB+"hf_20260815_115252_3caca9ca-9907-44c4-80b6-c3bd042c7ef4.png",
"alt":"A citizen drops a ballot into a wooden box in a San Salvador plaza before a colonial church, three-color linocut",
"body":r"""<p class="drop">El Salvador is still buying bitcoin, one coin at a time, almost every day. The dollar-cost-averaging policy President Nayib Bukele announced in November 2022 has pushed the national reserve toward 7,730 BTC, with more than 1,600 coins added in the 12 months since June 2025. The government has never sold a single coin from the stack.</p>

<p>What has changed is the politics around it. In January 2025, as a condition of a $1.4 billion IMF loan, El Salvador stripped bitcoin of its mandatory legal-tender status. Businesses are no longer required to accept it; the currency became optional rather than compulsory. The reserve stayed; the mandate went.</p>

<h2>A proof of concept, quietly delivered</h2>
<p>Set aside the headlines and El Salvador has demonstrated something specific: a sovereign state can hold a meaningful bitcoin reserve on its balance sheet, ride out deep drawdowns without a forced sale, and keep buying &mdash; all without forcing the asset on its citizens. The IMF, which spent 2021 warning of catastrophe, praised the country&rsquo;s 4% GDP growth in December and described tensions over the holdings as easing.</p>

<div class="pull">The coins are a national policy; the policy is one election from reversal.</div>

<h2>The 2027 problem</h2>
<p>That durability now runs into an electoral calendar. As the 2027 presidential race takes shape, the two main opposition parties have chosen candidates who reject the bitcoin strategy outright, casting it as a fiscal vanity project and a distraction from the cost of living. For the first time, a serious slice of the political class is campaigning on undoing the reserve rather than defending it.</p>

<p>The vulnerability is structural. Because the bitcoin policy is identified almost entirely with one president, it inherits his political fortunes. A reserve that depends on a single leader&rsquo;s survival is a thinner institution than a law with cross-party buy-in &mdash; and the mandate has already been softened once under outside pressure.</p>

<h2>The pivot underneath</h2>
<p>There is a second signal worth noting: the geothermal energy once earmarked to mine bitcoin from the country&rsquo;s volcanoes is increasingly being routed to power AI data centers instead. The reserve is being defended as a store of value while the state&rsquo;s cheap-energy bet migrates to a different buyer. El Salvador is not abandoning bitcoin. It is learning to hold it more quietly, and hedging where the money is.</p>

<p><em>Why it matters: El Salvador proved a state can hold bitcoin without making it legal tender &mdash; but a reserve tied to one man&rsquo;s politics is only as permanent as his next election.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Crypto Economy &mdash; <a href="https://crypto-economy.com/el-salvadors-bitcoin-future-in-doubt/">El Salvador&rsquo;s Bitcoin Future in Doubt? 2027 Election Rivals Take Aim</a></li>
        <li>Bitcoin Magazine &mdash; <a href="https://bitcoinmagazine.com/news/five-years-on-el-salvador-bitcoin">Five Years On, El Salvador Is Still Buying Bitcoin</a></li>
        <li>CoinDesk &mdash; <a href="https://www.coindesk.com/business/2025/12/23/tensions-over-el-salvador-s-bitcoin-holdings-ease-as-imf-praises-economic-progress">IMF praises El Salvador&rsquo;s 4% GDP growth as bitcoin tensions ease</a></li>
      </ol>
    </div>
    <p class="note">Reserve size (~7,730 BTC; +1,600 in 12 months), the November 2022 one-a-day policy, the January 2025 IMF loan and legal-tender change, and the 2027 opposition positions are from the cited sources. Informational only &mdash; not financial advice.</p>
"""})

# ---- 5. MONEY & MACRO ----
STORIES.append({
"slug":"sovereign-funds-bitcoin-etf","beat":"money-macro",
"title":"Gulf Wealth Funds Are Quietly Buying the Bitcoin ETF",
"title_plain":"Gulf Wealth Funds Are Quietly Buying the Bitcoin ETF",
"standfirst":"From Abu Dhabi to Luxembourg, sovereign funds are taking bitcoin exposure through Wall Street wrappers &mdash; not private keys.",
"ogdesc":"Sovereign wealth funds from Abu Dhabi to Luxembourg are building bitcoin exposure through regulated ETFs rather than direct custody, disclosures show.",
"place_disp":"Abu Dhabi","dateline":"ABU DHABI","read":"5 min read",
"hero":HB+"hf_20260815_115256_445ebc74-318f-411e-a8fd-752e7d73267e.png",
"alt":"A robed figure gazes across the water toward the Abu Dhabi skyline beside a stone sovereign vault, three-color linocut",
"body":r"""<p class="drop">When El Salvador wanted bitcoin, it bought coins and put them on its balance sheet. When the world&rsquo;s largest sovereign wealth funds want bitcoin, they buy an exchange-traded fund. The gap between those two routes is becoming one of the defining features of how bitcoin enters institutional portfolios.</p>

<p>Abu Dhabi&rsquo;s Mubadala Investment Company expanded its stake in BlackRock&rsquo;s iShares Bitcoin Trust, the ETF known as IBIT, to 12.7 million shares by the end of 2025 &mdash; a position that topped $1 billion at its peak valuation. Luxembourg&rsquo;s Intergenerational Sovereign Wealth Fund put roughly 1% of its portfolio, about &euro;850 million, into bitcoin ETFs in late 2025. As of mid-2026, at least one sovereign fund is reported to be buying spot bitcoin directly, with a second said to be considering it.</p>

<h2>The wrapper is the point</h2>
<p>These funds are not choosing bitcoin over the traditional system; they are choosing bitcoin through it. A regulated US ETF offers custody by a name a state auditor recognizes, a familiar reporting line, and an exit that clears through the same brokers as everything else they own. The private key &mdash; the thing bitcoiners treat as the entire innovation &mdash; is exactly what these institutions are paying a fee to avoid touching.</p>

<div class="pull">Nations now take bitcoin exposure through the same wrapper retail investors use.</div>

<h2>Read the disclosures carefully</h2>
<p>The steelman for skepticism is real. These positions surface in lagged regulatory filings that offer a snapshot months old, and a sovereign fund&rsquo;s ETF stake can be a hedge, a client-driven mandate, or a small tactical allocation rather than a conviction bet. One quarter&rsquo;s 13F is not a doctrine. A billion dollars is also a rounding error inside funds that manage hundreds of billions.</p>

<h2>Why it still matters</h2>
<p>Even discounted, the direction is notable. The ETF that critics dismissed as a vehicle for retail speculation has become the on-ramp of choice for some of the most conservative pools of capital on earth. That normalizes bitcoin as a portfolio line item &mdash; and it concentrates a growing share of demand inside a handful of regulated custodians, the mirror image of the self-custody ideal playing out on the ground in Africa and El Salvador.</p>

<p><em>Why it matters: the same regulated wrapper retail uses is now how nations get bitcoin exposure &mdash; convenient, auditable, and one more step away from anyone holding a key.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>ETF Stream &mdash; <a href="https://www.etfstream.com/articles/abu-dhabi-s-mubadala-one-of-many-sovereign-wealth-funds-buying-blackrock-bitcoin-etf">Abu Dhabi&rsquo;s Mubadala one of many sovereign wealth funds buying BlackRock bitcoin ETF</a></li>
        <li>CoinShares &mdash; <a href="https://coinshares.com/us/insights/knowledge/sovereign-funds-a-new-class-of-investors-for-crypto-/">Sovereign wealth funds: a new class of investors in crypto</a></li>
        <li>Crypto Briefing &mdash; <a href="https://cryptobriefing.com/sovereign-wealth-funds-bitcoin-regulated-access/">Sovereign wealth funds favor regulated access to Bitcoin</a></li>
      </ol>
    </div>
    <p class="note">The Mubadala 12.7M-share IBIT stake and the Luxembourg 1% / &euro;850M allocation are drawn from the cited disclosures and reporting; both reflect end-2025 filings and may have changed. Informational only &mdash; not financial advice.</p>
"""})

# ---- 6. THE TAKE ----
STORIES.append({
"slug":"miners-hashrate-flat-price-take","beat":"opinion",
"title":"Miners Are Betting on a Price That Hasn&rsquo;t Arrived",
"title_plain":"Miners Are Betting on a Price That Hasn't Arrived",
"standfirst":"Hashrate keeps setting records while the price sits flat. That is a wager, not a vote of confidence.",
"ogdesc":"Bitcoin's hashrate and difficulty keep climbing toward records while the price stays flat near $63,000 — a bet on the future, not proof of it.",
"place_disp":"The Take","dateline":"GLOBAL","read":"5 min read",
"hero":HB+"hf_20260815_115247_71a1f099-1236-48bb-b91c-fd536f192ad7.png",
"alt":"Editorial linocut of finance and markets",
"body":r"""<p class="drop">The most-cited bullish statistic in bitcoin is also the most misread. Network hashrate is hovering near 900 exahashes a second, and mining difficulty sits around 127 trillion, close to an all-time high, with the next upward adjustment due around August 23. The standard interpretation: miners are pouring in, so miners must be confident. The reality is more like a poker table late in a losing session.</p>

<p>Because here is the other half of the picture. The price has gone nowhere &mdash; bitcoin is stuck in the low $63,000s, and the loudest voices on the timeline are talking about capitulation, not breakout. Rising difficulty against a flat price means one thing mechanically: revenue per unit of hashrate is falling. Every new rig plugged in makes every existing rig earn less.</p>

<h2>The economics don&rsquo;t care about vibes</h2>
<p>A miner&rsquo;s income is the block subsidy &mdash; currently 3.125 BTC per block &mdash; plus fees, and fees right now are almost nothing; the network is clearing transactions at well under two satoshis per byte. So miners live on the subsidy priced in dollars. When difficulty climbs and price stalls, the same electricity buys a smaller and smaller slice of a fixed reward. That is not a signal of health. It is a squeeze.</p>

<div class="pull">Hashrate is a lagging vote. It reflects rigs ordered months ago, not conviction today.</div>

<h2>What record hashrate actually tells you</h2>
<p>Hashrate is a trailing indicator dressed as a leading one. The machines humming today were ordered and financed months back, when the trade looked different. They keep running because the marginal cost of switching them off is real and the hope of a higher price is free. What resolves the squeeze is not sentiment but attrition: if the price stays flat, the miners with the worst power contracts and the oldest hardware capitulate first, difficulty drops at the next retarget, and the survivors inherit a cheaper network.</p>

<p>The steelman for the incumbents is that this is exactly the plan &mdash; the lowest-cost operators expand into weakness precisely so that when rivals fold, they own more of the subsidy. That is rational, and some will win it. But it is a bet on a future price, financed by burning through a present one. Read record hashrate as ambition, not confirmation. The chart that matters is not how much computing power is guarding the network. It is whether the price ever shows up to pay for it.</p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>mempool.space &mdash; <a href="https://mempool.space/mining">Mining Dashboard</a> (hashrate ~900 EH/s; difficulty 127.48T; next adjustment ~Aug. 23 &mdash; read this run)</li>
        <li>CoinWarz &mdash; <a href="https://www.coinwarz.com/bitcoin-difficulty">Bitcoin Difficulty Chart</a></li>
      </ol>
    </div>
    <p class="note">Hashrate, difficulty and the retarget estimate were read from mempool.space during this edition&rsquo;s production run. The block subsidy (3.125 BTC) reflects the post-2024-halving schedule. Opinion; informational only &mdash; not financial advice.</p>
"""})

# ---- WRITE STORY PAGES ----
sdir = os.path.join(BASE, "public", "stories", DATE)
os.makedirs(sdir, exist_ok=True)
for s in STORIES:
    with open(os.path.join(sdir, s["slug"]+".html"), "w") as f:
        f.write(story_page(s))

print("wrote %d story pages to %s" % (len(STORIES), sdir))
for s in STORIES:
    print("  -", s["slug"])
