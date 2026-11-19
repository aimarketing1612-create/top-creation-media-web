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

  var media = window.TCM_MEDIA || { videos: {}, testimonials: [] };

  // ---- Video slots: <div class="video" data-video="home"> (configured in site-media.js)
  Array.prototype.forEach.call(document.querySelectorAll('[data-video]'), function (box) {
    var v = (media.videos || {})[box.getAttribute('data-video')] || {};
    var btn = box.querySelector('.video-btn');
    var title = box.getAttribute('aria-label') || 'Video';
    var src = v.youtubeId ? 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(v.youtubeId) + '?autoplay=1&rel=0'
      : v.driveId ? 'https://drive.google.com/file/d/' + encodeURIComponent(v.driveId) + '/preview' : '';
    if (!src && !v.mp4) return;
    btn.classList.remove('video-soon');
    btn.querySelector('.video-cap').textContent = 'Play video';
    if (v.poster) box.style.background = 'center/cover no-repeat url("' + v.poster.replace(/"/g, '%22') + '")';
    btn.addEventListener('click', function () {
      var el;
      if (v.mp4) {
        el = document.createElement('video');
        el.src = v.mp4; el.controls = true; el.autoplay = true; el.playsInline = true;
        if (v.poster) el.poster = v.poster;
      } else {
        el = document.createElement('iframe');
        el.src = src; el.title = title; el.allow = 'autoplay; fullscreen; picture-in-picture'; el.allowFullscreen = true;
      }
      box.textContent = '';
      box.appendChild(el);
    });
  });

  // ---- Testimonials: hidden until real ones are added in site-media.js
  var tq = document.getElementById('testimonials');
  var list = (media.testimonials || []).filter(function (t) { return t && t.quote; });
  if (tq && list.length) {
    var grid = tq.querySelector('.quotes');
    list.forEach(function (t) {
      var card = document.createElement('figure'); card.className = 'quote';
      var p = document.createElement('p'); p.textContent = '“' + t.quote + '”';
      var who = document.createElement('figcaption'); who.className = 'quote-who';
      if (t.photo) { var im = document.createElement('img'); im.src = t.photo; im.alt = ''; who.appendChild(im); }
      var nm = document.createElement('span'); var b = document.createElement('b'); b.textContent = t.name || '';
      nm.appendChild(b); nm.appendChild(document.createTextNode(t.role || '')); who.appendChild(nm);
      card.appendChild(p); card.appendChild(who); grid.appendChild(card);
    });
    tq.hidden = false;
  }

  // ---- Home: portfolio preview from portfolio-data.js
  var hg = document.getElementById('home-gallery');
  var pf = window.TCM_PORTFOLIO;
  if (hg && pf && pf.items) {
    pf.items.slice(0, 6).forEach(function (it) {
      var a = document.createElement('a'); a.className = 'work'; a.href = '/portfolio';
      a.setAttribute('aria-label', (it.title || 'Portfolio item') + ', view in portfolio');
      var img = document.createElement('div'); img.className = 'work-img cover';
      var t = it.image || (it.driveThumbId ? 'https://drive.google.com/thumbnail?id=' + encodeURIComponent(it.driveThumbId) + '&sz=w800'
        : it.youtubeId ? 'https://i.ytimg.com/vi/' + encodeURIComponent(it.youtubeId) + '/hqdefault.jpg' : '');
      if (t) img.style.backgroundImage = 'url("' + t.replace(/"/g, '%22') + '")';
      if (it.type === 'dashboard') img.className = 'work-img';
      a.appendChild(img); hg.appendChild(a);
    });
  }

  // ---- Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
