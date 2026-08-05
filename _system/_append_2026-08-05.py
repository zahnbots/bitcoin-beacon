# -*- coding: utf-8 -*-
import io
BASE = "/sessions/charming-affectionate-davinci/mnt/bitcoin beacon"
D = "2026-08-05"
ISSUE = "bitcoin-beacon-newspaper-2026-08-05.html"

rows = [
  ("guatemala-bitcoin-lake-panajachel", 'A Guatemalan Lake Town Runs on Bitcoin', "on-the-ground", "Panajachel, Guatemala",
   "bitcoin-lake;lago-bitcoin;lake-atitlan;panajachel;circular-economy;lightning;blink;used-cooking-oil;kaboom;my-first-bitcoin;unbanked;merchants;guatemala;central-america;latam",
   "bitcoinmagazine.com;cryptopotato.com;bitcoinbeach.com;bitcoinnews.com"),
  ("tom-lee-quantum-bitcoin-2028", 'Tom Lee Says Quantum Could Break Bitcoin by 2028', "network-mining", "New York, USA",
   "quantum;tom-lee;fundstrat;q-day;2028;ecdsa;shors-algorithm;post-quantum;google-quantum-ai;ibm;arvind-krishna;exposed-keys;437-billion;galaxy;bitgo;cnbc;united-states;global",
   "coindesk.com;beincrypto.com;bitcoinfoundation.org;x.com"),
  ("us-treasury-bitcoin-policy-chief-resigns", "Treasury's Bitcoin-Policy Chief Resigns as CLARITY Stalls", "policy-nation-states", "Washington, USA",
   "tyler-williams;scott-bessent;treasury;strategic-bitcoin-reserve;clarity-act;arma;bitcoin-act;328000-btc;seizures;silk-road;bitfinex;q4-2026;resignation;united-states",
   "cointelegraph.com;cryptotimes.io;cryptoslate.com;thestreet.com;coincodex.com"),
  ("bitdeer-liquidates-bitcoin-treasury", 'Bitdeer Sold Every Bitcoin It Held', "markets", "Singapore",
   "bitdeer;btdr;treasury-liquidation;1132-btc;zero-holdings;sealminer;63-eh;marathon;ai-pivot;mining-margins;american-bitcoin;forced-sellers;singapore;asia;global",
   "theblock.co;cointelegraph.com;bitcoinmagazine.com;ccn.com;tftc.io"),
  ("saudi-arabia-youth-bitcoin-gulf", "Young Saudis Are Buying Bitcoin Faster Than the Rest of the Gulf", "money-macro", "Riyadh, Saudi Arabia",
   "saudi-arabia;chainalysis;153-percent;47-billion;youth-adoption;vision-2030;sama;gulf;gcc;discretionary-demand;mena;middle-east",
   "chainalysis.com;cryptopolitan.com;bingx.com;disruptionbanking.com"),
  ("bitcoin-annual-obituary-quantum-take", "Bitcoin's Obituary Is Due Again. This Time It's Quantum.", "opinion", "Global",
   "fud-cycle;bitcoin-obituary;mt-gox;china-ban;etf;quantum;post-quantum;segwit;taproot;galaxy;exposed-keys;steelman;take;global",
   "coindesk.com;beincrypto.com;thebitcoinbeacon.com"),
]

def q(v):
    # quote if contains comma, quote, or leading/trailing space; escape internal quotes
    if ',' in v or '"' in v:
        return '"' + v.replace('"','""') + '"'
    return v

# ---- catalog ----
cat = BASE + "/_system/catalog.csv"
lines = []
with io.open(cat, encoding="utf-8") as f:
    content = f.read()
if not content.endswith("\n"):
    content += "\n"
for slug, title, beat, place, tags, sources in rows:
    full_slug = "%s-%s" % (D, slug)
    url = "stories/%s/%s.html" % (D, slug)
    row = [D, ISSUE, full_slug, title, beat, place, tags, sources, url, "published"]
    content += ",".join(q(x) for x in row) + "\n"
io.open(cat, "w", encoding="utf-8").write(content)
print("catalog appended (%d rows)" % len(rows))

# ---- sitemap ----
sm = BASE + "/public/sitemap.xml"
x = io.open(sm, encoding="utf-8").read()
ins = ""
for slug, title, beat, place, tags, sources in rows:
    ins += '  <url><loc>https://thebitcoinbeacon.com/stories/%s/%s</loc><lastmod>%s</lastmod></url>\n' % (D, slug, D)
x = x.replace("</urlset>", ins + "</urlset>")
io.open(sm, "w", encoding="utf-8").write(x)
print("sitemap appended")
