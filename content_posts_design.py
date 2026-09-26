"""Legaltech, legal design ve sözleşme tasarımı yazıları.
Mevzuat atıfları mevzuat.gov.tr metinlerinden 26.09.2026 tarihinde doğrulanmıştır.
Sözleşme tasarımı yazısındaki madde metni tamamen kurgusaldır.
"""

M = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo={}&MevzuatTur={}&MevzuatTertip=5"

SRC_EXTRA = {
    "6098": ("6098 sayılı Türk Borçlar Kanunu", M.format(6098, 1)),
    "6102": ("6102 sayılı Türk Ticaret Kanunu", M.format(6102, 1)),
    "hagan": ("Stanford Law School, Margaret Hagan profil sayfası", "https://law.stanford.edu/margaret-hagan/"),
}

CLAUSE_LEGAL = """<p><strong>Madde 6. Teslim, kabul ve gecikme.</strong> 6.1. Yüklenici, işbu Sözleşme'nin imza tarihinden itibaren doksan (90) takvim günü içinde, Ek-1'de tanımlanan yazılımı İş Sahibi'nin test ortamına kurulu ve çalışır hâlde teslim etmeyi kabul ve taahhüt eder. 6.2. İş Sahibi, teslimden itibaren on (10) iş günü içinde kabul testlerini tamamlayarak sonucu Yüklenici'ye yazılı olarak bildirir; bu süre içinde bildirimde bulunulmaması hâlinde yazılım kabul edilmiş sayılır. 6.3. Teslimin Yüklenici'ye atfedilebilen bir sebeple gecikmesi hâlinde Yüklenici, geciken her takvim günü için sözleşme bedelinin binde biri (%0,1) oranında cezai şart ödemekle yükümlü olup cezai şartın toplam tutarı sözleşme bedelinin yüzde onunu (%10) aşamaz. 6.4. Mücbir sebep hâllerinde teslim süresi, mücbir sebebin devam ettiği süre kadar uzar; ancak bu hükümden yararlanmak isteyen taraf, mücbir sebebin ortaya çıkmasından itibaren beş (5) iş günü içinde diğer tarafa yazılı bildirimde bulunmakla yükümlüdür.</p>"""

CLAUSE_DESIGN = """<div class="cd">
  <p class="cd-sum"><b>Bu madde ne diyor?</b> Yazılım 90 gün içinde teslim edilir, İş Sahibi 10 iş günü içinde test edip cevap verir. Geç teslimde günlük ceza işler ama toplamı %10'u geçemez.</p>
  <div class="cd-parties">
    <div><span class="cd-role">Yüklenici</span><span>Yazılımı test ortamında çalışır hâlde teslim eder.</span></div>
    <div><span class="cd-role cd-role-b">İş Sahibi</span><span>Kabul testini yapar, sonucu yazılı bildirir.</span></div>
  </div>
  <ol class="cd-time" aria-label="Zaman çizelgesi">
    <li><b>İmza</b><span>Süre başlar</span></li>
    <li><b>90 takvim günü</b><span>Geliştirme</span></li>
    <li><b>Teslim</b><span>Test ortamında</span></li>
    <li><b>10 iş günü</b><span>Kabul testi</span></li>
    <li><b>Kabul</b><span>Ya da yazılı ret</span></li>
  </ol>
  <div class="cd-nums">
    <div><b>%0,1</b><span>Geciken her gün için ceza</span></div>
    <div><b>%10</b><span>Cezanın üst sınırı</span></div>
    <div><b>5 iş günü</b><span>Mücbir sebep bildirimi</span></div>
  </div>
  <ul class="cd-if">
    <li><span>Teslim geç kalırsa</span><i aria-hidden="true">→</i><span>Günlük %0,1 ceza, toplamı en fazla %10</span></li>
    <li><span>İş Sahibi 10 iş günü susarsa</span><i aria-hidden="true">→</i><span>Yazılım kabul edilmiş sayılır</span></li>
    <li><span>Mücbir sebep çıkarsa</span><i aria-hidden="true">→</i><span>5 iş günü içinde yazılı bildirim; süre uzar</span></li>
  </ul>
</div>"""

NEW_POSTS = [
# ---------------------------------------------------------------------------
{
"slug": "legaltech-nedir",
"cat": "Legaltech", "cat_en": "Legaltech", "date": "2026-09-26",
"title": "Legaltech nedir? Hukuka yazılım eklemekten fazlası",
"title_en": "What is legaltech? More than adding software to law",
"excerpt": "Legaltech tek bir ürün türü değil. Belge otomasyonu, sözleşme yönetimi, uyum taraması ve yapay zekâ destekli analiz ayrı katmanlardır; her birinin hukuki riski de ayrıdır.",
"cover": 9,
"src": ["6698"],
"body": """
<p>Legaltech, hukuki hizmetin nasıl üretildiğini ve nasıl sunulduğunu değiştiren teknolojilerin ortak adıdır. Terim çoğu zaman "hukuka yazılım eklemek" diye anlaşılır. Bu tanım eksik kalır. Aynı çatı altında birbirinden çok farklı işler yapan dört katman vardır.</p>

<h2>Dört katman</h2>
<ul>
<li><strong>Belge ve süreç otomasyonu.</strong> Şablondan sözleşme, dilekçe veya aydınlatma metni üretmek. İşin özü koşullu mantıktır: "tüketiciye satış varsa şu madde, yurt dışına aktarım varsa şu paragraf."</li>
<li><strong>Sözleşme yaşam döngüsü yönetimi (CLM).</strong> Taslak, müzakere, onay, imza, yükümlülük takibi ve yenileme tek akışta izlenir. Sözleşme bir dosya olmaktan çıkar, tarihleri ve sorumluları olan bir kayda dönüşür.</li>
<li><strong>Uyum taraması ve izleme.</strong> Bir web sitesini, reklamı veya formu mevzuata göre tarayıp eksikleri bulmak. Regtech ile sınırı burada incelir.</li>
<li><strong>Yapay zekâ destekli analiz.</strong> Uzun bir sözleşmeyi özetlemek, maddeleri sınıflandırmak, riskli ifadeleri işaretlemek.</li>
</ul>
<p>Dördünü tek kelimeyle anmak, bir sözleşme şablonu ile bir dil modelini aynı risk sepetine koymak demektir. Oysa ilkinin hatası öngörülebilirdir, sonuncusununki değil.</p>

<h2>Ürünün içinden: kural mı, model mi?</h2>
<p>Legaltech ürünlerinin hukuki tarafında en sık tartışılan soru şudur: bir bulgu hangi katmandan gelmeli? Bir web sitesinde çerez politikası bağlantısı var mı, reddet düğmesi ilk ekranda mı, sözleşmede cayma süresi yazıyor mu? Bu sorular kurala dönüştürülebilir. Kural, avukatın yazdığı ve her seferinde aynı sonucu veren bir kontroldür.</p>
<p>Yapay zekâ ise kuralın yetmediği yerde devreye girer: bir reklam cümlesinin yanıltıcı olup olmadığını yorumlamak, bir oyun mağaza sayfasındaki beyanları okumak. Burada tek bir çizgim var. <strong>Kaynağı gösterilmeyen bulgu, bulgu değildir.</strong> Model bir madde numarası öneriyorsa o madde birincil kaynaktan kontrol edilmeden kullanıcıya gösterilmemelidir.</p>

<div class="test"><b>Pratik test</b>Kullandığınız legaltech aracı size bir risk gösterdiğinde, hangi mevzuat hükmüne dayandığını tek tıkla açabiliyor musunuz? Açamıyorsanız elinizdeki şey bir görüş değil, bir tahmindir.</div>

<h2>Legaltech de mevzuata tabidir</h2>
<p>Hukuki uyumu denetleyen bir ürün, kendi uyumunu da taşımak zorundadır. Kullanıcının yüklediği sözleşme kişisel veri içeriyorsa ürünü sunan taraf, verinin hukuka aykırı işlenmesini ve erişilmesini önlemek için gerekli teknik ve idari tedbirleri almakla yükümlüdür (6698 s. KVKK m.12/1). Veriyi kendi adına işleyen bir hizmet sağlayıcıyla, ör. bir bulut ya da yapay zekâ sağlayıcısıyla çalışıyorsa bu tedbirlerden onunla birlikte sorumludur (m.12/2).</p>
<p>Sağlayıcı yurt dışındaysa bir adım daha vardır: aktarım, 7499 sayılı Kanun'la 2024'te değişen KVKK m.9'daki yeterlilik kararı, uygun güvence veya arızi aktarım şartlarından birine dayanmalıdır. Bir yapay zekâ servisine gönderilen her sözleşme, bu sorunun cevabını ister.</p>

<h2>Avukatın yerini alır mı?</h2>
<p>Hayır; ama iş bölümünü değiştirir. Tekrar eden kontrol makineye geçer, yorum ve sorumluluk avukatta kalır. Legaltech'in değeri, avukatın zamanını tarama işinden alıp karar gerektiren işe vermesindedir. Bunun için kuralları yazan ekipte hem hukuku hem ürünün nasıl çalıştığını bilen biri bulunmalıdır.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "legal-design-nedir",
"cat": "Legal design", "cat_en": "Legal design", "date": "2026-09-26",
"title": "Legal design nedir? Hukuki metni okunur ve uygulanır kılmak",
"title_en": "What is legal design? Making legal text readable and usable",
"excerpt": "Legal design bir süsleme işi değil. Sade dil, bilgi hiyerarşisi, görselleştirme ve kullanıcı testiyle hukuki doğruluğu koruyarak metni işler hâle getirir.",
"cover": 10,
"src": ["tebligaydin", "6698", "hagan"],
"body": """
<p>Legal design, tasarım yöntemlerini hukuki metinlere, belgelere ve süreçlere uygulamaktır. Soru şudur: bu metni okuyan kişi, ne yapması gerektiğini anlıyor mu? Yaklaşım, Stanford Hukuk Fakültesi'ndeki Legal Design Lab'i yöneten Margaret Hagan'ın akademik çalışmalarıyla yaygınlaştı; bugün sözleşmelerden mahkeme formlarına kadar geniş bir alanda uygulanıyor.</p>

<h2>Süsleme değil, yükümlülük</h2>
<p>Legal design çoğu zaman "metni güzelleştirmek" sanılır. Türk hukukunda bazı metinler için okunurluk bir tercih değil, şarttır. Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ, ilgili kişiye yapılacak bildirimin <strong>anlaşılır, açık ve sade bir dil</strong> kullanılarak yapılmasını ister (m.5/1-ğ). Aynı Tebliğ genel nitelikte ve muğlak ifadeleri de yasaklar (m.5/1-g). Okunamayan bir aydınlatma metni, eksik yerine getirilmiş bir yükümlülüktür.</p>

<h2>Dört araç</h2>
<h3>1. Sade dil</h3>
<p>Uzun cümle bölünür, edilgen çatı etkene çevrilir, "işbu", "mezkûr" gibi kelimeler yerini gündelik karşılıklarına bırakır. Hukuki terim gerekiyorsa kalır, ama ilk geçtiği yerde açıklanır. Sade dil, hukuki sonucu değiştirmez; sadece sonucu görünür kılar.</p>
<h3>2. Bilgi hiyerarşisi</h3>
<p>Okuyucu en çok neyi bilmeli? O en üste çıkar. Katmanlı aydınlatma bunun tipik örneğidir: kısa bir üst katman temel soruları cevaplar, ayrıntı alt katmanda durur.</p>
<h3>3. Görselleştirme</h3>
<p>Süreler zaman çizelgesine, koşullar akış şemasına, taraflar rol kartlarına dönüşür. Amaç görsel eklemek değil, metnin içinde gömülü duran yapıyı çıkarmaktır. <a href="/yazilar/sozlesme-tasarimi-bes-yol/">Sözleşme tasarımı yazısında</a> bunun etkileşimli bir örneği var.</p>
<h3>4. Kullanıcı testi</h3>
<p>Metni, hedef kitleden beş kişiye okutun ve üç soru sorun: Ne kabul ettiniz? Ne zamana kadar? Vazgeçmek isterseniz ne yaparsınız? Cevaplar farklıysa metin çalışmıyor demektir.</p>

<div class="test"><b>Pratik test</b>Ana sayfadaki <a href="/#legal-design">"Hukukça / Sade dil"</a> örneğinde aynı paragrafın iki hâli var. 69 kelimelik tek cümle ile beş satırlık tablo aynı hukuki sebebi anlatıyor. Şimdi kendi metninizden bir paragraf seçin: aynı bilgiyi beş satırlık bir tabloya sığdırabiliyor musunuz? Sığmıyorsa paragraf bir değil, birden fazla şey söylüyordur.</div>

<h2>Ne değildir?</h2>
<ul>
<li>Hukuki doğruluktan ödün vermek değildir. Sadeleşen cümle, aslıyla aynı hükmü taşımalıdır.</li>
<li>Özet koyup asıl metni saklamak değildir. Özet ile madde metni birlikte kullanılıyorsa, çelişki hâlinde hangisinin esas alınacağı metinde yazmalıdır.</li>
<li>Bir kez yapılıp biten iş değildir. Mevzuat ve ürün değiştikçe metin ve tasarım birlikte güncellenir.</li>
</ul>
<p>İyi tasarlanmış bir hukuki metin, avukat okuduğunda eksiksiz, kullanıcı okuduğunda anlaşılır olandır. İkisinden biri eksikse iş bitmemiştir.</p>
""",
},
# ---------------------------------------------------------------------------
{
"slug": "sozlesme-tasarimi-bes-yol",
"cat": "Legal design", "cat_en": "Legal design", "date": "2026-09-26",
"title": "Sözleşme tasarımı: uzun bir maddeyi okunur kılmanın beş yolu",
"title_en": "Contract design: five ways to make a long clause readable",
"excerpt": "Kurgusal bir teslim ve gecikme maddesi üzerinden etkileşimli bir örnek: özet, rol kartları, öne çıkan rakamlar, zaman çizelgesi ve koşul akışı.",
"cover": 11,
"src": ["6098", "6102"],
"body": f"""
<p>Bir sözleşme maddesi hukuken eksiksiz olabilir ve yine de okunamaz. Aşağıdaki madde, bir yazılım geliştirme sözleşmesinden alınmış gibi görünüyor ama <strong>tamamen kurgusaldır</strong>. Düğmeyle madde metni ile tasarlanmış hâli arasında geçiş yapın; ardından her tekniği tek tek açıyorum.</p>

<div class="ld-demo">
  <div class="seg" data-ld data-mode="legal" role="group" aria-label="Görünüm">
    <span class="pill" aria-hidden="true"></span>
    <button type="button" data-mode="legal" aria-pressed="true">Madde metni</button>
    <button type="button" data-mode="plain" aria-pressed="false">Tasarlanmış hâli</button>
  </div>
  <div class="ld-stage" aria-live="polite">
    <div class="ld-pane ld-legal">{CLAUSE_LEGAL}<div class="meter"><span>4 fıkra</span><span>{{words}} kelime</span><span>5 ayrı süre ve oran</span></div></div>
    <div class="ld-pane ld-plain" hidden>{CLAUSE_DESIGN}</div>
  </div>
</div>

<h2>1. Önce sonuç</h2>
<p>Okuyucunun ilk sorusu "bu madde bana ne yükletiyor?" sorusudur. Tasarlanmış hâlin en üstündeki iki cümlelik özet bu soruyu cevaplar. Özet sözleşmenin parçası yapılacaksa, madde metniyle çelişmesi hâlinde hangisinin esas alınacağı açıkça yazılmalıdır.</p>

<h2>2. Tarafları görünür kılmak</h2>
<p>Madde metninde "Yüklenici" ve "İş Sahibi" dört fıkraya dağılmış hâlde. Rol kartları her tarafın tek bir işini gösterir: biri teslim eder, diğeri test eder. Kim ne yapıyor sorusu, metni baştan okumadan cevaplanır.</p>

<h2>3. Rakamları öne çıkarmak</h2>
<p>Bu kısa maddede beş ayrı süre ve oran var: 90 takvim günü, 10 iş günü, %0,1, %10 ve 5 iş günü. Metin içinde gömülü dururken hepsi aynı ağırlıkta görünür. Ayrı kutularda durduklarında hangisinin ceza, hangisinin süre olduğu ilk bakışta anlaşılır.</p>
<p>Ceza koşulunun üst sınırını görünür kılmanın hukuki bir anlamı da var. Taraflar cezanın miktarını serbestçe belirler, ama hâkim aşırı gördüğü ceza koşulunu kendiliğinden indirir (6098 s. TBK m.182). Borçlu tacir ise bu indirimi mahkemeden isteyemez (6102 s. TTK m.22/1). Tacir bir yüklenici için %10 sınırı, pratikte ödeyebileceği en yüksek tutardır.</p>

<h2>4. Zamanı çizmek</h2>
<p>Zaman çizelgesi, metinde kaybolan bir ayrımı ortaya çıkarır: teslim süresi <strong>takvim günüyle</strong>, kabul testi ve mücbir sebep bildirimi <strong>iş günüyle</strong> sayılıyor. Aynı sözleşmede iki farklı gün hesabı en sık uyuşmazlık kaynaklarından biridir. Çizelgede yan yana durduklarında fark gözden kaçmaz.</p>

<h2>5. Koşulu akışa çevirmek</h2>
<p>"Eğer şu olursa, şu sonuç doğar" kalıbı madde metninde uzun bir yan cümleye gizlenir. Akışa çevrildiğinde en önemli tuzak görünür olur: İş Sahibi 10 iş günü içinde cevap vermezse yazılım kabul edilmiş sayılıyor. Sessizlik burada bir irade beyanı gibi sonuç doğuruyor. Bunu bilen İş Sahibi, test takvimini imzadan önce planlar.</p>

<div class="test"><b>Pratik test</b>Kendi sözleşmenizden bir madde seçin ve içindeki bütün süre, oran ve tutarları bir listeye yazın. Liste beşi geçiyorsa o madde, tasarımdan en çok fayda görecek maddedir.</div>

<h2>Tasarım hukuku değiştirmez</h2>
<p>Bu beş teknik maddenin içeriğine tek kelime eklemedi, tek kelime çıkarmadı. Değişen tek şey, okuyucunun o içeriğe ulaşma süresi. İyi bir sözleşme tasarımı, imzalayan kişinin neyi kabul ettiğini imzadan önce görmesini sağlar.</p>
""",
},
]
