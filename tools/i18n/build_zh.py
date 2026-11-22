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
from html.parser import HTMLParser
from urllib.parse import quote, unquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, 'deploy')
ZH = json.load(open(os.path.join(HERE, 'zh.json'), encoding='utf8'))
TEXT_ATTRS = {'alt', 'aria-label', 'title', 'data-alt'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
PAGES = {'', 'social-media', 'marketing-services', 'marketing-classes', 'ai-classes', 'portfolio', 'scan-buddy', 'ai-video', 'membership'}
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
                    else zh_href_abs(v) if k == 'url' and isinstance(v, str) else ld(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [ld(v) for v in o]
    return o


def zh_href_abs(v):
    site = 'https://topcreation.media/'
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
            elif k in TEXT_ATTRS:
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
        self.handle_starttag(tag, attrs)

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
            self.out.append(html.escape(tr(d), quote=False))


def build_all():
    os.makedirs(os.path.join(OUT, 'zh'), exist_ok=True)
    missing.clear()
    for f in sorted(glob.glob(os.path.join(OUT, '*.html'))):
        name = os.path.basename(f)
        slug = '' if name == 'index.html' else name[:-5]
        p = Tr('/' + slug)
        p.feed(open(f, encoding='utf8').read())
        p.close()
        with open(os.path.join(OUT, 'zh', name), 'w', encoding='utf8') as w:
            # A comma before the coloured phrase is hidden when that phrase drops to its own line (phones).
            w.write(''.join(p.out).replace('，<span class="accent">', '<span class="zh-p">，</span><span class="accent">'))
    if missing:
        print(f'zh: {len(missing)} strings not in tools/i18n/zh.json (kept in English):')
        for m in sorted(missing):
            print('   ', m[:110])
    else:
        print('zh: all strings translated')


if __name__ == '__main__':
    build_all()
