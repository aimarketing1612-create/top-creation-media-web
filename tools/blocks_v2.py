# ---------------------------------------------------------------- v2 blocks
# Pricing, the refund promise, the compact Marketing Academy curriculum, sample work for
# every AI module, and Scan Buddy plans. Text is written as Z(english, chinese): the pair
# goes into the Chinese build's dictionary, so no entry is needed in zh.json.
# This file is exec'd inside build_site.py (it uses its helpers: esc, head, ticks, tabs, wa…).
from insights import T as Z

MEM = dict(m=350, y=250, ytotal='3,000', full='4,200', save='1,200')
SB = dict(m=150, y=999, full='1,800', save=801, pct=44)
KONGSIKAN = 'https://kongsikan.cfd/'
# Stripe Payment Links. While a value is empty, that plan's button opens WhatsApp instead.
# In Stripe, set each link's "after payment" redirect to https://www.topcreationmedia.com/thank-you
PAY = {'mem_m': '', 'mem_y': '', 'sb_m': '', 'sb_y': ''}
MEM_M = f"Hi, I'd like to subscribe to the TCM Membership, monthly plan (RM{MEM['m']}/month)."
MEM_Y = f"Hi, I'd like to subscribe to the TCM Membership, yearly plan (RM{MEM['ytotal']}/year)."
SB_M = f"Hi, I'd like to try Scan Buddy, monthly plan (RM{SB['m']}/month)."
SB_Y = f"Hi, I'd like to subscribe to Scan Buddy, yearly plan (RM{SB['y']}/year)."
for _en, _zh in [(MEM_M, f"你好，我想订阅 TCM 会员月付配套（每月 RM{MEM['m']}）。"), (MEM_Y, f"你好，我想订阅 TCM 会员年付配套（每年 RM{MEM['ytotal']}）。"),
                 (SB_M, f"你好，我想试用 Scan Buddy 月付配套（每月 RM{SB['m']}）。"), (SB_Y, f"你好，我想订阅 Scan Buddy 年付配套（每年 RM{SB['y']}）。")]:
    Z(_en, _zh)


def guarantee(subject=''):
    steps = [Z('Join every session', '每堂课都参与'), Z('Do the practice tasks', '完成练习任务'), Z('Still cannot do it? 100% refund', '还是学不会？100% 退款')]
    li = ''.join(f'<li><b>{i}</b><span>{esc(t)}</span></li>' for i, t in enumerate(steps, 1))
    return f'''    <section class="tile tile-dark" id="guarantee">
      <div class="promise" data-rv>
        <div class="promise-seal" aria-hidden="true"><b>100%</b><span>{esc(Z('Money back', '全额退款'))}</span></div>
        <div class="promise-body">
          <div class="eyebrow">{esc(Z('Our promise', '我们的承诺'))}</div>
          <h2 class="h2">{esc(Z('Cannot learn it?', '学不会？'))} <span class="accent">{esc(Z('100% refund.', '100% 退款。'))}</span></h2>
          <p class="lede">{esc(Z('We are confident in how we teach. Follow the classes and do the practice tasks. If you still cannot do it yourself, we refund your full fee.', '我们对自己的教学有信心。跟着上课、完成练习任务，如果你还是没办法自己做出来，我们全额退还学费。'))}</p>
          <ol class="promise-steps">{li}</ol>
          <p class="promise-terms">{esc(Z('Terms and conditions apply. WhatsApp us for the full T&C.', '须符合条款与条件。完整条款请 WhatsApp 我们。'))}</p>
        </div>
      </div>
    </section>'''


# ------------------------------------------------ Marketing Academy: lighter curriculum
def modules_compact(rows):
    """Step cards: number, title and what you will do. The longer explanation opens on tap."""
    more = esc(Z('What you learn', '学什么'))
    out = []
    for i, (t, d, build, tools) in enumerate(rows, 1):
        out.append(f'''<div class="stepc" data-rv><div class="stepc-n">{i:02d}</div><h3 class="stepc-t">{esc(t)}</h3>
            <p class="stepc-b">{esc(build)}</p><details><summary>{more}</summary><p>{esc(d)}</p></details></div>''')
    return '        <div class="stepcs">' + '\n          '.join(out) + '</div>'


def classroom_strip():
    shots = [('/assets/bts/mission.jpg', Z('Trainer teaching a marketing class to a full room', '导师在满座的教室里讲解营销课程'), Z('Taught live, in a real class', '真人现场授课'), Z('Ask anything, get an answer on the spot.', '有问题当场问，当场得到答案。')),
             ('/assets/img/training.webp', Z('Students practising on their own laptops in a workshop', '学员在工作坊里用自己的电脑练习'), Z('Your own account, your own ads', '用你自己的账号和广告'), Z('You set it up yourself, with a coach beside you.', '你亲手设置，教练就在旁边。')),
             ('/assets/img/mem-live.webp', Z('Instructor running a live online class with students on screen', '导师正在进行线上直播课，屏幕上是学员'), Z('Support after class', '课后继续支援'), Z('Monthly live sessions keep you up to date.', '每月直播课，让你一直跟上最新做法。'))]
    figs = ''.join(f'<figure class="cshot" data-rv><img src="{src}" alt="{esc(alt)}" loading="lazy"><figcaption><b>{esc(t)}</b><span>{esc(d)}</span></figcaption></figure>' for src, alt, t, d in shots)
    return f'''    <section class="tile tile-raise">
      <div class="wrap">
        {head(esc(Z('Learn by doing,', '边做边学，')) + ' <span class="accent">' + esc(Z('not by watching.', '不是光看。')) + '</span>', esc(Z('Inside the class', '课堂实况')))}
        <div class="cshots">{figs}</div>
      </div>
    </section>'''


# ------------------------------------------------ AI Academy: three samples for every module
CHAT_SAMPLES = [
    ('ChatGPT', Z('Ad captions in seconds', '几秒写好广告文案'),
     Z('Write 3 Facebook ad captions for a durian mochi shop in Penang. Friendly, under 20 words each, end with a call to action.', '为槟城一家榴莲麻糬店写 3 则 Facebook 广告文案。语气亲切，每则不超过 30 个字，结尾要有行动呼吁。'),
     [Z('1. Soft outside, Musang King inside. Fresh daily in Penang. Order before we sell out!', '1. 外皮软糯，里面是猫山王。槟城每日现做，卖完就没有，快下单！'),
      Z('2. One bite and you will understand the queue. Durian mochi, made this morning. WhatsApp to order.', '2. 咬一口就知道为什么要排队。今早现做的榴莲麻糬，WhatsApp 下单。'),
      Z('3. Durian lovers, this one is for you. Box of 6, free delivery this week. Tap to order.', '3. 榴莲控看过来。一盒 6 粒，本周免运费，点击下单。')]),
    ('Claude', Z('A long document, summarised', '长文件，一页看完'),
     Z('Here is our 28-page supplier contract. Summarise the 5 points I must know before signing, and list anything unusual.', '这是我们 28 页的供应商合约。请整理签约前我必须知道的 5 个重点，并列出不寻常的条款。'),
     [Z('1. Payment: 50% upfront, balance within 14 days of delivery.', '1. 付款：先付 50%，余款在交货后 14 天内付清。'),
      Z('2. Minimum order: 500 units a month for 12 months.', '2. 最低订购量：每月 500 件，为期 12 个月。'),
      Z('Unusual: clause 9.2 lets the supplier raise prices with 7 days notice. Ask to change this to 60 days.', '不寻常：第 9.2 条允许供应商提前 7 天通知就涨价，建议要求改为 60 天。')]),
    ('Gemini', Z('Enquiries sorted into a sheet', '把询问整理成表格'),
     Z('Read last month\'s enquiry emails in Gmail and build a Google Sheet: name, what they asked, budget, and whether we replied.', '读取上个月 Gmail 里的询问邮件，整理成 Google 表格：姓名、询问内容、预算、是否已回复。'),
     [Z('Done. 46 enquiries added to "Enquiries, October".', '完成。已把 46 个询问加入「十月询问」表格。'),
      Z('31 asked about pricing, 9 about delivery, 6 about bulk orders.', '31 个问价格，9 个问配送，6 个问批发。'),
      Z('8 have not been replied to. I marked them in red.', '有 8 个还没回复，我已经用红色标出来。')]),
]
CAPTION_SAMPLES = [
    (Z('Skincare serum', '护肤精华'),
     Z('Sold out 3 times. Back for 2 days only.', '断货 3 次。这次只回来 2 天。'),
     Z('The vitamin C serum everyone is fighting for is finally back in stock. Brighter skin in 7 days, light, never sticky. Last time it was gone in 48 hours.', '全网都在抢的维 C 精华终于补货了。7 天提亮，质地轻盈不黏腻。上一次 48 小时就卖光。'),
     Z('Tap "Shop now" before it sells out again. 20% off ends Sunday.', '趁还没再断货，点击"立即购买"。20% 折扣星期天截止。'),
     '#skincaremalaysia #vitaminc #backinstock #viralskincare'),
    (Z('Bubble tea shop', '奶茶店'),
     Z('Buy 1 Free 1. Only 2 days left.', '买一送一，只剩最后 2 天。'),
     Z('Every brown sugar boba, all day, until Sunday night. After that it goes back to full price, and you will wish you had come.', '黑糖珍珠奶茶全线、全天买一送一，到星期天晚上为止。之后恢复原价，到时候你会后悔没来。'),
     Z('Tag the friend who owes you a drink and come today.', '标记那个还欠你一杯的朋友，今天就来。'),
     '#bobamalaysia #buy1free1 #last2days #奶茶控'),
    (Z('Gym membership', '健身房会员'),
     Z('Why did 300 people join this gym in one week?', '为什么一个星期内有 300 人加入这家健身房？'),
     Z('First month RM1. No joining fee. A coach plans your first 4 weeks for you. Only 37 spots are left at this price.', '首月只要 RM1，免入会费，教练帮你规划头 4 个星期。这个价格只剩 37 个名额。'),
     Z('WhatsApp "RM1" now to lock your spot before midnight.', '现在就 WhatsApp "RM1"，午夜前锁定你的名额。'),
     '#gymmalaysia #rm1 #limitedspots #健身'),
]
FLOW_SAMPLES = [
    (Z('WhatsApp auto-reply', 'WhatsApp 自动回复'), [Z('Customer sends a message', '顾客发来信息'), Z('AI reads the question', 'AI 读懂问题'), Z('Replies with price and stock', '回复价格和库存'), Z('Hot lead? Alerts your sales team', '高意向顾客？通知销售团队')]),
    (Z('Lead follow-up', '潜在顾客跟进'), [Z('New lead from a Meta ad', 'Meta 广告带来新顾客'), Z('Saved to Google Sheets', '存进 Google 表格'), Z('Day 1: thank-you message', '第 1 天：感谢信息'), Z('Day 3: reminder with an offer', '第 3 天：附优惠的提醒')]),
    (Z('Post once, publish everywhere', '发一次，全平台发布'), [Z('Upload one video', '上传一支视频'), Z('AI writes each caption', 'AI 为各平台写文案'), Z('Posts to Facebook, Instagram and TikTok', '发布到 Facebook、Instagram 和 TikTok'), Z('Weekly results in one report', '每周成效汇成一份报告')]),
]
PLAN_SAMPLES = [
    (Z('Customer persona', '顾客画像'), [(Z('Who', '对象'), Z('Working mums, 28 to 40, Klang Valley', '28 至 40 岁的职场妈妈，巴生谷')), (Z('Problem', '痛点'), Z('No time to cook healthy dinners', '没时间煮健康的晚餐')), (Z('Where', '在哪里'), Z('Instagram Reels, Facebook groups', 'Instagram Reels、Facebook 群组')), (Z('Message', '信息'), Z('Dinner ready in 15 minutes', '15 分钟晚餐上桌'))]),
    (Z('7-day content calendar', '7 天内容日历'), [(Z('Mon', '周一'), Z('Behind the scenes video', '幕后花絮视频')), (Z('Wed', '周三'), Z('Customer story', '顾客故事')), (Z('Fri', '周五'), Z('Weekend promo post', '周末促销贴文')), (Z('Sun', '周日'), Z('Tips carousel', '实用贴士图集'))]),
    (Z('Ad campaign plan', '广告活动规划'), [(Z('Goal', '目标'), Z('100 WhatsApp leads a month', '每月 100 个 WhatsApp 询问')), (Z('Budget', '预算'), Z('RM50 a day on Meta', 'Meta 每天 RM50')), (Z('Test', '测试'), Z('3 videos x 2 audiences', '3 支视频 × 2 组受众')), (Z('Track', '追踪'), Z('CPL, CTR and ROAS weekly', '每周看 CPL、CTR 和 ROAS'))]),
]
POSTERS = [('poster-skin', Z('Luxury skincare launch', '高端护肤品上市海报'), Z('AI-made poster: a gold serum bottle with the headline Sold out 3 times', 'AI 制作的海报：金色精华瓶，标题为"断货 3 次"')),
           ('poster-boba', Z('Food & drink promotion', '餐饮促销海报'), Z('AI-made poster: bubble tea splash with Buy 1 Free 1, only 2 days left', 'AI 制作的海报：奶茶飞溅画面，买一送一只剩 2 天')),
           ('poster-gym', Z('Fitness campaign', '健身品牌海报'), Z('AI-made poster: athlete with chalk dust and the headline No more Mondays', 'AI 制作的海报：运动员与飞扬的镁粉，标题为 No more Mondays'))]
SITES = [('site-dining', Z('Fine-dining restaurant', '高级餐厅'), Z('Sample home page for a tasting-menu restaurant, dark with serif type', '品尝菜单餐厅的首页样本，深色配衬线字体')),
         ('site-villa', Z('Luxury property launch', '高端房产项目'), Z('Sample home page for a rainforest villa development', '雨林别墅项目的首页样本')),
         ('site-derma', Z('Aesthetic clinic', '医美诊所'), Z('Sample home page for a doctor-led aesthetic clinic', '医美诊所的首页样本'))]
AV_ROWS = [('ai-video-1', 'UGC ads', 'Creator-style clips that feel native on TikTok and Reels.'),
           ('ai-video-2', 'AI short films', 'Story-led drama that holds attention to the end.'),
           ('ai-video-4', 'Outfit & background swap', 'Change the person, the outfit and the location, without a reshoot.'),
           ('ai-video-5', 'Product footage', 'Clean product shots from every angle, no studio needed.'),
           ('ai-video-6', 'Cinematic B-roll', 'Atmosphere shots of your shop and service, with sound.')]


def av_figs():
    return ''.join(f'''<figure class="sample" data-rv>{video9(k, t + " sample").replace(' data-rv', '')}<figcaption><b>{esc(t)}</b><span>{esc(d)}</span></figcaption></figure>''' for k, t, d in AV_ROWS)


def av_samples():
    return f'''    <section class="tile tile-dark" id="ai-video-types">
      <div class="wrap">
        {head('AI video comes in <span class="accent">many forms</span>', 'Samples', esc(Z('Every clip here was made with AI.', '这里每一支视频都是用 AI 做的。')))}
        <div class="samples">{av_figs()}</div>
      </div>
    </section>
'''


def _imgs(rows, cls):
    return f'<div class="smp-grid {cls}">' + ''.join(
        f'<figure class="smp-img" data-rv><a href="/assets/samples/{f}.webp" target="_blank" rel="noopener"><img src="/assets/samples/{f}.webp" alt="{esc(alt)}" loading="lazy"></a><figcaption>{esc(t)}</figcaption></figure>' for f, t, alt in rows) + '</div>'


def module_samples():
    lbl = {k: esc(v) for k, v in dict(prompt=Z('Prompt', '指令'), hook=Z('Hook', '开头'), body=Z('Body', '内容'), cta=Z('CTA', '行动呼吁'), tags=Z('Hashtags', '话题标签')).items()}
    chat = '<div class="smp-grid g3">' + ''.join(
        f'''<div class="smp-card" data-rv><div class="smp-k">{tool}</div><h3 class="smp-t">{esc(t)}</h3>
          <div class="chat-q"><span>{lbl["prompt"]}</span><p>{esc(q)}</p></div><div class="chat-a">{"".join(f"<p>{esc(x)}</p>" for x in a)}</div></div>''' for tool, t, q, a in CHAT_SAMPLES) + '</div>'
    caps = '<div class="smp-grid g3">' + ''.join(
        f'''<div class="smp-card" data-rv><div class="smp-k">{esc(prod)}</div>
          <dl class="cap"><dt>{lbl["hook"]}</dt><dd class="cap-hook">{esc(h)}</dd><dt>{lbl["body"]}</dt><dd>{esc(b)}</dd><dt>{lbl["cta"]}</dt><dd>{esc(c)}</dd><dt>{lbl["tags"]}</dt><dd class="cap-tags">{Z(tags, tags)}</dd></dl></div>''' for prod, h, b, c, tags in CAPTION_SAMPLES) + '</div>'
    flows = '<div class="smp-grid g3">' + ''.join(
        f'''<div class="smp-card" data-rv><h3 class="smp-t">{esc(t)}</h3><ol class="flow">{"".join(f"<li>{esc(x)}</li>" for x in st)}</ol></div>''' for t, st in FLOW_SAMPLES) + '</div>'
    plans = '<div class="smp-grid g3">' + ''.join(
        f'''<div class="smp-card" data-rv><h3 class="smp-t">{esc(t)}</h3><dl class="kv">{"".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in rows)}</dl></div>''' for t, rows in PLAN_SAMPLES) + '</div>'
    panels = [('s-tools', Z('AI tools', 'AI 工具'), chat), ('s-video', Z('AI video', 'AI 视频'), f'<div class="samples">{av_figs()}</div>'),
              ('s-graphics', Z('AI graphics', 'AI 设计'), _imgs(POSTERS, 'g3 posters')), ('s-web', Z('AI website', 'AI 网站'), _imgs(SITES, 'g3 sites')),
              ('s-captions', Z('AI captions', 'AI 文案'), caps), ('s-flow', Z('AI system flow', 'AI 自动化'), flows), ('s-marketing', Z('AI marketing', 'AI 营销'), plans)]
    return f'''    <section class="tile tile-dark" id="samples">
      <div class="wrap">
        {head(esc(Z('See what you will', '看看你将会')) + ' <span class="accent">' + esc(Z('make in class.', '在课堂上做出什么。')) + '</span>', esc(Z('Sample work', '作品样本')), esc(Z('Three samples from every module. All of it was made with AI.', '每个单元 3 个样本，全部用 AI 完成。')), style='margin-bottom:40px')}
{tabs('Sample work by module', panels)}
      </div>
    </section>
'''


# ------------------------------------------------ plans
def price_plan(name, price, unit, note, feats, msg, label, flag='', best=False, pay=''):
    href = PAY.get(pay) or wa(msg)
    secure = f'<p class="plan-secure">{esc(Z("Secure checkout by Stripe: card, FPX or GrabPay", "由 Stripe 安全结账：信用卡、FPX 或 GrabPay"))}</p>' if PAY.get(pay) else ''
    fl = f'<span class="plan-flag">{esc(flag)}</span>' if flag else ''
    return f'''<div class="plan{' plan-best' if best else ''}" data-rv>
            <div class="plan-top"><span class="plan-name">{esc(name)}</span>{fl}</div>
            <div class="plan-price"><span class="plan-cur">RM</span>{price}<span class="plan-unit">{esc(unit)}</span></div>
            <p class="plan-note">{note}</p>
            {ticks(feats)}
            <a class="btn {'btn-primary' if best else 'btn-ghost'}" href="{href}" onclick="{CONV}" target="_blank" rel="noopener">{esc(label)}</a>{secure}
          </div>'''


def join_steps(product):
    rows = [(Z('Choose your plan', '选择配套'), Z('Monthly or yearly. Tap the button to start on WhatsApp.', '月付或年付，点击按钮到 WhatsApp 开始。')),
            (Z('Make payment', '完成付款'), Z('Our admin sends you the payment details and confirms once it is received.', '我们的客服会发给你付款资料，收到款项后向你确认。')),
            (Z('Get your invite code', '领取邀请码'), Z('We send your personal invite code on WhatsApp. Use it to log in and start.', '我们会通过 WhatsApp 发给你专属邀请码，用它登入就可以开始。'))]
    li = ''.join(f'<li data-rv><b>{i}</b><div><strong>{esc(t)}</strong><span>{esc(d)}</span></div></li>' for i, (t, d) in enumerate(rows, 1))
    return f'<ol class="join">{li}</ol>'


def sb_plans():
    # The QR image is a static file (deploy/assets/scanbuddy-qr.svg) that opens KONGSIKAN; regenerate it if the link changes.
    qr = '<img src="/assets/scanbuddy-qr.svg" alt="' + esc(Z('QR code that opens Scan Buddy', '打开 Scan Buddy 的二维码')) + '" width="132" height="132" loading="lazy">'
    feats = [Z('Google reviews', 'Google 评价'), Z('Xiaohongshu posts', '小红书笔记'), Z('Facebook reviews', 'Facebook 评价'), Z('Dianping (大众点评) reviews', '大众点评评价'),
             Z('One QR code for every platform', '一个二维码通往所有平台'), Z('Scan tracking', '扫码数据追踪')]
    per = round(SB['y'] / 12)
    return f'''    <section class="tile tile-dark" id="plans">
      <div class="wrap">
        {head(esc(Z('Simple pricing.', '价格简单。')) + ' <span class="accent">' + esc(Z('Start with a trial.', '先试用再决定。')) + '</span>', esc(Z('Scan Buddy plans', 'Scan Buddy 配套')))}
        <div class="plans">
          {price_plan(Z('Monthly trial', '月付试用'), SB['m'], Z('/month', '/月'), esc(Z('Try it for a month. Cancel anytime.', '先试一个月，随时可以取消。')), feats, SB_M, Z('Start the trial', '开始试用'), pay='sb_m')}
          {price_plan(Z('Yearly', '年付'), SB['y'], Z('/year', '/年'), esc(Z('About RM' + str(per) + ' a month.', '约每月 RM' + str(per) + '。')) + f' <s>RM{SB["full"]}</s>', feats, SB_Y, Z('Subscribe yearly', '订阅年付'), flag=Z('Save RM' + str(SB['save']) + ' (' + str(SB['pct']) + '%)', '省 RM' + str(SB['save']) + '（' + str(SB['pct']) + '%）'), best=True, pay='sb_y')}
        </div>
        <div class="apply" data-rv>
          <div class="apply-qr">{qr}</div>
          <div><b>{esc(Z('Apply as a merchant', '申请成为商家'))}</b><span>{esc(Z('Scan the QR code, or tap the button, to open Scan Buddy and register your shop.', '扫描二维码或点击按钮，打开 Scan Buddy 登记你的店。'))}</span></div>
          <a class="btn btn-ghost btn-sm" href="{KONGSIKAN}" target="_blank" rel="noopener">{esc(Z('Open Scan Buddy', '打开 Scan Buddy'))}</a>
        </div>
        {join_steps('sb')}
        <div class="offer" data-rv>
          <div><b>{esc(Z('Want every tool and every course?', '想要全部工具和全部课程？'))}</b><span>{esc(Z('Scan Buddy is included in the TCM Membership, from RM' + str(MEM['y']) + ' a month.', 'TCM 会员已包含 Scan Buddy，每月 RM' + str(MEM['y']) + ' 起。'))}</span></div>
          <a class="btn btn-ghost btn-sm" href="/membership">{esc(Z('See the Membership', '了解会员'))}</a>
        </div>
      </div>
    </section>
'''


def tool_extra(key):
    return sb_plans() if key == 'scan-buddy' else av_samples()
