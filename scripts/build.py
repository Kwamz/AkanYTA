#!/usr/bin/env python3
"""Generates the static prototype pages for Akan's YTA Program.

Run from the project root:  python3 scripts/build.py
Header, footer, nav and icons are defined once here so every page stays consistent.
Every unknown fact is a bracketed placeholder (see PLACEHOLDERS.md).
"""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- helpers
def ph(text):
    """Inline placeholder marker."""
    return f'<span class="ph">[{html.escape(text)}]</span>'

def ph_block(title, text=""):
    return f'<p class="ph-block"><strong>[{html.escape(title)}]</strong> {text}</p>'

ICONS = {  # Lucide-style line icons (24x24, stroke)
    "key": '<path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/>',
    "house": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
    "briefcase": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "cap": '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "buoy": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "menu": '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
}

def icon(name, cls=""):
    c = f"icon {cls}".strip()
    return f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'

HOME_PATHS = [
    ("Young people", "I&rsquo;m 15 to 22 and want support", "program.html", "See if the program is right for you"),
    ("Family and support people", "I&rsquo;m helping a young person", "contact.html", "Ask us a question"),
    ("Professionals", "I want to refer a young person", "referral.html", "Make a referral"),
    ("Partners, volunteers and donors", "I want to help", "get-involved.html", "Find a way to help"),
]

SERVICES = [
    ("life-skills", "key", "Independent living and life skills",
     "Learn the everyday skills that make living on your own feel doable, like cooking, cleaning, managing your time and looking after your health.",
     "Practical skills for running a home and a daily routine."),
    ("housing", "house", "Housing and accommodation",
     "Get help understanding your housing options, finding a place and knowing your rights as a tenant.",
     "Help to find and keep a safe place to live."),
    ("finances", "wallet", "Financial literacy and budgeting",
     "Build a budget, understand credit and banking, and plan for the costs of living on your own.",
     "Understand money and plan with confidence."),
    ("work-school", "briefcase", "Employment readiness and career development",
     "Work on your resume, practise interviews and explore career paths that fit your goals.",
     "Get ready for work and grow a career."),
    ("education", "cap", "Education planning",
     "Explore ways to finish school, upgrade or start training, and map out the steps to get there.",
     "Plan your next step in school or training."),
    ("community", "pin", "Access to community resources",
     "Find out about programs and services in Edmonton and get connected to the ones that fit what you need.",
     "Find services and supports near you."),
    ("relationships", "users", "Healthy relationships and support networks",
     "Build skills for healthy relationships and grow a circle of people you can count on.",
     "Grow your circle of support."),
    ("wellness", "buoy", "Mental health and addiction connections",
     "When you need more support, your youth worker can help you connect with mental health and addiction services.",
     "Be connected to care when you need it."),
]

NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("program.html", "The YTA Program"),
    ("services.html", "Our Services"),
    ("how-it-works.html", "How It Works"),
    ("resources.html", "Resources"),
    ("get-involved.html", "Get Involved"),
    ("contact.html", "Contact Us"),
]

SITE = "Akan's YTA Program"
TAGLINE = "Supporting Youth. Building Brighter Tomorrows."

# ---------------------------------------------------------------- layout
# Header navigation: five top-level items instead of eight. Groups are
# disclosure dropdowns (button + list of links). The logo links home.
NAV_TREE = [
    ("group", "About", [("about.html", "About Us"), ("program.html", "The YTA Program"),
                        ("services.html", "Our Services"), ("stories.html", "Stories")]),
    ("link", "how-it-works.html", "How It Works"),
    ("link", "resources.html", "Resources"),
    ("group", "Get Involved", [("get-involved.html", "Ways to get involved"), ("referral.html", "Make a referral"),
                               ("volunteer.html", "Volunteer"), ("donate.html", "Donate"),
                               ("events.html", "Events and updates")]),
    ("link", "contact.html", "Contact Us"),
]

def cur_attr(is_current):
    return ' aria-current="page"' if is_current else ""

def header(current):
    items = [f'<li class="nav-home"><a href="index.html"{cur_attr(current == "index.html")}>Home</a></li>']
    for n, entry in enumerate(NAV_TREE):
        if entry[0] == "link":
            _, href, label = entry
            items.append(f'<li><a href="{href}"{cur_attr(href == current)}>{label}</a></li>')
        else:
            _, label, kids = entry
            on = any(h == current for h, _ in kids)
            links = "".join(
                f'<li><a href="{h}"{cur_attr(h == current)}>{t}</a></li>' for h, t in kids)
            items.append(
                f'<li class="has-sub"><button type="button" class="nav-trigger{" is-current" if on else ""}" '
                f'aria-expanded="false" aria-controls="sub-{n}">{label}{icon("chevron", "icon--sm chev")}</button>'
                f'<ul class="subnav" id="sub-{n}">{links}</ul></li>')
    return f'''<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html"><img src="assets/yta-logo-horizontal.jpg" width="1000" height="398" alt="Akan's YTA Program, Edmonton, Alberta. Home"></a>
    <nav class="primary-nav" id="primary-nav" aria-label="Primary">
      <ul>{"".join(items)}</ul>
    </nav>
    <div class="header-actions">
      <button type="button" class="quick-exit" aria-label="Quick exit: leave this site now">Quick exit</button>
      <a class="btn btn--outline btn--donate" href="donate.html"{cur_attr(current == "donate.html")}>{icon("heart","icon--sm")}<span class="btn-label">Donate</span></a>
      <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="primary-nav">
        <span class="icon-open">{icon("menu")}</span><span class="icon-close">{icon("x")}</span>
        <span>Menu</span>
      </button>
    </div>
  </div>
</header>'''

FOOTER_LINKS = [
    ("about.html", "About Us"), ("program.html", "The YTA Program"), ("services.html", "Our Services"),
    ("how-it-works.html", "How It Works"), ("resources.html", "Resources"), ("referral.html", "Make a referral"),
    ("volunteer.html", "Volunteer"), ("donate.html", "Donate"),
]

def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOTER_LINKS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="logo-tile"><img src="assets/yta-logo-horizontal.jpg" width="1000" height="397" loading="lazy"
          alt="Akan's YTA Program, Edmonton, Alberta"></div>
        <p class="footer-tagline">{TAGLINE}</p>
      </div>
      <nav aria-label="Footer"><h2 class="visually-hidden">Explore</h2><ul class="footer-links">{links}</ul></nav>
      <div class="footer-contact"><h2>Contact</h2>
        <ul>
          <li>{ph("Program phone")}</li>
          <li>{ph("Program email")}</li>
          <li>{ph("Office address")}, Edmonton, Alberta</li>
        </ul>
        <h2 class="visually-hidden">Social media</h2>
        <ul class="social-list">
          <li>{ph("Instagram")}</li>
          <li>{ph("Facebook")}</li>
          <li>{ph("LinkedIn")}</li>
          <li>{ph("YouTube")}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>A program of {ph("Parent organization name")}</p>
      <ul class="footer-legal">
        <li><a href="privacy.html">Privacy policy</a></li>
        <li><a href="accessibility.html">Accessibility</a></li>
        <li>{ph("Safeguarding statement — pending")}</li>
        <li>&copy; <span id="year">2026</span></li>
      </ul>
    </div>
  </div>
</footer>'''

def cta_band(title="Ready to talk? Get in touch.", text="Reach out in whatever way feels easiest. We&rsquo;ll follow up to learn more."):
    return f'''<section class="cta-band" aria-labelledby="cta-title">
  <div class="container">
    <div><h2 id="cta-title">{title}</h2><p>{text}</p></div>
    <a class="btn btn--teal" href="contact.html">Contact us {icon("arrow","icon--sm")}</a>
  </div>
</section>'''

def page(filename, title, desc, body, extra_head="", robots=""):
    full_title = f"{title} | {SITE}" if filename != "index.html" else f"{SITE} | Youth Transitions to Adulthood in Edmonton"
    robots_tag = f'<meta name="robots" content="{robots}">' if robots else ""
    out = f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
{robots_tag}
<meta name="theme-color" content="#175451">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full_title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:image" content="assets/yta-logo.png">
<link rel="icon" href="assets/yta-logo.png" type="image/png">
<link rel="preload" href="assets/fonts/manrope-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
{extra_head}
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</body>
</html>
'''
    (ROOT / filename).write_text(out, encoding="utf-8")
    print("wrote", filename)

def page_hero(eyebrow, h1, lead=""):
    lead_html = f'<p class="hero__lead">{lead}</p>' if lead else ""
    return f'''<section class="hero hero--page on-dark">
  <div class="container"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1>{lead_html}</div>
</section>'''

def service_cards(link=True):
    cards = []
    for slug, ic, name, _, short in SERVICES:
        cards.append(f'''<li><a class="card card--link" href="services.html#{slug}">
  <span class="card__icon">{icon(ic)}</span><h3>{name}</h3><p>{short}</p></a></li>''')
    return '<ul class="grid grid--services" style="list-style:none;margin:0;padding:0">' + "".join(cards) + "</ul>"

# ---------------------------------------------------------------- pages
def home_extra():
    stats = "".join(f'''<li class="card stat-ph"><p class="big">{ph("Figure")}</p><p>{ph("What it measures — approved data only")}</p></li>''' for _ in range(3))
    return f'''<section class="section section--sage" aria-labelledby="impact-h">
  <div class="container">
    <div class="section__head"><p class="eyebrow">Community impact</p><h2 id="impact-h">The difference we make, together</h2>
      <p>Real numbers and stories will appear here once the program approves them.</p></div>
    <ul class="paths" style="margin-bottom:2rem">{stats}</ul>
    <div class="grid grid--2">
      <article class="card quote-card"><h3>Success stories</h3>
        <p>Stories from young people appear only with their documented consent.</p>
        <p><a class="link-arrow" href="stories.html">Read stories {icon("arrow","icon--sm")}</a></p></article>
      <article class="card"><h3>Events and community updates</h3>
        <p>See what&rsquo;s coming up and what&rsquo;s new in the program.</p>
        <p><a class="link-arrow" href="events.html">View events {icon("arrow","icon--sm")}</a></p></article>
    </div>
  </div>
</section>'''

def home():
    org_ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Akan's YTA Program","slogan":"Supporting Youth. Building Brighter Tomorrows.","areaServed":"Edmonton, Alberta, Canada","parentOrganization":{"@type":"Organization","name":"[Parent organization name]"},"url":"[Website URL]","email":"[Program email]","telephone":"[Program phone]"}
</script>'''
    body = f'''<section class="hero hero--photo on-dark">
  <img class="hero-bg" src="assets/images/hero-home.jpg" width="1920" height="1280" alt="" fetchpriority="high">
  <div class="container hero__grid">
    <div>
    <p class="eyebrow">Youth Transitions to Adulthood</p>
    <h1>Your future. Your journey. <span>Your possibilities.</span></h1>
    <p class="hero__lead">We&rsquo;re here to help you build the skills, confidence and support network for independent living.</p>
    <div class="hero__actions">
      <a class="btn btn--gold" href="program.html">Discover the YTA Program {icon("arrow","icon--sm")}</a>
      <a class="link-arrow" href="referral.html" style="color:#fff">Make a referral</a>
    </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="intro-title">
  <div class="container split">
    <div>
      <p class="eyebrow">About the program</p>
      <h2 id="intro-title">Support that starts with you</h2>
      <p>Akan&rsquo;s Youth Transitions to Adulthood (YTA) Program supports young people aged 15 to 22 as they move into independent adulthood. It&rsquo;s for youth who are leaving foster care or group care, or who are heading into adulthood without steady support from family.</p>
      <p>You work one-on-one with a youth worker. Together you set your own goals and take the next step at your pace.</p>
      <a class="link-arrow" href="program.html">Learn about the YTA Program {icon("arrow","icon--sm")}</a>
    </div>
    <div class="photo-ph" role="img" aria-label="Photo placeholder. Real photo needs consent before it is added.">[Photo — consent required]</div>
  </div>
</section>

<section class="section" aria-labelledby="paths-title" style="padding-top:0">
  <div class="container">
    <div class="section__head"><h2 id="paths-title">Where would you like to start?</h2></div>
    <ul class="paths">{"".join(f'<li><a class="card card--link" href="{h}"><h3>{t}</h3><p><strong>{q}</strong></p><p style="margin-top:.5rem">{go} &rarr;</p></a></li>' for t,q,h,go in HOME_PATHS)}</ul>
  </div>
</section>

<section class="section section--sage" aria-labelledby="services-title">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">What we offer</p>
      <h2 id="services-title">Support for the things that matter on your own</h2>
      <p>Eight areas of support, shaped around your goals.</p>
    </div>
    {service_cards()}
    <p style="margin-top:2rem"><a class="link-arrow" href="services.html">See all our services {icon("arrow","icon--sm")}</a></p>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">How it works</p>
      <h2 id="how-title">Getting started, step by step</h2>
    </div>
    <ol class="steps">
      <li><h3>Reach out</h3><p>Contact us yourself, or ask a worker you trust to reach out for you. {ph("Self-referral — pending confirmation")}</p></li>
      <li><h3>Have a first conversation</h3><p>We learn about you and what you want. {ph("Intake details — pending")}</p></li>
      <li><h3>Meet your youth worker</h3><p>You&rsquo;re matched with a youth worker who supports you one-on-one.</p></li>
      <li><h3>Set goals and get going</h3><p>Build a plan around your goals, and work on it together at your pace.</p></li>
    </ol>
    <p style="margin-top:2rem"><a class="link-arrow" href="how-it-works.html">More about how it works {icon("arrow","icon--sm")}</a></p>
  </div>
</section>

<section class="statement on-dark" aria-label="Our message">
  <div class="container"><p>Stronger. Brighter. Independent. <span>Together.</span></p></div>
</section>

<section class="section" aria-labelledby="community-title">
  <div class="container split split--flip">
    <div class="photo-ph" role="img" aria-label="Photo placeholder. Real photo needs consent before it is added.">[Photo — consent required]</div>
    <div>
      <p class="eyebrow">Community and partners</p>
      <h2 id="community-title">Stronger when we work together</h2>
      <p>Young people do best when the adults and organizations around them work as a team. We work with referral professionals and community partners across Edmonton to make sure youth get the right support.</p>
      <a class="link-arrow" href="get-involved.html">Get involved {icon("arrow","icon--sm")}</a>
    </div>
  </div>
</section>

{home_extra()}

{cta_band()}'''
    page("index.html", "Home",
         "Akan's YTA Program supports young people aged 15 to 22 in Edmonton as they move into independent adulthood.",
         body, extra_head=org_ld)

def about():
    body = page_hero("About us", "Supporting youth. Building brighter tomorrows.",
                     "A program for young people who are stepping into adulthood.") + f'''
<section class="section" id="mission" aria-labelledby="mission-title">
  <div class="container split">
    <div class="prose">
      <h2 id="mission-title">Our mission</h2>
      <p>{ph("Mission statement — pending approval")}</p>
      <p>Our work is youth-centred. That means you decide what matters, and your youth worker helps you get there. We build on your strengths, we listen first, and we stay with you as you grow.</p>
      <h2>Stronger. Brighter. Independent. Together.</h2>
      <p>These four words describe where we hope every young person ends up, and how we get there: side by side.</p>
    </div>
    <div class="logo-tile"><img src="assets/yta-logo.png" width="1254" height="1254"
      alt="Akan's YTA Program logo: four young people standing together under a roof, with the Edmonton skyline behind them. Tagline: Supporting Youth. Building Brighter Tomorrows."></div>
  </div>
</section>
<section class="section section--sage" id="parent-organization" aria-labelledby="parent-title">
  <div class="container prose">
    <h2 id="parent-title">Our parent organization</h2>
    <p>Akan&rsquo;s YTA Program is a program of {ph("Parent organization name")}.</p>
    {ph_block("Parent organization details — pending", "Description, website link and any approved wording about the parent organization go here once confirmed.")}
  </div>
</section>
{cta_band()}'''
    page("about.html", "About Us",
         "Learn about Akan's YTA Program in Edmonton: our youth-centred approach and the organization behind the program.", body)

def program():
    body = page_hero("The YTA Program", "A steady partner as you step into adulthood",
                     "One-on-one support from a youth worker who works with your goals.") + f'''
<section class="section" id="who-its-for" aria-labelledby="who-title">
  <div class="container grid grid--2" style="align-items:start">
    <div class="prose">
      <h2 id="who-title">Who it&rsquo;s for</h2>
      <p>The YTA Program is for young people aged <strong>15 to 22</strong> who are:</p>
      <ul class="checklist">
        <li>{icon("check")}<span>leaving foster care or group care, or</span></li>
        <li>{icon("check")}<span>heading into adulthood without steady support from family.</span></li>
      </ul>
      <p>Not sure if you fit? Reach out. We&rsquo;d rather talk it through with you.</p>
    </div>
    <div class="prose">
      <h2>What you can expect</h2>
      <ul class="checklist">
        <li>{icon("check")}<span>A youth worker who gets to know you and listens first.</span></li>
        <li>{icon("check")}<span>One-on-one support built around your own goals.</span></li>
        <li>{icon("check")}<span>Help with everyday things like housing, money, school and work.</span></li>
        <li>{icon("check")}<span>Connections to people and services in your community.</span></li>
      </ul>
    </div>
  </div>
</section>
<section class="section section--sage" id="eligibility" aria-labelledby="elig-title">
  <div class="container prose">
    <h2 id="elig-title">Eligibility</h2>
    <p>Participants are aged 15 to 22. Any further criteria are still being confirmed.</p>
    {ph_block("Eligibility criteria — pending approval", "Approved wording for youth and for referring professionals goes here. Do not add rules until the program confirms them.")}
    <p style="margin-top:1.5rem"><a class="btn btn--teal" href="how-it-works.html">See how it works</a></p>
  </div>
</section>
{cta_band()}'''
    page("program.html", "The YTA Program",
         "Akan's YTA Program offers one-on-one support to young people aged 15 to 22 who are leaving care or moving into adulthood without steady family support.", body)

def services():
    rows = []
    for slug, ic, name, long, _ in SERVICES:
        rows.append(f'''<section class="service-row" id="{slug}" aria-labelledby="{slug}-h">
  <span class="card__icon">{icon(ic)}</span>
  <div><h2 id="{slug}-h">{name}</h2><p>{long}</p>
  <p>{ph("Approved description, 2 to 3 sentences — pending")}</p></div>
</section>''')
    body = page_hero("Our services", "Support that fits your goals",
                     "Your youth worker helps you with the areas that matter most to you.") + f'''
<div class="section"><div class="container" style="max-width:56rem">{"".join(rows)}</div></div>
{cta_band()}'''
    page("services.html", "Our Services",
         "Eight areas of support: life skills, housing, money, work, education, community resources, relationships and connections to health services.", body)

def how():
    body = page_hero("How it works", "From first hello to your first goal") + f'''
<section class="section" id="what-to-expect" aria-labelledby="youth-title">
  <div class="container">
    <div class="section__head"><h2 id="youth-title">What to expect, if you&rsquo;re a young person</h2></div>
    <ol class="steps steps--stacked">
      <li><h3>You reach out</h3><p>Send us a message, or ask someone you trust to help. You don&rsquo;t need to have it all figured out.</p></li>
      <li><h3>We talk</h3><p>We chat about what you&rsquo;re looking for and answer your questions. {ph("Intake steps — pending")}</p></li>
      <li><h3>You meet your youth worker</h3><p>Your worker gets to know you and what matters to you.</p></li>
      <li><h3>You set goals together</h3><p>You pick what to work on first. It&rsquo;s your plan, at your pace.</p></li>
    </ol>
  </div>
</section>
<section class="section section--sage" id="referral" aria-labelledby="ref-title">
  <div class="container">
    <div class="section__head"><p class="eyebrow">For professionals</p><h2 id="ref-title">Referral process</h2>
      <p>For social workers, case managers and other referring professionals.</p></div>
    <ol class="steps steps--stacked">
      <li><h3>Check fit</h3><p>Review the <a href="program.html#eligibility">eligibility information</a>. {ph("Referral criteria — pending approval")}</p></li>
      <li><h3>Submit a referral or enquiry</h3><p><a href="referral.html">Use the online referral form</a>. {ph("Other referral methods (email, phone) — pending")}</p></li>
      <li><h3>We follow up</h3><p>{ph("Response timeline — pending")}</p></li>
      <li><h3>Youth and worker connect</h3><p>{ph("Transition and communication steps — pending")}</p></li>
    </ol>
  </div>
</section>
<section class="section" aria-labelledby="who-refers">
  <div class="container prose">
    <h2 id="who-refers">Self-referral or professional referral?</h2>
    {ph_block("Referral pathways — pending confirmation", "Whether young people can refer themselves, and whether guardian or agency consent is needed, has not been confirmed.")}
  </div>
</section>
{cta_band("Questions about getting started?", "Get in touch and we&rsquo;ll talk it through.")}'''
    page("how-it-works.html", "How It Works",
         "How to get started with Akan's YTA Program: what to expect for young people and how professionals can refer.", body)

def resources():
    cats = ["Housing", "Health and wellness", "Employment", "Education"]
    items = []
    for i, c in enumerate(cats, 1):
        items.append(f'''<li class="card resource-item" data-category="{c}">
  <span class="tag">{c}</span>
  <h3>{ph(f"Resource name {i}")}</h3>
  <p>{ph("Short description — to be verified")}</p>
  <dl><div class="meta"><dt>Website:</dt> <dd>{ph("URL")}</dd></div>
  <div class="meta"><dt>Phone:</dt> <dd>{ph("Phone, optional")}</dd></div></dl>
</li>''')
    chips = '<button type="button" class="chip" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="chip" data-filter="{c}" aria-pressed="false">{c}</button>' for c in cats)
    body = page_hero("Resources", "Find help in your community",
                     "A directory of services and supports in Edmonton.") + f'''
<section class="section" id="helplines" aria-labelledby="crisis-title">
  <div class="container">
    <div class="crisis">
      <h2 id="crisis-title">Need help right now?</h2>
      <p>If you or someone else is in immediate danger, call <strong>911</strong>.</p>
      {ph_block("Crisis and helpline numbers — staff must verify before launch", "Add each service name, phone number, hours and website only after the program has confirmed them.")}
    </div>
  </div>
</section>
<section class="section section--sage" id="directory" aria-labelledby="dir-title">
  <div class="container">
    <div class="section__head"><h2 id="dir-title">Community resource directory</h2>
      <p>Filter by category. The live site will manage this list in the CMS.</p></div>
    <fieldset class="filter-bar" data-filter-bar><legend>Filter by category</legend>{chips}</fieldset>
    <p id="filter-status" class="visually-hidden" role="status" aria-live="polite"></p>
    <ul class="resource-list">{"".join(items)}</ul>
  </div>
</section>
{cta_band("Can&rsquo;t find what you need?", "Tell us what you&rsquo;re looking for and we&rsquo;ll help point you in the right direction.")}'''
    page("resources.html", "Resources",
         "A community resource directory and crisis supports for young people in Edmonton.", body)

def involved():
    body = page_hero("Get involved", "Better together",
                     "Partners and referral professionals help young people get the support they need.") + f'''
<section class="section">
  <div class="container grid grid--2">
    <article class="card" id="partners" aria-labelledby="partners-h">
      <h2 id="partners-h" style="font-size:1.6rem">Community partners</h2>
      <p>Your organization and ours can complement each other. We&rsquo;d like to hear how we might work together.</p>
      <p>Collaborate with us to create meaningful opportunities, share resources and build stronger support networks.</p>
      <a class="btn btn--teal" href="contact.html" style="margin-top:1rem">Connect to partner</a>
    </article>
    <article class="card" id="referrers" aria-labelledby="referral-h">
      <h2 id="referral-h" style="font-size:1.6rem">Referral partners</h2>
      <p>Social workers, case managers and other professionals can refer a young person or ask questions about fit.</p>
      <p><a href="how-it-works.html#referral">See the referral process</a></p>
      <a class="btn btn--teal" href="referral.html" style="margin-top:1rem">Make a referral</a>
    </article>
  </div>
</section>
<section class="section section--sage" aria-labelledby="more-h">
  <div class="container">
    <div class="section__head"><h2 id="more-h">More ways to take part</h2></div>
    <ul class="grid grid--3" style="list-style:none;margin:0;padding:0">
      <li><a class="card card--link" href="volunteer.html"><h3>Volunteer</h3><p>Share your time and skills.</p></a></li>
      <li><a class="card card--link" href="donate.html"><h3>Donate</h3><p>Support young people in Edmonton.</p></a></li>
      <li><a class="card card--link" href="events.html"><h3>Events and updates</h3><p>See what&rsquo;s coming up.</p></a></li>
    </ul>
  </div>
</section>
{cta_band("Have a question or an idea?", "Send us an enquiry. We&rsquo;ll get back to you.")}'''
    page("get-involved.html", "Get Involved",
         "Partner with Akan's YTA Program or make a referral for a young person aged 15 to 22 in Edmonton.", body)

def contact():
    body = page_hero("Contact us", "Ready to talk? Get in touch.",
                     "Tell us a little about yourself and how we can help.") + f'''
<section class="section">
  <div class="container grid grid--2" style="align-items:start;gap:3rem">
    <div>
      <div id="enquiry" class="notice" style="margin-bottom:2rem">{icon("shield")}
        <p><strong>Please don&rsquo;t include private details</strong> like health information or case numbers. We&rsquo;ll follow up to learn more.</p></div>
      <form id="enquiry-form" class="form" data-validate novalidate method="post" action="#" aria-describedby="form-status">
        <div class="field" data-field="name" data-rule="text" data-invalid="false">
          <label for="f-name">Name or preferred name</label>
          <input type="text" id="f-name" name="name" autocomplete="name" required aria-describedby="e-name">
          <p class="error-msg" id="e-name">Please enter a name. A first name or nickname is fine.</p>
        </div>
        <div class="field" data-field="contact" data-rule="contact" data-invalid="false">
          <label for="f-contact">Email or phone</label>
          <p class="hint" id="h-contact">How should we reach you?</p>
          <input type="text" id="f-contact" name="contact" autocomplete="email" required aria-describedby="h-contact e-contact">
          <p class="error-msg" id="e-contact">Please enter a valid email address or a phone number.</p>
        </div>
        <div class="field" data-field="role" data-rule="radio" data-invalid="false">
          <fieldset style="border:0;padding:0;margin:0" aria-describedby="e-role">
            <legend>I am a&hellip;</legend>
            <div class="radio-row">
              <label><input type="radio" name="role" value="youth"> Young person</label>
              <label><input type="radio" name="role" value="family"> Family member or support person</label>
              <label><input type="radio" name="role" value="professional"> Professional</label>
              <label><input type="radio" name="role" value="organization"> Organization</label>
              <label><input type="radio" name="role" value="other"> Other</label>
            </div>
          </fieldset>
          <p class="error-msg" id="e-role">Please choose one.</p>
        </div>
        <div class="field" data-field="message" data-rule="long" data-invalid="false">
          <label for="f-message">Message</label>
          <textarea id="f-message" name="message" required aria-describedby="e-message"></textarea>
          <p class="error-msg" id="e-message">Please write a short message.</p>
        </div>
        <div class="honeypot" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="field check" data-field="consent" data-rule="checkbox" data-invalid="false">
          <label for="f-consent"><input type="checkbox" id="f-consent" name="consent" required aria-describedby="e-consent">
            <span>I agree to the program contacting me about this message. See the <a href="privacy.html">privacy policy</a>.</span></label>
          <p class="error-msg" id="e-consent">Please tick the box so we know it&rsquo;s okay to contact you.</p>
        </div>
        <div><button type="submit" class="btn btn--gold">Send message</button></div>
        <div id="form-status" class="form-status" role="status" aria-live="polite"></div>
      </form>
    </div>
    <aside id="location" aria-labelledby="details-h" class="card" style="scroll-margin-top:100px">
      <h2 id="details-h" style="font-size:1.4rem">Contact details</h2>
      <ul class="contact-list">
        <li>{icon("phone")}<span>{ph("Program phone")}</span></li>
        <li>{icon("mail")}<span>{ph("Program email")}</span></li>
        <li>{icon("pin")}<span>{ph("Office address")}<br>Edmonton, Alberta</span></li>
        <li><span></span><span>{ph("Office hours")}</span></li>
      </ul>
    </aside>
  </div>
</section>'''
    page("contact.html", "Contact Us",
         "Contact Akan's YTA Program in Edmonton with a question, enquiry or referral.", body)

def donate():
    benefits = [
        "Greater confidence and independence.",
        "Essential budgeting and financial management skills.",
        "Housing stability and independent living.",
        "Education and employment opportunities.",
        "Healthy relationships and supportive networks.",
        "Connections to important community resources.",
    ]
    benefit_items = "".join(f'<li>{icon("check")}<span>{t}</span></li>' for t in benefits)
    journey = [
        ("Support the Program", "Help strengthen opportunities and resources that contribute to youth development and independence.", "#contribute", "Ask about giving"),
        ("Become a Community Partner", "Collaborate with us to create meaningful opportunities, share resources and build stronger support networks.", "get-involved.html#partners", "Partner with us"),
        ("Volunteer Your Time", "Share your experience, skills and time to contribute positively to the community.", "volunteer.html", "Volunteer"),
    ]
    journey_cards = "".join(
        f'''<li class="card"><h3>{t}</h3><p>{d}</p><p style="margin:1rem 0 0"><a class="link-arrow" href="{h}">{g} {icon("arrow","icon--sm")}</a></p></li>'''
        for t, d, h, g in journey)
    stats = "".join(f'''<li class="card stat-ph"><p class="big">{ph("Figure")}</p><p>{ph("What it measures, approved data only")}</p></li>''' for _ in range(4))
    give_amounts = "".join(f'<button type="button" class="give-btn" data-amount="{a}" aria-pressed="{"true" if a == 50 else "false"}">${a}</button>' for a in (50, 75, 150, 200))
    give_areas = "".join(f'<label><input type="radio" name="area" value="{n}"> {n}</label>' for _, _, n, _, _ in SERVICES)
    body = f"""<section class="hero hero--page on-dark">
  <div class="container hero__grid">
    <div>
      <p class="eyebrow">Donate</p>
      <h1>Make a Difference. Build Brighter Futures.</h1>
      <p class="hero__lead">Every young person deserves the opportunity to build a stable, confident and independent future.</p>
      <div class="hero__actions" style="margin-top:1.75rem">
        <a class="btn btn--gold" href="contact.html">Contact us {icon("arrow","icon--sm")}</a>
        <a class="link-arrow" href="program.html" style="color:#fff">Explore our programs</a>
      </div>
    </div>
    <div class="hero__art"><img class="hero-photo" src="assets/images/hero-donate.jpg" width="900" height="599" fetchpriority="high" alt="A man with long locs, wearing a blue shirt and tie, leans in to read a notebook with a teenager in a maroon jersey at a classroom table."></div>
  </div>
</section>

<section class="section" aria-labelledby="intro-title">
  <div class="container prose">
    <h2 id="intro-title" class="visually-hidden">About supporting the program</h2>
    <p style="font-size:1.2rem">At Akan&rsquo;s Youth Transitions to Adulthood (YTA) Program, we believe that the right support, guidance and opportunities can make a lasting difference in a young person&rsquo;s life.</p>
    <p>Your interest in supporting our work helps strengthen a community where young people are encouraged to discover their potential, develop essential life skills and take meaningful steps toward independence.</p>
    <nav class="notice" aria-label="On this page" style="margin-top:2rem">{icon("arrow")}
      <p><strong>On this page:</strong> <a href="#why">Why your support matters</a> &middot; <a href="#journey">Be part of their journey</a> &middot; <a href="#contribute">Making a contribution</a> &middot; <a href="#questions">Questions</a></p></nav>
  </div>
</section>

<section class="section section--sage" id="why" style="scroll-margin-top:90px" aria-labelledby="why-title">
  <div class="container split" style="align-items:start">
    <div>
      <h2 id="why-title">Why Your Support Matters</h2>
      <p>Transitioning into adulthood can bring challenges, particularly for young people without consistent family support.</p>
      <p>Through individualized guidance and practical support, Akan&rsquo;s YTA helps young people work toward:</p>
      <ul class="checklist">{benefit_items}</ul>
    </div>
    <div class="photo-ph" role="img" aria-label="Photo placeholder. Real photo needs consent before it is added.">[Photo — consent required]</div>
  </div>
</section>

<section class="section" id="journey" style="scroll-margin-top:90px" aria-labelledby="journey-title">
  <div class="container">
    <div class="section__head"><h2 id="journey-title">Be Part of Their Journey</h2>
      <p>There are different ways to support young people as they work toward brighter futures.</p></div>
    <ul class="grid grid--3" style="list-style:none;margin:0;padding:0">{journey_cards}</ul>
  </div>
</section>

<section class="section section--sage" id="contribute" style="scroll-margin-top:90px" aria-labelledby="contribute-title">
  <div class="container split" style="align-items:start">
    <div>
      <h2 id="contribute-title">Interested in Making a Contribution?</h2>
      <p>We welcome conversations with individuals, businesses and community organizations interested in supporting Akan&rsquo;s YTA Program.</p>
      <p><strong>Our donation arrangements are currently being finalized.</strong> Please contact the program to discuss approved ways to contribute.</p>
      <p style="margin-top:1.5rem"><a class="btn btn--teal" href="contact.html">Contact us {icon("arrow","icon--sm")}</a></p>
    </div>
    <div class="card give-card" id="give">
      {ph_block("Preview of the future giving form", "Online giving is not available yet. Nothing here is charged or sent. The payment processor, amounts and receipt wording are still to be confirmed.")}
      <form id="give-form" novalidate style="margin-top:1.5rem">
        <div class="give-toggle" role="group" aria-label="Gift frequency">
          <button type="button" class="give-btn give-btn--freq" data-freq="once" aria-pressed="true">Give once</button>
          <button type="button" class="give-btn give-btn--freq" data-freq="monthly" aria-pressed="false">Monthly</button>
        </div>
        <p class="give-label" id="amt-label">Select or enter gift amount:</p>
        <div class="give-amounts" role="group" aria-labelledby="amt-label">{give_amounts}</div>
        <div class="give-other"><span aria-hidden="true">$</span><label for="g-other" class="visually-hidden">Other amount in dollars</label>
          <input type="text" id="g-other" inputmode="decimal" placeholder="Other amount" autocomplete="off" aria-describedby="g-err"></div>
        <p class="give-err" id="g-err" role="alert" hidden>Please choose or enter an amount greater than $0.</p>
        <h3 class="give-h">How your donation makes an impact</h3>
        <p>Your gift supports one-on-one, youth-centred help for young people aged 15 to 22 as they move into independent adulthood.</p>
        <div class="check give-focus"><label for="g-focus"><input type="checkbox" id="g-focus"><span>I wish to focus my gift toward a specific area of support.</span></label></div>
        <fieldset class="give-areas" id="g-areas" hidden><legend>Choose an area</legend>{give_areas}</fieldset>
        <div class="give-next"><button type="submit" class="btn btn--teal">Next {icon("arrow","icon--sm")}</button></div>
        <div class="form-status" role="status" aria-live="polite" id="give-status"></div>
      </form>
      <p style="margin:1.25rem 0 0;font-size:.95rem;color:var(--color-muted)">{ph("Receipt and registration wording, parent organization to supply")}</p>
    </div>
  </div>
</section>

<section class="section" id="questions" aria-labelledby="q-title">
  <div class="container">
    <div class="section__head" style="text-align:center;margin-inline:auto"><h2 id="q-title">Have questions? We&rsquo;re here to help</h2></div>
    <ul class="grid grid--2" style="list-style:none;margin:0 auto;padding:0;max-width:44rem">
      <li class="card" style="display:grid;grid-template-columns:auto auto;gap:1rem;align-items:center;justify-content:center"><span class="card__icon" style="margin:0">{icon("phone")}</span><span>{ph("Program phone")}</span></li>
      <li class="card" style="display:grid;grid-template-columns:auto auto;gap:1rem;align-items:center;justify-content:center"><span class="card__icon" style="margin:0">{icon("mail")}</span><span>{ph("Donations email")}</span></li>
    </ul>
  </div>
</section>

<section class="section section--sage" id="campaign" aria-labelledby="camp-title">
  <div class="container split split--flip">
    <div class="photo-ph" role="img" aria-label="Photo placeholder. Real photo needs consent before it is added.">[Photo — consent required]</div>
    <div>
      <p class="eyebrow">Featured campaign</p>
      <h2 id="camp-title">{ph("Campaign title")}</h2>
      <p>{ph("Short campaign description. Approved wording only, no invented stories")}</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="numbers-title">
  <div class="container">
    <div class="section__head"><p class="eyebrow">By the numbers</p><h2 id="numbers-title">Your donation at work in {ph("Year")}</h2>
      <p>No figures are shown yet. Add statistics only once the program supplies and approves them.</p></div>
    <ul class="grid" style="list-style:none;margin:0;padding:0;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">{stats}</ul>
    <p style="margin-top:2.5rem;font-size:.95rem">{ph("Charitable status and registration wording, parent organization to supply. Do not describe the program as its own registered charity")}</p>
  </div>
</section>

<section class="cta-band" aria-labelledby="cta-title">
  <div class="container">
    <div>
      <h2 id="cta-title">Together, We Can Build Brighter Tomorrows.</h2>
      <p>A little support can create opportunities for lasting change. Join us in helping young people move forward with confidence, purpose and independence.</p>
      <p style="margin-top:1rem"><strong>Akan&rsquo;s YTA Program</strong><br><em>Supporting Youth. Building Brighter Tomorrows.</em></p>
    </div>
    <div class="hero__actions">
      <a class="btn btn--teal" href="contact.html">Contact us {icon("arrow","icon--sm")}</a>
      <a class="btn btn--outline" href="program.html">Explore our programs</a>
    </div>
  </div>
</section>"""
    page("donate.html", "Donate",
         "Support young people aged 15 to 22 in Edmonton as they move into independent adulthood with Akan's YTA Program.", body)

def field(key, rule, label, input_html, hint="", err="Please complete this field."):
    h = f'<p class="hint" id="h-{key}">{hint}</p>' if hint else ""
    e = f'<p class="error-msg" id="e-{key}">{err}</p>'
    rule_attr = f' data-rule="{rule}"' if rule else ""
    return f'<div class="field" data-field="{key}"{rule_attr} data-invalid="false"><label for="r-{key}">{label}</label>{h}{input_html}{e}</div>'

def referral():
    f = [
        field("name", "text", "Your name", '<input type="text" id="r-name" name="name" autocomplete="name" required aria-describedby="e-name">', err="Please enter your name."),
        field("org", "", "Organization and role (optional)", '<input type="text" id="r-org" name="org" autocomplete="organization-title">'),
        field("contact", "contact", "Your email or phone", '<input type="text" id="r-contact" name="contact" required aria-describedby="e-contact">', err="Please enter a valid email address or phone number."),
        f'''<div class="field" data-field="role" data-rule="radio" data-invalid="false"><fieldset style="border:0;padding:0;margin:0"><legend>I am referring as a&hellip;</legend><div class="radio-row">
          <label><input type="radio" name="role" value="professional"> Professional (social worker, case manager, other)</label>
          <label><input type="radio" name="role" value="family"> Family member or support person</label>
          <label><input type="radio" name="role" value="other"> Other</label></div></fieldset><p class="error-msg">Please choose one.</p></div>''',
        field("yp", "", "Young person&rsquo;s first name or initials (optional)", '<input type="text" id="r-yp" name="yp" aria-describedby="h-yp">', hint="Use as little identifying information as you can."),
        field("age", "", "Young person&rsquo;s age (optional)", '<select id="r-age" name="age"><option value="">Choose&hellip;</option>' + "".join(f"<option>{a}</option>" for a in range(15, 23)) + '<option>Under 15</option><option>Over 22</option><option>Not sure</option></select>'),
        f'''<div class="field" data-field="aware" data-rule="radio" data-invalid="false"><fieldset style="border:0;padding:0;margin:0"><legend>Does the young person know about this referral?</legend><div class="radio-row">
          <label><input type="radio" name="aware" value="yes"> Yes</label>
          <label><input type="radio" name="aware" value="no"> No</label>
          <label><input type="radio" name="aware" value="unsure"> Not sure</label></div></fieldset><p class="error-msg">Please choose one.</p></div>''',
        field("message", "long", "How can we help?", '<textarea id="r-message" name="message" required aria-describedby="h-message e-message"></textarea>', hint="A few sentences is plenty. We&rsquo;ll follow up to learn more.", err="Please write a short message."),
    ]
    body = page_hero("Make a referral", "Refer a young person",
                     "For social workers, case managers, family members and others who support a young person aged 15 to 22.") + f"""
<section class="section">
  <div class="container grid grid--2" style="align-items:start;gap:3rem">
    <div>
      <div class="notice" style="margin-bottom:2rem">{icon("shield")}
        <p><strong>Please don&rsquo;t include private details</strong> like health information or case numbers. We&rsquo;ll follow up to learn more.</p></div>
      <form id="referral-form" class="form" data-validate novalidate method="post" action="#" aria-describedby="form-status">
        {"".join(f)}
        <div class="honeypot" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="field check" data-field="consent" data-rule="checkbox" data-invalid="false">
          <label for="r-consent"><input type="checkbox" id="r-consent" name="consent" required>
            <span>I&rsquo;m allowed to share this information, and I agree to the program contacting me. See the <a href="privacy.html">privacy policy</a>.</span></label>
          <p class="error-msg">Please tick the box to continue.</p></div>
        <div><button type="submit" class="btn btn--gold">Send referral</button></div>
        <div class="form-status" role="status" aria-live="polite" id="form-status"></div>
      </form>
    </div>
    <aside class="card" aria-labelledby="before-h">
      <h2 id="before-h" style="font-size:1.4rem">Before you refer</h2>
      <ul class="checklist">
        <li>{icon("check")}<span>The program supports young people aged 15 to 22.</span></li>
        <li>{icon("check")}<span>See the <a href="program.html#eligibility">eligibility information</a>.</span></li>
      </ul>
      <p>{ph("Consent requirements for youth, guardians and agencies — pending")}</p>
      <p>{ph("What happens after you refer, and the response time — pending")}</p>
      <p>Prefer to talk first? <a href="contact.html">Contact us</a>.</p>
    </aside>
  </div>
</section>"""
    page("referral.html", "Make a Referral",
         "Refer a young person aged 15 to 22 to Akan's YTA Program in Edmonton.", body)

def events():
    updates = "".join(f'''<li class="card"><p class="tag-date">{ph("Date")}</p><h3>{ph("Update headline")}</h3><p>{ph("Short summary — to be written and approved")}</p></li>''' for _ in range(3))
    body = page_hero("Events and updates", "What&rsquo;s on and what&rsquo;s new",
                     "Program events, community happenings and news.") + f"""
<section class="section" aria-labelledby="cal-title">
  <div class="container">
    <div class="cal-wrap">
      <div class="cal-head">
        <button type="button" class="cal-btn" id="cal-prev" aria-label="Previous month">&larr;</button>
        <h2 id="cal-title" aria-live="polite">Calendar</h2>
        <button type="button" class="cal-btn" id="cal-next" aria-label="Next month">&rarr;</button>
      </div>
      <table id="calendar"><caption class="visually-hidden">Event calendar</caption>
        <thead><tr><th scope="col" abbr="Sunday">Sun</th><th scope="col" abbr="Monday">Mon</th><th scope="col" abbr="Tuesday">Tue</th><th scope="col" abbr="Wednesday">Wed</th><th scope="col" abbr="Thursday">Thu</th><th scope="col" abbr="Friday">Fri</th><th scope="col" abbr="Saturday">Sat</th></tr></thead>
        <tbody></tbody></table>
    </div>
    <noscript><p class="ph-block">The calendar needs JavaScript. Upcoming events are listed below.</p></noscript>
  </div>
</section>
<section class="section section--sage" aria-labelledby="up-title">
  <div class="container">
    <div class="section__head"><h2 id="up-title">Upcoming events</h2></div>
    <ul class="grid grid--3" id="event-list" style="list-style:none;margin:0;padding:0">
      <li>{ph_block("No events listed yet", "Events appear here and on the calendar once staff add them. Nothing is scheduled in this prototype.")}</li>
    </ul>
  </div>
</section>
<section class="section" aria-labelledby="news-title">
  <div class="container">
    <div class="section__head"><h2 id="news-title">Community updates</h2>
      <p>Approved news and announcements from the program.</p></div>
    <ul class="grid grid--3" style="list-style:none;margin:0;padding:0">{updates}</ul>
  </div>
</section>
{cta_band("Have an event or news to share?", "Partners are welcome to get in touch.")}
<script>window.YTA_EVENTS = [];</script>"""
    page("events.html", "Events and Updates",
         "Events, community news and updates from Akan's YTA Program in Edmonton.", body)

def volunteer():
    roles = "".join(f'''<li class="card"><h3>{ph(f"Volunteer role {i}")}</h3><p>{ph("Description, time commitment — pending")}</p></li>''' for i in (1, 2, 3))
    body = page_hero("Volunteer", "Share your time and skills",
                     "Volunteers help young people feel connected and supported.") + f"""
<section class="section" aria-labelledby="why-v">
  <div class="container prose">
    <h2 id="why-v">Why volunteer?</h2>
    <p>Share your experience, skills and time to contribute positively to the community.</p>
    <h2>What volunteers do</h2>
  </div>
  <div class="container"><ul class="grid grid--3" style="list-style:none;margin:0;padding:0">{roles}</ul></div>
</section>
<section class="section section--sage" aria-labelledby="req-v">
  <div class="container prose">
    <h2 id="req-v">What we ask of volunteers</h2>
    {ph_block("Screening, training and age requirements — pending", "Because the program works with young people, confirm the parent organization&rsquo;s screening and safeguarding rules before listing any requirements.")}
    <p style="margin-top:1.5rem"><a class="btn btn--teal" href="contact.html">Tell us you&rsquo;re interested</a></p>
  </div>
</section>
<section class="section" aria-labelledby="give-v">
  <div class="container grid grid--2" style="align-items:start">
    <div class="prose"><h2 id="give-v">Prefer to give?</h2>
      <p>Donations help support young people in the program.</p>
      <p><a class="btn btn--gold" href="donate.html">Donation information</a></p></div>
    <div class="prose"><h2>Other ways to help</h2>
      <p>Partner with us, share an event, or make a connection for a young person.</p>
      <p><a class="link-arrow" href="get-involved.html">See all the ways to get involved {icon("arrow","icon--sm")}</a></p></div>
  </div>
</section>
{cta_band("Interested in volunteering?", "Send us a message and we&rsquo;ll be in touch.")}"""
    page("volunteer.html", "Volunteer",
         "Volunteer with Akan's YTA Program in Edmonton and help young people step into adulthood.", body)

def stories():
    cards = "".join(f'''<li class="card quote-card"><blockquote>{ph("Quote — documented consent required")}</blockquote><p>{ph("Name or first name only, role, and year, as the person agreed")}</p></li>''' for _ in range(3))
    body = page_hero("Stories", "In their words",
                     "Stories from young people, families and partners, shared with their permission.") + f"""
<section class="section" aria-labelledby="consent-h">
  <div class="container prose">
    <div class="notice">{icon("shield")}<div><h2 id="consent-h" style="font-size:1.3rem;margin-bottom:.4rem">How we share stories</h2>
      <p>We only share a story, quote or photo with clear, written consent. For young people under 18 that includes a guardian or agency. People can choose to use a different name, or to stay anonymous, and can ask us to remove their story at any time.</p></div></div>
    <p style="margin-top:1rem">{ph("Consent process and withdrawal wording — parent organization to approve")}</p>
  </div>
</section>
<section class="section section--sage" aria-labelledby="stories-h">
  <div class="container">
    <div class="section__head"><h2 id="stories-h">Stories and testimonials</h2>
      <p>No stories are shown yet. Nothing here may be written, adapted or invented without a real person&rsquo;s consent.</p></div>
    <ul class="grid grid--3" style="list-style:none;margin:0;padding:0">{cards}</ul>
  </div>
</section>
<section class="section" aria-labelledby="share-h">
  <div class="container prose">
    <h2 id="share-h">Would you like to share your story?</h2>
    <p>It&rsquo;s always your choice. If you&rsquo;re a past or current participant, a family member or a partner, you can <a href="contact.html">get in touch</a> and we&rsquo;ll talk about it, with no pressure.</p>
  </div>
</section>
{cta_band()}"""
    page("stories.html", "Stories",
         "Success stories and testimonials from young people, families and partners, shared with consent.", body)

def privacy():
    body = page_hero("Privacy policy", "Your privacy matters") + f'''
<section class="section"><div class="container prose">
  <h2>What this site collects</h2>
  <p>This site collects only what you choose to send through the contact form: a name or preferred name, an email or phone number, who you are, and your message. We use it to reply to you.</p>
  <p>The site does not set tracking cookies or load social media embeds. {ph("Analytics approach — pending; must load only after consent")}</p>
  {ph_block("Approved privacy policy — to be supplied by the parent organization", "Replace this page with the parent organization&rsquo;s approved policy, including how long messages are kept and who to contact about your information.")}
  {ph_block("Safeguarding statement — pending approval")}
</div></section>'''
    page("privacy.html", "Privacy Policy",
         "How Akan's YTA Program handles information shared through this website.", body)

def access():
    body = page_hero("Accessibility statement", "A website everyone can use") + f'''
<section class="section"><div class="container prose">
  <h2>Our goal</h2>
  <p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.2, level AA. That includes keyboard navigation, readable colour contrast, clear headings, and support for screen readers and zoom.</p>
  <h2>Status</h2>
  <p>This site is still being built. Accessibility testing has not been completed. {ph("Test results and date — to add after audit")}</p>
  <h2>Tell us about a barrier</h2>
  <p>If something on this site is hard to use, please <a href="contact.html">contact us</a> and we&rsquo;ll work to fix it. You can also reach us at {ph("Program email")}.</p>
</div></section>'''
    page("accessibility.html", "Accessibility Statement",
         "Our commitment to an accessible website for young people, professionals and partners.", body)

def not_found():
    body = f'''<section class="section not-found"><div class="container">
  <p class="eyebrow" style="justify-content:center">Error 404</p>
  <h1>We can&rsquo;t find that page</h1>
  <p>It may have moved, or the link might be wrong. Here are some good places to start.</p>
  <div class="hero__actions" style="margin-top:1.5rem">
    <a class="btn btn--gold" href="index.html">Go to the home page</a>
    <a class="btn btn--outline" href="contact.html">Contact us</a>
  </div>
</div></section>'''
    page("404.html", "Page not found", "This page could not be found.", body, robots="noindex")

if __name__ == "__main__":
    for fn in (home, about, program, services, how, resources, involved, contact, donate, referral, events, volunteer, stories, privacy, access, not_found):
        fn()
