(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");

  // ---------- Tarayıcı depolaması: rıza kaydı ve tema ----------
  // sz-consent: seçiminizin kaydı (zorunlu). sz-theme: tema (yalnızca "tercih" izni verildiyse).
  var KEY = "sz-consent", THEME = "sz-theme", VERSION = 1, TTL = 365 * 864e5;
  function readConsent() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || "null");
      if (!c || c.v !== VERSION || Date.now() - c.ts > TTL) return null;
      return c;
    } catch (e) { return null; }
  }
  function writeConsent(pref) {
    var c = { v: VERSION, pref: !!pref, ts: Date.now() };
    try {
      localStorage.setItem(KEY, JSON.stringify(c));
      if (!pref) localStorage.removeItem(THEME);
      else if (doc.getAttribute("data-theme")) localStorage.setItem(THEME, doc.getAttribute("data-theme"));
    } catch (e) {}
    return c;
  }
  var consent = readConsent();

  // ---------- Tema ----------
  var mq = window.matchMedia("(prefers-color-scheme: dark)");
  function currentTheme() { return doc.getAttribute("data-theme") || (mq.matches ? "dark" : "light"); }
  function setTheme(t) {
    // Geçiş animasyonlarını bir kareliğine kapat: renkler eski temada takılı kalmasın
    doc.classList.add("theme-switching");
    doc.setAttribute("data-theme", t);
    void doc.offsetWidth;
    requestAnimationFrame(function () { requestAnimationFrame(function () { doc.classList.remove("theme-switching"); }); });
    if (consent && consent.pref) { try { localStorage.setItem(THEME, t); } catch (e) {} }
    syncThemeBtn();
    document.dispatchEvent(new CustomEvent("sz-theme"));
  }
  var themeBtn = document.querySelector("[data-theme-toggle]");
  function syncThemeBtn() {
    if (!themeBtn) return;
    var dark = currentTheme() === "dark";
    themeBtn.setAttribute("aria-pressed", String(dark));
  }
  if (themeBtn) {
    syncThemeBtn();
    themeBtn.addEventListener("click", function () { setTheme(currentTheme() === "dark" ? "light" : "dark"); });
  }
  if (mq.addEventListener) mq.addEventListener("change", syncThemeBtn);

  // ---------- Çerez paneli ----------
  var panel = document.getElementById("consent");
  if (panel) {
    var prefs = panel.querySelector(".prefs");
    var prefBox = panel.querySelector("#pref-toggle");
    var state = panel.querySelector(".state");
    var closeBtn = panel.querySelector(".x");
    var opener = null;
    function show(fromUser) {
      panel.hidden = false;
      prefBox.checked = !!(consent && consent.pref);
      state.textContent = consent ? (consent.pref ? panel.getAttribute("data-on") : panel.getAttribute("data-off")) : "";
      closeBtn.hidden = !consent;
      if (fromUser) panel.querySelector("h2").focus();
    }
    function hide() {
      panel.hidden = true;
      if (opener) { opener.focus(); opener = null; }
    }
    function decide(pref) { consent = writeConsent(pref); hide(); }
    panel.querySelector("[data-c=reject]").addEventListener("click", function () { decide(false); });
    panel.querySelector("[data-c=accept]").addEventListener("click", function () { decide(true); });
    panel.querySelector("[data-c=prefs]").addEventListener("click", function (ev) {
      var open = prefs.hidden;
      prefs.hidden = !open;
      ev.currentTarget.setAttribute("aria-expanded", String(open));
    });
    panel.querySelector("[data-c=save]").addEventListener("click", function () { decide(prefBox.checked); });
    closeBtn.addEventListener("click", hide);
    panel.addEventListener("keydown", function (e) { if (e.key === "Escape" && consent) hide(); });
    document.querySelectorAll("[data-consent-open]").forEach(function (b) {
      b.addEventListener("click", function () { opener = b; show(true); });
    });
    if (!consent) show(false);
  }

  // ---------- Başlık çizgisi ----------
  var head = document.querySelector(".site-head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---------- Görünür olunca giriş ----------
  var els = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add("in"); });

  // ---------- Legal design: Hukukça / Sade dil ----------
  document.querySelectorAll("[data-ld]").forEach(function (seg) {
    var box = seg.closest(".ld, .ld-demo");
    var stage = box && box.querySelector(".ld-stage");
    if (!stage) return;
    var panes = { legal: stage.querySelector(".ld-legal"), plain: stage.querySelector(".ld-plain") };
    var buttons = seg.querySelectorAll("button");
    function setMode(mode) {
      var from = stage.offsetHeight;
      seg.setAttribute("data-mode", mode);
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-mode") === mode)); });
      Object.keys(panes).forEach(function (k) { panes[k].hidden = k !== mode; });
      var to = panes[mode].offsetHeight;
      stage.style.height = from + "px";
      requestAnimationFrame(function () { stage.style.height = to + "px"; });
      setTimeout(function () { stage.style.height = ""; }, 700);
    }
    stage.addEventListener("transitionend", function (e) { if (e.propertyName === "height") stage.style.height = ""; });
    buttons.forEach(function (b) { b.addEventListener("click", function () { setMode(b.getAttribute("data-mode")); }); });
  });
})();

// Yazılar: konuya göre süzme
(function () {
  var group = document.querySelector("[data-filter]");
  var list = document.querySelector("[data-filter-list]");
  if (!group || !list) return;
  var status = document.querySelector("[data-filter-status]");
  var cards = list.querySelectorAll("[data-cat]");
  group.addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-cat]");
    if (!b) return;
    var cat = b.getAttribute("data-cat"), n = 0;
    group.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
    cards.forEach(function (c) {
      var show = cat === "*" || c.getAttribute("data-cat") === cat;
      c.hidden = !show;
      if (show) { n++; c.classList.add("in"); }
    });
    if (status) status.textContent = n + (document.documentElement.lang === "en" ? " articles shown" : " yazı gösteriliyor");
  });
})();

// Mobil menü
(function () {
  var head = document.querySelector(".site-head");
  var btn = document.querySelector(".menu-btn");
  if (!head || !btn) return;
  function set(open) {
    head.classList.toggle("menu-open", open);
    btn.setAttribute("aria-expanded", String(open));
  }
  btn.addEventListener("click", function () { set(btn.getAttribute("aria-expanded") !== "true"); });
  document.querySelectorAll(".nav-links a").forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && head.classList.contains("menu-open")) { set(false); btn.focus(); } });
  document.addEventListener("click", function (e) { if (!head.contains(e.target)) set(false); });
})();

// Animasyon kaydırıcısı
(function () {
  var box = document.querySelector("[data-reels]");
  if (!box) return;
  var trackEl = box.querySelector(".reels-track");
  var slides = box.querySelectorAll(".reel-slide");
  var tabs = box.querySelectorAll("[data-slide]");
  function mark(i) {
    slides.forEach(function (s, k) { s.classList.toggle("is-active", k === i); });
    tabs.forEach(function (b, k) { b.setAttribute("aria-pressed", String(k === i)); });
  }
  mark(0);
  if (/[?&]reel2=/.test(location.search)) { trackEl.style.scrollBehavior = "auto"; trackEl.scrollLeft = slides[1].offsetLeft - trackEl.offsetLeft; mark(1); }
  tabs.forEach(function (b) {
    b.addEventListener("click", function () {
      var i = +b.getAttribute("data-slide");
      trackEl.scrollTo({ left: slides[i].offsetLeft - trackEl.offsetLeft, behavior: "smooth" });
      mark(i);
    });
  });
  var tmr;
  trackEl.addEventListener("scroll", function () {
    clearTimeout(tmr);
    tmr = setTimeout(function () {
      var best = 0, dist = Infinity;
      slides.forEach(function (s, k) { var d = Math.abs(s.offsetLeft - trackEl.offsetLeft - trackEl.scrollLeft); if (d < dist) { dist = d; best = k; } });
      mark(best);
    }, 80);
  }, { passive: true });
})();
