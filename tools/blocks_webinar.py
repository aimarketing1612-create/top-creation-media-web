# ---------------------------------------------------------------- Webinar landing page (/webinar)
# A free AI marketing session for ad traffic: pick a session, leave a name and WhatsApp number,
# then add it to your calendar, join the WhatsApp Community and confirm on WhatsApp.
# exec'd inside build_site.py after blocks_v2.py (uses Z, esc, head, wa, ARROW, PHONE).
#
# SETTINGS (edit here, then rebuild):
#   weekday / time   when sessions run (Malaysia time). The page always shows the next upcoming dates.
#   community        your WhatsApp Community invite link. Empty: the button opens a chat with us instead.
#   lead_endpoint    a Google Apps Script web app URL (see tools/webinar-apps-script.gs). When set, every
#                    sign-up is saved to your Google Sheet and added to your Google Calendar automatically.
#   booking_url      optional Cal.com / Google appointment link for 1-to-1 consultations.
WEBINAR = dict(
    weekday=6,            # 0 = Sunday ... 6 = Saturday
    time='20:30',         # 24-hour, Malaysia time (UTC+8)
    minutes=60,
    show=3,               # how many upcoming sessions to offer
    community='',
    lead_endpoint='',
    booking_url='',
)

WB_TITLE = Z('Free AI Marketing Class for Business Owners | Top Creation Media', '免费 AI 营销分享会：写给老板 | Top Creation Media')
WB_DESC = Z('A free online class for business owners in Malaysia: how to use AI to make content, run ads and follow up leads, with live Q&A. Pick a session and save your seat.',
            '写给马来西亚老板的免费线上分享会：怎样用 AI 做内容、投广告、跟进顾客，最后有真人问答。选一个场次，立即预留位子。')
WB_LEARN_IMG = {'sparkles': ('/assets/samples/poster-boba.webp', Z('AI-made poster for a bubble tea promotion', 'AI 制作的奶茶促销海报')),
                'target': ('/assets/meta-dashboard.webp', Z('Meta Ads Manager showing campaign results', 'Meta 广告管理工具里的活动成效')),
                'zap': ('/assets/samples/flow-wa.webp', Z('WhatsApp AI auto-reply booking a customer', 'WhatsApp AI 自动回复帮顾客预约'))}
WB_AGENDA = [('0–10', Z('Where AI saves you the most time', 'AI 最能帮你省时间的地方')), ('10–40', Z('Live demo: content, ads and follow-up', '现场示范：内容、广告与跟进')),
             ('40–60', Z('Q&A with our trainers', '导师真人问答'))]
WB_TEAM = [('emma', 'Emma', Z('AI & Marketing Director', 'AI 与营销总监')), ('mac', 'Mac', Z('SEO & AI Strategist', 'SEO 与 AI 策略师')),
           ('jess', 'Jess', Z('HR & Media Advertising Manager', '人事与媒体广告经理')), ('marcus', 'Marcus', Z('Planning & Operation Consultant', '策划与营运顾问'))]
WB_LEARN = [
    ('sparkles', Z('Make a month of content in one afternoon', '一个下午做完一个月的内容'), Z('The prompts and tools we use to plan posts, write captions and make videos with AI.', '我们用来规划贴文、写文案、做视频的 AI 指令和工具。')),
    ('target', Z('Ads that bring enquiries, not just likes', '带来询问的广告，不只是点赞'), Z('How to set up a Meta ad that sends people to your WhatsApp, and which numbers to watch.', '怎样设置把人带到 WhatsApp 的 Meta 广告，以及要看哪几个数字。')),
    ('zap', Z('Follow up every lead, even while you sleep', '睡觉时也能跟进每一个顾客'), Z('A simple AI flow that replies on WhatsApp and reminds you who to call back.', '一个简单的 AI 流程，自动在 WhatsApp 回复，并提醒你该回电给谁。')),
]
WB_PAINS = [
    ('money', Z('You pay for ads, but the enquiries do not come', '广告费一直在烧，询问却没有进来'), Z('Boosting posts and hoping for the best. Money gone, and you cannot tell what worked.', '一直 Boost 贴文碰运气，钱花了，却不知道哪一个有效。')),
    ('clock', Z('Thinking of content every day is exhausting', '每天想内容想到头痛'), Z('You know you should post more, but there is no time between running the business.', '知道要多发内容，可是忙着做生意，根本没时间。')),
    ('outsource', Z('Want more content? The agency charges extra', '想多一些内容，外包又要加钱'), Z('And when you need them, they disappear or reply late. By the time the video is ready, the trend is over.', '要找他们时人又不见、回复又慢，等到内容做好，流量期早就过了。')),
    ('people', Z('Good marketing staff are hard to hire and keep', '好的营销人员请不到、也留不住'), Z('Hiring takes months, and when staff leave, everything they learned leaves with them.', '请人要花好几个月，员工一走，经验也跟着带走。')),
    ('chat', Z('Customers ask on WhatsApp, and no one replies in time', '顾客在 WhatsApp 问了，没人及时回'), Z('A late reply is a lost sale. At night and on weekends, leads go cold.', '回慢一点，生意就跑了。晚上和周末的询问，很多都流失了。')),
    ('ai', Z('Everyone talks about AI, but where do you start?', '大家都在讲 AI，可是要从哪里开始？'), Z('Too many tools, too many videos, and none of it is about your business.', '工具太多、教学太杂，没有一个是针对你的生意。')),
]
WB_AFTER = [Z('Know which AI tool to use for each job, and which to skip', '知道每件事该用哪个 AI 工具，哪些不用浪费时间'),
            Z('A clear way to make a month of content in one afternoon', '一套一个下午做完一个月内容的方法'),
            Z('A simple ad setup that sends enquiries to your WhatsApp', '一个把询问带到 WhatsApp 的简单广告设置'),
            Z('A follow-up flow so no customer is left waiting', '一个让每位顾客都不会等太久的跟进流程'),
            Z('Answers to your own questions, from people who do this every day', '每天在做营销的导师，直接回答你自己的问题')]
WB_WHY = [('8+', Z('years running marketing', '年营销实战经验')), ('500+', Z('clients served', '服务过的客户')), ('3,000+', Z('videos produced', '支制作过的视频')), ('RM0', Z('to join, no card needed', '免费参加，不需要信用卡'))]
WB_PIC = {
    'outsource': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/><path d="M3 3l18 18"/>',
    'money': '<circle cx="12" cy="12" r="8.5"/><path d="M14.8 9.2c-.5-1-1.6-1.5-2.8-1.5-1.6 0-2.8.9-2.8 2.1 0 2.9 5.8 1.4 5.8 4.3 0 1.2-1.3 2.2-3 2.2-1.3 0-2.5-.6-3-1.6M12 6v1.7M12 16.3V18"/>',
    'clock': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    'people': '<circle cx="9" cy="8" r="3"/><path d="M3.5 19a5.5 5.5 0 0111 0"/><path d="M16 5.5a3 3 0 010 5.6M17.5 13.5a5 5 0 013 5.5"/>',
    'chat': '<path d="M20 11.5a7.5 7.5 0 01-11.1 6.6L4 19.5l1.4-4.6A7.5 7.5 0 1120 11.5z"/><path d="M9 10.5h6M9 13.5h4"/>',
    'ai': '<rect x="6" y="6" width="12" height="12" rx="3"/><path d="M9.5 14.5l1.5-5 1.5 5M10 13h2M15 9.5v5M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/>',
    'down': '<path d="M3 7l6.5 6.5 4-4L21 17"/><path d="M21 11v6h-6"/>',
}
WB_FOR = [Z('Business owners who want more customers without hiring more staff', '想多一些顾客、又不想多请人的老板'),
          Z('Marketing teams that want to work faster with AI', '想用 AI 提高效率的营销团队'),
          Z('Beginners: no coding or design skills needed', '零基础：不需要会写程式或设计')]
WB_FAQ = [
    (Z('Is the class really free?', '分享会真的免费吗？'), Z('Yes. There is no fee and no card needed. At the end we share how our Live Class and Membership work, for those who want to go further.', '是的，完全免费，也不需要信用卡。最后我们会介绍线下实战班和会员，给想继续深入的人参考。')),
    (Z('Where does the class happen?', '分享会在哪里进行？'), Z('Online. After you sign up, we send the link to your WhatsApp before the class starts.', '线上进行。报名后，我们会在开课前把链接发到你的 WhatsApp。')),
    (Z('Is it live?', '是现场直播吗？'), Z('The lesson is a prepared class so every session covers everything. Our trainers then join live to answer your questions.', '课程部分是预先准备好的完整内容，确保每一场都讲到重点；之后导师会真人上线回答你的问题。')),
    (Z('What if I cannot make it?', '如果那天没空怎么办？'), Z('Pick another session, or WhatsApp us and we will move you to the next one.', '选择其他场次，或 WhatsApp 我们，帮你改到下一场。')),
]
WB_IC = {
    'sparkles': '<path d="M12 3l1.8 4.9L19 9.7l-5.2 1.9L12 16.5l-1.8-4.9L5 9.7l5.2-1.8z"/><path d="M19 15l.8 2.2 2.2.8-2.2.8L19 21l-.8-2.2-2.2-.8 2.2-.8z"/>',
    'target': '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
    'zap': '<path d="M13 2.5L5 13.5h6l-1 8 8-11h-6z"/>',
}
for _en, _zh in [
    ('Hi, I signed up for the free AI marketing class.', '你好，我报名了免费 AI 营销分享会。'),
]:
    Z(_en, _zh)


def _wb_ic(k):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{WB_IC[k]}</svg>'


def webinar_body():
    W = WEBINAR
    L = {k: esc(v) for k, v in dict(
        seat=Z('Save my free seat', '免费预留位子'), name=Z('Your name', '你的名字'), phone=Z('WhatsApp number', 'WhatsApp 号码'),
        pick=Z('Choose a session', '选择场次'), loading=Z('Loading the next sessions…', '正在载入场次…'), note=Z('We only use your number to send the class link and reminders.', '你的号码只会用来发送上课链接和提醒。'),
        done=Z('You are in!', '报名成功！'), next=Z('Three quick steps so you do not miss it:', '三个小步骤，确保你不会错过：'),
        cal=Z('Add to my calendar', '加入我的日历'), comm=Z('Join the WhatsApp Community', '加入 WhatsApp 社群'), conf=Z('Confirm on WhatsApp', '在 WhatsApp 确认'),
        s1=Z('Save the date', '记下时间'), s2=Z('Get reminders and the link', '收到提醒和链接'), s3=Z('Tell us you are coming', '告诉我们你会来'),
        starts=Z('Starts in', '距离开始'), d=Z('days', '天'), h=Z('hours', '小时'), m=Z('min', '分'), s=Z('sec', '秒'),
        err_phone=Z('Please enter a valid WhatsApp number.', '请输入正确的 WhatsApp 号码。'), err_name=Z('Please enter your name.', '请输入你的名字。'),
        evt=Z('Free AI Marketing Class by Top Creation Media', 'Top Creation Media 免费 AI 营销分享会'),
        evtd=Z('Online class with live Q&A. We will send the link to your WhatsApp before it starts.', '线上分享会，最后有真人问答。开课前会把链接发到你的 WhatsApp。'),
        msg=Z('Hi, I signed up for the free AI marketing class.', '你好，我报名了免费 AI 营销分享会。'),
        sess=Z('Session', '场次'), nm=Z('Name', '名字'),
    ).items()}
    learn = ''.join(f'<div class="wb-card" data-rv><div class="wb-card-img"><img src="{WB_LEARN_IMG[k][0]}" alt="{esc(WB_LEARN_IMG[k][1])}" loading="lazy"></div><div class="wb-card-body"><i>{_wb_ic(k)}</i><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for k, t, d in WB_LEARN)
    pains = ''.join(f'<div class="wb-pain" data-rv><i><svg viewBox="0 0 24 24" aria-hidden="true">{WB_PIC[k]}</svg></i><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for k, t, d in WB_PAINS)
    after = ''.join(f'<li>{esc(t)}</li>' for t in WB_AFTER)
    why = ''.join(f'<li data-rv><b>{n}</b><span>{esc(t)}</span></li>' for n, t in WB_WHY)
    agenda = ''.join(f'<li data-rv><b>{a}<small>{esc(Z("min", "分钟"))}</small></b><span>{esc(t)}</span></li>' for a, t in WB_AGENDA)
    team = ''.join(f'<figure class="wb-tr" data-rv><img src="/assets/video/team-{k}-cover.jpg" alt="{esc(n)}, {esc(r)}" loading="lazy"><figcaption><b>{n}</b><span>{esc(r)}</span></figcaption></figure>' for k, n, r in WB_TEAM)
    community = W['community'] or wa(Z('Hi, please add me to the TCM WhatsApp Community.', '你好，请把我加入 TCM 的 WhatsApp 社群。'))
    data = (f'data-weekday="{W["weekday"]}" data-time="{W["time"]}" data-minutes="{W["minutes"]}" data-show="{W["show"]}" '
            f'data-endpoint="{esc(W["lead_endpoint"])}" data-phone="{PHONE}" data-community="{esc(community)}"')
    labels = ' '.join(f'data-l-{k}="{v}"' for k, v in L.items())
    form = f'''<form class="wb-form" id="seat" {data} {labels} novalidate>
            <div class="wb-form-head"><b>{L['seat']}</b><span>{esc(Z('Free · Online · Live Q&A', '免费 · 线上 · 真人问答'))}</span></div>
            <fieldset class="wb-sessions"><legend>{L['pick']}</legend><div class="wb-slots" role="radiogroup"><p class="wb-loading">{L['loading']}</p></div></fieldset>
            <label class="wb-field"><span>{L['name']}</span><input name="name" autocomplete="name" required></label>
            <label class="wb-field"><span>{L['phone']}</span><div class="wb-tel"><b>+60</b><input name="phone" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="12 345 6789" required></div></label>
            <p class="wb-err" role="alert" hidden></p>
            <button class="btn btn-primary btn-lg wb-submit" type="submit">{L['seat']} {ARROW}</button>
            <p class="wb-note">{L['note']}</p>
          </form>
          <div class="wb-done" id="wb-done" hidden tabindex="-1">
            <div class="wb-tick" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>
            <h2>{L['done']}</h2><p class="wb-when"></p>
            <div class="wb-count" aria-live="polite"></div>
            <p class="wb-next">{L['next']}</p>
            <ol class="wb-steps">
              <li><b>1</b><div><strong>{L['s1']}</strong><a class="btn btn-ghost btn-sm wb-cal" href="#" target="_blank" rel="noopener">{L['cal']}</a></div></li>
              <li><b>2</b><div><strong>{L['s2']}</strong><a class="btn btn-primary btn-sm wb-comm" href="{esc(community)}" target="_blank" rel="noopener">{L['comm']}</a></div></li>
              <li><b>3</b><div><strong>{L['s3']}</strong><a class="btn btn-ghost btn-sm wb-conf" href="#" target="_blank" rel="noopener">{L['conf']}</a></div></li>
            </ol>
          </div>'''
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in WB_FAQ)
    return f'''    <section class="wb-hero">
      <div class="wb-hero-bg" aria-hidden="true"></div>
      <div class="wb-grid">
        <div class="wb-copy">
          <div class="crumbs rise"><a href="/">Home</a> / {esc(Z('Free class', '免费分享会'))}</div>
          <div class="eyebrow rise">{esc(Z('Free online class · Live Q&A', '免费线上分享会 · 真人问答'))}</div>
          <h1 class="h1 rise wb-h1" style="animation-delay:.05s">{esc(Z('Let AI do your marketing.', '让 AI 帮你做营销，'))} <span class="accent">{esc(Z('You run the business.', '你专心做生意。'))}</span></h1>
          <p class="lede rise" style="animation-delay:.15s">{esc(Z('In one hour, see how business owners in Malaysia use AI to make content, run ads and follow up every lead. Then ask our trainers anything.', '一个小时，看马来西亚的老板们怎样用 AI 做内容、投广告、跟进每一个顾客，最后直接问我们的导师。'))}</p>
          <ul class="wb-facts rise" style="animation-delay:.25s">
            <li><b>60</b><span>{esc(Z('minutes', '分钟'))}</span></li><li><b>RM0</b><span>{esc(Z('free to join', '免费参加'))}</span></li><li><b>Q&amp;A</b><span>{esc(Z('with our trainers', '导师真人答疑'))}</span></li>
          </ul>
        </div>
        <div class="wb-panel rise" style="animation-delay:.2s">{form}</div>
      </div>
    </section>

    <section class="tile tile-dark wb-pains-sec">
      <div class="wrap">
        {head(esc(Z('Does this sound like', '这是不是')) + ' <span class="accent">' + esc(Z('your business?', '你的生意？')) + '</span>', esc(Z('Sound familiar?', '你也遇到吗？')), esc(Z('Most business owners we meet tell us the same six things.', '我们见过的老板，几乎都在为这六件事烦恼。')))}
        <div class="wb-pains">{pains}</div>
        <div class="wb-turn" data-rv>
          <div class="wb-turn-copy"><div class="eyebrow">{esc(Z('After one hour', '一个小时之后'))}</div><h2 class="h2">{esc(Z('You leave with a plan,', '你带走的是一套方法，'))} <span class="accent">{esc(Z('not just ideas.', '不只是灵感。'))}</span></h2>
            <a class="btn btn-primary btn-lg" href="#seat">{L['seat']} {ARROW}</a></div>
          <ul class="wb-after">{after}</ul>
        </div>
      </div>
    </section>


    <section class="tile tile-raise">
      <div class="wrap">
        {head(esc(Z('What you will learn', '你会学到什么')), esc(Z('In one hour', '一个小时')))}
        <div class="wb-cards">{learn}</div>
        <ol class="wb-agenda">{agenda}</ol>
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap">
        {head(esc(Z('Meet your trainers', '认识你的导师')), esc(Z('Live Q&A', '真人问答')), esc(Z('The team that runs marketing for 500+ clients answers your questions at the end.', '为 500 多个客户操盘营销的团队，最后亲自回答你的问题。')))}
        <div class="wb-team">{team}</div>
      </div>
    </section>

    <section class="tile tile-dark">
      <div class="wrap wb-split">
        <figure class="banner" data-rv><img src="/assets/img/mem-class.webp" alt="{esc(Z('A TCM trainer teaching a class of business owners how to use AI', 'TCM 导师正在教一班老板使用 AI'))}" width="1500" height="842" loading="lazy"></figure>
        <div data-rv>
          <div class="eyebrow">{esc(Z('Who it is for', '适合谁'))}</div>
          <h2 class="h2" style="margin-top:12px">{esc(Z('Made for busy owners.', '为忙碌的老板而设。'))}</h2>
          {ticks(WB_FOR)}
          <a class="btn btn-primary" href="#seat" style="margin-top:28px">{L['seat']} {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="tile tile-raise">
      <div style="max-width:900px;margin:0 auto">
        {head(esc(Z('Questions, answered.', '常见问题')), 'FAQ')}
        <div class="faq" data-rv>{faq}</div>
      </div>
    </section>

    <section class="cta wb-cta">
      <h2 class="h2" data-rv>{esc(Z('One hour can change how you market.', '一个小时，改变你做营销的方式。'))}</h2>
      <p class="lede" data-rv>{esc(Z('Free, online, with live Q&A. Seats for each session are limited.', '免费、线上、有真人问答。每一场名额有限。'))}</p>
      <div class="btn-row" data-rv><a class="btn btn-primary btn-lg" href="#seat">{L['seat']} {ARROW}</a></div>
    </section>
'''


def webinar_ld():
    # Session dates are computed in the browser, so no Event markup (Google requires a fixed startDate).
    return {'@context': 'https://schema.org', '@graph': [faq_ld(WB_FAQ)]}
