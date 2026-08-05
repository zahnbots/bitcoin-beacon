# -*- coding: utf-8 -*-
import re, io
P = "/sessions/charming-affectionate-davinci/mnt/bitcoin beacon/public/index.html"
IMG = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"
s = io.open(P, encoding="utf-8").read()

# 1) strap date
s = s.replace("Tuesday, August 4, 2026", "Wednesday, August 5, 2026")

# 2) main column
main = '''    <!-- main column -->
    <div>
      <a class="hero" href="stories/2026-08-05/guatemala-bitcoin-lake-panajachel.html">
        <div class="heroart"><img fetchpriority="high" width="1376" height="768" src="%(img)shf_20260805_112248_feff985c-c4a0-43eb-ae78-c7f8213d2d19.png" style="width:100%%;height:100%%;object-fit:cover;display:block;" alt="A Maya market vendor accepts a bitcoin phone payment on the shore of Lake Atitlan, volcanoes behind, linocut"></div>
        <span class="tag" style="margin-top:14px;color:#127a5b;">On the Ground &middot; Panajachel</span>
        <h1>A Guatemalan Lake Town Runs on Bitcoin</h1>
        <p>On Lake Atitl&aacute;n, roughly 80 shops take bitcoin over Lightning &mdash; and a miner fed on fried-food grease turns the town&rsquo;s waste oil into hashrate.</p>
        <div class="by">By The Bitcoin Beacon &middot; 6 min read</div>
      </a>

      <div class="row">
        <div class="rowhd">Today&rsquo;s Dispatches</div>
        <div class="cards">
          <a class="story" href="stories/2026-08-05/tom-lee-quantum-bitcoin-2028.html">
            <img src="%(img)shf_20260805_111936_d1c70993-5051-4245-bfe9-a903c0ec53eb.png" loading="lazy" decoding="async" width="1376" height="768" style="width:100%%;height:130px;object-fit:cover;border-radius:9px;margin-bottom:10px;display:block;" alt="A towering quantum computer over a bitcoin padlock as an engineer looks up, linocut">
            <span class="tag" style="color:#b5601f;">Network &amp; Mining &middot; New York</span>
            <h3>Tom Lee Says Quantum Could Break Bitcoin by 2028</h3>
            <p>The Fundstrat strategist warned CNBC of a 2028 &ldquo;Q-Day.&rdquo; The threat is real but early &mdash; and the fix is already in draft.</p></a>
          <a class="story" href="stories/2026-08-05/us-treasury-bitcoin-policy-chief-resigns.html">
            <img src="%(img)shf_20260805_111940_6a025f20-5002-4eff-95fe-93501a4bf3a5.png" loading="lazy" decoding="async" width="1376" height="768" style="width:100%%;height:130px;object-fit:cover;border-radius:9px;margin-bottom:10px;display:block;" alt="A lone official with a briefcase leaving the US Treasury, a bitcoin emblem on the pediment, linocut">
            <span class="tag" style="color:#127a5b;">Nation-States &middot; Washington</span>
            <h3>Treasury&rsquo;s Bitcoin-Policy Chief Resigns as CLARITY Stalls</h3>
            <p>The adviser who helped build America&rsquo;s bitcoin reserve is out &mdash; and the plan to buy more just lost its engine.</p></a>
          <a class="story" href="stories/2026-08-05/bitdeer-liquidates-bitcoin-treasury.html">
            <img src="%(img)shf_20260805_111945_c1e4dc0a-5875-46fc-aaa9-c9e491fecae1.png" loading="lazy" decoding="async" width="1376" height="768" style="width:100%%;height:130px;object-fit:cover;border-radius:9px;margin-bottom:10px;display:block;" alt="Workers wheeling an empty steel vault out of a bitcoin mining hall as a coin rolls away, linocut">
            <span class="tag" style="color:#7a4dd1;">Markets &amp; Institutions &middot; Singapore</span>
            <h3>Bitdeer Sold Every Bitcoin It Held</h3>
            <p>The listed miner liquidated its entire 1,133-coin treasury to zero to fund an AI pivot. Mining margins are at record lows.</p></a>
          <a class="story" href="stories/2026-08-05/saudi-arabia-youth-bitcoin-gulf.html">
            <img src="%(img)shf_20260805_111948_413208e5-af2e-4707-823c-81ba9f77e305.png" loading="lazy" decoding="async" width="1376" height="768" style="width:100%%;height:130px;object-fit:cover;border-radius:9px;margin-bottom:10px;display:block;" alt="A young Saudi checking bitcoin on a phone in a Riyadh market with the skyline behind, linocut">
            <span class="tag" style="color:#8a5a12;">Money &amp; Macro &middot; Riyadh</span>
            <h3>Young Saudis Are Buying Bitcoin Faster Than the Gulf</h3>
            <p>The kingdom is the region&rsquo;s fastest-growing digital-asset market &mdash; driven by under-35s, not sovereigns hoarding coins.</p></a>
        </div>
      </div>

      <a class="opinion" href="stories/2026-08-05/bitcoin-annual-obituary-quantum-take.html" style="display:block;">
        <span class="tag opinion">The Take &middot; Opinion</span>
        <h3>Bitcoin&rsquo;s Obituary Is Due Again. This Time It&rsquo;s Quantum.</h3>
        <p>Bitcoin died at Mt. Gox, died each time China banned it, was going to die when Wall Street wrapped it in ETFs. This week it&rsquo;s dying of quantum computers. The obituaries are well written and, so far, all early. Quantum deserves better than an eye-roll: a cryptographic break is physics, not a market panic, and more than a third of all coins sit in addresses with exposed keys. But look at the two clocks. The threat runs on hardware still orders of magnitude short of breaking a private key. The fix runs on proposals that already exist &mdash; post-quantum signatures in draft, custodians scoring wallets, a Galaxy-funded readiness effort &mdash; and on the strongest migration incentive ever built: every holder who moves gets to keep their money. Governments gave themselves until 2030 to go post-quantum. Bitcoin has the same window and a few hundred billion reasons for its users to hurry.</p>
      </a>
    </div>

    <!-- right rail -->''' % {"img": IMG}

s = re.sub(r'    <!-- main column -->.*?    <!-- right rail -->', main, s, count=1, flags=re.S)

# 3) vital stats fallback numbers
s = re.sub(r'(id="vs-price">)[^<]*(<)', r'\g<1>$64,035\g<2>', s)
s = re.sub(r'(id="vs-block">)[^<]*(<)', r'\g<1>961,148\g<2>', s)
s = re.sub(r'(id="vs-hash">)[^<]*(<)', r'\g<1>955 EH/s\g<2>', s)

# 4) most read
mostread = '''<ol>
          <li><a href="stories/2026-08-05/guatemala-bitcoin-lake-panajachel.html">A Guatemalan Lake Town Runs on Bitcoin</a></li>
          <li><a href="stories/2026-08-05/tom-lee-quantum-bitcoin-2028.html">Tom Lee Says Quantum Could Break Bitcoin by 2028</a></li>
          <li><a href="stories/2026-08-05/us-treasury-bitcoin-policy-chief-resigns.html">Treasury&rsquo;s Bitcoin-Policy Chief Resigns as CLARITY Stalls</a></li>
          <li><a href="stories/2026-08-05/bitdeer-liquidates-bitcoin-treasury.html">Bitdeer Sold Every Bitcoin It Held</a></li>
          <li><a href="stories/2026-08-05/saudi-arabia-youth-bitcoin-gulf.html">Young Saudis Are Buying Bitcoin Faster Than the Gulf</a></li>
          <li><a href="stories/2026-08-05/bitcoin-annual-obituary-quantum-take.html">Bitcoin&rsquo;s Obituary Is Due Again. This Time It&rsquo;s Quantum.</a></li>
        </ol>'''
s = re.sub(r'<ol>.*?</ol>', mostread, s, count=1, flags=re.S)

io.open(P, "w", encoding="utf-8").write(s)
print("index patched OK")
