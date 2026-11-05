/* Renders portfolio.html from portfolio-data.js. You normally never edit this file. */
(function () {
  'use strict';
  var data = window.TCM_PORTFOLIO || { types: {}, items: [], clients: [] };
  var gallery = document.getElementById('gallery');
  var filters = document.getElementById('filters');
  var clientsEl = document.getElementById('clients');
  var lb = document.getElementById('lb');
  var lbBox = document.getElementById('lb-box');
  var lastFocus = null;
  var active = 'all';

  var PLAY = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
  var ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>';

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  function thumbUrl(it) {
    if (it.image) return it.image;
    if (it.driveThumbId) return 'https://drive.google.com/thumbnail?id=' + encodeURIComponent(it.driveThumbId) + '&sz=w800';
    if (it.youtubeId) return 'https://i.ytimg.com/vi/' + encodeURIComponent(it.youtubeId) + '/hqdefault.jpg';
    return '';
  }

  function embedUrl(it) {
    if (it.driveVideoId) return 'https://drive.google.com/file/d/' + encodeURIComponent(it.driveVideoId) + '/preview';
    if (it.youtubeId) return 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(it.youtubeId) + '?autoplay=1&rel=0';
    return '';
  }

  function openLightbox(it) {
    lbBox.textContent = '';
    var src = embedUrl(it);
    if (src) {
      var f = document.createElement('iframe');
      f.src = src;
      f.title = it.title || 'Video';
      f.allow = 'autoplay; fullscreen';
      f.allowFullscreen = true;
      lbBox.appendChild(f);
    } else if (it.image) {
      var im = document.createElement('img');
      im.src = it.image;
      im.alt = it.title || '';
      lbBox.appendChild(im);
    } else return;
    lastFocus = document.activeElement;
    lb.classList.add('open');
    lb.querySelector('.lb-x').focus();
  }
  function closeLightbox() {
    lb.classList.remove('open');
    lbBox.textContent = '';
    if (lastFocus) lastFocus.focus();
  }
  lb.addEventListener('click', function (e) { if (e.target === lb || e.target.closest('.lb-x')) closeLightbox(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && lb.classList.contains('open')) closeLightbox(); });

  function tile(it) {
    var isLink = !!it.url && !embedUrl(it);
    var node = el(isLink ? 'a' : 'button', 'work');
    if (isLink) { node.href = it.url; node.target = '_blank'; node.rel = 'noopener'; }
    else { node.type = 'button'; node.addEventListener('click', function () { openLightbox(it); }); }
    node.setAttribute('aria-label', (it.title || 'Portfolio item') + (embedUrl(it) ? ' — play video' : isLink ? ' — open website' : ' — enlarge'));

    var img = el('div', 'work-img' + (it.type === 'video' || it.type === 'poster' || it.type === 'event' ? ' cover' : ''));
    var t = thumbUrl(it);
    if (t) img.style.backgroundImage = 'url("' + t.replace(/"/g, '%22') + '")';
    node.appendChild(img);

    if (it.title || it.sub) {
      var meta = el('div', 'work-meta');
      if (it.title) meta.appendChild(el('div', 'work-title', it.title));
      if (it.sub) meta.appendChild(el('div', 'work-sub', it.sub));
      node.appendChild(meta);
    }
    if (embedUrl(it) || isLink) {
      var badge = el('span', 'work-play');
      badge.innerHTML = embedUrl(it) ? PLAY : ARROW;
      node.appendChild(badge);
    }
    return node;
  }

  function render() {
    gallery.textContent = '';
    var shown = data.items.filter(function (it) { return active === 'all' || it.type === active; });
    if (!shown.length) {
      gallery.appendChild(el('div', 'gallery-empty', 'New work is coming soon. Message us on WhatsApp to see more.'));
      return;
    }
    shown.forEach(function (it) { gallery.appendChild(tile(it)); });
  }

  function buildFilters() {
    var present = {};
    data.items.forEach(function (it) { present[it.type] = true; });
    var keys = Object.keys(data.types).filter(function (k) { return present[k]; });
    // Types used by items but missing from `types` still get a tab.
    Object.keys(present).forEach(function (k) { if (keys.indexOf(k) < 0) keys.push(k); });
    var all = [['all', 'All']].concat(keys.map(function (k) { return [k, data.types[k] || k]; }));
    filters.textContent = '';
    all.forEach(function (pair, i) {
      var b = el('button', '', pair[1]);
      b.type = 'button';
      b.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
      b.addEventListener('click', function () {
        active = pair[0];
        Array.prototype.forEach.call(filters.children, function (c) { c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
        render();
      });
      filters.appendChild(b);
    });
  }

  function buildClients() {
    clientsEl.textContent = '';
    data.clients.forEach(function (c) {
      var d = el('div', 'client');
      d.setAttribute('role', 'img');
      d.setAttribute('aria-label', c.name);
      d.title = c.name;
      d.style.backgroundImage = 'url("' + c.logo.replace(/"/g, '%22') + '")';
      clientsEl.appendChild(d);
    });
  }

  buildFilters();
  render();
  buildClients();
})();
