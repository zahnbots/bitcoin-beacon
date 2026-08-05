# -*- coding: utf-8 -*-
import os
OUT = "/sessions/charming-affectionate-davinci/mnt/bitcoin beacon/public/stories/2026-08-05"
IMG = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"

STYLE = """<style>
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
  .callout{ background:var(--wash); border:1px solid var(--line); border-radius:12px; padding:18px 20px; margin:26px 0; font-size:15px; }
  .callout h4{ margin:0 0 8px; font-size:12px; letter-spacing:1.2px; text-transform:uppercase; color:var(--accent); }
  .callout ul,.callout ol{ margin:0; padding-left:18px; } .callout li{ margin-bottom:6px; }
  .bottom{ border:1px solid var(--ink); border-radius:12px; padding:18px 20px; margin:30px 0; }
  .bottom h4{ margin:0 0 6px; font-size:12px; letter-spacing:1.4px; text-transform:uppercase; }
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

HEADER = """<body>
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
  (function(){var b=document.querySelector('.nav .menu-btn');if(b){b.addEventListener('click',function(){var n=b.closest('.nav');var open=n.classList.toggle('open');b.setAttribute('aria-expanded',open?'true':'false');});}})();
  </script>
"""

FOOTER = """  <div class="subscribe" id="subscribe"><div class="box">
    <h3>The world&rsquo;s bitcoin headlines, in your inbox every morning.</h3>
    <p>Free. Five minutes. No hype.</p>
    <a class="btn" href="/subscribe.html">Subscribe free</a>
  </div></div>

  <footer>THE BITCOIN BEACON &bull; The daily record of Bitcoin's global adoption &bull; Informational only &mdash; not financial advice</footer>

<!-- subscribe modal (site-wide) -->
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
</script>

</body>
</html>
"""

def page(slug, title, desc, tagcolor, crumb, standfirst, metaline, hero, alt, cap, body):
    hero_url = IMG + hero
    colorattr = (' style="color:%s;"' % tagcolor) if tagcolor else ''
    head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="%(desc)s">
<link rel="canonical" href="https://thebitcoinbeacon.com/stories/2026-08-05/%(slug)s">
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
<meta property="og:image" content="%(hero_url)s">
<meta property="og:url" content="https://thebitcoinbeacon.com/stories/2026-08-05/%(slug)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(hero_url)s">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"NewsArticle","headline":"%(title)s","description":"%(desc)s","image":["%(hero_url)s"],"datePublished":"2026-08-05","dateModified":"2026-08-05","mainEntityOfPage":"https://thebitcoinbeacon.com/stories/2026-08-05/%(slug)s","author":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com"},"publisher":{"@type":"Organization","name":"The Bitcoin Beacon","url":"https://thebitcoinbeacon.com","logo":{"@type":"ImageObject","url":"https://thebitcoinbeacon.com/assets/masthead-ink.png"}}}</script>
<title>%(title)s &mdash; The Bitcoin Beacon</title>
""" % dict(desc=desc, slug=slug, title=title, hero_url=hero_url)

    mid = """
  <div class="crumb"><span class="tag"%(colorattr)s>%(crumb)s</span></div>
  <div class="wrap">
    <h1 class="title">%(title)s</h1>
    <p class="standfirst">%(standfirst)s</p>
    <div class="meta">%(metaline)s</div>
  </div>
  <div class="hero"><div class="heroart">
    <img src="%(hero_url)s" alt="%(alt)s">
    <div class="cap">%(cap)s &mdash; Illustration: The Bitcoin Beacon</div>
  </div></div>
  <div class="wrap body">
%(body)s
  </div>
""" % dict(colorattr=colorattr, crumb=crumb, title=title, standfirst=standfirst,
           metaline=metaline, hero_url=hero_url, alt=alt, cap=cap, body=body)

    html = head + STYLE + "\n</head>\n" + HEADER + mid + FOOTER
    with open(os.path.join(OUT, slug + ".html"), "w") as f:
        f.write(html)
    print("wrote", slug)


# ---------------- STORY 2: QUANTUM ----------------
body_quantum = """
    <p class="drop">Tom Lee spends most of his television time telling investors why bitcoin goes up. On August 5 he went on CNBC to explain how it could go to zero. Quantum computers, the Fundstrat co-founder and head of research said, could break bitcoin&rsquo;s cryptography as soon as <strong>2028</strong> &mdash; and the network, he argued, has not agreed on how to stop them.</p>

    <p>&ldquo;Google thinks all encryption could break by 2028,&rdquo; Lee said, adding that the risk was specific to bitcoin&rsquo;s signature scheme and that the community &ldquo;has not come up with a consensus on how to prevent it.&rdquo; Coming from a reliable bull, the warning traveled fast. It also compressed a real, slow-moving engineering problem into a scary round number.</p>

    <h2>What quantum actually threatens</h2>
    <p>Bitcoin leans on two kinds of math. Its mining and its addresses use SHA-256, a hashing algorithm that quantum computers weaken only modestly. The vulnerable part is the other kind: the elliptic-curve digital signature (ECDSA) that proves you own the coins in an address. A large, error-corrected quantum computer running Shor&rsquo;s algorithm could, in principle, derive a private key from a public key &mdash; and spend those coins.</p>

    <p>The catch is the phrase &ldquo;large, error-corrected.&rdquo; No such machine exists. IBM&rsquo;s chief executive, Arvind Krishna, has told CNBC that quantum will start affecting revenue around <strong>2028&ndash;2029</strong>, and the company has demonstrated what it calls &ldquo;trusted quantum advantage&rdquo; on a roughly 70-qubit system &mdash; impressive, and still orders of magnitude short of the millions of physical qubits most estimates require to break ECDSA.</p>

    <div class="callout">
      <h4>The number that changed the mood</h4>
      <p>In March, Google Quantum AI researchers cut the estimated resources needed to break elliptic-curve cryptography by roughly <strong>20-fold</strong>, to under 500,000 qubits. That did not build the machine &mdash; but it moved the finish line closer, which is why 2026 is the year the quantum debate stopped being theoretical.</p>
    </div>

    <h2>Why bitcoin is the loud example</h2>
    <p>Every bank, government, and messaging app relies on the same public-key cryptography, so quantum threatens far more than one asset. Bitcoin is simply the most legible target: its ledger is public, its rewards are enormous, and its exposure is measurable. By common estimates, more than <strong>a third of all bitcoin</strong> sits in addresses whose public keys are already visible on-chain &mdash; including, famously, the roughly one million coins attributed to Satoshi Nakamoto, which will never move to safety because no one will move them.</p>

    <p>That is the asymmetry Lee is pointing at. A bank can quietly migrate its systems to post-quantum algorithms on a schedule. Bitcoin has to do it in the open, by consensus, across millions of self-interested holders &mdash; and it cannot force anyone to upgrade.</p>

    <div class="pull">A bank can migrate quietly. Bitcoin has to do it in the open, by consensus, in front of everyone.</div>

    <h2>The fix already has drafts</h2>
    <p>Lee&rsquo;s claim that there is &ldquo;no consensus&rdquo; is true and incomplete. There is no activated solution, but there is active work. Developers have circulated proposals to add post-quantum signature schemes to bitcoin and, in some drafts, to eventually freeze or force-migrate coins in exposed addresses &mdash; each a contentious soft fork that would take years to debate and deploy. Galaxy Digital has funded a quantum-readiness effort; custodians such as BitGo have begun scoring wallets by their quantum exposure. The tools are early. They are not absent.</p>

    <p>His side note &mdash; that a break would not hurt Ethereum or Solana &mdash; is the weakest part of the pitch. Those chains use the same elliptic-curve family bitcoin does; a working cryptographic attack would threaten most of the industry at once, not spare the competitors. The quantum threat, if it arrives, is an internet problem wearing a bitcoin costume.</p>

    <h2>What to watch</h2>
    <p>The signal is not the price reaction, which faded within the day. It is the pace of two clocks: the qubit count on real hardware, and the progress of post-quantum proposals through bitcoin&rsquo;s glacial governance. The White House has said it wants a working quantum computer by 2028 and federal systems on post-quantum cryptography by 2030. Bitcoin has roughly the same window and a harder coordination problem. It also has the strongest incentive ever devised for millions of people to move their coins to safety: keeping them.</p>

    <p><em>Why it matters: quantum won&rsquo;t break bitcoin in 2026, but the timeline for the fix is now shorter than the timeline for the threat &mdash; and closing that gap is a governance test, not just a math one.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Pete Rizzo (X) &mdash; <a href="https://x.com/pete_rizzo_">Tom Lee&rsquo;s CNBC remarks on quantum and bitcoin, reported live</a></li>
        <li>CoinDesk &mdash; <a href="https://www.coindesk.com/markets/2026/07/27/crypto-is-the-canary-in-the-coal-mine-for-the-quantum-computing-threat">Bitcoin is the canary in the coal mine for the quantum threat</a></li>
        <li>CoinDesk &mdash; <a href="https://www.coindesk.com/markets/2026/03/31/quantum-computers-could-break-crypto-wallet-encryption-with-just-10-000-qubits-researchers-say">Google research slashes qubits needed to break ECC</a></li>
        <li>BeInCrypto &mdash; <a href="https://beincrypto.com/ibm-quantum-timeline-bitcoin-notice/">Bitcoin&rsquo;s $437 billion quantum exposure meets IBM&rsquo;s 2028 deadline</a></li>
        <li>Bitcoin Foundation &mdash; <a href="https://bitcoinfoundation.org/news/bitcoin/quantum-advantage-bitcoin/">IBM claims quantum advantage &mdash; bitcoin not ready</a></li>
      </ol>
    </div>

    <p class="note">Editor&rsquo;s note: qubit-count and timeline estimates vary widely between researchers and are moving targets; Tom Lee&rsquo;s remarks are his own forecast, not a technical claim of a working attack. Nothing here is financial advice.</p>
"""

page("tom-lee-quantum-bitcoin-2028",
     "Tom Lee Says Quantum Could Break Bitcoin by 2028",
     "Fundstrat&rsquo;s Tom Lee told CNBC a quantum computer could crack bitcoin&rsquo;s cryptography by 2028. The claim is early &mdash; but the clock behind the post-quantum fix is real.",
     "#b5601f", "Network &amp; Mining &middot; New York",
     "The Fundstrat strategist told CNBC a quantum computer could crack bitcoin&rsquo;s cryptography within two years. The claim is early &mdash; but the clock behind it is real.",
     "<b>By The Bitcoin Beacon</b> &middot; NEW YORK, USA &middot; August 5, 2026 &middot; 7 min read",
     "hf_20260805_111936_d1c70993-5051-4245-bfe9-a903c0ec53eb.png",
     "A towering quantum computer looming over a small padlock shaped like a bitcoin coin as an engineer gazes up, linocut",
     "Network &amp; Mining &middot; The quantum question",
     body_quantum)


# ---------------- STORY 3: US TREASURY ----------------
body_us = """
    <p class="drop">The people who wrote America&rsquo;s bitcoin policy are leaving the building. Tyler Williams, the senior Treasury official who ran digital-asset policy and advised Secretary Scott Bessent, has resigned, with his last day at the end of the week. His exit lands as the administration&rsquo;s signature crypto legislation stalls in Congress &mdash; and it is not the only departure.</p>

    <p>Williams was, by Washington&rsquo;s own account, central to the effort. He helped shape the Strategic Bitcoin Reserve created by executive order in March 2025 and was described inside Treasury as instrumental to the drive to make the United States, in the administration&rsquo;s phrase, the &ldquo;crypto capital of the world.&rdquo; He is said to be returning to the private sector.</p>

    <h2>A bill running out of runway</h2>
    <p>His departure coincides with the Digital Asset Market Clarity Act &mdash; the CLARITY Act &mdash; stalling ahead of Congress&rsquo;s August recess. The market-structure bill, meant to divide oversight of digital assets between the SEC and CFTC, has snagged on disagreements over ethics provisions for federal officials. One prediction market now puts the odds of CLARITY passing this session at around <strong>27%</strong>.</p>

    <p>Williams is not leaving alone. Reporting this summer has tracked a cluster of exits across the SEC, the Senate, and the White House among the officials who had driven crypto policy &mdash; a brain drain at exactly the moment the agenda needs shepherds through a divided Congress.</p>

    <div class="pull">The reserve exists on paper. What it does next depends on people who are now leaving.</div>

    <h2>A reserve that isn&rsquo;t buying</h2>
    <p>For bitcoin holders, the substance sits in what the reserve is and is not. The Strategic Bitcoin Reserve currently holds an estimated <strong>328,000-plus BTC</strong> &mdash; roughly 1.6% of all bitcoin &mdash; accumulated almost entirely through law-enforcement seizures, including Silk Road and the Bitfinex-hack recovery. It is a stockpile of forfeited coins, not a program of open-market purchases.</p>

    <p>Whether it becomes one is the open question. Legislation reintroduced as the American Reserves Modernization Act would authorize Treasury to buy up to 200,000 BTC a year for five years and lock the holdings for two decades; supporters have floated a first purchase as early as the fourth quarter of 2026. But Bessent has publicly said the government will not buy more bitcoin to expand the reserve &mdash; a direct contradiction of the legislative ambition, and a gap that the departing staff were supposed to help resolve.</p>

    <h2>Why the personnel is the story</h2>
    <p>Executive orders establish intent; statutes and staff execute it. A reserve that only holds seized coins costs nothing and does little. A reserve that buys on the open market would make the United States the first major sovereign to actively accumulate bitcoin as a reserve asset &mdash; a decision with real budget and market consequences that needs congressional authority and civil servants to implement. Losing the architects while the enabling law is stuck pushes any such move further out.</p>

    <p>None of this touches the coins already held; seized bitcoin does not walk out with a resigning adviser. What it touches is momentum. The maximalist case for a state bitcoin reserve was always that policy would compound &mdash; order, then law, then purchases. This week that compounding looks slower.</p>

    <h2>What to watch</h2>
    <p>Three things: whether CLARITY is revived after the recess or dies for the session; who replaces Williams and whether the successor shares his brief; and whether Bessent&rsquo;s &ldquo;no new purchases&rdquo; line survives contact with a Congress that keeps drafting bills to the contrary. The reserve is not going anywhere. Its trajectory just lost some of its engine.</p>

    <p><em>Why it matters: America already owns a big pile of bitcoin &mdash; but whether it ever buys more depends on laws and staff, and both just got shakier.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Cointelegraph &mdash; <a href="https://cointelegraph.com/news/bessent-top-crypto-adviser-tyler-williams-leaves-us-treasury-report">Bessent&rsquo;s top crypto adviser Tyler Williams leaves US Treasury</a></li>
        <li>The Crypto Times &mdash; <a href="https://www.cryptotimes.io/2026/08/03/bessents-top-crypto-adviser-tyler-williams-exits-treasury-as-clarity-stalls/">Tyler Williams exits Treasury as CLARITY stalls</a></li>
        <li>CryptoSlate &mdash; <a href="https://cryptoslate.com/us-crypto-regulation-loses-key-washington-allies/">Odds of CLARITY passing sink to 27% as key allies quit</a></li>
        <li>TheStreet &mdash; <a href="https://www.thestreet.com/crypto/markets/white-house-official-reveals-new-details-on-bitcoin-reserve-">White House official reveals new details on the bitcoin reserve</a></li>
        <li>CoinCodex &mdash; <a href="https://coincodex.com/article/71505/us-treasury-secretary-rules-out-bitcoin-purchases-for-strategic-reserve">Treasury Secretary rules out new bitcoin purchases for the reserve</a></li>
      </ol>
    </div>

    <p class="note">Editor&rsquo;s note: reserve holdings are estimates based on tracked government wallets and seizure disclosures; personnel details reflect reporting on Treasury staffing. Nothing here is financial advice.</p>
"""

page("us-treasury-bitcoin-policy-chief-resigns",
     "Treasury&rsquo;s Bitcoin-Policy Chief Resigns as CLARITY Stalls",
     "Tyler Williams, the Treasury adviser who helped design America&rsquo;s Strategic Bitcoin Reserve, is leaving as the CLARITY Act stalls &mdash; slowing the push toward open-market government bitcoin buys.",
     "#127a5b", "Nation-States &middot; Washington",
     "Tyler Williams, the Treasury adviser who helped design America&rsquo;s Strategic Bitcoin Reserve, is leaving &mdash; and the market-structure bill he championed has stalled before the August recess.",
     "<b>By The Bitcoin Beacon</b> &middot; WASHINGTON, USA &middot; August 5, 2026 &middot; 6 min read",
     "hf_20260805_111940_6a025f20-5002-4eff-95fe-93501a4bf3a5.png",
     "A lone official with a briefcase walking down the steps of the US Treasury, a bitcoin emblem carved on the pediment, linocut",
     "Nation-States &middot; Washington",
     body_us)


# ---------------- STORY 4: BITDEER ----------------
body_bitdeer = """
    <p class="drop">Bitdeer used to hold bitcoin. As of this month it holds none. The Singapore-based, Nasdaq-listed miner liquidated its entire treasury &mdash; selling <strong>1,132.9 BTC</strong> down to zero &mdash; and put the proceeds toward expansion, note repurchases, and a push into artificial-intelligence computing. A company built to produce bitcoin decided it would rather spend it.</p>

    <p>The final tranche was about 943 coins of reserves plus roughly 190 freshly mined, according to disclosures parsed by trackers. The result is a milestone with a message: Bitdeer is now the largest publicly traded self-mining company holding <strong>no bitcoin at all</strong> on its balance sheet.</p>

    <h2>Why a miner stops hoarding</h2>
    <p>The backdrop is brutal economics. Mining profitability has scraped all-time lows in 2026 as the post-halving block reward, a record-high network hashrate near 955 exahashes per second, and rising power costs squeeze margins from three directions. When each coin costs more to produce and the price drifts sideways, holding inventory becomes a luxury. Selling production &mdash; and sometimes reserves &mdash; becomes survival.</p>

    <p>Bitdeer&rsquo;s pivot has a direction as well as a cause. The company has been redeploying capital and power toward AI and high-performance computing, the same trade that Core Scientific, TeraWulf, and others have chased as data-center tenants outbid block rewards for electricity. Its own SEALMINER rigs pushed self-mining hashrate to <strong>63.2 EH/s</strong>, edging past Marathon&rsquo;s 60.4 &mdash; even as it sold the coins those machines produced.</p>

    <div class="pull">A company built to produce bitcoin decided it would rather spend it.</div>

    <h2>Not everyone is selling</h2>
    <p>The move is not the whole industry&rsquo;s verdict. In the same week, American Bitcoin reported mining a record 932 BTC in the second quarter and growing its treasury 14% to about 8,002 coins &mdash; even as the spot price fell 12%. One miner is liquidating to fund a pivot; another is stacking through the downturn. The split is the point: &ldquo;miner&rdquo; is no longer a single strategy.</p>

    <p>For the network, a miner selling coins is not a threat; it is the mechanism working as designed. Bitcoin&rsquo;s security does not depend on miners holding what they earn &mdash; only on their competing to produce blocks. Bitdeer&rsquo;s hashrate stayed on the network. Only its balance sheet changed.</p>

    <h2>The signal for holders</h2>
    <p>Two readings compete. The bearish one: forced miner selling adds steady supply into a soft market, and a marquee miner abandoning its own product is a vote of low conviction. The bullish one: coins are simply migrating from operators with power bills to buyers with time horizons &mdash; the same rotation, from miners and funds toward long-term holders and corporates, that has defined 2026.</p>

    <p>What is not in dispute is the strategic drift. The biggest miners increasingly see themselves as energy-and-compute companies that happen to run bitcoin machines, ready to point megawatts at whichever workload pays. That makes them more resilient. It also loosens the old identity in which a miner was bitcoin&rsquo;s most committed believer.</p>

    <p><em>Why it matters: when the companies that make bitcoin stop holding it, the coins don&rsquo;t vanish &mdash; they move to owners who will, and the miners quietly become AI landlords.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>The Block &mdash; <a href="https://www.theblock.co/post/390719/bitdeers-bitcoin-treasury-drops-to-zero-after-miner-liquidates-remaining-943-btc">Bitdeer&rsquo;s bitcoin treasury drops to zero after liquidating 943 BTC</a></li>
        <li>Cointelegraph &mdash; <a href="https://cointelegraph.com/news/bitdeer-sells-bitcoin-treasury-zero-holdings">Bitcoin miner Bitdeer liquidates entire BTC treasury</a></li>
        <li>Bitcoin Magazine &mdash; <a href="https://bitcoinmagazine.com/news/bitdeer-btdr-dumps-bitcoin-treasury">Bitdeer ($BTDR) sells all bitcoin after eight-week drawdown</a></li>
        <li>CCN &mdash; <a href="https://www.ccn.com/news/crypto/bitdeer-liquidates-entire-bitcoin-treasury-as-mining-margins-tighten-will-other-crypto-miners-follow-in-2026/">Bitdeer liquidates entire treasury as mining margins tighten</a></li>
        <li>TFTC &mdash; <a href="https://www.tftc.io/american-bitcoin-q2-2026-results-932-btc-mined-treasury">American Bitcoin Q2 2026: 932 BTC mined, 8,002 BTC treasury</a></li>
      </ol>
    </div>

    <p class="note">Editor&rsquo;s note: coin totals reflect company disclosures aggregated by third-party trackers and may be restated in official filings; hashrate figures are company-reported. Nothing here is financial advice.</p>
"""

page("bitdeer-liquidates-bitcoin-treasury",
     "Bitdeer Sold Every Bitcoin It Held",
     "Nasdaq-listed miner Bitdeer liquidated its entire 1,133-coin bitcoin treasury to zero to fund an AI pivot &mdash; the largest self-mining company now holding no BTC on its balance sheet.",
     "#7a4dd1", "Markets &amp; Institutions &middot; Singapore",
     "The Singapore-listed miner liquidated its entire 1,133-coin treasury to zero to fund an AI pivot &mdash; a bet that building the machines beats holding the money they make.",
     "<b>By The Bitcoin Beacon</b> &middot; SINGAPORE &middot; August 5, 2026 &middot; 6 min read",
     "hf_20260805_111945_c1e4dc0a-5875-46fc-aaa9-c9e491fecae1.png",
     "Workers wheeling an empty steel vault out of a bitcoin mining hall as a single coin rolls away across the floor, linocut",
     "Markets &amp; Institutions &middot; Singapore",
     body_bitdeer)


# ---------------- STORY 5: SAUDI ----------------
body_saudi = """
    <p class="drop">In Riyadh, the fastest-moving bitcoin market in the Gulf is not a sovereign fund or a state miner. It is a generation with smartphones. Saudi Arabia has become the region&rsquo;s quickest-growing digital-asset economy, and the demand is running well ahead of the rules meant to govern it.</p>

    <p>The clearest figure comes from Chainalysis, which found Saudi Arabia grew crypto transaction value by roughly <strong>153% year over year</strong> in its most recent regional survey &mdash; the fastest in the Middle East and North Africa &mdash; on an estimated <strong>$47 billion</strong> of inflows. An important caveat sits inside that number: it counts all crypto, not bitcoin alone. But in Gulf portfolios bitcoin remains the anchor asset, the thing bought first and held longest, and the growth curve is the point.</p>

    <h2>A young, wired market</h2>
    <p>Demographics do the heavy lifting. Analysts estimate around <strong>3 million Saudis</strong> now hold or trade digital assets, concentrated among 18-to-35-year-olds in a country where smartphone penetration tops 95%. This is not a diaspora sending remittances home or a population fleeing a collapsing currency &mdash; the riyal is pegged and stable. It is a young, connected middle class treating bitcoin as a normal line in a savings portfolio.</p>

    <p>That makes Saudi adoption a different species from the stories the Beacon usually files. In Lagos or Buenos Aires, bitcoin is a hedge against monetary failure. In Riyadh it is discretionary demand &mdash; closer to how a young professional in Seoul or Singapore treats it. The driver is not desperation. It is access, phones, and yield-seeking.</p>

    <div class="pull">This is not a population fleeing a collapsing currency. It is a young middle class treating bitcoin as normal savings.</div>

    <h2>Policy chasing the crowd</h2>
    <p>Officially, the ground is still soft. The Saudi Central Bank has long been cautious on crypto and has not enacted a comprehensive framework for trading and custody, even as it explores blockchain and central-bank digital-currency work under the Vision 2030 modernization plan. Much of the activity therefore runs through global exchanges and peer-to-peer channels rather than a licensed domestic market &mdash; the familiar pattern in which citizens adopt first and regulators formalize later.</p>

    <p>The trajectory points one way. Industry projections cited across the Gulf see the Saudi digital-asset market expanding toward roughly <strong>$50 billion by 2034</strong> as Vision 2030 pulls finance and technology into the center of the economy. Whether Riyadh writes rules that channel that demand onshore &mdash; as the UAE has aggressively done &mdash; or lets it keep flowing offshore is the decision that will shape the next few years.</p>

    <h2>What to watch</h2>
    <p>Two markers matter: whether the central bank moves from study to a licensing regime for exchanges and custody, and whether Saudi capital shows up in bitcoin specifically rather than the broader crypto basket the headline data lumps together. A young market growing at triple digits is a prize. The country that regulates it well gets to keep the activity at home.</p>

    <p><em>Why it matters: the Gulf&rsquo;s bitcoin story is usually about sovereigns hoarding coins &mdash; here it&rsquo;s ordinary young savers, and their demand is arriving faster than the rulebook.</em></p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>Chainalysis &mdash; <a href="https://www.chainalysis.com/blog/middle-east-north-africa-crypto-adoption-2024/">MENA: regulatory momentum and adoption; Saudi Arabia&rsquo;s 153% growth</a></li>
        <li>Cryptopolitan &mdash; <a href="https://www.cryptopolitan.com/saudi-arabias-crypto-market-to-hit-50-billion/">Saudi crypto market seen reaching $50 billion by 2034 under Vision 2030</a></li>
        <li>BingX &mdash; <a href="https://bingx.com/en/blog/article/the-state-of-crypto-in-ksa-trends-and-opportunities-in-2025">The state of crypto in KSA: trends and opportunities</a></li>
        <li>Disruption Banking &mdash; <a href="https://www.disruptionbanking.com/2025/11/11/how-the-philippines-became-asias-crypto-giant/">Gulf and Asia adoption context</a></li>
      </ol>
    </div>

    <p class="note">Editor&rsquo;s note: headline adoption figures from Chainalysis measure all digital assets, not bitcoin alone, and cover the July 2023&ndash;June 2024 survey window; bitcoin is the largest single asset held but is not separately broken out. Nothing here is financial advice.</p>
"""

page("saudi-arabia-youth-bitcoin-gulf",
     "Young Saudis Are Buying Bitcoin Faster Than the Rest of the Gulf",
     "Saudi Arabia is the Gulf&rsquo;s fastest-growing digital-asset market &mdash; up ~153% year over year on $47B of inflows &mdash; driven by under-35s with smartphones, running ahead of the rules.",
     None, "Money &amp; Macro &middot; Riyadh",
     "Saudi Arabia is the Gulf&rsquo;s fastest-growing digital-asset market, driven by under-35s with smartphones &mdash; adoption running well ahead of the rules meant to govern it.",
     "<b>By The Bitcoin Beacon</b> &middot; RIYADH, Saudi Arabia &middot; August 5, 2026 &middot; 5 min read",
     "hf_20260805_111948_413208e5-af2e-4707-823c-81ba9f77e305.png",
     "A young Saudi man checking bitcoin on a smartphone in a Riyadh market with the city skyline and date palms behind, linocut",
     "Money &amp; Macro &middot; Riyadh",
     body_saudi)


# ---------------- STORY 6: THE TAKE ----------------
body_take = """
    <p class="drop">Bitcoin dies on a schedule. It died at Mt. Gox in 2014, when the biggest exchange collapsed and took the confidence with it. It died each time China banned it &mdash; in 2013, in 2017, definitively in 2021. It was going to die when Wall Street wrapped it in ETFs and, we were told, financialized the life out of it. This week it is dying of quantum computers. The obituaries are well written and, so far, all early.</p>

    <p>Tom Lee&rsquo;s warning that a quantum machine could break bitcoin by 2028 is the newest entry in a long genre. The genre has a rhythm: a genuine risk appears, a credible voice attaches a round-number deadline, and the deadline does the work the evidence can&rsquo;t. The pattern of being wrong is not proof this time is wrong. But it earns the pattern a hearing.</p>

    <h2>Why the network keeps not dying</h2>
    <p>The unglamorous answer is incentives. Bitcoin has no chief executive to panic and no marketing department to reassure, but it does have a few hundred thousand people with money on the line and an open process for changing the rules when enough of them agree. That process is slow and ugly &mdash; see the years it took to activate SegWit and Taproot &mdash; and it has, so far, shipped every upgrade the network actually needed. Threats that carry a financial incentive to fix tend to get fixed.</p>

    <div class="pull">The pattern of being wrong is not proof this time is wrong. But it earns the pattern a hearing.</div>

    <h2>The steelman: this one is different</h2>
    <p>Here is where honesty requires a pause, because quantum is not China. A regulatory ban is a market event; a cryptographic break is a physics event, and physics does not negotiate. More than a third of all bitcoin sits in addresses with exposed public keys, including coins that can never be moved to safety because their owners are gone. A migration to quantum-resistant signatures is not a patch; it is a contentious, multi-year soft fork that has to herd millions of self-interested holders through an upgrade none of them can be forced to take. If Q-Day arrives before that migration finishes, the loss would be real and unfixable for the coins left behind.</p>

    <p>So the quantum warning deserves better than the reflexive eye-roll that greets the hundredth &ldquo;bitcoin is dead.&rdquo; It is the first killer in a while that could, in principle, kill.</p>

    <h2>Why the odds still favor the network</h2>
    <p>But look at the two clocks. The threat clock runs on hardware that is still orders of magnitude short of breaking a private key, advancing fast but from far away. The fix clock runs on proposals that already exist &mdash; post-quantum signature schemes in draft, a Galaxy-funded readiness effort, custodians already scoring wallets by exposure &mdash; and on the strongest migration incentive ever built, which is that every holder who moves gets to keep their money. Governments are giving themselves until 2030 to go post-quantum. Bitcoin has the same window and, uniquely, a few hundred billion dollars of reasons for its users to hurry.</p>

    <p>The honest forecast is not &ldquo;quantum is nothing.&rdquo; It is that quantum is a deadline, and bitcoin&rsquo;s entire history is a record of hitting deadlines late, ugly, and in time. Bet against that if you like. Just remember how the last dozen obituaries aged.</p>

    <p class="sig" style="font-family:'Inter',sans-serif; font-size:13px; color:#6b6459; border-top:1px solid #e7e3da; padding-top:14px; margin-top:22px;">The Take is The Bitcoin Beacon&rsquo;s opinion column. Arguments here are ours; the reporting they lean on is linked below.</p>

    <div class="sources">
      <h4>Sources</h4>
      <ol>
        <li>CoinDesk &mdash; <a href="https://www.coindesk.com/markets/2026/07/27/crypto-is-the-canary-in-the-coal-mine-for-the-quantum-computing-threat">Bitcoin is the canary in the coal mine for the quantum threat</a></li>
        <li>BeInCrypto &mdash; <a href="https://beincrypto.com/ibm-quantum-timeline-bitcoin-notice/">Bitcoin&rsquo;s $437 billion quantum exposure meets IBM&rsquo;s 2028 deadline</a></li>
        <li>The Bitcoin Beacon &mdash; <a href="https://thebitcoinbeacon.com/stories/2026-07-23/galaxy-bitcoin-quantum-readiness-initiative">Galaxy puts $5 million toward quantum-proofing bitcoin</a></li>
        <li>The Bitcoin Beacon &mdash; <a href="https://thebitcoinbeacon.com/stories/2026-07-10/bitgo-quantum-custody">BitGo gives bitcoin wallets a quantum risk score</a></li>
      </ol>
    </div>

    <p class="note">Editor&rsquo;s note: this is opinion, and quantum timelines are contested estimates, not settled facts. Nothing here is financial advice.</p>
"""

page("bitcoin-annual-obituary-quantum-take",
     "Bitcoin&rsquo;s Obituary Is Due Again. This Time It&rsquo;s Quantum.",
     "Every cycle produces a thing that will finally kill bitcoin &mdash; Mt. Gox, China, the ETFs, now quantum. The obituary writers keep being early. Quantum might make them right &mdash; here&rsquo;s why the odds still favor the network.",
     "#c0392b", "The Take &middot; Opinion",
     "Every cycle produces a thing that will finally kill bitcoin &mdash; Mt. Gox, China, the ETFs, now quantum computers. The obituary writers keep being early. Quantum may make them right.",
     "<b>By The Bitcoin Beacon</b> &middot; Opinion &middot; August 5, 2026 &middot; 5 min read",
     "hf_20260805_112344_8d99985a-a5e4-4a81-beef-e4616aa941b7.png",
     "A printing press rolling out a blank page as a bitcoin phoenix rises from carved flames, linocut",
     "The Take &middot; Opinion",
     body_take)

print("DONE")
