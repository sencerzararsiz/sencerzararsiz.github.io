"""Teknoloji yazıları: ISO/IEC 27001 iç denetim ve smart contract audit.
Mevzuat atıfları mevzuat.gov.tr metinlerinden (7545, 6362, 6698, 6098) 26.09.2026 tarihinde doğrulanmıştır.
DDO belgeleri cbddo.gov.tr üzerinde yayımlanan PDF sürümlerinden okunmuştur.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"

SRC_TECH = {
    "7545": ("7545 sayılı Siber Güvenlik Kanunu", M.format(7545, 1)),
    "6362": ("6362 sayılı Sermaye Piyasası Kanunu", M.format(6362, 1)),
    "6698": ("6698 sayılı Kişisel Verilerin Korunması Kanunu", M.format(6698, 1)),
    "6098": ("6098 sayılı Türk Borçlar Kanunu", M.format(6098, 1)),
    "iso27001": ("ISO, ISO/IEC 27001:2022 Information security management systems", "https://www.iso.org/standard/27001"),
    "iso27002": ("ISO, ISO/IEC 27002:2022 Information security controls", "https://www.iso.org/standard/75652.html"),
    "ias17021": ("IAS, ISO/IEC 17021-1:2015 Section 9: Process Requirements (özet)", "https://www.iasonline.org/wp-content/uploads/2021/02/17021-1-2015-Section-9.pdf"),
    "bgrehber": ("Cumhurbaşkanlığı Dijital Dönüşüm Ofisi, Bilgi ve İletişim Güvenliği Rehberi", "https://cbddo.gov.tr/bgrehber"),
    "bgdenetim": ("Cumhurbaşkanlığı Dijital Dönüşüm Ofisi, Bilgi ve İletişim Güvenliği Denetim Rehberi, Sürüm 2021/1.0", "https://cbddo.gov.tr/SharedFolderServer/Projeler/File/BG_Denetim_Rehberi.pdf"),
    "bgeslestirme": ("Cumhurbaşkanlığı Dijital Dönüşüm Ofisi, ISO/IEC 27001 - Bilgi ve İletişim Güvenliği Rehberi Eşleştirme Tablosu", "https://cbddo.gov.tr/SharedFolderServer/Projeler/File/ISO27001%20-%20BGRehberEslestirmeTablosu.pdf"),
    "btkdergi": ("H. İ. Özbilger, B. Sarıyar, A. Ertürk, \"Bilgi ve İletişim Güvenliği Rehberinin Uygulanması ve Denetimlerine Yönelik İyileştirme Önerileri\", BTK Dergi, C.1, S.1, 2023, s.1-41", "https://dergipark.org.tr/tr/pub/btkdergi/issue/79910/1292527"),
    "ethsec": ("ethereum.org, Smart contract security", "https://ethereum.org/developers/docs/smart-contracts/security/"),
    "ethforks": ("ethereum.org, Timeline of all Ethereum forks (DAO fork)", "https://ethereum.org/ethereum-forks/"),
    "owaspsc": ("OWASP Smart Contract Top 10 (2025)", "https://owasp.org/www-project-smart-contract-top-10/"),
    "solc080": ("Solidity Documentation, Solidity v0.8.0 Breaking Changes", "https://docs.soliditylang.org/en/latest/080-breaking-changes.html"),
}

POSTS_TECH = [
# ---------------------------------------------------------------------------
{
"slug": "iso-27001-ve-ic-denetim-nedir",
"cat": "Teknoloji", "cat_en": "Technology", "date": "2026-09-26",
"title": "ISO/IEC 27001 BGYS ve iç denetim nedir?",
"title_en": "What is an ISO/IEC 27001 ISMS, and what is an internal audit?",
"excerpt": "ISO/IEC 27001 bir kontrol listesi değil, riske göre kontrol seçen bir yönetim sistemidir. İç denetim bu sistemin kâğıtta değil sahada işleyip işlemediğini kanıtla sınar; kamu kurumlarında ise DDO Rehberi bu denetimi yıllık bir yükümlülüğe bağlar.",
"cover": 15,
"src": ["iso27001", "iso27002", "ias17021", "bgrehber", "bgdenetim", "bgeslestirme", "btkdergi", "7545"],
"body": """
<p>ISO/IEC 27001 sertifikası bir kurumun güvenli olduğunu göstermez. Gösterdiği şey başkadır: kurum bilgi güvenliği risklerini belirleyen, bu risklere göre kontrol seçen ve seçtiği kontrollerin işleyip işlemediğini düzenli ölçen bir yönetim sistemi kurmuştur. İç denetim, bu ölçümün kurum içindeki ayağıdır. Kamu kurumları ve kritik altyapı işletmeleri için ikinci bir katman daha var. Cumhurbaşkanlığı Dijital Dönüşüm Ofisinin (DDO) Bilgi ve İletişim Güvenliği Rehberi'ne uyum, yılda en az bir kez denetlenmek zorundadır.</p>

<h2>BGYS bir karar mekanizmasıdır</h2>
<p>Bilgi güvenliği yönetim sistemi (BGYS), kurumun hangi bilgiyi koruduğunu, o bilgiye ne olabileceğini ve buna karşı ne yaptığını kayda bağlar. Merkezinde risk değerlendirmesi durur. Kurum varlıklarını ve tehditleri belirler, riski puanlar, sonra riski azaltmak, aktarmak, ondan kaçınmak veya kabul etmek arasında seçim yapar.</p>
<p>Klasik anlatım bunu Planla-Uygula-Kontrol et-Önlem al (PUKÖ) döngüsüyle açıklar. Standardın güncel metni bu adı kullanmasa da madde yapısı aynı döngüyü izler: planlama (madde 6), işletim (madde 8), performans değerlendirme (madde 9) ve iyileştirme (madde 10). İç denetim madde 9.2'dedir.</p>

<h2>Ek A: 93 kontrol, dört tema</h2>
<p>ISO/IEC 27001:2022'nin Ek A'sı 93 kontrol içerir ve bunları dört temada toplar: organizasyonel, insan, fiziksel ve teknolojik. Kontrollerin uygulama rehberi ISO/IEC 27002:2022'dir. 2013 sürümündeki 114 kontrol ve 14 başlık bu revizyonla yeniden düzenlendi; tehdit istihbaratı, bulut hizmetlerinin güvenliği, veri maskeleme ve güvenli kodlama yeni kontroller arasındadır.</p>
<p>Ek A zorunlu bir liste değildir. Kurum her kontrol için uygulanabilir olup olmadığını belirler ve gerekçesini Uygulanabilirlik Bildirgesi'ne yazar (madde 6.1.3). Bir kontrolü kapsam dışı bırakmak mümkündür. Gerekçesiz bırakmak değildir.</p>

<h2>İç denetim ile belgelendirme denetimi</h2>
<p>İç denetimi kurum kendisi planlar. Sorduğu soru şudur: BGYS hem standarda hem kurumun kendi kurallarına uygun mu ve gerçekten işliyor mu? Standart, denetçilerin tarafsızlığı gözetilerek seçilmesini ve denetim programı ile sonuçlarının kanıtının saklanmasını ister. Kimse kendi kurduğu süreci denetlememelidir.</p>
<p>Belgelendirme denetimi ise akredite bir belgelendirme kuruluşunun işidir. ISO/IEC 17021-1'e göre ilk belgelendirme iki aşamada yürür: birinci aşamada dokümantasyon ve hazırlık, ikinci aşamada sistemin fiilen işleyişi incelenir. Sertifika üç yıllık bir döngüye girer, ara yıllarda gözetim denetimi yapılır. Belgelendirme denetçisi, iç denetimin yapıldığını ve bulgularının izlendiğini gösteren kayıtları da inceler.</p>

<h2>Denetim kanıtı neye benzer?</h2>
<p>Politika belgesi kontrolün tasarımını gösterir, işletimini değil. DDO'nun Denetim Rehberi bu ayrımı açıkça yapar: denetçi hem tasarım etkinliğini hem işletim etkinliğini test eder. Rehber kanıtta dört nitelik arar: güvenilirlik, uygunluk, yeterlilik ve tekrar edilebilirlik. Sonuncusu, aynı kanıtın başka bir denetçi tarafından aynı koşullarda yeniden elde edilebilmesidir.</p>
<p>Tipik kanıtlar şunlardır:</p>
<ul>
<li>erişim yetkilerinin dönemsel gözden geçirme kayıtları ve ayrılan personelin hesap kapatma tarihleri,</li>
<li>yedekten geri dönüş testinin tarihli çıktısı,</li>
<li>farkındalık eğitimi katılım listeleri,</li>
<li>değişiklik taleplerinin onay akışı,</li>
<li>sızma testi raporu ve bulguların kapatıldığını gösteren yeniden test sonucu,</li>
<li>tedarikçi sözleşmelerindeki güvenlik maddeleri.</li>
</ul>
<p>Rehber'in saydığı yöntemler mülakat, gözden geçirme, güvenlik denetimi, sızma testi ve kaynak kod analizidir. Tüm personele verilmesi gereken eğitim gibi kontrollerde örneklem seçilir; kanıt yetmezse örneklem büyütülür.</p>

<div class="test"><b>Pratik test</b>Uygulanabilirlik Bildirgenizden rastgele bir kontrol seçin. Bu kontrolün son üç ayda çalıştığını gösteren tarihli bir kaydı beş dakika içinde bulabiliyor musunuz? Bulamıyorsanız o kontrol yalnızca kâğıt üzerinde vardır.</div>

<h2>Kamu tarafı: DDO Rehberi ve Denetim Rehberi</h2>
<p>Zincir 2019/12 sayılı Bilgi ve İletişim Güvenliği Tedbirleri Genelgesi ile başlar (RG 06.07.2019, S.30823). Bilgi ve İletişim Güvenliği Rehberi 27 Temmuz 2020'de yayımlandı; Denetim Rehberi'nin 2021/1.0 sürümü Ekim 2021'de geldi. Genelge, kurumların uygulamayı yılda en az bir defa denetlemesini ve sonuçları DDO'ya iletmesini öngörür.</p>
<p>Denetim Rehberi'nin tercihi nettir: denetimi öncelikle iç denetim birimleri yapar. Yetkin iç denetçi yoksa kurum içi diğer personel, başka kamu kurumlarından geçici görevlendirme veya hizmet alımı devreye girer. Hizmet alımında iki sınır var. Son iki yıl içinde kuruma Rehber uyumu konusunda danışmanlık vermiş firmadan denetim hizmeti alınmaz. Aynı firmadan art arda üçten fazla denetim de alınmaz. Raporun belirlenen ekleri, rapor tarihinden itibaren en geç <strong>iki ay</strong> içinde güvenli elektronik imzayla DDO'ya iletilir.</p>
<p>ISO/IEC 27001 ile bağlantı doğrudan kurulmuştur. BGYS kapsamı ile Rehber uyum kapsamı aynıysa BGYS iç tetkiki ve Rehber denetimi tek denetim altında yürütülebilir; DDO bunun için bir eşleştirme tablosu yayımlamıştır. Tablo 2017 ve 2022 sürümlerini birlikte kapsar ve kendi uyarısını taşır: eşleşen bir Rehber tedbiri ile standart kontrolünün birebir aynı hedefi karşıladığı sonucuna varılmamalıdır. Tabloyu bir eksik listesi olarak okumak doğru olur.</p>
<p>Sahadan gelen veri de aynı yöne işaret ediyor. BTK Dergi'de yayımlanan ve 21 kamu iç denetçisiyle yapılan bir araştırma, Rehber denetiminde sekiz iyileştirme alanı saptamış. Bulgu izleme süreci ve sertifikalı iç denetçi eksikliği bunların arasında.</p>

<h2>7545 sayılı Siber Güvenlik Kanunu ne ekledi?</h2>
<p>19.03.2025 tarihinde yürürlüğe giren 7545 sayılı Kanun, siber uzayda faaliyet yürüten kamu kurumlarını, gerçek ve tüzel kişileri kapsar (m.2/1). Bu kişiler tespit ettikleri zafiyet ve siber olayları gecikmeksizin Siber Güvenlik Başkanlığına bildirir (m.7/1-b). Başkanlık, Kanun kapsamındaki fiil ve işlemleri denetleyebilir; denetimi Başkanlık personeli ile yetkilendirilmiş bağımsız denetçiler ve bağımsız denetim kuruluşları yapar (m.8/1, m.6/1-ğ). Denetim programı önemlilik, öncelik ve risk değerlendirmesi ilkelerine göre kurulur (m.8/2).</p>
<p>Kanun ISO/IEC 27001'i anmaz. Standart hazırlama ve kabul etme yetkisini Başkanlığa verir (m.5/1-g). Sertifika bu nedenle bir muafiyet belgesi değildir. İşe yarayan şey, iç denetimin her yıl ürettiği tarihli kanıt dosyasıdır: bir kamu otoritesi kapıyı çaldığında gösterilecek olan odur.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "smart-contract-audit-nedir",
"cat": "Teknoloji", "cat_en": "Technology", "date": "2026-09-26",
"title": "Smart contract audit nedir?",
"title_en": "What is a smart contract audit?",
"excerpt": "Smart contract audit, belirli bir kod sürümünün belirli bir kapsamda incelenmesidir; güvenlik garantisi değildir. Türkiye'de kripto varlık hizmet sağlayıcıları için bilgi sistemleri denetimi ve kayıplardan sorumluluk ise 6362 sayılı Kanun'da doğrudan düzenlenmiştir.",
"cover": 16,
"src": ["ethsec", "owaspsc", "solc080", "ethforks", "6362", "6098", "6698"],
"body": """
<p>Bir smart contract audit raporu, belirli bir commit'teki kodun, belirli bir süre içinde ve belirli bir kapsamla incelendiğini gösterir. Kodun güvenli olduğunu garanti etmez. Denetimden sonra değiştirilen tek bir satır raporu o satır bakımından geçersiz kılar. Türk hukukunda akıllı sözleşme denetimini genel olarak zorunlu tutan bir hüküm bulunmuyor. Kripto varlık hizmet sağlayıcıları için ise tablo farklıdır: 6362 sayılı Sermaye Piyasası Kanunu, 2024'te 7518 sayılı Kanun'la eklenen hükümlerle bilgi sistemleri denetimini ve siber saldırı kaynaklı kayıplardan sorumluluğu açıkça düzenler.</p>

<h2>Audit neyi inceler?</h2>
<p>Akıllı sözleşme, blokzincir üzerinde çalışan ve yayına alındıktan sonra çoğu durumda değiştirilemeyen bir programdır. Hata sonradan yamanamaz. İçinde tutulan varlık da doğrudan saldırının hedefidir. Audit bu yüzden üç katmanda yürür.</p>
<ol>
<li>Kapsam ve tehdit modeli: Hangi sözleşmeler, hangi commit, hangi roller? Yönetici anahtarı kimde, harici fiyat verisi nereden geliyor, sözleşme yükseltilebilir mi?</li>
<li>Otomatik analiz: Statik analiz araçları bilinen kalıpları tarar; fuzzing ve özellik tabanlı testler, sözleşmeyi rastgele girdilerle zorlayarak "toplam arz hiçbir zaman şu değeri aşmaz" gibi değişmezlerin bozulup bozulmadığını arar.</li>
<li>Manuel inceleme: Araçların göremediği iş mantığı hataları burada yakalanır: yanlış sırayla yapılan bir hesap, eksik bir yetki kontrolü, ekonomik olarak istismar edilebilir bir teşvik.</li>
</ol>

<h2>Tipik açık sınıfları</h2>
<p>OWASP'ın 2025 tarihli Smart Contract Top 10 listesi erişim kontrolü açıklarını ilk sıraya koyar. Başlıca sınıflar şunlardır:</p>
<ul>
<li>Reentrancy: Sözleşme, kendi iç durumunu güncellemeden önce harici bir adrese çağrı yapar; çağrılan taraf aynı fonksiyona geri girerek, örneğin bakiye henüz düşülmeden, tekrar tekrar çekim yapar. Bilinen savunma, önce kontrol, sonra durum güncellemesi, en son harici çağrı sırasıdır (checks-effects-interactions). 2016'daki The DAO saldırısında 3,6 milyon ETH'yi aşan bir tutar sözleşmeden çekildi; Ethereum ağı buna 20 Temmuz 2016'da, 1.920.000 numaralı blokta yapılan hard fork ile yanıt verdi.</li>
<li>Erişim kontrolü: Yalnızca yöneticinin çağırması gereken bir fonksiyonun herkese açık kalması; basım (mint), duraklatma veya yükseltme yetkisinin tek bir anahtarda toplanması.</li>
<li>Oracle manipülasyonu: Fiyatı tek bir merkeziyetsiz borsa havuzundan anlık okuyan sözleşme, flash loan ile aynı işlem içinde bozulan fiyata göre borç verir veya tasfiye yapar.</li>
<li>Tam sayı taşması: Solidity 0.8.0'dan itibaren aritmetik işlemler taşma durumunda varsayılan olarak geri alınır (revert). Risk, <code>unchecked</code> blokları içinde ve eski derleyici sürümüyle yazılmış kodda sürer.</li>
</ul>

<h2>Rapor ne içerir, neyi içermez?</h2>
<p>İyi bir rapor incelenen commit hash'ini, kapsam dışı dosyaları, kullanılan yöntemleri ve her bulgu için önem derecesini, etkilenen kodu, istismar senaryosunu ve önerilen düzeltmeyi yazar. Bulguya proje ekibinin cevabı ve düzeltmenin yeniden incelenip incelenmediği de rapora girer.</p>
<p>Raporun sınırı da açıktır. ethereum.org'un güvenlik sayfası, audit'lerin her hatayı yakalamayacağını ve esas olarak ek bir inceleme turu işlevi gördüğünü söyler. Kapsam dışı bırakılan bir köprü sözleşmesi, zincir dışı bir anahtar yönetimi süreci veya denetimden sonra yapılan bir yükseltme rapora hiç girmemiştir. Rapor bir güvence belgesi olarak pazarlanıyorsa, sorun rapordan önce iletişimdedir.</p>

<div class="test"><b>Pratik test</b>Projenin web sitesinde "audited" rozeti var mı? Rozetin bağlandığı raporu açın ve iki şeyi karşılaştırın: raporda yazan commit hash'i ile zincir üzerinde doğrulanmış (verified) sözleşme kodunun kaynağı aynı mı? Aynı değilse rozet, bugün çalışan kod hakkında bir şey söylemiyor.</div>

<h2>Türk hukukunda karşılığı</h2>
<p>6362 sayılı Kanun kripto varlık hizmet sağlayıcılarını tanımlar (m.3/1-cc) ve kuruluş ile faaliyet için Kurul izni arar (m.35/B-1). Hizmet sağlayıcılar sistemlerinin güvenli yönetimi için gerekli önlemleri almak ve iç kontrol sistemlerini kurmakla yükümlüdür; izin için bilgi sistemleri ve teknolojik altyapı bakımından TÜBİTAK'ın belirleyeceği kriterlere uygunluk aranır (m.35/B-2).</p>
<p>Bilgi sistemleri bağımsız denetimi, Kurulun ilan ettiği listedeki bağımsız denetim kuruluşlarınca yapılır (m.99/B-2). Platformlar listeleme için yazılı bir prosedür kurmak zorundadır ve bu ilke ve esaslarda kripto varlıkların teknolojik özelliklerine ilişkin teknik kriterlere yer verilebilir (m.35/C-2). Aynı fıkra bir sınır da koyar: listelenmiş olmak kamuca tekeffül anlamına gelmez.</p>
<p>Sorumluluk hükmü en keskin olanıdır. Kripto varlık hizmet sağlayıcıları; bilişim sistemlerinin işletilmesinden, siber saldırı ve bilgi güvenliği ihlallerinden kaynaklanan kripto varlık kayıplarından <strong>6098 sayılı TBK m.71</strong> kapsamında, yani tehlike sorumluluğu esasına göre sorumludur (m.99/B-4). Bu nedenle bir platform için audit raporu, kusursuz sorumluluğa karşı bir kalkan değil, risk yönetiminin kaydıdır.</p>

<h2>KVKK: değiştirilemezlik ve silme hakkı</h2>
<p>KVKK m.7/1'e göre işlenmesini gerektiren sebepler ortadan kalkan kişisel veri resen veya ilgili kişinin talebi üzerine silinir, yok edilir ya da anonim hâle getirilir; ilgili kişi bunu m.11/1-e ile talep edebilir. Açık bir blokzincire yazılan veri ise pratikte silinemez. Veri sorumlusu, m.12/1 uyarınca verinin hukuka aykırı işlenmesini ve erişilmesini önleyecek teknik ve idari tedbirleri almak zorundadır.</p>
<p>"Endüstri 4.0'da Verinin Önemi ve Veri Koruma Bakımından Blokzincir Teknolojisine Özgü Yenilikler" başlıklı çalışmamda iki noktanın altını çizmiştim. Zincire yazmadan önce alınan açık rıza, silme talebinden feragat anlamına gelmez. Açık zincirlerde veri sorumlusunun kim olduğu da çoğu zaman belirsizdir. Audit açısından sonuç somuttur: kişisel veriyi zincir üzerinde, düz metin olarak veya kişiyle eşleştirilebilir biçimde tutan bir sözleşme, kodu kusursuz olsa bile hukuki bir bulgu taşır. Bu tasarım kararı kod yazılmadan önce verilmelidir.</p>
""",
},
]
