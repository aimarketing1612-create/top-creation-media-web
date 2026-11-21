"""Lists every translatable string in deploy/*.html (English pages) -> tools/i18n/strings.txt"""
import glob, os, re, json
from html.parser import HTMLParser
from urllib.parse import unquote
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = {'script', 'style'}
ATTRS = {'alt', 'aria-label', 'title', 'data-alt'}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack = [], []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        a = dict(attrs)
        for k, v in attrs:
            if k in ATTRS and v and v.strip():
                self.out.append(v.strip())
            if k == 'href' and v and 'wa.me' in v and 'text=' in v:
                self.out.append(unquote(v.split('text=', 1)[1]))
        if tag == 'meta' and a.get('content') and (a.get('name') == 'description' or a.get('property') in ('og:title', 'og:description')):
            self.out.append(a['content'].strip())
        if tag in ('img', 'meta', 'link', 'br', 'input', 'source'):
            self.stack.pop()

    def handle_endtag(self, tag):
        while self.stack and self.stack.pop() != tag:
            pass

    def handle_data(self, d):
        if self.stack and self.stack[-1] in SKIP:
            if self.stack[-1] == 'script' and '"@context"' in d:
                def walk(o):
                    if isinstance(o, dict):
                        for k, v in o.items():
                            if k in ('name', 'text', 'description') and isinstance(v, str):
                                self.out.append(v.strip())
                            else:
                                walk(v)
                    elif isinstance(o, list):
                        for v in o:
                            walk(v)
                walk(json.loads(d))
            return
        t = ' '.join(d.split())
        if t and re.search(r'[A-Za-z]', t):
            self.out.append(t)


def strings():
    seen = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'deploy', '*.html'))):
        p = P()
        p.feed(open(f, encoding='utf8').read())
        for s in p.out:
            if s not in seen and re.search(r'[A-Za-z]', s):
                seen.append(s)
    return seen


if __name__ == '__main__':
    s = strings()
    open(os.path.join(ROOT, 'tools', 'i18n', 'strings.txt'), 'w', encoding='utf8').write('\n'.join(s))
    print(len(s), 'strings,', sum(len(x) for x in s), 'chars')
