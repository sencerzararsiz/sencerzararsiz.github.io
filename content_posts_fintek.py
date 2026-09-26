"""Fintek ve sözleşme yazıları.
Mevzuat atıfları mevzuat.gov.tr metinlerinden 26.09.2026 tarihinde doğrulanmıştır.
Akademik kaynak: Baker & Odinet, "The Gamification of Banking", 2025 U. Ill. L. Rev. 1567.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip={}"

SRC_FIN = {
    "6362": ("6362 sayılı Sermaye Piyasası Kanunu", M.format(6362, 1, 5)),
    "6502": ("6502 sayılı Tüketicinin Korunması Hakkında Kanun", M.format(6502, 1, 5)),
    "6493": ("6493 sayılı Ödeme ve Menkul Kıymet Mutabakat Sistemleri, Ödeme Hizmetleri ve Elektronik Para Kuruluşları Hakkında Kanun", M.format(6493, 1, 5)),
    "6698": ("6698 sayılı Kişisel Verilerin Korunması Kanunu", M.format(6698, 1, 5)),
    "bakerodinet": ("Colleen Baker & Christopher K. Odinet, \"The Gamification of Banking\", University of Illinois Law Review, 2025, s.1567", "https://scholarship.law.tamu.edu/facscholar/2310"),
    "6098": ("6098 sayılı Türk Borçlar Kanunu", M.format(6098, 1, 5)),
    "6102": ("6102 sayılı Türk Ticaret Kanunu", M.format(6102, 1, 5)),
    "6100": ("6100 sayılı Hukuk Muhakemeleri Kanunu", M.format(6100, 1, 5)),
    "5846": ("5846 sayılı Fikir ve Sanat Eserleri Kanunu", M.format(5846, 1, 3)),
}

POSTS_FIN = [
# ---------------------------------------------------------------------------
{
"slug": "finansal-oyunlastirma-hukuki-sinirlar",
"cat": "Fintek", "cat_en": "Fintech", "date": "2026-09-26",
"title": "Finansal oyunlaştırma: yatırım ve bankacılık uygulamalarında oyunun hukuki sınırları",
"title_en": "Financial gamification: the legal limits of play in investing and banking apps",
"excerpt": "Rozet, seri ve liderlik tablosu kendi başına yasak değil. Sınırı, mekaniğin neyi ödüllendirdiği çizer: ders mi, işlem mi, gerçek para mı?",
"cover": 20,
"src": ["bakerodinet", "6362", "6502", "6493", "6698"],
"body": """
<p>Bir yatırım veya bankacılık uygulamasına rozet, seri ya da liderlik tablosu eklemek Türk hukukunda kendi başına yasak değildir. Sınırı mekaniğin kendisi değil, bağlandığı davranış çizer. Rozet bir finansal okuryazarlık dersini ödüllendiriyorsa mesele bir tasarım tercihidir. Aynı rozet işlem sayısını, yatırılan tutarı veya kaldıraçlı bir pozisyonu ödüllendirdiğinde sermaye piyasası izni, tüketici hukuku ve kişisel verilerin korunması birlikte devreye girer. Para cüzdanı varsa ödeme hizmetleri mevzuatı da.</p>

<h2>Oyun bankacılığa nasıl girdi</h2>
<p>Colleen Baker ve Christopher K. Odinet, University of Illinois Law Review'da 2025'te yayımlanan "The Gamification of Banking" makalesinde bu dönüşümü ABD bankacılığı üzerinden inceler. Yazarlar örnekleri üç kümeye ayırır: sanal bir ekonomide kazanmak, finansal okuryazarlığı teşvik etmek ve finansal iyi oluşu hedeflemek. Yayılmayı da üç dalgada anlatırlar: banka-fintek ortaklıkları, özel banka lisansları ve henüz tam gerçekleşmemiş "mega finansal platformlar." Makalenin tartıştığı sorulardan biri, düzenlemenin arayüzü mü yoksa arkasındaki iş modelini mi hedeflemesi gerektiğidir. İşlem sonrası ekranda patlayan konfeti bu tartışmanın simgesi olmuştur.</p>
<p>Türk hukukunda da cevap çoğu zaman iş modelindedir. Aşağıda anılan kanunların hiçbiri konfetiyi yasaklamaz. İzinsiz aracılığı, aldatıcı reklamı ve dayanaksız veri işlemeyi yasaklayan hükümler var.</p>

<h2>Simülasyon ile gerçek işlem arasındaki çizgi</h2>
<p>6362 sayılı Sermaye Piyasası Kanunu, sermaye piyasası araçlarını menkul kıymetler, türev araçlar ve yatırım sözleşmeleri üzerinden tanımlar (m.3/1-ş). Benim değerlendirmem şu: gerçek parayla hiçbir bağı olmayan, satın alınamayan ve paraya çevrilemeyen sanal bir bakiye bu tanımlara girmez; böyle bir alım satım oyunu tek başına izin konusu olmaz. Bakiye satın alınabiliyor, ödüle ya da paraya dönüşebiliyorsa bu değerlendirme değişir.</p>
<p>Çizgi, oyun gerçek bir hesaba bağlandığında aşılır. Döviz ve kıymetli madenler üzerine yapılan kaldıraçlı işlemler türev araç tanımının içindedir (m.3/1-u-3). Forex benzeri bir oyun "turnuvayı kazanana gerçek hesap" veya "sanal kârını gerçek pozisyona taşı" düğmesiyle birleştiğinde, uygulama artık bir yatırım hizmetine açılan kapıdır. Sermaye piyasasında izinsiz faaliyette bulunanlar için yaptırım <strong>iki yıldan beş yıla kadar hapis</strong> ve beş bin günden on bin güne kadar adli para cezasıdır (m.109/2). Türkiye'de yerleşik kişilere internet üzerinden yurt dışında kaldıraçlı işlem yaptırıldığı öğrenilirse Kurul içeriğin çıkarılmasına veya erişimin engellenmesine karar verir (m.99/4).</p>
<p>GameFi tarafında ölçüt kripto varlık tanımıdır: dağıtık defter teknolojisiyle oluşturulan, dijital ağlar üzerinden dağıtılan ve değer ya da hak ifade edebilen gayri maddi varlık (m.3/1-bb, 7518 sayılı Kanun'la eklendi). Oyun içi jeton bu niteliği taşıyor ve uygulama jetonun alım satımına veya takasına aracılık ediyorsa, işletme "platform" tanımına girer (m.3/1-dd). Kripto varlık hizmet sağlayıcısının faaliyete başlamadan Kuruldan izin alması zorunludur (m.35/B-1). Yurt dışındaki bir platformun Türkçe internet sitesi açması, faaliyetin Türkiye'deki kişilere yönelik sayılması için yeterlidir (m.99/A-1). İzinsiz kripto varlık hizmet sağlayıcılığının cezası üç yıldan beş yıla kadar hapistir (m.109/A-1).</p>

<h2>Seri, sıralama ve bildirim</h2>
<p>Yatırım içermeyen bankacılık uygulamaları da serbest alan değildir. Tüketicinin tecrübe ve bilgi noksanlığını istismar eden ticari reklam yapılamaz (6502 sayılı Kanun m.61/3). Reklamdaki iddiaların doğruluğunu ispat yükü reklam verendedir (m.61/6). Mesleki özenin gereklerine uymayan ve ortalama tüketicinin ekonomik davranışını önemli ölçüde bozan ya da bozma ihtimali taşıyan ticari uygulama haksızdır (m.62/1). Uygulamanın haksız olmadığını ispat etmek işletmeye düşer (m.62/2).</p>
<p>Somut bir örnek: "Serini kaybetme, bugün bir işlem yap" bildirimi kullanıcıyı kayıp korkusuyla işleme iter. Yalnızca en çok kazananları gösteren bir liderlik tablosu kaybedenleri görünmez kılar. İkisi de m.62'deki ölçüte doğrudan temas eder. Aynı seri bir tasarruf hedefine veya tamamlanan bir derse bağlandığında itirazın dayanağı zayıflar.</p>

<h2>Cüzdan ve davranış verisi</h2>
<p>Oyun içi cüzdana gerçek para yüklenebiliyor ve bu para kullanıcılar arasında aktarılabiliyorsa, ödeme hesabının işletilmesi bir ödeme hizmetidir (6493 sayılı Kanun m.12/1-a). Ödeme kuruluşu ancak Türkiye Cumhuriyet Merkez Bankasından izin alarak faaliyette bulunabilir (m.14/1; "Banka" tanımı için m.3/1).</p>
<p>Oyunlaştırmanın yakıtı davranış verisidir. Uygulamanın hangi saatte açıldığı, hangi bildirimin işleme dönüştüğü, kimin seriyi bıraktığı ölçülebilir. Kişisel veri kural olarak açık rıza olmadan işlenemez (6698 sayılı KVKK m.5/1). Sözleşmenin ifası istisnası, veri işlemenin sözleşmenin kurulması veya ifasıyla doğrudan ilgili ve gerekli olmasını arar (m.5/2-c). Hesabı yönetmek bu şartı karşılar. Kullanıcının hangi bildirimle daha çok işlem yapacağını ölçen bir profil ise hesabın işletilmesi için gerekli değildir. Meşru menfaat dayanağı (m.5/2-f) ilgili kişinin temel hak ve özgürlüklerine zarar vermeme koşuluna bağlıdır; işlem sıklığını artırmaya dönük bir profil bu koşulla sınanır. Verilerin münhasıran otomatik sistemlerle analiz edilmesi sonucunda kişi aleyhine bir sonuç doğarsa, kişinin buna itiraz hakkı vardır (m.11/1-g).</p>

<div class="test"><b>Pratik test</b>Uygulamadaki her oyun mekaniğinin yanına ödüllendirdiği davranışı yazın: ders, tasarruf, işlem, yatırılan tutar. "İşlem" veya "tutar" yazan her satır, yukarıdaki dört rejimden en az biri açısından ayrıca incelenmesi gereken satırdır.</div>

<h2>Tek arayüz, birden çok statü</h2>
<p>Baker ve Odinet'in üçüncü dalgası, oyunu, ödemeyi ve yatırımı tek uygulamada birleştiren platformlardır. Böyle bir ürün Türkiye'de tek bir izinle çalışmaz. Kaldıraçlı işlem ve kripto katmanı Sermaye Piyasası Kuruluna, cüzdan katmanı Merkez Bankasına, reklam ve bildirim dili tüketici mevzuatına, profil çıkarma KVKK'ya tabidir. Arayüz tek, hukuki statü katman sayısı kadardır.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "sozlesme-imzalamadan-once",
"cat": "Sözleşme", "cat_en": "Contracts", "date": "2026-09-26",
"title": "Sözleşme imzalamadan önce bakılacak yedi madde",
"title_en": "Seven clauses to check before you sign a contract",
"excerpt": "Taraflardan yetkili mahkemeye kadar yedi kontrol. Cezai şartta tacirin indirim isteyemeyeceği, sorumluluk sınırının ağır kusuru kapsayamayacağı ve fikri hak devrinin yazılı olması gerektiği dahil.",
"cover": 21,
"src": ["6098", "6102", "6100", "5846", "6698"],
"body": """
<p>Sözleşmelerin çoğu imzadan sonra, bir şey ters gittiğinde okunur. Bu yazı imzadan önce yapılacak okuma içindir. Bakılacak yedi madde var. İkisi karşı tarafın kim olduğu ve ne yapacağıyla ilgilidir, üçü paranın nasıl ve ne zaman el değiştireceğini belirler, son ikisi işin kime ait olacağını ve uyuşmazlığın nerede görüleceğini gösterir.</p>

<h2>1. Taraflar ve imza yetkisi</h2>
<p>Sözleşmedeki ticaret unvanını ticaret sicilindeki unvanla karşılaştırın. İmzalayan kişinin temsil yetkisini imza sirkülerinden kontrol edin. Anonim şirkette temsil yetkisine getirilen sınırlamalar iyiniyetli üçüncü kişilere karşı kural olarak hüküm ifade etmez; yetkinin birlikte kullanılmasına ilişkin tescil ve ilan edilmiş sınırlama ise geçerlidir (6102 sayılı TTK m.371/3). Sicilde müşterek imza görünüyorsa tek imza yetmez.</p>

<h2>2. Konu, kapsam ve ekler</h2>
<p>İşin ne olduğu çoğu zaman ana metinde değil, Ek-1'de, teklifte veya teknik şartnamede yazar. O ek imza anında sözleşmeye gerçekten bağlı mı? Ana metin ile ek çeliştiğinde hangisinin esas alınacağı yazıyor mu? Kapsam dışı işler, yani ek revizyon, bakım veya entegrasyon, nasıl fiyatlanacak? Bu soruların cevabı yoksa bedel maddesi de belirsizdir.</p>

<h2>3. Bedel ve ödeme</h2>
<p>Tutarın KDV dahil mi hariç mi olduğu, döviz cinsinden ise hangi kurla ve hangi tarihte çevrileceği yazılmalıdır. Vade de öyle. Muaccel bir borcun borçlusu kural olarak alacaklının ihtarıyla temerrüde düşer; ifa günü taraflarca birlikte belirlenmişse bu günün geçmesi yeterlidir (6098 sayılı TBK m.117). "Uygun bir sürede ödenir" yazan bir sözleşmede gecikme faizi için önce ihtar çekmeniz gerekir. Belirli bir ödeme günü bu adımı ortadan kaldırır.</p>

<h2>4. Süre ve fesih</h2>
<p>Sözleşme belirli süreli mi, otomatik yenileniyor mu? Yenilemeyi durdurmak için kaç gün önce bildirim gerekiyor? Haklı nedenle fesih hâlleri sayılmış mı? En çok atlanan soru ise fesihten sonra ne olacağıdır: veriler, kaynak kodu, ödenmiş ama henüz karşılığı verilmemiş bedel. Bunlar yazılı değilse sözleşme bittiği gün bir müzakere başlar.</p>

<h2>5. Cezai şart ve sorumluluk sınırı</h2>
<p>Bu iki madde, bir ihlalin size ya da karşı tarafa kaça mal olacağını belirler. Taraflar cezanın miktarını serbestçe belirler, ama hâkim aşırı gördüğü ceza koşulunu kendiliğinden indirir (TBK m.182). Borçlu tacirse bu indirimi mahkemeden isteyemez (TTK m.22/1). <strong>Tacir olarak imzaladığınız ceza, ödeyeceğiniz cezadır.</strong></p>
<p>Cezanın ne için kararlaştırıldığı da sonucu değiştirir. Ceza sözleşmenin hiç veya gereği gibi ifa edilmemesi için öngörülmüşse, alacaklı aksi sözleşmeden anlaşılmadıkça ya borcun ya cezanın ifasını isteyebilir. Belirlenen zamanda veya yerde ifa edilmeme için öngörülmüşse ikisini birlikte isteyebilir; ancak ifayı çekincesiz kabul ettiyse bu hak düşer (TBK m.179). Geç teslimi kabul ederken cezayı saklı tuttuğunuzu yazılı bildirin. Alacaklı hiç zarara uğramamış olsa da ceza ödenir; zarar cezayı aşıyorsa alacaklı aşan kısmı ancak borçlunun kusurunu ispat ederek isteyebilir (TBK m.180).</p>
<p>Sorumluluğu sözleşme bedeliyle sınırlayan maddeler yaygındır. Böyle bir sınır ağır kusuru kapsayamaz: borçlunun ağır kusurundan sorumlu olmayacağına ilişkin önceden yapılan anlaşma kesin olarak hükümsüzdür. Uzmanlık gerektiren ve ancak kanun veya yetkili makam izniyle yürütülebilen bir hizmette hafif kusur için sorumsuzluk anlaşması da hükümsüzdür (TBK m.115). Bu tür izne bağlı hizmetler dışında, sorumsuzluğu hafif kusurla sınırlamak maddeyi ayakta tutar. Uzun ve iç içe geçmiş bir ceza maddesinin nasıl okunur hâle getirilebileceğini <a href="/yazilar/sozlesme-tasarimi-bes-yol/">sözleşme tasarımı yazısında</a> kurgusal bir örnekle gösterdim.</p>

<div class="test"><b>Pratik test</b>Sözleşmeyi açmadan iki soruyu kâğıda yazın: "Karşı taraf işi yapmazsa en fazla ne alırım?" ve "Ben yapmazsam en fazla ne öderim?" Sonra sözleşmede bu iki tutarı arayın. Bulamıyorsanız cezai şart ya da sorumluluk maddesi eksiktir.</div>

<h2>6. Fikri mülkiyet, gizlilik ve kişisel veri</h2>
<p>Yazılım, tasarım veya içerik ürettiriyorsanız, bedeli ödemek eserin mali haklarını size geçirmez. Mali haklara dair sözleşmelerin yazılı olması ve devredilen hakların ayrı ayrı gösterilmesi şarttır (5846 sayılı FSEK m.52). "Tüm fikri haklar devredilmiştir" yerine işleme, çoğaltma, yayma, temsil ve umuma iletim hakları tek tek sayılmalıdır (FSEK m.21-25). Aksi kararlaştırılmadıkça mali hakkın devri eserin tercüme ve diğer işlenmelerini kapsamaz (FSEK m.55). Yani bir yazılımın sonraki sürümleri için ayrıca hüküm gerekir.</p>
<p>Gizlilik maddesinde sürenin sözleşme bitince devam edip etmediğine bakın. Karşı taraf sizin adınıza kişisel veri işleyecekse, veri güvenliği tedbirlerinden onunla birlikte müştereken sorumlu olursunuz (6698 sayılı KVKK m.12/2). Bu yükümlülüğün sözleşmede karşılığı olmalıdır.</p>

<h2>7. Uyuşmazlık ve yetkili mahkeme</h2>
<p>Tacirler veya kamu tüzel kişileri, aralarındaki uyuşmazlık için bir veya birden fazla mahkemeyi sözleşmeyle yetkili kılabilir. Aksi kararlaştırılmadıkça dava yalnız o mahkemede açılır (6100 sayılı HMK m.17). Yetki sözleşmesi yazılı olmalı, uyuşmazlığın kaynaklandığı hukuki ilişki belirli veya belirlenebilir olmalı ve yetkili mahkeme gösterilmelidir (HMK m.18/2). Kesin yetki hâllerinde yetki sözleşmesi yapılamaz (HMK m.18/1). Karşı taraf tacir değilse "İstanbul mahkemeleri yetkilidir" cümlesi HMK m.17'ye dayanamaz.</p>
""",
},
]
