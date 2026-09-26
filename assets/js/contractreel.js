/* Sözleşme süreci animasyonu: taslak → müzakere → onay → imza → takip → yenileme.
   showreel.js ile aynı ilke: her stil seek(t) içinde zamandan hesaplanır. */
(function () {
  "use strict";

  var root = document.querySelector("[data-reel2]");
  if (!root) return;

  var L = 16, TAU = Math.PI * 2;
  var lang = (document.documentElement.lang || "tr").slice(0, 2);
  var T = {
    tr: {
      draft: "Hizmet Sözleşmesi", ver: "Taslak v1", neg: "Müzakere · 2 değişiklik",
      del: "Yüklenici her türlü zarardan sınırsız sorumludur.",
      ins: "Sorumluluk, sözleşme bedeliyle sınırlıdır.",
      steps: ["Hukuk", "Finans", "Yönetim"], appr: "Onay akışı",
      sign: "E-imza", signed: "İmzalandı",
      trackT: "Yükümlülük takvimi",
      rows: [["Teslim", "90 gün"], ["Kabul testi", "10 iş günü"], ["Yenileme bildirimi", "30 gün önce"]],
      toast: "Yenilemeye 30 gün kaldı"
    },
    en: {
      draft: "Services Agreement", ver: "Draft v1", neg: "Negotiation · 2 changes",
      del: "The Contractor is liable without limit for any loss.",
      ins: "Liability is capped at the contract price.",
      steps: ["Legal", "Finance", "Management"], appr: "Approval flow",
      sign: "E-signature", signed: "Signed",
      trackT: "Obligation calendar",
      rows: [["Delivery", "90 days"], ["Acceptance test", "10 working days"], ["Renewal notice", "30 days before"]],
      toast: "30 days to renewal"
    }
  }[lang === "en" ? "en" : "tr"];

  var CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';
  var BELL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16V11a6 6 0 0112 0v5l1.5 2h-15zM10 20a2 2 0 004 0"/></svg>';

  root.innerHTML =
    '<div class="sr-scene" aria-hidden="true">' +
      '<div class="sr-shape cr-shape">' +
        '<div class="sr-c cr-doc" data-s="doc"><div class="cr-head"><b>' + T.draft + '</b><span class="sr-chip">' + T.ver + '</span></div>' +
          '<i class="cr-line w90"></i><i class="cr-line w70"></i><i class="cr-line w80"></i><i class="cr-line w60"></i><i class="cr-line w75"></i></div>' +
        '<div class="sr-c cr-neg" data-s="neg"><div class="cr-head"><b>' + T.draft + '</b><span class="sr-chip cr-chip-a">' + T.neg + '</span></div>' +
          '<i class="cr-line w90"></i><p class="cr-del"><span>' + T.del + '</span><i class="cr-strike"></i></p><p class="cr-ins">' + T.ins + '</p><i class="cr-line w60"></i></div>' +
        '<div class="sr-c cr-appr" data-s="appr"><span class="cr-label">' + T.appr + '</span><div class="cr-steps">' +
          T.steps.map(function (s) { return '<span class="cr-step"><i>' + CHECK + '</i>' + s + '</span>'; }).join('<b class="cr-bar"><em></em></b>') +
        '</div></div>' +
        '<div class="sr-c cr-sign" data-s="sign"><span class="cr-label">' + T.sign + '</span>' +
          '<svg class="cr-sig" viewBox="0 0 220 60" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path class="cr-sig-p" pathLength="1" stroke-dasharray="1 1" d="M8 42c14-20 22-30 30-28 9 2-4 30 6 30 8 0 14-26 22-26 7 0 3 20 10 20 8 0 12-16 20-16s6 14 14 14c10 0 16-22 26-22 8 0 6 18 14 18 9 0 18-12 28-14 10-2 18 4 34 2"/></svg>' +
          '<span class="cr-signed"><i>' + CHECK + '</i>' + T.signed + '</span></div>' +
        '<div class="sr-c cr-track" data-s="track"><span class="cr-label">' + T.trackT + '</span><ul>' +
          T.rows.map(function (r) { return '<li><span>' + r[0] + '</span><b>' + r[1] + '</b><i class="cr-prog"><em></em></i></li>'; }).join('') +
        '</ul></div>' +
        '<div class="sr-c sr-toast cr-toast" data-s="toast"><i>' + BELL + '</i>' + T.toast + '</div>' +
      '</div>' +
      '<div class="sr-ripple"></div>' +
      '<div class="sr-cursor"><svg viewBox="0 0 26 26"><path d="M5 3l15 9.2-6.6 1.4-3.3 6.4z" fill="#111" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg></div>' +
    '</div>';

  var scene = root.querySelector(".sr-scene");
  var shape = root.querySelector(".sr-shape");
  var cursor = root.querySelector(".sr-cursor");
  var ripple = root.querySelector(".sr-ripple");
  var strike = root.querySelector(".cr-strike");
  var del = root.querySelector(".cr-del span");
  var ins = root.querySelector(".cr-ins");
  var stepEls = root.querySelectorAll(".cr-step");
  var bars = root.querySelectorAll(".cr-bar em");
  var sig = root.querySelector(".cr-sig-p");
  var signed = root.querySelector(".cr-signed");
  var progs = root.querySelectorAll(".cr-prog em");
  var contents = {};
  Array.prototype.forEach.call(root.querySelectorAll(".sr-c"), function (el) { contents[el.getAttribute("data-s")] = el; });

  function spring(t, f, z) {
    if (t <= 0) return 0;
    var w = TAU * f;
    if (z >= 1) return 1 - Math.exp(-w * t) * (1 + w * t);
    var wd = w * Math.sqrt(1 - z * z);
    return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t));
  }
  function track(keys, f, z) {
    f = f || 2.3; z = z || 0.82;
    var n = keys.length, vec = Array.isArray(keys[0][1]);
    return function (t) {
      var base = keys[n - 1][1], out = vec ? base.slice() : base;
      for (var c = -1; c <= 0; c++) {
        for (var i = 0; i < n; i++) {
          var te = keys[i][0] + c * L;
          if (t < te) break;
          var s = spring(t - te, f, z), prev = keys[(i - 1 + n) % n][1], cur = keys[i][1];
          if (vec) { for (var k = 0; k < out.length; k++) out[k] += (cur[k] - prev[k]) * s; } else out += (cur - prev) * s;
        }
      }
      return out;
    };
  }
  function bump(t, at, dur) { var x = (t - at) / dur; return x <= 0 || x >= 1 ? 0 : Math.sin(Math.PI * x); }
  function c01(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }

  // Şekil: [w, h, r, ink, card, accent]
  var S = {
    doc: [320, 210, 18, 0, 1, 0], neg: [360, 230, 18, 0, 1, 0], appr: [380, 110, 22, 0, 1, 0],
    sign: [320, 150, 22, 1, 0, 0], track: [360, 200, 18, 0, 1, 0], toast: [320, 60, 30, 1, 0, 0]
  };
  var shapeT = track([[0, S.doc], [2.3, S.neg], [5.3, S.appr], [7.9, S.sign], [10.4, S.track], [13.4, S.toast], [15.3, S.doc]]);
  var curT = track([[0, [470, 470]], [1.2, [420, 420]], [3.0, [440, 330]], [4.2, [470, 440]],
                    [5.8, [218, 318]], [6.4, [300, 318]], [7.0, [396, 318]], [7.6, [470, 440]],
                    [8.1, [230, 318]], [9.6, [470, 450]], [15.2, [470, 470]]], 1.7, 0.9);
  var PRESS = [3.4, 6.0, 6.6, 7.2, 8.3];
  var VIS = {
    doc: [[2.2, 0], [15.4, 1]], neg: [[2.4, 1], [5.2, 0]], appr: [[5.4, 1], [7.8, 0]],
    sign: [[8.0, 1], [10.3, 0]], track: [[10.5, 1], [13.3, 0]], toast: [[13.5, 1], [15.2, 0]]
  };
  var visT = {};
  Object.keys(VIS).forEach(function (k) { visT[k] = track(VIS[k], 3.2, 1); });
  var strikeT = track([[0, 0], [3.4, 1]], 2.4, 1);
  var insT = track([[0, 0], [3.9, 1]], 2.6, 1);
  var stepT = [track([[0, 0], [6.0, 1]], 3, 1), track([[0, 0], [6.6, 1]], 3, 1), track([[0, 0], [7.2, 1]], 3, 1)];
  var barT = [track([[0, 0], [6.1, 1]], 2.2, 1), track([[0, 0], [6.7, 1]], 2.2, 1)];
  var sigT = track([[0, 0], [8.35, 1]], 0.9, 1);
  var signedT = track([[0, 0], [9.5, 1]], 3, 1);
  var progT = [track([[0, 0], [10.8, 0.85]], 0.8, 1), track([[0, 0], [11.1, 0.4]], 0.8, 1), track([[0, 0], [11.4, 0.15]], 0.8, 1)];

  var colors = {};
  function readColors() {
    var cs = getComputedStyle(document.documentElement);
    ["--ink", "--card", "--accent"].forEach(function (v) {
      var m = cs.getPropertyValue(v).trim().replace("#", "");
      if (m.length === 3) m = m.split("").map(function (c) { return c + c; }).join("");
      colors[v] = [parseInt(m.slice(0, 2), 16), parseInt(m.slice(2, 4), 16), parseInt(m.slice(4, 6), 16)];
    });
  }
  readColors();
  document.addEventListener("sz-theme", function () { readColors(); seek(t); });
  var mq = window.matchMedia("(prefers-color-scheme: dark)");
  if (mq.addEventListener) mq.addEventListener("change", function () { readColors(); seek(t); });

  function seek(t) {
    var s = shapeT(t);
    var w = s[0], h = s[1], r = Math.min(s[2], h / 2, w / 2), sum = (s[3] + s[4] + s[5]) || 1;
    var rgb = [0, 1, 2].map(function (k) { return Math.round((colors["--ink"][k] * s[3] + colors["--card"][k] * s[4] + colors["--accent"][k] * s[5]) / sum); });
    shape.style.width = w.toFixed(2) + "px";
    shape.style.height = h.toFixed(2) + "px";
    shape.style.borderRadius = r.toFixed(2) + "px";
    shape.style.background = "rgb(" + rgb.join(",") + ")";
    shape.style.transform = "translate(-50%,-50%) scale(" + (1 - bump(t, 8.3, 0.22) * 0.03).toFixed(4) + ")";
    for (var k in contents) {
      var v = c01(visT[k](t)), el = contents[k];
      el.style.opacity = v.toFixed(3);
      el.style.filter = v > 0.995 ? "none" : "blur(" + ((1 - v) * 6).toFixed(2) + "px)";
      el.style.transform = "translate(-50%,-50%) translateY(" + ((1 - v) * 5).toFixed(2) + "px)";
    }
    var sv = c01(strikeT(t));
    strike.style.transform = "scaleX(" + sv.toFixed(3) + ")";
    del.style.opacity = (1 - sv * 0.55).toFixed(3);
    var iv = c01(insT(t));
    ins.style.opacity = iv.toFixed(3);
    ins.style.transform = "translateY(" + ((1 - iv) * 6).toFixed(2) + "px)";
    for (var i = 0; i < stepEls.length; i++) {
      var on = c01(stepT[i](t));
      stepEls[i].style.setProperty("--on", on.toFixed(3));
      stepEls[i].classList.toggle("is-on", on > 0.5);
    }
    for (var j = 0; j < bars.length; j++) bars[j].style.transform = "scaleX(" + c01(barT[j](t)).toFixed(3) + ")";
    sig.style.strokeDashoffset = (1 - c01(sigT(t))).toFixed(3);
    var sd = c01(signedT(t));
    signed.style.opacity = sd.toFixed(3);
    signed.style.transform = "scale(" + (0.9 + sd * 0.1).toFixed(3) + ")";
    for (var q = 0; q < progs.length; q++) progs[q].style.transform = "scaleX(" + c01(progT[q](t)).toFixed(3) + ")";

    var p = curT(t), cp = 0, rip = null;
    for (var x = 0; x < PRESS.length; x++) {
      cp = Math.max(cp, bump(t, PRESS[x], 0.2));
      var dt = t - PRESS[x];
      if (dt >= 0 && dt < 0.5) rip = dt / 0.5;
    }
    cursor.style.transform = "translate(" + (p[0] - 5).toFixed(2) + "px," + (p[1] - 3).toFixed(2) + "px) scale(" + (1 - cp * 0.16).toFixed(4) + ")";
    if (rip !== null) {
      ripple.style.opacity = (1 - rip).toFixed(3);
      ripple.style.transform = "translate(" + p[0].toFixed(2) + "px," + p[1].toFixed(2) + "px) scale(" + (0.3 + rip * 0.9).toFixed(3) + ")";
    } else ripple.style.opacity = "0";
  }

  function fit() { scene.style.transform = "scale(" + (root.clientWidth / 600) + ")"; }
  fit();
  if (window.ResizeObserver) new ResizeObserver(fit).observe(root); else window.addEventListener("resize", fit);

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var t = 0, last = null, visible = false, raf = null;
  function paused() { return document.documentElement.classList.contains("motion-paused") || reduce.matches; }
  function frame(now) {
    raf = null;
    if (last !== null) t = (t + Math.min(0.05, (now - last) / 1000)) % L;
    last = now; seek(t); loop();
  }
  function loop() {
    var run = !paused() && visible && !document.hidden;
    if (run && raf === null) raf = requestAnimationFrame(frame);
    else if (!run) last = null;
  }
  var fixed = /[?&]reel2=([\d.]+)/.exec(location.search);
  if (fixed) t = parseFloat(fixed[1]) % L; else if (reduce.matches) t = 9.9;
  seek(t);
  new MutationObserver(function () { last = null; loop(); }).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
  document.addEventListener("visibilitychange", loop);
  if (window.IntersectionObserver) {
    new IntersectionObserver(function (es) { visible = es[0].isIntersecting && es[0].intersectionRatio > 0.5; last = null; loop(); }, { threshold: [0, 0.5, 1] }).observe(root);
  } else { visible = true; loop(); }
  if (fixed) { document.documentElement.classList.add("motion-paused"); }
})();
