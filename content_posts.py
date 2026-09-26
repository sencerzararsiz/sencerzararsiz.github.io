"""Yazılar. Her yazıdaki mevzuat atfı mevzuat.gov.tr / kvkk.gov.tr üzerinden 26.09.2026 tarihinde
doğrulanmıştır. Yazılar ilk olarak Legalitify blogunda yayımlanmış, burada gözden geçirilip
güncellenmiştir.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"
REHBER = "https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/fb193dbb-b159-4221-8a7b-3addc083d33f.pdf"
ACCESS = "26.09.2026"

SRC = {
    "6698": ("6698 sayılı Kişisel Verilerin Korunması Kanunu", M.format(6698, 1)),
    "6502": ("6502 sayılı Tüketicinin Korunması Hakkında Kanun", M.format(6502, 1)),
    "6563": ("6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun", M.format(6563, 1)),
    "5651": ("5651 sayılı İnternet Ortamında Yapılan Yayınların Düzenlenmesi Kanunu", M.format(5651, 1)),
    "rehber": ("KVKK, Çerez Uygulamaları Hakkında Rehber, Temmuz 2025", REHBER),
    "reklamyon": ("Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği", M.format(20435, 7)),
    "rkyon": ("Reklam Kurulu Yönetmeliği", M.format(19832, 7)),
    "kozmetik": ("Kozmetik Ürünler Yönetmeliği", M.format(40405, 7)),
    "iysyon": ("Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik", M.format(20914, 7)),
    "msy": ("Mesafeli Sözleşmeler Yönetmeliği", M.format(20237, 7)),
    "verbisyon": ("Veri Sorumluları Sicili Hakkında Yönetmelik", M.format(24276, 7)),
    "silmeyon": ("Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik", M.format(24038, 7)),
    "tebligaydin": ("Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ", "https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=24454&mevzuatTur=Teblig&mevzuatTertip=5"),
    "kurul2023": ("KVKK, 2023/1154 sayılı Kurul Kararı (VERBİS kayıt istisnası)", "https://www.kvkk.gov.tr/Icerik/7647/2023-1154"),
}

POSTS = [
# ---------------------------------------------------------------------------
{
"slug": "cerez-banneri-en-sik-5-hata",
"cat": "KVKK", "cat_en": "Data protection", "date": "2026-06-17",
"title": "Çerez banner'larında en sık görülen beş hata",
"title_en": "The five most common cookie banner mistakes",
"excerpt": "Saklı Reddet düğmesi, önceden işaretli kutular, rızadan önce yazılan çerezler. Rehber'e göre banner'ınızı beş soruda test edin.",
"cover": 1,
"src": ["rehber", "6698"],
"body": """
<p>Çerez banner'ı bir tasarım süsü değil, açık rızanın toplandığı yerdir. KVKK'nın Çerez Uygulamaları Hakkında Rehberi'nin güncel sürümü (Temmuz 2025) bu mekanizmanın nasıl kurulması gerektiğini ayrıntılı anlatıyor. Uygulamada ise aynı beş hata sık sık karşıma çıkıyor.</p>

<h2>1. Reddet düğmesi yok ya da saklı</h2>
<p>Kocaman bir "Kabul et" ve yanında soluk gri bir "Ayarlar" bağlantısı. Rehber, "Kabul et", "Reddet" ve "Tercihler" düğmelerinin renk, büyüklük ve punto bakımından eşit sunulmasını iyi uygulama örneği olarak gösteriyor (s.30). Reddetmek için üç menü açmak gereken bir tasarımda rızanın özgür iradeye dayandığını ispat etmek zorlaşır.</p>

<h2>2. Kutular önceden işaretli</h2>
<p>Tercih panelini açıyorsunuz; analitik ve pazarlama zaten açık. Rehber'e göre açık rızayla işlenmesi gereken çerezlerin yönetim panelinde ilk elde pasif gelmesi gerekir (s.31). Önceden işaretli kutu kullanıcının değil, sitenin iradesidir.</p>

<h2>3. Rıza gelmeden çerezler yazılmış</h2>
<p>En teknik ama en ağır hata budur. Rehber, açık rızanın çerezler yerleştirilmeden önce alınmasını ister (s.29). Banner ekranda dururken arka planda analitik ve reklam pikselleri çalışıyorsa banner dekordan ibarettir.</p>
<div class="test"><b>Pratik test</b>Sitenizi gizli pencerede açın. Hiçbir şeye tıklamadan geliştirici araçlarında çerezlere bakın. Zorunlu olmayan tek bir çerez görüyorsanız kurulum yanlış.</div>

<h2>4. "Gezinmeye devam etmek kabul sayılır"</h2>
<p>Banner'da "sitemizi kullanmaya devam ederek çerezleri kabul etmiş olursunuz" yazıyorsa rıza aktif bir hareketle verilmemiş demektir. Rehber, siteye girmenin tek başına açık rıza sayılamayacağını açıkça belirtir (s.28). Sayfayı kaydırmak da rıza değildir.</p>

<h2>5. Rızayı geri almanın yolu yok</h2>
<p>Banner bir kez kapanıyor ve bir daha ulaşılamıyor. Rehber, rızanın geri alınabilmesini ve yönetim paneline her an erişilebilmesini ister; bunun için sayfada kalıcı küçük bir simgeyi iyi örnek olarak gösterir (s.29-30). Her sayfanın altındaki bir "Çerez tercihleri" bağlantısı bu işi görür.</p>

<h2>Beşinin ortak kökü</h2>
<p>Beş hatanın arkasında aynı yanılgı var: banner'ı bir uyarı kutusu sanmak. Oysa kaydı sizde durmalıdır. Hangi tarihte, hangi kategorilere, banner'ın hangi sürümünde onay verildiği gösterilebilmelidir.</p>
<p>Bu sitenin çerez paneli, bu beş kuralın tümüne göre kurulmuştur.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "cerez-duvari-neden-gecerli-riza-degil",
"cat": "KVKK", "cat_en": "Data protection", "date": "2026-07-10",
"title": "Kabul etmezsen giremezsin: çerez duvarı rızayı neden tehlikeye atar?",
"title_en": "\"Accept or leave\": why a cookie wall puts consent at risk",
"excerpt": "Reddet seçeneği olmayan ve içeriği kilitleyen banner, rızayı hizmetin ön koşuluna çevirir. Rehber'in yaklaşımı ve geçerli rızanın üç unsuru.",
"cover": 2,
"src": ["rehber", "6698"],
"body": """
<p>Bir habere tıklıyorsunuz, ekranı bir pencere kaplıyor ve tek gerçek seçenek "Tümünü kabul et". Reddet düğmesi ya menülerin altına gömülmüş ya da hiç yok. Kapatmaya çalıştığınızda içerik gri bir perdenin arkasında kilitli kalıyor. Bu tasarıma <strong>çerez duvarı</strong> deniyor.</p>

<h2>Rıza neden sakatlanabilir?</h2>
<p>6698 sayılı KVKK m.3/1-a açık rızayı "belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan rıza" olarak tanımlar. Çerez duvarı üçüncü unsura dokunur. Kişi analitik ve pazarlama çerezlerini istemese bile içeriğe ulaşmak için kabul etmek zorunda kalıyorsa, verdiği onay bir tercih değil, bir kaçış refleksidir.</p>
<p>KVKK'nın Çerez Rehberi (Temmuz 2025) konuyu bu çerçevede ele alır. Rıza hizmetin ön koşulu hâline getirildiğinde özgür iradenin sakatlanabileceğini belirtir. Her olayın ayrıca değerlendirileceğini ve adil alternatifler sunulabileceğini de not eder (s.31-32). Duvar kendiliğinden hukuka aykırı değildir; ama kuran taraf, rızanın özgür olduğunu ispat yükünü ağırlaştırır.</p>

<h2>Zorunlu çerez ile pazarlama çerezi aynı şey değil</h2>
<ul>
<li><strong>Zorunlu çerezler</strong> oturum açma, form doldurma ya da gizlilik tercihinin hatırlanması gibi hizmetin çalışması için gereken işlevleri görür. Rehber bunları genel olarak açık rıza dışındaki işleme şartlarına dayanan çerezler arasında sayar.</li>
<li><strong>Analitik ve pazarlama çerezleri</strong> hizmetin sunulması için gerekli değildir. Açık rıza alınmadan yerleştirilemezler.</li>
</ul>
<p>Çerez duvarının sorunu tam burada başlar. Hizmete erişim, hizmet için gerekli olmayan bir işleme razı olmaya bağlanır.</p>

<div class="test"><b>Pratik test</b>Reddetmek, kabul etmek kadar kolay mı? Aynı ekranda, aynı büyüklükte ve tek tıkla ulaşılan bir "Reddet" düğmesi yoksa rızanın özgür iradeye dayandığını ispat etmek zorlaşır.</div>

<h2>Sessiz onay da onay değil</h2>
<p>Önceden işaretli kutular ve "siteyi kullanmaya devam ederek kabul etmiş sayılırsınız" ifadesi aynı sorunun sessiz biçimleridir. Rehber, onayın aktif bir hareketle verilmesini ister ve siteye girmeyi rıza saymaz (s.28). Eylemsizlik bir irade beyanı değildir.</p>

<h2>Geçerli rıza neye benzer?</h2>
<p>Ziyaretçi hangi çerezin ne için çalıştığını anlayabilmeli. Onay tereddütsüz ve aktif bir hareketle verilmeli. Reddetmek, kabul etmekle aynı görünürlükte durmalı. Bu üçü bir arada değilse toplanan onay kâğıt üzerinde kalır.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "reklamda-kanitsiz-ustunluk-iddialari",
"cat": "Reklam", "cat_en": "Advertising", "date": "2026-07-08",
"title": "\"En iyi\", \"%100\", \"mucize\": reklamda kanıtsız üstünlük iddiası",
"title_en": "\"Best\", \"100%\", \"miracle\": unsubstantiated superiority claims in advertising",
"excerpt": "İddia reklam verenin, ispat da reklam verenin. Hangi belge kanıt sayılır, sağlık ve kozmetikte çıta neden daha yüksek?",
"cover": 3,
"src": ["6502", "reklamyon", "kozmetik"],
"body": """
<p>"Türkiye'nin en iyisi", "%100 doğal", "garantili sonuç". Bir e-ticaret sitesinin ana sayfasında, ürün başlığında, hatta meta açıklamasında bu ifadelerden en az biri çoğu zaman yer alır. Sorun kelimede değil, arkasında belge olmamasında.</p>

<h2>İddia sizin, ispat da sizin</h2>
<p>6502 sayılı Tüketicinin Korunması Hakkında Kanun m.61/3 aldatıcı ve yanıltıcı reklamı yasaklar. İspat yükü açıktır: reklamdaki iddiayı reklam veren ispatlar (6502 s. Kanun m.61/6; Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği m.9/1). "En ucuz biziz" dediğinizde bunu Reklam Kurulu'na siz kanıtlarsınız.</p>
<p>Kanıtın niteliği de düzenlenmiştir. Yönetmelik m.9/2 bilimsel ve bağımsız araştırmaları, akredite kuruluş raporlarını esas alır. m.9/4 ise sunulan raporun iddiayı <strong>reklamın yayınlandığı dönem</strong> için kanıtlamasını ister. Bu yüzden en güvenli yol, belgeyi yayından önce hazırlamaktır.</p>

<div class="test"><b>Pratik test</b>Sitenizdeki her üstünlük cümlesinin yanına bir not düşün: "Bunu kime, hangi belgeyle kanıtlarım?" Yalnızca kendi satış verinizi gösterebiliyorsanız, "sektörün lideri" iddiası bağımsız belgeyle desteklenmiş sayılmaz.</div>

<h2>Sağlık ve kozmetik: çıta daha yüksek</h2>
<p>Yönetmelik m.16/3, reklamda doktor, diş hekimi, veteriner hekim, eczacı veya sağlık kuruluşlarının ürün hakkında sağlık beyanında bulunduğu izleniminin verilmesini yasaklar. "Doktorların önerdiği" gibi bir ifade tek başına sorun doğurur.</p>
<p>Kozmetikte durum daha nettir. Kozmetik Ürünler Yönetmeliği m.4 kozmetiği temizleme, koku verme, görünümü değiştirme ve koruma amaçlarıyla tanımlar; tedavi bu tanımda yoktur. m.23/1 ürünün sahip olmadığı özellik veya işlevi ima eden iddiaları yasaklar. "Selülitleri bitirir" yazan bir krem sayfası bu nedenle risk altındadır.</p>

<h2>Karşılaştırmalı reklam</h2>
<p>Rakibi kötüleyemezsiniz; karşılaştırdığınız özellik nesnel, ölçülebilir ve ürün için tipik olmalıdır (Yönetmelik m.8/1-e ve g). Durdurulan bir reklamı küçük bir kelime değişikliğiyle yeniden yayımlamak aynı ihlali sürdürmek anlamına gelebilir. Kurul, ceza miktarını belirlerken aykırılığın ağırlığını ve kusuru dikkate alır (6502 s. Kanun m.77/12).</p>

<h2>Yayından önce üç adım</h2>
<ul>
<li>Mutlak iddiaları tarayın: en, %100, garantili, mucize, anında.</li>
<li>Her iddianın belgesini yayından önce dosyalayın; belge yoksa ifadeyi yumuşatın.</li>
<li>Sağlık çağrışımı olan cümleleri ayrıca ve öncelikle inceleyin.</li>
</ul>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "reklam-kurulu-nasil-calisir",
"cat": "Reklam", "cat_en": "Advertising", "date": "2026-07-09",
"title": "Reklam Kurulu'nda bir dosyanın yolculuğu",
"title_en": "The life cycle of a case before Türkiye's Advertising Board",
"excerpt": "Dosya şikâyetle ya da re'sen açılır, Kurul ayda en az bir kez toplanır. Başvurudan yaptırıma kadar her durak ve ispatın zamanlaması.",
"cover": 4,
"src": ["6502", "rkyon", "reklamyon"],
"body": """
<p>Uygulamada sık görülen tablo şudur: şirket, aylar önce yayımladığı kampanyanın Kurul gündemine girdiğini iş işten geçtikten sonra öğrenir. Pazarlama ekibi başka projeye geçmiştir, iddiayı destekleyen belge hiç hazırlanmamıştır. Mekanizmayı bilenler için bu sürpriz değildir.</p>

<h2>Dayanak</h2>
<p>Reklam Kurulu'nun dayanağı 6502 sayılı Tüketicinin Korunması Hakkında Kanun'dur. m.61 ticari reklamın ilkelerini ve ispat yükünü, m.62 haksız ticari uygulamaları, m.63 Kurul'un kendisini düzenler. Usul, Reklam Kurulu Yönetmeliği'ndedir.</p>

<h2>Dosya nasıl açılır?</h2>
<p>İki yolu vardır. Birincisi başvurudur: Reklam Kurulu Yönetmeliği m.8, gerçek ve tüzel kişilerin başvurabileceğini öngörür. Bu yolu tüketiciler kadar rakipler de kullanır. İkincisi re'sen incelemedir: Kurul Başkanı, başvuru olmadan da inceleme başlatabilir (m.15/1-b).</p>
<p>Kurul ayda en az bir kez, gerektiğinde daha sık toplanır (m.9/1).</p>

<h2>İspat yükü ve zamanlama</h2>
<p>İddiayı kanıtlama yükü reklam verendedir (6502 s. Kanun m.61/6). Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği m.9/4 ise sunulan belgenin iddiayı reklamın yayınlandığı dönem için kanıtlamasını ister. Savunma aşamasında ısmarlanan bir test raporu bu şartı her zaman karşılamaz.</p>

<div class="test"><b>Pratik test</b>Sitenizdeki her iddialı cümle için tek soru sorun: bu cümle yayına girdiği gün, onu destekleyen belge elimde miydi?</div>

<h2>Yaptırımlar</h2>
<p>İhlal tespit edilirse Kurul, 6502 s. Kanun m.63/1 ve m.77/12 kapsamında şu araçlardan seçer:</p>
<ul>
<li><strong>Durdurma:</strong> reklamın yayınına son verilir; Kurul üç aya kadar tedbiren durdurma kararı da verebilir.</li>
<li><strong>Düzeltme:</strong> ihlal, aynı yöntemle yayımlanacak düzeltmeyle giderilir.</li>
<li><strong>İdari para cezası.</strong></li>
<li><strong>Erişim engelleme:</strong> internetteki ihlallerde içerik önce kaldırılmak üzere bildirilir; bildirim mümkün değilse erişim engellenir.</li>
</ul>
<p>Kararlar kamuya duyurulur (Reklam Kurulu Yönetmeliği m.14). Markanın adı ihlal anlatısıyla birlikte herkesin erişebildiği bir metne girer.</p>
<p>Sorumluluk tek omuzda da değildir. Reklam veren, reklam ajansı ve mecra kuruluşu aynı kurallara uymakla yükümlüdür (6502 s. Kanun m.61/7). "Ajans hazırladı" savunması dosyadaki kişi sayısını azaltmaz.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "iys-kanal-bazli-onay-ve-ret",
"cat": "E-ticaret", "cat_en": "E-commerce", "date": "2026-07-05",
"title": "SMS atmadan önce: İYS'de kanal bazlı onay ve 3 iş günü kuralı",
"title_en": "Before you hit send: channel-based consent and the 3-working-day rule",
"excerpt": "Kargo için verilen numara kampanya onayı değildir. Onay kanal bazında alınır, İYS'ye kaydedilir; ret gelince saat işlemeye başlar.",
"cover": 5,
"src": ["6563", "iysyon"],
"body": """
<p>Sık duyulan bir itiraz: "Ben bu firmaya numaramı hiç vermedim." Aslında vermiştir, ama kargo takibi için. Sorun şu: teslimat bildirimi için verilen numara, kampanya SMS'i için verilmiş onay değildir. Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik m.6/2 teslimat gibi bildirimler için onay aramaz, ama bu iletilerde ürün tanıtımı yapılmasına da izin vermez.</p>

<h2>Önce onay, sonra İYS kaydı</h2>
<p>6563 sayılı Kanun m.6/1 uyarınca ticari elektronik ileti alıcının önceden onayı olmadan gönderilemez. İYS tarafı ise Yönetmelik'tedir. Onay İYS üzerinden alınmadıysa 3 iş günü içinde İYS'ye kaydedilmelidir (m.7/11). Kaydedilmeyen onay geçersiz sayılır (m.7/12) ve İYS'de onayı olmayan alıcıya ileti gönderilemez (m.5).</p>

<h2>Onay kanala göre ayrı ayrı alınır</h2>
<p>En pahalı yanılgı, tek bir "evet"in her şeyi kapsadığını sanmaktır. SMS, e-posta ve arama ayrı kanallardır; ileti, alınan onayın kapsamına uygun olmalıdır (Yönetmelik m.8/1). Ret de kanal bazında işler: ret bildirimi o kanal için onayı ortadan kaldırır (m.9/1) ve ret imkânı iletinin geldiği kanalda sunulmalıdır (m.9/3).</p>
<p>Onayın şekli de önemlidir:</p>
<ul>
<li>Önceden işaretli kutu geçerli onay değildir (m.7/8).</li>
<li>Onay, mal veya hizmet satışının ön şartı yapılamaz (m.7/9).</li>
<li>Onay bir sözleşmenin içinde alınacaksa, m.7/5'teki şekil şartlarına uyulmalıdır: imzadan önce, ayrı başlık altında, en az 12 punto ve ret seçeneğiyle.</li>
<li>İletide göndereni tanıtan bilgiler yer almalıdır: SMS'te MERSİS numarası (esnaf için ad-soyad ile T.C. kimlik veya vergi numarası), e-postada unvan ve MERSİS numarası ile en az bir iletişim bilgisi (6563 s. Kanun m.7/2; Yönetmelik m.8).</li>
</ul>

<div class="test"><b>Pratik test</b>Son kampanya SMS'inizi açın. Alıcı kim olduğunuzu görüyor mu? Tek adımda ve ücretsiz reddedebiliyor mu? O numara için SMS kanalında İYS onay kaydınız var mı? Biri bile "hayır"sa o gönderim şikâyete aday.</div>

<h2>Ret gelince saat işlemeye başlar</h2>
<p>Alıcı onayını her an ve gerekçe göstermeden geri alabilir (6563 s. Kanun m.8/1). Gönderim, ret talebinin ulaşmasından itibaren <strong>3 iş günü</strong> içinde durdurulmalıdır (m.8/3). Ret bildiriminin kolay ve ücretsiz iletilebilmesini sağlamak da gönderenin yükümlülüğüdür (m.8/2). Doğrudan size iletilen retleri de 3 iş günü içinde İYS'ye bildirmeniz gerekir (Yönetmelik m.9/6). Uygulamada en sık takılınan yer burasıdır: ret İYS'ye düşer, kimse gönderim listesini güncellemez ve dördüncü gün giden tek bir SMS şikâyete dönüşür.</p>
<p>Gece yarısı gönderimi yasaklayan bir hüküm 6563'te ve bu Yönetmelik'te yoktur. Ama ret düğmesine en hızlı o saatte basılır.</p>

<h2>Esnaf ve tacirler</h2>
<p>Esnaf ve tacirlere gönderimde önceden onay aranmaz (6563 s. Kanun m.6/2). Ret hakkı orada da işler. Gönderimden önce alıcının İYS'de ret kaydı olup olmadığı kontrol edilmelidir (Yönetmelik m.6/3 ve m.6/6).</p>
<p>İspat yükü her durumda gönderendedir. Onaya ilişkin kayıtlar 3 yıl saklanmalıdır (Yönetmelik m.13). Kaydı olmayan onay, yok hükmündedir.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "uye-kayit-formu-kvkk-ve-5651",
"cat": "KVKK", "cat_en": "Data protection", "date": "2026-07-10",
"title": "Üyelik formu açtınız: aynı ekranda iki ayrı hukuki yük",
"title_en": "One sign-up form, two legal burdens",
"excerpt": "Üyelik formu hem bir veri işleme noktası hem de ticari ileti onayının alındığı yer. Aydınlatma, açık rıza ve onayı neden ayrı kurmalısınız?",
"cover": 6,
"src": ["6698", "tebligaydin", "6563", "iysyon", "5651"],
"body": """
<p>Siteye "Üye ol" düğmesi eklendiği an çoğu ekip tek bir soru sorar: hangi metni koyalım? Oysa o formla birlikte masaya birden fazla yük gelir ve her biri farklı mantıkla çalışır.</p>

<h2>Birinci yük: kişisel veri</h2>
<p>Kullanıcı ad-soyad, e-posta ve telefon girip hesap oluşturduğunda bir kişisel veri işleme faaliyeti başlar. Kayıt anında aydınlatma yapılmalıdır (6698 s. KVKK m.10). Aydınlatma bir bilgilendirmedir; kullanıcının "okudum, kabul ediyorum" demesini gerektirmez.</p>
<p>İşleme açık rızaya dayanıyorsa aydınlatma ile açık rıza ayrı ayrı alınmalıdır (Aydınlatma Tebliği m.5/1-f). İkisini tek kutuya bağlayan bir form, alınan rızanın geçerliliğini ciddi biçimde tartışmalı hâle getirir.</p>

<h2>İkinci yük: ticari ileti onayı</h2>
<p>Üyelere kampanya e-postası ya da SMS göndermek istiyorsanız 6563 sayılı Kanun m.6 uyarınca ayrı ve açık bir <strong>onay</strong> gerekir. Bu onay üyeliğin şartı yapılamaz (Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik m.7/9) ve İYS'ye kaydedilmelidir (m.7/11).</p>
<ul>
<li>Aydınlatma: bilgi verir, onay istemez.</li>
<li>Açık rıza (KVKK): gerekiyorsa ayrı alınır.</li>
<li>Ticari ileti onayı (6563): ayrı, serbest ve İYS'ye kayıtlı olur.</li>
</ul>

<div class="test"><b>Pratik test</b>"Kampanyalardan haberdar olmak istiyorum" kutusunu işaretlemeden üye olunabiliyor mu? Olunamıyorsa onay serbest değildir.</div>

<h2>Görünmeyen yük: 5651</h2>
<p>Kendi içeriğini sunan bir site, 5651 sayılı Kanun'da öncelikle içerik sağlayıcıdır (m.2/1-f). Kullanıcıların içerik yükleyebildiği alanlar açıyorsanız o alanlar bakımından yer sağlayıcı konumuna geçebilirsiniz (m.2/1-m). Yer sağlayıcı, sunduğu hizmete ilişkin trafik bilgisini yönetmelikle belirlenen, bir yıldan az ve iki yıldan fazla olmayan süre saklamakla, doğruluğunu, bütünlüğünü ve gizliliğini sağlamakla yükümlüdür (m.5/3).</p>
<p>Formun ön yüzünde rıza mimarisini kurarken arka yüzde kayıtların nasıl tutulacağına da o gün karar verilir. Sonradan istendiğinde okunabilir ve tutarlı olmaları bu karara bağlıdır.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "verbis-kayit-yukumlulugu",
"cat": "KVKK", "cat_en": "Data protection", "date": "2026-07-10",
"title": "VERBİS: \"biz küçüğüz\" demeden önce sorulacak soru",
"title_en": "VERBİS: the question to ask before saying \"we're too small\"",
"excerpt": "Kayıt kural, istisna Kurul'un çizdiği bir çerçeve. İstisna kapsamında olmak hangi yükümlülükleri kaldırır, hangilerini bırakır?",
"cover": 7,
"src": ["6698", "verbisyon", "kurul2023", "silmeyon"],
"body": """
<p>Sık duyulan cümle: "Biz küçük bir firmayız, VERBİS bizi ilgilendirmez." Sitenin iletişim formu, bülten kutusu ve başvuru sayfası ise aynı firmanın kişisel veri işlediğini gösterir. Bu cümlenin arkasında çoğu zaman kötü niyet değil, kaydın ne zaman ve kimin için zorunlu olduğuna dair bir yanlış anlama vardır.</p>

<h2>Kural: işlemeye başlamadan önce kayıt</h2>
<p>Veri sorumluları, veri işlemeye başlamadan önce Veri Sorumluları Siciline kaydolmak zorundadır (6698 s. KVKK m.16/2; Veri Sorumluları Sicili Hakkında Yönetmelik m.5/1-a). Kayıt veriyi topladıktan sonra tamamlanacak bir formalite değildir. Site yayına alınıp formlar çalışmaya başladığında süre çoktan işlemeye başlamıştır.</p>

<h2>İstisna bir muafiyet değil, bir çerçevedir</h2>
<p>Kurul, bazı veri sorumlularını kayıt yükümlülüğünden istisna tutar. Ölçütler çalışan sayısı, yıllık mali bilanço toplamı ve ana faaliyetin özel nitelikli veri işlemeye dayanıp dayanmamasıdır (ör. 2023/1154 sayılı Kurul Kararı). Kurul bu ölçütleri zaman içinde güncelleyebildiğinden, karar vermeden önce kvkk.gov.tr'deki güncel karar kontrol edilmelidir.</p>
<p>İki yanılgı tehlikelidir. Birincisi: "küçük olmak" tek başına yetmez; ölçütler birlikte değerlendirilir. İkincisi: istisna yalnızca kayıttan istisnadır.</p>

<div class="test"><b>Pratik test</b>Sitenizde ad, e-posta, telefon ya da özgeçmiş alan tek bir alan bile varsa kişisel veri işliyorsunuz. Sorulacak soru "veri işliyor muyum" değil, "istisna ölçütlerinin hepsini gerçekten karşılıyor muyum" olmalı.</div>

<h2>İstisna neyi kaldırmaz?</h2>
<p>Kayıttan istisna olan veri sorumlusu için şu yükümlülükler aynen devam eder:</p>
<ul>
<li>Her form için aydınlatma yapılması (6698 s. KVKK m.10),</li>
<li>Veri güvenliği için teknik ve idari tedbirlerin alınması (m.12),</li>
<li>İşleme sebebi ortadan kalkan verinin silinmesi, yok edilmesi veya anonim hâle getirilmesi (m.7).</li>
</ul>
<p>Yazılı bir saklama ve imha politikası hazırlama yükümlülüğü ise yalnızca Sicile kayıt zorunluluğu olanlar içindir (Silme Yönetmeliği m.5/1). İstisna kapsamındaki veri sorumlusu bu belgeyi hazırlamak zorunda değildir, ama süresi dolan veriyi silme yükümlülüğü sürer (m.5/3).</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "iade-magaza-kredisi-dayatilamaz",
"cat": "Tüketici", "cat_en": "Consumer law", "date": "2026-05-20",
"title": "\"İadenizi hediye çeki olarak yaptık\" diyemezsiniz",
"title_en": "You can't refund with store credit",
"excerpt": "Cayma hâlinde bedel, ödendiği araca uygun biçimde ve tek seferde iade edilir. Süre ne zaman başlar, hediye çeki neden yerine geçmez?",
"cover": 8,
"src": ["msy", "6502"],
"body": """
<p>Cayma bildirimi geldi, süreç doğru işledi, sıra iadede. Müşterinin hesabına hediye çeki tanımlandı. "Böylece müşteri bizde kalıyor" düşüncesi pazarlama açısından anlaşılır. Hukuken savunulamaz.</p>

<h2>Kural: ödeme aracına uygun, tek seferde</h2>
<p>Mesafeli Sözleşmeler Yönetmeliği m.12/4, iadenin tüketicinin satın alırken kullandığı ödeme aracına uygun şekilde, tüketiciye herhangi bir masraf veya yükümlülük getirmeden ve tek seferde yapılmasını emreder. Kredi kartıyla ödendiyse karta, havaleyle geldiyse hesaba iade edilir. Aynı hüküm, kart çıkaran kuruluşun iade tutarını kart limitine tek seferde eklemesini de öngörür.</p>
<p>Hediye çeki, puan veya mağaza kredisi bu yükümlülüğün yerine geçmez.</p>

<h2>Süre ne zaman başlar?</h2>
<p>İade süresi 14 gündür, ama başlangıcı işlemin türüne göre değişir (Yönetmelik m.12):</p>
<ul>
<li><strong>Teslim edilmiş mallarda</strong>, malın ön bilgilendirmede belirtilen iade taşıyıcısına teslim edildiği tarihten; başka bir taşıyıcı kullanılmışsa malın satıcıya ulaştığı tarihten başlar (m.12/1).</li>
<li><strong>Teslimattan önce caymada</strong> cayma bildiriminin ulaştığı tarihten başlar (m.12/2).</li>
<li><strong>Hizmetlerde</strong> de cayma bildiriminin ulaştığı tarih esas alınır (m.12/3).</li>
</ul>

<h2>Sahada görülen üç kalıp</h2>
<ul>
<li>"İadeler yalnızca hediye çeki olarak yapılır": m.12/4'e aykırıdır; sözleşmeye yazılmışsa 6502 s. Kanun m.5 anlamında haksız şart niteliği taşıması muhtemeldir.</li>
<li>"Kapıda ödemede iade mağaza kredisiyle yapılır": ödeme aracına uygun iade kuralı burada da geçerlidir.</li>
<li>"İade 30 gün içinde yapılır": süre 14 gündür.</li>
</ul>

<div class="test"><b>Pratik test</b>İade ve cayma metninizde "hediye çeki", "mağaza kredisi" veya "alışveriş kredisi" geçiyorsa cümlenin bağlamına bakın. Tüketiciye seçenek değil dayatma sunuluyorsa düzeltin.</div>
<p>Bu tür uyuşmazlıklarda tüketici, ödeme aracına iade yapılmadığını dekontla kolayca ortaya koyabilir.</p>
""",
},
]
