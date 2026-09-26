/* Showreel: tek şekil, kesintisiz morph.
   Her stil seek(t) içinde zamandan hesaplanır; CSS geçişi, zamanlayıcı ya da
   kareler arası durum yok. Yaylar kapalı-form basamak yanıtıdır; hedefi birden
   çok kez değişen bir değer, her değişim için bir yayın toplamıdır. */
(function () {
  "use strict";

  var root = document.querySelector("[data-reel]");
  if (!root) return;

  var L = 16;            // döngü süresi (sn)
  var TAU = Math.PI * 2;
  var lang = (document.documentElement.lang || "tr").slice(0, 2);

  var T = {
    tr: {
      btn: "Taramayı başlat",
      found: "3 bulgu",
      fix: "Düzelt",
      cookieT: "Çerez tercihleri",
      cookieP: "Analitik çerezleri yalnızca onay verirseniz kullanırız.",
      reject: "Reddet",
      accept: "Kabul et",
      smsT: "SMS ile bilgilendirme",
      smsS: "Onay İYS'ye iletildi",
      legalChip: "Hukukça",
      legal: "Veri sorumlusu sıfatıyla Şirketimiz tarafından, 6698 sayılı Kanun'un 5. maddesinin 2. fıkrasının (c) bendi uyarınca, bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması kaydıyla sözleşmenin taraflarına ait kişisel verilerin işlenmesinin gerekli olması hukuki sebebine dayanılarak kimlik ve iletişim verileriniz işlenmektedir…",
      plainChip: "Sade dil",
      plain: "Adresinizi yalnızca siparişinizi teslim etmek için kullanırız.",
      plainRef: "KVKK m.5/2-c · sözleşmenin ifası",
      ph: "Mevzuatta ara…",
      items: [["KVKK m.10", "Aydınlatma yükümlülüğü"], ["KVKK m.11", "İlgili kişinin hakları"], ["6563 m.6", "Ticari elektronik ileti"]],
      toast: "Uyum raporu hazır"
    },
    en: {
      btn: "Run compliance scan",
      found: "3 findings",
      fix: "Fix",
      cookieT: "Cookie preferences",
      cookieP: "We only use analytics cookies if you say yes.",
      reject: "Reject",
      accept: "Accept",
      smsT: "SMS updates",
      smsS: "Consent sent to İYS",
      legalChip: "Legalese",
      legal: "In its capacity as data controller, the Company processes your identity and contact data on the legal ground that processing personal data of the parties is necessary, provided that it is directly related to the conclusion or performance of a contract, pursuant to Article 5(2)(c) of Law No. 6698…",
      plainChip: "Plain language",
      plain: "We use your address only to deliver your order.",
      plainRef: "KVKK Art. 5(2)(c) · contract",
      ph: "Search the law…",
      items: [["KVKK m.10", "Duty to inform"], ["KVKK m.11", "Data subject rights"], ["6563 m.6", "Commercial e-messages"]],
      toast: "Compliance report ready"
    }
  }[lang === "en" ? "en" : "tr"];

  var QUERY = "m.11";
  var I_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';

  // ---------- Sahne ----------
  root.innerHTML =
    '<div class="sr-scene" aria-hidden="true">' +
      '<div class="sr-shape">' +
        '<div class="sr-c sr-btn" data-s="btn"><span>' + T.btn + '</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>' +
        '<div class="sr-c sr-load" data-s="load"><svg viewBox="0 0 30 30"><circle cx="15" cy="15" r="11" fill="none" stroke="currentColor" stroke-opacity=".2" stroke-width="3"/><circle class="arc" cx="15" cy="15" r="11" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray=".28 1"/></svg></div>' +
        '<div class="sr-c sr-check" data-s="check"><svg viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path class="tick" d="M8 15.5l4.8 4.8L22.5 10" pathLength="1" stroke-dasharray="1 1"/></svg></div>' +
        '<div class="sr-c sr-find" data-s="find"><span class="l"><i class="dot"></i>' + T.found + '</span><span class="mini">' + T.fix + '</span></div>' +
        '<div class="sr-c sr-cookie" data-s="cookie"><div><strong>' + T.cookieT + '</strong><p>' + T.cookieP + '</p></div><div class="row"><span class="b rej">' + T.reject + '</span><span class="b">' + T.accept + '</span></div></div>' +
        '<div class="sr-c sr-toggle" data-s="toggle"><span class="t"><strong>' + T.smsT + '</strong><small>' + T.smsS + '</small></span><span class="sr-sw"><i class="sr-knob"></i></span></div>' +
        '<div class="sr-c sr-legal" data-s="legal"><span class="sr-chip">' + T.legalChip + '</span><p>' + T.legal + '</p></div>' +
        '<div class="sr-c sr-plain" data-s="plain"><span class="sr-chip">' + T.plainChip + '</span><p>' + T.plain + '</p><span class="ref">' + T.plainRef + '</span></div>' +
        '<div class="sr-c sr-cmdk" data-s="cmdk"><div class="in"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><span class="q"></span><span class="kbd">⌘K</span></div><ul>' +
          T.items.map(function (it) { return '<li><b>' + it[0] + '</b>' + it[1] + '</li>'; }).join("") +
        '</ul></div>' +
        '<div class="sr-c sr-toast" data-s="toast"><i>' + I_CHECK + '</i>' + T.toast + '</div>' +
      '</div>' +
      '<div class="sr-ripple"></div>' +
      '<div class="sr-cursor"><svg viewBox="0 0 26 26"><path d="M5 3l15 9.2-6.6 1.4-3.3 6.4z" fill="#111" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg></div>' +
    '</div>';

  var scene = root.querySelector(".sr-scene");
  var shape = root.querySelector(".sr-shape");
  var cursor = root.querySelector(".sr-cursor");
  var ripple = root.querySelector(".sr-ripple");
  var arc = root.querySelector(".arc");
  var tick = root.querySelector(".tick");
  var rej = root.querySelector(".rej");
  var mini = root.querySelector(".mini");
  var sw = root.querySelector(".sr-sw");
  var knob = root.querySelector(".sr-knob");
  var q = root.querySelector(".q");
  var lis = root.querySelectorAll(".sr-cmdk li");
  var contents = {};
  Array.prototype.forEach.call(root.querySelectorAll(".sr-c"), function (el) { contents[el.getAttribute("data-s")] = el; });

  // ---------- Matematik ----------
  function spring(t, f, z) {
    if (t <= 0) return 0;
    var w = TAU * f;
    if (z >= 1) return 1 - Math.exp(-w * t) * (1 + w * t); // kritik sönüm
    var wd = w * Math.sqrt(1 - z * z);
    return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t));
  }
  // keys: [[zaman, değer|dizi], ...] sıralı. Önceki döngünün olayları da
  // eklenir; böylece değer periyodik kalır ve son kare ilk kareyle aynıdır.
  function track(keys, f, z) {
    f = f || 2.3; z = z || 0.82;
    var n = keys.length, vec = Array.isArray(keys[0][1]);
    return function (t) {
      var base = keys[n - 1][1];
      var out = vec ? base.slice() : base;
      for (var c = -1; c <= 0; c++) {
        for (var i = 0; i < n; i++) {
          var te = keys[i][0] + c * L;
          if (t < te) break;
          var s = spring(t - te, f, z);
          var prev = keys[(i - 1 + n) % n][1], cur = keys[i][1];
          if (vec) { for (var k = 0; k < out.length; k++) out[k] += (cur[k] - prev[k]) * s; }
          else out += (cur - prev) * s;
        }
      }
      return out;
    };
  }
  function bump(t, at, dur) { // tık için kısa nabız, 0→1→0
    var x = (t - at) / dur;
    if (x <= 0 || x >= 1) return 0;
    return Math.sin(Math.PI * x);
  }
  function clamp01(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }

  // ---------- Zaman çizelgesi ----------
  // Şekil: [w, h, r, ink, paper, accent] (arka plan karışım ağırlıkları)
  var S = {
    btn:    [256, 60, 30, 1, 0, 0],
    load:   [64, 64, 32, 1, 0, 0],
    check:  [64, 64, 32, 0, 0, 1],
    find:   [330, 64, 32, 0, 1, 0],
    cookie: [360, 176, 22, 0, 1, 0],
    toggle: [300, 72, 36, 0, 1, 0],
    legal:  [400, 200, 18, 0, 1, 0],
    plain:  [400, 168, 18, 0, 1, 0],
    cmdk3:  [380, 189, 16, 1, 0, 0],
    cmdk2:  [380, 149, 16, 1, 0, 0],
    cmdk1:  [380, 109, 16, 1, 0, 0],
    toast:  [300, 60, 30, 1, 0, 0]
  };
  // Harfler: "m" 13.35, "." 13.50, "1" 13.65, "1" 13.80
  var CH = [13.35, 13.5, 13.65, 13.8];
  var shapeT = track([
    [0, S.btn], [1.35, S.load], [3.0, S.check], [3.9, S.find], [5.4, S.cookie],
    [7.6, S.toggle], [9.8, S.legal], [11.4, S.plain], [12.7, S.cmdk3],
    [CH[2], S.cmdk2], [CH[3], S.cmdk1], [14.7, S.toast], [15.7, S.btn]
  ]);
  // Cursor pozisyonu (sahne koordinatı, ucun konumu)
  var curT = track([
    [0, [468, 488]], [0.3, [304, 304]], [1.55, [438, 420]],
    [4.25, [414, 304]], [5.55, [470, 440]], [5.95, [218, 350]],
    [7.35, [468, 432]], [8.05, [406, 302]], [9.2, [470, 424]],
    [12.85, [236, 221]], [13.45, [470, 438]], [15.1, [468, 488]]
  ], 1.7, 0.9);
  var PRESS = [1.1, 5.0, 7.0, 8.75, 13.15];

  // İçerik görünürlüğü: çıkış, girişten önce; metin üst üste binmez.
  var VIS = {
    btn: [[1.25, 0], [15.78, 1]],
    load: [[1.45, 1], [2.92, 0]],
    check: [[3.06, 1], [3.8, 0]],
    find: [[4.0, 1], [5.3, 0]],
    cookie: [[5.5, 1], [7.5, 0]],
    toggle: [[7.7, 1], [9.7, 0]],
    legal: [[9.92, 1], [11.28, 0]],
    plain: [[11.5, 1], [12.6, 0]],
    cmdk: [[12.8, 1], [14.6, 0]],
    toast: [[14.8, 1], [15.6, 0]]
  };
  var visT = {};
  Object.keys(VIS).forEach(function (k) { visT[k] = track(VIS[k], 3.2, 1); });

  // Anahtar düğmesi: öndeki kenar hızlı, arkadaki yavaş yaya bağlı → esneme.
  var knobR = track([[0, 28], [8.8, 50]], 4.2, 0.8);
  var knobL = track([[0, 2], [8.86, 24]], 2.4, 0.8);
  var swOn = track([[0, 0], [8.8, 1]], 3, 1);
  var rejT = track([[0, 0], [7.02, 1]], 3.5, 1);
  var tickT = track([[0, 0], [3.1, 1]], 1.6, 1);
  // ⌘K satırları: eşleşmeyen satır yüksekliği 40 → 0
  var liT = [
    track([[0, 40], [CH[3], 0]]),          // m.10: "m.11" ile elenir
    track([[0, 40]]),                        // m.11 kalır
    track([[0, 40], [CH[2], 0]])           // 6563 m.6: "m.1" ile elenir
  ];
  var liSel = track([[0, 0], [14.3, 1], [14.62, 0]], 4, 1);

  var colors = {};
  function readColors() {
    var cs = getComputedStyle(document.documentElement);
    ["--ink", "--card", "--accent"].forEach(function (v) {
      var hex = cs.getPropertyValue(v).trim();
      var m = hex.replace("#", "");
      if (m.length === 3) m = m.split("").map(function (c) { return c + c; }).join("");
      colors[v] = [parseInt(m.slice(0, 2), 16), parseInt(m.slice(2, 4), 16), parseInt(m.slice(4, 6), 16)];
    });
  }
  readColors();
  var mq = window.matchMedia("(prefers-color-scheme: dark)");
  if (mq.addEventListener) mq.addEventListener("change", function () { readColors(); seek(t); });

  // ---------- seek(t): saf zaman fonksiyonu ----------
  function seek(t) {
    var s = shapeT(t);
    var press = bump(t, PRESS[0], 0.22) * 0.05;
    var w = s[0], h = s[1], r = Math.min(s[2], h / 2, w / 2);
    var a = s[3], b = s[4], c = s[5], sum = a + b + c || 1;
    var ci = colors["--ink"], cp = colors["--card"], ca = colors["--accent"];
    var rgb = [0, 1, 2].map(function (k) { return Math.round((ci[k] * a + cp[k] * b + ca[k] * c) / sum); });
    shape.style.width = w.toFixed(2) + "px";
    shape.style.height = h.toFixed(2) + "px";
    shape.style.borderRadius = r.toFixed(2) + "px";
    shape.style.background = "rgb(" + rgb.join(",") + ")";
    shape.style.transform = "translate(-50%,-50%) scale(" + (1 - press).toFixed(4) + ")";

    for (var k in contents) {
      var v = clamp01(visT[k](t));
      var el = contents[k];
      el.style.opacity = v.toFixed(3);
      el.style.filter = v > 0.995 ? "none" : "blur(" + ((1 - v) * 6).toFixed(2) + "px)";
      var base = k === "cmdk" ? "translate(-50%,0)" : "translate(-50%,-50%)";
      el.style.transform = base + " translateY(" + ((1 - v) * 5).toFixed(2) + "px)";
    }

    // Yükleniyor yayı
    arc.style.transform = "rotate(" + ((t * 400) % 360).toFixed(1) + "deg)";
    arc.style.transformOrigin = "15px 15px";
    tick.style.strokeDashoffset = (1 - clamp01(tickT(t))).toFixed(3);

    // Bulgu → Düzelt'e basış
    mini.style.transform = "scale(" + (1 - bump(t, PRESS[1], 0.22) * 0.08).toFixed(4) + ")";

    // Çerez: Reddet dolar (eşit ağırlıklı iki düğme — legal design)
    var rv = clamp01(rejT(t));
    rej.style.background = rv > 0.01 ? "rgba(" + colors["--ink"].join(",") + "," + rv.toFixed(3) + ")" : "transparent";
    rej.style.color = rv > 0.5 ? "var(--card)" : "var(--ink)";
    rej.style.transform = "scale(" + (1 - bump(t, PRESS[2], 0.22) * 0.06).toFixed(4) + ")";

    // Anahtar
    var l = knobL(t), rr = knobR(t);
    knob.style.left = l.toFixed(2) + "px";
    knob.style.width = Math.max(26, rr - l).toFixed(2) + "px";
    var on = clamp01(swOn(t));
    var lc = [216, 213, 206];
    var mix = [0, 1, 2].map(function (k2) { return Math.round(lc[k2] * (1 - on) + colors["--accent"][k2] * on); });
    sw.style.background = "rgb(" + mix.join(",") + ")";
    sw.style.transform = "scale(" + (1 - bump(t, PRESS[3], 0.22) * 0.08).toFixed(4) + ")";

    // ⌘K: yazma
    var n = 0;
    for (var j = 0; j < CH.length; j++) if (t >= CH[j]) n++;
    var typed = QUERY.slice(0, n);
    var caretOn = (Math.floor(t * 2.2) % 2 === 0) || (n > 0 && n < 4);
    q.innerHTML = (typed ? typed : '<span class="ph">' + T.ph + '</span>') + (t > 13.2 && caretOn ? '<i class="caret"></i>' : "");
    for (var m = 0; m < lis.length; m++) {
      var hh = Math.max(0, liT[m](t));
      lis[m].style.height = hh.toFixed(2) + "px";
      lis[m].style.opacity = clamp01(hh / 40).toFixed(3);
    }
    var sel = clamp01(liSel(t));
    lis[1].style.background = "rgba(" + colors["--accent"].join(",") + "," + (0.12 + sel * 0.5).toFixed(3) + ")";

    // Cursor + tıklama halkası
    var p = curT(t);
    var cp2 = 0, rip = null;
    for (var i2 = 0; i2 < PRESS.length; i2++) {
      cp2 = Math.max(cp2, bump(t, PRESS[i2], 0.2));
      var dt = t - PRESS[i2];
      if (dt >= 0 && dt < 0.5) rip = dt / 0.5;
    }
    cursor.style.transform = "translate(" + (p[0] - 5).toFixed(2) + "px," + (p[1] - 3).toFixed(2) + "px) scale(" + (1 - cp2 * 0.16).toFixed(4) + ")";
    if (rip !== null) {
      ripple.style.opacity = (1 - rip).toFixed(3);
      ripple.style.transform = "translate(" + p[0].toFixed(2) + "px," + p[1].toFixed(2) + "px) scale(" + (0.3 + rip * 0.9).toFixed(3) + ")";
    } else ripple.style.opacity = "0";
  }

  // ---------- Ölçek ----------
  function fit() {
    var wpx = root.clientWidth;
    scene.style.transform = "scale(" + (wpx / 600) + ")";
  }
  fit();
  if (window.ResizeObserver) new ResizeObserver(fit).observe(root);
  else window.addEventListener("resize", fit);

  // ---------- Oynatma ----------
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var btn = document.querySelector("[data-reel-toggle]");
  var t = 0, last = null, playing = !reduce.matches, visible = true, raf = null;

  function frame(now) {
    raf = null;
    if (last !== null) t = (t + Math.min(0.05, (now - last) / 1000)) % L;
    last = now;
    seek(t);
    loop();
  }
  function loop() {
    if (playing && visible && !document.hidden && raf === null) raf = requestAnimationFrame(frame);
    else if (!(playing && visible && !document.hidden)) last = null;
  }
  function setPlaying(v) {
    playing = v;
    if (btn) {
      btn.setAttribute("aria-pressed", String(!v));
      var lbl = btn.querySelector(".lbl");
      if (lbl) lbl.textContent = v ? btn.getAttribute("data-pause") : btn.getAttribute("data-play");
    }
    last = null;
    loop();
  }
  // ?reel=<sn> belirli bir kareyi dondurur (kare kontrolü ve paylaşım görseli için)
  var fixed = /[?&]reel=([\d.]+)/.exec(location.search);
  if (fixed) { t = parseFloat(fixed[1]) % L; playing = false; seek(t); }
  else if (reduce.matches) { t = 11.95; seek(t); }
  else seek(0);
  setPlaying(playing);

  if (btn) btn.addEventListener("click", function () { setPlaying(!playing); });
  document.addEventListener("visibilitychange", loop);
  if (window.IntersectionObserver) {
    new IntersectionObserver(function (es) { visible = es[0].isIntersecting; last = null; loop(); }, { threshold: 0.05 }).observe(root);
  }
})();
