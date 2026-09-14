/**
 * FullOfJoy — Banner cookie e caricamento condizionato di Google Analytics
 * =======================================================================
 * GA4 (gtag.js) NON viene caricato finché l'utente non accetta i cookie
 * analitici: senza consenso non parte nessuna richiesta verso Google.
 *
 * - La scelta è salvata in localStorage ("foj_consent": "granted" | "denied")
 *   e vale 6 mesi; poi il banner viene riproposto.
 * - Il link "Preferenze cookie" nel footer (data-cookie-prefs) riapre il banner.
 * - Il markup del banner è generato qui, così non va copiato in ogni pagina.
 *
 * Nell'<head> di ogni pagina resta solo lo stub:
 *   window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);}
 * così tracking.js può chiamare gtag() anche se GA non è caricato (eventi ignorati).
 */
(function () {
  'use strict';
  var GA_ID = 'G-C4D3CFZRBG';
  var KEY = 'foj_consent';
  var MAX_AGE = 1000 * 60 * 60 * 24 * 180; // 6 mesi

  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return null;
      var v = JSON.parse(raw);
      if (!v || !v.t || Date.now() - v.t > MAX_AGE) return null;
      return v.c;
    } catch (e) { return null; }
  }
  function write(choice) {
    try { localStorage.setItem(KEY, JSON.stringify({ c: choice, t: Date.now() })); } catch (e) { /* storage bloccato: vale per la sessione */ }
  }

  var gaLoaded = false;
  function loadGA() {
    if (gaLoaded) return;
    gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }

  var root = document.documentElement.getAttribute('data-root') || '';
  var banner = null;

  function closeBanner() {
    if (banner) { banner.remove(); banner = null; }
    document.body.classList.remove('has-cookie-banner');
  }

  function openBanner() {
    if (banner) return;
    banner = document.createElement('div');
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-modal', 'false');
    banner.setAttribute('aria-labelledby', 'cookie-title');
    banner.innerHTML =
      '<div class="cookie-banner__box">' +
        '<p class="cookie-banner__hand" aria-hidden="true">una cosa veloce, promesso</p>' +
        '<h2 id="cookie-title" class="cookie-banner__title">Cookie e statistiche</h2>' +
        '<p class="cookie-banner__text">Usiamo solo cookie tecnici e, se sei d’accordo, Google Analytics per capire quali pagine sono utili. Nessuna pubblicità, nessuna profilazione. ' +
          '<a href="' + root + 'privacy.html#cookie">Come funziona</a></p>' +
        '<div class="cookie-banner__actions">' +
          '<button type="button" class="btn btn--primary" data-consent="granted">Accetta</button>' +
          '<button type="button" class="btn btn--primary" data-consent="denied">Solo necessari</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);
    document.body.classList.add('has-cookie-banner');
    banner.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]');
      if (!b) return;
      var choice = b.getAttribute('data-consent');
      write(choice);
      if (choice === 'granted') loadGA();
      closeBanner();
    });
    // Nessuno spostamento automatico del focus: il banner non interrompe la lettura.
  }

  function init() {
    var choice = read();
    if (choice === 'granted') loadGA();
    else if (choice === null) openBanner();

    document.addEventListener('click', function (e) {
      var a = e.target.closest('[data-cookie-prefs]');
      if (!a) return;
      e.preventDefault();
      openBanner();
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
