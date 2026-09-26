# sencerzararsiz.github.io

Ahmet Sencer Zararsız'ın kişisel sitesi. Canlı adres: https://sencerzararsiz.github.io

Statik HTML/CSS/JS; framework, çerez, analitik ya da üçüncü taraf istek yok.

## Yapı

- `build.py` ana sayfa içeriği ve tüm sayfa şablonları; `python build.py` 24 sayfayı üretir.
- `content_posts.py` yazılar (mevzuat atıfları 26.09.2026'da birincil kaynaktan doğrulandı).
- `content_legal.py` KVKK Aydınlatma Metni, Çerez Politikası, Kullanım Koşulları, Yasal Bilgiler, Erişilebilirlik Beyanı.
- `assets/js/main.js` tema düğmesi, çerez tercih paneli, kaydırma girişleri, "Hukukça / Sade dil" demosu.
- `assets/js/showreel.js` kahraman bölümündeki animasyon. Her kare `seek(t)` içinde zamandan hesaplanır; yaylar kapalı-form çözümdür, döngü kesintisizdir. `?reel=12` gibi bir parametre belirli kareyi dondurur.
- `assets/fonts` Geist, Geist Mono ve Instrument Serif (SIL Open Font License), yerel olarak sunulur.
- `tools/og.html` paylaşım görselinin (`assets/img/og.png`, `og-en.png`) kaynağı.

## İçeriği güncellemek

1. `build.py` içindeki `CONTENT`, `EXPERIENCE`, `VENTURES`, `POSTS` vb. listeleri düzenleyin.
2. `python build.py` çalıştırın.
3. Commit + push; GitHub Pages birkaç dakika içinde yayınlar.

Yerelde önizleme: `python -m http.server 8030` ve http://localhost:8030

## Reklam yasağı

Site, 1136 s. Avukatlık Kanunu m.55 ve TBB Reklam Yasağı Yönetmeliği m.7 gözetilerek kuruldu:
müvekkil/referans bilgisi, iş çağrısı, rakamla övgü, JSON-LD, sitemap.xml ve anahtar sözcük kullanılmaz.
Yeni içerik eklerken bu çizgiyi koruyun.
