"""Builds every page of www.topcreationmedia.com into deploy/.

Run:  python3 tools/build_site.py
Edit the text below, run it again, commit. Videos and testimonials live in
deploy/site-media.js, portfolio items in deploy/portfolio-data.js, and
behind-the-scenes photos in deploy/assets/bts/ (see the README there).
"""
import html as H
import json
import os
from PIL import Image
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'deploy')
SITE = 'https://www.topcreationmedia.com/'  # main domain; topcreation.media redirects here (deploy/vercel.json)
TRACK = open(os.path.join(ROOT, 'tools', 'partials', 'tracking.html'), encoding='utf8').read().strip()

PHONE = '60127816121'
CONV = "if (window.gtag) gtag('event', 'conversion', {'send_to':'AW-18334047674/RhA_CIXz2OIcELq7raZE'});"


def wa(msg):
    return f'https://wa.me/{PHONE}?text={quote(msg)}'


def esc(s):
    return H.escape(s, quote=True)


WA_PATH = 'M12 2a10 10 0 0 0-8.53 15.23L2 22l4.9-1.42A10 10 0 1 0 12 2Zm5.07 14.13c-.22.62-1.28 1.2-1.78 1.24-.48.05-.93.23-3.12-.65-2.64-1.06-4.32-3.75-4.45-3.92-.13-.18-1.07-1.42-1.07-2.71 0-1.29.68-1.92.92-2.19.24-.26.52-.33.7-.33h.5c.16 0 .38-.06.59.45.22.52.74 1.8.8 1.93.07.13.11.29.02.46-.09.18-.13.28-.26.44-.13.15-.28.35-.4.47-.13.13-.27.28-.12.54.15.26.68 1.12 1.46 1.81 1 .9 1.85 1.17 2.11 1.3.26.13.42.11.57-.07.16-.17.66-.77.84-1.03.17-.26.35-.22.59-.13.24.09 1.52.71 1.78.84.26.13.43.2.5.31.06.11.06.64-.15 1.24Z'
ICON_PATHS = {
    'megaphone': 'M3 11l18-5v12L3 14v-3zM11.6 16.8a3 3 0 1 1-5.8-1.6',
    'video': 'M3 6h11a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2zM16 10l6-4v12l-6-4',
    'live': 'M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM16.24 7.76a6 6 0 0 1 0 8.49M7.76 16.24a6 6 0 0 1 0-8.49M19.07 4.93a10 10 0 0 1 0 14.14M4.93 19.07a10 10 0 0 1 0-14.14',
    'users': 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75',
    'ai': 'M5 5h14v14H5zM9 9h6v6H9zM9 2v3M15 2v3M9 19v3M15 19v3M19 9h3M19 15h3M2 9h3M2 15h3',
    'layers': 'M12 2 2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5',
    'search': 'M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.35-4.35',
    'book': 'M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2zM22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z',
    'music': 'M9 18V5l12-2v13M9 18a3 3 0 1 1-6 0 3 3 0 0 1 6 0zM21 16a3 3 0 1 1-6 0 3 3 0 0 1 6 0z',
    'pen': 'M12 19l7-7 3 3-7 7-3-3zM18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5zM2 2l7.59 7.59',
    'calendar': 'M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z',
    'zap': 'M13 2 3 14h9l-1 8 10-12h-9l1-8z',
    'coins': 'M12 8c4.97 0 9-1.34 9-3s-4.03-3-9-3-9 1.34-9 3 4.03 3 9 3zM21 12c0 1.66-4 3-9 3s-9-1.34-9-3M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5',
    'target': 'M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12zM12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
    'qr': 'M3 3h7v7H3zM14 3h7v7h-7zM3 14h7v7H3zM14 14h3v3h-3zM18 18h3v3h-3zM14 20h1M20 14h1',
    'sparkles': 'M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z',
    'facebook': 'M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z',
}


def icon(name):
    return f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{ICON_PATHS[name]}"/></svg></span>'


ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PLAY = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'

# ---------------------------------------------------------------- shared parts
ACADEMY_KEYS = ('academy', 'ai', 'member')
TOOL_KEYS = ('tools', 'scan', 'aivideo')


def nav(cur, slug=''):
    def on(hit):
        return ' aria-current="page"' if hit else ''

    def logo(n):
        return f'<img src="/assets/brands/{n}.svg" alt="" width="18" height="18">'

    main = f'''<div class="dd">
          <a href="/marketing-services"{on(cur == 'services')}>Services</a>
          <div class="dd-menu">
            <a class="dd-row" href="/marketing-services#facebook">{logo('meta')}Facebook &amp; Instagram</a>
            <a class="dd-row" href="/marketing-services#tiktok">{logo('tiktok')}TikTok</a>
            <a class="dd-row" href="/marketing-services#xiaohongshu">{logo('xiaohongshu')}Xiaohongshu</a>
            <a class="dd-row" href="/marketing-services#google">{logo('google')}Google SEO &amp; Ads</a>
            <hr>
            <a href="/marketing-services#more">AI video production</a>
            <a href="/marketing-services#more">Websites &amp; landing pages</a>
            <a href="/marketing-services#more">Video, livestream, KOL &amp; events</a>
          </div>
        </div>
        <div class="dd">
          <a href="/marketing-classes"{on(cur in ACADEMY_KEYS)}>Academy</a>
          <div class="dd-menu">
            <a href="/marketing-classes">Marketing Academy<small>Facebook, TikTok, Google, Xiaohongshu</small></a>
            <a href="/ai-classes">AI Academy<small>7 modules, no coding needed</small></a>
            <hr>
            <a class="dd-hl" href="/membership">Membership<small>Every class and AI tool, from RM250/mo</small></a>
          </div>
        </div>
        <div class="dd">
          <a href="/ai-tools"{on(cur in TOOL_KEYS)}>AI Tools</a>
          <div class="dd-menu">
            <a href="/scan-buddy">Scan Buddy<small>One QR code for followers and reviews</small></a>
            <a href="/ai-video">AI Video<small>Product photo to video ads</small></a>
          </div>
        </div>
        <a href="/insights"{on(cur == 'insights')}>Insights</a>
        <a href="/portfolio"{on(cur == 'portfolio')}>Portfolio</a>'''
    sub = [(cur == 'home', '/', 'Home'), (cur == 'services', '/marketing-services', 'Services'),
           (cur == 'academy', '/marketing-classes', 'Marketing Academy'), (cur == 'ai', '/ai-classes', 'AI Academy'),
           (cur == 'member', '/membership', 'Membership'), (cur == 'insights', '/insights', 'Insights'), (cur in TOOL_KEYS, '/ai-tools', 'AI Tools'),
           (cur == 'portfolio', '/portfolio', 'Portfolio')]
    subs = '\n        '.join(f'<a href="{h}"{on(hit)}>{l}</a>' for hit, h, l in sub)
    return f'''<a class="skip" href="#main">Skip to content</a>
  <header class="nav">
    <div class="progress" aria-hidden="true"><i></i></div>
    <div class="nav-in">
      <a class="brand" href="/" aria-label="Top Creation Media, home"><img src="/assets/tcm-wordmark.webp" alt="TCM Top Creation Media" width="960" height="401"></a>
      <nav class="nav-links" aria-label="Main">
        {main}
        <a class="lang" href="/zh/{slug}" hreflang="zh-Hans" lang="zh-Hans" data-lang-switch aria-label="中文 / English">中文</a>
        <a class="btn btn-primary btn-sm" href="{wa("Hi, I'd like a customized package!")}" onclick="{CONV}" target="_blank" rel="noopener"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg>WhatsApp Us</a>
      </nav>
    </div>
    <nav class="subnav" aria-label="Pages"><div class="subnav-in">
        {subs}
    </div></nav>
  </header>'''


FOOT = f'''<footer class="foot">
    <div style="display:flex;align-items:center;gap:10px">
      <img src="/assets/tcm-wordmark.webp" alt="" width="960" height="401" style="width:auto;height:30px">
      <span>© <span id="year">2026</span> Top Creation Media Sdn Bhd · Strategy. Execution. Growth.</span>
    </div>
    <div class="foot-links">
      <a href="/marketing-services">Services</a>
      <a href="/marketing-classes">Marketing Academy</a>
      <a href="/ai-classes">AI Academy</a>
      <a href="/membership">Membership</a>
      <a href="/ai-tools">AI Tools</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/insights">Insights</a>
      <a href="https://facebook.com/topcreationmedia" target="_blank" rel="noopener">Facebook</a>
      <a href="https://instagram.com/topcreationmedia" target="_blank" rel="noopener">Instagram</a>
      <a href="https://tiktok.com/@topcreationmedia" target="_blank" rel="noopener">TikTok</a>
    </div>
  </footer>
  <a class="wa-float" href="{wa("Hi, I'd like to know more!")}" onclick="{CONV}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="{WA_PATH}"/></svg></a>'''


def crumbs_ld(body, slug):
    """BreadcrumbList from the visible breadcrumb line of a page."""
    import re as _re
    m = _re.search(r'<div class="crumbs[^>]*>(.*?)</div>', body, _re.S)
    if not m:
        return None
    items = []
    for i, part in enumerate(m.group(1).split(' / '), 1):
        a = _re.match(r'\s*<a href="([^"]+)">(.*?)</a>\s*$', part, _re.S)
        name = H.unescape(_re.sub('<[^>]+>', '', a.group(2) if a else part)).strip()
        url = SITE + (a.group(1).lstrip('/') if a else slug)
        items.append({'@type': 'ListItem', 'position': i, 'name': name, 'item': url})
    return {'@type': 'BreadcrumbList', 'itemListElement': items}


def page(slug, title, desc, cur, ld, body, scripts=()):
    canon = SITE + slug
    bc = crumbs_ld(body, slug)
    if bc and ld:
        ld = dict(ld)
        ld['@graph'] = list(ld['@graph']) + [bc] if '@graph' in ld else [{k: v for k, v in ld.items() if k != '@context'}, bc]
        ld['@context'] = 'https://schema.org'
    tags = '\n  '.join(f'<script src="{s}"></script>' for s in ('/site-media.js', *scripts, '/site.js'))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  {TRACK}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="theme-color" content="#07051A">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="en" href="{canon}">
  <link rel="alternate" hreflang="zh-Hans" href="{SITE}zh/{slug}">
  <link rel="alternate" hreflang="x-default" href="{canon}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Top Creation Media">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}assets/tcm-logo.jpg">
  <meta property="og:image:width" content="2048">
  <meta property="og:image:height" content="2048">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="/assets/tcm-logo.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Unbounded:wght@700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/site.css">
  <script>document.documentElement.className='js'</script>
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  {nav(cur, slug)}

  <main id="main">
{body}
  </main>

  {FOOT}

  {tags}
</body>
</html>
'''


# ---------------------------------------------------------------- helpers
_MEDIA = open(os.path.join(OUT, 'site-media.js'), encoding='utf8').read()
HAS_VIDEO = {m.group(1) for m in __import__('re').finditer(r"\n\s+'?([\w-]+)'?:\s*\{ youtubeId: '([^']*)', driveId: '([^']*)', mp4: '([^']*)'", _MEDIA)
             if m.group(2) or m.group(3) or m.group(4)}


def video(key, label):
    if key not in HAS_VIDEO:   # no empty "coming soon" frames
        return ''
    return f'''<div class="video" data-video="{key}" aria-label="{esc(label)}" data-rv>
        <button class="video-btn video-soon" type="button" aria-label="{esc(label)}"><span class="play">{PLAY}</span><span class="video-cap">Video coming soon</span></button>
      </div>'''


def video9(key, label):
    return video(key, label).replace('class="video"', 'class="video v916"', 1)


def svc_cards(rows, cls='svc-grid'):
    """rows: (title, line, href, kind, src, alt). kind 'logo' shows a real brand logo, 'photo' a photograph."""
    out = []
    for t, d, href, kind, src, alt in rows:
        if kind == 'logo':
            chips = ''.join(f'<span>{esc(c)}</span>' for c in LOGO_CHIPS.get(src, ()))
            media = (f'<div class="svc-media svc-logo brand-{src}">{brand_bg(src)}<i class="orbit" aria-hidden="true"></i>'
                     f'<img src="/assets/brands/{src}.svg" alt="{esc(alt)}" width="120" height="120" loading="lazy">'
                     f'<div class="svc-chips" aria-hidden="true">{chips}</div></div>')
        else:
            w, h = IMG_DIMS.get(src, (1200, 892))
            media = f'<div class="svc-media"><img src="/assets/img/{src}.webp" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"></div>'
        out.append(f'<a class="svc" href="{href}" data-rv>{media}<div class="svc-body"><div class="card-t">{esc(t)}</div><p class="card-d">{esc(d)}</p></div></a>')
    return f'<div class="{cls}">' + '\n          '.join(out) + '</div>'


# Calm backdrop behind each platform logo: a fine dot grid and two thin rings (aria-hidden).
def brand_bg(src):
    return ('<svg class="svc-art" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            '<defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#fff" fill-opacity=".16"/></pattern>'
            '<radialGradient id="fade" cx="50%" cy="44%" r="60%"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".55" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff"/></radialGradient>'
            '<mask id="m"><rect width="400" height="300" fill="url(#fade)"/></mask></defs>'
            '<rect width="400" height="300" fill="url(#dots)" mask="url(#m)"/>'
            '<g fill="none" stroke="#fff"><circle cx="200" cy="132" r="88" stroke-opacity=".10"/><circle cx="200" cy="132" r="124" stroke-opacity=".06"/></g></svg>')


LOGO_CHIPS = {'meta': ('Ads', 'Reels', 'Leads'), 'tiktok': ('Video', 'LIVE', 'Shop'),
              'xiaohongshu': ('Notes', 'KOC', 'Search'), 'google': ('SEO', 'Ads', 'AI search')}


def banner(src, alt):
    w, h = IMG_DIMS.get(src, (1200, 678))
    return f'<figure class="banner" data-rv><img src="/assets/img/{src}.webp" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"></figure>'


PHOTO_POS = {'mission.jpg': '70% 50%'}


def photo(file, alt):
    pos = f' style="--pos:{PHOTO_POS[file]}"' if file in PHOTO_POS else ''
    return f'''<figure class="photo"{pos} data-rv>
          <div class="photo-ph"><b>Behind the scenes</b>Top Creation Media studio</div>
          <img src="/assets/bts/{file}" alt="{esc(alt)}" loading="lazy" onerror="this.remove()">
        </figure>'''


def head(h2, eyebrow='', lede='', style=''):
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ''
    ld = f'<p class="lede" data-rv style="margin-top:18px">{lede}</p>' if lede else ''
    st = f' style="{style}"' if style else ''
    return f'<div class="sec-head"{st}><div data-rv>{eb}<h2 class="h2">{h2}</h2></div>{ld}</div>'


def ticks(items):
    return '<ul class="ticks">' + ''.join(f'<li>{esc(t)}</li>' for t in items) + '</ul>'


def arches(cls=''):
    """Decorative line art taken from the logo: double-line arches that draw themselves, then a light runs along them."""
    shapes = ['M40 320V170A110 110 0 0 1 260 170V320', 'M72 320V170A78 78 0 0 1 228 170V320',
              'M260 320V170A110 110 0 0 1 480 170V320', 'M292 320V170A78 78 0 0 1 448 170V320',
              'M480 320V170A110 110 0 0 1 700 170V320', 'M512 320V170A78 78 0 0 1 668 170V320']
    base = ''.join(f'<path pathLength="1" style="--d:{i * 90}" d="{d}"/>' for i, d in enumerate(shapes))
    glint = ''.join(f'<path pathLength="1" style="--d:{i * 700}" d="{d}"/>' for i, d in enumerate(shapes[::2]))
    return (f'<svg class="arches {cls}" viewBox="0 0 740 320" fill="none" aria-hidden="true" focusable="false" data-rv>'
            '<defs><linearGradient id="tcm-line" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="740" y2="0">'
            '<stop offset="0" stop-color="#9327D2"/><stop offset=".5" stop-color="#5271E9"/><stop offset="1" stop-color="#2DB9DB"/></linearGradient></defs>'
            f'<g class="arches-base" stroke="url(#tcm-line)">{base}</g><g class="arches-glint">{glint}</g></svg>')


def hero(crumbs, h1, lede, buttons='', extra='', eyebrow=''):
    crumb = ' / '.join(f'<a href="{h}">{esc(t)}</a>' if h else esc(t) for t, h in crumbs)
    return f'''    <section class="page-hero">
      {arches('arches-side')}
      <div class="crumbs rise">{crumb}</div>
      {f'<div class="eyebrow rise">{eyebrow}</div>' if eyebrow else ''}
      <h1 class="h1 rise" style="animation-delay:.05s">{h1}</h1>
      <p class="lede rise" style="animation-delay:.2s">{lede}</p>
      {buttons}
      {extra}
    </section>'''


def btns(*pairs):
    out = []
    for i, (label, href) in enumerate(pairs):
        cls = 'btn-primary' if i == 0 else 'btn-ghost'
        ext = ' target="_blank" rel="noopener"' if href.startswith('https://wa.me') else ''
        out.append(f'<a class="btn {cls}" href="{href}"{ext}>{esc(label)}</a>')
    return '<div class="btn-row rise" style="animation-delay:.35s">' + ''.join(out) + '</div>'


def _switch(links, cur, label):
    a = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if k == cur else ""}>{l}</a>' for k, h, l in links)
    return f'<div class="switch-wrap rise" style="animation-delay:.3s"><nav class="switch" aria-label="{label}">{a}</nav></div>'


def switch(cur):
    return _switch([('academy', '/marketing-classes', 'Marketing Academy'), ('ai', '/ai-classes', 'AI Academy'),
                    ('member', '/membership', 'Membership')], cur, 'Academy sections')


def tool_switch(cur):
    return _switch([('scan', '/scan-buddy', 'Scan Buddy'), ('aivideo', '/ai-video', 'AI Video')], cur, 'AI Tools')


def member_band():
    return '''    <section class="tile tile-dark" style="padding-top:0">
      <div class="wrap">
        <div class="offer" data-rv>
          <div><b>Prefer to learn online, at your own pace?</b><span>The Membership includes every class video, every AI tool and a live class every month. From RM250 a month.</span></div>
          <a class="btn btn-ghost btn-sm" href="/membership">See the Membership</a>
        </div>
      </div>
    </section>'''


def faq_html(items):
    rows = '\n'.join(f'        <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in items)
    return f'<div class="faq" data-rv>\n{rows}\n      </div>'


def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def faq_section(items, cls='tile-dark', title='Questions, answered.'):
    return f'''    <section class="tile {cls}">
      <div style="max-width:900px;margin:0 auto">
        {head(title, 'FAQ', style='margin-bottom:48px')}
        {faq_html(items)}
      </div>
    </section>'''


def cta(h2, lede, label, msg):
    return f'''    <section class="cta" id="contact">
      {arches('arches-centre')}
      <h2 class="h2" data-rv>{h2}</h2>
      <p class="lede" data-rv>{lede}</p>
      <div class="btn-row" data-rv><a class="btn btn-primary btn-lg" href="{wa(msg)}" target="_blank" rel="noopener">{esc(label)}</a></div>
      <div class="cta-meta" data-rv><span>Malaysia · Singapore · USA</span><span>In-house video &amp; livestream studio</span><span>English · 中文 · Bahasa</span></div>
    </section>'''


def guarantee(subject):
    return f'''    <section class="tile tile-dark" id="guarantee">
      <div class="guarantee" data-rv>
        <div class="guarantee-seal">100%</div>
        <h2 class="h2">Can&#8217;t learn it? Full refund.</h2>
        <p class="lede">Follow the {subject} and do the practice tasks. If you still can&#8217;t do it yourself, we refund 100% of your fee. That is our promise: we guide you until you are the next professional marketer.</p>
        <p class="guarantee-terms">Terms apply: attend every session and complete the practice tasks. WhatsApp us for the full terms.</p>
      </div>
    </section>'''


def cards(rows, cls='grid', ics=None):
    out = []
    for n, row in enumerate(rows):
        t, d = row[0], row[1]
        links = ''
        if len(row) > 2 and row[2]:
            links = '<div class="card-links">' + ''.join(f'<a href="{h}">{esc(l)} &rarr;</a>' for l, h in row[2]) + '</div>'
        name = row[3] if len(row) > 3 and row[3] else (ics[n] if ics else '')
        ico = icon(name) if name else ''
        out.append(f'<div class="card" data-rv>{ico}<div class="card-t">{esc(t)}</div><p class="card-d">{esc(d)}</p>{links}</div>')
    return f'<div class="{cls}">' + '\n          '.join(out) + '</div>'


def modules(rows, key='You will build'):
    out = []
    for i, (t, d, build, tools) in enumerate(rows, 1):
        mid = 'm-' + '-'.join(''.join(c if c.isalnum() else ' ' for c in t.lower()).split())
        chips = ''.join(f'<span class="chip">{esc(x)}</span>' for x in tools)
        out.append(f'''        <div class="mod" id="{mid}" data-rv>
          <div class="mod-n">{i:02d}</div>
          <div><h3 class="mod-t">{esc(t)}</h3><p class="mod-d">{esc(d)}</p></div>
          <div><div class="mod-k">{key}</div><p class="mod-b">{esc(build)}</p><div class="mod-tools">{chips}</div></div>
        </div>''')
    return '\n'.join(out)


def tabs(label, panels, icons=None):
    def ic(i):
        return f'<img src="/assets/brands/{icons[i]}.svg" alt="" width="20" height="20">' if icons else ''
    buttons = ''.join(
        f'<button role="tab" id="t-{pid}" aria-controls="{pid}" aria-selected="{"true" if i == 0 else "false"}">{ic(i)}{esc(name)}</button>'
        for i, (pid, name, _) in enumerate(panels))
    bodies = '\n'.join(
        f'''      <div role="tabpanel" class="panel" id="{pid}" aria-labelledby="t-{pid}"{"" if i == 0 else " hidden"}>
{html}
      </div>''' for i, (pid, name, html) in enumerate(panels))
    return f'''        <div class="seg-wrap" data-rv>
          <div class="seg" role="tablist" aria-label="{esc(label)}">{buttons}</div>
        </div>
{bodies}'''


def panel_intro(h3, lede):
    return f'        <div class="panel-intro"><h3 class="h3">{h3}</h3><p class="lede">{lede}</p></div>'


ORG_ID = SITE + '#org'
PROVIDER = {'@type': 'Organization', '@id': ORG_ID, 'name': 'Top Creation Media', 'url': SITE}
STEPS3 = '''        <div class="cols">
          <div class="col" data-rv><div class="col-n">1</div><div class="col-t">Strategy &amp; discussion</div><p class="col-d">We study your market, define the offer and agree the goals before a single asset is made.</p></div>
          <div class="col" data-rv><div class="col-n">2</div><div class="col-t">Planning &amp; approval</div><p class="col-d">Content calendar, creative direction and media plan, mapped, budgeted and signed off with you.</p></div>
          <div class="col" data-rv><div class="col-n">3</div><div class="col-t">Execution &amp; growth</div><p class="col-d">Our studio produces, campaigns launch, and we optimise every week: scale what works, stop what doesn&#8217;t.</p></div>
        </div>'''

CLIENTS = [('3cat.jpeg', '3cat'), ('hairology.png', 'Hairology 丝域养发'), ('mobil.jpg', 'Mobil'), ('tcl.png', 'TCL'), ('nescafe.jpg', 'Nescafé'),
           ('nomi.png', 'NOMI'), ('tp-link.png', 'TP-Link'), ('polo-club.jpeg', 'Royal County of Berkshire Polo Club'),
           ('golden-tropics.jpeg', 'Golden Tropics'), ('joy-paradise.jpg', 'Joy Paradise'), ('lau-homecook.png', 'Lau Homecook'),
           ('sofei.png', 'SOFEI'), ('haroma.jpg', 'Haroma Signature')]
def _logo_box(f):
    w, h = Image.open(os.path.join(OUT, 'assets', 'logos-web', f)).size
    ar = w / h
    hh = max(28, min(60, (5400 / ar) ** .5))
    return round(hh * ar), round(hh)


def marquee():
    imgs = []
    for f, n in CLIENTS:
        png = f.rsplit('.', 1)[0] + '.png'
        w, h = _logo_box(png)
        imgs.append(f'<img src="/assets/logos-web/{png}" alt="{esc(n)}" title="{esc(n)}" width="{w}" height="{h}" loading="lazy">')
    group = ''.join(imgs)
    dup = group.replace(' alt="', ' alt="" data-alt="')
    return (f'<div class="marquee" data-rv><div class="marquee-track">'
            f'<div class="marquee-group">{group}</div><div class="marquee-group" aria-hidden="true">{dup}</div>'
            f'</div></div>')


CLIENTS_HTML = marquee()
IMG_DIMS = {}
for _f in os.listdir(os.path.join(OUT, 'assets', 'img')):
    if _f.endswith('.webp'):
        IMG_DIMS[_f[:-5]] = Image.open(os.path.join(OUT, 'assets', 'img', _f)).size

DIMS = {'meta-dashboard.webp': (1665, 945), 'tiktok-dashboard.webp': (1672, 941), 'google-dashboard.webp': (1692, 930)}


def result(img, alt, tag, heading, bullets, flip=False):
    w, h = DIMS[img]
    return f'''        <div class="result{" flip" if flip else ""}">
          <div class="shot" data-rv><img src="/assets/{img}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"></div>
          <div data-rv><div class="split-k">{esc(tag)}</div><h3 class="h3" style="margin-top:12px">{esc(heading)}</h3>{ticks(bullets)}</div>
        </div>'''


RES_META = ('meta-dashboard.webp', 'Meta Ads Manager dashboard showing campaign results', 'Meta ads', 'Scaling conversions',
            ['Optimised cost per result', 'High-volume WhatsApp lead generation', 'Retargeting funnels that compound'])
RES_TT = ('tiktok-dashboard.webp', 'TikTok analytics dashboard showing live and video results', 'TikTok', 'Viral reach and live sales',
          ['High-volume livestream traffic', 'Rapid follower growth', 'Strong brand awareness'])
RES_GG = ('google-dashboard.webp', 'Google Search Console dashboard showing organic growth', 'Google search', 'Winning search intent',
          ['+108% organic clicks', '58M+ impressions', 'High-converting search ad traffic'])

# =================================================================== HOME
exec(open(os.path.join(ROOT, 'tools', 'blocks_v2.py'), encoding='utf8').read())

HOME_FAQ = [
    ('Do you work with large companies and franchise brands in Malaysia?', 'Yes. We run marketing for multi-outlet and franchise brands and for companies with 50+ staff: one strategy for the whole brand, local ads for each outlet, and training so your in-house team can run the day-to-day work.'),
    ('What does a digital marketing agency in Malaysia and Singapore do for my business?', 'We plan your strategy, produce the content, run ads on Facebook, Instagram, TikTok, Google and Xiaohongshu, work with KOLs and report the leads and sales each ringgit or dollar brings back. One team, every channel, for brands in Malaysia and Singapore.'),
    ('Do you offer SEO services in Malaysia?', 'Yes. Technical SEO, content, Google Business Profile and AI search (AEO and GEO), so you show up on Google and in ChatGPT and Gemini answers. We pair it with Google Ads when you need leads this month.'),
    ('Can you train our staff in AI and digital marketing?', 'Yes. We run corporate AI and marketing training for teams and departments, hands-on with your own accounts, products and data rules. Your staff leave able to make the video, launch the ad and read the report themselves.'),
    ('Do I need experience or coding to join your AI course in Malaysia?', 'No. Every class starts from zero. If you can use WhatsApp and a browser, you can follow along, and if you follow the class and still cannot do it, we refund you in full (terms apply).'),
    ('How much does digital marketing cost in Malaysia?', 'Done-For-You packages are customised to your goals, platforms and content volume, so WhatsApp us for a quote. To learn it yourself with our AI tools and classes, the TCM Membership is RM350 a month, or RM250 a month on the yearly plan.'),
    ('Are you a social media agency for TikTok, Facebook, Instagram and Xiaohongshu?', 'Yes. We run all four in-house: content, ads, TikTok Live and Shop, Xiaohongshu notes and creator seeding, plus Google. You get one plan and one report instead of four agencies.'),
    ('Do you work with KOLs and influencers in Malaysia?', 'Yes. We shortlist KOLs and KOCs by audience fit, engagement quality and real followers, then manage the brief, approvals and results, so every collaboration is measured in reach and sales.'),
    ('Do you do video production and livestreaming in Malaysia?', 'Yes. Our in-house studio shoots short videos, product films and brand films, and runs TikTok and Facebook livestreams with hosts, scripts and live offers.'),
    ('What is the TCM Membership?', 'Every TCM AI tool (Scan Buddy and AI Video), the full video course library, our marketing resources and a live class every month, with a coach who guides you step by step. It is RM350 a month, or RM250 a month on the yearly plan (RM3,000 a year, save RM1,200). Cannot learn it? 100% refund (terms apply).'),
]
home_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'ProfessionalService', 'name': 'Top Creation Media', 'url': SITE, 'logo': SITE + 'assets/tcm-logo.jpg',
     'image': SITE + 'assets/tcm-logo.jpg', 'telephone': '+' + PHONE, 'areaServed': ['MY', 'SG'],
     'description': 'Digital marketing agency and AI & marketing training studio in Malaysia.',
     'sameAs': ['https://facebook.com/topcreationmedia', 'https://instagram.com/topcreationmedia', 'https://tiktok.com/@topcreationmedia']},
    faq_ld(HOME_FAQ)]}

INDEX = [
    ('Marketing services', [
        ('SEO agency Malaysia', '/marketing-services#google'),
        ('Google Ads management', '/marketing-services#google'),
        ('Facebook & Instagram ads', '/marketing-services#facebook'),
        ('TikTok marketing & TikTok Live', '/marketing-services#tiktok'),
        ('Xiaohongshu marketing', '/marketing-services#xiaohongshu'),
        ('Social media management', '/marketing-services'),
    ]),
    ('Content & creators', [
        ('Video production', '/marketing-services#more'),
        ('AI video production', '/marketing-services#more'),
        ('Livestream studio', '/marketing-services#more'),
        ('KOL & influencer marketing', '/marketing-services#more'),
        ('IP & personal branding', '/marketing-services#more'),
        ('Websites & landing pages', '/marketing-services#more'),
    ]),
    ('Training', [
        ('Digital marketing course', '/marketing-classes'),
        ('Facebook ads course', '/marketing-classes#facebook'),
        ('TikTok ads course', '/marketing-classes#tiktok'),
        ('AI course, no coding', '/ai-classes'),
        ('Corporate AI & marketing training', '/ai-classes'),
        ('TCM Membership', '/membership'),
    ]),
    ('AI tools & proof', [
        ('AI tools for marketing', '/ai-tools'),
        ('Scan Buddy: Google review QR code', '/scan-buddy'),
        ('AI Video: product photo to video', '/ai-video'),
        ('Portfolio & campaign results', '/portfolio'),
        ('Insights: AI & marketing guides', '/insights'),
    ]),
]


def index_section():
    cols = ''.join(
        f'<div class="index-col" data-rv><h3>{esc(t)}</h3><ul>' + ''.join(f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in links) + '</ul></div>'
        for t, links in INDEX)
    return f'''    <section class="tile tile-dark" id="explore">
      <div class="wrap">
        {head('Digital marketing in Malaysia, <span class="accent">all under one roof</span>', 'Explore TCM', 'SEO and paid ads, video and KOLs, AI tools, and training for your team.')}
        <div class="index">{cols}</div>
      </div>
    </section>'''


home_ld['@graph'][0].update({
    'description': 'Digital marketing agency in Malaysia for SEO, Google and Meta ads, TikTok, Xiaohongshu, KOL marketing and video production, with AI and digital marketing training for teams.',
    'availableLanguage': ['English', 'Chinese', 'Malay'],
    'knowsAbout': [l for _, links in INDEX[:3] for l, _ in links],
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Marketing services', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': l, 'url': SITE + h.lstrip('/').split('#')[0]}}
        for _, links in INDEX[:2] for l, h in links]},
})
home_ld['@graph'].insert(1, {'@type': 'WebSite', 'name': 'Top Creation Media', 'url': SITE, 'inLanguage': ['en', 'zh-Hans']})

SERVICES = [
    ('Meta ads', 'Facebook and Instagram ads, measured on CPM, CPL and ROAS.', '/marketing-services#facebook', 'logo', 'meta', 'Meta'),
    ('TikTok', 'Short video, Live and TikTok Shop as one sales engine.', '/marketing-services#tiktok', 'logo', 'tiktok', 'TikTok'),
    ('Xiaohongshu', 'Notes and creators for Chinese-speaking buyers.', '/marketing-services#xiaohongshu', 'logo', 'xiaohongshu', 'Xiaohongshu'),
    ('Google SEO & SEM', 'More Google traffic and higher rankings, with AEO and GEO built in.', '/marketing-services#google', 'logo', 'google', 'Google'),
    ('Video & livestream', 'In-house studio, hosts and crew.', '/marketing-services#more', 'photo', 'livestream', 'Livestream host selling skincare live from a studio'),
    ('KOC & KOL', 'Creators matched on real audience fit.', '/marketing-services#more', 'photo', 'kol', 'Creator filming a product review on her phone'),
    ('IP branding', 'Turn the founder into the face of the brand.', '/marketing-services#more', 'photo', 'ip-branding', 'Founder being interviewed on camera for a personal brand video'),
    ('Events, offline to online', 'Launches filmed on the day, amplified after.', '/marketing-services#more', 'photo', 'events', 'Videographer filming a brand launch event in a mall'),
]

TEAM = [
    ('team-emma', 'Emma', 'AI & Marketing Director'),
    ('team-jess', 'Jess', 'HR & Media Advertising Manager'),
    ('team-mac', 'Mac', 'SEO & AI Strategist'),
    ('team-marcus', 'Marcus', 'Planning & Operation Consultant'),
]


def member(key, name, role, i):
    return f'''<figure class="member" style="--i:{i}" data-rv>
            {video(key, f'{name}, {role}').replace(' data-rv', '')}
            <figcaption><b>{esc(name)}</b><span>{esc(role)}</span></figcaption>
          </figure>'''


home_body = f'''    <section class="hero">
      <div class="hero-grid">
        <div>
          <div class="eyebrow rise eb-split"><span class="nb">Digital marketing agency</span> <span class="eb-dot">·</span> <span class="nb">Malaysia &amp; International</span></div>
          <h1 class="h1 rise" style="animation-delay:.05s">Your Marketing,<br><span class="accent">Simplified.</span></h1>
          <p class="lede rise" style="animation-delay:.15s">From offline to fully online: ads, videos, livestream, KOC/KOL and AI automation. Let our team run it for you, or learn to run it yourself in just a few clicks.</p>
          <div class="btn-row rise" style="animation-delay:.3s">
            <a class="btn btn-primary" href="{wa("Hi, I'd like a free consultation!")}" target="_blank" rel="noopener">Get a free consultation {ARROW}</a>
            <a class="btn btn-ghost" href="#services">Explore our services</a>
          </div>
        </div>
        <div class="rise" style="animation-delay:.2s">{video('home', 'Top Creation Media introduction video').replace(' data-rv', '')}</div>
      </div>
      <div class="hero-logos">
        <p data-rv>Trusted by brands across Malaysia and beyond</p>
        {CLIENTS_HTML}
      </div>
    </section>

    <section class="tile tile-raise" id="what-we-do">
      <div class="wrap">
        {head('Everything you need to <span class="accent">grow online</span>', 'Our services')}
        {svc_cards(SERVICES)}
      </div>
    </section>

    <section class="tile tile-raise" id="about">
      <div class="wrap">
        <div class="sec-head sec-wide" style="margin-bottom:0">
          <div data-rv><div class="eyebrow">About us</div><h2 class="h2">One team, from <span class="accent">offline to online.</span></h2></div>
          <p class="lede" data-rv style="margin-top:22px">Top Creation Media is a digital marketing agency and training studio in Malaysia. We plan, shoot, launch and scale marketing for brands, and teach business owners and teams to do the same with AI.</p>
        </div>
        <div class="stats">
          <div class="stat" data-rv><div class="stat-n">8+</div><div class="stat-l">Years of experience</div></div>
          <div class="stat" data-rv><div class="stat-n">3,000+</div><div class="stat-l">Videos produced</div></div>
          <div class="stat" data-rv><div class="stat-n">500+</div><div class="stat-l">Clients served</div></div>
          <div class="stat" data-rv><div class="stat-n">5</div><div class="stat-l">Markets: MY, SG, CN, US, ID</div></div>
        </div>
      </div>
    </section>

    <section class="tile tile-dark team" id="team">
      <div class="wrap">
        {head('The people behind <span class="accent">your growth</span>', 'Meet the team')}
        <div class="team-grid" data-sound-group>
          {''.join(member(*m, i) for i, m in enumerate(TEAM))}
        </div>
      </div>
    </section>

    <section class="tile mvp" id="mvp">
      <div class="wrap">
        <div class="mvp-head" data-rv>
          <div class="eyebrow">Mission · Vision · Performance</div>
          <h2 class="mvp-title">Our <span class="accent">MVP</span></h2>
          <p class="lede">Three promises behind everything we teach and everything we run for you.</p>
        </div>
        <div class="split">
        {photo('mission.jpg', 'Trainer teaching a digital marketing strategy masterclass to a full room')}
          <div class="mvp-text" data-letter="M" data-rv>
            <div class="split-k mvp-num"><b>01</b>Our mission</div>
            <h3 class="h2">We guide you until you can do it yourself.</h3>
            <p class="lede">We coach every participant to learn AI and marketing hands-on. You set up the account, make the video and launch the ad with your own hands, with us beside you.</p>
            {ticks(['Learn by doing, on your own business', 'Step-by-step guidance, starting from zero', 'Templates and prompts you keep for good'])}
          </div>
        </div>
        <div class="split flip">
        {photo('vision.jpg', 'Behind the scenes of a product shoot in the green-screen studio')}
          <div class="mvp-text" data-letter="V" data-rv>
            <div class="split-k mvp-num"><b>02</b>Our vision</div>
            <h3 class="h2">Every beginner can become a professional marketer.</h3>
            <p class="lede">Anyone who finds this website, with no experience and no coding, should be able to become a professional marketer. Every class and service we build is held to that standard.</p>
            {ticks(['No experience or coding needed', 'Skills for your own business, or to freelance', 'Learn the right way first and skip costly mistakes'])}
          </div>
        </div>
        <div class="split">
        {photo('performance.jpg', 'Client team celebrating at their shop counter')}
          <div class="mvp-text" data-letter="P" data-rv>
            <div class="split-k mvp-num"><b>03</b>Our performance</div>
            <h3 class="h2">Our experience becomes your performance.</h3>
            <p class="lede">Everything we learned serving 500+ clients, we hand to you. Run your marketing more efficiently, save on costly agency fees, and grow your sales and your brand.</p>
            {ticks(['Higher sales, from proven campaign playbooks', 'Lower costs: do in-house what you used to outsource', 'Faster workflows with AI and ready templates', 'A stronger brand that customers trust'])}
          </div>
        </div>
      </div>
    </section>

    <section class="tile tile-raise" id="services">
      <div class="wrap">
        {head('Two ways to grow. <span class="accent">You choose.</span>', 'How we work with you', 'Same team, same platforms. The difference is who does the work.')}
        <div class="ways">
          <div class="way" data-rv>
            <div class="way-k">Services</div>
            <div class="way-t">We run it for you.</div>
            <p class="way-d">Strategy, content, ads, livestream and KOC/KOL, handled by our team while you focus on your business.</p>
            {ticks(['Facebook & Instagram ads', 'TikTok video, Live & TikTok Shop', 'Google SEO & search ads', 'Xiaohongshu notes & creator seeding', 'KOC & KOL collaborations'])}
            <a class="btn btn-primary" href="/marketing-services">See our services</a>
          </div>
          <div class="way" data-rv>
            <div class="way-k">Academy</div>
            <div class="way-t">We teach you to do it.</div>
            <p class="way-d">Learn every setting, hands-on, from account setup to scaling. Save on agency fees and skip the costly trial and error.</p>
            {ticks(['Every platform, from A to Z', 'Practise on your own business', 'Templates and checklists you keep', "Can't learn it? 100% refund"])}
            <a class="btn btn-primary" href="/marketing-classes">See the Academy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="tile tile-raise" id="results">
      <div class="wrap">
        {head('Real numbers from <span class="accent">real campaigns</span>', 'Results', style='margin-bottom:16px')}
{result(*RES_GG)}
{result(*RES_META, flip=True)}
{result(*RES_TT)}
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap">
        {head('Recent work', 'Portfolio')}
        <div class="gallery" id="home-gallery"></div>
        <div class="btn-row" data-rv><a class="btn btn-ghost" href="/portfolio">View the full portfolio</a></div>
      </div>
    </section>

    <section class="tile tile-raise" id="testimonials" hidden>
      <div class="wrap">
        {head('What clients say', 'Testimonials')}
        <div class="quotes"></div>
      </div>
    </section>

{index_section()}

{faq_section(HOME_FAQ, 'tile-raise')}

{cta('Stop guessing. Start growing.', 'One chat. One customized plan. One team for every channel, or a class that teaches you to run it yourself.', 'WhatsApp Us for a Free Consultation', "Hi, I'd like a free consultation!")}'''

# =================================================================== DONE-FOR-YOU
XHS_NOTE_UNUSED = " Xiaohongshu&#8217;s Juguang (聚光) ad platform generally requires a mainland China business entity, so overseas brands usually advertise through certified agency partners. We handle the access route for you, and put most of the effort where it pays off first: search-led notes and creator seeding."


def svc_panel(h3, lede, points, res=None, note='', ics=None):
    r = f'\n        <div style="margin-top:56px">\n{result(*res)}\n        </div>' if res else ''
    n = f'\n        <p class="note" data-rv>{note}</p>' if note else ''
    return f'''{panel_intro(h3, lede)}
        {cards(points, 'grid g3', ics)}{r}{n}
        <div class="btn-row" data-rv><a class="btn btn-ghost" href="/portfolio">See our work</a></div>'''


DFY_FB = [
    ('Strategy & funnel design', 'Audience research, offer and a content calendar built around your sales goal.'),
    ('Video production', 'Scroll-stopping short videos shot and edited in our studio.'),
    ('High-converting posters', 'Static ads built around a hook, proof and one clear call to action.'),
    ('Carousel designs', 'Swipe-through stories for product ranges, offers and social proof.'),
    ('Advanced Meta ads', 'Advantage+ and manual campaigns, creative testing and retargeting, tuned weekly.'),
    ('Tracking & WhatsApp leads', 'Pixel and Conversions API set up, click-to-WhatsApp campaigns and clear monthly reports.'),
]
DFY_TT = [
    ('Short video creation', 'Trend-native scripts, hooks and edits, produced at volume without losing quality.'),
    ('TikTok Live operations', 'Studio, hosts, scripts, run-of-show and real-time offers for selling lives.'),
    ('TikTok Shop', 'Shop setup, product catalog, affiliate creators and GMV Max campaigns.'),
    ('Malay KOC network', 'Key opinion consumers creating authentic product content at scale.'),
    ('Spark Ads & Smart+', 'Boost the posts that already work and scale them with TikTok ads.'),
    ('Results reporting', 'Views, live sales, cost per result and ROAS, reported clearly.'),
]
DFY_GG = [
    ('SEO', 'Technical fixes, content and authority building for page-one rankings.'),
    ('SEM: Google Ads', 'Search campaigns with keyword, bid and landing-page optimisation.'),
    ('AI search: AEO & GEO', 'Get your brand into Google AI answers, ChatGPT and Gemini with clear FAQs and structured data.'),
    ('Websites & landing pages', 'Fast pages that turn visitors into WhatsApp enquiries, built and measured.'),
    ('Google Business Profile', 'Show up on Google Maps with reviews, photos and up-to-date details.'),
    ('Search Console & GA4', 'See what people search, which pages rank and which ones bring leads.'),
]
DFY_XHS = [
    ('Account setup & positioning', 'A professional profile that says who you help and why they should follow.'),
    ('Search-led notes', 'Keyword research, titles, covers and a posting rhythm that builds search ranking.'),
    ('博主 & KOC seeding', 'Creators selected and briefed to post genuine reviews, including through Pugongying (蒲公英).'),
    ('Juguang (聚光) ads', 'Search and feed ads through certified partners, when the time is right.'),
    ('Compliance', 'Content and claims that stay within platform rules.'),
    ('Leads & conversion', 'DMs, lead forms and store links that turn attention into enquiries.'),
]
TOOLKIT = [
    ('AI video production', 'UGC ads, AI short films and product videos.', '/ai-classes#ai-video-types', 'photo', 'ai-video', 'Three AI-made videos: an outfit and background swap, product footage and salon B-roll'),
    ('Websites & landing pages', 'Fast pages built to turn visitors into enquiries.', '#google', 'photo', 'website', 'Web designer working on a landing page design'),
    ('Video production', 'Short videos, product and brand films.', '#more', 'photo', 'production', 'Crew filming a product on a turntable in a studio'),
    ('Livestream studio', 'Hosts, scripts and crew for selling lives.', '#more', 'photo', 'livestream', 'Livestream host presenting products to a phone camera'),
    ('KOC & KOL', 'Creators shortlisted, briefed and measured.', '#more', 'photo', 'kol', 'Creator recording a product review'),
    ('IP branding', 'Turn the founder into the face of the brand.', '#more', 'photo', 'ip-branding', 'Founder being interviewed on camera for a personal brand video'),
    ('Events, offline to online', 'Launches filmed live and amplified online.', '#more', 'photo', 'events', 'Brand launch event being filmed in a mall atrium'),
    ('Team training', 'Train your staff to take over day-to-day.', '/marketing-classes', 'photo', 'training', 'Corporate marketing and AI training workshop'),
]
DFY_FAQ = [
    ('What is included in your social media management in Malaysia?', 'Strategy, a monthly content plan, video and design made in our studio, posting, community replies, ads and a monthly results report. You choose the platforms and content volume.'),
    ('Do you run Google Ads and Meta ads for companies in Malaysia?', 'Yes. We plan, launch and optimise Google Search, Performance Max, Facebook and Instagram campaigns every week, with tracking set up so you see cost per lead and return on ad spend.'),
    ('What is the minimum ad budget in Malaysia?', 'Enough for the platform to learn: we start with a test budget, find the winning creative and audience, then scale. We recommend a realistic number for your industry on the first call.'),
    ('Can you handle marketing for a franchise with many outlets?', 'Yes. One brand standard and shared content for the group, local campaigns per outlet, and a report that compares every branch.'),
    ('Do you also do branding?', 'Yes. Logo, visual identity, positioning and brand guidelines, so every post, ad and outlet looks like one brand.'),
]
dfy_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Service', 'name': 'Done-For-You Social Media Marketing', 'serviceType': 'Digital marketing agency services',
     'provider': PROVIDER, 'areaServed': ['MY', 'SG'], 'url': SITE + 'marketing-services',
     'description': 'Facebook, Instagram, TikTok, Google and Xiaohongshu marketing run by Top Creation Media: strategy, content, ads, livestream and KOC/KOL.'},
    faq_ld(DFY_FAQ)]}

dfy_body = f'''{hero([("Home", "/"), ("Services", "")], 'Your marketing, <span class="accent">done for you.</span>',
       'Strategy, content, ads, livestream and KOC/KOL across Facebook, Instagram, TikTok, Google and Xiaohongshu, handled end to end by one team.',
       btns(('Get a free strategy chat', wa("Hi, I'd like to know more about your marketing services!")), ('Choose a platform', '#platforms')),
       video('services', 'Marketing services video'), eyebrow='Marketing services')}

    <section class="tile tile-raise" id="platforms">
      <div class="wrap">
        {head('Choose a platform', 'What we do', style='margin-bottom:40px')}
{tabs('Platforms', [
    ('facebook', 'Facebook & IG', svc_panel('Facebook &amp; Instagram, from scroll to sale', 'We run Facebook and Instagram as one engine: strategy first, creative built to convert, then ads tuned every week.', DFY_FB, RES_META, ics=['target', 'video', 'pen', 'layers', 'megaphone', 'zap'])),
    ('tiktok', 'TikTok', svc_panel('TikTok video, Live and Shop', 'From trend-driven short video to full livestream selling, we run the whole TikTok flywheel.', DFY_TT, RES_TT, ics=['music', 'live', 'coins', 'users', 'zap', 'target'])),
    ('google', 'Google', svc_panel('Own the search results, human and AI', 'When customers search on Google or ask an AI, your brand should be the answer.', DFY_GG, RES_GG, ics=['search', 'megaphone', 'sparkles', 'layers', 'target', 'zap'])),
    ('xiaohongshu', 'Xiaohongshu', svc_panel('Xiaohongshu (RED): notes, 博主 and ads', 'Reach Chinese-speaking buyers in Malaysia, Singapore and China with content that gets found and creators who build trust.', DFY_XHS, ics=['book', 'search', 'users', 'megaphone', 'layers', 'target'])),
])}
      </div>
    </section>

    <section class="tile tile-dark" id="more">
      <div class="wrap">
        {head('Everything else we do', 'More services')}
        {svc_cards(TOOLKIT)}
      </div>
    </section>

    <section class="tile tile-raise">
      <div class="wrap">
        {head('How we work', 'Our process')}
{STEPS3}
      </div>
    </section>

{faq_section(DFY_FAQ)}

{cta('Ready to hand it over?', 'Tell us your goal and budget range. We will build a customized plan.', 'WhatsApp Us for a Customized Package', "Hi, I'd like a customized package!")}'''

# =================================================================== ACADEMY
META = [
    ('Business setup', 'Set up your Meta Business Portfolio, Facebook Page, Instagram professional account and ad account the right way: payment, roles and domain verification, so nothing gets restricted later.', 'A clean, verified account structure.', ['Business Portfolio', 'Ad account', 'Instagram professional', 'Domain verification']),
    ('Tracking', 'Install the Meta Pixel and Conversions API, choose the right events (Lead, Purchase, Message) and check them in Events Manager before you spend a ringgit.', 'A tested pixel and server events.', ['Pixel', 'Conversions API', 'Events Manager']),
    ('Campaign structure', 'Pick the right objective, understand Advantage+ versus manual campaigns, and set up budgets, ad sets and ads with names you can still read in six months.', 'A campaign built from a proven structure.', ['Objectives', 'Advantage+', 'CBO / ABO']),
    ('Audiences', 'Broad versus interest targeting, custom audiences, lookalikes, exclusions, and location and language settings for Malaysia and Singapore.', 'Three audiences, tested against each other.', ['Broad', 'Custom audiences', 'Lookalikes']),
    ('Creative that converts', 'Hooks, formats and copy for video, Reels, Stories, carousel and static ads. How to run a creative test so every ad teaches you something.', 'A creative testing plan and your first ads.', ['Hooks', 'Reels', 'Carousel', 'UGC style']),
    ('Launch', 'Placements, schedule and budget, click-to-WhatsApp and Messenger destinations, ad policy pitfalls and a pre-launch checklist.', 'A campaign live, with a launch checklist.', ['Click-to-WhatsApp', 'Placements', 'Policy']),
    ('Instagram growth & DMs', 'Reels that get watched, partnership ads with creators, product tags and DM auto-replies that turn interest into sales.', 'A Reels plan and a DM flow that answers in seconds.', ['Reels', 'Partnership ads', 'Auto-replies']),
    ('Reading the numbers', 'ROAS, cost per lead, CTR, CPM and frequency: what each tells you, which to ignore, and how attribution changes what you see.', 'A weekly report you can read in five minutes.', ['ROAS', 'CPL', 'CTR']),
    ('Optimise & scale', 'When to switch off, when to wait and when to scale. Creative refresh, budget steps, retargeting and A/B tests.', 'A 30-day optimisation plan.', ['Retargeting', 'A/B tests', 'Scaling']),
]
TT = [
    ('Business setup', 'Create your TikTok Business Center and Ads Manager account and link your profile. Connect TikTok Shop if you sell products.', 'A working Business Center and ad account.', ['Business Center', 'Ads Manager', 'TikTok Shop']),
    ('Tracking', 'Install the TikTok Pixel and Events API, pick your conversion events and test them before launch.', 'Verified conversion tracking.', ['TikTok Pixel', 'Events API']),
    ('Content that feels native', 'Hook-first video that looks like TikTok, not like an ad: scripting, filming on a phone, editing and trends.', 'Five native-style videos.', ['Hooks', 'Scripts', 'CapCut']),
    ('Campaign types', 'Manual campaigns versus Smart+, Spark Ads, GMV Max for TikTok Shop and LIVE ads. Which to use at which stage.', 'A campaign plan for your business.', ['Smart+', 'Spark Ads', 'GMV Max']),
    ('TikTok Live & Shop', 'Plan a selling live: run-of-show, host script, product lineup, offers and how to drive traffic to your LIVE.', 'A livestream run-of-show.', ['LIVE', 'TikTok Shop', 'Offers']),
    ('KOC collaborations', 'Find, brief and work with KOCs and affiliates, then turn their best posts into Spark Ads.', 'A KOC brief and shortlist.', ['KOC', 'Affiliates', 'Spark Ads']),
    ('Results & refresh', 'Read cost per result and ROAS, spot creative fatigue early and refresh before performance drops.', 'A weekly report and refresh schedule.', ['ROAS', 'Creative fatigue']),
]
GOOGLE = [
    ('Google basics & Business Profile', 'How Google search works, and how to set up your Google Business Profile so you appear on Maps with reviews and photos.', 'A verified, complete Business Profile.', ['Google Business Profile', 'Maps', 'Reviews']),
    ('Keyword research with ChatGPT', 'Find what your customers actually search, then use ChatGPT or Claude with Keyword Planner to group keywords and plan your pages.', 'A keyword map for your website.', ['ChatGPT', 'Claude', 'Keyword Planner']),
    ('SEO on your website', 'Titles, descriptions, headings, content, page speed and internal links, checked in Search Console.', 'An optimised page, live.', ['On-page SEO', 'Search Console', 'PageSpeed']),
    ('AI search: AEO & GEO', 'FAQs, structured data and clear answers so you appear in Google AI answers, ChatGPT and Gemini.', 'A search-ready FAQ page.', ['FAQ schema', 'Google AI', 'ChatGPT search']),
    ('Google Ads: search', 'Search campaigns, keywords and match types, ad copy, assets and conversion tracking.', 'A search campaign ready to launch.', ['Google Ads', 'Keywords', 'Conversions']),
    ('Performance Max & YouTube', 'When Performance Max and YouTube ads make sense, and how to feed them good creative.', 'A plan for your next campaign.', ['Performance Max', 'YouTube']),
    ('Measure & improve', 'GA4, Search Console and cost per lead: read your sample website results and decide what to fix next.', 'A monthly review template.', ['GA4', 'Search Console', 'Cost per lead']),
]
XHS = [
    ('Account & positioning', 'Personal versus professional accounts, a profile that says who you help, and what the platform expects from brands.', 'A positioned, ready-to-post profile.', ['Business account', 'Profile']),
    ('Search-led notes', 'Xiaohongshu is a search platform. Keyword research, note titles and covers, tags, image versus video notes, and a posting rhythm.', 'Five notes built around real search keywords.', ['Keywords', 'Covers', 'Tags']),
    ('博主 & KOC seeding', 'Seed genuine content through creators before spending on ads: briefs, selection, approvals and the Pugongying (蒲公英) platform.', 'A creator brief and shortlist.', ['KOC', 'KOL', 'Pugongying 蒲公英']),
    ('Juguang (聚光) ads', 'Search versus feed ads, keyword bidding and targeting, and how overseas brands access Juguang through certified partners.', 'A paid plan and access route.', ['Juguang 聚光', 'Search ads', 'Feed ads']),
    ('Compliance & disclosure', 'Ad and sponsored-content rules, claims you cannot make, and how to stay within platform policy.', 'A compliance checklist.', ['Ad rules', 'Disclosure']),
    ('Leads & measurement', 'Turn attention into enquiries with DMs, lead forms and Qianfan (千帆), then track note performance and cost per lead.', 'A lead path and monthly review.', ['DMs', 'Qianfan 千帆', 'Note metrics']),
]
ACADEMY_FAQ = [
    ('Is this digital marketing course in Malaysia suitable for beginners?', 'Yes. Every platform starts from account setup and builds to optimising and scaling. If you already run ads, jump straight to the module you need.'),
    ('Can you run the course in-house for our company team?', 'Yes. We train teams and departments on your own accounts and products, so the practice work becomes real campaigns for your business.'),
    ('What does the 100% refund guarantee cover?', 'Attend every session, complete the practice tasks and still cannot do it yourself? We refund your class fee in full. WhatsApp us for the full terms.'),
    ('Do I need an ad budget to join?', 'You can learn setup and structure without spending. Real learning comes from a small live test, and we help you choose a sensible budget.'),
    ('Are the courses included in the TCM Membership?', 'Yes. The Membership includes the full video course library, a live class every month, our marketing resources and every TCM AI tool. It is RM350 a month, or RM250 a month on the yearly plan.'),
]
academy_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Course', 'name': 'Marketing Academy: Facebook, Instagram, TikTok, Google & Xiaohongshu',
     'description': 'Hands-on marketing classes in Malaysia, from account setup and tracking to creative, optimisation and scaling, for Facebook, Instagram, TikTok, Google and Xiaohongshu.',
     'provider': PROVIDER, 'url': SITE + 'marketing-classes'},
    faq_ld(ACADEMY_FAQ)]}

academy_body = f'''{hero([("Home", "/"), ("Academy", "/marketing-classes"), ("Marketing Academy", "")], 'Learn to run your own ads, <span class="accent">A to Z.</span>',
       'Facebook, Instagram, TikTok, Google and Xiaohongshu, taught hands-on on your own accounts. Save on agency fees and never waste money on the wrong strategy again.',
       btns(('Join the next class', wa("Hi, I'd like to join the marketing classes!")), ('Choose a platform', '#platforms')),
       switch('academy') + video('academy', 'Marketing classes introduction video'), eyebrow='Marketing Academy')}

{classroom_strip()}

    <section class="tile tile-dark" id="platforms">
      <div class="wrap">
        {head('One platform at a time', 'Curriculum', 'Tap a step to see what you learn.', style='margin-bottom:40px')}
{tabs('Platforms', [
    ('facebook', 'Facebook & IG', panel_intro('Facebook &amp; Instagram, from account to scale', 'Nine steps from a blank account to campaigns you can optimise and grow. Facebook and Instagram share the same Meta Ads Manager.') + '\n' + modules_compact(META)),
    ('tiktok', 'TikTok', panel_intro('TikTok content, ads and live selling', 'From Business Center to Smart+ and GMV Max, with videos that feel native and a plan for TikTok Live.') + '\n' + modules_compact(TT)),
    ('google', 'Google', panel_intro('Google SEO, search ads and AI search', 'Get found when customers search, with ChatGPT doing the heavy lifting on research and writing.') + '\n' + modules_compact(GOOGLE)),
    ('xiaohongshu', 'Xiaohongshu', panel_intro('Xiaohongshu (RED): notes, 博主 and ads', 'Reach Chinese-speaking customers with notes that get found, creators who build trust, and paid support.') + '\n' + modules_compact(XHS)),
])}
      </div>
    </section>

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Templates you take home', 'Take-home kit', 'So you can run it again next month without us.')}
        <div class="cols">
          <div class="col" data-rv><div class="col-t">Launch checklist</div><p class="col-d">Every setting to confirm before you press publish, by platform.</p></div>
          <div class="col" data-rv><div class="col-t">Creative testing tracker</div><p class="col-d">A simple sheet to plan, run and learn from every creative test.</p></div>
          <div class="col" data-rv><div class="col-t">Weekly report template</div><p class="col-d">The five numbers that matter, and what to do when they move.</p></div>
        </div>
      </div>
    </section>

{guarantee('classes')}

{member_band()}

{faq_section(ACADEMY_FAQ, 'tile-raise')}

{cta('Become the next professional marketer.', 'Tell us your business and goal. We will point you to the right platform to start.', 'WhatsApp Us About the Classes', "Hi, I'd like to know more about the marketing classes!")}'''

# =================================================================== AI CLASSES
AI_MODS = [
    ('Know your AI tools', 'Start here. ChatGPT, Claude and Gemini: what each is best at, free versus paid, and how to give AI the context, examples and checks that turn generic text into usable work.', 'Your own prompt library and a brand-voice assistant.', ['ChatGPT', 'Claude', 'Gemini', 'Perplexity']),
    ('AI video', 'Auto-edit footage, change backgrounds, swap outfits, add motion and generate AI footage and UGC-style clips, with subtitles and voice in English, 中文 and Bahasa.', 'A product video and a set of vertical shorts.', ['CapCut', 'Kling', 'Veo', 'Runway', 'HeyGen', 'ElevenLabs']),
    ('AI graphics', 'Posters, product photos, carousels and brand visuals without a designer, kept on-brand with your colours and fonts.', 'A poster set and a carousel for your next campaign.', ['Canva AI', 'ChatGPT images', 'Gemini', 'Adobe Firefly']),
    ('AI website builder & AI SEO', 'Plan a page, write the copy and build the website with AI, publish it on your own domain, then get it found on Google and in AI answers.', 'A landing page, live and search-ready.', ['Claude', 'Lovable', 'Vercel', 'Search Console']),
    ('AI captions: hook, body, CTA', 'Write captions that stop the scroll: a hook in the first line, a body that builds desire, and a call to action that gets the click, in seconds.', 'A caption formula and 30 days of captions.', ['ChatGPT', 'Claude', 'Gemini']),
    ('AI system flow', 'Let work run without you: AI auto-replies on WhatsApp and Instagram, a lead system that follows up, and posting to every platform at once.', 'One working flow, from enquiry to follow-up.', ['n8n', 'Make', 'ManyChat', 'WhatsApp Business', 'Meta Business Suite']),
    ('AI marketing', 'Research, personas, content calendars, AI-powered ad campaigns (Advantage+, Smart+, Performance Max) and reading performance data with AI.', 'A 30-day AI marketing plan for your business.', ['Claude', 'ChatGPT', 'Advantage+', 'GA4']),
]
AI_FAQ = [
    ('Do I need coding experience to join the AI course?', 'No coding at all. If you can use WhatsApp and a browser, you can follow along. AI does the technical parts and we explain every step in plain language.'),
    ('Which AI tools for marketing do you teach?', 'ChatGPT, Claude and Gemini, plus the AI video, design, website and automation tools around them. We teach the method first, because tools change every month.'),
    ('Can you run AI training for our whole company in Malaysia?', 'Yes. We train teams and departments of any size, with examples built on your industry, products and data rules, so staff use AI on real work from day one.'),
    ('What does the 100% refund guarantee cover?', 'Attend every session, complete the practice tasks and still cannot do it yourself? We refund your class fee in full. WhatsApp us for the full terms.'),
    ('Are the AI classes included in the TCM Membership?', 'Yes. The Membership includes the AI class videos, a live class every month, the marketing course library, our resources and every TCM AI tool. It is RM350 a month, or RM250 a month on the yearly plan.'),
]
ai_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Course', 'name': 'AI Classes: AI Video, Graphics, Captions, Websites & Automation',
     'description': 'Hands-on AI classes in Malaysia, no coding needed: ChatGPT, Claude and Gemini, AI video, AI graphics, AI websites and SEO, AI captions, AI automation and AI marketing.',
     'provider': PROVIDER, 'url': SITE + 'ai-classes'},
    faq_ld(AI_FAQ)]}

ai_body = f'''{hero([("Home", "/"), ("Academy", "/marketing-classes"), ("AI Academy", "")], 'Let AI do the work. <span class="accent">You run the show.</span>',
       'AI already helps businesses work smarter and replace complex manual tasks. Learn to use it for video, graphics, captions, websites and automation. No coding, no tech background.',
       btns(('Join the next class', wa("Hi, I'd like to join the AI classes!")), ('See the 7 modules', '#curriculum')),
       switch('ai') + video('ai', 'AI Classes introduction video'), eyebrow='AI Academy · No coding needed')}

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Save costs, or earn from it', 'Who it is for')}
        {banner('training', 'Team learning AI and marketing tools in a hands-on workshop')}
        <div class="cols">
          <div class="col" data-rv><div class="col-t">Business owners</div><p class="col-d">Stop paying thousands to outsource what AI can do in a few clicks. One person can now run a whole marketing operation.</p></div>
          <div class="col" data-rv><div class="col-t">Teams &amp; companies</div><p class="col-d">Replace repetitive manual work with AI flows, so your people spend time on what grows the business.</p></div>
          <div class="col" data-rv><div class="col-t">Freelancers &amp; beginners</div><p class="col-d">Build skills businesses pay for: AI video, graphics, captions and automation. A new income stream starts here.</p></div>
        </div>
      </div>
    </section>

    <section class="tile tile-dark" id="curriculum">
      <div class="wrap">
        {head('Seven modules. Take one, or all', 'Curriculum', 'Every module ends with something you made, for your own business.')}
{modules(AI_MODS)}
      </div>
    </section>

{module_samples()}
    <section class="tile tile-raise">
      <div class="wrap">
        {head('How a class works', 'How it works')}
        <div class="cols">
          <div class="col" data-rv><div class="col-n">1</div><div class="col-t">See it done</div><p class="col-d">Short, focused demos of what works right now, and why. Not a tour of every button.</p></div>
          <div class="col" data-rv><div class="col-n">2</div><div class="col-t">Do it yourself</div><p class="col-d">Your products, your brand, your customers. You do the work with your own hands, with us beside you.</p></div>
          <div class="col" data-rv><div class="col-n">3</div><div class="col-t">Leave with results</div><p class="col-d">A finished video, page or working flow, plus the prompts and templates to do it again.</p></div>
        </div>
      </div>
    </section>

{guarantee('AI classes')}

{member_band()}

{faq_section(AI_FAQ, 'tile-raise')}

{cta('Ready to put AI to work?', 'Tell us about your business and we will point you to the right modules.', 'WhatsApp Us About the AI Classes', "Hi, I'd like to know more about the AI classes!")}'''

# =================================================================== PORTFOLIO
pf_ld = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Portfolio — Top Creation Media',
         'description': 'Short-form videos, ad results dashboards and brand work by Top Creation Media.',
         'url': SITE + 'portfolio', 'publisher': PROVIDER}
pf_body = f'''{hero([("Home", "/"), ("Portfolio", "")], 'Work that <span class="accent">moves numbers.</span>',
       'Videos, ad results and brand work for clients across Malaysia, Singapore and beyond.', eyebrow='Portfolio')}

    <section class="tile tile-raise" style="padding-top:72px">
      <div class="wrap">
        <div class="seg-wrap" style="margin-bottom:40px"><div class="seg" id="filters" role="group" aria-label="Filter portfolio"></div></div>
        <div class="gallery" id="gallery" aria-live="polite"></div>
        <noscript><p class="lede" style="text-align:center;margin-top:24px">Please enable JavaScript to browse the portfolio, or <a class="accent" href="https://wa.me/{PHONE}">WhatsApp us</a> to see our work.</p></noscript>
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap">
        {head('Brands we have worked with', 'Clients')}
        {CLIENTS_HTML}
      </div>
    </section>

{cta('Want results like these?', 'Tell us your goal and we will build a customized plan.', 'WhatsApp Us for a Customized Package', "Hi, I'd like a customized package!")}

  <div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Portfolio viewer">
    <button class="lb-x" aria-label="Close"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 4l16 16M20 4 4 20"/></svg></button>
    <div class="lb-box" id="lb-box"></div>
  </div>'''


# =================================================================== TOOL PAGES
def steps(rows):
    return '<ol class="steps">' + ''.join(f'<li data-rv><b>{esc(t)}</b><span>{esc(d)}</span></li>' for t, d in rows) + '</ol>'


def tool_body(key, h1, lede, wa_msg, video_label, step_rows, feat_h2, feats, extra, faq, cta_h2, cta_lede, feat_icons=None):
    sw = tool_switch('scan' if key == 'scan-buddy' else 'aivideo')
    tag_txt = f'From RM{SB["m"]} a month' if key == 'scan-buddy' else 'Included in the TCM Membership'
    tag = f'<div class="rise" style="margin-bottom:24px"><a class="tag" href="{"#plans" if key == "scan-buddy" else "/membership"}">{tag_txt}</a></div>'
    return f'''{hero([("Home", "/"), ("AI Tools", "/ai-tools"), (h1.split(':')[0], "")], h1, lede,
       btns(('See plans', '#plans' if key == 'scan-buddy' else '/membership#plans'), ('How it works', '#how')), sw + video(key, video_label)).replace('<div class="crumbs', tag + '<div class="crumbs', 1)}

    <section class="tile tile-raise" id="how">
      <div class="wrap">
        {head('How it works', 'How it works')}
        {steps(step_rows)}
      </div>
    </section>

{extra}
{tool_extra(key)}
    <section class="tile tile-raise">
      <div class="wrap">
        {head(feat_h2, 'Features')}
        {cards(feats, 'grid g3', feat_icons)}
      </div>
    </section>

{faq_section(faq)}

{cta(cta_h2, cta_lede, 'Join on WhatsApp', wa_msg)}'''



def qr_svg(seed=7, n=25):
    # Decorative QR-style pattern (not scannable).
    rnd = __import__('random').Random(seed)
    cells = []
    def finder(x, y):
        return (f'<rect x="{x}" y="{y}" width="7" height="7" rx="1.6" fill="none" stroke="#14123B" stroke-width="1"/>'
                f'<rect x="{x+2}" y="{y+2}" width="3" height="3" rx=".8" fill="url(#qg)"/>')
    for yy in range(n):
        for xx in range(n):
            if (xx < 8 and yy < 8) or (xx > n - 9 and yy < 8) or (xx < 8 and yy > n - 9):
                continue
            if rnd.random() < .46:
                cells.append(f'<rect x="{xx}" y="{yy}" width=".92" height=".92" rx=".25"/>')
    return (f'<svg viewBox="-.5 -.5 {n+1} {n+1}" aria-hidden="true"><defs><linearGradient id="qg" x1="0" x2="1">'
            '<stop offset="0" stop-color="#A855F7"/><stop offset="1" stop-color="#3B8BFF"/></linearGradient></defs>'
            f'<g fill="#14123B">{"".join(cells)}</g>{finder(.5, .5)}{finder(n-7.5, .5)}{finder(.5, n-7.5)}</svg>')


def sb_mockup():
    links = [('Follow on Facebook', '#1877F2'), ('Follow on Instagram', '#E1306C'), ('Follow on TikTok', '#FFFFFF'),
             ('Follow on Xiaohongshu', '#FF2442'), ('Chat on WhatsApp', '#25D366'), ('Leave a Google review', '#F4B400')]
    btns = ''.join(f'<span class="ph-link"><i style="background:{c}"></i>{t}</span>' for t, c in links)
    return f'''    <section class="tile tile-dark">
      <div class="wrap">
        {head('See it in action', 'Preview')}
        <div class="mock" data-rv>
          <div class="mock-qr"><div class="qr-card">{qr_svg()}<b>Scan to follow us</b><small>Your shop name</small></div></div>
          <div class="mock-arrow" aria-hidden="true">{ARROW}</div>
          <div class="phone" aria-label="Example Scan Buddy page on a phone" role="img">
            <div class="ph-top"><span class="ph-avatar">TCM</span><b>Your shop name</b><small>Follow us everywhere</small></div>
            <div class="ph-links">{btns}</div>
            <div class="ph-stat"><b>1,248</b> scans this month</div>
          </div>
        </div>
      </div>
    </section>
'''


AV_SCENES = [('Showcase', 'linear-gradient(160deg,#F3E8FF,#C4B5FD)', 'This changed my mornings'),
             ('Lifestyle', 'linear-gradient(160deg,#FFE4D6,#FDBA8C)', 'POV: your new favourite'),
             ('UGC style', 'linear-gradient(160deg,#DBEAFE,#93C5FD)', 'Honest review, 7 days in')]


def av_clips():
    clips = ''.join(f'<div class="clip" style="background:{bg}"><span class="clip-tag">{t}</span><span class="clip-prod"></span><span class="clip-cap">{cap}</span></div>' for t, bg, cap in AV_SCENES)
    return f'<div class="clips" role="img" aria-label="Three example AI videos in vertical format">{clips}</div>'


def av_mockup():
    scenes = [('Showcase', 'linear-gradient(160deg,#F3E8FF,#C4B5FD)', 'This changed my mornings'),
              ('Lifestyle', 'linear-gradient(160deg,#FFE4D6,#FDBA8C)', 'POV: your new favourite'),
              ('UGC style', 'linear-gradient(160deg,#DBEAFE,#93C5FD)', 'Honest review, 7 days in')]
    clips = ''.join(f'''<div class="clip" style="background:{bg}"><span class="clip-tag">{t}</span><span class="clip-prod"></span><span class="clip-cap">{cap}</span></div>''' for t, bg, cap in scenes)
    return f'''    <section class="tile tile-dark">
      <div class="wrap">
        {head('One photo in. Videos out.', 'Preview')}
        <div class="mock" data-rv>
          <div class="mock-in"><div class="prod-card"><span class="clip-prod big"></span><b>product.jpg</b><small>Your product photo</small></div></div>
          <div class="mock-arrow" aria-hidden="true">{ARROW}</div>
          <div class="clips" role="img" aria-label="Three example AI videos in vertical format">{clips}</div>
        </div>
      </div>
    </section>
'''


SB_FAQ = [
    ('What is Scan Buddy?', 'A smart QR code for your business. Customers scan once to follow your social media, chat on WhatsApp or leave a Google review, and you see every scan.'),
    ('Can Scan Buddy work as a Google review QR code?', 'Yes. One tap takes happy customers straight to your Google review page while they are still in the shop, next to your social and WhatsApp links.'),
    ('Do my customers need an app?', 'No. Any phone camera scans the code and opens your page in the browser.'),
    ('Can I change my links after printing?', 'Yes. Update your links any time and the same printed QR code keeps working.'),
    ('How much is Scan Buddy?', 'RM150 a month on the trial plan, or RM999 a year (save RM801). It covers Google, Xiaohongshu, Facebook and Dianping reviews. Scan Buddy is also included in the TCM Membership.'),
]
sb_body = tool_body(
    'scan-buddy', 'Scan Buddy: <span class="accent">one scan, every channel.</span>',
    'A smart QR code for your shop, packaging and events. Customers scan once to follow you on every platform, chat on WhatsApp or leave a Google review. You see every scan.',
    "Hi, I'd like to get Scan Buddy!", 'Scan Buddy demo video',
    [('Pick a plan', 'Start with the monthly trial, or save with the yearly plan.'), ('Add your links', 'Facebook, Instagram, TikTok, Xiaohongshu, WhatsApp and Google reviews.'),
     ('Print your QR', 'On your counter, packaging, menus, flyers and event booths.'), ('Watch the scans', 'See how many people scanned, and when.')],
    'Turn offline customers into online fans.',
    [('Every social in one scan', 'One QR code instead of five. Customers pick the platform they use.'),
     ('Grow followers offline', 'Turn walk-in customers and event visitors into followers you can reach again.'),
     ('More Google reviews', 'Send happy customers straight to your review page while they are still in the shop.'),
     ('WhatsApp in one tap', 'Customers start a chat with you instantly, ready for follow-up and repeat orders.'),
     ('Scan tracking', 'See scans by day, so you know which location or campaign brings customers.'),
     ('One QR per KOC & KOL', 'Give each influencer or event its own code and see which one really brings people in.')],
    sb_mockup(), SB_FAQ, 'Ready to connect offline to online?', 'WhatsApp us and we will set up Scan Buddy for your business.', ['qr', 'users', 'target', 'zap', 'calendar', 'megaphone'])

AV_FAQ = [
    ('Do I need to film anything?', 'No. Start from a product photo. AI creates the scenes, motion, captions and music. Add your own footage if you have it.'),
    ('How is TCM AI Video different from a free AI video generator?', 'It is built for selling: ad-ready formats, hooks and captions in English, 中文 and Bahasa, and our team to help when a video needs polish.'),
    ('What kind of videos can I make?', 'Product showcases, new scenes, AI model try-ons, UGC-style clips and short ads, in 9:16, 1:1 and 16:9.'),
    ('What photos work best?', 'Clear, well-lit product photos on a plain background give the best results.'),
    ('How do I get AI Video?', 'AI Video is included in the TCM Membership: RM350 a month, or RM250 a month on the yearly plan, together with Scan Buddy and the full course library.'),
]
av_body = tool_body(
    'ai-video', 'AI Video: <span class="accent">your product, made into ads.</span>',
    'Upload a product photo. AI turns it into ready-to-post marketing videos: model showcases, new backgrounds, UGC-style clips, captions and music. No filming, no editing.',
    "Hi, I'd like to get AI Video!", 'AI Video demo video',
    [('Upload your product', 'A clear product photo or your product link.'), ('Pick a style', 'Showcase, lifestyle scene, model try-on or UGC style.'),
     ('AI makes the video', 'Scenes, motion, captions and music, generated for you.'), ('Download & post', 'Ready for TikTok, Reels, Facebook and Xiaohongshu.')],
    'What you can make.',
    [('Product showcases', 'Clean, eye-catching product videos that show every angle.'),
     ('Background & scene change', 'Put your product in a kitchen, a café or a studio without a shoot.'),
     ('Model & outfit try-on', 'Show clothing and accessories on AI models, in different looks and poses.'),
     ('UGC-style clips', 'Natural, creator-style videos that feel native on TikTok and Reels.'),
     ('Captions that sell', 'Hook, body and call to action written for you, in English, 中文 or Bahasa.'),
     ('Every format', '9:16 for TikTok and Reels, 1:1 for feeds, 16:9 for YouTube and websites.')],
    av_mockup(), AV_FAQ, 'Make your next ad in minutes.', 'WhatsApp us to get AI Video for your business.', ['video', 'layers', 'users', 'sparkles', 'pen', 'zap'])

# =================================================================== MEMBERSHIP
MEM_FAQ = [
    ('What is included in the TCM Membership?', 'Every TCM AI tool (Scan Buddy and AI Video), the full video course library, our marketing resources (templates, checklists and prompts) and a live class every month. A coach guides you step by step and checks your progress.'),
    ('How much is the TCM Membership?', 'RM350 a month, or RM250 a month when you sign up for a year (RM3,000 billed yearly). The yearly plan saves you RM1,200.'),
    ('How do I log in after I pay?', 'WhatsApp us after payment. Our admin sends your personal invite code, and you use it to log in and start.'),
    ('Will the trainer disappear after a few lessons?', 'No. We go live every month with the newest tools and tactics, answer your questions and guide you step by step until your marketing runs.'),
    ('I joined a TCM offline course. Do I get anything?', 'Yes. Offline course participants get their first 6 months of the Membership free, so you can keep learning and use every tool after class.'),
    ('What if I cannot learn it?', 'Follow the classes, do the practice tasks, and if you still cannot do it, we refund you 100%. Terms and conditions apply; WhatsApp us for the details.'),
]
mem_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Product', 'name': 'TCM Membership', 'description': 'Membership with every TCM AI tool, our marketing resources and the full AI and marketing video course library.',
     'brand': PROVIDER, 'offers': [
         {'@type': 'Offer', 'name': 'Monthly', 'price': '350', 'priceCurrency': 'MYR', 'url': SITE + 'membership'},
         {'@type': 'Offer', 'name': 'Yearly', 'price': '3000', 'priceCurrency': 'MYR', 'url': SITE + 'membership'}]},
    faq_ld(MEM_FAQ)]}
MEM_C = "Hi, I joined a TCM offline course and would like my 6 free months of the Membership."
MEM_MSG = MEM_Y
MEM_INSIDE = [
    ('Every AI tool', 'Scan Buddy for reviews and followers, AI Video for product ads, and every new tool we release.', '/ai-tools', 'photo', 'mem-tools', 'Customer scanning a review QR code at a counter beside a laptop running an AI video tool'),
    ('The full course library', 'Every marketing platform and all 7 AI modules, in short episodes you can finish.', '/ai-classes', 'photo', 'mem-library', 'Member browsing a library of video lessons on a monitor'),
    ('Marketing resources', 'The checklists, calendars and prompts we use for our own clients.', '#plans', 'photo', 'mem-resources', 'Campaign checklist, content calendar and ad copy prompts on a desk'),
]
PLAN_FEATS = ['Scan Buddy and AI Video', 'Full marketing and AI course library', 'New hands-on classes every month', 'Templates, checklists and prompts', "Can't learn it? Full refund"]


def plan(name, price, unit, note, msg, label, best=False):
    flag = '<span class="plan-flag">Save 40%</span>' if best else ''
    return f'''<div class="plan{' plan-best' if best else ''}" data-rv>
            <div class="plan-top"><span class="plan-name">{name}</span>{flag}</div>
            <div class="plan-price"><span class="plan-cur">RM</span>{price}<span class="plan-unit">{unit}</span></div>
            <p class="plan-note">{note}</p>
            {ticks(PLAN_FEATS)}
            <a class="btn {'btn-primary' if best else 'btn-ghost'}" href="{wa(msg)}" onclick="{CONV}" target="_blank" rel="noopener">{label}</a>
          </div>'''


MEM_FEATS = ['Scan Buddy and AI Video', 'Full marketing and AI course library', 'A live class every month', 'A coach who guides and checks your work', 'Templates, checklists and prompts', '100% refund promise']
MEM_PROMISES = [
    (Z('Not a screen recording', '不是录屏课'), Z('Every lesson is filmed like a show, with several camera angles, on-screen animation and clear steps. You stay awake, and you finish it.', '每一课都像节目一样拍摄：多个机位、画面动画、步骤清楚。你不会看到睡着，而且看得完。')),
    (Z('A live class every month', '每月一堂直播课'), Z('Every month we go live with the newest tools and tactics, and you ask your questions on the spot. You always learn the latest version.', '每个月我们都会开直播，带来最新的工具和做法，你可以当场提问。你学到的永远是最新版本。')),
    (Z('A coach who stays with you', '一路陪着你的教练'), Z('We guide you step by step and check your work. No paying for a few lessons and watching the trainer disappear.', '我们一步一步带着你做，并检查你的进度。不会付了钱、上几堂课，导师就不见了。')),
    (Z('Marketing on autopilot', '营销自动化'), Z('Our goal is your marketing running with AI: content, replies and follow-ups set up and working for you.', '我们的目标是让你的营销用 AI 跑起来：内容、回复和跟进都设置好，替你工作。')),
]
mem_promises = ''.join(f'<li data-rv><b>{i:02d}</b><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(MEM_PROMISES, 1))
mem_body = f'''    <section class="hero">
      <div class="hero-grid">
        <div>
          <div class="crumbs rise" style="margin-bottom:14px"><a href="/">Home</a> / <a href="/marketing-classes">Academy</a> / Membership</div>
          <div class="eyebrow rise">TCM Membership</div>
          <h1 class="h1 rise mem-h1" style="animation-delay:.05s">Every AI tool and every course, <span class="accent">one membership.</span></h1>
          <p class="lede rise" style="animation-delay:.15s">{esc(Z('Tools, lessons and a coach to put your marketing on autopilot with AI. From RM250 a month.', '工具、课程，加上一路带着你的教练，用 AI 让你的营销自动化。每月 RM250 起。'))}</p>
          <div class="btn-row rise" style="animation-delay:.3s">
            <a class="btn btn-primary" href="#plans">See plans {ARROW}</a>
            <a class="btn btn-ghost" href="#inside">What is inside</a>
          </div>
        </div>
        <div class="rise" style="animation-delay:.2s">{banner('mem-class', Z('Marketing trainer teaching a full class of students how to use AI', '营销导师在教一整班学员使用 AI')).replace(' data-rv', '')}</div>
      </div>
      <div style="height:88px"></div>
    </section>

    <section class="tile tile-raise mem" id="inside">
      <div class="wrap">
        {head('What you get', 'Inside the membership')}
        {svc_cards(MEM_INSIDE, 'svc-grid g3 mem-cards')}
      </div>
    </section>

    <section class="tile tile-dark mem" id="why">
      <div class="wrap">
        {head(esc(Z('We do not teach and', '我们不会教完就')) + ' <span class="accent">' + esc(Z('disappear.', '消失。')) + '</span>', esc(Z('Why members stay', '会员为什么留下来')), esc(Z('You get the newest lessons, a live class every month and someone checking that you actually get it done.', '你会得到最新的课程、每月一堂直播课，还有人盯着你真的把事情做出来。')))}
        <div class="why-split">
          <figure class="banner" data-rv><img src="/assets/img/mem-live.webp" alt="{esc(Z('Instructor running a live online class with students on screen', '导师正在进行线上直播课，屏幕上是学员'))}" width="1360" height="768" loading="lazy"></figure>
          <ol class="promises">{mem_promises}</ol>
        </div>
      </div>
    </section>

    <section class="tile tile-raise mem" id="plans">
      <div class="wrap">
        {head('Choose your plan', 'Pricing')}
        <div class="plans">
          {price_plan(Z('Monthly', '月付'), MEM['m'], Z('/month', '/月'), esc(Z('Billed monthly. Cancel anytime.', '按月付款，随时可以取消。')), MEM_FEATS, MEM_M, Z('Subscribe monthly', '订阅月付'))}
          {price_plan(Z('Yearly', '年付'), MEM['y'], Z('/month', '/月'), esc(Z('RM' + MEM['ytotal'] + ' billed yearly.', '每年付 RM' + MEM['ytotal'] + '。')) + f' <s>RM{MEM["full"]}</s>', MEM_FEATS, MEM_Y, Z('Subscribe yearly', '订阅年付'), flag=Z('Save RM' + MEM['save'], '省 RM' + MEM['save']), best=True)}
        </div>
        {join_steps('mem')}
        <div class="offer" data-rv>
          <div><b>Joined a TCM offline course?</b><span>Your first 6 months of the Membership are free.</span></div>
          <a class="btn btn-ghost btn-sm" href="{wa(MEM_C)}" target="_blank" rel="noopener">Claim on WhatsApp</a>
        </div>
        <div class="offer" data-rv>
          <div><b>{esc(Z('Only need Scan Buddy?', '只需要 Scan Buddy？'))}</b><span>{esc(Z('RM' + str(SB['m']) + ' a month, or RM' + str(SB['y']) + ' a year.', '每月 RM' + str(SB['m']) + '，或每年 RM' + str(SB['y']) + '。'))}</span></div>
          <a class="btn btn-ghost btn-sm" href="/scan-buddy#plans">{esc(Z('See Scan Buddy plans', '查看 Scan Buddy 配套'))}</a>
        </div>
      </div>
    </section>

{guarantee('lessons')}

{faq_section(MEM_FAQ, 'tile-raise')}

{cta('Start this month.', 'One membership. Every tool and every course.', 'Subscribe on WhatsApp', MEM_Y)}'''

# =================================================================== AI TOOLS HUB
TOOLS_FAQ = [
    ('What AI tools does TCM offer?', 'Two so far. Scan Buddy is a smart QR code that turns offline customers into followers, WhatsApp chats and Google reviews. AI Video turns a product photo into ready-to-post video ads.'),
    ('Do I need technical skills to use them?', 'No. If you can use WhatsApp, you can use both. Add your links or upload a photo, and the tool does the rest.'),
    ('How much do the AI tools cost?', 'Scan Buddy alone is RM150 a month, or RM999 a year. Both tools and every course are included in the TCM Membership: RM350 a month, or RM250 a month on the yearly plan.'),
    ('Which tool should I start with?', 'Have a shop, a booth or packaging? Start with Scan Buddy. Sell products online and need more content? Start with AI Video.'),
    ('Will you add more tools?', 'Yes. Members get every new tool we release at no extra cost.'),
]
tools_ld = {'@context': 'https://schema.org', '@graph': [faq_ld(TOOLS_FAQ)]}
tools_body = f'''{hero([("Home", "/"), ("AI Tools", "")], 'AI tools that <span class="accent">sell for you.</span>',
       'Built by TCM for real shops and brands. No coding, no setup headaches.',
       btns(('Join the Membership', '/membership'), ('See the tools', '#tools')), eyebrow='AI Tools')}

    <section class="tile tile-raise" id="tools">
      <div class="wrap">
        {head('Two tools, one membership', 'The tools')}
        <div class="ways">
          <div class="way tool" data-rv>
            <div class="tool-art"><div class="qr-card">{qr_svg()}<b>Scan to follow us</b></div></div>
            <div class="way-k">Offline to online</div>
            <div class="way-t">Scan Buddy</div>
            <p class="way-d">One smart QR code for your shop, packaging and events.</p>
            {ticks(['Follow on every platform in one scan', 'More Google reviews', 'WhatsApp chats in one tap', 'See every scan'])}
            <a class="btn btn-primary" href="/scan-buddy">Explore Scan Buddy</a>
          </div>
          <div class="way tool" data-rv>
            <div class="tool-art">{av_clips()}</div>
            <div class="way-k">Photo to video</div>
            <div class="way-t">AI Video</div>
            <p class="way-d">Upload a product photo. Get ready-to-post video ads.</p>
            {ticks(['No filming, no editing', 'Showcase, lifestyle and UGC styles', 'Captions in English, 中文 and Bahasa', 'Every format: 9:16, 1:1, 16:9'])}
            <a class="btn btn-primary" href="/ai-video">Explore AI Video</a>
          </div>
        </div>
        <div class="offer" data-rv style="max-width:none;margin-top:20px">
          <div><b>Both tools are included in the Membership.</b><span>RM350 a month, or RM250 a month on the yearly plan. Every class is included too.</span></div>
          <a class="btn btn-ghost btn-sm" href="/membership">See plans</a>
        </div>
      </div>
    </section>

{faq_section(TOOLS_FAQ)}

{cta('Put AI to work in your business.', 'WhatsApp us and we will set up your tools.', 'Join on WhatsApp', "Hi, I'd like to use the TCM AI tools!")}'''

tool_ld = lambda faq: {'@context': 'https://schema.org', '@graph': [faq_ld(faq)]}

# =================================================================== WRITE
# ---------------------------------------------------------------- Insights (articles)
import insights as INS
import datetime as _dt

INS_LBL = INS.LABELS
_d = _dt.date.fromisoformat(INS.DATE)
INS_DATE_TXT = INS.T(_d.strftime('%-d %b %Y'), f'{_d.year}年{_d.month}月{_d.day}日')


def _plain(a):
    """All English text of an article, for the reading time."""
    out = [a['h1'], a['lede']]
    for b in a['blocks']:
        for x in b[1:]:
            if isinstance(x, str):
                out.append(x)
            elif isinstance(x, list):
                for y in x:
                    out.extend(y if isinstance(y, tuple) else [y])
    return ' '.join(s for s in out if isinstance(s, str))


def _mins(a):
    return max(3, round(len(_plain(a).split()) / 200))


def _block(b):
    k = b[0]
    if k == 'tldr':
        return f'<div class="post-tldr" data-rv><b>{esc(b[1])}</b><p>{esc(b[2])}</p></div>'
    if k == 'h2':
        return f'<h2 class="post-h2">{esc(b[1])}</h2>'
    if k == 'p':
        return f'<p>{esc(b[1])}</p>'
    if k == 'tip':
        return f'<aside class="post-tip"><p>{esc(b[1])}</p></aside>'
    if k == 'prompt':
        return f'<div class="post-prompt"><span>{esc(INS_LBL["prompt"])}</span><p>{esc(b[1])}</p></div>'
    if k in ('ul', 'ol'):
        items = ''.join(f'<li><b>{esc(lead)}</b> {esc(text)}</li>' for lead, text in b[1])
        return f'<{k} class="post-list">{items}</{k}>'
    if k == 'table':
        cols, rows = b[1], b[2]
        th = '<th></th>' + ''.join(f'<th scope="col">{esc(c)}</th>' for c in cols)
        tr = ''.join(f'<tr><th scope="row">{esc(r)}</th>' + ''.join(f'<td>{esc(c)}</td>' for c in cells) + '</tr>' for r, cells in rows)
        return f'<div class="post-table"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    raise ValueError(k)


def _card(a):
    tags = ''.join(f'<span>{esc(t)}</span>' for t in a['tags'])
    return f'''<a class="post-card" href="/insights/{a['slug']}" data-rv>
          <div class="post-tags">{tags}</div>
          <h3 class="h3">{esc(a['short'])}</h3>
          <p>{esc(a['card'])}</p>
          <span class="post-more">{esc(INS_LBL['readmore'])} {ARROW}</span>
        </a>'''


def h1_accent(key):
    first, second = INS.H1_PARTS[key]
    return f'{esc(first)} <span class="accent">{esc(second)}</span>'


def article_body(a):
    meta = (f'<div class="post-meta rise" style="animation-delay:.3s"><span><span>{esc(INS_LBL["updated"])}</span> <time datetime="{INS.DATE}">{esc(INS_DATE_TXT)}</time></span>'
            f'<span>{_mins(a)} <span>{esc(INS_LBL["read"])}</span></span><span>{esc(INS_LBL["by"])}</span></div>')
    href, nh, nl, nb = a['next']
    others = ''.join(_card(o) for o in INS.ARTICLES if o is not a)
    blocks = '\n          '.join(_block(b) for b in a['blocks'])
    return f'''{hero([(INS_LBL['home'], '/'), (INS_LBL['insights'], '/insights'), (a['short'], '')], h1_accent(a['slug']), esc(a['lede']), extra=meta)}
    <section class="tile post-wrap">
      <article class="post">
          {blocks}
          <div class="post-next" data-rv>
            <h2 class="h3">{esc(nh)}</h2>
            <p>{esc(nl)}</p>
            <a class="btn btn-primary" href="{href}">{esc(nb)} {ARROW}</a>
          </div>
      </article>
    </section>
{faq_section(a['faq'], title=INS_LBL['faq'])}
    <section class="tile">
      {head(esc(INS_LBL['more']), esc(INS_LBL['insights']))}
      <div class="post-grid">{others}</div>
    </section>
{cta('Not sure where to start? <span class="accent">Ask us.</span>', 'Tell us about your business and we will point you to the right next step: a service, a class or a tool.', 'WhatsApp us', "Hi, I read your article and have a question.")}'''


def article_ld(a):
    url = SITE + 'insights/' + a['slug']
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BlogPosting', '@id': url + '#article', 'headline': a['h1'], 'description': a['desc'], 'url': url,
         'mainEntityOfPage': url, 'datePublished': INS.DATE, 'dateModified': INS.DATE, 'inLanguage': 'en',
         'image': SITE + 'assets/tcm-logo.jpg', 'keywords': ', '.join(a['tags']),
         'author': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID}, 'isPartOf': {'@id': SITE + 'insights#blog'}},
        faq_ld(a['faq'])]}


insights_body = f'''{hero([(INS_LBL['home'], '/'), (INS_LBL['insights'], '')], h1_accent('index'), esc(INS.INDEX['lede']), eyebrow=esc(INS_LBL['insights']))}
    <section class="tile">
      <div class="post-grid">{''.join(_card(a) for a in INS.ARTICLES)}</div>
    </section>
{cta('Want this done for you? <span class="accent">Let&#8217;s talk.</span>', 'Our team runs SEO, ads, content and AI for brands in Malaysia and Singapore, or teaches your team to do it.', 'WhatsApp us', "Hi, I'd like to talk about my marketing.")}'''
insights_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Blog', '@id': SITE + 'insights#blog', 'name': 'TCM Insights', 'url': SITE + 'insights', 'publisher': {'@id': ORG_ID},
     'description': INS.INDEX['desc'], 'inLanguage': ['en', 'zh-Hans'],
     'blogPost': [{'@type': 'BlogPosting', 'headline': a['h1'], 'url': SITE + 'insights/' + a['slug'], 'datePublished': INS.DATE} for a in INS.ARTICLES]}]}

INSIGHT_PAGES = [('insights.html', 'insights', INS.INDEX['title'], INS.INDEX['desc'], 'insights', insights_ld, insights_body, ())] + [
    (f'insights/{a["slug"]}.html', f'insights/{a["slug"]}', a['title'], a['desc'], 'insights', article_ld(a), article_body(a), ()) for a in INS.ARTICLES]


# ---------------------------------------------------------------- SEO, AEO and GEO layer
# One Organization entity (@id ORG_ID) that every page points to, so Google and AI
# answer engines see a single, consistent "Top Creation Media" with its people,
# services, languages and markets (Malaysia and Singapore).
SOCIAL = ['https://facebook.com/topcreationmedia', 'https://instagram.com/topcreationmedia', 'https://tiktok.com/@topcreationmedia']
MARKETS = [{'@type': 'Country', 'name': 'Malaysia'}, {'@type': 'Country', 'name': 'Singapore'}]
ORG = {
    '@type': ['Organization', 'ProfessionalService'], '@id': ORG_ID,
    'name': 'Top Creation Media', 'alternateName': ['TCM', 'Top Creation Media Sdn Bhd'],
    'url': SITE, 'logo': SITE + 'assets/tcm-logo.jpg', 'image': SITE + 'assets/tcm-logo.jpg',
    'slogan': 'Your Marketing, Simplified.',
    'description': 'Top Creation Media (TCM) is a digital marketing agency and AI and marketing training studio serving Malaysia and Singapore: SEO, social media marketing, Google and Meta ads, TikTok, Xiaohongshu, KOL marketing, video and livestream production, plus hands-on AI and digital marketing courses and corporate training.',
    'telephone': '+' + PHONE, 'areaServed': MARKETS,
    'address': {'@type': 'PostalAddress', 'addressCountry': 'MY'},
    'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'sales', 'telephone': '+' + PHONE, 'url': f'https://wa.me/{PHONE}',
                      'areaServed': ['MY', 'SG'], 'availableLanguage': ['English', 'Chinese', 'Malay']}],
    'availableLanguage': ['English', 'Chinese', 'Malay'],
    'sameAs': SOCIAL,
    'employee': [{'@type': 'Person', 'name': n, 'jobTitle': r, 'worksFor': {'@id': ORG_ID}} for _, n, r in TEAM],
    'knowsAbout': [l for _, links in INDEX[:3] for l, _ in links] + ['Answer engine optimisation (AEO)', 'Generative engine optimisation (GEO)'],
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Marketing services', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': l, 'url': SITE + h.lstrip('/').split('#')[0], 'areaServed': MARKETS, 'provider': {'@id': ORG_ID}}}
        for _, links in INDEX[:2] for l, h in links]},
}
home_ld['@graph'][0] = ORG
home_ld['@graph'][1] = {'@type': 'WebSite', '@id': SITE + '#website', 'name': 'Top Creation Media', 'url': SITE,
                        'inLanguage': ['en', 'zh-Hans'], 'publisher': {'@id': ORG_ID}}

# Services: one Service per platform and offer, all in Malaysia and Singapore
dfy_ld['@graph'][0].update({'areaServed': MARKETS, 'name': 'Digital marketing services: SEO, social media, ads, video and KOL',
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Done-For-You marketing', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n, 'serviceType': n, 'areaServed': MARKETS, 'provider': {'@id': ORG_ID}}}
        for n in ['Facebook & Instagram ads', 'TikTok marketing & TikTok Live', 'Google SEO & Google Ads', 'Xiaohongshu (RED) marketing',
                  'AI video production', 'Websites & landing pages', 'Video production', 'Livestream studio', 'KOC & KOL marketing',
                  'IP & personal branding', 'Events', 'Corporate AI & marketing training']]}})

# Courses: who teaches, in which languages, how they are run
def course_extra(teaches):
    return {'inLanguage': ['en', 'zh'], 'educationalLevel': 'Beginner', 'teaches': teaches, 'isAccessibleForFree': False,
            'audience': {'@type': 'Audience', 'audienceType': 'Business owners, marketing teams and staff in Malaysia and Singapore'},
            'hasCourseInstance': [
                {'@type': 'CourseInstance', 'courseMode': 'Onsite', 'location': {'@type': 'Place', 'name': 'Top Creation Media studio', 'address': {'@type': 'PostalAddress', 'addressCountry': 'MY'}}},
                {'@type': 'CourseInstance', 'courseMode': 'Online', 'courseWorkload': 'PT1H'}]}
academy_ld['@graph'][0].update(course_extra(['Facebook and Instagram ads', 'TikTok ads and TikTok Live', 'Google Ads and SEO', 'Xiaohongshu marketing', 'Ad tracking and reporting']))
ai_ld['@graph'][0].update(course_extra(['ChatGPT, Claude and Gemini for business', 'AI video', 'AI graphics', 'AI captions and copywriting', 'AI websites and SEO', 'AI automation', 'AI marketing']))
ai_ld['@graph'][0]['name'] = 'AI Course & AI Training: AI Video, Graphics, Captions, Websites & Automation'
mem_ld['@graph'][0]['brand'] = {'@id': ORG_ID}
pf_ld.update({'isPartOf': {'@id': SITE + '#website'}, 'about': {'@id': ORG_ID}})

# AI tools as web apps, available through the Membership
def app_ld(name, desc, slug):
    return {'@type': 'SoftwareApplication', 'name': name, 'description': desc, 'url': SITE + slug, 'applicationCategory': 'BusinessApplication',
            'operatingSystem': 'Web', 'publisher': {'@id': ORG_ID},
            'offers': {'@type': 'Offer', 'price': '350', 'priceCurrency': 'MYR', 'description': 'Included in the TCM Membership (RM350 a month)', 'url': SITE + 'membership'}}
SB_APP = app_ld('Scan Buddy', 'One smart QR code that turns offline customers into followers, WhatsApp chats and Google reviews, with scan tracking.', 'scan-buddy')
AV_APP = app_ld('AI Video', 'Turns a product photo into ready-to-post marketing videos: showcases, new backgrounds, model try-ons, UGC-style clips and captions.', 'ai-video')
tools_ld['@graph'].insert(0, {'@type': 'ItemList', 'name': 'TCM AI tools', 'itemListElement': [
    {'@type': 'ListItem', 'position': 1, 'item': SB_APP}, {'@type': 'ListItem', 'position': 2, 'item': AV_APP}]})


def build_seo_files(pages):
    """sitemap.xml (with lastmod and en/zh alternates), robots.txt and llms.txt."""
    import hashlib
    import datetime
    state_f = os.path.join(ROOT, 'tools', 'sitemap_state.json')
    state = json.load(open(state_f)) if os.path.exists(state_f) else {}
    today = datetime.date.today().isoformat()
    rows = []
    for fname, slug, *_ in pages:
        for pre in ('', 'zh/'):
            f = os.path.join(OUT, pre + fname)
            h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
            key = pre + fname
            if state.get(key, [None])[0] != h:
                state[key] = [h, today]
            en, zh = SITE + slug, SITE + 'zh/' + slug
            rows.append(f'  <url>\n    <loc>{SITE}{pre}{slug}</loc>\n    <lastmod>{state[key][1]}</lastmod>\n'
                        f'    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>\n'
                        f'    <xhtml:link rel="alternate" hreflang="zh-Hans" href="{zh}"/>\n'
                        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>\n  </url>\n')
    json.dump(state, open(state_f, 'w'), indent=1, sort_keys=True)
    with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + ''.join(rows) + '</urlset>\n')

    # Search and AI answer engines are welcome: being cited by ChatGPT, Gemini, Perplexity
    # and Claude is part of the GEO plan.
    bots = ['Googlebot', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User',
            'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot', 'Applebot-Extended', 'DuckDuckBot', 'YandexBot']
    robots = ''.join(f'User-agent: {b}\n' for b in bots) + 'Allow: /\n\nUser-agent: *\nAllow: /\n\n' + f'Sitemap: {SITE}sitemap.xml\n'
    open(os.path.join(OUT, 'robots.txt'), 'w').write(robots)

    # llms.txt: a plain summary for AI assistants (llmstxt.org format)
    def ans(faq):
        return ''.join(f'- **{q}** {a}\n' for q, a in faq)
    page_lines = ''.join(f'- [{t.split(" | ")[0]}]({SITE}{slug}): {d}\n' for _, slug, t, d, *_ in pages)
    zh_lines = ''.join(f'- [{t.split(" | ")[0]} (中文)]({SITE}zh/{slug})\n' for _, slug, t, d, *_ in pages)
    team = ''.join(f'- {n}: {r}\n' for _, n, r in TEAM)
    llms = f'''# Top Creation Media (TCM)

> Digital marketing agency and AI & marketing training studio serving Malaysia and Singapore. TCM runs SEO, social media marketing, Google and Meta ads, TikTok and TikTok Live, Xiaohongshu (RED), KOL/KOC campaigns, video and livestream production for brands, and teaches business owners and staff to do it themselves through hands-on marketing and AI courses, corporate training and the TCM Membership.

## Key facts
- Name: Top Creation Media (TCM), Top Creation Media Sdn Bhd
- Markets: Malaysia and Singapore
- Languages: English, Chinese (中文), Malay
- Contact: WhatsApp +{PHONE} (https://wa.me/{PHONE})
- Website: {SITE} (Chinese: {SITE}zh/)
- Social: {", ".join(SOCIAL)}
- Two ways to work with TCM: Done-For-You marketing services, or learn it yourself in the Marketing Academy and AI Academy
- TCM Membership: RM350 a month, or RM250 a month on the yearly plan (RM3,000 a year, save RM1,200). Includes every TCM AI tool (Scan Buddy, AI Video), the full course library and a live class every month with a coach. After payment, members get an invite code on WhatsApp to log in. Offline course participants get the first 6 months free.
- Scan Buddy alone: RM150 a month (trial), or RM999 a year (save RM801). Covers Google, Xiaohongshu, Facebook and Dianping reviews.
- Courses: beginner-friendly, no coding needed, taught hands-on on your own accounts; full refund if you follow the class and still cannot do it (terms apply)
- In-house video and livestream studio

## Team
{team}
## Pages
{page_lines}
## Chinese pages
{zh_lines}
## Frequently asked questions
{ans(HOME_FAQ)}'''
    open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf8').write(llms)


PAGES = [
    ('index.html', '', 'Digital Marketing Agency Malaysia & Singapore | Top Creation Media',
     'Digital marketing agency in Malaysia and Singapore: SEO, social media, Google & Meta ads, TikTok, Xiaohongshu, KOL and video, plus AI training for your team.',
     'home', home_ld, home_body, ('/portfolio-data.js',)),
    ('marketing-services.html', 'marketing-services', 'SEO, Social Media & Ads Agency Malaysia | Top Creation Media',
     'SEO and social media agency in Malaysia and Singapore: Facebook, Instagram, TikTok Live, Google SEO & Ads, Xiaohongshu, video, livestream and KOL, done for you.',
     'services', dfy_ld, dfy_body, ()),
    ('marketing-classes.html', 'marketing-classes', 'Digital Marketing Course Malaysia | Facebook, TikTok, Google & RED',
     'Learn Facebook, Instagram, TikTok, Google and Xiaohongshu marketing from A to Z, hands-on. Beginner-friendly classes in Malaysia with a 100% refund guarantee.',
     'academy', academy_ld, academy_body, ()),
    ('ai-classes.html', 'ai-classes', 'AI Course & AI Training Malaysia | No Coding Needed | TCM',
     'AI course and corporate AI training in Malaysia, no coding needed: ChatGPT, Claude, Gemini, AI video, graphics, captions, websites and automation. Full refund guarantee.',
     'ai', ai_ld, ai_body, ()),
    ('portfolio.html', 'portfolio', 'Portfolio | Video, Ads & KOL Work in Malaysia & Singapore | TCM',
     'See Top Creation Media work: short-form videos, ad results dashboards and brand projects for clients across Malaysia and Singapore.',
     'portfolio', pf_ld, pf_body, ('/portfolio-data.js', '/portfolio.js')),
    ('scan-buddy.html', 'scan-buddy', 'Scan Buddy | Smart QR Code for Social Media | TCM',
     'Scan Buddy: one smart QR code for Google, Xiaohongshu, Facebook and Dianping reviews, followers and WhatsApp chats. RM150/month or RM999/year.',
     'scan', {'@context': 'https://schema.org', '@graph': [SB_APP, faq_ld(SB_FAQ)]}, sb_body, ()),
    ('ai-tools.html', 'ai-tools', 'AI Tools for Business Malaysia | Scan Buddy & AI Video | TCM',
     'TCM AI tools for Malaysian businesses: Scan Buddy smart QR codes and AI Video, which turns product photos into video ads. Included in the Membership.',
     'tools', tools_ld, tools_body, ()),
    ('ai-video.html', 'ai-video', 'AI Video | Turn Product Photos into Video Ads | TCM',
     'AI Video turns a product photo into ready-to-post marketing videos: showcases, new backgrounds, model try-ons, UGC-style clips and captions.',
     'aivideo', {'@context': 'https://schema.org', '@graph': [AV_APP, faq_ld(AV_FAQ)]}, av_body, ()),
    ('membership.html', 'membership', 'TCM Membership | AI Tools & Marketing Courses from RM250/mo',
     'TCM Membership: every AI tool, the full course library and a live class every month with a coach. RM350/month, or RM250/month yearly. 100% refund promise.',
     'member', mem_ld, mem_body, ()),
] + INSIGHT_PAGES

NOT_FOUND_LINKS = [
    ('/', 'Home', '首页'),
    ('/marketing-services', 'Marketing services', '营销服务'),
    ('/marketing-classes', 'Marketing Academy', '营销课程'),
    ('/ai-classes', 'AI Academy', 'AI 课程'),
    ('/membership', 'Membership', '会员'),
    ('/portfolio', 'Portfolio', '作品集'),
]
nf_links = ''.join(f'<a class="btn btn-ghost" href="{h}">{esc(en)} <span lang="zh-Hans">· {zh}</span></a>' for h, en, zh in NOT_FOUND_LINKS)
nf_body = f'''    <section class="hero nf">
      <div class="wrap nf-wrap">
        <div class="eyebrow rise">404</div>
        <h1 class="h1 rise" style="animation-delay:.05s">This page has <span class="accent">moved.</span></h1>
        <p class="lede rise" style="animation-delay:.15s">The link may be from our old website. Pick where you were heading, or message us and we will help.</p>
        <p class="lede rise nf-zh" lang="zh-Hans" style="animation-delay:.2s"><span class="nb">这个页面已经搬家或不存在。</span><span class="nb">请从下面选择，</span><span class="nb">或直接 WhatsApp 我们。</span></p>
        <div class="nf-links rise" style="animation-delay:.3s">{nf_links}</div>
        <div class="btn-row rise" style="animation-delay:.4s">
          <a class="btn btn-primary" href="{wa("Hi, I found a broken link on your website.")}" target="_blank" rel="noopener">WhatsApp us {ARROW}</a>
        </div>
      </div>
    </section>
'''


def not_found_page():
    """deploy/404.html: Vercel serves it for any unknown path. Not indexed, no canonical."""
    html_ = page('', 'Page not found | Top Creation Media', 'This page has moved or no longer exists.', '', {}, nf_body)
    import re as _re
    html_ = _re.sub(r'  <link rel="(canonical|alternate)"[^>]*>\n', '', html_)
    html_ = html_.replace('<meta property="og:url" content="' + SITE + '">\n  ', '')
    html_ = html_.replace('  <meta name="theme-color"', '  <meta name="robots" content="noindex">\n  <meta name="theme-color"', 1)
    html_ = html_.replace('<script type="application/ld+json">{}</script>\n', '')
    return html_


if __name__ == '__main__':
    for fname, slug, title, desc, cur, ld, body, scripts in PAGES:
        os.makedirs(os.path.dirname(os.path.join(OUT, fname)), exist_ok=True)
        with open(os.path.join(OUT, fname), 'w', encoding='utf8') as f:
            f.write(page(slug, title, desc, cur, ld, body, scripts))
        print(f'wrote {fname:24} title={len(title):3} desc={len(desc):3}')
    import sys
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'i18n'))
    import build_zh
    build_zh.ZH.update(INS.PAIRS)
    build_zh.PAGES.update(slug for _, slug, *_ in INSIGHT_PAGES)
    build_zh.build_all()
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf8') as f:
        f.write(not_found_page())
    print('wrote 404.html')
    build_seo_files(PAGES)
    print('wrote sitemap.xml, robots.txt, llms.txt')
