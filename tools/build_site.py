"""Builds every page of topcreation.media into deploy/.

Run:  python3 tools/build_site.py
Edit the text below, run it again, commit. Videos and testimonials live in
deploy/site-media.js, portfolio items in deploy/portfolio-data.js, and
behind-the-scenes photos in deploy/assets/bts/ (see the README there).
"""
import html as H
import json
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'deploy')
SITE = 'https://topcreation.media/'
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
NAV = [
    ('home', '/', 'Home'),
    ('social', '/social-media', 'Social Media'),
    ('ai', '/ai-classes', 'AI Classes'),
    ('portfolio', '/portfolio', 'Portfolio'),
    ('scan', '/scan-buddy', 'Scan Buddy'),
    ('aivideo', '/ai-video', 'AI Video'),
]
SOCIAL_KEYS = ('social', 'services', 'academy')
AI_MENU = [('m-know-your-ai-tools', 'Know your AI tools'), ('m-ai-video', 'AI video'), ('m-ai-graphics', 'AI graphics'),
           ('m-ai-website-builder-ai-seo', 'AI website &amp; SEO'), ('m-ai-captions-hook-body-cta', 'AI captions'),
           ('m-ai-system-flow', 'AI system flow'), ('m-ai-marketing', 'AI marketing')]


def nav(cur):
    def cur_attr(key):
        hit = key == cur or (key == 'social' and cur in SOCIAL_KEYS)
        return ' aria-current="page"' if hit else ''

    items = []
    for key, href, label in NAV[1:]:
        if key == 'social':
            items.append(f'''<div class="dd">
          <a href="{href}"{cur_attr(key)}>{label}</a>
          <div class="dd-menu">
            <a href="/social-media">Overview<small>Compare the two ways to grow</small></a>
            <a href="/marketing-services">Done-For-You<small>We run your marketing</small></a>
            <a href="/marketing-classes">Marketing Academy<small>Learn to run it yourself</small></a>
          </div>
        </div>''')
        elif key == 'ai':
            mods = ''.join(f'<a href="/ai-classes#{mid}">{name}</a>' for mid, name in AI_MENU)
            items.append(f'''<div class="dd">
          <a href="{href}"{cur_attr(key)}>{label}<span class="badge">New</span></a>
          <div class="dd-menu">
            <a href="/ai-classes">All AI classes<small>7 modules, no coding needed</small></a>
            {mods}
          </div>
        </div>''')
        else:
            badge = ''
            items.append(f'<a href="{href}"{cur_attr(key)}>{label}{badge}</a>')
    sub = [('home', '/', 'Home'), ('social', '/social-media', 'Social Media'), ('services', '/marketing-services', 'Done-For-You'),
           ('academy', '/marketing-classes', 'Academy'), ('ai', '/ai-classes', 'AI Classes'), ('portfolio', '/portfolio', 'Portfolio'),
           ('scan', '/scan-buddy', 'Scan Buddy'), ('aivideo', '/ai-video', 'AI Video')]
    subs = '\n        '.join(f'<a href="{h}"{" aria-current=\"page\"" if k == cur else ""}>{l}</a>' for k, h, l in sub)
    main = '\n        '.join(items)
    return f'''<a class="skip" href="#main">Skip to content</a>
  <header class="nav">
    <div class="nav-in">
      <a class="brand" href="/" aria-label="Top Creation Media, home"><img src="/assets/tcm-wordmark.webp" alt="TCM Top Creation Media" width="480" height="207"></a>
      <nav class="nav-links" aria-label="Main">
        {main}
        <a class="btn btn-primary btn-sm" href="{wa("Hi, I'd like a customized package!")}" onclick="{CONV}" target="_blank" rel="noopener"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg>WhatsApp Us</a>
      </nav>
    </div>
    <nav class="subnav" aria-label="Pages"><div class="subnav-in">
        {subs}
    </div></nav>
  </header>'''


FOOT = f'''<footer class="foot">
    <div style="display:flex;align-items:center;gap:10px">
      <img src="/assets/tcm-logo.jpg" alt="" width="26" height="26" style="width:26px;height:26px;border-radius:7px;object-fit:cover">
      <span>© <span id="year">2026</span> Top Creation Media Sdn Bhd · Strategy. Execution. Growth.</span>
    </div>
    <div class="foot-links">
      <a href="/social-media">Social Media</a>
      <a href="/marketing-services">Done-For-You</a>
      <a href="/marketing-classes">Marketing Academy</a>
      <a href="/ai-classes">AI Classes</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/scan-buddy">Scan Buddy</a>
      <a href="/ai-video">AI Video</a>
      <a href="https://facebook.com/topcreationmedia" target="_blank" rel="noopener">Facebook</a>
      <a href="https://instagram.com/topcreationmedia" target="_blank" rel="noopener">Instagram</a>
      <a href="https://tiktok.com/@topcreationmedia" target="_blank" rel="noopener">TikTok</a>
    </div>
  </footer>
  <a class="wa-float" href="{wa("Hi, I'd like to know more!")}" onclick="{CONV}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="{WA_PATH}"/></svg></a>'''


def page(slug, title, desc, cur, ld, body, scripts=()):
    canon = SITE + slug
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
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/site.css">
  <script>document.documentElement.className='js'</script>
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  {nav(cur)}

  <main id="main">
{body}
  </main>

  {FOOT}

  {tags}
</body>
</html>
'''


# ---------------------------------------------------------------- helpers
def video(key, label):
    return f'''<div class="video" data-video="{key}" aria-label="{esc(label)}" data-rv>
        <button class="video-btn video-soon" type="button" aria-label="{esc(label)}"><span class="play">{PLAY}</span><span class="video-cap">Video coming soon</span></button>
      </div>'''


def photo(file, alt):
    return f'''<figure class="photo" data-rv>
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


def hero(crumbs, h1, lede, buttons='', extra='', eyebrow=''):
    crumb = ' / '.join(f'<a href="{h}">{esc(t)}</a>' if h else esc(t) for t, h in crumbs)
    return f'''    <section class="page-hero">
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


def switch(cur):
    links = [('social', '/social-media', 'Overview'), ('services', '/marketing-services', 'Done-For-You'), ('academy', '/marketing-classes', 'Marketing Academy')]
    a = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if k == cur else ""}>{l}</a>' for k, h, l in links)
    return f'<div class="switch-wrap rise" style="animation-delay:.3s"><nav class="switch" aria-label="Social Media sections">{a}</nav></div>'


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
        <p class="lede">Follow the {subject} and do the practice tasks. If you still can&#8217;t do it yourself, we refund 100% of your class fee. That is our promise: we guide you until you are the next professional marketer.</p>
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


def tabs(label, panels):
    buttons = ''.join(
        f'<button role="tab" id="t-{pid}" aria-controls="{pid}" aria-selected="{"true" if i == 0 else "false"}">{esc(name)}</button>'
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


PROVIDER = {'@type': 'Organization', 'name': 'Top Creation Media', 'url': SITE}
STEPS3 = '''        <div class="cols">
          <div class="col" data-rv><div class="col-n">1</div><div class="col-t">Strategy &amp; discussion</div><p class="col-d">We study your market, define the offer and agree the goals before a single asset is made.</p></div>
          <div class="col" data-rv><div class="col-n">2</div><div class="col-t">Planning &amp; approval</div><p class="col-d">Content calendar, creative direction and media plan, mapped, budgeted and signed off with you.</p></div>
          <div class="col" data-rv><div class="col-n">3</div><div class="col-t">Execution &amp; growth</div><p class="col-d">Our studio produces, campaigns launch, and we optimise every week: scale what works, stop what doesn&#8217;t.</p></div>
        </div>'''

CLIENTS = [('3cat.jpeg', '3cat'), ('fnc.jpeg', 'FnC'), ('mobil.jpg', 'Mobil'), ('tcl.png', 'TCL'), ('nescafe.jpg', 'Nescafé'),
           ('nomi.png', 'NOMI'), ('tp-link.png', 'TP-Link'), ('polo-club.jpeg', 'Royal County of Berkshire Polo Club'),
           ('golden-tropics.jpeg', 'Golden Tropics'), ('joy-paradise.jpg', 'Joy Paradise'), ('lau-homecook.png', 'Lau Homecook'),
           ('sofei.png', 'SOFEI'), ('haroma.jpg', 'Haroma Signature')]
CLIENTS_HTML = '<div class="clients" data-rv>' + ''.join(
    f'<div class="client" role="img" aria-label="{esc(n)}" title="{esc(n)}" style="background-image:url(\'/assets/logos/{f}\')"></div>' for f, n in CLIENTS) + '</div>'


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
HOME_FAQ = [
    ('Why choose us over other digital marketing agencies in Malaysia and Singapore?', "With years of proven industry experience, we don't just run ads; we build full-funnel marketing ecosystems. From high-converting Facebook and Instagram strategies to Google SEO, we combine creative video production with hard data to deliver measurable results for clients across Malaysia, Singapore and beyond."),
    ('What is the difference between your marketing services and your marketing academy?', 'With our Done-For-You services, our team runs your marketing for you: strategy, content, ads, livestream and KOC/KOL. With the Marketing Academy, we teach you or your staff to do it yourselves, step by step, on your own accounts. Many clients start with one and add the other later.'),
    ('How much does digital marketing cost in Malaysia?', "It depends on your goals, the platforms you need, and how much content is involved. A business running Facebook and Instagram ads has very different needs from a brand that wants TikTok livestreams, SEO and video production together. That's why we build a customized package for every client. WhatsApp us with your goals and budget range, and we'll recommend the most cost-effective mix."),
    ('What is the minimum ad budget for Facebook, Instagram, or TikTok ads in Malaysia?', "You can start small, but your budget needs to be big enough for the platform's algorithm to learn. We usually recommend a test budget first, finding the winning creatives and audiences, then scaling what works. On a strategy call we'll suggest a realistic starting budget for your industry and goals."),
    ('Which is better for my business: Facebook ads, TikTok ads, or Google ads?', "It depends on how your customers buy. Google Ads captures people already searching for your product, which is great for high-intent leads. Facebook and Instagram ads are excellent for precise targeting and retargeting. TikTok is ideal for viral reach, younger audiences and live selling. Most brands get the best results from a mix, and we'll recommend the right split."),
    ('Do I need any experience or coding to join your AI or marketing classes?', 'No. The classes start from zero. If you can use WhatsApp and a browser, you can follow along. You practise on your own business with us guiding every step, and if you follow the classes and still can\'t do it yourself, we refund your class fee in full (terms apply).'),
    ('Do you provide TikTok Live streaming and TikTok Shop services in Malaysia?', 'Yes. We run the full TikTok flywheel, from trend-driven short videos to complete livestream operations in our in-house livestream studio. We handle live hosts, scripting, TikTok Shop catalog setup, affiliate creators and paid traffic to your live sessions, turning viewers into real sales.'),
    ('Can you help my brand market on Xiaohongshu (RED) to reach Chinese-speaking customers?', 'Yes. Xiaohongshu (Little Red Book) is one of the most powerful platforms for reaching Chinese-speaking consumers in Malaysia, Singapore and China. We create authentic, native-style notes, work with KOCs and KOLs, and plan search-led content so customers who look for recommendations discover your brand.'),
    ('Do you work with KOLs and influencers (KOC & KOL marketing)?', 'Yes. We match your brand with the right KOLs (key opinion leaders) and KOCs (key opinion consumers) based on audience fit, engagement quality and budget, not just follower count. We manage briefing, content approval and result tracking, so every collaboration drives real awareness and sales.'),
    ('Does your team handle video production and event marketing?', "Yes. Our in-house team handles video production, from short-form reels to brand films. We also run event marketing: capturing offline events and amplifying them online through targeted search and social campaigns, taking your brand from offline to online."),
    ('Do you offer Google SEO and SEM, including AI search?', 'Yes. We cover SEO (search engine optimization), SEM (Google Ads), AEO (answer engine optimization) and GEO (generative engine optimization), so your brand shows up both in Google results and in AI answers from ChatGPT, Gemini and Google AI.'),
    ('How long does it take to see results from SEO?', 'SEO is a long-term investment. Most websites start to see movement in Google rankings and organic traffic within 3 to 6 months, depending on competition and the current state of the site. Paid ads on Google, Meta and TikTok can bring traffic within days, which is why we often combine SEM for fast leads with SEO for sustainable growth.'),
    ('What are Scan Buddy and AI Video?', 'They are AI tools for TCM subscribers. Scan Buddy is a smart QR code that sends customers to all your social media, WhatsApp and Google reviews in one scan, and shows you every scan. AI Video turns a product photo into ready-to-post marketing videos. WhatsApp us for access.'),
    ('How do you track and report campaign results?', 'We measure what matters to your business: leads, sales, cost per result and return on ad spend (ROAS), not just likes and views. Using Meta Pixel, Google Analytics and platform dashboards, we track every channel and share clear reports, so you always know where your money goes and what it brings back.'),
    ('Can you help local brands expand into international markets?', 'Yes. We combine Google SEO, localized search ads and targeted Instagram, Facebook and TikTok campaigns to introduce your brand to new markets, with clients across Malaysia, Singapore, China, the USA and Indonesia.'),
]
home_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'ProfessionalService', 'name': 'Top Creation Media', 'url': SITE, 'logo': SITE + 'assets/tcm-logo.jpg',
     'image': SITE + 'assets/tcm-logo.jpg', 'telephone': '+' + PHONE, 'areaServed': ['MY', 'SG'],
     'description': 'Digital marketing agency and AI & marketing training studio in Malaysia.',
     'sameAs': ['https://facebook.com/topcreationmedia', 'https://instagram.com/topcreationmedia', 'https://tiktok.com/@topcreationmedia']},
    faq_ld(HOME_FAQ)]}

SERVICES = [
    ('Meta ads', 'Facebook and Instagram campaigns built around one goal: sales and leads, tracked to the ringgit.', None, 'megaphone'),
    ('TikTok', 'Short video at volume, livestream operations and TikTok Shop, run as one sales engine.', None, 'music'),
    ('Xiaohongshu', 'Search-led notes and KOC seeding that put your brand in front of Chinese-speaking buyers.', None, 'book'),
    ('Google SEO & SEM', 'Page-one rankings, Google Ads and AI search visibility in ChatGPT and Gemini answers.', None, 'search'),
    ('Video & livestream studio', 'In-house shooting, editing and live hosting, from product clips to brand films.', None, 'video'),
    ('KOC & KOL', 'Influencers matched on audience fit and engagement quality, not just follower count.', None, 'users'),
    ('Branding', 'Visual identity, positioning and guidelines so every post looks like you.', None, 'pen'),
    ('Events, offline to online', 'Launches and activations captured on the day and amplified online after it.', None, 'layers'),
]

home_body = f'''    <section class="hero">
      <div class="hero-grid">
        <div>
          <div class="eyebrow rise">Digital marketing × Content × AI</div>
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
        {cards(SERVICES, 'grid center')}
      </div>
    </section>

    <section class="tile tile-dark" style="padding-top:72px;padding-bottom:72px">
      <div class="why">
        <div class="why-head" data-rv><div class="eyebrow">Why TCM</div><h2 class="h2" style="font-size:clamp(30px,3.4vw,42px)">Why businesses choose <span class="accent">TCM</span></h2></div>
        <div class="why-list">
          <div data-rv>{icon('zap')}<p>Marketing made simple, in a few clicks</p></div>
          <div data-rv>{icon('coins')}<p>Save thousands on wasted ad spend</p></div>
          <div data-rv>{icon('target')}<p>Skip the trial and error: we have done it already</p></div>
          <div data-rv>{icon('users')}<p>One team, all platforms</p></div>
        </div>
      </div>
    </section>

    <section class="tile tile-raise" id="about">
      <div class="wrap">
        <div class="sec-head" style="margin-bottom:0">
          <div data-rv><div class="eyebrow">About us</div><h2 class="h2">One team, from <span class="accent">offline to online.</span></h2></div>
          <p class="lede" data-rv style="margin-top:22px">Top Creation Media is a digital marketing agency and training studio in Malaysia. We plan, shoot, launch and scale marketing for brands, and we teach business owners and teams to do the same with AI. Follow our way and you save on wasted ad spend and skip years of trial and error.</p>
        </div>
        <div class="stats">
          <div class="stat" data-rv><div class="stat-n">8+</div><div class="stat-l">Years of experience</div></div>
          <div class="stat" data-rv><div class="stat-n">3,000+</div><div class="stat-l">Videos produced</div></div>
          <div class="stat" data-rv><div class="stat-n">500+</div><div class="stat-l">Clients served</div></div>
          <div class="stat" data-rv><div class="stat-n">5</div><div class="stat-l">Markets: MY, SG, CN, US, ID</div></div>
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
        {photo('mission.jpg', 'Top Creation Media team guiding participants during a hands-on class')}
          <div class="mvp-text" data-letter="M" data-rv>
            <div class="split-k mvp-num"><b>01</b>Our mission</div>
            <h3 class="h2">We guide you until you can do it yourself.</h3>
            <p class="lede">We coach every participant to learn AI and marketing hands-on. You set up the account, make the video and launch the ad with your own hands, with us beside you.</p>
            {ticks(['Learn by doing, on your own business', 'Step-by-step guidance, starting from zero', 'Templates and prompts you keep for good'])}
          </div>
        </div>
        <div class="split flip">
        {photo('vision.jpg', 'Behind the scenes at a Top Creation Media shoot')}
          <div class="mvp-text" data-letter="V" data-rv>
            <div class="split-k mvp-num"><b>02</b>Our vision</div>
            <h3 class="h2">Every beginner can become a professional marketer.</h3>
            <p class="lede">Anyone who finds this website, with no experience and no coding, should be able to become a professional marketer. Every class and service we build is held to that standard.</p>
            {ticks(['No experience or coding needed', 'Skills for your own business, or to freelance', 'Learn the right way first and skip costly mistakes'])}
          </div>
        </div>
        <div class="split">
        {photo('performance.jpg', 'Top Creation Media livestream session in the studio')}
          <div class="mvp-text" data-letter="P" data-rv>
            <div class="split-k mvp-num"><b>03</b>Our performance</div>
            <h3 class="h2">Sales that sell out. Brands that last.</h3>
            <p class="lede">We measure ourselves in results: orders, leads and a brand people remember. Not likes for the sake of likes.</p>
            {ticks(['Sell-out campaigns and livestreams', 'Leads and sales you can count', 'A brand people trust and come back to'])}
          </div>
        </div>
      </div>
    </section>

    <section class="tile tile-raise" id="services">
      <div class="wrap">
        {head('Two ways to grow. <span class="accent">You choose.</span>', 'How we work with you', 'Same team, same platforms. The difference is who does the work.')}
        <div class="ways">
          <div class="way" data-rv>
            <div class="way-k">Done-For-You services</div>
            <div class="way-t">We run it for you.</div>
            <p class="way-d">Strategy, content, ads, livestream and KOC/KOL, handled by our team while you focus on your business.</p>
            {ticks(['Facebook & Instagram ads', 'TikTok video, Live & TikTok Shop', 'Google SEO & search ads', 'Xiaohongshu notes & creator seeding', 'KOC & KOL collaborations'])}
            <a class="btn btn-primary" href="/marketing-services">See Done-For-You</a>
          </div>
          <div class="way" data-rv>
            <div class="way-k">Marketing Academy</div>
            <div class="way-t">We teach you to do it.</div>
            <p class="way-d">Learn every setting, hands-on, from account setup to scaling. Save on agency fees and skip the costly trial and error.</p>
            {ticks(['Every platform, from A to Z', 'Practise on your own business', 'Templates and checklists you keep', "Can't learn it? 100% refund"])}
            <a class="btn btn-primary" href="/marketing-classes">See the Academy</a>
          </div>
        </div>
        <div style="margin-top:16px">
        {cards([
            ('AI Classes', 'AI video, graphics, captions, websites and automation. No coding needed.', [('Explore AI Classes', '/ai-classes')], 'sparkles'),
            ('Scan Buddy', 'One smart QR code that turns offline customers into followers, chats and reviews.', [('See Scan Buddy', '/scan-buddy')], 'qr'),
            ('AI Video', 'Upload a product photo. Get ready-to-post marketing videos.', [('See AI Video', '/ai-video')], 'video'),
        ], 'grid g3')}
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

{faq_section(HOME_FAQ, 'tile-raise')}

{cta('Stop guessing. Start growing.', 'One chat. One customized plan. One team for every channel, or a class that teaches you to run it yourself.', 'WhatsApp Us for a Free Consultation', "Hi, I'd like a free consultation!")}'''

# =================================================================== SOCIAL MEDIA HUB
SOCIAL_FAQ = [
    ('Should I choose Done-For-You or the Marketing Academy?', 'Choose Done-For-You if you want results without spending your own time on the tools. Choose the Academy if you want you or your staff to own the skill and save on agency fees long term. If you are unsure, WhatsApp us your goal and we will recommend one honestly.'),
    ('Can I do both?', 'Yes. Many clients start with Done-For-You to get results quickly, then train their staff in the Academy so they can take over day-to-day work.'),
    ('Which platform should I start with?', 'It depends on where your customers spend time and how they buy. Google suits people already searching, Facebook and Instagram suit precise targeting, TikTok suits reach and live selling, and Xiaohongshu suits Chinese-speaking buyers who search for recommendations.'),
]
social_ld = {'@context': 'https://schema.org', '@graph': [faq_ld(SOCIAL_FAQ)]}
PLATFORMS = [
    ('Facebook & Instagram', 'Ads, posters, carousels and Reels on Meta, with tracking that shows what each ringgit brings back.', [('We do it', '/marketing-services#facebook'), ('Learn it', '/marketing-classes#facebook')], 'megaphone'),
    ('TikTok', 'Short video, livestream selling, TikTok Shop and KOC content that feels native.', [('We do it', '/marketing-services#tiktok'), ('Learn it', '/marketing-classes#tiktok')], 'music'),
    ('Google', 'SEO, search ads and AI search, so you show up when customers look for you.', [('We do it', '/marketing-services#google'), ('Learn it', '/marketing-classes#google')], 'search'),
    ('Xiaohongshu', 'Search-led notes, creator (博主) seeding and Juguang ads for Chinese-speaking buyers.', [('We do it', '/marketing-services#xiaohongshu'), ('Learn it', '/marketing-classes#xiaohongshu')], 'book'),
]

social_body = f'''{hero([("Home", "/"), ("Social Media", "")], 'Social media marketing, <span class="accent">two ways.</span>',
       'Facebook, Instagram, TikTok, Google and Xiaohongshu. Let our team run it for you, or learn to run it yourself the right way, from day one.',
       extra=switch('social') + video('social', 'Social media marketing: two ways to work with us'), eyebrow='Social media marketing')}

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Pick the way that fits you', 'Two options')}
        <div class="ways">
          <div class="way" data-rv>
            <div class="way-k">Option 1 · Done-For-You</div>
            <div class="way-t">We handle everything.</div>
            <p class="way-d">Ads, content, livestream, account management and KOC/KOL, run by our team. You focus on your business and read a clear report.</p>
            {ticks(['Strategy and monthly plan', 'Video, posters and carousels made in-house', 'Ads set up, tested and scaled', 'Monthly results report'])}
            <a class="btn btn-primary" href="/marketing-services">Explore Done-For-You</a>
          </div>
          <div class="way" data-rv>
            <div class="way-k">Option 2 · Marketing Academy</div>
            <div class="way-t">Learn it yourself.</div>
            <p class="way-d">Master the skill step by step, save on costs, and never waste money on the wrong strategy again. You can even take on clients of your own.</p>
            {ticks(['Every platform, A to Z', 'Hands-on, on your own accounts', 'Checklists and templates you keep', "Can't learn it? 100% refund"])}
            <a class="btn btn-primary" href="/marketing-classes">Explore the Academy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap">
        {head('The difference, side by side', 'Compare')}
        <div class="compare-scroll" data-rv>
          <table class="compare">
            <thead><tr><th></th><th>Done-For-You</th><th>Marketing Academy</th></tr></thead>
            <tbody>
              <tr><th>Best for</th><td>Busy owners and brands who want results without learning the tools</td><td>Owners, staff and freelancers who want to do it themselves</td></tr>
              <tr><th>Your time</th><td>A short check-in each week</td><td>Class time plus hands-on practice</td></tr>
              <tr><th>What you get</th><td>Strategy, content, ads, livestream, KOC/KOL and monthly reports</td><td>Step-by-step classes, templates and guidance on your own accounts</td></tr>
              <tr><th>Who owns the skill</th><td>Our team runs it; you see everything</td><td>You do, for good</td></tr>
              <tr><th>Start with</th><td>A free strategy chat</td><td>A short chat about your goals</td></tr>
            </tbody>
          </table>
        </div>
        <p class="lede" data-rv style="text-align:center;margin-top:40px">Or both: many clients start with Done-For-You, then train their staff in the Academy.</p>
      </div>
    </section>

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Platforms we run and teach', 'Platforms')}
        {cards(PLATFORMS)}
      </div>
    </section>

{faq_section(SOCIAL_FAQ)}

{cta('Not sure which to choose?', 'Tell us your business and goal. We will recommend the right option honestly.', 'WhatsApp Us for Advice', "Hi, I'm not sure whether to choose Done-For-You or the Academy. Can you advise?")}'''

# =================================================================== DONE-FOR-YOU
XHS_NOTE = "<strong>Good to know:</strong> Xiaohongshu&#8217;s Juguang (聚光) ad platform generally requires a mainland China business entity, so overseas brands usually advertise through certified agency partners. We handle the access route for you, and put most of the effort where it pays off first: search-led notes and creator seeding."


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
    ('KOC & KOL collaborations', 'We scan and shortlist influencers by audience fit, engagement quality and real followers, then manage briefs, approvals and results.'),
    ('Livestream studio', 'An in-house studio with hosts and crew for TikTok, Facebook and Shopee lives.'),
    ('Account management', 'Posting, replies and community management across your channels.'),
    ('Branding', 'Logo, visual identity and guidelines so every channel looks consistent.'),
    ('Events, offline to online', 'Launches and activations organised, filmed and amplified online.'),
    ('AI-powered production', 'AI speeds up captions, variations and edits, so you get more creative for the same budget.'),
]
DFY_FAQ = [HOME_FAQ[2], HOME_FAQ[3], HOME_FAQ[4], HOME_FAQ[13]]
dfy_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Service', 'name': 'Done-For-You Social Media Marketing', 'serviceType': 'Digital marketing agency services',
     'provider': PROVIDER, 'areaServed': ['MY', 'SG'], 'url': SITE + 'marketing-services',
     'description': 'Facebook, Instagram, TikTok, Google and Xiaohongshu marketing run by Top Creation Media: strategy, content, ads, livestream and KOC/KOL.'},
    faq_ld(DFY_FAQ)]}

dfy_body = f'''{hero([("Home", "/"), ("Social Media", "/social-media"), ("Done-For-You", "")], 'Your marketing, <span class="accent">done for you.</span>',
       'Strategy, content, ads, livestream and KOC/KOL across Facebook, Instagram, TikTok, Google and Xiaohongshu, handled end to end by one team.',
       btns(('Get a free strategy chat', wa("Hi, I'd like the Done-For-You marketing service!")), ('Choose a platform', '#platforms')),
       switch('services') + video('services', 'Done-For-You marketing services video'), eyebrow='Done-For-You services')}

    <section class="tile tile-raise" id="platforms">
      <div class="wrap">
        {head('Choose a platform', 'Done-For-You', style='margin-bottom:40px')}
{tabs('Platforms', [
    ('facebook', 'Facebook & IG', svc_panel('Facebook &amp; Instagram, from scroll to sale', 'We run Facebook and Instagram as one engine: strategy first, creative built to convert, then ads tuned every week.', DFY_FB, RES_META, ics=['target', 'video', 'pen', 'layers', 'megaphone', 'zap'])),
    ('tiktok', 'TikTok', svc_panel('TikTok video, Live and Shop', 'From trend-driven short video to full livestream selling, we run the whole TikTok flywheel.', DFY_TT, RES_TT, ics=['music', 'live', 'coins', 'users', 'zap', 'target'])),
    ('google', 'Google', svc_panel('Own the search results, human and AI', 'When customers search on Google or ask an AI, your brand should be the answer.', DFY_GG, RES_GG, ics=['search', 'megaphone', 'sparkles', 'layers', 'target', 'zap'])),
    ('xiaohongshu', 'Xiaohongshu', svc_panel('Xiaohongshu (RED): notes, 博主 and ads', 'Reach Chinese-speaking buyers in Malaysia, Singapore and China with content that gets found and creators who build trust.', DFY_XHS, note=XHS_NOTE, ics=['book', 'search', 'users', 'megaphone', 'layers', 'target'])),
])}
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap">
        {head('Also in our toolkit', 'More services')}
        {cards(TOOLKIT, 'grid g3', ['users', 'live', 'calendar', 'pen', 'layers', 'sparkles'])}
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
    ('Is this for complete beginners?', 'Yes. Each platform starts from account setup and builds step by step to optimising and scaling. If you already run ads, you can jump straight to the module you need.'),
    ('What does the 100% refund guarantee cover?', 'If you attend every session, complete the practice tasks and still cannot do it yourself, we refund your class fee in full. WhatsApp us for the full terms before you join.'),
    ('Do I need an ad budget to join?', 'You can learn the setup and structure without spending, but real learning comes from a small live test. We will help you choose a sensible test budget for your industry and goal.'),
    ('Can I use these skills to freelance?', 'Yes. Many participants learn to run their own business marketing first, then take on clients. The templates and checklists you keep are the same ones we use.'),
    ('Can I send my staff or run it for my company?', 'Yes. We can run the classes for your team and use your own products and accounts as practice material. WhatsApp us your team size and goals.'),
    ('How much do the classes cost and when do they start?', 'Dates and fees depend on the platforms you choose and group size. WhatsApp us for the current schedule and a quote.'),
]
academy_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Course', 'name': 'Marketing Academy: Facebook, Instagram, TikTok, Google & Xiaohongshu',
     'description': 'Hands-on marketing classes in Malaysia, from account setup and tracking to creative, optimisation and scaling, for Facebook, Instagram, TikTok, Google and Xiaohongshu.',
     'provider': PROVIDER, 'url': SITE + 'marketing-classes'},
    faq_ld(ACADEMY_FAQ)]}

academy_body = f'''{hero([("Home", "/"), ("Social Media", "/social-media"), ("Marketing Academy", "")], 'Learn to run your own ads, <span class="accent">A to Z.</span>',
       'Facebook, Instagram, TikTok, Google and Xiaohongshu, taught hands-on on your own accounts. Save on agency fees and never waste money on the wrong strategy again.',
       btns(('Join the next class', wa("Hi, I'd like to join the Marketing Academy!")), ('Choose a platform', '#platforms')),
       switch('academy') + video('academy', 'Marketing Academy introduction video'), eyebrow='Marketing Academy')}

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Made for beginners. Used by pros', 'Who it is for')}
        <div class="cols">
          <div class="col" data-rv><div class="col-t">Business owners</div><p class="col-d">Stop paying for guesswork. Learn to run your own ads and content, and know exactly what you are paying for.</p></div>
          <div class="col" data-rv><div class="col-t">Staff &amp; marketing teams</div><p class="col-d">Give your team a proven system: the same structures, checklists and reports we use for clients.</p></div>
          <div class="col" data-rv><div class="col-t">Beginners &amp; freelancers</div><p class="col-d">Start from zero and build a skill you can earn from, for your own business or for clients.</p></div>
        </div>
      </div>
    </section>

    <section class="tile tile-dark" id="platforms">
      <div class="wrap">
        {head('One platform at a time', 'Curriculum', style='margin-bottom:40px')}
{tabs('Platforms', [
    ('facebook', 'Facebook & IG', panel_intro('Facebook &amp; Instagram, from account to scale', 'Nine steps from a blank account to campaigns you can optimise and grow. Facebook and Instagram share the same Meta Ads Manager.') + '\n' + modules(META, 'You will do')),
    ('tiktok', 'TikTok', panel_intro('TikTok content, ads and live selling', 'From Business Center to Smart+ and GMV Max, with videos that feel native and a plan for TikTok Live.') + '\n' + modules(TT, 'You will do')),
    ('google', 'Google', panel_intro('Google SEO, search ads and AI search', 'Get found when customers search, with ChatGPT doing the heavy lifting on research and writing.') + '\n' + modules(GOOGLE, 'You will do')),
    ('xiaohongshu', 'Xiaohongshu', panel_intro('Xiaohongshu (RED): notes, 博主 and ads', 'Reach Chinese-speaking customers with notes that get found, creators who build trust, and paid support.') + '\n' + modules(XHS, 'You will do') + f'\n        <p class="note" data-rv>{XHS_NOTE}</p>'),
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

{faq_section(ACADEMY_FAQ, 'tile-raise')}

{cta('Become the next professional marketer.', 'Tell us your business and goal. We will point you to the right platform to start.', 'WhatsApp Us About the Academy', "Hi, I'd like to know more about the Marketing Academy!")}'''

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
    ('Do I need any technical or coding experience?', 'No coding at all. If you can use WhatsApp and a browser, you can follow along. The website and automation modules use AI to do the technical parts, and we explain each step in plain language.'),
    ('Which AI tools do you teach?', 'ChatGPT, Claude and Gemini, plus the video, design, website and automation tools around them. We teach the method first because tools change every month, and refresh the tool list at each intake.'),
    ('Can I earn money with these skills?', 'Yes. Many businesses now pay for AI video, graphics, captions and automation. You can use the skills to cut costs in your own business, or offer them as a freelancer.'),
    ('What does the 100% refund guarantee cover?', 'If you attend every session, complete the practice tasks and still cannot do it yourself, we refund your class fee in full. WhatsApp us for the full terms before you join.'),
    ('Can you train my whole team or company?', 'Yes. We can run the classes for your team and tailor the examples to your industry, brand and data rules. Tell us your team size and goals on WhatsApp.'),
    ('How much do the classes cost and when is the next one?', 'Dates and fees depend on the modules you choose and your group size. WhatsApp us for the current schedule and a quote.'),
]
ai_ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'Course', 'name': 'AI Classes: AI Video, Graphics, Captions, Websites & Automation',
     'description': 'Hands-on AI classes in Malaysia, no coding needed: ChatGPT, Claude and Gemini, AI video, AI graphics, AI websites and SEO, AI captions, AI automation and AI marketing.',
     'provider': PROVIDER, 'url': SITE + 'ai-classes'},
    faq_ld(AI_FAQ)]}

ai_body = f'''{hero([("Home", "/"), ("AI Classes", "")], 'Let AI do the work. <span class="accent">You run the show.</span>',
       'AI already helps businesses work smarter and replace complex manual tasks. Learn to use it for video, graphics, captions, websites and automation. No coding, no tech background.',
       btns(('Join the next class', wa("Hi, I'd like to join the AI classes!")), ('See the 7 modules', '#curriculum')),
       video('ai', 'AI Classes introduction video'), eyebrow='AI Classes · No coding needed')}

    <section class="tile tile-raise">
      <div class="wrap">
        {head('Save costs, or earn from it', 'Who it is for')}
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
        <div class="clients" id="clients" data-rv></div>
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
    tag = '<div class="rise" style="margin-bottom:24px"><span class="tag">For TCM subscribers</span></div>'
    return f'''{hero([("Home", "/"), (h1.split(':')[0], "")], h1, lede,
       btns(('Get access on WhatsApp', wa(wa_msg)), ('How it works', '#how')), video(key, video_label)).replace('<div class="crumbs', tag + '<div class="crumbs', 1)}

    <section class="tile tile-raise" id="how">
      <div class="wrap">
        {head('How it works', 'How it works')}
        {steps(step_rows)}
      </div>
    </section>

{extra}
    <section class="tile tile-raise">
      <div class="wrap">
        {head(feat_h2, 'Features')}
        {cards(feats, 'grid g3', feat_icons)}
      </div>
    </section>

{faq_section(faq)}

{cta(cta_h2, cta_lede, 'Get Access on WhatsApp', wa_msg)}'''



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
    ('What is Scan Buddy?', 'Scan Buddy is a smart QR code for your business. Customers scan it once to follow your Facebook, Instagram, TikTok and Xiaohongshu, message you on WhatsApp or leave a Google review, and you see how many people scanned.'),
    ('Do my customers need an app?', 'No. Any phone camera can scan the QR code and open your page in the browser.'),
    ('Can I change my links after printing?', 'Yes. Update your links any time and the same printed QR code keeps working.'),
    ('How do I get Scan Buddy?', 'Scan Buddy is available to TCM subscribers. WhatsApp us for plans and access.'),
]
sb_body = tool_body(
    'scan-buddy', 'Scan Buddy: <span class="accent">one scan, every channel.</span>',
    'A smart QR code for your shop, packaging and events. Customers scan once to follow you on every platform, chat on WhatsApp or leave a Google review. You see every scan.',
    "Hi, I'd like to get Scan Buddy!", 'Scan Buddy demo video',
    [('Subscribe', 'Join as a TCM subscriber and unlock Scan Buddy.'), ('Add your links', 'Facebook, Instagram, TikTok, Xiaohongshu, WhatsApp and Google reviews.'),
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
    ('Do I need to film anything?', 'No. Start from a product photo. AI creates the scenes, motion, captions and music. You can also add your own footage if you have it.'),
    ('What kind of videos can I make?', 'Product showcases, new backgrounds and scenes, AI model and outfit try-ons, UGC-style clips and short ads with captions, in 9:16, 1:1 and 16:9.'),
    ('What photos work best?', 'Clear, well-lit product photos on a plain background give the best results. Our team can help review and polish videos when needed.'),
    ('How do I get AI Video?', 'AI Video is available to TCM subscribers. WhatsApp us for plans and access.'),
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

tool_ld = lambda faq: {'@context': 'https://schema.org', '@graph': [faq_ld(faq)]}

# =================================================================== WRITE
PAGES = [
    ('index.html', '', 'Digital Marketing Agency Malaysia | Top Creation Media',
     'Digital marketing agency in Malaysia: Facebook & Instagram ads, TikTok Live, Google SEO, Xiaohongshu & KOL marketing, plus AI and marketing classes.',
     'home', home_ld, home_body, ('/portfolio-data.js',)),
    ('social-media.html', 'social-media', 'Social Media Marketing Malaysia | Done-For-You or Learn It',
     'Social media marketing in Malaysia, two ways: let Top Creation Media run your Facebook, TikTok, Google and Xiaohongshu, or learn to do it yourself.',
     'social', social_ld, social_body, ()),
    ('marketing-services.html', 'marketing-services', 'Social Media Marketing Services Malaysia | TCM',
     'Done-for-you Facebook, Instagram, TikTok Live, Google SEO and Xiaohongshu marketing in Malaysia: strategy, video, ads, livestream and KOC/KOL.',
     'services', dfy_ld, dfy_body, ()),
    ('marketing-classes.html', 'marketing-classes', 'Marketing Classes Malaysia | Facebook, TikTok, Google & RED',
     'Learn Facebook, Instagram, TikTok, Google and Xiaohongshu marketing from A to Z, hands-on. Beginner-friendly classes in Malaysia with a 100% refund guarantee.',
     'academy', academy_ld, academy_body, ()),
    ('ai-classes.html', 'ai-classes', 'AI Classes Malaysia | AI Video, Graphics & Automation',
     'AI classes in Malaysia, no coding needed: ChatGPT, Claude, Gemini, AI video, AI graphics, AI captions, AI websites and automation. 100% refund guarantee.',
     'ai', ai_ld, ai_body, ()),
    ('portfolio.html', 'portfolio', 'Portfolio | Videos, Ad Results & Brand Work | TCM',
     'See Top Creation Media work: short-form videos, ad results dashboards and brand projects for clients across Malaysia and Singapore.',
     'portfolio', pf_ld, pf_body, ('/portfolio-data.js', '/portfolio.js')),
    ('scan-buddy.html', 'scan-buddy', 'Scan Buddy | Smart QR Code for Social Media | TCM',
     'Scan Buddy: one smart QR code that turns offline customers into followers, WhatsApp chats and Google reviews, with scan tracking. For TCM subscribers.',
     'scan', tool_ld(SB_FAQ), sb_body, ()),
    ('ai-video.html', 'ai-video', 'AI Video | Turn Product Photos into Video Ads | TCM',
     'AI Video turns a product photo into ready-to-post marketing videos: showcases, new backgrounds, model try-ons, UGC-style clips and captions.',
     'aivideo', tool_ld(AV_FAQ), av_body, ()),
]

if __name__ == '__main__':
    for fname, slug, title, desc, cur, ld, body, scripts in PAGES:
        with open(os.path.join(OUT, fname), 'w', encoding='utf8') as f:
            f.write(page(slug, title, desc, cur, ld, body, scripts))
        print(f'wrote {fname:24} title={len(title):3} desc={len(desc):3}')
    urls = ''.join(f'  <url><loc>{SITE}{slug}</loc></url>\n' for _, slug, *_ in PAGES)
    with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf8') as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print('wrote sitemap.xml')
