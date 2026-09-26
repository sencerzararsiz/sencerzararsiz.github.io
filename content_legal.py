"""Hukuki sayfalar. Metinler birincil kaynaklardan doğrulanan atıflarla yazılmıştır:
6698 s. KVKK (mevzuat.gov.tr, 1.5.6698), Aydınlatma Tebliği (24454), Başvuru Tebliği (24455),
KVKK Çerez Uygulamaları Hakkında Rehber (Temmuz 2025), 1136 s. Avukatlık Kanunu m.55,
TBB Reklam Yasağı Yönetmeliği m.7 (RG 9/8/2024-32627 değişikliğiyle).
Türkçe metin esastır; İngilizce sürüm bilgilendirme amaçlı çeviridir.
"""

UPDATED = {"tr": "26 Eylül 2026", "en": "26 September 2026"}
EMAIL = "avahmetsencerzararsiz@gmail.com"

# --------------------------------------------------------------------------- KVKK
KVKK_TR = f"""
<div class="test"><b>Kısaca</b>Bu site çerez, analitik aracı ya da form kullanmaz ve ziyaretçi verisi toplamaz. Kişisel veriniz yalnızca bana e-posta gönderirseniz işlenir.</div>

<h2 id="veri-sorumlusu">1. Veri sorumlusu</h2>
<p>Bu metin 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) m.10 uyarınca hazırlanmıştır. Veri sorumlusu <strong>Ahmet Sencer Zararsız</strong>'dır. İletişim: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="e-posta">2. Bana e-posta gönderdiğinizde</h2>
<p>Adınızı, e-posta adresinizi ve mesajınızda paylaştığınız bilgileri yalnızca mesajınızı yanıtlamak için kullanırım. Hukuki sebep meşru menfaattir (KVKK m.5/2-f). Veriler, e-posta yoluyla elektronik ortamda toplanır ve e-posta hizmet sağlayıcısının altyapısında saklanır. Pazarlama amacıyla kimseyle paylaşılmaz. Yazışma, konu sonuçlandıktan sonra 2 yıl içinde silinir.</p>
<p>Mesajınıza sağlık bilgisi gibi özel nitelikli kişisel veri (KVKK m.6) eklememenizi rica ederim.</p>

<h2 id="site-ziyareti">3. Siteyi ziyaret ettiğinizde</h2>
<p>Sayfalar çerez yazmaz, analitik ya da reklam aracı yüklemez, başka bir sunucudan kaynak çekmez. Site GitHub Pages üzerinde barındırılır; barındırma hizmetinin sunucu kayıtları <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener" target="_blank">GitHub Gizlilik Bildirimi</a>'ne tabidir. Tarayıcınıza yazılabilecek iki küçük tercih kaydı <a href="/cerez-politikasi/">Çerez Politikası</a>'nda açıklanmıştır.</p>

<h2 id="haklariniz">4. Haklarınız</h2>
<p>KVKK m.11 uyarınca verinizin işlenip işlenmediğini öğrenme, bilgi isteme, düzeltme, silme ve itiraz haklarına sahipsiniz. Talebinizi <a href="mailto:{EMAIL}">{EMAIL}</a> adresine iletebilirsiniz; en geç 30 gün içinde ücretsiz sonuçlandırırım (KVKK m.13/2).</p>
"""

KVKK_EN = f"""
<p class="note">This is a courtesy translation. The Turkish version is the binding text.</p>
<div class="test"><b>In short</b>This site uses no cookies, analytics or forms and collects no visitor data. Your personal data is processed only if you e-mail me.</div>

<h2 id="controller">1. Data controller</h2>
<p>This notice is given under Article 10 of Türkiye's Personal Data Protection Law No. 6698 (KVKK). The data controller is <strong>Ahmet Sencer Zararsız</strong>. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="email">2. If you e-mail me</h2>
<p>I use your name, e-mail address and anything you share in your message only to reply to you. The legal basis is legitimate interest (KVKK Art. 5(2)(f)). Data is collected electronically by e-mail and stored on the e-mail service provider's infrastructure. It is not shared with anyone for marketing. Correspondence is deleted within 2 years after the matter is closed.</p>
<p>Please do not include special categories of personal data, such as health data (KVKK Art. 6).</p>

<h2 id="visits">3. When you visit the site</h2>
<p>Pages set no cookies, load no analytics or advertising tools and fetch nothing from other servers. The site is hosted on GitHub Pages; the hosting provider's server logs are governed by the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener" target="_blank">GitHub Privacy Statement</a>. The two small preference entries that may be written to your browser are explained in the <a href="/en/cookies/">Cookie Policy</a>.</p>

<h2 id="rights">4. Your rights</h2>
<p>Under KVKK Art. 11 you have the right to learn whether your data is processed, request information, and request rectification, erasure or object. Send your request to <a href="mailto:{EMAIL}">{EMAIL}</a>; I will resolve it free of charge within 30 days (KVKK Art. 13(2)).</p>
"""

# --------------------------------------------------------------------------- Çerez
def _storage_table(lang):
    if lang == "tr":
        return """<div class="table-wrap"><table>
<caption>Tarayıcınızın yerel depolamasına yazılabilecek kayıtlar</caption>
<thead><tr><th scope="col">Anahtar</th><th scope="col">Tür</th><th scope="col">Ne işe yarar</th><th scope="col">Ne zaman yazılır</th><th scope="col">Süre</th></tr></thead>
<tbody>
<tr><td><code>sz-consent</code></td><td>Zorunlu</td><td>Çerez panelindeki seçiminizi hatırlar; panel her sayfada yeniden açılmaz.</td><td>Panelde bir seçim yaptığınızda</td><td>12 ay; sonra panel yeniden sorulur</td></tr>
<tr><td><code>sz-theme</code></td><td>Tercih</td><td>Açık veya koyu tema seçiminizi hatırlar.</td><td>Yalnızca tercih depolamasına izin verdiyseniz ve tema düğmesine bastığınızda</td><td>İzni geri alana kadar, en fazla 12 ay</td></tr>
</tbody></table></div>"""
    return """<div class="table-wrap"><table>
<caption>Entries that may be written to your browser's local storage</caption>
<thead><tr><th scope="col">Key</th><th scope="col">Type</th><th scope="col">Purpose</th><th scope="col">When written</th><th scope="col">Duration</th></tr></thead>
<tbody>
<tr><td><code>sz-consent</code></td><td>Necessary</td><td>Remembers your choice in the cookie panel, so it doesn't reappear on every page.</td><td>When you make a choice in the panel</td><td>12 months, then you're asked again</td></tr>
<tr><td><code>sz-theme</code></td><td>Preference</td><td>Remembers your light or dark theme choice.</td><td>Only if you allowed preference storage and pressed the theme button</td><td>Until you withdraw consent, at most 12 months</td></tr>
</tbody></table></div>"""


COOKIES_TR = f"""
<div class="test"><b>Kısaca</b>Bu site çerez kullanmaz. Analitik, reklam ya da takip aracı yoktur. Tarayıcınıza yalnızca seçiminizi ve izin verirseniz tema tercihinizi yazar.</div>

<h2 id="kullanmadiklarim">1. Neyi kullanmıyorum?</h2>
<p>Sitede HTTP çerezi, analitik (ör. Google Analytics), reklam pikseli, sosyal medya eklentisi veya harici yazı tipi servisi yoktur. Yazı tipleri dahil tüm dosyalar sitenin kendi sunucusundan yüklenir. Sayfaları görüntülediğinizde tarayıcınız başka bir alan adına istek göndermez.</p>

<h2 id="yerel-depolama">2. Yerel depolamaya ne yazılır?</h2>
{_storage_table("tr")}
<p>Bu kayıtlar cihazınızda kalır; bana veya üçüncü kişilere iletilmez. Tercih depolamasına izin vermezseniz tema düğmesi yine çalışır, ancak seçiminiz yalnızca açık olan sayfada geçerli olur.</p>

<h2 id="dayanak">3. Neden izin istiyorum?</h2>
<p>KVKK'nın Çerez Uygulamaları Hakkında Rehberi (Temmuz 2025) çerezleri ele alır; yerel depolama gibi benzer teknolojiler için ayrı bir yönlendirme içermediğini açıkça belirtir. Rehber, gizlilik tercihlerinin hatırlanmasını zorunlu çerezlere örnek gösterir. Kullanıcının bir düğmeye basarak açıkça talep ettiği dil tercihi çerezinin oturum süreli olanını da açık rıza gerektirmeyen çerezler arasında sayar.</p>
<p>Tema tercihi bu örneğe benzer. Yine de ihtiyatlı davranıyorum: <code>sz-theme</code> kaydını yalnızca izin verirseniz yazıyorum.</p>

<h2 id="panel">4. Panel nasıl çalışır?</h2>
<ul>
<li><strong>Reddet</strong>, <strong>Tercihler</strong> ve <strong>Kabul et</strong> düğmeleri aynı boyut ve görünürlüktedir.</li>
<li>Tercih seçeneği kapalı başlar; önceden işaretli kutu yoktur.</li>
<li>Paneli kapatmadan siteyi kullanabilirsiniz; içerik hiçbir koşulda kilitlenmez.</li>
<li>Seçiminizi her sayfanın altındaki <strong>Çerez tercihleri</strong> bağlantısından istediğiniz an değiştirebilirsiniz. Reddettiğinizde <code>sz-theme</code> kaydı hemen silinir.</li>
</ul>

<h2 id="silme">5. Kayıtları kendiniz silmek</h2>
<p>Tarayıcınızın ayarlarından bu site için "site verilerini temizle" seçeneğini kullanarak iki kaydı da silebilirsiniz. Kişisel verilerinize ilişkin ayrıntılar <a href="/kvkk-aydinlatma-metni/">KVKK Aydınlatma Metni</a>'ndedir.</p>
"""

COOKIES_EN = f"""
<p class="note">This is a courtesy translation. The Turkish version is the binding text.</p>
<div class="test"><b>In short</b>This site uses no cookies and no analytics, advertising or tracking tools. It writes only your choice to your browser and, if you allow it, your theme preference.</div>

<h2 id="not-used">1. What I don't use</h2>
<p>There are no HTTP cookies, no analytics (e.g. Google Analytics), no ad pixels, no social media plug-ins and no external font services. Every file, fonts included, is served from the site itself. Viewing a page sends no request to any other domain.</p>

<h2 id="local-storage">2. What is written to local storage</h2>
{_storage_table("en")}
<p>These entries stay on your device and are never sent to me or anyone else. If you don't allow preference storage, the theme button still works, but only for the page you're on.</p>

<h2 id="why">3. Why I ask</h2>
<p>The Personal Data Protection Authority's Guidelines on Cookie Practices (July 2025) cover cookies and state that they give no guidance on similar technologies such as local storage. They list remembering privacy choices as an example of a strictly necessary cookie, and treat a session-length language-choice cookie that the user explicitly requests by pressing a button as not requiring explicit consent.</p>
<p>A theme choice is similar. I still take the cautious route and write <code>sz-theme</code> only if you allow it.</p>

<h2 id="panel">4. How the panel works</h2>
<ul>
<li><strong>Reject</strong>, <strong>Preferences</strong> and <strong>Accept</strong> have equal size and prominence.</li>
<li>The preference option starts switched off; nothing is pre-ticked.</li>
<li>You can use the site without closing the panel; content is never locked.</li>
<li>Change your choice at any time via <strong>Cookie preferences</strong> at the bottom of every page. Rejecting deletes <code>sz-theme</code> immediately.</li>
</ul>

<h2 id="clear">5. Clearing entries yourself</h2>
<p>Use your browser's "clear site data" option for this site to remove both entries. For personal data, see the <a href="/en/privacy/">Privacy Notice</a>.</p>
"""

# --------------------------------------------------------------------------- Kullanım
TERMS_TR = """
<h2 id="nitelik">1. Sitenin niteliği</h2>
<p>Bu site, Ahmet Sencer Zararsız'ın kişisel ve mesleki özgeçmişini, yayımladığı yazıları ve çalışmalarını tanıtan bir profil sayfasıdır. Hukuki danışmanlık teklifi içermez, iş elde etme amacı taşımaz.</p>

<h2 id="hukuki-gorus">2. Yazılar hukuki görüş değildir</h2>
<p>Yazılar genel bilgi verir ve yayım tarihindeki mevzuata göre hazırlanır; mevzuat sonradan değişebilir. Somut bir olaya uygulanmadan önce güncel mevzuat ve olayın kendine özgü koşulları ayrıca değerlendirilmelidir. Siteyi ziyaret etmek, yazıları okumak ya da e-posta göndermek avukat-müvekkil ilişkisi kurmaz.</p>

<h2 id="fikri-mulkiyet">3. Fikrî haklar</h2>
<p>Metinler, tasarım ve animasyon kodu Ahmet Sencer Zararsız'a aittir. Yazılardan kaynak gösterilerek ve bağlantı verilerek kısa alıntı yapabilirsiniz; metnin tamamını izinsiz çoğaltamaz veya yayımlayamazsınız. Yazı tipleri SIL Open Font License kapsamında kullanılmaktadır.</p>

<h2 id="baglantilar">4. Dış bağlantılar</h2>
<p>Site, LinkedIn, GameLaw.io gibi dış sitelere bağlantı içerir. Bu sitelerin içeriğinden ve kişisel veri uygulamalarından sorumlu değilim; kendi koşulları geçerlidir.</p>

<h2 id="degisiklik">5. Değişiklikler</h2>
<p>Bu koşulları güncelleyebilirim. Güncel sürüm her zaman bu sayfadadır; sayfanın başındaki tarih son değişikliği gösterir.</p>
"""

TERMS_EN = """
<p class="note">This is a courtesy translation. The Turkish version is the binding text.</p>
<h2 id="nature">1. What this site is</h2>
<p>This site is a profile page presenting Ahmet Sencer Zararsız's personal and professional background, publications and work. It does not offer legal services and is not intended to solicit work.</p>

<h2 id="no-advice">2. Articles are not legal advice</h2>
<p>Articles provide general information based on the law in force when published; the law may change. Current law and the specific facts must be assessed before applying anything to a real case. Visiting the site, reading articles or sending an e-mail does not create a lawyer-client relationship.</p>

<h2 id="ip">3. Intellectual property</h2>
<p>Copyright in the texts, design and animation code belongs to Ahmet Sencer Zararsız. You may quote short passages with attribution and a link; you may not reproduce or republish full texts without permission. Fonts are used under the SIL Open Font License.</p>

<h2 id="links">4. External links</h2>
<p>The site links to external sites such as LinkedIn and GameLaw.io. I am not responsible for their content or data practices; their own terms apply.</p>

<h2 id="changes">5. Changes</h2>
<p>I may update these terms. The current version is always on this page; the date at the top shows the last change.</p>
"""

# --------------------------------------------------------------------------- Yasal bilgiler
LEGAL_TR = f"""
<h2 id="kimlik">1. Site sahibi</h2>
<div class="table-wrap"><table>
<caption>Tanıtıcı bilgiler</caption>
<tbody>
<tr><th scope="row">Ad soyad</th><td>Ahmet Sencer Zararsız</td></tr>
<tr><th scope="row">Unvan</th><td>Avukat</td></tr>
<tr><th scope="row">Mezun olduğu üniversite</th><td>Atatürk Üniversitesi Hukuk Fakültesi (2022)</td></tr>
<tr><th scope="row">Yabancı dil</th><td>İngilizce</td></tr>
<tr><th scope="row">E-posta</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
</tbody></table></div>

<h2 id="yer-saglayici">2. Yer sağlayıcı</h2>
<p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, ABD.</p>

"""

LEGAL_EN = f"""
<p class="note">This is a courtesy translation. The Turkish version is the binding text.</p>
<h2 id="owner">1. Site owner</h2>
<div class="table-wrap"><table>
<caption>Identifying information</caption>
<tbody>
<tr><th scope="row">Name</th><td>Ahmet Sencer Zararsız</td></tr>
<tr><th scope="row">Title</th><td>Attorney at law (Avukat)</td></tr>
<tr><th scope="row">University</th><td>Atatürk University, Faculty of Law (2022)</td></tr>
<tr><th scope="row">Foreign language</th><td>English</td></tr>
<tr><th scope="row">E-mail</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
</tbody></table></div>

<h2 id="host">2. Hosting provider</h2>
<p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA.</p>

"""

# --------------------------------------------------------------------------- Erişilebilirlik
A11Y_TR = f"""
<div class="test"><b>Uyum durumu</b>Bu site, Web İçeriği Erişilebilirlik Yönergeleri (WCAG) 2.2 AA düzeyini hedefler ve bu düzeyle <strong>kısmen uyumludur</strong>. Bilinen eksikler aşağıdadır.</div>

<h2 id="onlemler">1. Aldığım önlemler</h2>
<ul>
<li>Metin ve arka plan kontrastı normal metinde en az 4,5:1'dir. Açık ve koyu temada ayrı ayrı hesaplanmıştır.</li>
<li>Tüm işlevler klavyeyle kullanılabilir; odak halkası her zaman görünür. Her sayfanın başında "İçeriğe geç" bağlantısı vardır.</li>
<li>Ana sayfadaki animasyon ve kayan şerit <strong>Durdur</strong> düğmesiyle durdurulabilir (WCAG 2.2.2). İşletim sisteminizde "hareketi azalt" açıksa animasyonlar hiç oynatılmaz.</li>
<li>Animasyonun anlattığı akış, ekran okuyucular için metin olarak da verilir.</li>
<li>Sayfalar başlık hiyerarşisi, işaretli bölgeler (header, nav, main, footer) ve doğru dil etiketleriyle (<code>lang</code>) kurulmuştur.</li>
<li>Çerez paneli ekranı kilitlemez, odak tuzağı kurmaz ve Esc ile kapanır.</li>
<li>Metin %200 büyütüldüğünde ve 320 piksel genişlikte yatay kaydırma gerekmez.</li>
</ul>

<h2 id="eksikler">2. Bilinen eksikler</h2>
<ul>
<li>Yazılar yalnızca Türkçedir; İngilizce sayfalarda Türkçe yazılara bağlantı verilir.</li>
<li>Animasyon içindeki metinler görsel olarak küçüktür; aynı içerik ekran okuyucu metninde yer alır.</li>
</ul>

<h2 id="test">3. Nasıl test edildi?</h2>
<p>Son değerlendirme {UPDATED["tr"]} tarihinde yapıldı: axe-core ile otomatik tarama, klavyeyle manuel gezinme, renk kontrastı hesaplaması ve 375 piksel genişlikte mobil görünüm kontrolü.</p>

<h2 id="geri-bildirim">4. Geri bildirim</h2>
<p>Erişemediğiniz bir içerik ya da çalışmayan bir işlev bulursanız <a href="mailto:{EMAIL}?subject=Erişilebilirlik">{EMAIL}</a> adresine yazın. 10 iş günü içinde yanıt vermeyi ve içeriği uygun bir biçimde sunmayı taahhüt ederim.</p>
"""

A11Y_EN = f"""
<p class="note">This is a courtesy translation. The Turkish version is the binding text.</p>
<div class="test"><b>Conformance status</b>This site targets Web Content Accessibility Guidelines (WCAG) 2.2 level AA and is <strong>partially conformant</strong>. Known gaps are listed below.</div>

<h2 id="measures">1. What I've done</h2>
<ul>
<li>Text contrast is at least 4.5:1 for normal text, checked separately for light and dark themes.</li>
<li>Everything works with a keyboard and the focus ring is always visible. Every page starts with a "Skip to content" link.</li>
<li>The home page animation and scrolling strip can be stopped with the <strong>Pause</strong> button (WCAG 2.2.2). If your system has "reduce motion" on, animations don't play at all.</li>
<li>The flow shown in the animation is also provided as text for screen readers.</li>
<li>Pages use a heading hierarchy, landmarks (header, nav, main, footer) and correct <code>lang</code> attributes.</li>
<li>The cookie panel doesn't block the screen or trap focus, and closes with Esc.</li>
<li>No horizontal scrolling at 200% text zoom or at 320 px width.</li>
</ul>

<h2 id="gaps">2. Known gaps</h2>
<ul>
<li>Articles are in Turkish only; English pages link to them.</li>
<li>Text inside the animation is visually small; the same content is available in the screen reader text.</li>
</ul>

<h2 id="testing">3. How it was tested</h2>
<p>Last assessed on {UPDATED["en"]}: automated scan with axe-core, manual keyboard navigation, contrast calculation and a 375 px mobile check.</p>

<h2 id="feedback">4. Feedback</h2>
<p>If you can't access something, write to <a href="mailto:{EMAIL}?subject=Accessibility">{EMAIL}</a>. I commit to replying within 10 working days and providing the content in a suitable format.</p>
"""
