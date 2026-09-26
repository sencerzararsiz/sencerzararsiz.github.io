# sencerzararsiz.github.io

Ahmet Sencer Zararsız'ın kişisel sitesi. Canlı adres: https://sencerzararsiz.github.io

Statik HTML/CSS/JS; framework, çerez, analitik ya da üçüncü taraf istek yok.

## Yapı

- `build.py` tüm içeriğin (TR + EN) tek kaynağı; `index.html` ve `en/index.html` buradan üretilir.
- `assets/js/showreel.js` kahraman bölümündeki animasyon. Her kare `seek(t)` içinde zamandan hesaplanır; yaylar kapalı-form çözümdür, döngü kesintisizdir. `?reel=12` gibi bir parametre belirli kareyi dondurur.
- `assets/js/main.js` kaydırma girişleri ve "Hukukça / Sade dil" demosu.
- `assets/fonts` Geist, Geist Mono ve Instrument Serif (SIL Open Font License), yerel olarak sunulur.
- `tools/og.html` paylaşım görselinin (`assets/img/og.png`, `og-en.png`) kaynağı.

## İçeriği güncellemek

1. `build.py` içindeki `CONTENT`, `EXPERIENCE`, `VENTURES`, `POSTS` vb. listeleri düzenleyin.
2. `python build.py` çalıştırın.
3. Commit + push; GitHub Pages birkaç dakika içinde yayınlar.

Yerelde önizleme: `python -m http.server 8030` ve http://localhost:8030
