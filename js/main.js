(function () {
  "use strict";

  var CONFIG = {
    phone: "+15037175744",
    phoneDisplay: "(503) 717-5744",
    storageKey: "river-inn-at-seaside-holds",
    cloudbeds: "https://hotels.cloudbeds.com/reservation/pVXpz4"
  };

  var yearEls = document.querySelectorAll("[data-year]");
  var thisYear = String(new Date().getFullYear());
  yearEls.forEach(function (el) {
    el.textContent = thisYear;
  });

  var header = document.querySelector(".site-header");
  if (header) {
    var syncHeader = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    syncHeader();
    window.addEventListener("scroll", syncHeader, { passive: true });
  }

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
      document.body.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
        document.body.classList.remove("nav-open");
      });
    });
  }

  function ymdLocal(date) {
    var y = date.getFullYear();
    var m = String(date.getMonth() + 1).padStart(2, "0");
    var d = String(date.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + d;
  }

  function parseYmd(value) {
    if (!value) return null;
    var parts = value.split("-");
    if (parts.length !== 3) return null;
    var dt = new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
    return isNaN(dt.getTime()) ? null : dt;
  }

  function addDays(date, days) {
    var next = new Date(date.getTime());
    next.setDate(next.getDate() + days);
    return next;
  }

  var checkin = document.querySelector("[name='checkin']");
  var checkout = document.querySelector("[name='checkout']");
  if (checkin && checkout) {
    var today = ymdLocal(new Date());
    checkin.min = today;
    if (!checkin.value || checkin.value < today) checkin.value = today;
    var minOut = ymdLocal(addDays(parseYmd(checkin.value) || new Date(), 1));
    checkout.min = minOut;
    if (!checkout.value || checkout.value <= checkin.value) checkout.value = minOut;

    checkin.addEventListener("change", function () {
      var inDate = parseYmd(checkin.value) || new Date();
      var next = ymdLocal(addDays(inDate, 1));
      checkout.min = next;
      if (!checkout.value || checkout.value <= checkin.value) checkout.value = next;
    });
  }

  var params = new URLSearchParams(window.location.search);
  ["checkin", "checkout", "guests", "room"].forEach(function (key) {
    var fromUrl = params.get(key);
    var fieldName = key === "room" ? "roomType" : key;
    var field = document.querySelector("[name='" + fieldName + "']");
    if (fromUrl && field && !field.value) field.value = fromUrl;
  });

  var recap = document.querySelector("[data-date-recap]");
  if (recap) {
    var inVal = params.get("checkin");
    var outVal = params.get("checkout");
    var guests = params.get("guests");
    var room = params.get("room");
    if (inVal || outVal) {
      recap.textContent =
        "Dates from the bar: " +
        (inVal || "—") +
        " to " +
        (outVal || "—") +
        (guests ? " · " + guests + " guest" + (guests === "1" ? "" : "s") : "") +
        (room ? " · " + room : "") +
        ". Live rates open on Cloudbeds — this page does not quote a nightly price.";
    }
  }

  var cloudbedsLink = document.querySelector("[data-cloudbeds]");
  if (cloudbedsLink) {
    var url = CONFIG.cloudbeds;
    var qs = [];
    if (params.get("checkin")) qs.push("checkin=" + encodeURIComponent(params.get("checkin")));
    if (params.get("checkout")) qs.push("checkout=" + encodeURIComponent(params.get("checkout")));
    if (params.get("room")) qs.push("room=" + encodeURIComponent(params.get("room")));
    if (qs.length) url += (url.indexOf("?") >= 0 ? "&" : "?") + qs.join("&");
    cloudbedsLink.setAttribute("href", url);
  }

  function setError(field, message) {
    var wrap = field.closest(".field");
    if (!wrap) return;
    var err = wrap.querySelector(".field-error");
    field.setAttribute("aria-invalid", message ? "true" : "false");
    if (err) err.textContent = message || "";
  }

  function validEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  function validPhone(value) {
    var digits = value.replace(/\D/g, "");
    if (digits.length === 11 && digits.charAt(0) === "1") digits = digits.slice(1);
    return digits.length === 10;
  }

  var form = document.querySelector("#hold-form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var name = form.querySelector("[name='name']");
      var phone = form.querySelector("[name='phone']");
      var email = form.querySelector("[name='email']");
      var ok = true;

      if (!name.value.trim()) {
        setError(name, "Name is required.");
        ok = false;
      } else setError(name, "");

      if (!validPhone(phone.value)) {
        setError(phone, "Use a 10-digit U.S. phone number.");
        ok = false;
      } else setError(phone, "");

      if (!validEmail(email.value)) {
        setError(email, "Enter a valid email.");
        ok = false;
      } else setError(email, "");

      if (checkin && checkout && checkout.value <= checkin.value) {
        setError(checkout, "Check-out must be after check-in.");
        ok = false;
      }

      if (!ok) return;

      var data = {};
      new FormData(form).forEach(function (value, key) {
        data[key] = String(value).trim();
      });
      if (checkin) data.checkin = checkin.value;
      if (checkout) data.checkout = checkout.value;
      var guestsField = document.querySelector("[name='guests']");
      if (guestsField) data.guests = guestsField.value;
      data.savedAt = new Date().toISOString();
      try {
        var existing = JSON.parse(localStorage.getItem(CONFIG.storageKey) || "[]");
        existing.push(data);
        localStorage.setItem(CONFIG.storageKey, JSON.stringify(existing));
      } catch (err) {
        /* storage may be blocked; the recap still shows */
      }

      var success = document.querySelector("#hold-success");
      var recapBox = document.querySelector("[data-hold-recap]");
      if (recapBox) {
        recapBox.textContent =
          data.name +
          " · " +
          data.phone +
          " · " +
          (data.checkin || "") +
          " to " +
          (data.checkout || "") +
          (data.roomType ? " · " + data.roomType : "") +
          ". This is a hold request only — call the desk or finish on Cloudbeds to confirm.";
      }
      form.classList.add("is-hidden");
      if (success) success.classList.add("is-visible");
    });
  }
})();
