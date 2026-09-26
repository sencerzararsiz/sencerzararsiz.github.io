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
    doc.setAttribute("data-theme", t);
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
