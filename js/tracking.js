/**
 * FullOfJoy — GA4 Conversion Tracking
 * =====================================
 * Traccia tutti gli eventi di conversione tramite event delegation
 * sul document. Non usa inline onclick, non blocca il caricamento.
 *
 * Prerequisiti: gtag.js deve essere già caricato (è nel <head> di ogni pagina).
 * ID proprietà: G-C4D3CFZRBG
 *
 * Eventi tracciati:
 *   click_whatsapp          → ogni link href*="wa.me"
 *   click_phone             → ogni link href^="tel:"
 *   click_email             → ogni link href^="mailto:"
 *   cta_valutazione_click   → link/bottoni con classe .btn--primary
 *   service_page_cta_click  → CTA nelle pagine servizio
 *   form_submit             → invio form .foj-form (successo Formspree)
 *
 * Come aggiungere un evento nuovo:
 *   Nel delegatore sottostante, aggiungi un blocco else if con il
 *   selettore CSS e chiama fojTrack(nome_evento, { params }).
 */
(function () {
  'use strict';

  // ── Helper: invia evento GA4 (no-op se gtag non disponibile) ────────────
  function fojTrack(eventName, params) {
    if (typeof gtag !== 'function') return;
    gtag('event', eventName, Object.assign({
      event_category: 'engagement',
      page_path: window.location.pathname,
    }, params));
  }

  // ── Ricava testo leggibile dal link ──────────────────────────────────────
  function linkLabel(el) {
    return (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0, 100);
  }

  // ── Rileva pagina corrente ───────────────────────────────────────────────
  var path = window.location.pathname;

  // ── Event delegation su tutto il documento ───────────────────────────────
  document.addEventListener('click', function (e) {
    var el = e.target;

    // Risali fino a trovare un <a> o <button> (max 5 livelli)
    for (var i = 0; i < 5; i++) {
      if (!el || el === document.body) break;
      if (el.tagName === 'A' || el.tagName === 'BUTTON') break;
      el = el.parentElement;
    }
    if (!el) return;

    var href = el.getAttribute('href') || '';

    // ── WhatsApp ────────────────────────────────────────────────────────────
    if (href.indexOf('wa.me') !== -1) {
      fojTrack('click_whatsapp', {
        event_category: 'conversion',
        event_label: 'WhatsApp',
      });
      return;
    }

    // ── Telefono ────────────────────────────────────────────────────────────
    if (href.indexOf('tel:') === 0) {
      fojTrack('click_phone', {
        event_category: 'conversion',
        event_label: href.replace('tel:', ''),
      });
      return;
    }

    // ── Email ───────────────────────────────────────────────────────────────
    if (href.indexOf('mailto:') === 0) {
      fojTrack('click_email', {
        event_category: 'conversion',
        event_label: href.replace('mailto:', ''),
      });
      return;
    }

    // ── CTA "Prenota una valutazione" (btn--primary) ────────────────────────
    if (el.classList && el.classList.contains('btn--primary')) {
      // Distingue CTA globale da CTA in pagine servizio
      var isServicePage = path.indexOf('/servizi/') !== -1;
      var eventName = isServicePage ? 'service_page_cta_click' : 'cta_valutazione_click';

      fojTrack(eventName, {
        event_category: 'conversion',
        event_label: linkLabel(el),
        service_page: isServicePage ? path : undefined,
      });
      return;
    }
  }, true); // useCapture: true per intercettare anche link che navigano via

  // ── Form submit — successo Formspree ────────────────────────────────────
  // main.js gestisce già il submit; qui ascoltiamo l'evento custom
  // lanciato da main.js oppure intercettiamo il form direttamente.
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('.foj-form');
    if (!form) return;

    // Patch: intercetta il reset del form (segnale di successo in main.js)
    var origReset = form.reset.bind(form);
    form.reset = function () {
      origReset();
      fojTrack('form_submit', {
        event_category: 'conversion',
        event_label: 'Contact Form — success',
      });
    };
  });

})();
