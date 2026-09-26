"""Web scraping ve uyum checklist'i yazıları.
Mevzuat atıfları mevzuat.gov.tr metinlerinden 26.09.2026 tarihinde doğrulanmıştır
(6698, 5846, 6102, 5237, 6098, 6563, 5549, Aydınlatma Tebliği).
Yabancı kararlar: hiQ v. LinkedIn (9th Cir., 18.04.2022, No. 17-16783) ca9.uscourts.gov;
Ryanair v PR Aviation (C-30/14, 15.01.2015) EUR-Lex.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"

SRC_SCR = {
    "6698": ("6698 sayılı Kişisel Verilerin Korunması Kanunu", M.format(6698, 1)),
    "tebligaydin": ("Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ", "https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=24454&mevzuatTur=Teblig&mevzuatTertip=5"),
    "5846": ("5846 sayılı Fikir ve Sanat Eserleri Kanunu", M.format(5846, 1)),
    "6102": ("6102 sayılı Türk Ticaret Kanunu", M.format(6102, 1)),
    "5237": ("5237 sayılı Türk Ceza Kanunu", M.format(5237, 1)),
    "6098": ("6098 sayılı Türk Borçlar Kanunu", M.format(6098, 1)),
    "6563": ("6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun", M.format(6563, 1)),
    "5549": ("5549 sayılı Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun", M.format(5549, 1)),
    "hiq": ("hiQ Labs, Inc. v. LinkedIn Corp., No. 17-16783 (9th Cir., 18.04.2022)", "https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf"),
    "ryanair": ("ABAD, C-30/14, Ryanair Ltd v PR Aviation BV, 15.01.2015", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62014CJ0030"),
}

POSTS_SCR = [
# ---------------------------------------------------------------------------
{
"slug": "web-scraping-hukuki-cerceve",
"cat": "Teknoloji", "cat_en": "Technology", "date": "2026-09-26",
"title": "Web scraping hukuka uygun mu? Veri kazımanın hukuki çerçevesi",
"title_en": "Is web scraping lawful? The legal framework of data scraping",
"excerpt": "Kazıma tekniği kendi başına yasak değil. Risk, neyin ve nasıl çekildiğinde doğar: kişisel veri, aşılan teknik engel, kullanım koşulları ve veri tabanının esaslı kısmı ayrı ayrı incelenir.",
"cover": 22,
"src": ["6698", "tebligaydin", "5846", "6102", "6098", "5237", "hiq", "ryanair"],
"body": """
<p>Web scraping Türk hukukunda ne genel olarak serbest ne genel olarak yasaktır. Kazımayı doğrudan düzenleyen bir kanun yok. Sonuç dört soruya verilen cevaba bağlıdır: çekilen veri kişisel veri mi, bir teknik engel aşılıyor mu, sitenin kullanım koşulları neyi yasaklıyor ve veri tabanının esaslı bir kısmı alınıyor mu? Herkese açık fiyatları makul hızda okuyan bir bot ile giriş duvarını aşıp profil toplayan bir bot aynı rejimde değildir.</p>

<h2>Teknik olarak ne oluyor?</h2>
<p>Tarayıcı (crawler) bağlantıları izleyerek sayfaları keşfeder. Kazıyıcı (scraper) ise sayfanın HTML'inden belirli alanları ayıklayıp kendi veri kümesine yazar. Arama motorunun dizinlemesi ile içeriği çekip ayrı bir veri tabanında saklamak farklı işlerdir; hukuki sonuç çoğu zaman ikinci adımda doğar.</p>
<p>API ayrı bir yoldur. Site sahibi veriyi belirlediği uç noktalardan, anahtar ve kota karşılığında sunar ve kuralları API koşullarına yazar. API koşulları belirli bir kullanımı yasaklarken aynı veriyi HTML'den çekmek, sonradan "iznimiz olduğunu düşündük" savunmasını zayıflatır.</p>
<p><code>robots.txt</code> bir kanun değil, bir teamüldür. Botlara hangi yolların taranmamasının istendiğini bildiren düz bir metin dosyasıdır ve teknik olarak hiçbir isteği engellemez. Ona uymamak tek başına bir suç tipini karşılamaz. Yine de site sahibinin iradesini gösteren en somut belgedir ve kötü niyet tartışmasında karşınıza çıkar.</p>

<h2>Kişisel veri: en geniş risk hattı</h2>
<p>Ad, e-posta, kullanıcı adı, profil fotoğrafı, yorum metni. Kimliği belirli veya belirlenebilir gerçek kişiye ilişkin her bilgi kişisel veridir (6698 s. KVKK m.3/1-d). Kanun "elde edilmesi" ve "kaydedilmesi" fiillerini işleme tanımına açıkça koyar (m.3/1-e). Kazıma bu nedenle ilk istekten itibaren veri işlemedir.</p>
<p>Hukuki sebep bulmak zordur. Kazıyanla ilgili kişi arasında sözleşme yoktur, açık rıza da alınmamıştır. En sık başvurulan dayanak m.5/2-d'deki "ilgili kişinin kendisi tarafından alenileştirilmiş olması" şartıdır ve dar okunmalıdır. Bir verinin internette görünür olması, kişinin onu her amaçla kullanılmak üzere herkese açtığı anlamına gelmez. Kanun koyucu özel nitelikli veriler için bu sınırı açıkça yazmıştır: m.6/3-ç, işlemenin "alenileştirme iradesine uygun" olmasını arar. İş ilanında paylaşılan telefon numarası, bir pazarlama listesine girmek için paylaşılmış değildir.</p>
<p>Geriye çoğu durumda meşru menfaat kalır (m.5/2-f). Bu şart, ilgili kişinin temel hak ve özgürlüklerine zarar vermeme kaydına bağlıdır; yazılı bir denge değerlendirmesi olmadan savunulamaz. "Önce her şeyi çekelim, sonra bakarız" yaklaşımı da amaçla bağlantılı, sınırlı ve ölçülü olma ilkesiyle çelişir (m.4/2-ç).</p>
<p>Aydınlatma yükümlülüğü ortadan kalkmaz (m.10/1). Veri ilgili kişiden elde edilmediğinde Aydınlatma Tebliği m.6/1 bildirimi üç ana göre bağlar: elde etmeden itibaren makul süre içinde, veri iletişim için kullanılacaksa ilk iletişimde, aktarılacaksa en geç ilk aktarımda. Kazınan veri yurt dışındaki bir sunucuya gidiyorsa m.9'daki aktarım rejimi ayrıca uygulanır.</p>

<h2>Veri tabanı hakkı ve haksız rekabet</h2>
<p>Kişisel veri içermeyen kazıma da serbest değildir. 5846 s. FSEK iki ayrı koruma tanır. Seçim ve düzenlemesi özgün olan veri tabanı işlenme eser sayılır (m.6/1-11); bu koruma, içindeki verinin kendisine genişletilemez. Ek m.8 ise yaratıcılık aramaz. İçeriğin oluşturulması, doğrulanması veya sunumu için nitelik ya da nicelik bakımından esaslı yatırım yapan yapımcıya, içeriğin önemli bir kısmının veya tamamının başka bir ortama aktarılmasına izin verme ya da yasaklama hakkı tanır. Koruma aleniyet tarihinden itibaren <strong>on beş yıl</strong> sürer. Bir ilan sitesinin kayıtlarını her gece baştan sona kopyalamak bu hükmün tam ortasına düşer.</p>
<p>Rakibin verisini çekip aynı pazarda sunmak 6102 s. TTK'ya da dokunur. m.55/1-c-3, kendisinin uygun bir katkısı olmaksızın başkasına ait pazarlanmaya hazır çalışma ürünlerini teknik çoğaltma yöntemleriyle devralıp onlardan yararlanmayı haksız rekabet sayar. Fiyat karşılaştırması için birkaç alan çekmek ile rakibin kataloğunu olduğu gibi yayımlamak arasındaki fark, "uygun katkı" ölçütünde görünür.</p>

<h2>Kullanım koşulları ve ceza hukuku</h2>
<p>Sitenin kullanım koşulları bir genel işlem koşulları setidir (6098 s. TBK m.20). Karşı tarafın aleyhine olan koşulların sözleşmeye girmesi için düzenleyenin bunları açıkça bildirmesi, içeriğini öğrenme imkânı sunması ve karşı tarafın kabul etmesi gerekir; aksi hâlde yazılmamış sayılırlar (m.21). Sayfa altındaki bir bağlantı ile hesap açarken işaretlenen onay kutusu bu testte aynı sonucu vermez. Oturum açarak kazıyorsanız koşulları kabul etmişsinizdir.</p>
<p>Ceza hukukunda sınır, erişimin hukuka aykırılığıdır. 5237 s. TCK m.243/1, bir bilişim sistemine hukuka aykırı olarak giren veya orada kalmaya devam edeni cezalandırır. Herkese açık bir sayfayı okumak bu tipe girmez. Başkasının hesabıyla oturum açmak, IP engelini veya erişim kontrolünü dolanmak ise tartışmayı değiştirir. Botun yükü hedef sistemin işleyişini engelliyor ya da bozuyorsa m.244/1 gündeme gelir; öngörülen ceza bir yıldan beş yıla kadar hapistir.</p>

<h2>Yabancı hukuktan iki işaret</h2>
<p>ABD'de hiQ Labs v. LinkedIn davasında 9. Daire, 18 Nisan 2022 tarihli kararında, herkese açık profillerin kazınmasının federal bilgisayar suçları yasasındaki (CFAA) "yetkisiz erişim" kavramına girmediği yönündeki argümanı güçlü buldu. Karar ihtiyati tedbir aşamasına ilişkindir ve sözleşme ihlali iddialarını çözmez. AB Adalet Divanı ise Ryanair v PR Aviation (C-30/14, 15 Ocak 2015) kararında, ne telif hakkı ne sui generis hakla korunan bir veri tabanının sahibinin kullanımına sözleşmeyle sınır koyabileceğini kabul etti. İki kararın ortak dersi şudur: fikri mülkiyet ve ceza hukuku boşluk bıraktığında sözleşme devreye girer.</p>

<h2>Kazımadan önce altı soru</h2>
<ol>
<li><strong>Kişisel veri var mı?</strong> Varsa hukuki sebep yazılı olmalı. Alenileştirme tek başına yetmez.</li>
<li><strong>Teknik bir engel aşılıyor mu?</strong> Giriş ekranı, IP engeli, hız sınırı. Aşılıyorsa TCK m.243 riski doğar.</li>
<li><strong>Kullanım koşulları ne diyor?</strong> Hesapla giriş yapılıyorsa koşullar sözleşme olarak bağlar.</li>
<li><strong>Veri tabanının esaslı kısmı mı alınıyor?</strong> Tamamı ya da önemli kısmı düzenli aktarılıyorsa FSEK Ek m.8 devrededir.</li>
<li><strong>Sistem yükü ne?</strong> İstek hızı, eşzamanlı bağlantı sayısı ve zamanlama kayıt altında olmalı.</li>
<li><strong>Amaç ne?</strong> Fiyat izleme, akademik araştırma, rakip ürün kopyalama ve pazarlama listesi kurma aynı riskte değildir.</li>
</ol>

<div class="test"><b>Pratik test</b> Botunuz kendini site sahibine tanıtsa ve neyi, hangi hızla, ne için topladığını söylese, site sahibi buna şaşırır mıydı? Cevap evetse kullanım koşullarını ve hukuki sebep kaydınızı yeniden okuyun.</div>
"""
},
# ---------------------------------------------------------------------------
{
"slug": "uyum-checklisti-nedir",
"cat": "Uyum", "cat_en": "Compliance", "date": "2026-09-26",
"title": "Uyum checklist'i nedir, nasıl hazırlanır?",
"title_en": "What is a compliance checklist and how do you build one?",
"excerpt": "Checklist bir hatırlatma listesi değil; yükümlülüğü kontrole, kontrolü kanıta bağlayan çalışma belgesidir. İyi bir satır tek kontrol taşır, dayanağını gösterir, sorumlusu ve sıklığı bellidir.",
"cover": 23,
"src": ["6698", "6563", "5549"],
"body": """
<p>Uyum checklist'i, bir kurumun uymak zorunda olduğu yükümlülükleri tek tek kontrol satırlarına çeviren ve her satır için neyin kanıt sayılacağını söyleyen çalışma belgesidir. Üç sütunla okunur: yükümlülük, kontrol, kanıt. Biri eksikse elinizdeki belge checklist değil, bir hatırlatma listesidir.</p>

<h2>Politika, denetim raporu ve checklist</h2>
<p>Politika kurumun ne yapacağını söyler. "Kişisel veriler amaçla sınırlı işlenir" bir politika cümlesidir. Checklist bunun yapılıp yapılmadığını sorar: web formundaki her alan, veri envanterinde bir işleme amacına bağlanmış mı? Denetim raporu ise geriye bakar; checklist'i uygular, bulguyu, delili ve etkiyi yazar.</p>
<p>Sıra kısaca şöyle: politika hedefi koyar, checklist ölçer, rapor sonucu kaydeder. Bu roller karıştığında iki hata tekrar eder. Politika cümleleri checklist'e kopyalanır ve hiçbir satır ölçülemez hâle gelir. Ya da checklist'in içine bulgu ve tavsiye yazılır, belge bir sonraki dönemde yeniden kullanılamaz.</p>

<h2>İyi bir kontrol satırının anatomisi</h2>
<p>Her satır tek bir kontrol taşır. "Aydınlatma metni güncel ve erişilebilir mi?" iki sorudur; biri evet, diğeri hayır çıktığında satır işaretlenemez. Bölün.</p>
<p>Satırın taşıması gereken alanlar:</p>
<ul>
<li><strong>Hukuki dayanak:</strong> kanun, madde, fıkra, bent. "İlgili mevzuat" dayanak değildir.</li>
<li><strong>Ölçülebilir soru:</strong> evet/hayır ya da bir sayı ile cevaplanabilmeli.</li>
<li><strong>Sorumlu:</strong> bir kişi veya rol. "Şirket" sorumlu sayılmaz.</li>
<li><strong>Sıklık:</strong> sürekli, aylık, yıllık ya da olay anında.</li>
<li><strong>Kanıt:</strong> ekran görüntüsü, sistem logu, imzalı form, rapor çıktısı ve bunun nerede saklandığı.</li>
</ul>
<p>Cevap seçenekleri de baştan tanımlanır: evet, hayır, kısmen, uygulanmaz. "Uygulanmaz" işaretlenen her satır bir gerekçe ister. Gerekçesiz bırakıldığında, zor bir kontrolden kaçmanın en kolay yoluna dönüşür.</p>
<p>Dört örnek satır:</p>
<ol>
<li>Kişisel verinin toplandığı her kanalda (web formu, mobil uygulama, çağrı merkezi) veri elde edilirken aydınlatma yapılıyor mu? Dayanak: 6698 s. KVKK m.10/1. Sorumlu: veri koruma birimi. Sıklık: her yeni kanal açılışında ve yılda bir. Kanıt: kanal bazında tarihli ekran görüntüsü.</li>
<li>Ticari elektronik ileti ret talebi ulaştıktan sonra gönderim en geç <strong>üç iş günü</strong> içinde duruyor mu? Dayanak: 6563 s. Kanun m.8/3. Sorumlu: CRM yöneticisi. Sıklık: aylık örneklem. Kanıt: ret tarihi ile son gönderim tarihini yan yana gösteren sistem kaydı.</li>
<li>İlgili kişi başvuruları en geç <strong>otuz gün</strong> içinde sonuçlanıyor mu? Dayanak: KVKK m.13/2. Sorumlu: başvuru birimi. Sıklık: üç ayda bir. Kanıt: geliş ve cevap tarihlerini içeren başvuru kayıt defteri.</li>
<li>Şüpheli işlem bildirimi yapıldığı bilgisinin işlemin taraflarına açıklanmaması konusunda ön büro çalışanları eğitim almış mı? Dayanak: 5549 s. Kanun m.4/2. Sorumlu: uyum görevlisi. Sıklık: yıllık ve işe girişte. Kanıt: imzalı eğitim katılım listesi.</li>
</ol>
<p>Dördüncü satır bilerek dar tutuldu. Bildirimin kendisinin yapılıp yapılmadığı (m.4/1) ayrı bir satırdır; ikisini birleştirmek, birini sağlayıp diğerini atlayan kurumu "uygun" gösterir.</p>

<h2>Sık kullanılan checklist aileleri</h2>
<p>Konu değiştikçe dayanak da kanıt türü de değişir.</p>
<ul>
<li><strong>KVKK ve e-ticaret:</strong> aydınlatma, açık rıza, <a href="/yazilar/verbis-kayit-yukumlulugu/">VERBİS kaydı</a>, çerezler, mesafeli satış bilgilendirmesi.</li>
<li><strong>Reklam ve pazarlama:</strong> ticari elektronik ileti onayı ve <a href="/yazilar/iys-kanal-bazli-onay-ve-ret/">İYS üzerinden kanal bazlı ret</a>, reklam içeriği, örtülü reklam.</li>
<li><strong>Rekabet:</strong> rakiplerle bilgi değişimi, bayi sözleşmelerindeki kısıtlar, sektör toplantıları. Kanıt çoğunlukla yazışma ve toplantı tutanağıdır.</li>
<li><strong>Yapay zekâ yönetişimi:</strong> kullanılan modellerin envanteri, eğitim verisinin kaynağı, insan gözetimi, çıktı kayıtları.</li>
<li><strong>ISO/IEC 27001 bilgi güvenliği yönetim sistemi ve iç denetim:</strong> satırlar standardın gereklerinden türetilir; varlık envanteri, erişim yetkisi gözden geçirmesi, olay kaydı. Kanıt burada neredeyse her zaman sistem çıktısıdır.</li>
<li><strong>MASAK:</strong> müşterinin tanınması (5549 m.3/1), şüpheli işlem bildirimi (m.4), eğitim, iç denetim ve kontrol sistemleri (m.5).</li>
</ul>

<h2>Checklist'i bozan üç alışkanlık</h2>
<p>İlki hazır şablon kopyalamaktır. Başka bir kurumun checklist'i onun iş modeline göre yazılmıştır. Çağrı merkezi olmayan bir şirkette "çağrı merkezi aydınlatması" satırı "uygulanmaz" diye geçilir; asıl eksik olan WhatsApp hattı ise listede hiç yer almaz.</p>
<p>Mevzuat değişince güncellememek ikinci hatadır. KVKK m.9, 2/3/2024 tarihli 7499 s. Kanun m.34 ile baştan yazıldı. Yeni metin yeterlilik kararı ve uygun güvenceler üzerine kademeli bir yapı kurar; standart sözleşmenin imzadan itibaren <strong>beş iş günü</strong> içinde Kuruma bildirilmesini de şart koşar (m.9/5). Bu satır eski checklist'lerde yoktur. Her satırın yanında bir "son doğrulama tarihi" sütunu bulunmalıdır.</p>
<p>Üçüncüsü kutucuk işaretlemektir. Kanıt eklenmeden "evet" yazılan satır, denetimde "hayır" muamelesi görür. Kanıt sütunu boş bir checklist, kurumun kendine verdiği bir beyandan ibarettir.</p>

<div class="test"><b>Pratik test</b> Checklist'inizden rastgele bir satır seçin. O satırı hiç görmemiş bir çalışma arkadaşınız, yalnızca satıra bakarak kimin, ne zaman, neyi kontrol edeceğini ve kanıtı nerede bulacağını söyleyebiliyor mu? Söyleyemiyorsa satır yeniden yazılmalıdır.</div>
"""
},
]
