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
  var ZH = (document.documentElement.lang || '').indexOf('zh') === 0;
  var T = ZH ? { on: '点击开声音', off: '声音已开', aon: '开启声音', aoff: '关闭声音', play: '播放视频' }
             : { on: 'Tap for sound', off: 'Sound on', aon: 'Turn sound on', aoff: 'Turn sound off', play: 'Play video' };
  var players = [];   // every autoplaying <video>, so only one has sound at a time

  // ---- Video slots: <div class="video" data-video="home"> (configured in site-media.js)
  // Browsers only allow autoplay when muted, so autoplay starts muted with an "unmute" button.
  // Reduced-motion visitors get a play button instead.
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SOUND_OFF = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4V5zM23 9l-6 6M17 9l6 6"/></svg>';
  var SOUND_ON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4V5zM15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg>';

  function ytSrc(id, auto) {
    var q = auto ? 'autoplay=1&mute=1&loop=1&playlist=' + encodeURIComponent(id) + '&playsinline=1&rel=0' : 'autoplay=1&rel=0&playsinline=1';
    return 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?' + q;
  }

  function mountMp4(box, v, auto) {
    var el = document.createElement('video');
    el.src = v.mp4; el.playsInline = true; el.setAttribute('playsinline', '');
    if (v.poster) el.poster = v.poster;
    box.textContent = '';
    box.appendChild(el);
    if (!auto) { el.controls = true; el.play(); return; }
    el.muted = true; el.loop = true; el.autoplay = true; el.preload = 'auto';
    // Videos in a [data-sound-group] share one soundtrack: one button, one audible video.
    var gRoot = box.closest ? box.closest('[data-sound-group]') : null;
    if (gRoot) {
      var g = soundGroup(gRoot);
      g.els.push(el);
      players.push({ el: el, paint: g.paint });
      el.addEventListener('click', g.toggle);
      el.style.cursor = 'pointer';
      watch(box, el);
      return;
    }
    var snd = document.createElement('button');
    snd.type = 'button'; snd.className = 'video-sound';
    function paint() {
      snd.innerHTML = (el.muted ? SOUND_OFF : SOUND_ON) + '<span>' + (el.muted ? T.on : T.off) + '</span>';
      snd.setAttribute('aria-label', el.muted ? T.aon : T.aoff);
      snd.classList.toggle('is-on', !el.muted);
    }
    function toggle() {
      el.muted = !el.muted;
      if (!el.muted) {
        players.forEach(function (p) { if (p.el !== el && !p.el.muted) { p.el.muted = true; p.paint(); } });
        el.play().catch(function () {});
      }
      paint();
    }
    paint();
    players.push({ el: el, paint: paint });
    snd.addEventListener('click', function (e) { e.stopPropagation(); toggle(); });
    el.addEventListener('click', toggle);
    el.style.cursor = 'pointer';
    box.appendChild(snd);
    watch(box, el);
  }

  // Pause and rewind when scrolled away, so the video plays from the start when the visitor comes back.
  function watch(box, el) {
    if (!('IntersectionObserver' in window)) { el.play().catch(function () {}); return; }
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { el.play().catch(function () {}); return; }
        el.pause();
        if (el.currentTime > 0) { try { el.currentTime = 0; } catch (err) {} }
      });
    }, { threshold: 0.25 }).observe(box);
  }

  function soundGroup(root) {
    if (root._tcmGroup) return root._tcmGroup;
    var g = root._tcmGroup = { els: [] };
    var wrap = document.createElement('div'); wrap.className = 'sound-group';
    var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'video-sound video-sound-group';
    wrap.appendChild(btn); root.parentNode.insertBefore(wrap, root);
    function live() { return g.els.filter(function (v) { return !v.muted; })[0]; }
    g.paint = function () {
      var on = !!live();
      btn.innerHTML = (on ? SOUND_ON : SOUND_OFF) + '<span>' + (on ? T.off : T.on) + '</span>';
      btn.setAttribute('aria-label', on ? T.aoff : T.aon);
      btn.classList.toggle('is-on', on);
    };
    g.toggle = function () {
      var cur = live();
      if (cur) { cur.muted = true; g.paint(); return; }
      var lead = g.els[0]; if (!lead) return;
      players.forEach(function (p) { if (!p.el.muted) { p.el.muted = true; p.paint(); } });
      g.els.forEach(function (v) { if (v !== lead) { try { v.currentTime = lead.currentTime; } catch (e) {} } });
      lead.muted = false; lead.play().catch(function () {});
      g.paint();
    };
    btn.addEventListener('click', g.toggle);
    g.paint();
    return g;
  }

  function mountIframe(box, src, title) {
    var f = document.createElement('iframe');
    f.src = src; f.title = title; f.allow = 'autoplay; fullscreen; picture-in-picture'; f.allowFullscreen = true;
    box.textContent = '';
    box.appendChild(f);
  }

  Array.prototype.forEach.call(document.querySelectorAll('[data-video]'), function (box) {
    var v = (media.videos || {})[box.getAttribute('data-video')] || {};
    var btn = box.querySelector('.video-btn');
    var title = box.getAttribute('aria-label') || 'Video';
    if (!v.youtubeId && !v.driveId && !v.mp4) return;
    var auto = v.autoplay !== false && !reduce && !v.driveId;
    btn.classList.remove('video-soon');
    btn.querySelector('.video-cap').textContent = T.play;
    if (v.poster) box.style.background = 'center/cover no-repeat url("' + v.poster.replace(/"/g, '%22') + '")';

    function start(autoMode) {
      if (v.mp4) mountMp4(box, v, autoMode);
      else if (v.youtubeId) mountIframe(box, ytSrc(v.youtubeId, autoMode), title);
      else mountIframe(box, 'https://drive.google.com/file/d/' + encodeURIComponent(v.driveId) + '/preview', title);
    }
    btn.addEventListener('click', function () { start(false); });
    if (!auto) return;
    // Load the video only when it is about to be seen.
    if ('IntersectionObserver' in window) {
      var io2 = new IntersectionObserver(function (es) {
        if (es.some(function (e) { return e.isIntersecting; })) { io2.disconnect(); start(true); }
      }, { rootMargin: '200px' });
      io2.observe(box);
    } else start(true);
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
      var a = document.createElement('a'); a.className = 'work'; a.href = ZH ? '/zh/portfolio' : '/portfolio';
      a.setAttribute('aria-label', (it.title || 'Portfolio item') + ', view in portfolio');
      var img = document.createElement('div'); img.className = 'work-img cover';
      var t = it.image || (it.driveThumbId ? 'https://drive.google.com/thumbnail?id=' + encodeURIComponent(it.driveThumbId) + '&sz=w800'
        : it.youtubeId ? 'https://i.ytimg.com/vi/' + encodeURIComponent(it.youtubeId) + '/hqdefault.jpg' : '');
      if (t) img.style.backgroundImage = 'url("' + t.replace(/"/g, '%22') + '")';
      if (it.type === 'dashboard') img.className = 'work-img';
      a.appendChild(img); hg.appendChild(a);
    });
  }

  // ---- Motion: scroll progress (the logo's double line) and a condensed nav after scrolling
  var bar = document.querySelector('.progress i');
  var navEl = document.querySelector('.nav');
  var ticking = false;
  function onScroll() {
    ticking = false;
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
    if (navEl) navEl.classList.toggle('is-scrolled', window.scrollY > 24);
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // ---- Motion: a soft light follows the pointer across cards (mouse only, never on touch)
  if (window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches && !reduce) {
    var SPOT = '.card,.svc,.way,.mod,.col,.stat,.plan,.index-col,.plat';
    document.addEventListener('pointermove', function (e) {
      var t = e.target.closest ? e.target.closest(SPOT) : null;
      if (!t) return;
      var r = t.getBoundingClientRect();
      t.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      t.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }

  // ---- Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
