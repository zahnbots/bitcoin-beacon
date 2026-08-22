# -*- coding: utf-8 -*-
import os
DATE = "2026-08-22"
OUT = "/sessions/festive-nice-archimedes/mnt/bitcoin beacon/public/stories/" + DATE
os.makedirs(OUT, exist_ok=True)

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<link rel="canonical" href="https://thebitcoinbeacon.com/stories/{date}/{slug}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#15130f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta property="og:site_name" content="The Bitcoin Beacon">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{hero}">
<meta property="og:url" content="https://thebitcoinbeacon.com/stories/{date}/{slug}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{hero}">
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "NewsArticle", "headline": "{title}", "description": "{desc}", "image": ["{hero}"], "datePublished": "{date}", "dateModified": "{date}", "mainEntityOfPage": "https://thebitcoinbeacon.com/stories/{date}/{slug}", "author": {{"@type": "Organization", "name": "The Bitcoin Beacon", "url": "https://thebitcoinbeacon.com"}}, "publisher": {{"@type": "Organization", "name": "The Bitcoin Beacon", "url": "https://thebitcoinbeacon.com", "logo": {{"@type": "ImageObject", "url": "https://thebitcoinbeacon.com/assets/masthead-ink.png"}}}}}}</script>
<title>{title} &mdash; The Bitcoin Beacon</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&display=swap');
  :root{{ --ink:#15130f; --muted:#6b6459; --line:#e7e3da; --accent:#e8820c; --paper:#ffffff; --wash:#faf7f1; }}
  *{{ box-sizing:border-box; }}
  body{{ margin:0; background:var(--paper); color:var(--ink); font-family:'Inter',system-ui,Arial,sans-serif; line-height:1.6; }}
  a{{ color:inherit; text-decoration:none; }}
  .nav{{ position:sticky; top:0; z-index:20; background:rgba(255,255,255,.94); backdrop-filter:blur(6px); border-bottom:1px solid var(--line); }}
  .nav .in{{ max-width:1120px; margin:0 auto; display:flex; align-items:center; gap:26px; padding:12px 24px; }}
  .nav img{{ height:56px; }}
  .nav .links{{ display:flex; gap:20px; font-size:13px; font-weight:600; color:#4a463f; margin-left:6px; }}
  .nav .links a:hover{{ color:var(--accent); }}
  .nav .sub{{ background:var(--ink); color:#fff; font-size:12px; font-weight:700; padding:9px 15px; border-radius:999px; }}
  .nav .menu-btn{{ display:none; background:none; border:0; font-size:22px; line-height:1; cursor:pointer; color:var(--ink); padding:4px 8px; -webkit-tap-highlight-color:transparent; }}
  .wrap{{ max-width:720px; margin:0 auto; padding:0 24px; }}
  .crumb{{ max-width:720px; margin:26px auto 0; padding:0 24px; }}
  .tag{{ display:inline-block; font-size:11px; font-weight:800; letter-spacing:1.4px; text-transform:uppercase; color:#8a5a12; }}
  h1.title{{ font-family:'Fraunces',Georgia,serif; font-weight:700; font-size:44px; line-height:1.08; letter-spacing:-.5px; margin:10px 0 14px; }}
  .standfirst{{ font-size:20px; line-height:1.5; color:#3b382f; font-family:'Fraunces',Georgia,serif; font-style:italic; margin:0 0 20px; }}
  .meta{{ display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; font-size:13px; color:var(--muted); border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:12px 0; margin-bottom:24px; }}
  .meta b{{ color:var(--ink); font-weight:700; }}
  .hero{{ max-width:1000px; margin:0 auto 28px; padding:0 24px; }}
  .heroart{{ height:360px; border-radius:14px; position:relative; overflow:hidden; background:#111; }}
  .heroart img{{ width:100%; height:100%; object-fit:cover; display:block; }}
  .heroart .cap{{ position:absolute; left:0; bottom:0; width:100%; padding:14px 18px; font-size:12px; color:#fff; background:linear-gradient(transparent,rgba(0,0,0,.55)); }}
  .body{{ font-size:18px; }}
  .body p{{ margin:0 0 18px; }}
  .body h2{{ font-family:'Fraunces',Georgia,serif; font-size:26px; font-weight:700; margin:34px 0 10px; letter-spacing:-.3px; }}
  .body .drop::first-letter{{ float:left; font-family:'Fraunces',serif; font-weight:700; font-size:64px; line-height:50px; padding:6px 10px 0 0; color:var(--accent); }}
  .pull{{ font-family:'Fraunces',Georgia,serif; font-size:26px; line-height:1.3; font-weight:500; color:var(--ink); border-left:4px solid var(--accent); padding:6px 0 6px 20px; margin:26px 0; }}
  .sources{{ background:var(--wash); border:1px solid var(--line); border-radius:12px; padding:16px 20px; margin:26px 0; font-size:14px; }}
  .sources h4{{ margin:0 0 8px; font-size:12px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted); }}
  .sources ol{{ margin:0; padding-left:20px; }} .sources li{{ margin-bottom:6px; }}
  .sources a{{ color:var(--accent); text-decoration:underline; word-break:break-word; }}
  .note{{ font-size:12.5px; color:var(--muted); font-style:italic; border-top:1px solid var(--line); padding-top:14px; margin-top:24px; }}
  .subscribe{{ max-width:1120px; margin:34px auto; padding:26px 24px; text-align:center; }}
  .subscribe .box{{ background:var(--ink); color:#fff; border-radius:16px; padding:30px 24px; }}
  .subscribe h3{{ font-family:'Fraunces',serif; font-size:24px; margin:0 0 8px; }}
  .subscribe p{{ color:#c9c3b8; margin:0 0 16px; font-size:15px; }}
  .subscribe .btn{{ display:inline-block; background:var(--accent); color:#fff; font-weight:700; padding:12px 22px; border-radius:999px; font-size:14px; }}
  footer{{ border-top:1px solid var(--line); padding:26px 24px; text-align:center; color:var(--muted); font-size:12px; }}
  @media(max-width:720px){{ h1.title{{ font-size:32px; }} }}
  @media(max-width:768px){{
    html,body{{ max-width:100%; overflow-x:hidden; }}
    .nav .in{{ flex-wrap:nowrap; gap:8px 10px; padding:10px 14px; }}
    .nav .menu-btn{{ display:inline-flex; align-items:center; }}
    .nav img{{ height:34px; }}
    .nav .links{{ display:none; }}
    .nav .sub{{ margin-left:auto; padding:8px 12px; white-space:nowrap; }}
    .crumb{{ margin-top:20px; padding:0 16px; }}
    .wrap{{ padding:0 16px; }}
    h1.title{{ font-size:27px; }}
    .standfirst{{ font-size:17px; }}
    .hero{{ padding:0 16px; margin-bottom:22px; }}
    .heroart{{ height:210px; }}
    .body{{ font-size:16px; }}
    .body h2{{ font-size:22px; }}
    .pull{{ font-size:21px; }}
  }}
  .mast{{ background:var(--paper); border-bottom:1px solid var(--line); }}
  .mast a{{ display:flex; align-items:center; justify-content:center; gap:18px; padding:20px 24px 16px; }}
  .mast img{{ height:119px; width:119px; border-radius:50%; }}
  .mast span{{ font-family:'Fraunces',Georgia,serif; font-weight:700; font-size:42px; letter-spacing:-.5px; color:var(--ink); }}
  .nav .in{{ position:relative; justify-content:center; }}
  .nav .sub{{ position:absolute; right:24px; top:50%; transform:translateY(-50%); margin-left:0; }}
  .nav .menu-btn{{ position:absolute; left:14px; top:50%; transform:translateY(-50%); }}
  @media(max-width:768px){{
    .mast a{{ gap:12px; padding:18px 14px 12px; }}
    .mast img{{ height:64px; width:64px; }}
    .mast span{{ font-size:24px; letter-spacing:-.3px; }}
    .nav{{ position:static !important; background:var(--paper) !important; backdrop-filter:none !important; }}
    .nav .in{{ flex-direction:column !important; align-items:center; padding:12px 14px 16px !important; gap:0 !important; }}
    .nav .links{{ display:flex !important; flex-direction:row !important; flex-wrap:wrap !important; justify-content:center; overflow:visible !important; gap:9px 18px; padding:0 !important; margin:0; width:100%; font-size:13.5px; position:static !important; box-shadow:none !important; background:transparent !important; border:0 !important; }}
    .nav .links a{{ white-space:nowrap; border-top:0 !important; padding:0 !important; font-size:13.5px !important; }}
    .nav .sub{{ display:inline-block !important; position:static !important; transform:none !important; margin:14px auto 0 !important; padding:9px 26px; box-shadow:none !important; font-size:13px; }}
    .nav .menu-btn{{ display:none !important; }}
  }}
</style>
</head>
<body>
  <div class="mast"><a href="/">
    <img src="/assets/beacon-badge-400.png" alt="The Bitcoin Beacon" width="400" height="400">
    <span>The Bitcoin Beacon</span>
  </a></div>
  <div class="nav"><div class="in">
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    <div class="links"><a href="/archive/on-the-ground.html">On the Ground</a><a href="/archive/money-macro.html">Money &amp; Macro</a><a href="/archive/markets.html">Markets</a><a href="/archive/network-mining.html">Network &amp; Mining</a><a href="/archive/opinion.html">Opinion</a><a href="/archive/policy-nation-states.html">Nation-States</a><a href="/archive.html">Archive</a><a href="/custody/">Custody</a></div>
    <a class="sub" href="#subscribe">Subscribe</a>
  </div></div>
  <script>
  (function(){{var b=document.querySelector('.nav .menu-btn');if(b){{b.addEventListener('click',function(){{var n=b.closest('.nav');var open=n.classList.toggle('open');b.setAttribute('aria-expanded',open?'true':'false');}});}}}})();
  </script>

  <div class="crumb"><span class="tag" style="color:#8a5a12;">{tagtext}</span></div>
  <div class="wrap">
    <h1 class="title">{title}</h1>
    <p class="standfirst">{standfirst}</p>
    <div class="meta"><b>By The Bitcoin Beacon</b> &middot; {place} &middot; August 22, 2026 &middot; {minread} min read</div>
  </div>
  <div class="hero"><div class="heroart">
    <img src="{hero}" alt="{alt}">
    <div class="cap">{cap}</div>
  </div></div>
  <div class="wrap body">
{body}
    <div class="sources">
      <h4>Sources</h4>
      <ol>
{sources}
      </ol>
    </div>
    <p class="note">{note}</p>
  </div>
  <div class="subscribe" id="subscribe"><div class="box">
    <h3>The world&rsquo;s bitcoin headlines, in your inbox every morning.</h3>
    <p>Free. Five minutes. No hype.</p>
    <a class="btn" href="/subscribe.html">Subscribe free</a>
  </div></div>

  <footer>THE BITCOIN BEACON &bull; The daily record of Bitcoin's global adoption &bull; Informational only &mdash; not financial advice</footer>

<!-- subscribe modal (site-wide) -->
<style>
.bb-modal{{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;background:rgba(21,19,15,.62);padding:20px;}}
.bb-modal.open{{display:flex;}}
.bb-modal .bb-card{{background:#faf7f1;border-radius:16px;max-width:620px;width:100%;padding:16px 16px 8px;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.35);}}
.bb-modal .bb-x{{position:absolute;top:6px;right:12px;background:none;border:0;font-size:28px;color:#6b6459;cursor:pointer;line-height:1;}}
.bb-modal iframe{{width:100%;height:340px;border:0;border-radius:10px;background:#fff;}}
</style>
<div class="bb-modal" id="bb-modal" role="dialog" aria-modal="true" aria-label="Subscribe to The Bitcoin Beacon">
  <div class="bb-card">
    <button class="bb-x" aria-label="Close">&times;</button>
    <iframe data-src="https://subscribe-forms.beehiiv.com/2c9c948c-bcee-4d82-ad46-d31816c72af4" title="Subscribe to The Bitcoin Beacon"></iframe>
  </div>
</div>
<script>
(function(){{
  var m=document.getElementById('bb-modal');if(!m)return;
  var f=m.querySelector('iframe');
  function open(e){{if(e)e.preventDefault();if(!f.src)f.src=f.getAttribute('data-src');m.classList.add('open');document.body.style.overflow='hidden';}}
  function close(){{m.classList.remove('open');document.body.style.overflow='';}}
  document.addEventListener('click',function(e){{
    var a=e.target.closest('a');if(!a)return;
    var h=a.getAttribute('href')||'';
    if(/subscribe\\.html$/.test(h)||h==='#subscribe'){{open(e);}}
  }});
  m.addEventListener('click',function(e){{if(e.target===m)close();}});
  m.querySelector('.bb-x').addEventListener('click',close);
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}})();
</script>

</body>
</html>"""

CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"

stories = []

# 1. LEAD — Kazakhstan
stories.append(dict(
  slug="kazakhstan-mines-bitcoin-national-reserve",
  tagtext="Policy &amp; Nation-States &middot; Astana",
  place="ASTANA",
  minread=7,
  title="Kazakhstan Claims a Tenth of Its Miners&rsquo; Bitcoin",
  standfirst="A rule in force since Aug. 1 diverts a slice of every approved miner&rsquo;s output into a state reserve &mdash; a country buying bitcoin by taxing the machines it powers.",
  desc="Kazakhstan's Resolution 638, effective Aug. 1, 2026, forces large miners to hand 10% of net mined coins to a national crypto reserve run by the central bank.",
  hero=CF+"hf_20260822_105823_51bbaf5b-8c7c-477d-96d6-9cfb5d0f7e86.png",
  alt="A Kazakh engineer inspecting rows of mining machines on the steppe below the Astana skyline, three-color linocut",
  cap="Policy &amp; Nation-States &middot; A state turns its hosted hashrate into a national ledger entry &middot; Illustration: The Bitcoin Beacon",
  body="""<p class="drop">Kazakhstan has stopped waiting for a national bitcoin reserve to fill itself by purchase. Since <strong>August 1</strong>, under Government Resolution No. 638, the country&rsquo;s largest licensed miners have been required to hand over <strong>10% of the digital assets they mine</strong>, every month, to a state-run fund &mdash; coins that flow to the National Bank&rsquo;s investment arm and into what officials call a national strategic crypto reserve.</p>

<p>It is a quietly radical design. Most governments that want bitcoin on their books either buy it, seize it, or mine it themselves. Kazakhstan is doing none of those. It is taxing the hashrate it already hosts, in kind, and keeping the coins.</p>

<h2>Who has to pay, and how much</h2>
<p>The rule targets scale, not hobbyists. To fall under the &ldquo;strategic mining&rdquo; regime, an operator must run a data center of at least <strong>150 megawatts</strong> and deploy rigs each clearing <strong>150 terahashes per second</strong>. Those that qualify get something valuable in a power-constrained country &mdash; regulated, priced electricity access &mdash; and in exchange transfer a tenth of their <em>net</em> mined output to the Astana Hub fund each month.</p>

<p>&ldquo;Net&rdquo; is doing real work in that sentence. The handover is calculated after electricity and transmission charges, including value-added tax, so the state takes its 10% of what is left once the miner&rsquo;s energy bill is settled, not of the gross block reward. The legal scaffolding came first: President Kassym-Jomart Tokayev signed the enabling decree on <strong>July 7</strong>, and the resolution operationalized it three weeks later.</p>

<h2>A reserve that isn&rsquo;t only bitcoin</h2>
<p>Here the story complicates. The reserve&rsquo;s mandate is not confined to bitcoin. Its charter reaches crypto derivatives and equity stakes in crypto companies, making it closer to a diversified state investment vehicle than a sovereign bitcoin stack in the mold El Salvador markets. The coins come in as bitcoin; what the fund becomes is a portfolio.</p>

<div class="pull">The coins arrive as bitcoin. What the reserve becomes is a portfolio.</div>

<p>That matters for anyone reading this as a nation-state endorsement of bitcoin-as-money. A government collecting bitcoin and then holding it as one line in a basket of crypto exposures is making a financial bet, not a monetary declaration. The digital-gold logic &mdash; scarce, neutral, held for decades &mdash; sits uneasily beside a fund permitted to trade derivatives.</p>

<h2>Why Kazakhstan, and why now</h2>
<p>Kazakhstan became a mining heavyweight almost by accident. When China expelled its miners in 2021, a large share of that hashrate crossed the border to Kazakh coal and gas power, briefly making the country one of the world&rsquo;s top mining destinations. The honeymoon soured fast: winter power shortages, grid strain, and a crackdown on unregistered operations pushed the government to license, meter, and tax the industry rather than tolerate it.</p>

<p>Resolution 638 is the next turn of that screw. Instead of merely charging miners for power, the state now takes a cut of their product &mdash; converting a volatile, hard-to-value industry into a stream of hard assets on the central bank&rsquo;s balance sheet. For a resource-exporting economy used to monetizing oil, gas, and uranium, bitcoin becomes one more extractable output of the grid.</p>

<h2>The catch</h2>
<p>Two risks sit under the policy. The first is avoidance: the 150 MW / 150 TH/s threshold draws a bright line, and operators just beneath it, or willing to fragment, may structure around the strategic-miner designation to keep their coins. The second is price. A reserve funded by a percentage of mining output grows fastest exactly when bitcoin is expensive and miner margins are thin &mdash; and thinnest when a downturn would make the coins cheap to accumulate. The state is a forced buyer on someone else&rsquo;s schedule.</p>

<p>Still, the direction is unmistakable. A government has decided that the most reliable way to accumulate bitcoin is to skim it from the machines drawing on its own power lines.</p>

<p><em>Why it matters: Kazakhstan is building a sovereign bitcoin position without spending a tenge on the open market &mdash; and showing every hydro- and hydrocarbon-rich state a template for turning hosted hashrate into a national asset.</em></p>""",
  sources="""        <li>TFTC &mdash; <a href="https://www.tftc.io/kazakhstan-national-crypto-reserve-miner-tax-resolution-638">Kazakhstan Builds Crypto Reserve by Taxing Bitcoin Miners 10%</a></li>
        <li>Cryptopolitan &mdash; <a href="https://www.cryptopolitan.com/kazakhstan-crypto-reserve-with-mined-coins/">Kazakhstan to top up crypto reserve with 10% of coins minted under &lsquo;strategic mining&rsquo; rules</a></li>
        <li>BigGo Finance &mdash; <a href="https://finance.biggo.com/news/9651da8e-baec-4083-bd08-bea8bf9e099d">Kazakhstan Ties Bitcoin Mining to National Reserve, Mandates 10% Production Handover</a></li>
        <li>CoinTurk &mdash; <a href="https://en.coin-turk.com/kazakhstan-approves-new-bitcoin-mining-rules-reserve-mechanism-set-for-2026/">Kazakhstan approves new Bitcoin mining rules, reserve mechanism set for 2026</a></li>
        <li>TradingView / Cointelegraph &mdash; <a href="https://www.tradingview.com/news/cointelegraph:43c67bd12094b:0-kazakhstan-approves-strategic-crypto-mining-rules-tied-to-national-reserve/">Kazakhstan approves strategic crypto mining rules tied to national reserve</a></li>""",
  note="Threshold, 10% handover, calculation method and effective date per Resolution No. 638 as reported by the sources above, August 2026. Informational only &mdash; not financial advice.",
))

# 2. Philippines
stories.append(dict(
  slug="philippines-pouch-lightning-remittances-ofw",
  tagtext="On the Ground &middot; Manila",
  place="MANILA",
  minread=6,
  title="Filipinos Abroad Send Money Home Over Bitcoin",
  standfirst="Pouch.ph and Neutronpay have opened Lightning corridors from Canada and Vietnam that land pesos in seconds &mdash; on a remittance flow worth $38 billion a year.",
  desc="Pouch.ph and Neutronpay let overseas Filipinos in Canada and Vietnam send remittances over the Lightning Network, settling to Philippine banks and e-wallets in seconds.",
  hero=CF+"hf_20260822_105823_86c59427-4c4a-416f-8f33-66fd23b242a4.png",
  alt="A Filipino family in a Manila neighborhood receiving money on a phone, jeepney and sari-sari store behind, three-color linocut",
  cap="On the Ground &middot; Bitcoin as the invisible rail under the remittances that keep households afloat &middot; Illustration: The Bitcoin Beacon",
  body="""<p class="drop">The money that keeps millions of Filipino households running rarely arrives as bitcoin &mdash; but increasingly it travels as bitcoin. Pouch.ph, a Manila-based Lightning payments company, has expanded its remittance service through a partnership with Neutronpay, letting overseas Filipino workers in <strong>Canada and Vietnam</strong> send funds that land in Philippine banks and e-wallets within seconds, at exchange rates that beat the incumbents.</p>

<p>The recipient never sees a coin. A worker in Toronto or Ho Chi Minh City pays in local currency; the value crosses borders as a Lightning payment; a mother in Cebu receives pesos in her GCash or bank account. Bitcoin is the pipe, not the product.</p>

<h2>Why the pipe matters</h2>
<p>Overseas Filipino workers send home roughly <strong>$38 billion a year</strong>, one of the largest remittance flows on earth and a pillar of the national economy. On that river of money, fees are not a rounding error &mdash; the few percent skimmed by banks and money-transfer operators, plus the spread hidden in bad exchange rates, add up to billions that never reach families.</p>

<p>Lightning attacks both. Settlement is near-instant instead of next-day, and because the corridor routes value as bitcoin rather than through a chain of correspondent banks, the cost structure is thinner. For a sender comparing what arrives at the other end, the pitch is simple: more of the money gets there, faster.</p>

<div class="pull">The worker pays in dollars, the family receives pesos, and bitcoin is the only part nobody in the transaction ever touches.</div>

<h2>A corridor strategy, not a wallet</h2>
<p>The design is deliberate. Rather than convince tens of millions of Filipinos to hold bitcoin &mdash; a hard sell in a country where the peso is the unit of daily life &mdash; Pouch is building the rails and letting fiat sit on both ends. Each new partnership is a corridor: Canada and Vietnam now, with the value of the network rising as sending countries multiply. The Neutronpay tie-up matters because it plugs Pouch into an existing Southeast Asian Lightning footprint instead of starting cold in each market.</p>

<p>The Philippines is fertile ground. It consistently ranks among the top countries for crypto ownership, its regulators have engaged rather than banned, and its diaspora is vast, digitally connected, and fee-sensitive. Those are the exact conditions in which a payments rail can scale before a savings culture does.</p>

<h2>The open question</h2>
<p>Whether this counts as bitcoin &ldquo;adoption&rdquo; depends on what you are counting. If adoption means people holding and saving in bitcoin, a corridor that converts to pesos on arrival barely moves the needle. If it means bitcoin quietly becoming the cheapest way to move value across borders &mdash; displacing correspondent banking on one of the world&rsquo;s biggest remittance routes &mdash; then Manila is a case study in winning by disappearing into the plumbing.</p>

<p><em>Why it matters: on a $38 billion flow, shaving fees and settlement time is a concrete, daily win for households &mdash; even as almost no one in the chain ever holds a satoshi.</em></p>""",
  sources="""        <li>BitPinas &mdash; <a href="https://bitpinas.com/news/pouch-neutronpay-canada-vietnam-partnership/">Pouch.ph&rsquo;s Bitcoin Remittance Service Can Now Be Used by OFWs in Canada, Vietnam Through Neutronpay</a></li>
        <li>Tranglo &mdash; <a href="https://www.tranglo.com/blog/the-state-of-digital-currency-and-remittance-in-the-philippines/">The state of digital currency and remittance in the Philippines</a></li>
        <li>CryptoBriefing &mdash; <a href="https://cryptobriefing.com/bitcoin-lightning-payments-kenya-tando/">Bitcoin used for everyday payments via the Lightning Network</a> (context on Lightning fiat-settlement apps)</li>""",
  note="Remittance total per Philippine central-bank (BSP) reporting; corridor details per BitPinas, August 2026. Informational only &mdash; not financial advice.",
))

# 3. Ethiopia
stories.append(dict(
  slug="ethiopia-halts-new-bitcoin-mining-permits",
  tagtext="Network &amp; Mining &middot; Addis Ababa",
  place="ADDIS ABABA",
  minread=6,
  title="Ethiopia Stops Approving New Bitcoin Miners",
  standfirst="The continent&rsquo;s biggest mining hub has frozen new permits, saying its grid is full. The ceiling on Africa&rsquo;s hashrate is now physical, not political.",
  desc="Ethiopia halted new bitcoin-mining permits as power capacity hit its limit. The country hosts ~600 MW of mining and about 2.5% of global hashrate on hydro power.",
  hero=CF+"hf_20260822_105823_913ad955-0391-41f0-9fd3-fc25731b0567.png",
  alt="A large Ethiopian hydroelectric dam beside container mines with a lowered barrier gate, three-color linocut",
  cap="Network &amp; Mining &middot; Hydro built the boom; a full grid now caps it &middot; Illustration: The Bitcoin Beacon",
  body="""<p class="drop">Ethiopia, the country that turned surplus hydropower into Africa&rsquo;s largest bitcoin-mining industry, has stopped letting new miners in. Officials have halted the issuance of new mining permits, citing a grid that has reached the limit of what it can spare &mdash; a ceiling drawn not by ideology but by megawatts.</p>

<p>It is a striking reversal of posture for a state that spent two years courting the industry. Ethiopia legalized bitcoin mining while keeping ordinary crypto trading banned, betting that the dams could earn foreign currency by selling power to rigs. The bet paid: the sector grew fast and pulled in dollars the treasury badly needed.</p>

<h2>How big the boom got</h2>
<p>By 2026 Ethiopia had allocated on the order of <strong>600 MW</strong> to mining across roughly two dozen licensed firms, and analysts put the country at around <strong>2.5% of global hashrate</strong> &mdash; small worldwide, but the dominant share of Africa&rsquo;s. State reporting earlier tallied tens of millions of dollars in mining revenue over a single 10-month stretch. Much of that hashrate runs on power from the Grand Ethiopian Renaissance Dam, the continent&rsquo;s largest hydro project and the government&rsquo;s prized source of exportable electricity.</p>

<div class="pull">The dams that made Ethiopia a mining magnet are the same dams the government would rather point at homes, factories, and export lines.</div>

<h2>Why freeze now</h2>
<p>Because the same electrons have better-paid uses. Ethiopia still has millions of people without reliable power, an industrialization drive that needs energy, and neighbors willing to buy exported electricity at attractive rates. Every megawatt sold to a mining container is one not lighting a household or running a factory. Earlier in 2026 the government had already raised power prices on miners; the permit freeze is the blunter instrument &mdash; a cap on growth while the state decides how much of its grid it wants rented to hashrate.</p>

<h2>The spillover</h2>
<p>Miners frozen out of Ethiopia do not vanish; they relocate. The industry&rsquo;s defining trait is mobility &mdash; rigs chase the cheapest available watt across borders, as they did out of China in 2021 and into Paraguay and Central Asia after. Kenya, Zambia, Malawi, and other hydro- and geothermal-rich neighbors are the natural next stops, and operators already scouting African sites will read Ethiopia&rsquo;s ceiling as a signal to diversify.</p>

<p>For the broader network, a permit freeze in one country barely dents global hashrate. For Africa&rsquo;s mining map, it is a turning point: the continent&rsquo;s anchor market has told the industry there is a limit, and that limit is the grid itself.</p>

<p><em>Why it matters: even a government that wants bitcoin miners eventually hits a wall where domestic electricity is worth more than the coins &mdash; and Africa&rsquo;s biggest hub just found it.</em></p>""",
  sources="""        <li>Mariblock &mdash; <a href="https://www.mariblock.com/stories/ethiopia-halts-new-crypto-mining-permits-as-power-capacity-reaches-limit">Ethiopia halts new crypto mining permits as power capacity reaches limit</a></li>
        <li>Crypto Briefing &mdash; <a href="https://cryptobriefing.com/bitcoin-mining-rises-ethiopia/">Bitcoin mining activity rises in Ethiopia as country becomes unlikely crypto powerhouse</a></li>
        <li>CoinGeek &mdash; <a href="https://coingeek.com/africa-power-play-how-btc-mining-turns-wasted-energy-to-light/">Africa&rsquo;s power play: how BTC mining turns wasted energy to light</a></li>""",
  note="Capacity allocation, firm count and hashrate share per the sources above, 2026; figures vary by report. Informational only &mdash; not financial advice.",
))

# 4. Gulf / Saudi
stories.append(dict(
  slug="gulf-bank-buys-into-strategy-bitcoin",
  tagtext="Markets &amp; Institutions &middot; Manama",
  place="MANAMA",
  minread=5,
  title="A Gulf State Bank Buys Into Bitcoin&rsquo;s Biggest Buyer",
  standfirst="Gulf International Bank, owned by GCC governments, disclosed a stake in Strategy. It is a rounding error &mdash; and that is exactly why the direction, not the size, is the story.",
  desc="Gulf International Bank, owned by GCC governments led by Saudi Arabia, disclosed a $2.27M stake in Strategy (MSTR), the world's largest corporate bitcoin holder.",
  hero=CF+"hf_20260822_105824_fc9acfa1-5948-4863-b834-2e631f33e10d.png",
  alt="A Gulf banker studying a ledger in a marble hall with skyscrapers and date palms beyond, three-color linocut",
  cap="Markets &amp; Institutions &middot; Sovereign-linked Gulf capital takes a first, tiny step toward bitcoin &middot; Illustration: The Bitcoin Beacon",
  body="""<p class="drop">Gulf International Bank &mdash; owned by the governments of the Gulf Cooperation Council, with Saudi Arabia&rsquo;s sovereign wealth the largest shareholder &mdash; has disclosed a position in Strategy, the Michael Saylor-chaired company that holds more bitcoin than any other public firm. The size is almost comically small: about <strong>$2.27 million</strong>, held through the bank&rsquo;s UK arm, and trimmed by 365 shares in the most recent quarter.</p>

<p>On its own, the number means nothing. A $2 million line in a portfolio run by a Gulf state bank is a rounding error, likely passive, and easily reversed &mdash; the bank sold down, not up. Anyone reading it as a sovereign endorsement of bitcoin is over-reading a 13F.</p>

<h2>So why note it</h2>
<p>Because of who is holding it, and what it is a proxy for. Strategy is not a normal stock; it is a leveraged bitcoin vehicle, a way to take on bitcoin exposure inside an ordinary equity mandate. When capital linked to Gulf sovereigns shows up on that register &mdash; even in trace amounts &mdash; it is bitcoin exposure arriving through the side door of Wall Street rather than the front door of a treasury announcement.</p>

<div class="pull">Two million dollars is not the story. Whose two million dollars it is might be.</div>

<h2>The steelman for shrugging</h2>
<p>The skeptical read is strong and worth stating plainly. Large asset managers hold Strategy through index and quantitative strategies without any house view on bitcoin; a state bank&rsquo;s UK subsidiary appearing on the cap table may be nothing more than benchmark-tracking. The position shrank last quarter, the opposite of conviction buying. Read this way, the disclosure is noise dressed up as signal.</p>

<h2>The watch-this read</h2>
<p>The other read is about trajectory. Gulf states are among the largest pools of sovereign capital on earth, and their public exposure to bitcoin has been near zero. The interesting question is not whether $2.27 million matters &mdash; it doesn&rsquo;t &mdash; but whether it is the first visible pixel of a larger picture, the point at which sovereign-linked money stops treating bitcoin as untouchable and starts treating it as an allocation to be sized. One filing cannot answer that. It can only mark where to look next.</p>

<p><em>Why it matters: sovereign Gulf capital&rsquo;s bitcoin footprint is still a rounding error &mdash; but the first rounding errors are worth watching precisely because of whose balance sheet they sit on.</em></p>""",
  sources="""        <li>BitcoinTreasuries.net &mdash; <a href="https://bitcointreasuries.net/news/saudi-government-owned-bank-discloses-stake-in-strategy">Saudi Government-Owned Bank Discloses $2.27 Million Stake in Strategy</a></li>
        <li>BitcoinTreasuries.net &mdash; <a href="https://bitcointreasuries.net/news">Latest Bitcoin Treasury News</a> (holder rankings and 13F coverage)</li>""",
  note="Stake size and share change per 13F filing as reported by BitcoinTreasuries.net, August 2026. A 13F is a quarterly snapshot and may lag current positions. Informational only &mdash; not financial advice.",
))

# 5. The Take
stories.append(dict(
  slug="bitcoin-payments-custodial-rails-take",
  tagtext="Opinion &middot; The Take",
  place="GLOBAL",
  minread=5,
  title="The Register Says Bitcoin. The Settlement Says Dollars.",
  standfirst="The Global South&rsquo;s bitcoin payment boom runs on apps that convert to local cash on contact. That is a real win on fees &mdash; and an open question about what &lsquo;adoption&rsquo; means.",
  desc="Opinion: the Global South's bitcoin payment apps settle instantly to fiat, so users rarely hold a coin. Is that bitcoin adoption, or bitcoin as plumbing?",
  hero=CF+"hf_20260822_105823_50ab484a-afeb-44a1-957f-4231c1f1caea.png",
  alt="A market phone showing a bitcoin payment converting into banknotes at a custodial gateway, a locked vault behind, three-color linocut",
  cap="Opinion &middot; A rail nobody holds a coin on is bitcoin as plumbing, not money &middot; Illustration: The Bitcoin Beacon",
  body="""<p class="drop">Read this week&rsquo;s adoption stories back to back and a pattern jumps out. In Manila, a remittance lands as pesos. In Nairobi, a shopper taps a phone and the merchant is paid in shillings. Across Africa, a miner-backed app lets you spend and the till reads local currency. Bitcoin moves through every one of these transactions. In almost none of them does anyone actually hold it.</p>

<p>This is the quiet shape of the payments boom: custodial apps that accept bitcoin, convert it the instant it lands, and hand the user familiar money. The bitcoin exists for milliseconds, as a rail. It is a genuinely useful rail &mdash; and it is worth being honest about what it is and isn&rsquo;t.</p>

<h2>The case for celebrating</h2>
<p>Start with what&rsquo;s real. Fees fall. Settlement that took a day takes seconds. A worker sending money home keeps more of it; a vendor takes a payment that would have been impossible or expensive otherwise. For families living on remittances and thin margins, that is not abstract &mdash; it is grocery money. The bull case is sequencing: build the rails, let people transact, and holding comes later, once bitcoin is familiar and the option to keep it is one tap away. Rails first, savers second.</p>

<div class="pull">Bitcoin that exists for milliseconds, as a rail, is doing something real. It is just not doing the thing its believers actually promise.</div>

<h2>The case for caution</h2>
<p>Now the other side. A rail nobody holds a coin on is bitcoin as plumbing, not money. Custodial convert-to-fiat means the user never touches self-custody, never holds a bearer asset, and depends on a company that can freeze, delist, or be ordered to stop. Strip the branding and much of this is a better Western Union &mdash; cheaper, faster, and still someone else&rsquo;s balance sheet. The monetary promise of bitcoin &mdash; that you can hold value no one can inflate or seize &mdash; is exactly the part these apps route around.</p>

<p>There is a sharper irony in today&rsquo;s issue. In Kazakhstan, the entity accumulating actual bitcoin is the <em>state</em>, skimming coins from miners into a reserve. On the street, the citizen using a bitcoin app ends up holding pesos or shillings. The government keeps the bearer asset; the user gets the receipt.</p>

<h2>Where this leaves us</h2>
<p>Both things are true at once. The rails are a real, measurable improvement in people&rsquo;s financial lives, and they are not, by themselves, monetary adoption. The honest scorecard tracks two numbers, not one: how much value moves over bitcoin rails, and how many people choose to keep any of it. The first is climbing fast. The second is the bet the whole story rests on &mdash; and it is still just a bet.</p>

<p><em>Why it matters: confusing a payment rail for a monetary standard flatters the numbers. Bitcoin is winning the plumbing. Whether it wins the holding is a different, unsettled question.</em></p>""",
  sources="""        <li>BitPinas &mdash; <a href="https://bitpinas.com/news/pouch-neutronpay-canada-vietnam-partnership/">Pouch.ph &amp; Neutronpay open Lightning remittance corridors</a></li>
        <li>CryptoBriefing &mdash; <a href="https://cryptobriefing.com/bitcoin-lightning-payments-kenya-tando/">Bitcoin used for taxi, steak and coffee payments in Kenya via Lightning</a></li>
        <li>TFTC &mdash; <a href="https://www.tftc.io/kazakhstan-national-crypto-reserve-miner-tax-resolution-638">Kazakhstan Builds Crypto Reserve by Taxing Bitcoin Miners 10%</a></li>""",
  note="Opinion. Examples drawn from reporting cited above and in today&rsquo;s issue. Informational only &mdash; not financial advice.",
))

for s in stories:
    html = HEAD.format(date=DATE, **s)
    with open(os.path.join(OUT, s["slug"] + ".html"), "w") as f:
        f.write(html)
    print("wrote", s["slug"] + ".html")
print("DONE", len(stories))
