"""Statik site üreticisi: tek içerik kaynağından iki sayfa üretir.

    python build.py   ->  index.html (TR) ve en/index.html (EN)

İçerik bu dosyadaki CONTENT sözlüğündedir. Harici bağımlılık yok.
"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://sencerzararsiz.github.io"
EMAIL = "avahmetsencerzararsiz@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/sencer-ahmet"
GITHUB = "https://github.com/sencerzararsiz"
BLOG = "https://legalitify.com/blog/"

# ---------------------------------------------------------------- ikonlar
ICON = {
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "ne": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>',
    "plus": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M6 1v10M1 6h10"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg>',
    "in": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.05c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.67 4.8 6.13V21h-4v-4.96c0-1.18-.02-2.7-1.65-2.7-1.65 0-1.9 1.29-1.9 2.62V21h-4z"/></svg>',
    "gh": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.91.83.09-.65.35-1.08.63-1.33-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.64 0 0 .84-.27 2.75 1.02a9.56 9.56 0 015 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.37.2 2.39.1 2.64.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0012 2z"/></svg>',
    "pause": '<svg class="i-pause" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true"><rect x="2.5" y="2" width="3" height="10" rx="1"/><rect x="8.5" y="2" width="3" height="10" rx="1"/></svg>',
    "play": '<svg class="i-play" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true"><path d="M3.5 2.2v9.6a.6.6 0 00.9.5l7.6-4.8a.6.6 0 000-1l-7.6-4.8a.6.6 0 00-.9.5z"/></svg>',
    # disiplin kartları
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16"/></svg>',
    "design": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 8h8M8 12h5M8 16h3"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"/></svg>',
}

# ---------------------------------------------------------------- içerik
CONTENT = {
    "tr": {
        "htmllang": "tr",
        "title": "Ahmet Sencer Zararsız · Avukat, Legal Engineer, Legal Designer",
        "desc": "Teknoloji, bilişim ve siber güvenlik hukuku avukatı. GameLaw.io Team Lead, Legalitify Legal Engineer. Hukuku, insanların gerçekten kullanabileceği ürünlere ve arayüzlere çeviriyorum.",
        "og_locale": "tr_TR",
        "skip": "İçeriğe geç",
        "nav": [("#yaklasim", "Yaklaşım"), ("#girisimler", "Girişimler"), ("#deneyim", "Deneyim"), ("#yazilar", "Yazılar"), ("#iletisim", "İletişim")],
        "status": "Şu an GameLaw.io'da Team Lead",
        "h1": ['Ahmet Sencer', 'Zararsız'],
        "lead": "Avukatım. Hukuku, insanların gerçekten <em>kullanabileceği</em> ürünlere ve arayüzlere çeviriyorum.",
        "roles": ["Teknoloji ve bilişim hukuku", "Legal Engineer", "Legal Designer", "Girişim yöneticisi", "Eğitmen"],
        "cta1": "İletişime geç",
        "cta2": "LinkedIn",
        "reel_cap": "Bu animasyonun tamamı kod. Tek bir şekil, bir uyum akışını baştan sona anlatıyor.",
        "reel_pause": "Durdur",
        "reel_play": "Oynat",
        "reel_label": "Hareketli gösterim: bir web sitesi uyum taraması, çerez tercihi, İYS onayı, sade dile çevrilen bir KVKK maddesi ve mevzuat araması.",
        "marquee": ["KVKK", "GDPR", "7545 Siber Güvenlik Kanunu", "6563 E-Ticaret", "5651 İnternet", "5809 Elektronik Haberleşme", "FSEK", "Marka", "Reklam Kurulu", "5549 MASAK", "6493 Ödeme Hizmetleri", "ISO/IEC 27001", "COSO", "SaaS sözleşmeleri", "CLM", "SHA", "Yapay zekâ yönetişimi", "Web3", "Legal Design", "LegalOps", "Oyun hukuku"],
        "marquee_hl": ["Legal Design", "ISO/IEC 27001", "Oyun hukuku"],
        "approach_k": "Yaklaşım",
        "approach_h": "Dört şapka, <em>tek masa.</em>",
        "approach_p": "Bir metni yazan avukat, onu ürüne döken mühendis, okunur kılan tasarımcı ve başkasına öğreten eğitmen çoğu zaman ayrı kişilerdir. Ben dördünü aynı masada birleştiriyorum.",
        "cards": [
            ("scale", "Hukuk", "Teknoloji, bilişim ve siber güvenlik hukuku", "KVKK/GDPR idari ve teknik uyum, 7545 sayılı Siber Güvenlik Kanunu, e-ticaret ve reklam mevzuatı, FSEK ve marka, arabuluculuk. Lisanslı MASAK Uyum Görevlisi, ISO/IEC 27001 Lead Auditor."),
            ("code", "Legal Engineering", "Hukuku ürüne çevirmek", "Legaltech/SaaS ürünlerinin hukuki altyapısı ve uyum mimarisi, sektöre göre koşullu metin şablonları, yapay zekâ yönetişimi, LegalOps ve süreç otomasyonu."),
            ("design", "Legal Design", "Okunan, anlaşılan, uygulanan metin", "Kullanıcı odaklı sözleşme mimarisi, sade dil, katmanlı aydınlatma ve uyum mimarisi. Hukuki doğruluktan ödün vermeden."),
            ("spark", "Girişim ve eğitim", "Kurmak ve öğretmek", "Legaltech girişim portföyü, yatırım süreçleri ve SHA. TÜBİTAK, Türkiye İhracatçılar Birliği ve Türkiye Fintek Topluluğu'nda eğitmenlik."),
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
        "stats": [
            ("150+", "", "müşteri ve üye iş yerine mevzuat geri bildirimi ve hukuki görüş"),
            ("13", "", "Legalitify'da yayımlanmış uyum yazısı"),
            ("147", "saat", "TÖDEB Fintek Çıraklık Programı, 9 ay"),
            ("3", "bölge", "Türkiye, Avrupa ve MENA'da şirket işlemleri"),
        ],
        "ven_k": "Girişimler ve ürünler",
        "ven_h": "Kurduğum, yönettiğim, <em>büyüttüğüm.</em>",
        "ven_p": "Hukuki altyapısını kurduğum ürünler ve içinde aktif rol aldığım girişimler.",
        "now": "Devam",
        "exp_k": "Deneyim",
        "exp_h": "Adliyeden ürün ekibine.",
        "exp_p": "Stajdan bugüne; dava dosyasından SaaS ürünlerinin uyum mimarisine. Ayrıntı için satırlara dokunun.",
        "teach_k": "Eğitmenlik ve topluluklar",
        "teach_h": "Bildiğini <em>paylaşmak.</em>",
        "teach_p": "Kurumlarda, akademilerde ve topluluklarda hukuk ve teknoloji eğitimleri.",
        "posts_k": "Yazılar",
        "posts_h": "Uyumu anlaşılır <em>yazmak.</em>",
        "posts_p": "Legalitify blogunda yazdığım yazılardan seçmeler. Her biri tek bir uyum sorusunu sade bir dille yanıtlıyor.",
        "posts_more": "Tüm yazılar",
        "read": "okuma",
        "min": "dk",
        "edu_k": "Eğitim ve sertifikalar",
        "edu_h": "Hukuk, fintek ve <em>bilişim.</em>",
        "edu_p": "Hukuk fakültesinden sonra fintek regülasyonu ve yönetim bilişim sistemleri; denetim ve uyum sertifikaları.",
        "edu_t": "Eğitim",
        "cert_t": "Sertifikalar",
        "langs": ["Türkçe · ana dil", "İngilizce · profesyonel çalışma yetkinliği"],
        "contact_h": "Bir sonraki işi <em>konuşalım.</em>",
        "contact_p": "Legaltech ürünü, uyum projesi, legal design çalışması, eğitim ya da sadece bir fikir. Yazın, dönüş yapayım.",
        "foot": "Bu sitede çerez, analitik ya da takip aracı yok; fontlar dahil her şey bu sunucudan yüklenir.",
        "foot2": "Kodla tasarlandı.",
        "other_lang": ("EN", "/en/"),
        "path": "/",
    },
    "en": {
        "htmllang": "en",
        "title": "Ahmet Sencer Zararsız · Lawyer, Legal Engineer, Legal Designer",
        "desc": "Technology, IT and cybersecurity lawyer. Team Lead at GameLaw.io, Legal Engineer at Legalitify. I turn law into products and interfaces people can actually use.",
        "og_locale": "en_US",
        "skip": "Skip to content",
        "nav": [("#approach", "Approach"), ("#ventures", "Ventures"), ("#experience", "Experience"), ("#writing", "Writing"), ("#contact", "Contact")],
        "status": "Now: Team Lead at GameLaw.io",
        "h1": ['Ahmet Sencer', 'Zararsız'],
        "lead": "I'm a lawyer. I turn law into products and interfaces people can actually <em>use</em>.",
        "roles": ["Technology & IT law", "Legal Engineer", "Legal Designer", "Startup manager", "Trainer"],
        "cta1": "Get in touch",
        "cta2": "LinkedIn",
        "reel_cap": "Every frame of this animation is code. One shape tells a whole compliance flow.",
        "reel_pause": "Pause",
        "reel_play": "Play",
        "reel_label": "Animated demo: a website compliance scan, a cookie choice, SMS consent, a KVKK clause rewritten in plain language and a statute search.",
        "marquee": ["KVKK", "GDPR", "Cybersecurity Law 7545", "E-Commerce Law 6563", "Internet Law 5651", "Electronic Communications 5809", "Copyright (FSEK)", "Trademarks", "Advertising Board", "AML · MASAK 5549", "Payment Services 6493", "ISO/IEC 27001", "COSO", "SaaS agreements", "CLM", "SHA", "AI governance", "Web3", "Legal Design", "LegalOps", "Games law"],
        "marquee_hl": ["Legal Design", "ISO/IEC 27001", "Games law"],
        "approach_k": "Approach",
        "approach_h": "Four hats, <em>one desk.</em>",
        "approach_p": "The lawyer who drafts a text, the engineer who ships it as a product, the designer who makes it readable and the trainer who teaches it are usually different people. I bring all four to the same desk.",
        "cards": [
            ("scale", "Law", "Technology, IT & cybersecurity law", "KVKK/GDPR administrative and technical compliance, Cybersecurity Law No. 7545, e-commerce and advertising regulation, copyright and trademarks, mediation. Licensed MASAK Compliance Officer, ISO/IEC 27001 Lead Auditor."),
            ("code", "Legal Engineering", "Turning law into product", "Legal infrastructure and compliance architecture for legaltech/SaaS products, sector-conditional legal text templates, AI governance, LegalOps and process automation."),
            ("design", "Legal Design", "Text that gets read and used", "User-centred contract architecture, plain language, layered privacy notices and compliance architecture, without giving up legal accuracy."),
            ("spark", "Ventures & teaching", "Building and teaching", "A legaltech startup portfolio, investment rounds and SHAs. Trainer at TÜBİTAK, the Turkish Exporters' Assembly and the Türkiye Fintech Community."),
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
        "stats": [
            ("150+", "", "clients and member merchants given regulatory feedback and legal opinions"),
            ("13", "", "compliance articles published on Legalitify"),
            ("147", "hrs", "TÖDEB Fintech Apprenticeship Programme, 9 months"),
            ("3", "regions", "corporate transactions in Türkiye, Europe and MENA"),
        ],
        "ven_k": "Ventures & products",
        "ven_h": "Built, run, <em>grown.</em>",
        "ven_p": "Products whose legal infrastructure I built and startups where I hold an active role.",
        "now": "Present",
        "exp_k": "Experience",
        "exp_h": "From courtroom to product team.",
        "exp_p": "From traineeship to today; from case files to the compliance architecture of SaaS products. Tap a row for details.",
        "teach_k": "Teaching & communities",
        "teach_h": "Sharing <em>what I know.</em>",
        "teach_p": "Law and technology training for institutions, academies and communities.",
        "posts_k": "Writing",
        "posts_h": "Writing compliance <em>clearly.</em>",
        "posts_p": "Selected pieces from the Legalitify blog, each answering one compliance question in plain language. Articles are in Turkish.",
        "posts_more": "All articles",
        "read": "read",
        "min": "min",
        "edu_k": "Education & certifications",
        "edu_h": "Law, fintech and <em>information systems.</em>",
        "edu_p": "A law degree, then fintech regulation and management information systems; audit and compliance certifications.",
        "edu_t": "Education",
        "cert_t": "Certifications",
        "langs": ["Turkish · native", "English · professional working proficiency"],
        "contact_h": "Let's talk about <em>what's next.</em>",
        "contact_p": "A legaltech product, a compliance project, a legal design piece, a training session or just an idea. Write to me and I'll get back to you.",
        "foot": "No cookies, analytics or trackers on this site; everything, fonts included, is served from this server.",
        "foot2": "Designed in code.",
        "other_lang": ("TR", "/"),
        "path": "/en/",
    },
}

# Deneyim: (tarih_tr, tarih_en, devam?, şirket, rol_tr, rol_en, yer_tr, yer_en, [madde_tr], [madde_en])
EXPERIENCE = [
    ("", "", True, "GameLaw.io", "Team Lead", "Team Lead", "", "",
     ["Oyun geliştiricileri, stüdyolar, yayıncılar, yatırımcılar ve espor ekosistemi için hukuki altyapı platformunda ekip liderliği.",
      "Platform; sözleşmeden fikrî mülkiyete, veri korumadan küresel pazara açılmaya kadar oyunun yaşam döngüsünü hukuki açıdan ele alıyor: oyun, uygulama ve web sitesi yasallık analizi, dijital due diligence, rehberler, yol haritaları ve sözleşme havuzu."],
     ["Team lead at a legal infrastructure platform for game developers, studios, publishers, investors and the esports ecosystem.",
      "The platform covers the game lifecycle from contracts and IP to data protection and global expansion: game, app and website legality analysis, digital due diligence, guides, roadmaps and a contract library."]),
    ("Ekim 2025", "Oct 2025", True, "Karataş & Partners Hukuk Bürosu", "Avukat · Teknoloji Hukuku, Uyum ve Denetim, Eğitmen", "Attorney · Technology Law, Compliance & Audit, Trainer", "İstanbul", "Istanbul",
     ["7545 sayılı Siber Güvenlik Kanunu, KVKK, GDPR, 6563, 5809 ve 5651 sayılı kanunlar kapsamında regülasyon uyumu ve uyum yol haritaları.",
      "ISO/IEC 27001 BGYS kapsamında şirket denetimleri ve belgelendirmeye hazırlık; denetim bulgularının ve risk analizlerinin raporlanması.",
      "KVKK uyum projeleri (mobil, web ve fiziksel ortam): veri envanteri, aydınlatma ve açık rıza metinleri, uyum dokümantasyonu. COSO yaklaşımıyla iç kontrol, due diligence ve risk raporlama.",
      "Yapay zekâ, Web3, fintek, e-ticaret ve SaaS ürünleri için hukuki risk analizleri; SaaS sözleşmeleri, sözleşme yönetimi (CLM) ve müzakere.",
      "Girişim hukuku ve yatırım turları (şirketleşme, SHA); Türkiye, Avrupa ve MENA'da şirket işlemleri; şirketler ve sağlık hukuku danışmanlığı.",
      "Reklam Kurulu nezdinde savunma ve uzlaşma; FSEK ve marka uyuşmazlıkları; arabuluculuk. Legal design, uyum mimarisi ve kurumsal eğitimler."],
     ["Regulatory compliance and compliance roadmaps under Cybersecurity Law No. 7545, KVKK, GDPR and Laws No. 6563, 5809 and 5651.",
      "Company audits and certification readiness under ISO/IEC 27001 ISMS; reporting of audit findings and risk analyses.",
      "KVKK compliance projects (mobile, web and physical): data inventories, privacy notices, explicit consent texts and documentation. Internal control with a COSO approach, due diligence and risk reporting.",
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
      "MASAK, TÖDEB ve TCMB yazışmaları; mevzuat takibi ve eğitim içerikleri. 150'den fazla müşteri ve üye iş yeri için mevzuat geri bildirimi ve hukuki görüş."],
     ["Compliance processes, obligation analyses and risk reporting for group companies under Laws No. 5549 (AML/MASAK), 6493 (payment services and e-money) and 6698 (KVKK).",
      "Suspicious transaction monitoring compliance; regulatory risk analyses for payment systems, e-commerce and social media processes.",
      "Personal data inventories, privacy notices, explicit consent texts, policies and procedures; contracts and website audits.",
      "Correspondence with MASAK, TÖDEB and the Central Bank; legislative monitoring and training content. Regulatory feedback and legal opinions for 150+ clients and member merchants."]),
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

# Girişimler: (ad, url, yıl_tr, yıl_en, rol_tr, rol_en, açıklama_tr, açıklama_en, öne_çıkan)
VENTURES = [
    ("GameLaw.io", "https://gamelaw.io", "Güncel", "Current", "Team Lead", "Team Lead",
     "Oyun ekosisteminin hukuki altyapısı: geliştiriciler, stüdyolar, yayıncılar, yatırımcılar ve espor için analiz araçları, rehberler ve sözleşme havuzu.",
     "Legal infrastructure for the games ecosystem: analysis tools, guides and a contract library for developers, studios, publishers, investors and esports.", True),
    ("Legalitify", "https://legalitify.com", "2025 –", "2025 –", "Legal Engineer · Startup Yöneticisi", "Legal Engineer · Startup Manager",
     "Yapay zekâyla yasal uyum: web sitesi, reklam, sözleşme ve içeriği KVKK, tüketici ve reklam mevzuatına göre tarayıp mevzuat atıflı düzeltme üreten SaaS.",
     "AI-powered legal compliance: a SaaS that scans websites, ads, contracts and content against data protection, consumer and advertising law and proposes cited fixes.", False),
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
     "Arabuluculuk, tahkim, uyum projeleri, girişim kuruluşu ve yatırım süreçleri; hukuk teknolojileri atölyeleri.",
     "Mediation, arbitration, compliance projects, startup incorporation and investment processes; legal technology workshops.", False),
]

# Eğitmenlik: (ad, yıl, rol_tr, rol_en, açıklama_tr, açıklama_en)
TEACHING = [
    ("TÜBİTAK", "", "Eğitmen ve Mentor", "Trainer & Mentor", "Fikri ve sınai haklar, şirketler hukuku ve yatırım süreçleri.", "Intellectual and industrial property, corporate law and investment processes."),
    ("Türkiye İhracatçılar Birliği", "", "Eğitmen", "Trainer", "Üye firmalara uluslararası ticaret hukuku ve regülasyon uyumu.", "International trade law and regulatory compliance for member companies."),
    ("Türkiye Fintek Topluluğu", "2025 –", "Kurucu Üye · Eğitmen", "Founding Member · Trainer", "Fintek, regtech, ödeme hizmetleri ve Web3 atölyeleri.", "Fintech, regtech, payment services and Web3 workshops."),
    ("Solana Allstars Academy Türkiye", "2025 – 2026", "Temsilci", "Representative", "Web3 ve blokzincir.", "Web3 and blockchain."),
    ("Yenilikçi Hukuk Akademisi", "2023 – 2024", "Eğitmen", "Trainer", "Hukuk ve inovasyon eğitimleri.", "Law and innovation training (Innovative Law Academy)."),
    ("Tekno Hukuk Akademisi", "2023 – 2024", "Ar-Ge Temsilcisi · Eğitmen", "R&D Representative · Trainer", "Legal design ve legaltech.", "Legal design and legaltech (Techno Law Academy)."),
]

# Yazılar: (slug, kategori_tr, kategori_en, tarih, dk, başlık_tr, başlık_en)
POSTS = [
    ("cerez-banneri-en-sik-5-hata", "KVKK", "KVKK", "2026-06-17", 5,
     "Çerez banner'ınız muhtemelen hukuka aykırı: en sık 5 hata",
     "Your cookie banner is probably non-compliant: the 5 most common mistakes"),
    ("reklamda-kanitsiz-ustunluk-iddialari", "Reklam Kurulu", "Advertising Board", "2026-07-08", 4,
     "Reklamda kanıtsız üstünlük iddiaları: \"en iyi\", \"%100\", \"mucize\" neden pahalıya patlar",
     "Unsubstantiated superiority claims in ads: why \"best\", \"100%\" and \"miracle\" cost you"),
    ("reklam-kurulu-nasil-calisir", "Reklam Kurulu", "Advertising Board", "2026-07-09", 4,
     "Kanıtınız yayından önce hazır mı? Reklam Kurulu'nda bir dosyanın yolculuğu",
     "How Türkiye's Advertising Board works: from complaint to sanction"),
    ("hukuki-web-analizi-nedir", "Uyum", "Compliance", "2026-07-10", 5,
     "Metnin sitede \"var\" olması sizi kurtarmaz: hukuki web analizi neyi tarar?",
     "Five laws, one website: what a legal scan actually checks"),
    ("grc-nedir-neden-onemli", "Uyum", "Compliance", "2026-07-10", 5,
     "Excel'leriniz GRC değil: üç harfin gerçeği ve KOBİ için beş taşlı kurulum",
     "Your spreadsheets are not GRC: a five-stone setup for SMEs"),
    ("gdpr-vs-kvkk-2026", "GDPR", "GDPR", "2026-03-25", 9,
     "GDPR vs KVKK 2026: AB pazarına satış yapan Türk şirketler için 5 kritik fark",
     "GDPR vs KVKK 2026: 5 critical differences for Turkish companies selling to the EU"),
]

# Eğitim: (okul, bölüm_tr, bölüm_en, yıl_tr, yıl_en, yer)
EDUCATION = [
    ("Atatürk Üniversitesi", "Hukuk Fakültesi, lisans", "Faculty of Law, LL.B.", "2018 – 2022", "2018 – 2022", "Erzurum"),
    ("Marmara Üniversitesi", "TÖDEB Fintek Programı: regülasyon ve uyum, siber güvenlik, finans ve teknoloji", "TÖDEB Fintech Programme: regulation & compliance, cybersecurity, finance & technology", "2024 – 2025", "2024 – 2025", "İstanbul"),
    ("Anadolu Üniversitesi", "Açıköğretim Fakültesi, Yönetim Bilişim Sistemleri lisans", "Open Education Faculty, Management Information Systems (B.Sc.)", "2024 – devam", "2024 – present", "Eskişehir"),
]

# Sertifikalar: (ad_tr, ad_en, kurum_tr, kurum_en, yıl, öne_çıkan)
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

MONTHS = {
    "tr": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
}

IDS = {
    "tr": {"approach": "yaklasim", "ld": "legal-design", "ventures": "girisimler", "exp": "deneyim", "teach": "egitmenlik", "posts": "yazilar", "edu": "egitim", "contact": "iletisim"},
    "en": {"approach": "approach", "ld": "legal-design", "ventures": "ventures", "exp": "experience", "teach": "teaching", "posts": "writing", "edu": "education", "contact": "contact"},
}


def yr(s, lang):
    """'2025 –' gibi açık uçlu aralıkları tamamlar."""
    s = s.strip()
    if s.endswith("–"):
        return s + (" present" if lang == "en" else " devam")
    return s


def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    mon = MONTHS[lang][int(m) - 1]
    return f"{int(d)} {mon} {y}" if lang == "tr" else f"{mon} {int(d)}, {y}"


def sec_head(kicker, h2, p, hid):
    return f'''
      <div class="sec-head rv">
        <div><div class="kicker">{e(kicker)}</div><h2 id="{hid}">{h2}</h2></div>
        <p>{e(p)}</p>
      </div>'''


def page(lang):
    c = CONTENT[lang]
    ids = IDS[lang]
    L = lang == "en"
    url = SITE + c["path"]
    prefix = "../" if L else ""

    nav = "".join(f'<a class="nav-link" href="{h}">{e(t)}</a>' for h, t in c["nav"])
    other_label, other_path = c["other_lang"]
    cur_label = "EN" if L else "TR"
    lang_sw = (f'<span aria-current="true">{cur_label}</span><a href="{other_path}" hreflang="{other_label.lower()}" lang="{other_label.lower()}">{other_label}</a>'
               if not L else f'<a href="{other_path}" hreflang="tr" lang="tr">TR</a><span aria-current="true">EN</span>')

    roles = "".join(f"<li>{e(r)}</li>" for r in c["roles"])

    chips = "".join(f'<li class="{"hl" if m in c["marquee_hl"] else ""}">{e(m)}</li>' for m in c["marquee"])
    marquee = f'<ul>{chips}</ul><ul aria-hidden="true">{chips}</ul>'

    cards = "".join(f'''
        <article class="card rv">
          <div class="glyph">{ICON[ic]}</div>
          <div class="tag">{e(tag)}</div>
          <h3>{e(h)}</h3>
          <p>{e(p)}</p>
        </article>''' for ic, tag, h, p in c["cards"])

    ld_rows = "".join(f"<div><dt>{e(k)}</dt><dd>{v}</dd></div>" for k, v in c["ld_rows"])
    words = len(c["ld_legal"].split())
    ld_meter = "".join(f"<span>{e(m.format(words=words))}</span>" for m in c["ld_meter"])

    stats = "".join(f'''
        <div class="stat rv"><div class="n">{e(n)}{f"<small>{e(u)}</small>" if u else ""}</div><p>{e(t)}</p></div>''' for n, u, t in c["stats"])

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
    vents = "".join(vents)

    exp = []
    for i, (dtr, den, cur, co, rtr, ren, wtr, wen, btr, ben) in enumerate(EXPERIENCE):
        d = den if L else dtr
        when = (f'{e(d)} – ' if d else "") + f'<span class="now">{e(c["now"])}</span>' if cur else e(d)
        bullets = "".join(f"<li>{e(b)}</li>" for b in (ben if L else btr))
        where = e(wen if L else wtr)
        exp.append(f'''
        <li class="rv">
          <details{" open" if i == 0 else ""}>
            <summary>
              <span class="when">{when}</span>
              <span class="what"><h3>{e(co)}</h3><span>{e(ren if L else rtr)}</span></span>
              <span class="where">{where}</span>
              <span class="plus">{ICON["plus"]}</span>
            </summary>
            <div class="body"><div></div><ul>{bullets}</ul></div>
          </details>
        </li>''')
    exp = "".join(exp)

    teach = "".join(f'''
        <li class="rv"><strong>{e(n)} <span style="font-weight:400;color:var(--muted)">· {e(re_ if L else rt)}</span></strong><span class="yr">{e(yr(y, lang))}</span><span class="d">{e(de if L else dt)}</span></li>''' for n, y, rt, re_, dt, de in TEACHING)

    posts = "".join(f'''
        <a class="post rv" href="{BLOG}{slug}" target="_blank" rel="noopener" hreflang="tr">
          <div class="meta"><span class="cat">{e(ce if L else ct)}</span><span>{fmt_date(d, lang)} · {m} {c["min"]}</span></div>
          <h3>{e(te if L else tt)}</h3>
          <span class="go">legalitify.com {ICON["arrow"]}</span>
        </a>''' for slug, ct, ce, d, m, tt, te in POSTS)

    edu = "".join(f'''
          <li><strong>{e(s)}</strong><span class="yr">{e(ye if L else yt)}</span><span class="d">{e(de if L else dt)} · {e(place)}</span></li>''' for s, dt, de, yt, ye, place in EDUCATION)
    certs = "".join(f'''
          <li class="{"key" if k else ""}"><strong>{e(ne if L else nt)}</strong><span class="yr">{e(y)}</span><span class="d">{e(oe if L else ot)}</span></li>''' for nt, ne, ot, oe, y, k in CERTS)
    langs = "".join(f"<span>{e(x)}</span>" for x in c["langs"])

    ld_b1, ld_b2 = c["ld_btn"]
    person_ld = f'''{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Ahmet Sencer Zararsız",
  "url": "{url}",
  "email": "mailto:{EMAIL}",
  "jobTitle": "{"Lawyer · Legal Engineer · Legal Designer" if L else "Avukat · Legal Engineer · Legal Designer"}",
  "worksFor": [{{"@type": "Organization", "name": "GameLaw.io", "url": "https://gamelaw.io"}}, {{"@type": "Organization", "name": "Karataş & Partners"}}, {{"@type": "Organization", "name": "Legalitify", "url": "https://legalitify.com"}}],
  "alumniOf": [{{"@type": "CollegeOrUniversity", "name": "Atatürk Üniversitesi"}}, {{"@type": "CollegeOrUniversity", "name": "Marmara Üniversitesi"}}, {{"@type": "CollegeOrUniversity", "name": "Anadolu Üniversitesi"}}],
  "knowsLanguage": ["tr", "en"],
  "sameAs": ["{LINKEDIN}", "{GITHUB}"]
}}'''

    return f'''<!doctype html>
<html lang="{c["htmllang"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["desc"])}">
<meta name="author" content="Ahmet Sencer Zararsız">
<meta name="theme-color" content="#ecebe7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121211" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="tr" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Ahmet Sencer Zararsız">
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og{"-en" if L else ""}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{c["og_locale"]}">
<meta property="profile:first_name" content="Ahmet Sencer">
<meta property="profile:last_name" content="Zararsız">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(c["title"])}">
<meta name="twitter:description" content="{e(c["desc"])}">
<meta name="twitter:image" content="{SITE}/assets/img/og{"-en" if L else ""}.png">
<link rel="preload" href="{prefix}assets/fonts/Geist-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}assets/css/style.css">
<script type="application/ld+json">
{person_ld}
</script>
</head>
<body>
<a class="skip" href="#main">{e(c["skip"])}</a>

<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{c["path"]}" aria-label="Ahmet Sencer Zararsız"><span class="brand-mark" aria-hidden="true">s</span><span>Sencer Zararsız</span></a>
    <nav class="nav" aria-label="{"Main" if L else "Ana menü"}">{nav}<span class="lang">{lang_sw}</span></nav>
  </div>
</header>

<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <a class="status" href="https://gamelaw.io" target="_blank" rel="noopener"><span class="pulse" aria-hidden="true"></span>{e(c["status"])}</a>
        <h1><span class="ln">{e(c["h1"][0])}</span><span class="ln">{e(c["h1"][1])}</span></h1>
        <p class="lead">{c["lead"]}</p>
        <ul class="roles">{roles}</ul>
        <div class="cta">
          <a class="btn btn-ink" href="#{ids["contact"]}">{e(c["cta1"])} {ICON["arrow"]}</a>
          <a class="btn btn-line" href="{LINKEDIN}" target="_blank" rel="noopener">{ICON["in"]} {e(c["cta2"])}</a>
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

  <div class="marquee" aria-label="{"Areas of practice" if L else "Uzmanlık alanları"}"><div class="marquee-track">{marquee}</div></div>

  <section class="block" id="{ids["approach"]}" aria-labelledby="h-approach">
    <div class="wrap">{sec_head(c["approach_k"], c["approach_h"], c["approach_p"], "h-approach")}
      <div class="cards">{cards}
      </div>
    </div>
  </section>

  <section class="block" id="{ids["ld"]}" aria-labelledby="h-ld">
    <div class="wrap">
      <div class="ld">
        <div class="ld-side rv">
          <div class="kicker">{e(c["ld_k"])}</div>
          <h2 id="h-ld" class="sec-title" style="font-size:clamp(34px,4.8vw,58px);line-height:1.02;letter-spacing:-.04em;font-weight:600;margin:0 0 20px">{c["ld_h"].replace("<em>", '<em class="serif-em">')}</h2>
          <p>{e(c["ld_p"])}</p>
          <div class="seg" data-ld data-mode="legal" role="group" aria-label="{"Version" if L else "Sürüm"}">
            <span class="pill" aria-hidden="true"></span>
            <button type="button" data-mode="legal" aria-pressed="true">{e(ld_b1)}</button>
            <button type="button" data-mode="plain" aria-pressed="false">{e(ld_b2)}</button>
          </div>
          <p class="note">{e(c["ld_note"])}</p>
        </div>
        <div class="ld-stage rv" aria-live="polite">
          <div class="ld-pane ld-legal">
            <p>{e(c["ld_legal"])}</p>
            <div class="meter">{ld_meter}</div>
          </div>
          <div class="ld-pane ld-plain" hidden>
            <h3>{e(c["ld_plain_h"])}</h3>
            <dl class="ld-rows">{ld_rows}</dl>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="block" aria-label="{"In numbers" if L else "Rakamlarla"}">
    <div class="wrap"><div class="stats">{stats}
    </div></div>
  </section>

  <section class="block" id="{ids["ventures"]}" aria-labelledby="h-ven">
    <div class="wrap">{sec_head(c["ven_k"], c["ven_h"], c["ven_p"], "h-ven")}
      <div class="ventures">{vents}
      </div>
    </div>
  </section>

  <section class="block" id="{ids["exp"]}" aria-labelledby="h-exp">
    <div class="wrap">{sec_head(c["exp_k"], e(c["exp_h"]), c["exp_p"], "h-exp")}
      <ol class="tl">{exp}
      </ol>
    </div>
  </section>

  <section class="block" id="{ids["teach"]}" aria-labelledby="h-teach">
    <div class="wrap">{sec_head(c["teach_k"], c["teach_h"], c["teach_p"], "h-teach")}
      <ul class="teach">{teach}
      </ul>
    </div>
  </section>

  <section class="block" id="{ids["posts"]}" aria-labelledby="h-posts">
    <div class="wrap">{sec_head(c["posts_k"], c["posts_h"], c["posts_p"], "h-posts")}
      <div class="posts">{posts}
      </div>
      <div class="more"><a class="btn btn-line" href="{BLOG.rstrip("/")}" target="_blank" rel="noopener">{e(c["posts_more"])} {ICON["arrow"]}</a></div>
    </div>
  </section>

  <section class="block" id="{ids["edu"]}" aria-labelledby="h-edu">
    <div class="wrap">{sec_head(c["edu_k"], c["edu_h"], c["edu_p"], "h-edu")}
      <div class="edu">
        <div class="rv">
          <h3>{e(c["edu_t"])}</h3>
          <ul class="list">{edu}
          </ul>
          <div class="langs">{langs}</div>
        </div>
        <div class="rv">
          <h3>{e(c["cert_t"])}</h3>
          <ul class="list">{certs}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="{ids["contact"]}" aria-labelledby="h-contact">
    <div class="wrap">
      <div class="contact rv">
        <span class="orb" aria-hidden="true"></span><span class="orb b" aria-hidden="true"></span>
        <h2 id="h-contact">{c["contact_h"]}</h2>
        <p>{e(c["contact_p"])}</p>
        <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
        <div class="links">
          <a href="{LINKEDIN}" target="_blank" rel="noopener">{ICON["in"]} LinkedIn</a>
          <a href="{GITHUB}" target="_blank" rel="noopener">{ICON["gh"]} GitHub</a>
          <a href="mailto:{EMAIL}">{ICON["mail"]} {"Email" if L else "E-posta"}</a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="wrap foot">
  <p>© 2026 Ahmet Sencer Zararsız · {e(c["foot2"])}</p>
  <p>{e(c["foot"])}</p>
</footer>

<script src="{prefix}assets/js/main.js" defer></script>
<script src="{prefix}assets/js/showreel.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page("tr"), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8")
    print("ok: index.html, en/index.html")
