// Site checks with Playwright. Run from the repo root:
//   node tools/test_site.js
// It serves deploy/ locally (Vercel-style clean URLs) and checks every page at
// desktop and phone width: no JS errors, no sideways scroll, every internal link
// answers 200, nav dropdowns open, platform tabs switch and deep links work.
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium, devices } = require('playwright');

const root = path.join(__dirname, '..', 'deploy');
const PORT = 8790, BASE = 'http://127.0.0.1:' + PORT;
const EN = ['/', '/social-media', '/marketing-services', '/marketing-classes', '/ai-classes', '/portfolio', '/scan-buddy', '/ai-video', '/membership'];
const PAGES = EN.concat(EN.map(p => '/zh' + (p === '/' ? '/' : p)));
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.xml': 'application/xml', '.txt': 'text/plain' };

function serve() {
  return http.createServer((req, res) => {
    let u = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
    if (u.endsWith('.html')) { res.writeHead(308, { Location: u === '/index.html' ? '/' : u.slice(0, -5) }); return res.end(); }
    let f = u === '/' ? '/index.html' : u;
    if (f.endsWith('/')) f += 'index.html';
    if (!path.extname(f) && fs.existsSync(path.join(root, f + '.html'))) f += '.html';
    const fp = path.join(root, f);
    if (!fp.startsWith(root) || !fs.existsSync(fp) || fs.statSync(fp).isDirectory()) { res.writeHead(404); return res.end('404'); }
    res.writeHead(200, { 'Content-Type': types[path.extname(fp)] || 'application/octet-stream' });
    fs.createReadStream(fp).pipe(res);
  }).listen(PORT, '127.0.0.1');
}

const fails = [];
const check = (ok, msg) => { if (!ok) fails.push(msg); };

(async () => {
  const srv = serve();
  const browser = await chromium.launch();
  const links = new Set();

  for (const [label, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['phone', devices['iPhone 13']]]) {
    const ctx = await browser.newContext(opts);
    for (const p of PAGES) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('pageerror', e => errs.push(e.message));
      const res = await page.goto(BASE + p, { waitUntil: 'load' });
      check(res.status() === 200, `${p} [${label}] status ${res.status()}`);
      check(errs.length === 0, `${p} [${label}] JS errors: ${errs.join(' | ')}`);
      const over = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      check(over <= 0, `${p} [${label}] sideways scroll ${over}px`);
      check(await page.locator('h1').count() === 1, `${p} [${label}] needs exactly one h1`);
      const noAlt = await page.locator('img:not([alt])').count();
      check(noAlt === 0, `${p} [${label}] ${noAlt} images without alt`);
      (await page.$$eval('a[href^="/"]', as => as.map(a => a.getAttribute('href')))).forEach(h => links.add(h.split('#')[0] || '/'));
      await page.close();
    }
    await ctx.close();
  }

  // Internal links
  for (const h of links) {
    const code = await new Promise(r => http.get(BASE + h, x => { x.resume(); r(x.statusCode); }).on('error', () => r(0)));
    check(code === 200, `link ${h} answers ${code}`);
  }

  // Interactions (desktop)
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(BASE + '/');
  await page.locator('.dd').first().hover();
  check(await page.locator('.dd-menu').first().isVisible(), 'nav dropdown does not open on hover');

  await page.goto(BASE + '/marketing-classes');
  const tabs = page.getByRole('tab');
  const n = await tabs.count();
  check(n >= 4, `academy has ${n} platform tabs, expected 4`);
  await tabs.nth(1).click();
  check(await tabs.nth(1).getAttribute('aria-selected') === 'true', 'clicking a tab does not select it');
  check(await page.locator('[role=tabpanel]:visible').count() === 1, 'more than one tab panel visible');

  await page.goto(BASE + '/marketing-services#tiktok');
  const sel = await page.locator('[role=tab][aria-selected=true]').getAttribute('aria-controls');
  check(sel === 'tiktok', `deep link #tiktok opened "${sel}"`);

  await page.goto(BASE + '/zh/');
  check(await page.getAttribute('html', 'lang') === 'zh-Hans', 'Chinese home is not lang=zh-Hans');
  check((await page.locator('h1').innerText()).includes('变简单'), 'Chinese home h1 is not translated');
  await page.locator('a.lang').click();
  check(new URL(page.url()).pathname === '/', 'language switch on /zh/ does not lead to /');

  await page.goto(BASE + '/');
  const wa = await page.locator('a[href*="wa.me/60127816121"]').count();
  check(wa > 0, 'no WhatsApp link on the home page');

  await browser.close();
  srv.close();
  if (fails.length) { console.log('FAIL\n- ' + fails.join('\n- ')); process.exit(1); }
  console.log(`PASS: ${PAGES.length} pages x 2 widths, ${links.size} internal links, nav, tabs, deep link, WhatsApp`);
})();
