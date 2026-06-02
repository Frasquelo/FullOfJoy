// FullOfJoy — menu mobile toggle
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.querySelector('.nav-links');
    if (!toggle || !links) return;

    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      var expanded = links.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });

    // Chiudi il menu cliccando un link (mobile)
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
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
