(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");

  // Başlık: kaydırınca ince çizgi
  var head = document.querySelector(".site-head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Görünür olunca yumuşak giriş
  var els = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add("in"); });
  }

  // Legal design: Hukukça / Sade dil
  var seg = document.querySelector("[data-ld]");
  var stage = document.querySelector(".ld-stage");
  if (seg && stage) {
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
    }
    stage.addEventListener("transitionend", function (e) { if (e.propertyName === "height") stage.style.height = ""; });
    buttons.forEach(function (b) { b.addEventListener("click", function () { setMode(b.getAttribute("data-mode")); }); });
  }
})();
