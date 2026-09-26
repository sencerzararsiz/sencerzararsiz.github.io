"""Site test paketi (SDET). Yerel ya da canlı adrese karşı çalışır.

    python tools/test_site.py                       # http://127.0.0.1:8030
    python tools/test_site.py https://sencerzararsiz.github.io
    python tools/test_site.py URL --external        # dış linkleri de dener

Hata varsa çıkış kodu 1 döner.
"""
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = next((a for a in sys.argv[1:] if a.startswith("http")), "http://127.0.0.1:8030").rstrip("/")
CHECK_EXTERNAL = "--external" in sys.argv

# Sitede asla geçmemesi gerekenler: müvekkil/büro adları, eski roller, yapay zekâ izleri
FORBIDDEN = [
    "Karataş Partners Design", "Trade Clash", "TradeClash", "Yatport", "MİMU", "Castrum", "CASTRUM",
    "Hiperaktif", "Creality", "Gameness", "Lumia", "Kontrol Edelim",
    "Claude", "Anthropic", "ChatGPT", "Co-Authored", "yapay zekâ tarafından üretil", "AI-generated",
    "Startup Yöneticisi", "Avukatım", "legalitify.com/blog", "150+", "github.com/sencerzararsiz",
    "Legalitify blogunda", "application/ld+json",
]

fails, warns = [], []
def fail(msg): fails.append(msg)
def warn(msg): warns.append(msg)

def fetch(url):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(url + sep + "t=" + str(time.time()), headers={"User-Agent": "site-test"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return e.code, "", ""
    except Exception as e:  # noqa: BLE001
        return 0, str(e), ""

pages, assets, anchors, external = {}, {}, [], set()
queue = ["/", "/en/"]
while queue:
    path = queue.pop()
    if path in pages:
        continue
    st, body, ctype = fetch(BASE + path)
    pages[path] = body if st == 200 else ""
    if st != 200:
        fail(f"HTTP {st}: {path}")
        continue
    for ref in re.findall(r'(?:href|src)="([^"]+)"', body):
        ref = html.unescape(ref)
        if ref.startswith("mailto:"):
            continue
        if ref.startswith("#"):
            if len(ref) > 1:
                anchors.append((path, ref[1:]))
            continue
        if ref.startswith("http") and not ref.startswith(BASE) and not ref.startswith("https://sencerzararsiz.github.io"):
            external.add(ref)
            continue
        ref = re.sub(r"^https://sencerzararsiz\.github\.io", "", re.sub("^" + re.escape(BASE), "", ref))
        target, _, frag = ref.partition("#")
        target = urllib.parse.urljoin(path, target) if target else path
        if frag:
            anchors.append((target, frag))
        if target.endswith("/"):
            if target not in pages:
                queue.append(target)
        elif target not in assets:
            assets[target] = fetch(BASE + target)[0]
            if assets[target] != 200:
                fail(f"asset HTTP {assets[target]}: {target} (from {path})")

html_pages = {p: b for p, b in pages.items() if b}

for path, frag in anchors:
    body = html_pages.get(path, "")
    if body and f'id="{frag}"' not in body:
        fail(f"missing anchor #{frag} on {path}")

for path, b in html_pages.items():
    text = html.unescape(b)
    lang = re.search(r'<html lang="([a-z]{2})"', b)
    if not lang:
        fail(f"no html lang: {path}")
    elif lang.group(1) != ("en" if path.startswith("/en/") else "tr"):
        fail(f"wrong html lang {lang.group(1)}: {path}")
    if not re.search(r"<title>[^<]{5,}</title>", b):
        fail(f"missing title: {path}")
    if not re.search(r'<meta name="description" content="[^"]{20,}"', b):
        fail(f"missing/short description: {path}")
    n_h1 = len(re.findall(r"<h1[\s>]", b))
    if n_h1 != 1:
        fail(f"{n_h1} h1 elements: {path}")
    for need in ('<link rel="canonical"', 'property="og:image"', 'class="skip"', '<main id="main">', 'hreflang="tr"', 'hreflang="en"', 'id="consent"', "data-theme-toggle"):
        if need not in b:
            fail(f"missing {need}: {path}")
    for tag in re.findall(r"<(?:script|link|img|iframe)\b[^>]*(?:src|href)=\"(https?://[^\"]+)\"", b):
        if "sencerzararsiz.github.io" not in tag and not tag.startswith(BASE):
            fail(f"third-party resource {tag}: {path}")
    for img in re.findall(r"<img\b[^>]*>", b):
        if "alt=" not in img:
            fail(f"img without alt: {path}")
    for w in FORBIDDEN:
        if w in text:
            fail(f"forbidden text '{w}': {path}")
    for h in ("/kvkk-aydinlatma-metni/", "/cerez-politikasi/", "/erisilebilirlik/", "/site-haritasi/") if not path.startswith("/en/") else ("/en/privacy/", "/en/cookies/", "/en/accessibility/", "/en/sitemap/"):
        if f'href="{h}"' not in b:
            fail(f"footer link {h} missing: {path}")
    if path.startswith("/yazilar/") and path != "/yazilar/":
        if 'id="kaynakca"' not in b:
            fail(f"article without sources: {path}")
        if 'class="disclaimer"' not in b:
            fail(f"article without disclaimer: {path}")
        words = len(re.sub(r"<[^>]+>", " ", re.search(r'<div class="prose">(.*?)<h2 id="kaynakca">', b, re.S).group(1)).split()) if '<div class="prose">' in b else 0
        if words < 250:
            warn(f"short article ({words} words): {path}")

# hreflang karşılıklılığı
for path, b in html_pages.items():
    alt = re.search(r'hreflang="(tr|en)" href="https://sencerzararsiz\.github\.io([^"]+)"', b)
    for code, href in re.findall(r'hreflang="(tr|en)" href="https://sencerzararsiz\.github\.io([^"]+)"', b):
        if href not in html_pages and href.rstrip("/") + "/" not in html_pages:
            fail(f"hreflang {code} target not crawled: {href} (from {path})")

if CHECK_EXTERNAL:
    for u in sorted(external):
        st = fetch(u)[0] if "linkedin.com" not in u else 200
        if st not in (200, 301, 302, 999):
            warn(f"external {st}: {u}")

print(f"pages: {len(html_pages)} | assets: {len(assets)} | anchors: {len(anchors)} | external links: {len(external)}")
for w in warns:
    print("WARN ", w)
for f in fails:
    print("FAIL ", f)
print("RESULT:", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(1 if fails else 0)
