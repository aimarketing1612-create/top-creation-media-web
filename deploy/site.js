/* Top Creation Media — shared behaviour for inner pages. No dependencies. */
(function () {
  'use strict';

  // ---- Scroll reveal (content stays visible if JS or IntersectionObserver is missing)
  var els = Array.prototype.slice.call(document.querySelectorAll('[data-rv]'));
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
    // Safety net: anything already on screen after load is shown.
    setTimeout(function () {
      els.forEach(function (el) {
        if (el.classList.contains('in')) return;
        if (el.getBoundingClientRect().top < window.innerHeight * 1.1) el.classList.add('in');
      });
    }, 1200);
  }

  // ---- Tabs: <div role="tablist"> buttons[role=tab][aria-controls] + [role=tabpanel]
  function initTabs(list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;

    function select(tab, focus, silent) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
      if (!silent && history.replaceState) history.replaceState(null, '', '#' + tab.getAttribute('aria-controls'));
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab, false); });
      tab.addEventListener('keydown', function (e) {
        var next = null;
        if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
        else if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
        else if (e.key === 'Home') next = tabs[0];
        else if (e.key === 'End') next = tabs[tabs.length - 1];
        if (next) { e.preventDefault(); select(next, true); }
      });
    });

    // Deep link: marketing-classes.html#tiktok opens the TikTok tab.
    var hash = (location.hash || '').slice(1);
    var initial = tabs.filter(function (t) { return t.getAttribute('aria-controls') === hash; })[0]
      || tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0]
      || tabs[0];
    select(initial, false, true);
  }
  Array.prototype.forEach.call(document.querySelectorAll('[role="tablist"]'), initTabs);

  // ---- Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
