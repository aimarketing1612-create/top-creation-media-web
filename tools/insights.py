"""Insights: TCM's articles on AI and marketing, in English and Chinese.

Each text is written as T(english, chinese). The English goes into the page; the pair
is added to the Chinese build's dictionary (build_zh.ZH) at build time, so an article
and its translation live side by side here instead of in zh.json.
"""
import html

PAIRS = {}


def T(en, zh):
    # Chinese text uses Chinese quotes: a straight " next to ？ or ， blocks line breaks on phones.
    parts = zh.split('"')
    zh = ''.join(x + ('“' if i % 2 == 0 else '”') for i, x in enumerate(parts[:-1])) + parts[-1]
    PAIRS[' '.join(en.split())] = zh
    return en


def esc(s):
    return html.escape(s, quote=False)


DATE = '2026-11-25'

# --------------------------------------------------------------------------- articles
ARTICLES = [
    {
        'slug': 'chatgpt-vs-gemini-vs-claude',
        'short': T('ChatGPT vs Gemini vs Claude', 'ChatGPT、Gemini 与 Claude 比较'),
        'h1': T('ChatGPT vs Gemini vs Claude: which AI should your business use?', 'ChatGPT、Gemini 还是 Claude：你的生意该用哪个 AI？'),
        'title': T('ChatGPT vs Gemini vs Claude for Business (Malaysia Guide) | TCM', 'ChatGPT、Gemini 与 Claude 商用比较（马来西亚指南）| TCM'),
        'desc': T('ChatGPT, Gemini or Claude? A plain comparison for business owners in Malaysia and Singapore: what each does best, how to choose and how to use it safely.',
                  'ChatGPT、Gemini 还是 Claude？写给马来西亚与新加坡老板的白话比较：每个 AI 最擅长什么、15 分钟内怎么选、怎样安全使用。'),
        'lede': T('All three can write, summarise, analyse and brainstorm. The real difference is where each one fits into your working day. This is how we help business owners choose in our AI classes.',
                  '三个都会写作、总结、分析和想点子。真正的差别，是它们各自适合放进你一天工作的哪个环节。以下是我们在 AI 课程里帮老板做选择的方法。'),
        'card': T('What each AI does best, a 15-minute test to pick one, and how to use it safely with business data.',
                  '每个 AI 最擅长什么、15 分钟选出适合你的那个，以及怎样安全处理公司资料。'),
        'tags': ['ChatGPT', 'Gemini', 'Claude'],
        'blocks': [
            ('tldr', T('Short answer', '简短回答'),
             T('If your team already lives in Gmail, Docs and Sheets, start with Gemini. If you write long proposals or work with big documents, try Claude. If you want one all-rounder with images, voice and a huge library of add-ons, start with ChatGPT. Most businesses end up using two of them.',
               '如果团队每天都在用 Gmail、Docs 和 Sheets，先用 Gemini。如果常写长篇提案或处理大份文件，试试 Claude。如果想要一个什么都会、能做图、能语音、扩展功能最多的全能型，先用 ChatGPT。多数公司最后会同时用其中两个。')),
            ('h2', T('At a glance', '一眼看懂')),
            ('table',
             [T('ChatGPT', 'ChatGPT'), T('Gemini', 'Gemini'), T('Claude', 'Claude')],
             [
                 (T('Best at', '最擅长'), [T('All-round writing, images, voice and custom GPTs', '全能写作、做图、语音和自定义 GPT'),
                                         T('Working inside Google Search, Gmail, Docs, Sheets and Drive', '在 Google 搜索、Gmail、Docs、Sheets 和 Drive 里直接工作'),
                                         T('Long documents, careful writing and detailed analysis', '长篇文件、细致写作和深入分析')]),
                 (T('Good first task', '第一个可以试的任务'), [T('Write 10 versions of an ad caption', '写 10 个版本的广告文案'),
                                                         T("Summarise last month's enquiry emails into a sheet", '把上个月的询问邮件整理成一张表'),
                                                         T('Turn a 40-page proposal into a one-page brief', '把 40 页的提案浓缩成一页摘要')]),
                 (T('Watch out for', '要注意'), [T('Confident answers that are wrong: check facts and numbers', '自信但错误的答案：事实和数字要核对'),
                                               T('Quality differs from one Google app to another', '不同 Google 应用里的表现不一样'),
                                               T('Fewer built-in image and media tools', '内置的做图和多媒体功能较少')]),
             ]),
            ('p', T('Plans and features change almost every month, so treat this as a starting point and check each official page for current prices in ringgit or Singapore dollars.',
                    '这三家的方案和功能几乎每个月都在更新，以上只是起点。最新价格请到各自的官网查看。')),
            ('h2', T('How to choose in 15 minutes', '15 分钟内选出适合你的 AI')),
            ('ol', [
                (T('Pick three real tasks.', '挑三个真实任务。'), T('Use work you did this week: a promotion caption, a reply to a customer complaint, a summary of a supplier quote.', '用这个星期真的做过的工作：一则促销文案、一封回复客户投诉的信、一份供应商报价的摘要。')),
                (T('Give all three the same prompt.', '给三个 AI 同样的指令。'), T('Copy the exact same instructions and files into each one, so you compare the AI and not your wording.', '把完全一样的指令和文件分别贴进去，这样比较的是 AI，不是你的写法。')),
                (T('Score the answers.', '给答案打分。'), T('Rate each answer for accuracy, tone and how much editing it still needs. Time saved is the number that matters.', '按准确度、语气和还要改多少来评分。真正重要的是省下多少时间。')),
                (T('Check your data rules.', '确认公司的资料规定。'), T('Before the team uses it every day, decide what may and may not be pasted in, and whether you need a business plan with data controls.', '在团队天天使用之前，先定好什么资料可以贴、什么不可以，以及要不要用有资料管控的企业方案。')),
            ]),
            ('h2', T('Using AI safely with business data', '安全地用 AI 处理公司资料')),
            ('ul', [
                (T('Keep personal data out.', '个人资料不要贴进去。'), T('Do not paste IC numbers, bank details or full customer lists into a personal account.', '不要把身份证号码、银行资料或完整的客户名单贴进个人账号。')),
                (T('Use team or business plans for company work.', '公司工作用团队或企业方案。'), T('They give you admin controls and clearer terms on how your data is used.', '它们有管理权限，对资料如何被使用也有更清楚的条款。')),
                (T('A human checks before anything goes out.', '对外发布前一定要有人审核。'), T('AI drafts, people approve: prices, promises and claims must be right.', 'AI 起草，人来批准：价格、承诺和宣传内容都必须正确。')),
                (T('Save the prompts that work.', '把好用的指令存起来。'), T('A shared prompt library turns one good result into a team habit.', '建立共享的指令库，把一次成功变成整个团队的习惯。')),
            ]),
            ('h2', T('Three prompts to try today', '今天就能试的三个指令')),
            ('prompt', T('You are a marketing copywriter for a [type of business] in Kuala Lumpur. Write 10 short Facebook ad captions for [product or offer]. Mix English and simple Malay where it sounds natural. Each caption under 125 characters, with one clear call to action.',
                         '你是吉隆坡一家[行业]的营销文案。为[产品或优惠]写 10 则简短的 Facebook 广告文案。每则不超过 60 个字，并有一个清楚的行动呼吁。')),
            ('prompt', T('Here are 20 customer reviews. Group them into the top 5 things customers love and the top 3 complaints. For each complaint, suggest one fix we can make this month.',
                         '以下是 20 则顾客评价。整理出顾客最喜欢的 5 件事和最常见的 3 个抱怨。每个抱怨各建议一个这个月就能做到的改善。')),
            ('prompt', T('Turn this product description into a 30-second video script: a hook in the first 3 seconds, three benefits, and a closing line with our WhatsApp number.',
                         '把这段产品介绍改成 30 秒的视频脚本：前 3 秒要有吸引人的开头，讲三个好处，最后一句带出我们的 WhatsApp 号码。')),
            ('h2', T('What about English, Malay and Chinese?', '英文、马来文和中文都可以吗？')),
            ('p', T('All three handle English, Bahasa Melayu and Chinese well enough for everyday business writing. Tone is where they differ, so test a caption in the language your customers actually use, and ask a native speaker on your team to read it before it goes live.',
                    '三个 AI 处理英文、马来文和中文的日常商业写作都没问题，差别在语气。用你顾客实际使用的语言测试一则文案，上线前请团队里以该语言为母语的同事看一遍。')),
            ('tip', T('In our AI Academy, students run this comparison on their own business tasks in the first class, so they leave knowing which tool to open for which job.',
                      '在我们的 AI 学院，学员第一堂课就会用自己公司的任务做这个比较，下课时就知道什么工作该打开哪个工具。')),
        ],
        'faq': [
            (T('Which AI is best for a small business in Malaysia?', '马来西亚的小生意最适合用哪个 AI？'),
             T('There is no single winner. Gemini suits teams that work in Google Workspace, Claude suits long documents and careful writing, and ChatGPT is the most complete all-rounder. Run the same three real tasks in each and keep the one that saves your team the most time.',
               '没有绝对的赢家。用 Google Workspace 的团队适合 Gemini，处理长文件和细致写作适合 Claude，ChatGPT 则是功能最完整的全能型。用三个真实任务分别测试，留下最能帮团队省时间的那个。')),
            (T('Is the free version enough?', '免费版够用吗？'),
             T('For trying things out, yes. For daily company work, a paid business or team plan is usually worth it: higher limits, better models and admin controls over company data.',
               '试用的话够了。如果是公司每天要用，付费的企业或团队方案通常值得：用量更高、模型更强，也能管理公司资料。')),
            (T('Can these AI tools write in Bahasa Melayu and Chinese?', '这些 AI 能写马来文和中文吗？'),
             T('Yes. All three write in English, Bahasa Melayu and Chinese. Check the tone with a native speaker before publishing, especially for ads and customer replies.',
               '可以，三个都能写英文、马来文和中文。发布前请以该语言为母语的人检查语气，特别是广告和回复顾客的内容。')),
        ],
        'next': ('/ai-classes', T('Learn to use AI for your business, hands-on', '实战学会用 AI 做生意'),
                 T('Our AI Academy covers ChatGPT, Claude and Gemini, AI video, graphics, captions, websites and automation. No coding needed.',
                   '我们的 AI 学院教 ChatGPT、Claude 和 Gemini，还有 AI 视频、设计、文案、网站和自动化，零编程基础。'),
                 T('See the AI Academy', '了解 AI 学院')),
    },
    {
        'slug': 'what-is-aeo-geo',
        'short': T('What is AEO and GEO?', '什么是 AEO 和 GEO？'),
        'h1': T('What is AEO and GEO? How to get your business recommended by AI', '什么是 AEO 和 GEO？让 AI 推荐你的生意'),
        'title': T('What is AEO & GEO? Get Recommended by ChatGPT and Gemini | TCM', '什么是 AEO 与 GEO？让 ChatGPT 和 Gemini 推荐你 | TCM'),
        'desc': T('AEO and GEO explained for businesses in Malaysia and Singapore: how ChatGPT, Gemini and Google AI Overviews pick who to recommend, and 7 steps to get there.',
                  '写给马来西亚与新加坡老板的 AEO 与 GEO 说明：ChatGPT、Gemini 和 Google AI 摘要怎样决定推荐谁，以及成为答案的 7 个步骤。'),
        'lede': T('Customers no longer only type keywords into Google. They ask ChatGPT, Gemini or Google\'s AI Overviews "which agency should I hire?" or "best facial in Puchong?". AEO and GEO are how you become the answer.',
                  '顾客已经不只在 Google 打关键词了。他们会问 ChatGPT、Gemini 或 Google 的 AI 摘要："我该找哪家公司？""蒲种哪里做脸最好？"AEO 和 GEO，就是让你成为那个答案的方法。'),
        'card': T('How ChatGPT, Gemini and Google AI Overviews pick who to recommend, and 7 steps to become the answer.',
                  'ChatGPT、Gemini 和 Google AI 摘要怎样选择推荐对象，以及成为答案的 7 个步骤。'),
        'tags': ['AEO', 'GEO', 'SEO'],
        'blocks': [
            ('tldr', T('Short answer', '简短回答'),
             T('AEO (answer engine optimisation) means shaping your content so AI assistants and Google\'s answer features can quote it. GEO (generative engine optimisation) means making your brand show up, and be recommended, inside AI-written answers. Both build on good SEO; they do not replace it.',
               'AEO（答案引擎优化）是把内容整理成 AI 助手和 Google 答案功能可以直接引用的样子。GEO（生成式引擎优化）是让你的品牌出现在 AI 写出的答案里，而且被推荐。两者都建立在好的 SEO 之上，不是取代 SEO。')),
            ('h2', T('SEO, AEO and GEO side by side', 'SEO、AEO 与 GEO 对照')),
            ('table',
             [T('SEO', 'SEO'), T('AEO', 'AEO'), T('GEO', 'GEO')],
             [
                 (T('Goal', '目标'), [T('Rank in Google results', '在 Google 搜索结果排名'),
                                     T('Be the quoted answer', '成为被引用的答案'),
                                     T('Be named and recommended by AI', '被 AI 点名推荐')]),
                 (T('Where you show up', '出现在哪里'), [T('Blue links and the map pack', '蓝色链接和地图结果'),
                                                       T('Featured snippets, AI Overviews, voice answers', '精选摘要、AI 摘要、语音答案'),
                                                       T('ChatGPT, Gemini, Perplexity, Copilot answers', 'ChatGPT、Gemini、Perplexity、Copilot 的回答')]),
                 (T('What matters most', '最重要的是'), [T('Relevance, links, speed', '相关性、外部链接、速度'),
                                                       T('Clear answers and structured data', '清楚的答案和结构化数据'),
                                                       T('Mentions on trusted sites and consistent facts', '在可信网站被提及，以及资料一致')]),
             ]),
            ('h2', T('Why it matters now in Malaysia and Singapore', '为什么现在对马来西亚和新加坡很重要')),
            ('ul', [
                (T('AI answers name only a few businesses.', 'AI 的回答只会点名几家。'), T('A Google page shows ten results; an AI answer usually recommends three to five. If you are not one of them, the customer may never see you.', 'Google 一页有十个结果，AI 的回答通常只推荐三到五家。不在里面，顾客可能根本看不到你。')),
                (T('"Best of" lists carry weight.', '"十大推荐"类文章很有分量。'), T('When we researched "best digital marketing agency Malaysia", most of page one was list articles and directories, and AI assistants lean on the same sources.', '我们研究"马来西亚最佳数码营销公司"时，第一页大多是排行榜文章和目录网站，AI 助手也大量参考这些来源。')),
                (T('Customers ask in three languages.', '顾客用三种语言提问。'), T('People ask in English, Bahasa Melayu and Chinese. Content in only one language leaves the other answers to your competitors.', '大家会用英文、马来文和中文提问。只有一种语言的内容，其他语言的答案就让给了竞争对手。')),
            ]),
            ('h2', T('7 steps to get recommended by AI', '让 AI 推荐你的 7 个步骤')),
            ('ol', [
                (T('Answer real questions plainly.', '直接回答真实问题。'), T('Use the customer\'s question as a heading and answer it in the first two sentences, then add detail.', '用顾客的问题当标题，前两句就给出答案，再补充细节。')),
                (T('Add structured data.', '加上结构化数据。'), T('Organization, FAQ, product and local business markup tell search engines and AI exactly who you are and what you sell.', '公司、常见问题、产品和本地商家的标记，能清楚告诉搜索引擎和 AI 你是谁、卖什么。')),
                (T('Keep your facts the same everywhere.', '各处资料保持一致。'), T('Name, phone, address, opening hours and prices should match on your website, Google Business Profile, Facebook and every directory.', '公司名称、电话、地址、营业时间和价格，在网站、Google 商家资料、Facebook 和各个目录上都要一致。')),
                (T('Get mentioned on sites AI trusts.', '争取在 AI 信任的网站被提及。'), T('Industry directories, "best of" articles, local news and partner websites are where AI learns which businesses are credible.', '行业目录、"十大推荐"文章、本地新闻和合作伙伴的网站，是 AI 判断哪些商家可信的地方。')),
                (T('Earn reviews that say something.', '累积有内容的评价。'), T('Ask happy customers to mention the service and the result, not just give five stars.', '请满意的顾客写出用了什么服务、得到什么结果，而不只是给五颗星。')),
                (T('Let AI crawlers in.', '让 AI 爬虫进来。'), T('Make sure robots.txt does not block GPTBot, ClaudeBot, PerplexityBot or Google, and add an llms.txt summary of your business.', '确认 robots.txt 没有挡住 GPTBot、ClaudeBot、PerplexityBot 或 Google，并加一份介绍公司的 llms.txt。')),
                (T('Publish in your customers\' languages.', '用顾客的语言发布内容。'), T('A proper Chinese or Malay version of your key pages is one of the fastest ways to show up in more answers.', '把重要页面做成正式的中文或马来文版本，是出现在更多答案里最快的方法之一。')),
            ]),
            ('h2', T('How to check whether AI mentions you', '怎样知道 AI 有没有提到你')),
            ('p', T('Once a month, ask ChatGPT, Gemini and Perplexity the questions your customers would ask, in each language you serve. Note who gets named and which websites are cited. Those cited sites are your to-do list for step four. Keep watching Google Search Console too: AI features still draw on the same index.',
                    '每个月一次，用你服务的每种语言，向 ChatGPT、Gemini 和 Perplexity 问顾客会问的问题。记下哪些公司被点名、引用了哪些网站，这些被引用的网站就是第四步的待办清单。Google Search Console 也要继续看，因为 AI 功能用的还是同一套索引。')),
            ('h2', T('Common mistakes', '常见错误')),
            ('ul', [
                (T('Stuffing keywords.', '堆砌关键词。'), T('AI rewards clear answers, not repeated phrases.', 'AI 看重清楚的答案，不是重复的词。')),
                (T('Blocking AI bots by accident.', '不小心挡住 AI 爬虫。'), T('Some security plugins and old robots.txt files do this without you knowing.', '有些安全插件和旧的 robots.txt 会在你不知情的情况下这样做。')),
                (T('Different prices in different places.', '不同地方价格不一样。'), T('Conflicting facts make AI less sure about recommending you.', '资料互相矛盾，AI 就不太敢推荐你。')),
            ]),
            ('tip', T('AEO and GEO are a long game: expect months, not days. We applied every step above to our own website when we rebuilt it, in English and Chinese.',
                      'AEO 和 GEO 是长期工作，要以月计算，不是几天。我们重建自己的网站时，上面每一步都做了，中英文都有。')),
        ],
        'faq': [
            (T('Is AEO replacing SEO?', 'AEO 会取代 SEO 吗？'),
             T('No. AI assistants and Google\'s AI Overviews draw on the same web pages that SEO improves. AEO and GEO add clear answers, structured data and brand mentions on top of good SEO.',
               '不会。AI 助手和 Google AI 摘要用的，正是 SEO 在优化的那些网页。AEO 和 GEO 是在好的 SEO 之上，再加上清楚的答案、结构化数据和品牌提及。')),
            (T('How long does AEO or GEO take to work?', 'AEO 或 GEO 要多久才见效？'),
             T('Usually a few months. Technical fixes such as structured data and robots.txt work quickly, while mentions on trusted sites and reviews build up over time.',
               '通常要几个月。结构化数据和 robots.txt 这类技术修正很快见效，但在可信网站的提及和评价需要时间累积。')),
            (T('Can a small business show up in ChatGPT answers?', '小生意也能出现在 ChatGPT 的回答里吗？'),
             T('Yes, especially for local and niche questions such as "best bridal makeup in Johor Bahru". Clear answers on your site, a complete Google Business Profile and genuine reviews matter more than company size.',
               '可以，特别是本地和细分领域的问题，例如"新山哪里新娘化妆最好"。网站上有清楚的答案、完整的 Google 商家资料和真实评价，比公司大小更重要。')),
        ],
        'next': ('/marketing-services#google', T('Want AI to recommend your business?', '想让 AI 推荐你的生意？'),
                 T('We run SEO, AEO and GEO for brands in Malaysia and Singapore: technical fixes, content in English and Chinese, Google Business Profile and AI search.',
                   '我们为马来西亚与新加坡品牌做 SEO、AEO 与 GEO：技术优化、中英文内容、Google 商家资料和 AI 搜索。'),
                 T('See our SEO service', '了解 SEO 服务')),
    },
    {
        'slug': 'kling-ai-veo-3-product-video',
        'short': T('Kling AI and Veo 3 for product videos', '用 Kling AI 和 Veo 3 做产品视频'),
        'h1': T('Kling AI and Veo 3: how to turn a product photo into a video ad', 'Kling AI 与 Veo 3：把产品照片变成视频广告'),
        'title': T('Kling AI & Veo 3 Tutorial: Product Video Ads with AI | TCM', 'Kling AI 与 Veo 3 教学：用 AI 做产品视频广告 | TCM'),
        'desc': T('A step-by-step Kling AI and Veo 3 workflow: turn one product photo into short video ads, with a prompt template and what AI video still gets wrong.',
                  '写给商家的 Kling AI 与 Veo 3 步骤教学：把一张产品照片变成短视频广告，附指令模板，以及 AI 视频目前还做不好的地方。'),
        'lede': T('You no longer need a film crew for a product video that stops the scroll. This is the workflow we teach for turning one product photo into short ads with Kling AI and Google\'s Veo 3.',
                  '要做一支让人停下来看的产品视频，已经不一定要请拍摄团队。以下是我们教学员的流程：用 Kling AI 和 Google 的 Veo 3，把一张产品照片变成短视频广告。'),
        'card': T('A 6-step workflow from one product photo to a short video ad, with a prompt template you can copy.',
                  '从一张产品照片到短视频广告的 6 个步骤，附可以直接复制的指令模板。'),
        'tags': ['Kling AI', 'Veo 3', T('AI video', 'AI 视频')],
        'blocks': [
            ('tldr', T('Short answer', '简短回答'),
             T('Kling AI (from Kuaishou) and Veo 3 (from Google, available through Gemini and Google\'s video tools) turn text and images into short video clips. Kling is strong at animating your own product photos; Veo 3 can also generate sound and spoken lines. Use them for product reveals, B-roll and ad variations, not to fake reviews.',
               'Kling AI（快手出品）和 Veo 3（Google 出品，可在 Gemini 和 Google 的视频工具中使用）能把文字和图片变成短视频片段。Kling 擅长让你自己的产品照片动起来；Veo 3 还能生成声音和对白。适合用来做产品亮相、空镜和广告的不同版本，不要用来伪造评价。')),
            ('h2', T('Kling AI vs Veo 3 at a glance', 'Kling AI 与 Veo 3 一眼比较')),
            ('table',
             [T('Kling AI', 'Kling AI'), T('Veo 3', 'Veo 3')],
             [
                 (T('Best for', '最适合'), [T('Bringing an existing product photo to life', '让现有的产品照片动起来'),
                                           T('Cinematic scenes with sound and dialogue', '有声音和对白的电影感画面')]),
                 (T('Start from', '从什么开始'), [T('An image plus a short prompt', '一张图片加简短指令'),
                                                 T('A text prompt, or an image in some tools', '文字指令，部分工具也可用图片')]),
                 (T('Sound', '声音'), [T('Add music and voice when you edit', '剪辑时再加音乐和配音'),
                                      T('Can generate sound effects and speech', '能生成音效和说话声')]),
                 (T('Watch out for', '要注意'), [T('Small text and logos can warp', '小字和标志容易变形'),
                                                T('Your exact product can drift from reality', '产品细节可能和实物不一样')]),
             ]),
            ('p', T('Both tools update often, and plans, credits and limits change. Check the official sites before you budget for a campaign.',
                    '这两个工具更新很快，方案、点数和限制也常变。规划活动预算前，请先到官网确认。')),
            ('h2', T('The 6-step workflow', '6 个步骤的流程')),
            ('ol', [
                (T('Start with a clean product photo.', '先准备一张干净的产品照片。'), T('Good light, sharp focus, a plain background and the product filling most of the frame. AI can only animate what it can see.', '光线好、对焦清楚、背景简单，产品占画面大部分。AI 只能让它看得到的东西动起来。')),
                (T('Write a shot, not a wish.', '写镜头，不要写愿望。'), T('Describe the camera move, what the product does, the setting, the light and the length. "Make it nice" gives you random results.', '描述镜头怎么动、产品怎么动、场景、光线和长度。"弄漂亮一点"只会得到随机结果。')),
                (T('Generate three to five short clips per idea.', '每个想法生成三到五个短片段。'), T('Five to eight seconds each. Short clips fail less, and you will cut them anyway.', '每段五到八秒。短片段比较不容易出错，反正最后也会剪短。')),
                (T('Pick the best and check every frame.', '挑最好的，逐格检查。'), T('Look at the label, the shape and the colour. If the product looks different from the real one, do not use it in an ad.', '看清楚标签、形状和颜色。如果产品和实物不一样，就不要用在广告里。')),
                (T('Edit it into an ad.', '剪成广告。'), T('In CapCut or Canva: a hook in the first two seconds, captions, your logo, the offer and a clear call to action, in vertical 9:16.', '用 CapCut 或 Canva 剪辑：前两秒要有吸引人的开头，加字幕、标志、优惠和清楚的行动呼吁，做成 9:16 直式。')),
                (T('Test two or three versions.', '测试两到三个版本。'), T('Run them as ads with the same budget for a few days and keep the one with the best cost per enquiry.', '用相同预算投放几天，留下每个询问成本最低的那个。')),
            ]),
            ('h2', T('A prompt template you can copy', '可以直接复制的指令模板')),
            ('prompt', T('Slow push-in on [product] standing on [surface], [lighting, e.g. soft morning window light], [one movement, e.g. water droplets running down the bottle], shallow depth of field, premium commercial look, vertical 9:16, 6 seconds, no text.',
                         'Slow push-in on [product] standing on [surface], [lighting, e.g. soft morning window light], [one movement, e.g. water droplets running down the bottle], shallow depth of field, premium commercial look, vertical 9:16, 6 seconds, no text.')),
            ('p', T('Video models usually follow English prompts most closely, so keep the prompt in English even when the ad itself is in Malay or Chinese. Add the captions and voice-over in your language when you edit.',
                    '视频模型通常最能理解英文指令，所以即使广告本身是马来文或中文，指令也建议用英文写。字幕和配音在剪辑时再用你的语言加上。')),
            ('h2', T('What AI video does well, and where it fails', 'AI 视频擅长什么、哪里会出错')),
            ('ul', [
                (T('Good at:', '擅长：'), T('product reveals, mood shots, new backgrounds and seasons, and quick variations for ad testing.', '产品亮相、氛围镜头、更换背景和季节，以及快速做出不同版本测试广告。')),
                (T('Still weak at:', '还不擅长：'), T('readable text and logos, hands holding small items, and keeping the exact product details from shot to shot.', '清楚的文字和标志、手拿小物件，以及每个镜头都保持产品细节一致。')),
                (T('Never use it to:', '绝对不要用来：'), T('invent customer testimonials, show results the product cannot deliver, or copy another brand\'s look.', '伪造顾客见证、展示产品做不到的效果，或抄袭别的品牌风格。')),
                (T('Label it where required.', '按规定标示。'), T('Meta and TikTok ask advertisers to label realistic AI-generated content. Follow each platform\'s current rules.', 'Meta 和 TikTok 要求广告主标示逼真的 AI 生成内容。请遵守各平台最新的规定。')),
            ]),
            ('tip', T('You can see AI video samples, from UGC-style ads to product footage and cinematic B-roll, on our AI Academy page.',
                      '从 UGC 风格广告到产品画面和电影感空镜，各种 AI 视频样本都可以在我们的 AI 学院页面看到。')),
        ],
        'faq': [
            (T('Is Kling AI free?', 'Kling AI 免费吗？'),
             T('Kling has offered free credits with limits on length, quality and speed, and paid plans for more and better output. Plans change often, so check the official site for current pricing.',
               'Kling 一直有提供有限的免费点数（长度、画质和速度有限制），付费方案则可以生成更多、更好的视频。方案常有变动，最新价格请看官网。')),
            (T('Can I use AI video in Facebook and TikTok ads?', 'Facebook 和 TikTok 广告可以用 AI 视频吗？'),
             T('Yes, as long as the video does not mislead. Show the real product accurately, do not fake testimonials, and label realistic AI content where the platform asks you to.',
               '可以，只要视频不误导人。真实呈现产品，不伪造见证，平台要求时标示逼真的 AI 内容。')),
            (T('Do I need video editing skills?', '需要会剪辑视频吗？'),
             T('Basic skills are enough. Generating clips takes prompts, and turning them into an ad takes a free editor such as CapCut or Canva. Our AI classes cover both.',
               '基本技能就够了。生成片段靠指令，剪成广告用 CapCut 或 Canva 这类免费工具就行。我们的 AI 课程两部分都会教。')),
        ],
        'next': ('/ai-video', T('Turn your product photos into video ads', '把你的产品照片变成视频广告'),
                 T('TCM AI Video makes ready-to-post marketing videos from a product photo, and our AI Academy teaches the full workflow hands-on.',
                   'TCM AI Video 能把一张产品照片变成可直接发布的营销视频，AI 学院则实战教你完整流程。'),
                 T('Try AI Video', '试试 AI Video')),
    },
]

INDEX = {
    'title': T('Insights: AI and Marketing Guides for Business | Top Creation Media', '文章：写给老板的 AI 与营销指南 | Top Creation Media'),
    'desc': T('Practical guides on AI and marketing for business owners in Malaysia and Singapore: ChatGPT vs Gemini vs Claude, AEO and GEO, AI product videos and more.',
              '写给马来西亚与新加坡老板的 AI 与营销实用指南：ChatGPT、Gemini 与 Claude 比较、AEO 与 GEO、AI 产品视频等。'),
    'h1': T('Insights on AI and marketing.', 'AI 与营销，讲清楚。'),
    'lede': T('Plain, practical guides from the TCM team for business owners in Malaysia and Singapore. What works, what to avoid, and what to try this week.',
              'TCM 团队写给马来西亚与新加坡老板的白话实用指南：什么有效、什么要避免、这个星期可以试什么。'),
}

LABELS = {
    'insights': T('Insights', '文章'),
    'home': T('Home', '首页'),
    'read': T('min read', '分钟阅读'),
    'by': T('By the Top Creation Media team', 'Top Creation Media 团队'),
    'faq': T('Questions, answered.', '常见问题'),
    'more': T('Read next', '继续阅读'),
    'readmore': T('Read the guide', '阅读全文'),
    'updated': T('Updated', '更新于'),
    'prompt': T('Prompt', '指令'),
}

# Other page text on the Insights pages (breadcrumbs, call to action, nav and index links)
for en, zh in [
    ('/ Insights', '/ 文章'), ('/ ChatGPT vs Gemini vs Claude', '/ ChatGPT、Gemini 与 Claude 比较'),
    ('/ What is AEO and GEO?', '/ 什么是 AEO 和 GEO？'), ('/ Kling AI and Veo 3 for product videos', '/ 用 Kling AI 和 Veo 3 做产品视频'),
    ('Not sure where to start?', '不知道从哪里开始？'), ('Ask us.', '问我们。'),
    ('Tell us about your business and we will point you to the right next step: a service, a class or a tool.', '告诉我们你的生意情况，我们会建议最适合的下一步：服务、课程或工具。'),
    ('Want this done for you?', '想让我们帮你做？'), ('Let’s talk.', '聊一聊。'),
    ('Our team runs SEO, ads, content and AI for brands in Malaysia and Singapore, or teaches your team to do it.', '我们的团队为马来西亚与新加坡品牌做 SEO、广告、内容和 AI，也可以教你的团队自己做。'),
    ('Hi, I read your article and have a question.', '你好，我看了你们的文章，想问一个问题。'),
    ("Hi, I'd like to talk about my marketing.", '你好，我想聊聊我的营销。'),
    ('Guides on AI and marketing', 'AI 与营销指南'), ('Insights: AI & marketing guides', '文章：AI 与营销指南'),
    ('TCM Insights', 'TCM 文章'),
]:
    T(en, zh)

# Titles in two parts: the second part takes the TCM accent colour (the flowing logo gradient).
H1_PARTS = {
    'chatgpt-vs-gemini-vs-claude': (T('ChatGPT vs Gemini vs Claude:', 'ChatGPT、Gemini 还是 Claude：'), T('which AI should your business use?', '你的生意该用哪个 AI？')),
    'what-is-aeo-geo': (T('What is AEO and GEO?', '什么是 AEO 和 GEO？'), T('How to get your business recommended by AI', '让 AI 推荐你的生意')),
    'kling-ai-veo-3-product-video': (T('Kling AI and Veo 3:', 'Kling AI 与 Veo 3：'), T('how to turn a product photo into a video ad', '把产品照片变成视频广告')),
    'index': (T('Insights on', 'AI 与营销，'), T('AI and marketing.', '讲清楚。')),
}
