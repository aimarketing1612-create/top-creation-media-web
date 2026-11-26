/* Webinar sign-up: upcoming sessions, validation, calendar links, WhatsApp confirm, optional Google Sheet + Calendar. */
(function () {
  'use strict';
  var f = document.getElementById('seat'); if (!f) return;
  var done = document.getElementById('wb-done');
  var D = f.dataset, ZH = (document.documentElement.lang || '').indexOf('zh') === 0;
  function L(k) { return D['l' + k.charAt(0).toUpperCase() + k.slice(1)] || ''; }  // data-l-err_phone -> dataset.lErr_phone
  var wd = +D.weekday, hm = D.time.split(':'), mins = +D.minutes, show = +D.show;

  // Upcoming sessions in Malaysia time (UTC+8), whatever the visitor's own time zone.
  function sessions() {
    var out = [], now = Date.now(), MY = 8 * 3600e3;
    var my = new Date(now + MY); // "wall clock" in Malaysia, read with UTC getters
    for (var i = 0; out.length < show && i < 60; i++) {
      var d = new Date(Date.UTC(my.getUTCFullYear(), my.getUTCMonth(), my.getUTCDate() + i, +hm[0], +hm[1]));
      if (d.getUTCDay() !== wd) continue;
      var start = d.getTime() - MY;               // real instant
      if (start - now < 2 * 3600e3) continue;     // sign-up closes 2 hours before
      out.push(start);
    }
    return out;
  }
  function fmt(t) {
    var o = { weekday: 'long', day: 'numeric', month: 'long', hour: 'numeric', minute: '2-digit', timeZone: 'Asia/Kuala_Lumpur' };
    try { return new Date(t).toLocaleString(ZH ? 'zh-CN' : 'en-MY', o) + (ZH ? '（马来西亚时间）' : ' (Malaysia time)'); } catch (e) { return new Date(t).toString(); }
  }
  var slots = f.querySelector('.wb-slots'), list = sessions();
  slots.innerHTML = list.map(function (t, i) {
    return '<label class="wb-slot"><input type="radio" name="session" value="' + t + '"' + (i === 0 ? ' checked' : '') + '><span>' + fmt(t) + '</span></label>';
  }).join('');

  function phoneOk(v) { var d = v.replace(/\D/g, '').replace(/^60/, '').replace(/^0/, ''); return /^1\d{7,9}$/.test(d) ? '60' + d : ''; }
  function iso(t) { return new Date(t).toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); }

  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var err = f.querySelector('.wb-err'), name = f.name.value.trim(), phone = phoneOk(f.phone.value), pick = f.querySelector('input[name=session]:checked');
    err.hidden = true;
    if (!name) { err.textContent = L('err_name'); err.hidden = false; f.name.focus(); return; }
    if (!phone) { err.textContent = L('err_phone'); err.hidden = false; f.phone.focus(); return; }
    var t = +pick.value, end = t + mins * 60e3, when = fmt(t);

    // Optional: save the lead to Google Sheets and Calendar through a Google Apps Script web app.
    if (D.endpoint) {
      var body = new URLSearchParams({ name: name, phone: phone, start: new Date(t).toISOString(), end: new Date(end).toISOString(), session: when, lang: ZH ? 'zh' : 'en', page: location.href });
      try { fetch(D.endpoint, { method: 'POST', mode: 'no-cors', body: body }); } catch (x) {}
    }
    if (window.fbq) try { fbq('track', 'Lead'); } catch (x) {}
    if (window.gtag) try { gtag('event', 'generate_lead', { event_category: 'webinar' }); } catch (x) {}

    var cal = 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=' + encodeURIComponent(L('evt')) + '&dates=' + iso(t) + '/' + iso(end) + '&details=' + encodeURIComponent(L('evtd')) + '&ctz=Asia/Kuala_Lumpur';
    var msg = L('msg') + '\n' + L('nm') + ': ' + name + '\n' + L('sess') + ': ' + when;
    done.querySelector('.wb-cal').href = cal;
    done.querySelector('.wb-conf').href = 'https://wa.me/' + D.phone + '?text=' + encodeURIComponent(msg);
    done.querySelector('.wb-when').textContent = when;
    f.hidden = true; done.hidden = false; done.focus();

    var box = done.querySelector('.wb-count');
    function tick() {
      var s = Math.max(0, Math.floor((t - Date.now()) / 1000));
      var parts = [[Math.floor(s / 86400), L('d')], [Math.floor(s % 86400 / 3600), L('h')], [Math.floor(s % 3600 / 60), L('m')], [s % 60, L('s')]];
      box.innerHTML = '<span class="wb-count-k">' + L('starts') + '</span>' + parts.map(function (p) { return '<span><b>' + p[0] + '</b><small>' + p[1] + '</small></span>'; }).join('');
    }
    tick(); setInterval(tick, 1000);
  });
})();
