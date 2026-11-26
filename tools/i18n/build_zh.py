"""Builds the Chinese site (deploy/zh/*.html) from the English pages and tools/i18n/zh.json.

Every visible text, alt/aria-label/title, meta description, JSON-LD FAQ text and
WhatsApp message is looked up in zh.json (English -> 中文). Internal links get
the /zh prefix, so the Chinese visitor stays in Chinese. A string missing from
zh.json stays in English and is listed when the build runs: add it to zh.json.
Run through tools/build_site.py, which calls build_all() after the English pages.
"""
import glob
import html
import json
import os
import re
from html.parser import HTMLParser
from urllib.parse import quote, unquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, 'deploy')
ZH = json.load(open(os.path.join(HERE, 'zh.json'), encoding='utf8'))
TEXT_ATTRS = {'alt', 'aria-label', 'title', 'data-alt'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
PAGES = {'', 'ai-tools', 'marketing-services', 'marketing-classes', 'ai-classes', 'portfolio', 'scan-buddy', 'ai-video', 'membership'}
missing = set()
# Drop the licensed 字由点字玄真宋 web font here to use it on every Chinese page:
FONT_FILE = 'tcm-xuanzhen-song.woff2'


def tr(s):
    key = ' '.join(s.split())
    if not key or not any(c.isalpha() and c.isascii() for c in key):
        return s
    if key in ZH:
        z = ZH[key]
        # Chinese needs no space beside CJK text or punctuation; a space there shows as a gap.
        lead = '' if not z[:1].isascii() else s[:len(s) - len(s.lstrip())]
        trail = '' if not z[-1:].isascii() else s[len(s.rstrip()):]
        return lead + z + trail
    missing.add(key)
    return s


def zh_href(v):
    """/x -> /zh/x for page links; assets, scripts and external links stay."""
    if not v.startswith('/') or v.startswith('//') or v.startswith('/zh/') or v == '/zh':
        return v
    path, _, frag = v.partition('#')
    slug = path.strip('/')
    if slug not in PAGES:
        return v
    return '/zh/' + slug + ('#' + frag if frag else '') if slug else '/zh/' + ('#' + frag if frag else '')


def zh_wa(v):
    if 'wa.me' in v and 'text=' in v:
        head, msg = v.split('text=', 1)
        return head + 'text=' + quote(tr(unquote(msg)))
    return v


def ld(o):
    if isinstance(o, dict):
        return {k: (tr(v) if k in ('name', 'text', 'description') and isinstance(v, str)
                    else zh_href_abs(v) if k in ('url', 'item') and isinstance(v, str) else ld(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [ld(v) for v in o]
    return o


def zh_href_abs(v):
    site = 'https://www.topcreationmedia.com/'
    if v.startswith(site):
        slug = v[len(site):].split('#')[0].strip('/')
        if slug in PAGES:
            return site + 'zh/' + slug
    return v


class Tr(HTMLParser):
    def __init__(self, en_path):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.en_path = [], [], en_path
        self.in_switch = False

    def handle_decl(self, d):
        self.out.append(f'<!{d}>')

    def handle_comment(self, d):
        self.out.append(f'<!--{d}-->')

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        new = []
        meta_text = tag == 'meta' and (a.get('name') == 'description' or a.get('property') in ('og:title', 'og:description'))
        switch = 'data-lang-switch' in a
        for k, v in attrs:
            if v is None:
                new.append(k)
                continue
            if tag == 'html' and k == 'lang':
                v = 'zh-Hans'
            elif k in TEXT_ATTRS or k.startswith('data-l-'):   # data-l-*: text labels used by page scripts
                v = tr(v)
            elif k == 'content' and meta_text:
                v = tr(v)
            elif k == 'content' and a.get('property') == 'og:url':
                v = zh_href_abs(v)
            elif k == 'href' and switch:
                v = self.en_path
            elif k == 'hreflang' and switch:
                v = 'en'
            elif k == 'lang' and switch:
                v = 'en'
            elif k == 'href' and tag == 'link' and a.get('rel') == 'canonical':
                v = zh_href_abs(v)
            elif k == 'href' and tag == 'link' and 'fonts.googleapis.com/css2' in v:
                v = v.replace('&display=swap', '&family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;700&display=swap')
            elif k == 'href' and tag == 'link':
                pass
            elif k == 'href':
                v = zh_wa(zh_href(v))
            new.append(f'{k}="{html.escape(v, quote=True)}"')
        self.out.append(f'<{tag}' + ''.join(' ' + x for x in new) + '>')
        if switch:
            self.in_switch = True
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        # Self-closing tags (SVG <path/>, <circle/>, <rect/>) must stay self-closing, or later shapes
        # become children of the first one and are not drawn.
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.out[-1] = self.out[-1][:-1] + '/>'
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()

    def handle_endtag(self, tag):
        if tag == 'head' and os.path.exists(os.path.join(OUT, 'assets', 'fonts', FONT_FILE)):
            # Licensed Chinese display font, used first when its web font file is present.
            self.out.append(f'<link rel="preload" href="/assets/fonts/{FONT_FILE}" as="font" type="font/woff2" crossorigin>'
                            f'<style>@font-face{{font-family:"TCM XuanZhen Song";src:url(/assets/fonts/{FONT_FILE}) format("woff2");font-display:swap}}</style>')
        if tag == 'a':
            self.in_switch = False
        while self.stack:
            if self.stack.pop() == tag:
                break
        self.out.append(f'</{tag}>')

    def handle_data(self, d):
        top = self.stack[-1] if self.stack else ''
        if top == 'script':
            if '"@context"' in d:
                d = json.dumps(ld(json.loads(d)), ensure_ascii=False)
            self.out.append(d)
        elif top == 'style':
            self.out.append(d)
        elif self.in_switch:
            self.out.append(d.replace('中文', 'EN'))
        else:
            t = tr(d)
            # Chinese headings read cleaner without a closing 。 (it also pushes centred lines off-centre)
            if any(x in ('h1', 'h2', 'h3') for x in self.stack) and t.rstrip().endswith('。'):
                t = t.rstrip()[:-1]
            self.out.append(phrase_wrap(t, self.stack))


CJK_PUNCT = '，。、：；？！'


def phrase_wrap(t, stack):
    """Lets a Chinese line break only after punctuation: each short clause is kept whole (nowrap)."""
    esc = html.escape(t, quote=False)
    if not any('\u4e00' <= c <= '\u9fff' for c in t):
        return esc
    if any(x in ('h1', 'h2', 'h3') for x in stack):
        limit = 9
    elif any(x in ('p', 'li', 'td', 'figcaption') for x in stack):
        limit = 15
    else:
        return esc
    parts, cur = [], ''
    closers = '”’」』）)'
    for i, c in enumerate(t):
        cur += c
        nxt = t[i + 1] if i + 1 < len(t) else ''
        # Cut after punctuation, but keep a closing quote or bracket with it (it may not start a line).
        if (c in CJK_PUNCT or (c in closers and cur[:-1][-1:] in CJK_PUNCT)) and nxt not in closers:
            parts.append(cur); cur = ''
    if cur:
        parts.append(cur)
    def width(x):  # a Latin letter is about half a Chinese character wide
        return sum(1 if ord(c) > 0x2e80 else .55 for c in x.strip())
    # Browsers treat curly quotes as "never break here"; <wbr> after a closing quote restores a break point.
    def wrap(x):
        # Spaces stay outside the nowrap span, so the line can still break there.
        core = x.strip()
        lead, trail = x[:len(x) - len(x.lstrip())], x[len(x.rstrip()):]
        inner = f'<span class="nb">{html.escape(core, quote=False)}</span>' if 1.5 <= width(core) <= limit else html.escape(core, quote=False)
        return lead + inner + trail + ('<wbr>' if core[-1:] in '”’' else '')
    return ''.join(wrap(x) for x in parts)


def build_all():
    os.makedirs(os.path.join(OUT, 'zh'), exist_ok=True)
    missing.clear()
    files = sorted(glob.glob(os.path.join(OUT, '*.html')) + glob.glob(os.path.join(OUT, 'insights', '*.html')))
    for f in files:
        name = os.path.relpath(f, OUT)
        if name in ('404.html', 'thank-you.html'):   # one bilingual 404 page, served by Vercel for any unknown path
            continue
        slug = '' if name == 'index.html' else name[:-5]
        p = Tr('/' + slug)
        p.feed(open(f, encoding='utf8').read())
        p.close()
        os.makedirs(os.path.dirname(os.path.join(OUT, 'zh', name)), exist_ok=True)
        with open(os.path.join(OUT, 'zh', name), 'w', encoding='utf8') as w:
            # A comma before the coloured phrase is hidden when that phrase drops to its own line (phones).
            out = ''.join(p.out).replace('，<span class="accent">', '<span class="zh-p">，</span><span class="accent">')
            out = out.replace('，</span><span class="accent">', '</span><span class="zh-p">，</span><span class="accent">')
            # Keep the last four Chinese characters of a paragraph together, so no line ends with one or two orphans.
            out = re.sub(r'([\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]{4})</p>', r'<span class="nb">\1</span></p>', out)
            w.write(out)
    if missing:
        print(f'zh: {len(missing)} strings not in tools/i18n/zh.json (kept in English):')
        for m in sorted(missing):
            print('   ', m[:110])
    else:
        print('zh: all strings translated')


if __name__ == '__main__':
    build_all()
