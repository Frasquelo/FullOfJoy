// FullOfJoy — menu mobile toggle
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.querySelector('.nav-links');
    if (!toggle || !links) return;

    function setMenu(open) {
      links.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Chiudi il menu' : 'Apri il menu');
      document.body.classList.toggle('menu-open', open);
    }

    // Evidenzia la pagina corrente nel menu (aria-current)
    var norm = function (path) { return path.replace(/\/index\.html$/, '/').replace(/\.html$/, ''); };
    var here = norm(window.location.pathname);
    links.querySelectorAll('a[href]').forEach(function (a) {
      var target = a.getAttribute('href');
      if (!target || /^(https?:|mailto:|tel:)/.test(target) || a.classList.contains('btn')) return;
      var abs = norm(new URL(target, window.location.href).pathname);
      if (abs === here) a.setAttribute('aria-current', 'page');
    });

    function isMenuOpen() {
      return links.classList.contains('open');
    }

    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setMenu(!isMenuOpen());
    });

    // Chiudi il menu cliccando un link (mobile)
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        setMenu(false);
      });
    });

    // Chiudi con ESC e con click fuori dal menu, mantenendo aria-expanded coerente
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isMenuOpen()) {
        setMenu(false);
        toggle.focus();
      }
    });

    document.addEventListener('click', function (e) {
      if (!isMenuOpen()) return;
      if (links.contains(e.target) || toggle.contains(e.target)) return;
      setMenu(false);
    });
  });
})();

// FullOfJoy — invio form contatti via AJAX (Formspree) con messaggi di esito
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('.foj-form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');

    function show(type, html) {
      if (!status) return;
      status.className = 'form-status form-status--' + type;
      status.innerHTML = html;
      status.hidden = false;
    }

    form.addEventListener('submit', function (e) {
      // Se l'endpoint non è ancora configurato, lascia il submit normale
      if (form.action.indexOf('YOUR_FORM_ID') !== -1) return;
      e.preventDefault();
      var data = new FormData(form);
      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Invio in corso…'; }

      fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          form.reset();
          show('ok', '<strong>Grazie! Abbiamo ricevuto il tuo messaggio.</strong><br>Ti ricontatteremo il prima possibile. Se preferisci, puoi scriverci subito anche su WhatsApp.');
          document.dispatchEvent(new CustomEvent('foj:form-success', {
            detail: { formType: 'contact', provider: 'formspree' }
          }));
        } else {
          throw new Error('bad response');
        }
      }).catch(function () {
        show('err', '<strong>Ops, qualcosa non ha funzionato.</strong><br>Puoi riprovare oppure scriverci direttamente su <a href="https://wa.me/393283529976" target="_blank" rel="noopener">WhatsApp</a>.');
      }).finally(function () {
        if (btn) { btn.disabled = false; btn.textContent = label; }
      });
    });
  });
})();
