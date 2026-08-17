# -*- coding: utf-8 -*-
import os
BASE = "/sessions/loving-hopeful-curie/mnt/bitcoin beacon"
DATE = "2026-08-15"
DATE_LONG = "August 15, 2026"
DATE_STRAP = "Saturday, August 15, 2026"
ISSUE_NO = "42"
HB = "https://d8j0ntlcm91z4.cloudfront.net/user_3DMGhTlA4NfPrOIBsUsGT9mqIMx/"
S = "https://thebitcoinbeacon.com"

HERO = {
 "lead":HB+"hf_20260815_115243_e7df8eac-fdc3-4064-be97-7ec569a51db1.png",
 "msci":HB+"hf_20260815_115247_71a1f099-1236-48bb-b91c-fd536f192ad7.png",
 "trezor":HB+"hf_20260815_114919_923c816b-d346-44a8-9b64-1afcb8b9208b.png",
 "els":HB+"hf_20260815_115252_3caca9ca-9907-44c4-80b6-c3bd042c7ef4.png",
 "swf":HB+"hf_20260815_115256_445ebc74-318f-411e-a8fd-752e7d73267e.png",
}
def U(slug): return "%s/stories/%s/%s" % (S, DATE, slug)
SLUG = {
 "lead":"lightning-africa-payroll","msci":"msci-index-exclusion-strategy-metaplanet",
 "trezor":"trezor-shipmonk-data-breach","els":"el-salvador-keeps-buying-2027-election",
 "swf":"sovereign-funds-bitcoin-etf","take":"miners-hashrate-flat-price-take",
}
TITLE = {
 "lead":"Lightning Now Pays Salaries Across Africa",
 "msci":"MSCI Moves to Drop Strategy and Metaplanet",
 "trezor":"A Shipping Partner Leaked 13,689 Trezor Owners&rsquo; Addresses",
 "els":"El Salvador Keeps Buying Bitcoin as Rivals Vow to Stop",
 "swf":"Gulf Wealth Funds Are Quietly Buying the Bitcoin ETF",
 "take":"Miners Are Betting on a Price That Hasn&rsquo;t Arrived",
}

VS_PRICE="$62,972"; VS_BLOCK="962,568"; VS_HASH="~900 EH/s"; VS_LABEL="as of 11:45 UTC"

# ================= NEWSPAPER =================
tpl = open(os.path.join(BASE,"_system","_bitcoin-beacon-TEMPLATE.html")).read()

LEAD_BODY = (
 '<p class="first dropcap"><span class="kick">LAGOS &mdash;</span> The fastest-growing use of Bitcoin&rsquo;s Lightning Network in 2026 isn&rsquo;t speculation, and it isn&rsquo;t tipping. It&rsquo;s payroll. Bitnob, a Nigerian-founded payments company, now runs Lightning-based salary payments for remote workers across 23 African countries, with volume up 340%% in a year.</p>'
 '<p>The money crosses borders as bitcoin &mdash; settling in seconds for a fraction of a cent &mdash; and lands with a worker as local currency; the recipient often never sees a coin. Machankura pushes the same rail onto $15 feature phones over USSD and SMS, and in Kenya every M-Pesa number, some 40 million of them, is now reachable as a Lightning address.</p>'
 '<p>The catch is that these rails are custodial: convenience with a counterparty, the intermediary bitcoin was built to remove, quietly reintroduced.</p>'
 '<p><em>Why it matters: bitcoin is winning Africa as a payment wire, not as savings people hold themselves.</em></p>'
 '<p><a href="%s">Read the full dispatch &rarr;</a></p>' % U(SLUG["lead"])
)

SECTIONS = (
 '<span class="sub">Markets &amp; Institutions</span>'
 '<p><span class="kick">NEW YORK.</span> MSCI has proposed cutting &ldquo;non-operating companies&rdquo; from its global indexes, and its own simulation deletes the two biggest corporate bitcoin holders, Strategy and Metaplanet. Index funds must sell what leaves a benchmark, so exclusion means forced, price-blind outflows &mdash; potentially billions. Feedback runs to September; the deletion review is set for November 11. Strategy is already fighting back. <a href="%s">Full story &rarr;</a></p>' % U(SLUG["msci"]) +
 '<span class="sub">Network &amp; Mining</span>'
 '<p><span class="kick">PRAGUE.</span> A breach at Trezor&rsquo;s shipping partner ShipMonk exposed order data for 13,689 hardware-wallet customers &mdash; most records including names, phone numbers and home addresses. The wallets and keys were untouched, but a list of verified bitcoin owners and where they live is a phishing and physical-robbery target. It caps a rough summer after August&rsquo;s Coldcard exploit. <a href="%s">Full story &rarr;</a></p>' % U(SLUG["trezor"]) +
 '<span class="sub">Policy &amp; Nation-States</span>'
 '<p><span class="kick">SAN SALVADOR.</span> El Salvador&rsquo;s reserve is nearing 7,730 bitcoin and still growing about a coin a day, five years after Bukele&rsquo;s bet &mdash; and the state has never sold one. But the IMF stripped the legal-tender mandate in 2025, and 2027 opposition candidates now campaign on scrapping the policy. A reserve tied to one president is one election from reversal. <a href="%s">Full story &rarr;</a></p>' % U(SLUG["els"]) +
 '<span class="sub">Money &amp; Macro</span>'
 '<p><span class="kick">ABU DHABI.</span> The world&rsquo;s largest state funds want bitcoin &mdash; through Wall Street, not private keys. Abu Dhabi&rsquo;s Mubadala lifted its BlackRock IBIT stake past $1 billion; Luxembourg&rsquo;s sovereign fund put 1%%, some &euro;850 million, into bitcoin ETFs. The wrapper is the point: audited custody, familiar reporting, an easy exit. <a href="%s">Full story &rarr;</a></p>' % U(SLUG["swf"])
)

THE_TAKE = (
 '<div class="take">'
 '<div class="tag">The Take &middot; Opinion</div>'
 '<h3>Miners Are Betting on a Price That Hasn&rsquo;t Arrived</h3>'
 '<p>Record hashrate is the most misread number in bitcoin. Power near 900 EH/s and difficulty at a near-record 127 trillion get read as miners&rsquo; confidence. But the price is flat in the low $63,000s, so rising difficulty just means every rig earns less. Hashrate is a lagging vote &mdash; machines ordered months ago &mdash; not conviction today.</p>'
 '<p>If the price stays put, the weakest miners capitulate, difficulty falls at the next retarget, and the survivors inherit a cheaper network. Read record hashrate as ambition, not confirmation.</p>'
 '<p class="sig"><a href="%s">Read the argument &rarr;</a> &bull; The Bitcoin Beacon</p>'
 '</div>' % U(SLUG["take"])
)

WATCHING = (
 'The SEC abruptly scrapped its August 14 meeting to unveil a &ldquo;Regulation Crypto Assets&rdquo; framework, with no new date set &mdash; the rulebook every US desk is waiting on. Bitcoin Hong Kong (August 27&ndash;28) for how Asia&rsquo;s regulators are leaning on ETFs and custody. Whether Tether&rsquo;s dollar tokens, now live on Lightning, pull merchants toward stablecoin payments on bitcoin&rsquo;s rails. And the next US inflation print, the macro backdrop under every flow.'
)

hero_html = '<img src="%s" alt="A Lagos market vendor accepts a mobile payment, three-color linocut"><div class="cap">Lightning has become a payroll and remittance rail across Africa &middot; Illustration: The Bitcoin Beacon</div>' % HERO["lead"]

np = tpl
np = np.replace("The Bitcoin Beacon &mdash; July 3, 2026","The Bitcoin Beacon &mdash; "+DATE_LONG)
np = np.replace("The Bitcoin Beacon — July 3, 2026","The Bitcoin Beacon — "+DATE_LONG)
np = np.replace("{{ISSUE_NO}}",ISSUE_NO)
np = np.replace("{{DATE}}",DATE_LONG)
np = np.replace("{{LEAD_HEADLINE}}",TITLE["lead"])
np = np.replace("{{DECK}}","Bitnob, Machankura and Tando have turned Lightning into Africa&rsquo;s quiet payroll rail &mdash; mostly through apps that hide the coin.")
np = np.replace("{{DESK}}","On the Ground")
np = np.replace("{{HERO}}",hero_html)
np = np.replace("{{PRICE}}",VS_PRICE)
np = np.replace("{{BLOCK}}",VS_BLOCK)
np = np.replace("{{HASHRATE}}",VS_HASH)
np = np.replace("Vital Stats &middot; at press time","Vital Stats &middot; "+VS_LABEL)
np = np.replace("{{LEAD_BODY}}",LEAD_BODY)
np = np.replace("{{THE_TAKE}}",THE_TAKE)
np = np.replace("{{SECTIONS}}",SECTIONS)
np = np.replace("{{VOICES}}","")
np = np.replace("{{WATCHING}}",WATCHING)
# footer links (match recent issues)
np = np.replace('You&rsquo;re receiving this because you subscribed. <a href="#">Unsubscribe</a> &bull; <a href="#">Manage preferences</a>',
                'Read every dispatch at <a href="https://thebitcoinbeacon.com">thebitcoinbeacon.com</a> &bull; <a href="https://thebitcoinbeacon.com/subscribe.html">Subscribe free</a>')

idir = os.path.join(BASE,"issues",DATE)
os.makedirs(idir, exist_ok=True)
open(os.path.join(idir,"bitcoin-beacon-newspaper-%s.html"%DATE),"w").write(np)

# ================= PASTE =================
paste = (
'<!DOCTYPE html><html><head><meta charset="utf-8"><title>PASTE VERSION &mdash; %s</title></head>\n' % DATE +
'<body style="max-width:640px;margin:0 auto;font-family:Georgia,serif;">\n'
'<div style="background:#f2efe8;border:2px dashed #b5ad9e;border-radius:10px;padding:16px 20px;font-family:Arial,sans-serif;font-size:14px;line-height:1.6;">\n'
'<strong style="color:#c0392b;">SETTINGS &mdash; do not paste this box into beehiiv</strong><br>\n'
'<strong>Subject:</strong> Lightning Now Pays Salaries Across Africa<br>\n'
'<strong>Preview text:</strong> Bitcoin&rsquo;s payment layer became a payroll rail from Lagos to Nairobi &mdash; mostly through apps that hide the coin.<br>\n'
'<strong>Thumbnail:</strong> <a href="%s">download the hero image</a>, set as post thumbnail / first image<br>\n' % HERO["lead"] +
'<strong>Then:</strong> copy everything BELOW the red line and paste into the post body.\n'
'</div>\n'
'<div style="border-top:4px solid #c0392b;margin:18px 0;"></div>\n\n'
'<h1>Lightning Now Pays Salaries Across Africa</h1>\n'
'<p><strong>LAGOS</strong> &mdash; The fastest-growing use of Bitcoin&rsquo;s Lightning Network in 2026 isn&rsquo;t speculation, and it isn&rsquo;t tipping. It&rsquo;s payroll. Bitnob now runs Lightning-based salary payments for remote workers across <strong>23 African countries</strong>, with volume up <strong>340%%</strong> in a year.</p>\n'
'<p>Money crosses borders as bitcoin &mdash; settling in seconds for a fraction of a cent &mdash; and lands as local currency; the worker often never sees a coin. Machankura pushes the same rail onto feature phones over USSD, and in Kenya every M-Pesa number, some 40 million, is now reachable as a Lightning address.</p>\n'
'<p><em>Why it matters: bitcoin is winning Africa as a payment wire, not as savings people hold themselves &mdash; and it&rsquo;s arriving through custodial apps.</em></p>\n'
'<p><a href="%s">Read the full dispatch &rarr;</a></p>\n' % U(SLUG["lead"]) +
'<hr>\n'
'<h2>MSCI Moves to Drop Strategy and Metaplanet</h2>\n'
'<p>A proposed rule cutting &ldquo;non-operating companies&rdquo; from MSCI&rsquo;s global indexes would delete the two biggest corporate bitcoin holders &mdash; forcing index funds to sell, with the review set for November 11. <a href="%s">Full story &rarr;</a></p>\n' % U(SLUG["msci"]) +
'<h2>A Shipping Partner Leaked 13,689 Trezor Owners&rsquo; Addresses</h2>\n'
'<p>A breach at Trezor&rsquo;s fulfillment provider ShipMonk exposed names, phones and home addresses of hardware-wallet buyers &mdash; keys untouched, but a ready-made target list for phishing and robbery. <a href="%s">Full story &rarr;</a></p>\n' % U(SLUG["trezor"]) +
'<h2>El Salvador Keeps Buying Bitcoin as Rivals Vow to Stop</h2>\n'
'<p>The reserve is nearing 7,730 coins and still growing daily, but the IMF stripped the legal-tender mandate and 2027 opposition candidates now campaign on scrapping the policy. <a href="%s">Full story &rarr;</a></p>\n' % U(SLUG["els"]) +
'<h2>Gulf Wealth Funds Are Quietly Buying the Bitcoin ETF</h2>\n'
'<p>Abu Dhabi&rsquo;s Mubadala pushed its BlackRock IBIT stake past $1 billion and Luxembourg put 1%% into bitcoin ETFs &mdash; nations taking exposure through Wall Street, not private keys. <a href="%s">Full story &rarr;</a></p>\n' % U(SLUG["swf"]) +
'<hr>\n'
'<h2>The Take: Miners Are Betting on a Price That Hasn&rsquo;t Arrived</h2>\n'
'<p>Record hashrate near 900 EH/s reads as confidence, but with the price flat, rising difficulty just means every rig earns less. Hashrate is a lagging vote, not conviction. <a href="%s">Read the argument &rarr;</a></p>\n' % U(SLUG["take"]) +
'<hr>\n'
'<p><strong>Vital Stats</strong> (%s): BTC %s &middot; Block %s &middot; Hashrate %s</p>\n' % (VS_LABEL, VS_PRICE, VS_BLOCK, VS_HASH) +
'<p><em>Hero image for thumbnail:</em> <a href="%s">download here</a></p>\n' % HERO["lead"] +
'</body></html>'
)
open(os.path.join(idir,"bitcoin-beacon-paste-%s.html"%DATE),"w").write(paste)

# ================= ART =================
def artblock(head, url, lead=False):
    tag = " (use as email thumbnail)" if lead else ""
    return ('<h3 style="font-family:Georgia,serif;">%s%s</h3>'
            '<img src="%s" style="max-width:100%%;border-radius:8px;">'
            '<p><a href="%s">open full size</a> &mdash; right-click the image to save</p>\n' % (head, tag, url, url))
art = ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Art &mdash; %s</title></head>\n' % DATE +
 '<body style="max-width:760px;margin:0 auto;padding:20px;font-family:Arial,sans-serif;background:#faf7f1;">\n'
 '<h1 style="font-family:Georgia,serif;">The Bitcoin Beacon &mdash; Art for %s</h1>\n' % DATE +
 "<p>All of today&rsquo;s heroes. Right-click any image to save; the LEAD image is the beehiiv thumbnail.</p>\n" +
 artblock("LEAD &mdash; Lightning Now Pays Salaries Across Africa", HERO["lead"], lead=True) +
 artblock("MSCI Moves to Drop Strategy and Metaplanet", HERO["msci"]) +
 artblock("A Shipping Partner Leaked 13,689 Trezor Owners&rsquo; Addresses", HERO["trezor"]) +
 artblock("El Salvador Keeps Buying Bitcoin as Rivals Vow to Stop", HERO["els"]) +
 artblock("Gulf Wealth Funds Are Quietly Buying the Bitcoin ETF", HERO["swf"]) +
 '</body></html>')
open(os.path.join(idir,"art-%s.html"%DATE),"w").write(art)

print("issue files written to", idir)
print(os.listdir(idir))
