"""Uyum yazıları: MASAK uyumu, web sitesi uyumu, mobil uygulama uyumu.
Mevzuat atıfları mevzuat.gov.tr / kvkk.gov.tr metinlerinden 26.09.2026 tarihinde doğrulanmıştır.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"
REHBER = "https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/fb193dbb-b159-4221-8a7b-3addc083d33f.pdf"

SRC_UYUM = {
    "5549": ("5549 sayılı Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun",
             "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf"),
    "tedbiryon": ("Suç Gelirlerinin Aklanmasının ve Terörün Finansmanının Önlenmesine Dair Tedbirler Hakkında Yönetmelik",
                  M.format(200713012, 21)),
    "uyumyon": ("Suç Gelirlerinin Aklanmasının ve Terörün Finansmanının Önlenmesine İlişkin Yükümlülüklere Uyum Programı Hakkında Yönetmelik",
                M.format(12426, 7)),
    "6698": ("6698 sayılı Kişisel Verilerin Korunması Kanunu", M.format(6698, 1)),
    "6502": ("6502 sayılı Tüketicinin Korunması Hakkında Kanun", M.format(6502, 1)),
    "6563": ("6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun", M.format(6563, 1)),
    "5651": ("5651 sayılı İnternet Ortamında Yapılan Yayınların Düzenlenmesi Kanunu", M.format(5651, 1)),
    "5651yon": ("İnternet Ortamında Yapılan Yayınların Düzenlenmesine Dair Usul ve Esaslar Hakkında Yönetmelik",
                "https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=11746&mevzuatTur=KurumVeKurulusYonetmeligi&mevzuatTertip=5"),
    "5378": ("5378 sayılı Engelliler Hakkında Kanun", "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5378.pdf"),
    "rehber": ("KVKK, Çerez Uygulamaları Hakkında Rehber, Temmuz 2025", REHBER),
    "tebligaydin": ("Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ",
                    "https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=24454&mevzuatTur=Teblig&mevzuatTertip=5"),
    "msy": ("Mesafeli Sözleşmeler Yönetmeliği", M.format(20237, 7)),
    "iysyon": ("Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik", M.format(20914, 7)),
    "wcag22": ("W3C, Web Content Accessibility Guidelines (WCAG) 2.2", "https://www.w3.org/TR/WCAG22/"),
}

POSTS_UYUM = [
# ---------------------------------------------------------------------------
{
"slug": "masak-uyumu-nedir",
"cat": "Uyum", "cat_en": "Compliance", "date": "2026-09-26",
"title": "MASAK uyumu nedir?",
"title_en": "What is AML compliance under MASAK rules?",
"excerpt": "Her yükümlü müşterisini tanımak, şüpheli işlemi on iş günü içinde bildirmek ve kayıtları sekiz yıl saklamak zorunda. Uyum programı ve uyum görevlisi ise yalnızca yönetmelikte sayılan yükümlüler için zorunlu.",
"cover": 12,
"src": ["5549", "tedbiryon", "uyumyon"],
"body": """
<p>MASAK uyumu, 5549 sayılı Kanun'un yükümlü saydığı bir işletmenin üç işi yaptığını gösterebilmesidir: müşterisini işlemden önce tanımak, şüpheli işlemi bildirmek ve bu işlerin kaydını sekiz yıl saklamak. Uyum programı ve uyum görevlisi bu üç işin üstüne kurulan ikinci bir katmandır. Her yükümlüye aynı ölçüde uygulanmaz. Uygulamada sık gördüğüm hata, bu iki katmanı birbirine karıştırmak.</p>
<p>MASAK, Mali Suçları Araştırma Kurulu Başkanlığıdır (5549 s. Kanun m.2/1-c). Yükümlülüklerin ayrıntısı iki yönetmelikte: Tedbirler Yönetmeliği ve Uyum Programı Yönetmeliği.</p>

<h2>Kim yükümlü?</h2>
<p>Kanun yükümlüyü geniş tanımlar. Bankacılık, sigortacılık, sermaye piyasaları ve diğer finansal hizmetlerin yanında döviz, taşınmaz, değerli taş ve maden, mücevher, nakil vasıtası ve sanat eseri ticareti yapanlar, noterler ve spor kulüpleri de sayılır (5549 s. Kanun m.2/1-d). Liste Tedbirler Yönetmeliği m.4/1'de ayrıntılanır. Örnek olarak:</p>
<ul>
<li>ödeme kuruluşları ile elektronik para kuruluşları (m.4/1-e),</li>
<li>kıymetli maden, taş veya mücevher alım satımı yapanlar ile bu işlemlere aracılık edenler (m.4/1-k),</li>
<li>kripto varlık hizmet sağlayıcılar (m.4/1-ü),</li>
<li>orta, büyük veya çok büyük ölçekli elektronik ticaret aracı hizmet sağlayıcılar (m.4/1-y).</li>
</ul>
<p>Yükümlülük bir sektör etiketi değil, faaliyete bağlı bir statüdür. Yönetmelik, faaliyetin mağazada mı internette mi yürütüldüğüne göre bir ayrım yapmaz.</p>

<h2>Müşteriyi tanımak: işlemden önce</h2>
<p>Kimlik tespiti, iş ilişkisi kurulmadan veya işlem yapılmadan önce tamamlanır (5549 s. Kanun m.3/1; Tedbirler Yönetmeliği m.5/2). Tespitin zorunlu olduğu hâller Tedbirler Yönetmeliği m.5/1'de sayılır:</p>
<ul>
<li>sürekli iş ilişkisi kurulurken, tutara bakılmaksızın;</li>
<li>tek işlem ya da birbiriyle bağlantılı işlemlerin toplamı 185.000 TL veya üzerindeyse (kripto varlık hizmet sağlayıcılar için 15.000 TL);</li>
<li>elektronik transferlerde toplam 15.000 TL veya üzerindeyse;</li>
<li>şüpheli işlem bildirimini gerektiren durumlarda ve eldeki kimlik bilgilerinin doğruluğundan şüphe edildiğinde, yine tutara bakılmaksızın.</li>
</ul>
<p>Tespit, işlemin gerçek faydalanıcısını ortaya çıkarmak için gereken tedbirleri de kapsar (m.5/1). Yüksek riskli durumlarda fon kaynağının sorulması veya iş ilişkisinin üst düzey onaya bağlanması gibi sıkılaştırılmış tedbirler devreye girer (m.26/A).</p>

<div class="test"><b>Pratik test</b>Aynı müşterinin, tek tek eşiğin altında kalan ama toplamı 185.000 TL'yi aşan işlemlerini sisteminiz birleştirip gösterebiliyor mu? Gösteremiyorsa bağlantılı işlem kuralı sizde yalnızca kâğıt üzerindedir.</div>

<h2>Şüpheli işlem bildirimi: on iş günü</h2>
<p>Bildirim için kanıt gerekmez. Bir bilgi, şüphe ya da şüpheyi gerektiren bir husus yeterlidir (5549 s. Kanun m.4/1). Bildirim tutar gözetilmeksizin yapılır (Tedbirler Yönetmeliği m.27/2) ve şüphenin oluştuğu tarihten itibaren <strong>en geç on iş günü</strong> içinde MASAK'a ulaşmalıdır (m.28/2). Süre işlem tarihinden değil, şüphenin oluştuğu tarihten başlar. Şüphenin hangi gün oluştuğunu gösteren bir iç kayıt bu yüzden gerekir.</p>
<p>Bildirim yapıldığı, işleme taraf olanlar dahil kimseye açıklanamaz (5549 s. Kanun m.4/2; Tedbirler Yönetmeliği m.29/1). Müşteriye "sizi bildirdik" demek de bir ihlaldir. Bildirim yükümlülüğünü yerine getirenler ise hukuki ve cezai bakımdan sorumlu tutulamaz (Tedbirler Yönetmeliği m.29/4).</p>

<h2>Uyum programı: herkes için değil</h2>
<p>Uyum Programı Yönetmeliği m.4/1, program kurmak zorunda olanları tek tek sayar. Bankalar, sermaye piyasası aracı kurumları, sigorta ve emeklilik şirketleri, kıymetli madenler aracı kuruluşları, elektronik para kuruluşları, ödeme kuruluşları (bazı dar hizmet türleri hariç) ve kripto varlık hizmet sağlayıcılar bu listededir. Program altı unsurdan oluşur: kurum politikası ve prosedürleri, risk yönetimi, izleme ve kontrol, uyum görevlisi ve uyum birimi, eğitim, iç denetim (m.5/1). Tedbirler en az iki yılda bir gözden geçirilir (m.5/4).</p>
<p>Kapsamdaki yükümlü için takvim şöyle işler:</p>
<ul>
<li>Uyum görevlisi faaliyet izninden sonra 30 gün içinde atanır ve satış-pazarlama görevi üstlenemez (m.16/1-2).</li>
<li>Eğitim yıllık program dahilinde yürütülür (m.22/2); sonuçlar takip eden yılın Mart ayı sonuna kadar MASAK'a bildirilir (m.24).</li>
<li>İç denetim, programın yeterliliğini yılda bir ve risk temelli inceler (m.26/2); istatistikleri de Mart sonuna kadar bildirilir (m.28).</li>
<li>İzleme ve kontrol, en az yüksek riskli müşterileri, riskli ülkelerle yapılan işlemleri ve yüz yüze olmayan işlemleri kapsar (m.15/3).</li>
</ul>
<p>Kıymetli maden alım satımı yapan bir kuyumcu Tedbirler Yönetmeliği'ne göre yükümlüdür. Uyum programı kurmakla yükümlü olanları sayan Uyum Programı Yönetmeliği m.4/1 ise onu saymaz; uyum görevlisi atayacakları sayan aynı Yönetmeliğin m.29/1'i de. Bu serbestlik anlamına gelmez. Kimlik tespiti, bildirim ve saklama aynen işler; bildirimi tüzel kişide kanuni temsilci veya onun yetkilendirdiği kişi yapar (Tedbirler Yönetmeliği m.27/2).</p>

<h2>Sekiz yıl saklama</h2>
<p>Belgeler düzenleme tarihinden, defter ve kayıtlar son kayıt tarihinden, kimlik tespitine ilişkin belgeler son işlem tarihinden itibaren <strong>sekiz yıl</strong> saklanır ve istendiğinde ibraz edilir (5549 s. Kanun m.8/1). Hesaplarda kimlik belgeleri için süre hesabın kapandığı gün başlar. Uyum görevlisinin bildirimde bulunmama kararlarının yazılı gerekçeleri de saklanacak kayıtlardandır (Tedbirler Yönetmeliği m.46).</p>
<p>Bu son hüküm çoğu zaman gözden kaçıyor. Bildirmeme kararı da bir karardır ve gerekçesi yazılı olmalıdır. Kimlik dosyası, izleme alarmı ve bildirim kararı aynı müşteriyi aynı tarihlerle anlatmıyorsa denetimde savunulacak bir kayıt yoktur.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "web-sitesi-uyumu-nedir",
"cat": "Uyum", "cat_en": "Compliance", "date": "2026-09-26",
"title": "Web sitesi uyumu nedir?",
"title_en": "What does website compliance mean in Turkey?",
"excerpt": "Web sitesi uyumu tek bir KVKK metni değil. Kim olduğunuzu, hangi veriyi işlediğinizi, ne sattığınızı ve kime ileti gönderdiğinizi ayrı kanunlar soruyor.",
"cover": 13,
"src": ["5651", "5651yon", "6563", "6698", "tebligaydin", "rehber", "6502", "msy", "iysyon", "5378", "wcag22"],
"body": """
<p>Web sitesi uyumu, bir sitenin ziyaretçiye karşı taşıdığı bilgi verme borçlarının toplamıdır. Tek bir "KVKK metni" ile kapanmaz. Sitenin kime ait olduğu, veri işleyip işlemediği, satış yapıp yapmadığı ve ileti gönderip göndermediği dört ayrı sorudur. Her birinin cevabı başka bir düzenlemededir.</p>

<h2>Önce kim olduğunuzu söyleyin</h2>
<p>İçerik, yer ve erişim sağlayıcıları tanıtıcı bilgilerini kendi internet ortamlarında güncel olarak bulundurmak zorundadır (5651 s. Kanun m.3/1). Ticari veya ekonomik amaçlı bir site için Usul ve Esaslar Yönetmeliği m.5/1 bu bilgileri sayar. Bilgiler ana sayfadan doğrudan ulaşılabilir biçimde ve "iletişim" başlığı altında durmalıdır:</p>
<ul>
<li>gerçek kişide ad-soyad; tüzel kişide unvan ve sorumlu kişiler, vergi kimlik numarası veya ticaret sicil numarası,</li>
<li>yerleşim yeri ya da merkez adresi,</li>
<li>e-posta ve telefon,</li>
<li>faaliyet izne veya denetime tabiyse yetkili denetim mercii.</li>
</ul>
<p>Sık atlanan bir satır daha var. Ticari içerik sağlayıcı, sitesini barındıran yer sağlayıcının tanıtıcı bilgilerini de ana sayfasında bulundurmalıdır (m.5/2).</p>
<p>Sitede sözleşme kuruluyorsa 6563 sayılı Kanun m.3/1 devreye girer. Sözleşmeden önce tanıtıcı bilgiler, sözleşmenin kurulması için izlenecek teknik adımlar, sözleşme metninin saklanıp saklanmayacağı, veri girişi hatalarını düzeltme araçları ve gizlilik kuralları sunulur. Alıcı sözleşme hükümlerini saklayabilmelidir (m.3/4).</p>

<h2>Veri: aydınlatma girişte, rıza ayrı</h2>
<p>Kişisel veri elde edilirken veri sorumlusu kimliğini, işleme amacını, aktarım yapılan alıcıları ve amacını, toplama yöntemi ile hukuki sebebi ve ilgili kişinin haklarını bildirir (6698 s. KVKK m.10/1). Açık rızaya dayanan işlemelerde aydınlatma ile rıza ayrı ayrı alınır (Aydınlatma Tebliği m.5/1-f). Genel ve muğlak amaç ifadeleri kullanılmaz (m.5/1-g).</p>
<p>KVKK'nın Çerez Rehberi, çerezle veri işlemeye site ziyaretiyle başlanıyorsa aydınlatmanın siteye giriş aşamasında yapılması gerektiğini söyler. Çerezin adı, amacı, süresi ve birinci ya da üçüncü taraf olup olmadığının metinde yer almasını da tavsiye eder (s.36). Yurt dışındaki şirketlerin çerezleri veri aktarıyorsa bu aktarım m.9'a uygun olmalıdır (s.34-35). Banner tarafındaki hatalar için <a href="/yazilar/cerez-banneri-en-sik-5-hata/">çerez banner'larında en sık beş hata</a> yazısına bakılabilir. Kayıt yükümlülüğü ayrı bir sorudur: <a href="/yazilar/verbis-kayit-yukumlulugu/">VERBİS yazısı</a>.</p>

<h2>Satış yapıyorsanız: ödeme düğmesinden hemen önce</h2>
<p>Tüketici, mesafeli sözleşmeyi kabul etmeden önce bilgilendirilir ve ispat yükü satıcıdadır (6502 s. Kanun m.48/2). İçerik Mesafeli Sözleşmeler Yönetmeliği m.5/1'de: satıcının unvanı ve MERSİS ya da vergi kimlik numarası, vergiler dahil toplam fiyat, cayma hakkının şartları, cayma hakkı yoksa bunun bilgisi, tüketici hakem heyeti ve arabulucu yolu. Bilgilendirme en az on iki punto ile yapılır (m.6/1). İnternet satışında temel nitelikler, toplam fiyat ve cayma bilgisi, ödeme yükümlülüğünden hemen önce ayrıca bir bütün olarak gösterilir (m.6/2-a).</p>
<p>Eksiklerin bedeli somuttur. Ek masraf bildirilmemişse tüketici onu ödemez (m.5/3). Cayma hakkı konusunda gerektiği gibi bilgilendirilmeyen tüketici 14 günlük süreyle bağlı değildir; süre, cayma süresinin bittiği tarihten bir yıl sonra sona erer (6502 s. Kanun m.48/4). İade tarafı için: <a href="/yazilar/iade-magaza-kredisi-dayatilamaz/">iadede mağaza kredisi dayatılamaz</a>.</p>

<div class="test"><b>Pratik test</b>Sepetten ödeme ekranına kadar gidin ve düğmeye basmadan durun. Ürünün temel nitelikleri, vergiler dahil toplam tutar ve cayma hakkı bilgisi o ekranda birlikte görünüyor mu? Birini görmek için başka bir sayfaya gitmeniz gerekiyorsa m.6/2-a karşılanmamıştır.</div>

<h2>İleti gönderiyorsanız: İYS</h2>
<p>Ticari elektronik ileti önceden onay alınmadan gönderilemez (6563 s. Kanun m.6/1). Gönderici İYS'ye kaydolur ve İYS'de onayı bulunmayan alıcıya ileti gidemez (Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik m.5/2-3). Kanal bazlı ayrıntı için: <a href="/yazilar/iys-kanal-bazli-onay-ve-ret/">İYS'de kanal bazlı onay ve ret</a>.</p>

<h2>Erişilebilirlik</h2>
<p>5378 sayılı Engelliler Hakkında Kanun m.7, bilgi ve iletişim teknolojisinin engelliler için erişilebilir olmasının sağlanacağını söyler. Bu yazı için incelediğim metinlerde özel bir şirketin sitesine belirli bir teknik seviye dayatan ve yaptırım bağlayan bir hüküm bulamadım. Bu yüzden W3C'nin WCAG 2.2 yönergelerini yasal zorunluluk olarak değil, iyi uygulama olarak ele alıyorum. Klavyeyle gezilemeyen bir çerez paneli ise yalnızca erişilebilirlik sorunu değildir; kullanıcı reddetme seçeneğine hiç ulaşamıyorsa rızanın özgür iradeyle verildiği de tartışmalı hâle gelir (6698 s. KVKK m.3/1-a).</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "mobil-uygulama-uyumu-nedir",
"cat": "Uyum", "cat_en": "Compliance", "date": "2026-09-26",
"title": "Mobil uygulama uyumu nedir?",
"title_en": "What does mobile app compliance involve in Turkey?",
"excerpt": "Uygulamada veriyi çoğu zaman sizin kodunuz değil, gömdüğünüz SDK'lar toplar. İşletim sistemi izni açık rıza değildir; abonelik ve uygulama içi satın almada cayma istisnası ancak önceden söylenirse işe yarar.",
"cover": 14,
"src": ["6698", "tebligaydin", "rehber", "6563", "msy", "6502", "iysyon"],
"body": """
<p>Mobil uygulamada uyumun ağırlık merkezi siteden farklıdır. Veriyi toplayan çoğu zaman sizin kodunuz değil, uygulamaya gömdüğünüz üçüncü taraf SDK'lardır. Hukuk ise değişmez: 6698 sayılı Kanun siteye ne uyguluyorsa uygulamaya da onu uygular. Uygulamayı ayrıca düşünmeyi gerektiren dört konu var: izin ekranları, yurt dışına aktarım, uygulama içi satın alma ve bildirimler.</p>

<h2>İşletim sistemi izni açık rıza değildir</h2>
<p>Kamera, konum ya da rehbere erişim için çıkan pencere teknik bir izindir. Açık rıza ise belirli bir konuya ilişkin, bilgilendirmeye dayanan ve özgür iradeyle açıklanan rızadır (6698 s. KVKK m.3/1-a). İzin penceresinin kısa metni m.10'daki aydınlatma unsurlarını taşımaz. Kullanıcıya veri sorumlusunun kim olduğunu, verinin hangi hukuki sebeple ve kime aktarılacağını söylemez.</p>
<p>Ters yöndeki hata da yaygın. Her izin için açık rıza istenmez. Teslimat uygulamasının adres için konuma erişmesi sözleşmenin ifasına dayanabilir (m.5/2-c). Aynı konumun reklam hedeflemesinde kullanılması ise başka bir amaçtır ve başka bir dayanak ister. Açık rızaya dayanılan her yerde aydınlatma ve rıza ayrı adımlarla alınır (Aydınlatma Tebliği m.5/1-f).</p>
<p>İstenen izin amaçla sınırlı olmalıdır. Veri işleme, amaçla bağlantılı, sınırlı ve ölçülü olmak zorundadır (m.4/2-ç). El feneri uygulamasının rehbere ihtiyacı yoktur.</p>

<h2>SDK'lar ve yurt dışına aktarım</h2>
<p>Analitik, hata raporlama ve reklam SDK'ları veriyi çoğunlukla yurt dışındaki sunuculara gönderir. Bu bir yurt dışına aktarımdır ve 2024 değişikliğinden sonraki m.9'a tabidir. Önce yeterlilik kararına bakılır (m.9/1). Karar yoksa standart sözleşme gibi uygun güvencelerden biri gerekir (m.9/4); standart sözleşme imzadan itibaren <strong>beş iş günü</strong> içinde Kuruma bildirilir (m.9/5). Açık rıza ancak arızi aktarımlarda bir dayanaktır (m.9/6-a). Her açılışta çalışan bir analitik SDK'nın aktarımına arızi demek zordur.</p>
<p>KVKK'nın Çerez Rehberi kapsamını masaüstü ve mobil web siteleri ile web uygulamaları olarak tanımlar (s.9). Rehber, yurt dışındaki şirketler aracılığıyla yapılan aktarımların m.9'a uygun olması gerektiğini de hatırlatır (s.34-35). Yerel uygulamalara gömülen SDK'lar için Kurulun ayrı bir rehberini tespit edemedim. Dayanak doğrudan Kanun'dur.</p>

<div class="test"><b>Pratik test</b>Uygulamayı temiz bir cihaza kurun, ilk ekranda hiçbir yere dokunmadan trafiği bir proxy ile izleyin. Yurt dışındaki bir analitik veya reklam sunucusuna istek gidiyorsa, o aktarımın m.9'daki dayanağını yazılı olarak gösterebilmelisiniz.</div>

<h2>Abonelik ve uygulama içi satın alma</h2>
<p>6563 sayılı Kanun'a göre mobil uygulama da bir elektronik ticaret ortamıdır (m.2/1-ğ). Sözleşme öncesi bilgi verme yükümlülüğü uygulamada da geçerlidir (m.3/1).</p>
<p>Tüketicinin 14 günlük cayma hakkı vardır; hizmet sözleşmelerinde süre sözleşmenin kurulduğu gün başlar (Mesafeli Sözleşmeler Yönetmeliği m.9/1-2). Dijital ürünlerde iki istisna öne çıkar: elektronik ortamda anında ifa edilen hizmetler veya anında teslim edilen gayrimaddi mallar (m.15/1-ğ) ve cayma süresi dolmadan tüketicinin onayıyla ifasına başlanan hizmetler (m.15/1-h).</p>
<p>İstisna kendiliğinden işlemez. Cayma hakkının kullanılamadığını ya da hangi koşullarda kaybedildiğini ön bilgilendirmede söylemek zorunludur (m.5/1-h). İnternet yoluyla kurulan sözleşmede bu bilgi ödemeden hemen önce ayrıca gösterilir (m.6/2-a). Aboneliklerde toplam fiyat her faturalama dönemi için tüm masrafları içerecek şekilde verilir (m.5/4). Deneme süresi bitince ücretli pakete geçen bir akışta bu satır, ödeme ekranında görünmelidir.</p>
<p>Uygulama mağazalarının kuralları kanun değil, sözleşmedir. Uygulamanın yayında kalması onlara bağlıdır ama mağaza kurallarına uymak Türk hukukundaki yükümlülükleri karşılamaz.</p>

<h2>Çocuklar</h2>
<p>6698 sayılı Kanun çocuklar için ayrı bir rıza yaşı öngörmez. Çerez Rehberi ise çocuklara hitap eden ürünlerde aydınlatmanın çocuğun algı düzeyine uygun, gerekirse görsellerle desteklenmiş sade bir dille yapılmasını ister (s.37). Oyun ve eğitim uygulamalarında aydınlatma metni yalnızca ebeveyn için yazılmışsa bu beklenti karşılanmaz.</p>

<h2>Push bildirimleri</h2>
<p>Kanun'daki ticari elektronik ileti tanımı telefon, e-posta ve kısa mesajı sayar ve "gibi vasıtalar" ifadesiyle biter (6563 s. Kanun m.2/1-c). Push bildirimi açıkça sayılmaz. İYS ise e-posta ve telefon numarası gibi elektronik iletişim adresleri üzerine kuruludur (Yönetmelik m.4/1-d). Lafız kesin bir cevap vermediği için ben kampanya içerikli push bildirimini onaya bağlı bir ileti gibi tasarlamayı tercih ediyorum: ayrı bir açma düğmesi ve uygulama içinden tek adımda kapatma. SMS ve e-posta tarafındaki kurallar için: <a href="/yazilar/iys-kanal-bazli-onay-ve-ret/">İYS'de kanal bazlı onay ve ret</a>.</p>
""",
},
]
