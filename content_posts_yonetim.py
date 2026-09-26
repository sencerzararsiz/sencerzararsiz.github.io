"""Yönetim, pazarlama ve inovasyon denemeleri.
Akademik atıflar Crossref/Europe PMC/PMC üzerinden, HBR makaleleri hbr.org'dan,
TÜİK ve Ticaret Bakanlığı verileri kurumların kendi yayınlarından,
6502 s. Kanun m.52 ve m.61 mevzuat.gov.tr metninden 26.09.2026 tarihinde doğrulanmıştır.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"

SRC_YON = {
    "danziger2011": ("Danziger, S., Levav, J., Avnaim-Pesso, L., Extraneous factors in judicial decisions, PNAS 108(17), 6889-6892, 2011", "https://doi.org/10.1073/pnas.1018033108"),
    "weinshall2011": ("Weinshall-Margel, K., Shapard, J., Overlooked factors in the analysis of parole decisions, PNAS 108(42), E833, 2011", "https://doi.org/10.1073/pnas.1110910108"),
    "danziger2011r": ("Danziger, S., Levav, J., Avnaim-Pesso, L., Reply to Weinshall-Margel and Shapard: Extraneous factors in judicial decisions persist, PNAS 108(42), E834, 2011", "https://doi.org/10.1073/pnas.1112190108"),
    "glockner2016": ("Glöckner, A., The irrational hungry judge effect revisited, Judgment and Decision Making 11(6), 601-610, 2016", "https://doi.org/10.1017/S1930297500004812"),
    "hagger2016": ("Hagger, M. S. ve diğerleri, A Multilab Preregistered Replication of the Ego-Depletion Effect, Perspectives on Psychological Science 11(4), 546-573, 2016", "https://doi.org/10.1177/1745691616652873"),
    "tuik2026": ("TÜİK, Hanehalkı Bilişim Teknolojileri (BT) Kullanım Araştırması, 2026 (Bülten sayı 58006, 05.08.2026)", "https://veriportali.tuik.gov.tr/tr/press/58006"),
    "etbis2025": ("T.C. Ticaret Bakanlığı, Türkiye'de E-Ticaretin Görünümü Raporu 2025", "https://ticaret.gov.tr/data/6a02f2c7269de183c0b98bc4/T%C3%BCrkiye%27de%20E-Ticaretin%20G%C3%B6r%C3%BCn%C3%BCm%C3%BC%20Raporu%202025.pdf"),
    "6502": ("6502 sayılı Tüketicinin Korunması Hakkında Kanun", M.format(6502, 1)),
    "rkinfluencer": ("Reklam Kurulu, Sosyal Medya Etkileyicileri Tarafından Yapılan Ticari Reklam ve Haksız Ticari Uygulamalar Hakkında Kılavuz (04.05.2021, İlke Kararı 2021/2)", "https://tuketici.ticaret.gov.tr/duyurular/sosyal-medya-etkileyicileri-tarafindan-yapilan-ticari-reklam-ve-haksiz-ticari-uyg"),
    "christensen1997": ("Christensen, C. M., The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail, Harvard Business School Press, 1997", "https://www.hbs.edu/faculty/Pages/item.aspx?num=46"),
    "hbr2015": ("Christensen, C. M., Raynor, M. E., McDonald, R., What Is Disruptive Innovation?, Harvard Business Review, Aralık 2015", "https://hbr.org/2015/12/what-is-disruptive-innovation"),
    "kim2023": ("Kim, W. C., Mauborgne, R., Innovation Doesn't Have to Be Disruptive, Harvard Business Review, Mayıs-Haziran 2023", "https://hbr.org/2023/05/innovation-doesnt-have-to-be-disruptive"),
}

POSTS_YON = [
# ---------------------------------------------------------------------------
{
"slug": "karar-yorgunlugu",
"cat": "Yönetim", "cat_en": "Management", "date": "2026-09-26",
"title": "Karar yorgunluğu: gün sonunda neden kötü karar veririz?",
"title_en": "Decision fatigue: why do we make worse decisions at the end of the day?",
"excerpt": "Aç hâkim çalışması karar yorgunluğunun en bilinen kanıtı. Eleştirileri ise daha az bilinir. İkisinden birlikte çıkan ders, kararı yorgunluktan çok karar ortamının biçimlendirdiği.",
"cover": 17,
"src": ["danziger2011", "weinshall2011", "danziger2011r", "glockner2016", "hagger2016"],
"body": """
<p>Gün sonunda bir taslağa "böyle kalsın" denen anları çoğumuz biliriz. Çoğu zaman taslak iyi olduğu için değil, itiraz edecek enerji kalmadığı için onay verilir. Karar yorgunluğu kavramı bu hissi adlandırıyor: art arda verilen kararlar sonrakilerin kalitesini düşürür, insan varsayılana, ertelemeye ya da en az zahmetli seçeneğe kayar. Sezgiye uygun bir fikir. Kanıtı ise sanıldığından tartışmalı.</p>

<h2>Aç hâkim çalışması</h2>
<p>Konunun en çok alıntılanan kanıtı Shai Danziger, Jonathan Levav ve Liora Avnaim-Pesso'nun 2011'de PNAS'ta yayımlanan "Extraneous factors in judicial decisions" makalesi (cilt 108, sayı 17, s. 6889-6892). Yazarlar İsrail'de dört büyük cezaevine bakan şartlı tahliye kurullarının 10 ay içindeki 50 günde verdiği 1.112 kararı inceledi. Her kurulda bir hâkim, bir kriminolog ve bir sosyal hizmet uzmanı vardı; kararları sekiz hâkim verdi. Hâkimlerin gün içindeki iki yemek molası günü üç karar oturumuna bölüyordu.</p>
<p>Bulgu çarpıcıydı. Lehe karar oranı her oturumun başında yaklaşık %65'ken oturum ilerledikçe sıfıra yakın bir düzeye iniyor, moladan sonra yeniden %65 civarına sıçrıyordu. Makale, "adalet hâkimin kahvaltıda ne yediğidir" karikatürünü test etmek için yazılmıştı. Popüler anlatıda kısa sürede "aç hâkim etkisi" adını aldı ve çoğu zaman eleştirileri anılmadan aktarıldı.</p>

<h2>Eleştiriler neyi gösteriyor?</h2>
<p>Aynı yıl PNAS'ta Keren Weinshall-Margel ve John Shapard'ın "Overlooked factors in the analysis of parole decisions" başlıklı yorumu çıktı (108(42), E833). Onlara göre dosyaların sırası rastgele değildi. Kurul bir cezaevinin dosyalarını bitirmeden molaya çıkmıyordu ve avukatı olmayan hükümlülerin dosyaları oturum sonlarına toplanıyordu. Aktardıkları verilere göre avukatsız hükümlülerde lehe karar oranı %15, avukatlılarda %35'ti. Avukatların güçlü dosyalarını öne alması da muhtemeldi. Düşüş yorgunluğu değil, sıralamayı yansıtıyor olabilirdi.</p>
<p>Danziger ve arkadaşları aynı sayıdaki cevaplarında (E834) avukatla temsil değişkenini modele ekledi ve dosya sırasıyla yemek molasının anlamlı kaldığını bildirdi. Tartışma orada bitmedi. Andreas Glöckner 2016'da Judgment and Decision Making dergisinde (cilt 11, sayı 6, s. 601-610) bir simülasyonla başka bir açıklama önerdi. Lehe kararlar ret kararlarından uzun sürüyorsa, moladan hemen önce uzun sürecek bir dosyaya başlamayan ve azıcık plan yapan rasyonel bir hâkim de benzer büyüklükte bir desen üretir. Glöckner'e göre etkinin büyüklüğü abartılmıştı.</p>
<p>Arka plandaki kuram da sarsıldı. Öz denetimin tükenen bir kaynak olduğunu savunan "ego tükenmesi" modeli, M. S. Hagger ve arkadaşlarının 23 laboratuvarda ve toplam 2.141 katılımcıyla yürüttüğü önceden kayıtlı replikasyonda sıfırdan ayırt edilemeyen bir etki verdi (d = 0,04; Perspectives on Psychological Science, 2016, 11(4), s. 546-573).</p>
<p>Buradan çıkardığım sonuç şu: "Yorgun beyin kötü karar verir" cümlesini bilimsel bir kesinlik gibi kullanmak doğru değil. Savunulabilir iddia daha mütevazı. Karar ortamının düzeni, sırası ve varsayılanları sonucu etkiler. Aç hâkim tartışmasının iki tarafı da bunu gösteriyor; açıklama yorgunluk da olsa dosya sırası da olsa, kararı dosyanın esası dışındaki bir yapı biçimlendiriyor.</p>

<h2>Hukukçu, kurucu ve ürün ekibi için</h2>
<p>Pratik sonuçlar yorgunluk kuramının doğru çıkmasına bağlı değil. Sıranın ve bağlamın önemli olduğunu kabul etmek yeterli.</p>
<ul>
<li>Varsayılanı bilinçli seçin. Şablondaki varsayılan hüküm ya da üründe önceden seçili değer, gün sonunda kimse itiraz etmediğinde geçerli olacak seçenektir. Onu, yorgun birinin kabul etmesinde sakınca olmayan seçenek yapın.</li>
<li>Kararları gruplayın, ama sırasını rastgele bırakmayın. Benzer kararları bir arada vermek bağlam değiştirme maliyetini azaltır. Aç hâkim tartışması ise grubun sonundaki dosyanın baştakiyle aynı muameleyi görmeyebileceğini hatırlatıyor.</li>
<li>Kontrol listesini dikkat dağıldığında da çalışacak biçimde yazın. Sözleşme incelemesinde sorumluluk sınırı, fesih bildirim süresi, yetkili mahkeme ve devir yasağı için dört satırlık bir liste, akşam yapılan incelemenin tabanını yükseltir.</li>
<li>Küçük kararları kurala bağlayın. Belirli bir tutarın altındaki araç aboneliklerini ekip liderinin onaylayacağını söyleyen tek bir kural, kurucuyu aynı kararı yüzlerce kez vermekten kurtarır.</li>
</ul>

<h2>Kullanıcının karar yükü</h2>
<p>Aynı mesele kullanıcı tarafında da var. Çerez banner'ı, abonelik ekranı ya da uzun bir kullanım koşulları metni kullanıcıdan art arda karar ister. Kullanıcı bu kararları çoğu zaman telefonda, başka bir işin ortasında verir. Metni okumadan "kabul et"e basması ilgisizlikten çok karar yükünün sonucu.</p>
<p><a href="/yazilar/legal-design-nedir/">Legal design</a> bu yükü azaltmaya çalışır: önce özet, sonra ayrıntı; bir ekranda tek karar; kullanıcı aleyhine kurulmamış varsayılanlar. Ürün geliştirirken fark ettiğim şey, iyi tasarlanmış bir hukuki metnin kullanıcıyı daha az yorduğu ve verilen onayın da bu yüzden daha anlamlı olduğu. Yorgun kullanıcıdan alınan onay kâğıt üzerinde bir onaydır. Güven üretmez.</p>

<div class="test"><b>Pratik test</b> Son bir haftada verdiğiniz beş kararı yazın ve her birinin yanına saatini not edin. Gün sonundakilerin kaçında varsayılanı kabul ettiniz ya da kararı ertelediniz? Sonra ürününüzde kullanıcıdan istediğiniz onayları sayın. Tek ekranda birden fazla karar isteyen bir yer varsa, ilk düzeltilecek yer orası.</div>
"""
},
# ---------------------------------------------------------------------------
{
"slug": "tuketim-aliskanliklari-degisiyor",
"cat": "Pazarlama", "cat_en": "Marketing", "date": "2026-09-26",
"title": "Tüketim alışkanlıkları değişirken hukuk ve pazarlama",
"title_en": "Law and marketing as consumer habits change",
"excerpt": "TÜİK'e göre internetten alışveriş yapanların oranı %60'a çıktı; Ticaret Bakanlığı verilerine göre hızlı ticaret e-ticaretin %8,5'ine ulaştı. Yeni kanallar yeni kural istemiyor; eski kuralların hızla uygulanmasını istiyor.",
"cover": 18,
"src": ["tuik2026", "etbis2025", "6502", "rkinfluencer"],
"body": """
<p>Tüketici davranışı sezgiye çok açık bir alan, o yüzden bu yazıda yalnız okuduğum resmî verileri kullanıyorum. TÜİK'in 5 Ağustos 2026'da yayımladığı Hanehalkı Bilişim Teknolojileri Kullanım Araştırması'na göre bireylerin internet üzerinden özel amaçla mal veya hizmet satın alma ya da sipariş verme oranı 2025'te %55,7 iken 2026'da %60,0 oldu. 16-74 yaş grubunda internet kullanımı %92,3.</p>
<p>Ticaret Bakanlığı'nın ETBİS verilerine dayanan "Türkiye'de E-Ticaretin Görünümü Raporu 2025" işin hacmini gösteriyor. 2025'te e-ticaret hacmi bir önceki yıla göre %52,2 artışla 4,57 trilyon TL'ye ulaştı. Bu nominal TL artışı. Aynı rapor dolar bazında artışı %28,9 olarak veriyor ve hacmi 115,43 milyar dolar olarak hesaplıyor. Enflasyonlu bir ekonomide bu ayrımı yapmadan büyüme konuşmak yanıltıcı olur.</p>

<h2>Hız artık bir beklenti</h2>
<p>Hızlı ticaret ayrı bir başlığı hak ediyor. Anında ve randevulu teslimatı kapsayan hızlı ticaret hacmi 2025'te %55,6 artışla 388,7 milyar TL'ye çıktı. E-ticaret içindeki payı 2019'da %1,6 iken 2025'te %8,5 oldu. Bu hacmin %69,5'i yemek, %30,5'i gıda ve süpermarket.</p>
<p>Kargoda da benzer bir tablo var. Rapora göre teslimatların %53,1'i 24-48 saat aralığında, %13,8'i ilk 24 saat içinde yapıldı. Tüketici için "yarın kapında" artık bir vaat değil, varsayılan beklenti. Pazarlama ekipleri bu beklentiyi reklama taşımak istiyor: "10 dakikada teslim", "aynı gün kargo".</p>
<p>Hukuk tam bu noktada devreye giriyor. 6502 sayılı Tüketicinin Korunması Hakkında Kanun m.61/6 uyarınca reklam veren, reklamındaki iddiaların doğruluğunu ispatla yükümlü. Teslim süresi de bir iddia. İspat, kampanyanın geçerli olduğu bölge ve saatler için yapılabilmeli; ortalama bir teslim süresi tek başına yetmeyebilir. İspat yükünü <a href="/yazilar/reklamda-kanitsiz-ustunluk-iddialari/">kanıtsız üstünlük iddiaları</a> yazısında ayrıca ele aldım.</p>

<h2>Satış artık akışta başlıyor</h2>
<p>Aynı raporda Bakanlığın e-ticaret işletmeleriyle yaptığı anketin sonuçları da yer alıyor. Ankete katılan işletmelerin %58,3'ü sosyal medya reklamı kullanıyor, %56'sı fotoğraf ve video içeriği üretiyor, %19,1'i sosyal medya etkileyicileriyle iş birliği yapıyor. %26,9'u sosyal medyayı hiç kullanmıyor. Bunlar tüketici değil işletme verisi. Yine de satışın nerede başladığına dair fikir veriyor.</p>
<p>Etkileyici üzerinden satışın hukuki çerçevesi belli. 6502 m.61/4 reklam olduğu açıkça belirtilmeden bir markanın tanıtıcı biçimde sunulmasını örtülü reklam sayar ve her türlü iletişim aracında yasaklar. Reklam Kurulu 4 Mayıs 2021 tarihli 2021/2 sayılı ilke kararıyla "Sosyal Medya Etkileyicileri Tarafından Yapılan Ticari Reklam ve Haksız Ticari Uygulamalar Hakkında Kılavuz"u kabul etti. Bakanlığın duyurusuna göre paylaşımın reklam olduğunu belirten ibare, tüketicinin ilk bakışta fark edebileceği biçimde sunulmalı.</p>
<p>Pazarlama tarafında gördüğüm hata çoğunlukla kötü niyetten kaynaklanmıyor. İçerik etkileyicinin doğal diline uysun diye reklam ibaresi arka plana itiliyor. Kılavuzun sorduğu soru ise tektir: tüketici bunun reklam olduğunu ilk bakışta anlıyor mu?</p>

<h2>Abonelik: çıkış, giriş kadar kolay olmalı</h2>
<p>Yazılımdan yemek kutusuna kadar pek çok ürün artık abonelikle satılıyor. Bu modelin Türkiye'deki payını gösteren, doğruladığım bir veri yok; kural ise net. 6502 m.52/4 uyarınca satıcı veya sağlayıcı, abonelik sözleşmesinin feshi için sözleşmenin kurulmasını sağlayan yöntemden daha ağır koşullar içeren bir yöntem belirleyemez. Uygulamada iki tıkla açılan bir aboneliğin iptalini çağrı merkezine bağlamak bu kuralla çelişir. m.52/3 ise belirli süreli aboneliklere sözleşmenin kendiliğinden uzayacağına dair hüküm konulmasını yasaklar. Uzatma ancak tüketicinin talebi ya da onayıyla mümkün.</p>

<h2>Verisine sahip çıkan tüketici</h2>
<p>Pazarlama ekipleriyle çalışırken en sık duyduğum soru, tüketicinin verisi konusunda ne kadar hassas olduğu. Bunu ölçen ve okuduğum güvenilir bir Türkiye verisi yok. Bu yüzden sayı vermiyorum. Çıkardığım pratik ders şu: izin kanal bazında alınır ve kanal bazında geri çekilebilir. Ticari elektronik ileti onayının nasıl yönetileceğini <a href="/yazilar/iys-kanal-bazli-onay-ve-ret/">İYS'de kanal bazlı onay ve ret</a> yazısında anlattım. SMS için verilmiş izni e-postaya taşıyan marka, müşterinin güvenini kısa yoldan kaybeder.</p>
<p>Tüketim alışkanlığı değiştikçe hukuk her seferinde yeni kural yazmıyor. Örtülü reklam yasağı gazetede habere gizlenmiş tanıtım için de, bir hikâye paylaşımı için de aynı maddeden işliyor. Değişen, ihlalin ne kadar hızlı yayıldığı.</p>

<div class="test"><b>Pratik test</b> Son kampanyanızdaki en güçlü vaadi seçin: teslim süresi, fiyat ya da "en çok satan" iddiası. Bu vaadi ispatlayacak belgeyi bugün bulabiliyor musunuz? Sonra abonelik iptal akışınızı bir müşteri gibi deneyin ve adımları sayın. İptal, abone olmaktan daha uzun sürüyorsa m.52/4 bakımından düzeltilecek yer orası.</div>
"""
},
# ---------------------------------------------------------------------------
{
"slug": "inovasyon-yikici-olmak-zorunda-degil",
"cat": "İnovasyon", "cat_en": "Innovation", "date": "2026-09-26",
"title": "İnovasyon yıkıcı olmak zorunda değil",
"title_en": "Innovation does not have to be disruptive",
"excerpt": "Christensen'in yıkıcı inovasyon tanımı çoğu sunumda kullanıldığından çok daha dar. Hukuk hizmetinde kalıcı değişikliklerin çoğu kimseyi yerinden etmiyor; işi görünür ve denetlenebilir kılıyor.",
"cover": 19,
"src": ["christensen1997", "hbr2015", "kim2023"],
"body": """
<p>Legaltech sunumlarında en sık duyduğum cümle "hukuku yıkıma uğratıyoruz". Ürün geliştiren biri olarak bu cümleye her seferinde biraz daha mesafeli bakıyorum. Hukuk hizmetinde kalıcı olduğunu gördüğüm değişikliklerin çoğu kimseyi yerinden etmedi. Mevcut işi daha anlaşılır ve daha denetlenebilir hâle getirdi.</p>

<h2>Christensen aslında ne dedi?</h2>
<p>"Yıkıcı inovasyon" kavramı Clayton M. Christensen'in 1997'de Harvard Business School Press'ten çıkan <em>The Innovator's Dilemma</em> kitabıyla yaygınlaştı. Kitabın sorusu, iyi yönetilen büyük şirketlerin yeni teknolojiler karşısında neden başarısız olduğuydu. Kavram o kadar geniş kullanıldı ki Christensen, Michael E. Raynor ve Rory McDonald, Harvard Business Review'un Aralık 2015 sayısındaki "What Is Disruptive Innovation?" makalesinde tanımı yeniden çizme gereği duydu.</p>
<p>Makaledeki tanım dar. Yıkım, daha az kaynağa sahip küçük bir şirketin yerleşik şirketlere başarıyla meydan okuduğu bir süreçtir. Yerleşik şirketler en talepkâr ve genellikle en kârlı müşterileri için ürünlerini iyileştirirken bazı segmentlerin ihtiyacını aşar, bazılarını görmezden gelir. Yeni giren şirket ya bu alt segmentte "yeterince iyi" bir ürünle ya da daha önce hiç tüketici olmamış bir kitleyi tüketiciye çevirerek tutunur. Ana akım müşteriler yeni ürünü yaygın biçimde benimsediğinde yıkım gerçekleşmiş olur.</p>
<p>Yazarlar Uber'in bu tanıma uymadığını söyler. Uber ne alt segmentten ne de tüketici olmayanlardan başladı; hizmeti taksiden kötü görülmedi, pek çok kullanıcıya göre daha iyiydi. Bu, Christensen'in "sürdürücü inovasyon" dediği şeye daha yakın: iyi bir ürünü mevcut müşterinin gözünde daha iyi yapmak. Makalenin altını çizdiği ayrıntı önemli. Sürdürücü iyileştirmeler küçük adımlar da olabilir, büyük sıçramalar da.</p>
<p>Demek ki "artımlı" ile "yıkıcı" aynı eksenin iki ucu değil. Bir yenilik çok büyük olup yine de sürdürücü kalabilir. Yıkıcılık bir büyüklük ölçüsü değil, pazara giriş biçimi.</p>

<h2>Yıkımsız yeni pazar</h2>
<p>W. Chan Kim ve Renée Mauborgne, HBR'nin Mayıs-Haziran 2023 sayısındaki "Innovation Doesn't Have to Be Disruptive" makalesinde tartışmayı bir adım öteye taşır. Onlara göre mevcut sektörleri ve işleri yok etmeden yeni pazar yaratmak mümkündür. Büyüme birinin kaybı pahasına gelmek zorunda değil. Bu fikir hukuk hizmeti için özellikle anlamlı, çünkü hukukta "yerinden edilen" taraf çoğu zaman avukat değil, hukuki bilgiye hiç ulaşamayan kullanıcı.</p>

<h2>Hukuk hizmetinde değişim nerede oluyor?</h2>
<p>Dışarıdan bakan biri hukuktaki inovasyonu yapay zekâ modellerinde arar. İçeriden baktığımda değişikliğin önemli bir kısmı daha sessiz yerlerde oluyor.</p>
<p>Süreç inovasyonu bunlardan ilki. Bir sözleşme onay akışını kimin neyi ne zaman onaylayacağını gösterecek şekilde yeniden çizmek yıkıcı değildir. Avukatın işini ortadan kaldırmaz; zamanını rutin takipten hukuki değerlendirmeye kaydırır. Christensen'in terimleriyle bu sürdürücü bir inovasyon ve bunda küçümsenecek bir şey yok.</p>
<p><a href="/yazilar/legal-design-nedir/">Legal design</a> ikinci alan. Bir aydınlatma metnini katmanlı hâle getirmek ya da bir sözleşme maddesini zaman çizelgesiyle göstermek hukuki içeriği değiştirmez, içeriğe erişimi değiştirir. Hukuki metni hiç okumayan kullanıcı, Christensen'in "tüketici olmayan" kitlesine benzer. Metin okunabilir hâle geldiğinde bu kişi ilk kez hukuki bilginin gerçek kullanıcısı olur.</p>
<p>Üçüncü alan <a href="/yazilar/legaltech-nedir/">legaltech</a> ürünleri ve burada iki yol birbirine karışıyor. Bazı ürünler avukatın mevcut işini hızlandırır. Bazıları ise daha önce avukata hiç danışmamış küçük bir işletmeye ilk uyum kontrolünü sunar. İkincisi yeni pazar tutunmasına benziyor, ama avukatı yerinden etmiyor. Çoğu zaman onu daha erken ve daha doğru bir soruyla karşılaştırıyor.</p>

<h2>Ürün masasından bakınca</h2>
<p>Legaltech ürünü geliştirirken fark ettiğim şey, "yıkıcı olma" hedefinin ekip içinde yanlış öncelikler ürettiği. Yıkıcı olmak isteyen ekip gösterişli özelliğe yönelir. Kullanıcının ihtiyacı çoğu zaman daha sıradan: hangi maddenin neden sorunlu olduğunu tek cümlede görmek ve düzeltmenin nereye yapılacağını bilmek. Bunu karşılayan ürün bir sektörü yıkmaz. Kullanıcısının bir gününü kolaylaştırır.</p>
<p>Hukukta bir sınır daha var. Hukuki bir çıktının arkasında sorumlu bir kişi olması gerekir. Bir aracın ürettiği metni kimin kontrol ettiği belirsizse, ürün ne kadar yeni olursa olsun kullanıcı ona güvenmez. Bu yüzden hukuk alanında sürdürücü inovasyonu bir taviz olarak değil, güvenin ön koşulu olarak görüyorum. Bence kalıcı olacak araç avukatı devre dışı bırakan değil, avukatın kontrolünü görünür kılan araç.</p>

<div class="test"><b>Pratik test</b> Üzerinde çalıştığınız yeniliği tek cümleyle tarif edin ve iki soru sorun. Bu yenilik mevcut müşterinize daha iyi bir ürün mü sunuyor, yoksa daha önce hiç müşteri olmamış birini müşteriye mi çeviriyor? İkisi de değilse sunumdan "yıkıcı" kelimesini çıkarın ve yerine ürünün kimin hangi işini kolaylaştırdığını yazın.</div>
"""
},
]
