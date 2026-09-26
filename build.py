"""Statik site üreticisi. Tek içerik kaynağından tüm sayfaları üretir.

    python build.py

İçerik: bu dosya (ana sayfa), content_posts.py (yazılar), content_legal.py (hukuki sayfalar).
Harici bağımlılık yok. Sayfalar kök dizine göre mutlak yollarla bağlanır.

Reklam yasağı notu: 1136 s. Avukatlık Kanunu m.55 ve TBB Reklam Yasağı Yönetmeliği m.7
gözetildi. Müvekkil/referans, iş çağrısı, rakam övgüsü ve arama motoru sıralamasına yönelik
kod (JSON-LD, sitemap.xml, anahtar sözcük) bilinçli olarak kullanılmaz.
"""
import re
from html import escape as e
from math import ceil
from pathlib import Path

import content_legal as LG
from content_posts import POSTS, SRC, ACCESS

ROOT = Path(__file__).parent
SITE = "https://sencerzararsiz.github.io"
EMAIL = "avahmetsencerzararsiz@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/sencer-ahmet"
NAME = "Ahmet Sencer Zararsız"

# ---------------------------------------------------------------- ikonlar
def _svg(d, fill=False, w="1.8"):
    if fill:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="{d}"/></svg>'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{d}"/></svg>'

ICON = {
    "arrow": _svg("M5 12h14M13 6l6 6-6 6", w="2"),
    "ne": _svg("M7 17L17 7M8 7h9v9", w="2"),
    "plus": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M6 1v10M1 6h10"/></svg>',
    "x": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M2 2l8 8M10 2l-8 8"/></svg>',
    "mail": _svg("M3 7a2 2 0 012-2h14a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2zM4 7l8 6 8-6"),
    "in": _svg("M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.05c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.67 4.8 6.13V21h-4v-4.96c0-1.18-.02-2.7-1.65-2.7-1.65 0-1.9 1.29-1.9 2.62V21h-4z", fill=True),
    "pause": '<svg class="i-pause" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true" focusable="false"><rect x="2.5" y="2" width="3" height="10" rx="1"/><rect x="8.5" y="2" width="3" height="10" rx="1"/></svg>',
    "play": '<svg class="i-play" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true" focusable="false"><path d="M3.5 2.2v9.6a.6.6 0 00.9.5l7.6-4.8a.6.6 0 000-1l-7.6-4.8a.6.6 0 00-.9.5z"/></svg>',
    "moon": '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 14.5A8 8 0 019.5 4a8 8 0 1010.5 10.5z"/></svg>',
    "sun": '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "scale": _svg("M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"),
    "code": _svg("M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16"),
    "design": _svg("M6 3h12a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V5a2 2 0 012-2zM8 8h8M8 12h5M8 16h3"),
    "spark": _svg("M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"),
    "book": _svg("M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2zM4 19V5M8 7h7"),
}

# ---------------------------------------------------------------- yollar
PATHS = {
    "home": ("/", "/en/"),
    "posts": ("/yazilar/", "/en/writing/"),
    "kvkk": ("/kvkk-aydinlatma-metni/", "/en/privacy/"),
    "cookies": ("/cerez-politikasi/", "/en/cookies/"),
    "terms": ("/kullanim-kosullari/", "/en/terms/"),
    "legal": ("/yasal-bilgiler/", "/en/legal-notice/"),
    "a11y": ("/erisilebilirlik/", "/en/accessibility/"),
    "sitemap": ("/site-haritasi/", "/en/sitemap/"),
}
def P(key, lang):
    return PATHS[key][0 if lang == "tr" else 1]

MONTHS = {
    "tr": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
}
def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    mon = MONTHS[lang][int(m) - 1]
    return f"{int(d)} {mon} {y}" if lang == "tr" else f"{mon} {int(d)}, {y}"

def yr(s, lang):
    s = s.strip()
    if s.endswith("–"):
        return s + (" present" if lang == "en" else " devam")
    return s

TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")
def slugify(t):
    t = re.sub(r"<[^>]+>", "", t).translate(TR_MAP).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

# ---------------------------------------------------------------- arayüz metinleri
UI = {
    "tr": {
        "skip": "İçeriğe geç",
        "nav": [("/#hakkimda", "Hakkımda"), ("/#alanlar", "Alanlar"), ("/#deneyim", "Deneyim"), ("/yazilar/", "Yazılar"), ("/#iletisim", "İletişim")],
        "nav_label": "Ana menü",
        "theme": "Koyu temayı aç/kapat",
        "home": "Ana sayfa",
        "foot_tag": "Avukat. Teknoloji hukuku, regülasyon uyumu ve legal design üzerine çalışıyorum.",
        "foot_note": "Bu site bir özgeçmiş ve yayın sayfasıdır; iş elde etme amacı taşımaz.",
        "foot_cols": [
            ("Site", [("/", "Ana sayfa"), ("/yazilar/", "Yazılar"), ("/site-haritasi/", "Site haritası"), ("/en/", "English")]),
            ("Hukuki", [("/kvkk-aydinlatma-metni/", "KVKK Aydınlatma Metni"), ("/cerez-politikasi/", "Çerez Politikası"), ("/kullanim-kosullari/", "Kullanım Koşulları"), ("/yasal-bilgiler/", "Yasal Bilgiler")]),
            ("Erişim", [("/erisilebilirlik/", "Erişilebilirlik Beyanı"), ("#consent", "Çerez tercihleri"), (LINKEDIN, "LinkedIn")]),
        ],
        "foot_bottom": ["© 2026 Ahmet Sencer Zararsız", "Çerez, analitik ve takip aracı kullanılmaz."],
        "consent": {
            "title": "Çerez ve tarayıcı depolaması",
            "text": 'Bu sitede çerez, analitik ya da takip aracı yok. Seçiminizi hatırlamak için tarayıcınıza küçük bir kayıt yazılır; izin verirseniz tema tercihiniz de hatırlanır. <a href="/cerez-politikasi/">Çerez Politikası</a>',
            "need": "Zorunlu", "always": "Her zaman açık", "need_d": "Bu paneldeki seçiminiz (<code>sz-consent</code>). 12 ay saklanır.",
            "pref": "Tercih", "pref_d": "Açık veya koyu tema seçiminiz (<code>sz-theme</code>). Kapalıyken tema yalnızca açık sayfada geçerli olur.",
            "save": "Seçimi kaydet", "reject": "Reddet", "prefs": "Tercihler", "accept": "Kabul et", "close": "Kapat",
            "on": "Şu anki seçiminiz: tercih depolamasına izin verildi.", "off": "Şu anki seçiminiz: tercih depolaması reddedildi.",
        },
        "updated": "Son güncelleme",
        "binding": "",
        "read": "dk okuma",
        "by": "Yazan",
        "toc": "Bu sayfada",
        "sources": "Kaynakça",
        "accessed": "erişim",
        "first": "Bu yazı ilk olarak Legalitify blogunda yayımlandı ({d}); burada gözden geçirilip güncellendi.",
        "disclaimer": "Bu yazı genel bilgi verir ve yayım tarihindeki mevzuata dayanır. Hukuki görüş ya da danışmanlık teklifi değildir; somut bir olaya uygulanmadan önce güncel mevzuat ayrıca kontrol edilmelidir.",
        "more": "Diğer yazılar",
        "all_posts": "Tüm yazılar",
    },
    "en": {
        "skip": "Skip to content",
        "nav": [("/en/#about", "About"), ("/en/#areas", "Areas"), ("/en/#experience", "Experience"), ("/en/writing/", "Writing"), ("/en/#contact", "Contact")],
        "nav_label": "Main",
        "theme": "Toggle dark theme",
        "home": "Home",
        "foot_tag": "Attorney. I work on technology law, regulatory compliance and legal design.",
        "foot_note": "This site is a CV and publications page; it is not intended to solicit work.",
        "foot_cols": [
            ("Site", [("/en/", "Home"), ("/en/writing/", "Writing"), ("/en/sitemap/", "Sitemap"), ("/", "Türkçe")]),
            ("Legal", [("/en/privacy/", "Privacy Notice"), ("/en/cookies/", "Cookie Policy"), ("/en/terms/", "Terms of Use"), ("/en/legal-notice/", "Legal Notice")]),
            ("Access", [("/en/accessibility/", "Accessibility Statement"), ("#consent", "Cookie preferences"), (LINKEDIN, "LinkedIn")]),
        ],
        "foot_bottom": ["© 2026 Ahmet Sencer Zararsız", "No cookies, analytics or trackers."],
        "consent": {
            "title": "Cookies and browser storage",
            "text": 'This site uses no cookies, analytics or trackers. A small entry is written to your browser to remember your choice; if you allow it, your theme preference is remembered too. <a href="/en/cookies/">Cookie Policy</a>',
            "need": "Necessary", "always": "Always on", "need_d": "Your choice in this panel (<code>sz-consent</code>). Kept for 12 months.",
            "pref": "Preference", "pref_d": "Your light or dark theme choice (<code>sz-theme</code>). When off, the theme applies only to the open page.",
            "save": "Save choice", "reject": "Reject", "prefs": "Preferences", "accept": "Accept", "close": "Close",
            "on": "Current choice: preference storage allowed.", "off": "Current choice: preference storage rejected.",
        },
        "updated": "Last updated",
        "binding": "",
        "read": "min read",
        "by": "By",
        "toc": "On this page",
        "sources": "Sources",
        "accessed": "accessed",
        "first": "First published on the Legalitify blog ({d}); reviewed and updated here.",
        "disclaimer": "General information based on the law at the date of publication. Not legal advice or an offer of services.",
        "more": "More articles",
        "all_posts": "All articles",
    },
}

# ---------------------------------------------------------------- ana sayfa içeriği
HOME = {
    "tr": {
        "title": "Ahmet Sencer Zararsız · Avukat",
        "desc": "Ahmet Sencer Zararsız. Avukat; teknoloji hukuku, regülasyon uyumu, legaltech ve legal design üzerine çalışıyor. Özgeçmiş, yazılar ve eğitimler.",
        "og_locale": "tr_TR",
        "status": "Şu an GameLaw.io'da Team Lead",
        "lead": "Avukatım. Hukuku, insanların gerçekten <em>kullanabileceği</em> metinlere, ürünlere ve arayüzlere çeviriyorum.",
        "cta1": "LinkedIn profilim",
        "cta2": "Yazılarım",
        "reel_cap": "Bu animasyonun tamamı kod. Tek bir şekil, bir uyum akışını baştan sona anlatıyor.",
        "reel_pause": "Durdur",
        "reel_play": "Oynat",
        "reel_label": "Hareketli gösterim. Sırasıyla: web sitesinde uyum taraması başlatılıyor; tarama üç bulgu buluyor; eşit ağırlıkta Reddet ve Kabul et düğmeleri olan bir çerez paneli; SMS izni için İYS'ye iletilen bir onay anahtarı; KVKK m.5/2-c'ye dayanan uzun bir aydınlatma cümlesi, 'Adresinizi yalnızca siparişinizi teslim etmek için kullanırız' cümlesine sadeleşiyor; mevzuat aramasında 'm.11' yazılınca 'KVKK m.11, İlgili kişinin hakları' bulunuyor; son olarak 'Uyum raporu hazır' bildirimi.",
        "marquee": ["Kişisel verilerin korunması", "GDPR", "Tüketici hukuku", "E-ticaret hukuku", "İnternet hukuku", "Sosyal medya hukuku", "Web3 ve kripto varlıklar", "ISO/IEC 27001", "İç denetim", "MASAK uyumu", "Siber güvenlik", "Reklam hukuku", "Fikrî mülkiyet", "Oyun hukuku", "Yapay zekâ", "Legal Design", "LegalOps"],
        "marquee_hl": ["Legal Design", "ISO/IEC 27001", "Web3 ve kripto varlıklar"],
        "about_k": "Hakkımda",
        "about_big": "Hukuk fakültesinden sonra yolum mahkeme koridorlarından <em>ürün ekiplerine</em> uzandı.",
        "about": [
            "2022'de Atatürk Üniversitesi Hukuk Fakültesi'nden mezun oldum. Stajımı ve ilk avukatlık yıllarımı Ankara'da dava dosyaları, sözleşmeler ve KVKK metinleri arasında geçirdim. Aynı yıllarda kendi girişimlerimi kurdum, hukuk teknolojileri atölyeleri düzenledim.",
            "TÖDEB Fintek Programı ve PARAM'daki çalışmam beni ödeme hizmetleri, MASAK mevzuatı ve regülasyon uyumunun içine soktu. Bugün lisanslı MASAK Uyum Görevlisi ve ISO/IEC 27001 BGYS Baş Denetçisiyim. Bilgi güvenliği denetimleri, iç kontrol ve risk analizleri, uyum yol haritaları gündelik işimin parçası.",
            "Asıl merakım hukukun nasıl göründüğü ve nasıl kullanıldığı. Legalitify'da web sitelerini tarayan bir legaltech ürününün hukuki altyapısını kurdum. GameLaw.io'da oyun ekosistemi için kurulan hukuki platformun ekibini yönetiyorum. Legal design ve legaltech eğitimleriyle bu yaklaşımı bilişim ve teknoloji topluluklarına anlatıyorum.",
        ],
        "approach_k": "Yaklaşım",
        "approach_h": "Dört şapka, <em>tek masa.</em>",
        "approach_p": "Bir metni yazan avukat, onu ürüne döken mühendis, okunur kılan tasarımcı ve başkasına öğreten eğitmen çoğu zaman ayrı kişilerdir. Ben dördünü aynı masada birleştirmeye çalışıyorum.",
        "cards": [
            ("scale", "Hukuk", "Teknoloji, bilişim ve regülasyon", "KVKK ve GDPR uyumu, 7545 sayılı Siber Güvenlik Kanunu, e-ticaret, internet ve reklam mevzuatı, fikrî mülkiyet, arabuluculuk."),
            ("code", "Legal engineering", "Hukuku ürüne çevirmek", "Legaltech ürünlerinin hukuki altyapısı, sektöre göre koşullu metin şablonları, yapay zekâ yönetişimi, LegalOps ve süreç otomasyonu."),
            ("design", "Legal design", "Okunan ve uygulanan metin", "Sade dil, katmanlı aydınlatma, kullanıcı odaklı sözleşme mimarisi. Hukuki doğruluktan ödün vermeden."),
            ("spark", "Denetim ve uyum", "Yükümlülükten kontrole", "ISO/IEC 27001 BGYS denetimleri, COSO yaklaşımıyla iç kontrol, regülatif risk analizleri, MASAK uyumu ve uyum yol haritaları."),
        ],
        "areas_k": "Çalıştığım alanlar",
        "areas_h": "Nerede <em>çalışıyorum?</em>",
        "areas_p": "Günlük işimde en çok karşılaştığım hukuk alanları. Liste bir hizmet kataloğu değil, çalışma alanlarımın haritası.",
        "areas_note": "Bu bölüm, TBB Reklam Yasağı Yönetmeliği m.7/d uyarınca faaliyet alanlarını tanıtır; uzmanlık anlamına gelmez.",
        "areas": [
            ("Kişisel verilerin korunması", "KVKK ve GDPR kapsamında idari ve teknik uyum, veri envanteri, aydınlatma ve rıza mimarisi."),
            ("Bilgi güvenliği ve denetim", "ISO/IEC 27001 BGYS denetimleri, belgelendirmeye hazırlık, 7545 sayılı Siber Güvenlik Kanunu."),
            ("İç denetim ve risk analizi", "COSO yaklaşımıyla iç kontrol, regülatif risk analizleri, due diligence ve uyum yol haritaları."),
            ("Uyum süreçleri ve regülasyon", "5549 sayılı Kanun (MASAK), 6493 sayılı Kanun (ödeme hizmetleri), düzenleyici kurum yazışmaları, mevzuat takibi."),
            ("Tüketici hukuku", "Mesafeli sözleşmeler, ön bilgilendirme, cayma ve iade, haksız şartlar."),
            ("E-ticaret hukuku", "6563 sayılı Kanun, ticari elektronik ileti ve İYS, satıcı yükümlülükleri."),
            ("İnternet hukuku", "5651 sayılı Kanun, içerik ve yer sağlayıcı sorumluluğu, içerik kaldırma ve erişim engelleme."),
            ("Sosyal medya hukuku", "Influencer iş birlikleri, örtülü reklam, itibar yönetimi ve içerik uyuşmazlıkları."),
            ("Reklam hukuku", "Ticari reklam ilkeleri, iddiaların ispatı, Reklam Kurulu nezdinde savunma ve uzlaşma."),
            ("Web3 ve kripto varlık hukuku", "Blokzincir projelerinin regülasyon analizi, akıllı sözleşmeler, DAO yapıları, zincir üzerinde veri koruma."),
            ("Fikrî mülkiyet", "5846 sayılı FSEK kapsamında telif, marka, yazılım ve dijital içerik hakları."),
            ("Oyun ve espor hukuku", "Geliştirme ve yayıncılık sözleşmeleri, oyun içi ekonomi, oyuncu verileri."),
            ("Yapay zekâ ve teknoloji sözleşmeleri", "Yapay zekâ yönetişimi, SaaS sözleşmeleri, sözleşme yönetimi (CLM)."),
            ("Girişim hukuku", "Şirketleşme, yatırım turları ve hissedarlar sözleşmeleri (SHA)."),
        ],
        "ld_k": "Legal design, canlı",
        "ld_h": "Aynı madde, <em>iki hâli.</em>",
        "ld_p": "Legal design, hukuki doğruluğu kaybetmeden metni okunur ve uygulanabilir hâle getirmektir. Aşağıda bir e-ticaret aydınlatma metninden tek bir paragraf var. Düğmeyle iki hâli arasında geçiş yapın.",
        "ld_note": "Örnek gösterim amaçlıdır, hukuki görüş değildir.",
        "ld_btn": ("Hukukça", "Sade dil"),
        "ld_legal": "Veri sorumlusu sıfatıyla Şirketimiz tarafından, 6698 sayılı Kişisel Verilerin Korunması Kanunu'nun 5. maddesinin 2. fıkrasının (c) bendi uyarınca, bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması kaydıyla sözleşmenin taraflarına ait kişisel verilerin işlenmesinin gerekli olması hukuki sebebine dayanılarak; kimlik ve iletişim verileriniz siparişinizin ifası amacıyla işlenmekte ve bu amaçla sınırlı olarak Kanun'un 8. maddesi uyarınca kargo hizmet sağlayıcılarına aktarılabilmektedir. Kanun'un 11. maddesinde sayılan haklarınıza ilişkin taleplerinizi Şirketimize iletebilirsiniz.",
        "ld_meter": ["2 cümle", "{words} kelime", "Okuma: zor"],
        "ld_plain_h": "Siparişinizi teslim edebilmek için birkaç bilginize ihtiyacımız var.",
        "ld_rows": [
            ("Ne kullanıyoruz?", "Adınız, adresiniz ve telefonunuz."),
            ("Neden?", "Siparişinizi size ulaştırmak için. Başka bir amaçla kullanmayız."),
            ("Hukuki dayanak", 'Sözleşmenin ifası <code>KVKK m.5/2-c</code>'),
            ("Kimlerle paylaşıyoruz?", 'Yalnızca kargo şirketiyle <code>KVKK m.8</code>'),
            ("Haklarınız", 'Bilgi isteme, düzeltme, silme ve itiraz <code>KVKK m.11</code>'),
        ],
        "ven_k": "Girişimler ve ürünler",
        "ven_h": "Kurduğum ve <em>içinde yer aldığım.</em>",
        "ven_p": "Hukuki altyapısında çalıştığım ürünler ve aktif rol aldığım girişimler.",
        "now": "Devam",
        "exp_k": "Deneyim",
        "exp_h": "Adliyeden ürün ekibine.",
        "exp_p": "Stajdan bugüne; dava dosyasından ürünlerin uyum mimarisine. Ayrıntı için satırlara dokunun.",
        "teach_k": "Eğitimler ve yayınlar",
        "teach_h": "Bildiğini <em>paylaşmak.</em>",
        "teach_p": "Legal design, legaltech ve bilişim hukuku eğitimleri; bilişim ve teknoloji topluluklarında atölyeler.",
        "pub_k": "Makale",
        "pub_t": "Web3 ve Endüstri 4.0: blokzincir üzerinde kişisel verilerin korunmasına yönelik öneriler",
        "pub_d": "Değiştirilemez kayıt mantığı ile silme hakkı, veri minimizasyonu ve veri sorumlusunun belirlenmesi arasındaki gerilim üzerine.",
        "posts_k": "Yazılar",
        "posts_h": "Uyumu anlaşılır <em>yazmak.</em>",
        "posts_p": "Her yazı tek bir uyum sorusunu sade bir dille ele alıyor. Mevzuat atıfları yayın öncesinde birincil kaynaktan kontrol edildi.",
        "edu_k": "Eğitim ve sertifikalar",
        "edu_h": "Hukuk, fintek ve <em>bilişim.</em>",
        "edu_p": "Hukuk fakültesinden sonra fintek regülasyonu ve yönetim bilişim sistemleri; denetim ve uyum sertifikaları.",
        "edu_t": "Eğitim",
        "cert_t": "Sertifikalar",
        "langs": ["Türkçe · ana dil", "İngilizce · profesyonel çalışma yetkinliği"],
        "contact_h": "<em>Merhaba</em> demek için.",
        "contact_p": "Yazılarım, eğitimler ya da legaltech ve legal design üzerine fikir alışverişi için LinkedIn'den veya e-postayla ulaşabilirsiniz.",
        "contact_kvkk": 'E-posta gönderdiğinizde kişisel verileriniz <a href="/kvkk-aydinlatma-metni/">KVKK Aydınlatma Metni</a>\'ne uygun olarak işlenir. Lütfen mesajınıza özel nitelikli kişisel veri eklemeyin.',
        "email_btn": "E-posta",
    },
    "en": {
        "title": "Ahmet Sencer Zararsız · Attorney",
        "desc": "Ahmet Sencer Zararsız. Attorney working on technology law, regulatory compliance, legaltech and legal design. CV, writing and training.",
        "og_locale": "en_US",
        "status": "Now: Team Lead at GameLaw.io",
        "lead": "I'm a lawyer. I turn law into texts, products and interfaces people can actually <em>use</em>.",
        "cta1": "My LinkedIn",
        "cta2": "Writing",
        "reel_cap": "Every frame of this animation is code. One shape tells a whole compliance flow.",
        "reel_pause": "Pause",
        "reel_play": "Play",
        "reel_label": "Animated demo. In order: a website compliance scan starts; it finds three issues; a cookie panel with equally weighted Reject and Accept buttons; an SMS consent switch sent to İYS; a long privacy sentence based on KVKK Art. 5(2)(c) is simplified to 'We use your address only to deliver your order'; typing 'm.11' in a statute search finds 'KVKK Art. 11, data subject rights'; finally a 'Compliance report ready' notice.",
        "marquee": ["Data protection", "GDPR", "Consumer law", "E-commerce law", "Internet law", "Social media law", "Web3 & crypto assets", "ISO/IEC 27001", "Internal audit", "AML compliance", "Cybersecurity", "Advertising law", "Intellectual property", "Games law", "AI", "Legal Design", "LegalOps"],
        "marquee_hl": ["Legal Design", "ISO/IEC 27001", "Web3 & crypto assets"],
        "about_k": "About",
        "about_big": "After law school, my path ran from courtroom corridors to <em>product teams</em>.",
        "about": [
            "I graduated from Atatürk University Faculty of Law in 2022. I spent my traineeship and first years as a lawyer in Ankara among case files, contracts and data protection documents, and in the same years founded my own ventures and ran legal technology workshops.",
            "The TÖDEB Fintech Programme and my work at PARAM pulled me into payment services, anti-money-laundering rules and regulatory compliance. Today I'm a licensed MASAK Compliance Officer and an ISO/IEC 27001 ISMS Lead Auditor; information security audits, internal control, risk analyses and compliance roadmaps are part of my everyday work.",
            "What I'm really curious about is how law looks and how it's used. At Legalitify I built the legal infrastructure of a legaltech product that scans websites. At GameLaw.io I lead the team behind a legal platform for the games ecosystem. Through legal design and legaltech training I share this approach with IT and technology communities.",
        ],
        "approach_k": "Approach",
        "approach_h": "Four hats, <em>one desk.</em>",
        "approach_p": "The lawyer who drafts a text, the engineer who ships it as a product, the designer who makes it readable and the trainer who teaches it are usually different people. I try to bring all four to the same desk.",
        "cards": [
            ("scale", "Law", "Technology, IT and regulation", "KVKK and GDPR compliance, Cybersecurity Law No. 7545, e-commerce, internet and advertising rules, intellectual property, mediation."),
            ("code", "Legal engineering", "Turning law into product", "Legal infrastructure for legaltech products, sector-conditional legal text templates, AI governance, LegalOps and process automation."),
            ("design", "Legal design", "Text that gets read and used", "Plain language, layered privacy notices, user-centred contract architecture, without giving up legal accuracy."),
            ("spark", "Audit and compliance", "From obligation to control", "ISO/IEC 27001 ISMS audits, internal control with a COSO approach, regulatory risk analyses, AML compliance and compliance roadmaps."),
        ],
        "areas_k": "Areas I work in",
        "areas_h": "Where I <em>work.</em>",
        "areas_p": "The fields of law I deal with most in my daily work. This is a map of my work, not a catalogue of services.",
        "areas_note": "This section describes fields of activity as permitted by Art. 7(d) of the Turkish Bar Association's Regulation on the Advertising Ban; it does not denote specialisation.",
        "areas": [
            ("Data protection", "Administrative and technical compliance under KVKK and GDPR, data inventories, privacy notices and consent architecture."),
            ("Information security and audit", "ISO/IEC 27001 ISMS audits, certification readiness, Cybersecurity Law No. 7545."),
            ("Internal audit and risk analysis", "Internal control with a COSO approach, regulatory risk analyses, due diligence and compliance roadmaps."),
            ("Compliance and regulation", "Law No. 5549 (AML/MASAK), Law No. 6493 (payment services), regulator correspondence, legislative monitoring."),
            ("Consumer law", "Distance contracts, pre-contractual information, withdrawal and refunds, unfair terms."),
            ("E-commerce law", "Law No. 6563, commercial electronic messages and İYS, seller obligations."),
            ("Internet law", "Law No. 5651, content and hosting provider liability, content removal and access blocking."),
            ("Social media law", "Influencer partnerships, covert advertising, reputation management and content disputes."),
            ("Advertising law", "Commercial advertising principles, substantiating claims, defence and settlement before the Advertising Board."),
            ("Web3 and crypto-asset law", "Regulatory analysis of blockchain projects, smart contracts, DAO structures, on-chain data protection."),
            ("Intellectual property", "Copyright under Law No. 5846, trademarks, software and digital content rights."),
            ("Games and esports law", "Development and publishing agreements, in-game economies, player data."),
            ("AI and technology contracts", "AI governance, SaaS agreements, contract lifecycle management (CLM)."),
            ("Startup law", "Incorporation, investment rounds and shareholders' agreements (SHAs)."),
        ],
        "ld_k": "Legal design, live",
        "ld_h": "One clause, <em>two versions.</em>",
        "ld_p": "Legal design makes a text readable and usable without losing legal accuracy. Below is a single paragraph from an e-commerce privacy notice under Türkiye's data protection law (KVKK). Switch between the two versions.",
        "ld_note": "Illustrative example, not legal advice.",
        "ld_btn": ("Legalese", "Plain language"),
        "ld_legal": "In its capacity as data controller, the Company processes your identity and contact data for the purpose of performing your order, on the legal ground set out in Article 5(2)(c) of the Personal Data Protection Law No. 6698, namely that the processing of personal data belonging to the parties to a contract is necessary, provided that it is directly related to the conclusion or performance of that contract; and, limited to that purpose, such data may be transferred to cargo service providers pursuant to Article 8 of the Law. You may submit requests concerning your rights listed in Article 11 of the Law to the Company.",
        "ld_meter": ["2 sentences", "{words} words", "Readability: hard"],
        "ld_plain_h": "To deliver your order, we need a few details from you.",
        "ld_rows": [
            ("What we use", "Your name, address and phone number."),
            ("Why", "To get your order to you. We don't use it for anything else."),
            ("Legal basis", 'Performance of a contract <code>KVKK Art. 5(2)(c)</code>'),
            ("Who we share it with", 'Only the delivery company <code>KVKK Art. 8</code>'),
            ("Your rights", 'Access, correction, erasure and objection <code>KVKK Art. 11</code>'),
        ],
        "ven_k": "Ventures & products",
        "ven_h": "Founded and <em>built with.</em>",
        "ven_p": "Products whose legal infrastructure I work on and ventures where I hold an active role.",
        "now": "Present",
        "exp_k": "Experience",
        "exp_h": "From courtroom to product team.",
        "exp_p": "From traineeship to today; from case files to the compliance architecture of products. Tap a row for details.",
        "teach_k": "Training & publications",
        "teach_h": "Sharing <em>what I know.</em>",
        "teach_p": "Legal design, legaltech and IT law training; workshops in IT and technology communities.",
        "pub_k": "Article",
        "pub_t": "Web3 and Industry 4.0: recommendations for protecting personal data on the blockchain",
        "pub_d": "On the tension between immutable ledgers and the right to erasure, data minimisation and identifying the data controller.",
        "posts_k": "Writing",
        "posts_h": "Writing compliance <em>clearly.</em>",
        "posts_p": "Each piece answers one compliance question in plain language. Articles are in Turkish; statutory references were checked against primary sources before publication.",
        "edu_k": "Education & certifications",
        "edu_h": "Law, fintech and <em>information systems.</em>",
        "edu_p": "A law degree, then fintech regulation and management information systems; audit and compliance certifications.",
        "edu_t": "Education",
        "cert_t": "Certifications",
        "langs": ["Turkish · native", "English · professional working proficiency"],
        "contact_h": "To say <em>hello.</em>",
        "contact_p": "To talk about my writing, training, or ideas on legaltech and legal design, reach me on LinkedIn or by e-mail.",
        "contact_kvkk": 'If you e-mail me, your personal data is processed as described in the <a href="/en/privacy/">Privacy Notice</a>. Please don\'t include special categories of personal data.',
        "email_btn": "E-mail",
    },
}

HOME_IDS = {
    "tr": {"about": "hakkimda", "approach": "yaklasim", "areas": "alanlar", "ld": "legal-design", "ventures": "girisimler", "exp": "deneyim", "teach": "egitimler", "posts": "yazilar", "edu": "egitim", "contact": "iletisim"},
    "en": {"about": "about", "approach": "approach", "areas": "areas", "ld": "legal-design", "ventures": "ventures", "exp": "experience", "teach": "training", "posts": "writing", "edu": "education", "contact": "contact"},
}

# Deneyim: (tarih_tr, tarih_en, devam?, şirket, rol_tr, rol_en, yer_tr, yer_en, [madde_tr], [madde_en])
EXPERIENCE = [
    ("", "", True, "GameLaw.io", "Team Lead", "Team Lead", "", "",
     ["Oyun geliştiricileri, stüdyolar, yayıncılar, yatırımcılar ve espor ekosistemi için kurulan hukuki altyapı platformunda ekip liderliği.",
      "Platform; sözleşmeden fikrî mülkiyete, veri korumadan küresel pazara açılmaya kadar oyunun yaşam döngüsünü hukuki açıdan ele alıyor: oyun, uygulama ve web sitesi yasallık analizi, dijital due diligence, rehberler, yol haritaları ve sözleşme havuzu."],
     ["Team lead at a legal infrastructure platform for game developers, studios, publishers, investors and the esports ecosystem.",
      "The platform covers the game lifecycle from contracts and IP to data protection and global expansion: game, app and website legality analysis, digital due diligence, guides, roadmaps and a contract library."]),
    ("Ekim 2025", "Oct 2025", True, "Karataş & Partners Hukuk Bürosu", "Avukat · Teknoloji Hukuku, Uyum ve Denetim, Eğitmen", "Attorney · Technology Law, Compliance & Audit, Trainer", "İstanbul", "Istanbul",
     ["7545 sayılı Siber Güvenlik Kanunu, KVKK, GDPR, 6563, 5809 ve 5651 sayılı kanunlar kapsamında regülasyon uyumu ve uyum yol haritaları.",
      "ISO/IEC 27001 BGYS kapsamında şirket denetimleri ve belgelendirmeye hazırlık; denetim bulgularının ve risk analizlerinin raporlanması.",
      "KVKK uyum projeleri (mobil, web ve fiziksel ortam): veri envanteri, aydınlatma ve açık rıza metinleri, uyum dokümantasyonu.",
      "COSO yaklaşımıyla iç kontrol ve iç denetim, risk analizi ve ölçeklendirme; hukuki durum tespiti (due diligence) ve risk raporlama.",
      "Yapay zekâ, Web3, fintek, e-ticaret ve SaaS ürünleri için hukuki risk analizleri; SaaS sözleşmeleri, sözleşme yönetimi (CLM) ve müzakere.",
      "Girişim hukuku ve yatırım turları (şirketleşme, SHA); Türkiye, Avrupa ve MENA'da şirket işlemleri; şirketler ve sağlık hukuku danışmanlığı.",
      "Reklam Kurulu nezdinde savunma ve uzlaşma; FSEK ve marka uyuşmazlıkları; arabuluculuk. Legal design, uyum mimarisi ve kurumsal eğitimler."],
     ["Regulatory compliance and compliance roadmaps under Cybersecurity Law No. 7545, KVKK, GDPR and Laws No. 6563, 5809 and 5651.",
      "Company audits and certification readiness under ISO/IEC 27001 ISMS; reporting of audit findings and risk analyses.",
      "KVKK compliance projects (mobile, web and physical): data inventories, privacy notices, explicit consent texts and documentation.",
      "Internal control and internal audit with a COSO approach; risk analysis, due diligence and risk reporting.",
      "Legal risk analyses for AI, Web3, fintech, e-commerce and SaaS products; SaaS agreements, contract lifecycle management (CLM) and negotiation.",
      "Startup law and investment rounds (incorporation, SHAs); corporate transactions in Türkiye, Europe and MENA; corporate and health law advisory.",
      "Defence and settlement before the Advertising Board; copyright and trademark disputes; mediation. Legal design, compliance architecture and corporate training."]),
    ("Eylül 2025", "Sep 2025", True, "Legalitify", "Legal Engineer · Startup Yöneticisi", "Legal Engineer · Startup Manager", "Birleşik Krallık · uzaktan", "United Kingdom · remote",
     ["Web sitelerini KVKK ve e-ticaret mevzuatına uyum açısından tarayan, eksik hukuki metinleri tespit edip üreten legaltech/SaaS ürününün hukuki altyapısı, uyum mimarisi ve dokümantasyonu.",
      "Kullanıcı odaklı, entegrasyona uygun sözleşme mimarileri ve sektöre göre koşullu hukuki metin şablonları; legal design ilkeleriyle.",
      "Yapay zekâ destekli uyum analizinde AI yönetişimi, KVKK/GDPR uyumu ve risk analizi.",
      "LegalOps'un dijital araçlarla modernizasyonu; süreç verimliliği ve KPI odaklı büyüme takibi."],
     ["Legal infrastructure, compliance architecture and documentation for a legaltech/SaaS product that scans websites for KVKK and e-commerce compliance, flags missing legal texts and generates them.",
      "User-centred, integration-ready contract architectures and sector-conditional legal text templates, built on legal design principles.",
      "AI governance, KVKK/GDPR compliance and risk analysis for AI-assisted compliance analysis tools.",
      "Modernising LegalOps with digital tools; process efficiency and KPI-driven growth tracking."]),
    ("Mart 2025 – Haziran 2026", "Mar 2025 – Jun 2026", False, "PARAM · Türk Elektronik Para A.Ş.", "Avukat · KVKK ve Regülasyon Uyumu (TÖDEB Fintek Çıraklık Programı)", "Attorney · KVKK & Regulatory Compliance (TÖDEB Fintech Apprenticeship)", "Ankara · hibrit", "Ankara · hybrid",
     ["5549 (MASAK), 6493 (ödeme hizmetleri ve elektronik para) ve 6698 sayılı kanunlar çerçevesinde grup şirketlerinin uyum süreçleri, yükümlülük analizi ve risk raporlaması.",
      "Şüpheli işlem izleme uyumu; ödeme sistemleri, e-ticaret ve sosyal medya süreçlerine ilişkin regülatif risk analizleri.",
      "Kişisel veri envanteri, aydınlatma ve açık rıza metinleri, politika ve prosedürler; sözleşmeler ve web sitesi denetimleri.",
      "MASAK, TÖDEB ve TCMB yazışmaları; mevzuat takibi, eğitim içeriklerinin hazırlanması ve sunumu."],
     ["Compliance processes, obligation analyses and risk reporting for group companies under Laws No. 5549 (AML/MASAK), 6493 (payment services and e-money) and 6698 (KVKK).",
      "Suspicious transaction monitoring compliance; regulatory risk analyses for payment systems, e-commerce and social media processes.",
      "Personal data inventories, privacy notices, explicit consent texts, policies and procedures; contracts and website audits.",
      "Correspondence with MASAK, TÖDEB and the Central Bank; legislative monitoring, preparing and delivering training content."]),
    ("Ağustos – Aralık 2024", "Aug – Dec 2024", False, "GlobalTechs Company", "Blokzincir Araştırmacısı", "Blockchain Researcher", "Birleşik Krallık · uzaktan", "United Kingdom · remote",
     ["Blokzincir alanında regülasyon takibi, uyumluluk analizi ve raporlama."],
     ["Regulatory monitoring, compliance analysis and reporting in the blockchain field."]),
    ("Mayıs – Eylül 2024", "May – Sep 2024", False, "HTO Hukuk & Danışmanlık", "Avukat", "Attorney", "Ankara", "Ankara",
     ["Dava takibi ve vekillik, sözleşme süreçleri, KVKK metinleri, mevzuat takibi ve hukuki görüş."],
     ["Case management and representation, contracts, KVKK documentation, legislative monitoring and legal opinions."]),
    ("Haziran 2023 – Şubat 2025", "Jun 2023 – Feb 2025", False, "Sencer & Partners", "Kurucu · Avukat · Eğitmen", "Founder · Attorney · Trainer", "Ankara · hibrit", "Ankara · hybrid",
     ["Arabuluculuk, tahkim ve duruşma temsili; hukuki görüş ve uyum projeleri.",
      "Girişim kuruluşu, yatırım süreçleri ve hissedarlar sözleşmeleri (SHA); hukuk teknolojileri ve inovasyon atölyeleri."],
     ["Mediation, arbitration and court representation; legal opinions and compliance projects.",
      "Startup incorporation, investment processes and shareholders' agreements (SHAs); legal technology and innovation workshops."]),
    ("Ocak 2023 – Mayıs 2024", "Jan 2023 – May 2024", False, "H. Güzel Hukuk & Danışmanlık", "Stajyer Avukat", "Trainee Lawyer", "Ankara", "Ankara",
     ["Dava açılış işlemleri, dilekçe hazırlama ve duruşma temsili; sözleşme ve icra süreçleri."],
     ["Filing proceedings, drafting pleadings and court representation; contracts and enforcement proceedings."]),
]

VENTURES = [
    ("GameLaw.io", "https://gamelaw.io", "Güncel", "Current", "Team Lead", "Team Lead",
     "Oyun ekosisteminin hukuki altyapısı: geliştiriciler, stüdyolar, yayıncılar, yatırımcılar ve espor için analiz araçları, rehberler ve sözleşme havuzu.",
     "Legal infrastructure for the games ecosystem: analysis tools, guides and a contract library for developers, studios, publishers, investors and esports.", True),
    ("Legalitify", "https://legalitify.com", "2025 –", "2025 –", "Legal Engineer · Startup Yöneticisi", "Legal Engineer · Startup Manager",
     "Web sitelerini, reklamları ve sözleşmeleri veri koruma, tüketici ve reklam mevzuatına göre tarayıp mevzuat atıflı düzeltme öneren legaltech ürünü.",
     "A legaltech product that scans websites, ads and contracts against data protection, consumer and advertising law and proposes cited fixes.", False),
    ("Lexprotect · Lexzero · Banfake", "", "2025 –", "2025 –", "Startup Yöneticisi", "Startup Manager",
     "Legaltech girişim portföyü: altyapı, uyum ve operasyon stratejileri; KPI odaklı büyüme takibi.",
     "A legaltech startup portfolio: infrastructure, compliance and operations strategy; KPI-driven growth tracking.", False),
    ("Türkiye Fintek Topluluğu", "", "2025 –", "2025 –", "Kurucu Üye · Genel Sekreter · Eğitmen", "Founding Member · Secretary General · Trainer",
     "5549, 6493 ve 6698 sayılı kanunlar kapsamında insurtech, fintech, regtech, ödeme hizmetleri, Web3, blokzincir, akıllı sözleşmeler ve DAO eğitimleri.",
     "Training and workshops on insurtech, fintech, regtech, payment services, Web3, blockchain, smart contracts and DAOs under Laws No. 5549, 6493 and 6698.", False),
    ("Elaw Startup", "", "2024 – 2025", "2024 – 2025", "Kurucu", "Founder",
     "Hukuk teknolojileri alanında kurduğum ilk girişim.",
     "My first venture in legal technology.", False),
    ("Sencer & Partners", "", "2023 – 2025", "2023 – 2025", "Kurucu", "Founder",
     "Arabuluculuk, tahkim ve uyum projeleri; girişim kuruluşu ve yatırım süreçleri; hukuk teknolojileri atölyeleri.",
     "Mediation, arbitration and compliance projects; startup incorporation and investment processes; legal technology workshops.", False),
]

TEACHING = [
    ("Bilişim ve teknoloji toplulukları", "Bilişim ve teknoloji toplulukları", "", "Eğitmen", "Trainer", "Legal design, legaltech ve bilişim hukuku eğitimleri ve atölyeleri.", "Legal design, legaltech and IT law training and workshops."),
    ("TÜBİTAK", "TÜBİTAK", "", "Eğitmen ve Mentor", "Trainer & Mentor", "Fikri ve sınai haklar, şirketler hukuku ve yatırım süreçleri.", "Intellectual and industrial property, corporate law and investment processes."),
    ("Türkiye İhracatçılar Birliği", "Turkish Exporters' Assembly", "", "Eğitmen", "Trainer", "Üye firmalara uluslararası ticaret hukuku ve regülasyon uyumu.", "International trade law and regulatory compliance for member companies."),
    ("Türkiye Fintek Topluluğu", "Türkiye Fintech Community", "2025 –", "Kurucu Üye · Eğitmen", "Founding Member · Trainer", "Fintek, regtech, ödeme hizmetleri ve Web3 atölyeleri.", "Fintech, regtech, payment services and Web3 workshops."),
    ("Solana Allstars Academy Türkiye", "Solana Allstars Academy Türkiye", "2025 – 2026", "Temsilci", "Representative", "Web3 ve blokzincir.", "Web3 and blockchain."),
    ("Yenilikçi Hukuk Akademisi", "Innovative Law Academy", "2023 – 2024", "Eğitmen", "Trainer", "Hukuk ve inovasyon eğitimleri.", "Law and innovation training."),
    ("Tekno Hukuk Akademisi", "Techno Law Academy", "2023 – 2024", "Ar-Ge Temsilcisi · Eğitmen", "R&D Representative · Trainer", "Legal design ve legaltech.", "Legal design and legaltech."),
]

EDUCATION = [
    ("Atatürk Üniversitesi", "Atatürk University", "Hukuk Fakültesi, lisans", "Faculty of Law, LL.B.", "2018 – 2022", "2018 – 2022", "Erzurum"),
    ("Marmara Üniversitesi", "Marmara University", "TÖDEB Fintek Programı: regülasyon ve uyum, siber güvenlik, finans ve teknoloji", "TÖDEB Fintech Programme: regulation & compliance, cybersecurity, finance & technology", "2024 – 2025", "2024 – 2025", "İstanbul"),
    ("Anadolu Üniversitesi", "Anadolu University", "Açıköğretim Fakültesi, Yönetim Bilişim Sistemleri lisans", "Open Education Faculty, Management Information Systems (B.Sc.)", "2024 – devam", "2024 – present", "Eskişehir"),
]

CERTS = [
    ("MASAK Uyum Görevlisi Lisansı", "MASAK Compliance Officer Licence", "Mali Suçları Araştırma Kurulu", "Financial Crimes Investigation Board", "2026", True),
    ("ISO/IEC 27001 BGYS Baş Denetçi (Lead Auditor)", "ISO/IEC 27001 ISMS Lead Auditor", "Exemplar Global / TÜRKAK", "Exemplar Global / TÜRKAK", "2025", True),
    ("TÖDEB Fintek Çıraklık Programı", "TÖDEB Fintech Apprenticeship Programme", "Türkiye Ödeme ve Elektronik Para Kuruluşları Birliği · 9 ay, 147 saat", "Association of Payment and E-Money Institutions of Türkiye · 9 months, 147 hours", "2024 – 2025", False),
    ("Paris Anlaşması ve Sürdürülebilir Kalkınma", "Paris Agreement and Sustainable Development", "University of Cambridge", "University of Cambridge", "2024", False),
    ("Bilişim Hukuku Bootcamp", "IT Law Bootcamp", "Legal Talks", "Legal Talks", "2024", False),
    ("Hukuk ve Teknoloji Kampı", "Law and Technology Camp", "AYBÜ", "AYBÜ", "2024", False),
    ("Girişimcilik ve İnovasyon Okulu", "Entrepreneurship & Innovation School", "Anbean Kampüs", "Anbean Kampüs", "2024", False),
    ("Genç Pythian Programı", "Young Pythian Programme", "PythianGO", "PythianGO", "2024", False),
    ("Legal Design / Legaltech", "Legal Design / Legaltech", "Tekno Hukuk Akademisi", "Tekno Hukuk Akademisi", "2022 – 2024", False),
]

# ---------------------------------------------------------------- yazı yardımcıları
def post_words(p):
    return len(re.sub(r"<[^>]+>", " ", p["body"]).split())

for p in POSTS:
    p["rt"] = max(2, ceil(post_words(p) / 200))
POSTS.sort(key=lambda p: p["date"], reverse=True)

def cover(i):
    """Her yazı için sabit, soyut bir kapak: üç şekil, tek vurgu."""
    presets = [
        [("a", 18, 30, 70, 70), ("", 55, 45, 34, 34), ("o", 70, 10, 90, 90)],
        [("", 8, 55, 160, 26), ("a", 60, 20, 44, 44), ("o", 30, 12, 60, 60)],
        [("o", 12, 18, 110, 110), ("a", 62, 52, 52, 52), ("", 40, 30, 16, 16)],
        [("", 20, 60, 90, 22), ("", 45, 30, 90, 22), ("a", 72, 18, 22, 22)],
        [("a", 10, 20, 30, 30), ("o", 30, 20, 30, 30), ("", 50, 20, 30, 30)],
        [("", 50, 8, 130, 130), ("a", 20, 40, 60, 60)],
        [("o", 8, 40, 200, 44), ("a", 58, 36, 54, 54)],
        [("", 14, 26, 64, 64), ("a", 44, 50, 64, 64), ("o", 70, 12, 64, 64)],
    ]
    spans = "".join(
        f'<span class="{c}" style="left:{x}%;top:{y}%;width:{w}px;height:{h}px"></span>'
        for c, x, y, w, h in presets[(i - 1) % len(presets)])
    return f'<div class="cover" aria-hidden="true">{spans}</div>'

def post_card(p, lang, extra_cls="", h="h3"):
    L = lang == "en"
    title = p["title_en"] if L else p["title"]
    cat = p["cat_en"] if L else p["cat"]
    tr_note = ' <span class="sr-only">(in Turkish)</span>' if L else ""
    hl = ' hreflang="tr"' if L else ""
    return f'''
        <a class="post rv{extra_cls}" href="/yazilar/{p["slug"]}/"{hl}>
          {cover(p["cover"])}
          <div class="meta"><span class="cat">{e(cat)}</span><span>{fmt_date(p["date"], lang)} · {p["rt"]} {UI[lang]["read"]}</span></div>
          <{h}>{e(title)}{tr_note}</{h}>
          <span class="go">{"Read (Turkish)" if L else "Oku"} {ICON["arrow"]}</span>
        </a>'''

# ---------------------------------------------------------------- şablon
HEAD_SCRIPT = ("(function(){try{var c=JSON.parse(localStorage.getItem('sz-consent')||'null');"
               "if(c&&c.v===1&&c.pref&&Date.now()-c.ts<31536e6){var t=localStorage.getItem('sz-theme');"
               "if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();")

def consent_panel(lang):
    c = UI[lang]["consent"]
    return f'''
<section id="consent" class="consent" aria-labelledby="consent-title" hidden data-on="{e(c["on"])}" data-off="{e(c["off"])}">
  <button class="x" type="button" aria-label="{e(c["close"])}" hidden>{ICON["x"]}</button>
  <h2 id="consent-title" tabindex="-1">{e(c["title"])}</h2>
  <p>{c["text"]}</p>
  <div class="prefs" id="consent-prefs" hidden>
    <div class="cat"><strong>{e(c["need"])}</strong><span class="always">{e(c["always"])}</span><span class="d">{c["need_d"]}</span></div>
    <div class="cat"><label for="pref-toggle"><strong>{e(c["pref"])}</strong></label><span class="switch"><input type="checkbox" id="pref-toggle" role="switch"><i aria-hidden="true"></i></span><span class="d">{c["pref_d"]}</span></div>
    <button class="save" type="button" data-c="save">{e(c["save"])}</button>
  </div>
  <div class="row">
    <button type="button" data-c="reject">{e(c["reject"])}</button>
    <button type="button" data-c="prefs" aria-expanded="false" aria-controls="consent-prefs">{e(c["prefs"])}</button>
    <button type="button" data-c="accept">{e(c["accept"])}</button>
  </div>
  <p class="state" aria-live="polite"></p>
</section>'''

def header(lang, alt):
    u = UI[lang]
    nav = "".join(f'<a class="nav-link" href="{h}">{e(t)}</a>' for h, t in u["nav"])
    if lang == "tr":
        sw = f'<span aria-current="true">TR</span><a href="{alt}" hreflang="en" lang="en">EN</a>'
    else:
        sw = f'<a href="{alt}" hreflang="tr" lang="tr">TR</a><span aria-current="true">EN</span>'
    home = P("home", lang)
    return f'''
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{home}"><span class="brand-mark" aria-hidden="true">s</span><span>{NAME}</span></a>
    <nav class="nav" aria-label="{u["nav_label"]}">{nav}<span class="lang">{sw}</span><button class="theme-btn" type="button" data-theme-toggle aria-pressed="false" aria-label="{e(u["theme"])}">{ICON["moon"]}{ICON["sun"]}</button></nav>
  </div>
</header>'''

def footer(lang):
    u = UI[lang]
    cols = []
    for title, links in u["foot_cols"]:
        items = []
        for h, t in links:
            if h == "#consent":
                items.append(f'<li><button type="button" class="linklike" data-consent-open>{e(t)}</button></li>')
            else:
                ext = ' target="_blank" rel="noopener"' if h.startswith("http") else ""
                lng = ' lang="en" hreflang="en"' if h == "/en/" and lang == "tr" else (' lang="tr" hreflang="tr"' if h == "/" and lang == "en" else "")
                items.append(f'<li><a href="{h}"{ext}{lng}>{e(t)}</a></li>')
        cols.append(f'<div><h2>{e(title)}</h2><ul>{"".join(items)}</ul></div>')
    bottom = "".join(f"<p>{e(x)}</p>" for x in u["foot_bottom"])
    legal = P("legal", lang)
    return f'''
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-id"><strong>{NAME}</strong><p>{e(u["foot_tag"])}</p><p><a href="{legal}#{"reklam-yasagi" if lang == "tr" else "advertising"}">{e(u["foot_note"])}</a></p></div>
      {"".join(cols)}
    </div>
    <div class="foot-bottom">{bottom}</div>
  </div>
</footer>'''

def layout(lang, *, title, desc, path, alt, body, og_image=None, extra_head=""):
    url = SITE + path
    og = og_image or f'{SITE}/assets/img/og{"-en" if lang == "en" else ""}.png'
    tr_url, en_url = (path, alt) if lang == "tr" else (alt, path)
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{NAME}">
<meta name="theme-color" content="#ecebe7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121211" media="(prefers-color-scheme: dark)">
<script>{HEAD_SCRIPT}</script>
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="tr" href="{SITE}{tr_url}">
<link rel="alternate" hreflang="en" href="{SITE}{en_url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{"en_US" if lang == "en" else "tr_TR"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/Geist-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">{extra_head}
</head>
<body>
<a class="skip" href="#main">{e(UI[lang]["skip"])}</a>
{consent_panel(lang)}
{header(lang, alt)}
<main id="main">
{body}
</main>
{footer(lang)}
<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def sec_head(kicker, h2, p, hid):
    return f'''
      <div class="sec-head rv">
        <div><div class="kicker">{e(kicker)}</div><h2 id="{hid}">{h2}</h2></div>
        <p>{e(p)}</p>
      </div>'''

def crumbs(lang, items):
    lis = "".join(f'<li><a href="{h}">{e(t)}</a></li>' if h else f'<li aria-current="page">{e(t)}</li>' for h, t in items)
    return f'<nav class="crumbs" aria-label="{"Breadcrumb" if lang == "en" else "Konum"}"><ol>{lis}</ol></nav>'

# ---------------------------------------------------------------- ana sayfa
def home(lang):
    c = HOME[lang]; ids = HOME_IDS[lang]; L = lang == "en"; u = UI[lang]

    chips = "".join(f'<li class="{"hl" if m in c["marquee_hl"] else ""}">{e(m)}</li>' for m in c["marquee"])
    about = "".join(f"<p>{e(x)}</p>" for x in c["about"])
    cards = "".join(f'''
        <article class="card rv">
          <div class="glyph">{ICON[ic]}</div>
          <div class="tag">{e(tag)}</div>
          <h3>{e(h)}</h3>
          <p>{e(p)}</p>
        </article>''' for ic, tag, h, p in c["cards"])
    areas = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in c["areas"])
    words = len(c["ld_legal"].split())
    ld_meter = "".join(f"<span>{e(m.format(words=words))}</span>" for m in c["ld_meter"])
    ld_rows = "".join(f"<div><dt>{e(k)}</dt><dd>{v}</dd></div>" for k, v in c["ld_rows"])

    vents = []
    for name, href, yt, ye, rt, re_, dt, de, feat in VENTURES:
        tag = "a" if href else "div"
        attrs = f' href="{href}" target="_blank" rel="noopener"' if href else ""
        arrow = f'<span class="arrow">{ICON["ne"]}</span>' if href else ""
        vents.append(f'''
        <{tag} class="v rv{" feature" if feat else ""}"{attrs}>
          <div class="top"><span class="yr">{e(yr(ye if L else yt, lang))}</span>{arrow}</div>
          <h3>{e(name)}</h3>
          <div class="role">{e(re_ if L else rt)}</div>
          <p>{e(de if L else dt)}</p>
        </{tag}>''')

    exp = []
    for i, (dtr, den, cur, co, rtr, ren, wtr, wen, btr, ben) in enumerate(EXPERIENCE):
        d = den if L else dtr
        when = ((f'{e(d)} – ' if d else "") + f'<span class="now">{e(c["now"])}</span>') if cur else e(d)
        bullets = "".join(f"<li>{e(b)}</li>" for b in (ben if L else btr))
        exp.append(f'''
        <li class="rv">
          <details{" open" if i == 0 else ""}>
            <summary>
              <span class="when">{when}</span>
              <h3 class="what">{e(co)}<span>{e(ren if L else rtr)}</span></h3>
              <span class="where">{e(wen if L else wtr)}</span>
              <span class="plus">{ICON["plus"]}</span>
            </summary>
            <div class="body"><div></div><ul>{bullets}</ul></div>
          </details>
        </li>''')

    teach = "".join(f'''
        <li class="rv"><strong>{e(ne if L else nt)} <span class="teach-role">· {e(re_ if L else rt)}</span></strong><span class="yr">{e(yr(y, lang))}</span><span class="d">{e(de if L else dt)}</span></li>'''
        for nt, ne, y, rt, re_, dt, de in TEACHING)

    posts = "".join(post_card(p, lang) for p in POSTS[:3])
    edu = "".join(f'''
          <li><strong>{e(se if L else st)}</strong><span class="yr">{e(ye if L else yt)}</span><span class="d">{e(de if L else dt)} · {e(place)}</span></li>'''
        for st, se, dt, de, yt, ye, place in EDUCATION)
    certs = "".join(f'''
          <li class="{"key" if k else ""}"><strong>{e(ne if L else nt)}</strong><span class="yr">{e(y)}</span><span class="d">{e(oe if L else ot)}</span></li>'''
        for nt, ne, ot, oe, y, k in CERTS)
    langs = "".join(f"<span>{e(x)}</span>" for x in c["langs"])
    b1, b2 = c["ld_btn"]

    body = f'''
  <section class="hero" aria-labelledby="h-name">
    <div class="wrap hero-grid">
      <div>
        <a class="status" href="https://gamelaw.io" target="_blank" rel="noopener"><span class="pulse" aria-hidden="true"></span>{e(c["status"])}</a>
        <h1 id="h-name"><span class="ln">Ahmet Sencer</span><span class="ln">Zararsız</span></h1>
        <p class="lead">{c["lead"]}</p>
        <div class="cta">
          <a class="btn btn-ink" href="{LINKEDIN}" target="_blank" rel="noopener">{ICON["in"]} {e(c["cta1"])}</a>
          <a class="btn btn-line" href="{P("posts", lang)}">{e(c["cta2"])} {ICON["arrow"]}</a>
        </div>
      </div>
      <figure class="reel" style="margin:0">
        <div class="reel-frame" role="img" aria-label="{e(c["reel_label"])}"><div data-reel style="position:absolute;inset:0"></div></div>
        <figcaption class="reel-bar">
          <p class="reel-cap">{e(c["reel_cap"])}</p>
          <button class="reel-toggle" type="button" data-reel-toggle aria-pressed="false" data-pause="{e(c["reel_pause"])}" data-play="{e(c["reel_play"])}">{ICON["pause"]}{ICON["play"]}<span class="lbl">{e(c["reel_pause"])}</span></button>
        </figcaption>
      </figure>
    </div>
  </section>

  <div class="marquee" role="region" aria-label="{"Fields" if L else "Alanlar"}" tabindex="0"><div class="marquee-track"><ul>{chips}</ul><ul aria-hidden="true">{chips}</ul></div></div>

  <section class="block" id="{ids["about"]}" aria-labelledby="h-about">
    <div class="wrap about">
      <div class="rv"><div class="kicker">{e(c["about_k"])}</div><h2 id="h-about" class="big">{c["about_big"]}</h2></div>
      <div class="body rv">{about}<div class="sign" aria-hidden="true">{NAME}</div></div>
    </div>
  </section>

  <section class="block" id="{ids["approach"]}" aria-labelledby="h-approach">
    <div class="wrap">{sec_head(c["approach_k"], c["approach_h"], c["approach_p"], "h-approach")}
      <div class="cards">{cards}
      </div>
    </div>
  </section>

  <section class="block" id="{ids["areas"]}" aria-labelledby="h-areas">
    <div class="wrap">{sec_head(c["areas_k"], c["areas_h"], c["areas_p"], "h-areas")}
      <ul class="areas">{areas}</ul>
      <p class="areas-note">{e(c["areas_note"])}</p>
    </div>
  </section>

  <section class="block" id="{ids["ld"]}" aria-labelledby="h-ld">
    <div class="wrap">
      <div class="ld">
        <div class="ld-side rv">
          <div class="kicker">{e(c["ld_k"])}</div>
          <h2 id="h-ld" class="ld-title">{c["ld_h"]}</h2>
          <p>{e(c["ld_p"])}</p>
          <div class="seg" data-ld data-mode="legal" role="group" aria-label="{"Version" if L else "Sürüm"}">
            <span class="pill" aria-hidden="true"></span>
            <button type="button" data-mode="legal" aria-pressed="true">{e(b1)}</button>
            <button type="button" data-mode="plain" aria-pressed="false">{e(b2)}</button>
          </div>
          <p class="note">{e(c["ld_note"])}</p>
        </div>
        <div class="ld-stage rv" aria-live="polite">
          <div class="ld-pane ld-legal"><p>{e(c["ld_legal"])}</p><div class="meter">{ld_meter}</div></div>
          <div class="ld-pane ld-plain" hidden><h3>{e(c["ld_plain_h"])}</h3><dl class="ld-rows">{ld_rows}</dl></div>
        </div>
      </div>
    </div>
  </section>

  <section class="block" id="{ids["ventures"]}" aria-labelledby="h-ven">
    <div class="wrap">{sec_head(c["ven_k"], c["ven_h"], c["ven_p"], "h-ven")}
      <div class="ventures">{"".join(vents)}
      </div>
    </div>
  </section>

  <section class="block" id="{ids["exp"]}" aria-labelledby="h-exp">
    <div class="wrap">{sec_head(c["exp_k"], e(c["exp_h"]), c["exp_p"], "h-exp")}
      <ol class="tl">{"".join(exp)}
      </ol>
    </div>
  </section>

  <section class="block" id="{ids["teach"]}" aria-labelledby="h-teach">
    <div class="wrap">{sec_head(c["teach_k"], c["teach_h"], c["teach_p"], "h-teach")}
      <ul class="teach">{teach}
      </ul>
      <div class="pub rv"><div class="ic">{ICON["book"]}</div><div><small>{e(c["pub_k"])}</small><strong>{e(c["pub_t"])}</strong><p>{e(c["pub_d"])}</p></div></div>
    </div>
  </section>

  <section class="block" id="{ids["posts"]}" aria-labelledby="h-posts">
    <div class="wrap">{sec_head(c["posts_k"], c["posts_h"], c["posts_p"], "h-posts")}
      <div class="posts">{posts}
      </div>
      <div class="more"><a class="btn btn-line" href="{P("posts", lang)}">{e(u["all_posts"])} {ICON["arrow"]}</a></div>
    </div>
  </section>

  <section class="block" id="{ids["edu"]}" aria-labelledby="h-edu">
    <div class="wrap">{sec_head(c["edu_k"], c["edu_h"], c["edu_p"], "h-edu")}
      <div class="edu">
        <div class="rv"><h3>{e(c["edu_t"])}</h3><ul class="list">{edu}
          </ul><div class="langs">{langs}</div></div>
        <div class="rv"><h3>{e(c["cert_t"])}</h3><ul class="list">{certs}
          </ul></div>
      </div>
    </div>
  </section>

  <section id="{ids["contact"]}" aria-labelledby="h-contact">
    <div class="wrap">
      <div class="contact rv">
        <span class="orb" aria-hidden="true"></span><span class="orb b" aria-hidden="true"></span>
        <span class="who">{NAME}</span>
        <h2 id="h-contact">{c["contact_h"]}</h2>
        <p>{e(c["contact_p"])}</p>
        <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
        <div class="links">
          <a href="{LINKEDIN}" target="_blank" rel="noopener">{ICON["in"]} LinkedIn</a>
          <a href="mailto:{EMAIL}">{ICON["mail"]} {e(c["email_btn"])}</a>
        </div>
        <p class="kvkk">{c["contact_kvkk"]}</p>
      </div>
    </div>
  </section>'''
    other = P("home", "en" if lang == "tr" else "tr")
    return layout(lang, title=c["title"], desc=c["desc"], path=P("home", lang), alt=other, body=body,
                  extra_head="")

# ---------------------------------------------------------------- yazı listesi
def posts_index(lang):
    L = lang == "en"
    title = "Writing" if L else "Yazılar"
    sub = ("Compliance questions answered in plain language. The articles are in Turkish; every statutory reference was checked against primary sources."
           if L else "Uyum sorularını sade bir dille ele alan yazılar. Her yazıdaki mevzuat atfı yayın öncesinde birincil kaynaktan kontrol edildi.")
    cards = "".join(post_card(p, lang, h="h2") for p in POSTS)
    body = f'''
  <div class="wrap">
    <div class="page-head">
      {crumbs(lang, [(P("home", lang), UI[lang]["home"]), (None, title)])}
      <h1>{"Writing compliance <em>clearly.</em>" if L else "Uyumu anlaşılır <em>yazmak.</em>"}</h1>
      <p class="sub">{e(sub)}</p>
    </div>
    <div class="posts">{cards}
    </div>
    <p class="disclaimer">{e(UI[lang]["disclaimer"])}</p>
  </div>'''
    return layout(lang, title=f"{title} · {NAME}", desc=sub, path=P("posts", lang),
                  alt=P("posts", "en" if lang == "tr" else "tr"), body=body)

# ---------------------------------------------------------------- yazı sayfası
def add_h2_ids(html):
    toc = []
    def rep(m):
        text = m.group(1)
        hid = slugify(text)
        toc.append((hid, re.sub(r"<[^>]+>", "", text)))
        return f'<h2 id="{hid}">{text}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", rep, html), toc

def post_page(p):
    lang = "tr"; u = UI[lang]
    body_html, toc = add_h2_ids(p["body"])
    toc_html = "".join(f'<li><a href="#{h}">{e(t)}</a></li>' for h, t in toc)
    srcs = "".join(f'<li>{e(SRC[k][0])}. <a href="{SRC[k][1]}" rel="noopener" target="_blank">{e(SRC[k][1].split("//")[1].split("/")[0])}</a> ({u["accessed"]} {ACCESS})</li>' for k in p["src"])
    others = [x for x in POSTS if x["slug"] != p["slug"]][:3]
    more = "".join(post_card(x, lang) for x in others)
    body = f'''
  <article class="wrap">
    <div class="page-head">
      {crumbs(lang, [("/", u["home"]), ("/yazilar/", "Yazılar"), (None, p["title"])])}
      <h1>{e(p["title"])}</h1>
      <p class="sub">{e(p["excerpt"])}</p>
      <div class="meta"><span>{u["by"]} {NAME}</span><span><time datetime="{p["date"]}">{fmt_date(p["date"], lang)}</time></span><span>{p["rt"]} {u["read"]}</span><span>{e(p["cat"])}</span></div>
    </div>
    <div class="doc-layout">
      <div>
        <div class="prose">{body_html}
          <h2 id="kaynakca">{u["sources"]}</h2>
          <ol class="note">{srcs}</ol>
          <p class="note">{e(u["first"].format(d=fmt_date(p["date"], lang)))}</p>
        </div>
        <p class="disclaimer">{e(u["disclaimer"])}</p>
      </div>
      <aside class="toc" aria-label="{u["toc"]}"><h2>{u["toc"]}</h2><ol>{toc_html}<li><a href="#kaynakca">{u["sources"]}</a></li></ol></aside>
    </div>
    <section class="post-more" aria-labelledby="h-more">
      <h2 id="h-more">{u["more"]}</h2>
      <div class="posts">{more}</div>
    </section>
  </article>'''
    return layout(lang, title=f'{p["title"]} · {NAME}', desc=p["excerpt"], path=f'/yazilar/{p["slug"]}/',
                  alt="/en/writing/", body=body)

# ---------------------------------------------------------------- hukuki sayfalar
LEGAL_PAGES = {
    "kvkk": ({"tr": "KVKK Aydınlatma Metni", "en": "Privacy Notice"},
             {"tr": "Bu sitede hangi kişisel verinin, hangi amaçla ve hangi hukuki sebeple işlendiği; haklarınız ve nasıl başvuracağınız.",
              "en": "Which personal data is processed on this site, why and on what legal ground; your rights and how to apply."},
             {"tr": LG.KVKK_TR, "en": LG.KVKK_EN}),
    "cookies": ({"tr": "Çerez Politikası", "en": "Cookie Policy"},
                {"tr": "Bu site çerez kullanmaz. Tarayıcınıza neyin, ne zaman ve ne kadar süreyle yazıldığı.",
                 "en": "This site uses no cookies. What is written to your browser, when and for how long."},
                {"tr": LG.COOKIES_TR, "en": LG.COOKIES_EN}),
    "terms": ({"tr": "Kullanım Koşulları", "en": "Terms of Use"},
              {"tr": "Sitenin niteliği, yazıların hukuki görüş olmaması, fikrî haklar ve dış bağlantılar.",
               "en": "What this site is, why articles are not legal advice, intellectual property and external links."},
              {"tr": LG.TERMS_TR, "en": LG.TERMS_EN}),
    "legal": ({"tr": "Yasal Bilgiler", "en": "Legal Notice"},
              {"tr": "Site sahibi, yer sağlayıcı ve avukatlık reklam yasağına ilişkin beyan.",
               "en": "Site owner, hosting provider and statement on the advertising ban for attorneys."},
              {"tr": LG.LEGAL_TR, "en": LG.LEGAL_EN}),
    "a11y": ({"tr": "Erişilebilirlik Beyanı", "en": "Accessibility Statement"},
             {"tr": "WCAG 2.2 AA hedefi, aldığım önlemler, bilinen eksikler ve geri bildirim yolu.",
              "en": "WCAG 2.2 AA target, measures taken, known gaps and how to give feedback."},
             {"tr": LG.A11Y_TR, "en": LG.A11Y_EN}),
}

def legal_page(key, lang):
    titles, subs, bodies = LEGAL_PAGES[key]
    u = UI[lang]
    html = bodies[lang]
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    toc_html = "".join(f'<li><a href="#{h}">{e(re.sub(r"<[^>]+>", "", t))}</a></li>' for h, t in toc)
    body = f'''
  <div class="wrap">
    <div class="page-head">
      {crumbs(lang, [(P("home", lang), u["home"]), (None, titles[lang])])}
      <h1>{e(titles[lang])}</h1>
      <p class="sub">{e(subs[lang])}</p>
      <div class="meta"><span>{u["updated"]}: {LG.UPDATED[lang]}</span></div>
    </div>
    <div class="doc-layout">
      <div class="prose">{html}</div>
      <aside class="toc" aria-label="{u["toc"]}"><h2>{u["toc"]}</h2><ol>{toc_html}</ol></aside>
    </div>
  </div>'''
    return layout(lang, title=f"{titles[lang]} · {NAME}", desc=subs[lang], path=P(key, lang),
                  alt=P(key, "en" if lang == "tr" else "tr"), body=body)

# ---------------------------------------------------------------- site haritası
def sitemap(lang):
    L = lang == "en"; u = UI[lang]; ids = HOME_IDS[lang]; home_p = P("home", lang)
    main_links = [(home_p, u["home"])] + [
        (f"{home_p}#{ids[k]}", t) for k, t in (
            [("about", "About"), ("areas", "Areas I work in"), ("ventures", "Ventures"), ("exp", "Experience"), ("teach", "Training & publications"), ("edu", "Education & certifications"), ("contact", "Contact")]
            if L else
            [("about", "Hakkımda"), ("areas", "Çalıştığım alanlar"), ("ventures", "Girişimler"), ("exp", "Deneyim"), ("teach", "Eğitimler ve yayınlar"), ("edu", "Eğitim ve sertifikalar"), ("contact", "İletişim")])]
    post_links = [(P("posts", lang), "All articles" if L else "Tüm yazılar")] + [(f'/yazilar/{p["slug"]}/', p["title_en"] if L else p["title"]) for p in POSTS]
    legal_links = [(P(k, lang), LEGAL_PAGES[k][0][lang]) for k in ("kvkk", "cookies", "terms", "legal", "a11y")]
    def col(t, links):
        return f'<div><h2>{e(t)}</h2><ul>{"".join(f"<li><a href=\"{h}\">{e(x)}</a></li>" for h, x in links)}</ul></div>'
    title = "Sitemap" if L else "Site haritası"
    body = f'''
  <div class="wrap">
    <div class="page-head">
      {crumbs(lang, [(home_p, u["home"]), (None, title)])}
      <h1>{e(title)}</h1>
      <p class="sub">{"Every page on this site, in one place." if L else "Sitedeki tüm sayfalar, tek yerde."}</p>
    </div>
    <div class="smap">
      {col("Pages" if L else "Sayfalar", main_links)}
      {col("Writing (Turkish)" if L else "Yazılar", post_links)}
      {col("Legal" if L else "Hukuki", legal_links + [(P("home", "tr" if L else "en"), "Türkçe" if L else "English")])}
    </div>
  </div>'''
    return layout(lang, title=f"{title} · {NAME}", desc=title, path=P("sitemap", lang),
                  alt=P("sitemap", "en" if lang == "tr" else "tr"), body=body)

# ---------------------------------------------------------------- yazma
def write(path, html):
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out

if __name__ == "__main__":
    pages = []
    for lang in ("tr", "en"):
        html = home(lang).replace('<script src="/assets/js/main.js" defer></script>',
                                  '<script src="/assets/js/main.js" defer></script>\n<script src="/assets/js/showreel.js" defer></script>')
        pages.append(write(P("home", lang), html))
        pages.append(write(P("posts", lang), posts_index(lang)))
        pages.append(write(P("sitemap", lang), sitemap(lang)))
        for k in LEGAL_PAGES:
            pages.append(write(P(k, lang), legal_page(k, lang)))
    for p in POSTS:
        pages.append(write(f'/yazilar/{p["slug"]}/', post_page(p)))
    print(f"ok: {len(pages)} sayfa")
