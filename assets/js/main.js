/* Akan's YTA Program — minimal front-end behaviour.
   No third-party scripts, no cookies, no analytics (analytics must load only
   after consent — see README). */
(function () {
  "use strict";

  /* ---- Site settings (becomes a WordPress site option later) ---- */
  var CONFIG = {
    quickExit: false,                       // OFF by default. Enable only if stakeholders approve.
    quickExitUrl: "https://www.google.ca/"  // neutral page the quick exit sends people to
  };

  /* ---- Mobile menu ---- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /* ---- Quick exit (optional) ---- */
  var qe = document.querySelector(".quick-exit");
  if (qe && CONFIG.quickExit) {
    qe.classList.add("is-enabled");
    var leave = function () {
      window.open(CONFIG.quickExitUrl, "_blank", "noopener");
      window.location.replace(CONFIG.quickExitUrl);
    };
    qe.addEventListener("click", leave);
    var escCount = 0, escTimer;
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      escCount++;
      clearTimeout(escTimer);
      escTimer = setTimeout(function () { escCount = 0; }, 800);
      if (escCount >= 3) leave();
    });
  }

  /* ---- Resource directory filter (client side) ---- */
  var bar = document.querySelector("[data-filter-bar]");
  if (bar) {
    var items = Array.prototype.slice.call(document.querySelectorAll("[data-category]"));
    var status = document.getElementById("filter-status");
    bar.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-filter]");
      if (!btn) return;
      var f = btn.getAttribute("data-filter");
      bar.querySelectorAll("button").forEach(function (b) {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      var shown = 0;
      items.forEach(function (it) {
        var match = f === "all" || it.getAttribute("data-category") === f;
        it.hidden = !match;
        if (match) shown++;
      });
      if (status) status.textContent = "Showing " + shown + " resource" + (shown === 1 ? "" : "s") + ".";
    });
  }

  /* ---- Forms (prototype: validate only; nothing is sent or stored) ----
     Real handlers live in the companion plugin: nonce, server-side validation,
     honeypot, email to [Program email]. Each field wrapper declares a rule:
     data-rule = text | contact | radio | long | checkbox. No rule = optional. */
  var rules = {
    text: function (w) { return w.querySelector("input").value.trim() !== ""; },
    contact: function (w) {
      var v = w.querySelector("input").value.trim();
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || v.replace(/\D/g, "").length >= 10;
    },
    radio: function (w) { return !!w.querySelector("input:checked"); },
    long: function (w) { return w.querySelector("textarea").value.trim().length >= 5; },
    checkbox: function (w) { return w.querySelector("input").checked; }
  };
  document.querySelectorAll("form[data-validate]").forEach(function (form) {
    var statusEl = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      statusEl.className = "form-status";
      if (form.website && form.website.value) return; // honeypot tripped: silently drop
      var firstBad = null;
      form.querySelectorAll("[data-rule]").forEach(function (wrap) {
        var ok = rules[wrap.getAttribute("data-rule")](wrap);
        wrap.setAttribute("data-invalid", String(!ok));
        var input = wrap.querySelector("input, select, textarea");
        if (input) input.setAttribute("aria-invalid", String(!ok));
        if (!ok && !firstBad) firstBad = input;
      });
      if (firstBad) {
        statusEl.className = "form-status form-status--err";
        statusEl.textContent = "Please fix the highlighted fields and try again.";
        firstBad.focus();
        return;
      }
      statusEl.className = "form-status form-status--ok";
      statusEl.textContent =
        "Prototype only: your message was not sent. The live form will email the program team once it is connected.";
    });
  });

  /* ---- Event calendar ----
     Events come from window.YTA_EVENTS = [{date:"YYYY-MM-DD", title, time, place, url}].
     In WordPress this list is generated from an "event" post type. */
  var cal = document.getElementById("calendar");
  if (cal) {
    var events = window.YTA_EVENTS || [];
    var view = new Date(); view.setDate(1);
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    var title = document.getElementById("cal-title");
    var body = cal.querySelector("tbody");
    var listEl = document.getElementById("event-list");
    var esc = function (t) { var d = document.createElement("div"); d.textContent = t; return d.innerHTML; };
    var draw = function () {
      var y = view.getFullYear(), m = view.getMonth();
      title.textContent = months[m] + " " + y;
      var first = new Date(y, m, 1).getDay(), count = new Date(y, m + 1, 0).getDate();
      var html = "", day = 1;
      for (var r = 0; r < 6 && day <= count; r++) {
        html += "<tr>";
        for (var c = 0; c < 7; c++) {
          if ((r === 0 && c < first) || day > count) { html += "<td class=\"is-empty\"></td>"; continue; }
          var key = y + "-" + String(m + 1).padStart(2, "0") + "-" + String(day).padStart(2, "0");
          var hits = events.filter(function (ev) { return ev.date === key; });
          var label = days[c] + " " + months[m] + " " + day + (hits.length ? ", " + hits.length + " event" + (hits.length > 1 ? "s" : "") : "");
          html += "<td" + (hits.length ? " class=\"has-event\"" : "") + "><span aria-label=\"" + label + "\">" + day + "</span>" +
            hits.map(function (h) { return "<span class=\"cal-event\">" + esc(h.title) + "</span>"; }).join("") + "</td>";
          day++;
        }
        html += "</tr>";
      }
      body.innerHTML = html;
    };
    var today = new Date().toISOString().slice(0, 10);
    var upcoming = events.filter(function (ev) { return ev.date >= today; })
      .sort(function (a, b) { return a.date < b.date ? -1 : 1; });
    if (upcoming.length && listEl) {
      listEl.innerHTML = upcoming.map(function (ev) {
        return "<li class=\"card\"><p class=\"tag-date\">" + esc(ev.date) + (ev.time ? " &middot; " + esc(ev.time) : "") + "</p><h3>" +
          esc(ev.title) + "</h3>" + (ev.place ? "<p>" + esc(ev.place) + "</p>" : "") + "</li>";
      }).join("");
    }
    document.getElementById("cal-prev").addEventListener("click", function () { view.setMonth(view.getMonth() - 1); draw(); });
    document.getElementById("cal-next").addEventListener("click", function () { view.setMonth(view.getMonth() + 1); draw(); });
    draw();
  }

  /* ---- Gentle scroll reveal (skipped for reduced motion; content shows without JS) ---- */
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll(".card, .steps li, .section__head, .photo-ph, .statement p").forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight) return;   // already on screen: never hide
      el.classList.add("reveal");
      io.observe(el);
    });
  }

  /* ---- Donation form (prototype: selects and checks only; no payment, nothing sent) ---- */
  var give = document.getElementById("give-form");
  if (give) {
    var freqBtns = [].slice.call(give.querySelectorAll("[data-freq]"));
    var amtBtns = [].slice.call(give.querySelectorAll("[data-amount]"));
    var other = document.getElementById("g-other");
    var err = document.getElementById("g-err");
    var focusBox = document.getElementById("g-focus");
    var areas = document.getElementById("g-areas");
    var gStatus = document.getElementById("give-status");
    var press = function (group, btn) {
      group.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
    };
    freqBtns.forEach(function (b) { b.addEventListener("click", function () { press(freqBtns, b); }); });
    amtBtns.forEach(function (b) {
      b.addEventListener("click", function () { press(amtBtns, b); other.value = ""; err.hidden = true; other.removeAttribute("aria-invalid"); });
    });
    other.addEventListener("input", function () { press(amtBtns, null); err.hidden = true; other.removeAttribute("aria-invalid"); });
    focusBox.addEventListener("change", function () { areas.hidden = !focusBox.checked; });
    give.addEventListener("submit", function (e) {
      e.preventDefault();
      gStatus.className = "form-status";
      var picked = amtBtns.filter(function (b) { return b.getAttribute("aria-pressed") === "true"; })[0];
      var amount = picked ? Number(picked.getAttribute("data-amount")) : parseFloat(other.value.replace(/[$,\s]/g, ""));
      if (!(amount > 0)) {
        err.hidden = false; other.setAttribute("aria-invalid", "true"); other.focus(); return;
      }
      var area = give.querySelector('input[name="area"]:checked');
      if (focusBox.checked && !area) {
        gStatus.className = "form-status form-status--err";
        gStatus.textContent = "Please choose an area of support, or untick the box.";
        return;
      }
      var freq = freqBtns.filter(function (b) { return b.getAttribute("aria-pressed") === "true"; })[0].getAttribute("data-freq");
      gStatus.className = "form-status form-status--ok";
      gStatus.textContent = "You chose $" + amount.toFixed(2).replace(/\.00$/, "") + (freq === "monthly" ? " monthly" : ", once") +
        (focusBox.checked ? ", for " + area.value : "") + ". Prototype only: the payment step is not connected, so nothing was charged or sent.";
    });
  }

  /* ---- Dropdown navigation (disclosure pattern) ----
     Button toggles its list. Enter/Space open it, Tab walks the links, Esc closes
     and returns focus. On desktop it also opens on hover and closes on mouse-out. */
  var triggers = [].slice.call(document.querySelectorAll(".nav-trigger"));
  var desktop = window.matchMedia("(min-width: 1041px)");
  var closeAll = function (except) {
    triggers.forEach(function (t) { if (t !== except) t.setAttribute("aria-expanded", "false"); });
  };
  triggers.forEach(function (t) {
    var li = t.parentElement, timer;
    t.addEventListener("click", function () {
      var open = t.getAttribute("aria-expanded") === "true";
      closeAll(t);
      t.setAttribute("aria-expanded", String(!open));
    });
    li.addEventListener("mouseenter", function () {
      if (!desktop.matches) return;
      clearTimeout(timer); closeAll(t); t.setAttribute("aria-expanded", "true");
    });
    li.addEventListener("mouseleave", function () {
      if (!desktop.matches) return;
      timer = setTimeout(function () { t.setAttribute("aria-expanded", "false"); }, 180);
    });
    li.addEventListener("focusout", function (e) {
      if (!li.contains(e.relatedTarget)) t.setAttribute("aria-expanded", "false");
    });
    li.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && t.getAttribute("aria-expanded") === "true") {
        e.stopPropagation();
        t.setAttribute("aria-expanded", "false");
        t.focus();
      }
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-sub")) closeAll();
  });
})();
