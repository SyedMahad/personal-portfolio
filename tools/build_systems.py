#!/usr/bin/env python3
"""Build the /systems case-study pages, the /fixes write-ups, and their homepage cards.

Edit a page body in content/<section>/<slug>.html, or its card/summary details
in PAGES / FIXES below, then run:

    python3 tools/build_systems.py

It writes <section>/<slug>/index.html for every entry and refreshes the cards
between the <!-- <section>:cards:start/end --> markers in index.html. Commit the output.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://mahadehsan.com"

# Order = importance (most to least), used on the homepage and for prev/next links.
PAGES = [
    {
        "slug": "rag",
        "title": "Enterprise RAG knowledge platform",
        "signal": "Enterprise RAG",
        "company": "Diya Interactive",
        "role": "Team & Tech Lead",
        "years": "2023–now",
        "team": "4 engineers · 2 backend · 1 frontend · 1 mobile",
        "summary": "Conversational search over thousands of pages of OEM manuals, with page-level "
                   "citations and per-unit data isolation.",
        "metrics": ["91 endpoints", "~680 tests", "3,800+ chunks"],
        "chips": ["FastAPI", "ASP.NET Core", "PostgreSQL", "pgvector", "Microsoft Foundry",
                  "Docling", "SSE", "Azure"],
        "description": "Case study: a multi-tenant RAG platform with agentic hybrid retrieval, "
                       "page-level citations and SSE streaming, led by Syed Mahad Ehsan.",
    },
    {
        "slug": "workforce",
        "title": "Security workforce management SaaS",
        "signal": "Real-time ops",
        "company": "Diya Interactive",
        "role": "Team Lead & co-Tech Lead",
        "years": "2023–now",
        "team": "8 engineers · 3 backend · 3 frontend · 1 mobile · 1 QA",
        "summary": "Scheduling, attendance and compliance for security officers, live across web "
                   "and mobile.",
        "metrics": ["11 Django apps", "1,200+ tests", "~9s → 0.06s"],
        "chips": ["Django", "DRF", "Celery", "Redis", "MySQL", "SSE", "Firebase",
                  "AWS Elastic Beanstalk"],
        "description": "Case study: a multi-company workforce SaaS on Django, Celery and Redis: "
                       "realtime SSE, a production memory-leak fix and bulk scheduling cut from ~9s to 0.06s.",
    },
    {
        "slug": "django-scaling",
        "title": "Scaling a Django platform past 10k users",
        "signal": "10,000+ users",
        "company": "KNYSYS, LLC",
        "role": "Assoc. Software Developer",
        "years": "2021–2023",
        "team": None,
        "summary": "Re-architected a Django app onto Docker and Azure VMSS as it grew past 10k "
                   "users.",
        "metrics": ["10k+ users", "Azure VMSS", "demand-based scaling"],
        "chips": ["Django", "Docker", "Azure VMSS", "MySQL", "MongoDB", "Memcache"],
        "description": "Case study: re-architecting a Django platform onto Docker and Azure VMSS "
                       "to scale past 10,000 users.",
    },
    {
        "slug": "counselling",
        "title": "Online counselling platform",
        "signal": "Stack modernisation",
        "company": "Diya Interactive",
        "role": "Backend Software Engineer",
        "years": "2023–now",
        "team": None,
        "summary": "Rebuilt chat as a versioned REST API and upgraded Django 2.2 → 4.2, with CI "
                   "on every push.",
        "metrics": ["Django 2.2 → 4.2", "v2 chat API", "CI on every push"],
        "chips": ["Django", "DRF", "MySQL", "Vonage OpenTok", "SimpleJWT", "GitHub Actions"],
        "description": "Case study: rebuilding a counselling platform's chat as a versioned REST "
                       "API and upgrading Django 2.2 to 4.2 with CI.",
    },
    {
        "slug": "ai-commentary",
        "title": "AI sports commentary POC",
        "signal": "Multimodal AI",
        "company": "Diya Interactive",
        "role": "Senior Software Engineer",
        "years": "2023–now",
        "team": None,
        "summary": "Took a mock to a working video → commentary pipeline with burned-in "
                   "subtitles.",
        "metrics": ["Gemini Flash / Pro", "FFmpeg", "~2.5 weeks"],
        "chips": ["FastAPI", "Gemini", "FFmpeg", "React"],
        "description": "Case study: a FastAPI + Gemini multimodal pipeline that turns sports clips "
                       "into styled commentary with burned-in subtitles.",
    },
    {
        "slug": "open-edx",
        "title": "Open edX as a multi-tenant SaaS",
        "signal": "Multi-tenant",
        "company": "KNYSYS, LLC",
        "role": "Software Developer",
        "years": "2021–2023",
        "team": None,
        "summary": "Turned Open edX into a multi-tenant SaaS with per-organisation branding and "
                   "OTP login.",
        "metrics": ["multi-tenant", "OTP auth", "self-serve onboarding"],
        "chips": ["Open edX", "Python", "multi-tenant", "OTP auth"],
        "description": "Case study: turning Open edX into a multi-tenant SaaS with per-organisation "
                       "themes and OTP login.",
    },
]


FIXES = [
    {
        "slug": "schedule-generator",
        "title": "Pattern-based bulk schedule generator",
        "signal": "perf · 41× faster",
        "summary": "Re-checked every rule against the database inside a per-date loop. Hoisted, "
                   "prefetched and batched it, with output proven identical.",
        "metrics": ["8,879 → 53 queries", "12.7s → 311ms", "3 latent bugs fixed"],
        "foot": "Security workforce SaaS",
        "facts": [("Project", "Security workforce management SaaS"), ("Type", "Performance"),
                  ("Origin", "AI-generated, shipped unverified")],
        "chips": ["Django", "MySQL", "bulk_create", "query profiling"],
        "related": "workforce",
        "description": "How an AI-generated Django schedule generator went from 8,879 queries to 53 "
                       "and 12.7s to 311ms, with output proven identical.",
    },
    {
        "slug": "session-cap",
        "title": "Shared monthly session cap",
        "signal": "correctness · 18/18 checks",
        "summary": "Checked the wrong scope, counted cancellations, and let simultaneous bookings "
                   "slip past an account's monthly limit.",
        "metrics": ["wrong scope → account-wide", "race → serialized", "verified on production data"],
        "foot": "Online counselling platform",
        "facts": [("Project", "Online counselling platform"), ("Type", "Correctness"),
                  ("Origin", "AI-generated, shipped unverified")],
        "chips": ["Django", "MySQL", "transactions", "row locks"],
        "related": "counselling",
        "description": "Fixing an AI-generated booking limit check: wrong scope, counted cancellations "
                       "and a race between simultaneous bookings.",
    },
]

FAVICON = ("data:image/svg+xml,<svg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2032'>"
           "<rect%20width='32'%20height='32'%20rx='7'%20fill='%230A0E14'/><line%20x1='6'%20y1='16'%20"
           "x2='26'%20y2='16'%20stroke='%23F5A524'%20stroke-width='2'/><circle%20cx='16'%20cy='16'%20"
           "r='4'%20fill='%230A0E14'%20stroke='%23F5A524'%20stroke-width='2'/></svg>")

ICONS = {
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
}


def e(text):
    return escape(text, quote=True)


def card(p, section, go="read case study →"):
    metrics = "".join(f'<span class="sc-metric">{e(m)}</span>' for m in p["metrics"])
    foot = p.get("foot") or f'{p["company"]} · {p["years"]}'
    return f'''                <a class="sys-card reveal" href="{section}/{p["slug"]}/">
                    <span class="sc-signal"><span class="dot"></span>{e(p["signal"])}</span>
                    <h3>{e(p["title"])}</h3>
                    <p>{e(p["summary"])}</p>
                    <span class="sc-metrics">{metrics}</span>
                    <span class="sc-foot"><span>{e(foot)}</span><span class="sc-go">{e(go)}</span></span>
                </a>'''


def page(p, prev_p, next_p, section="systems"):
    url = f'{SITE}/{section}/{p["slug"]}/'
    chips = "".join(f'<span class="chip">{e(c)}</span>' for c in p["chips"])
    facts = p.get("facts") or [("Role", p["role"]), ("Company", f'{p["company"]} · {p["years"]}')] + \
        ([("Team", p["team"])] if p.get("team") else [])
    facts_html = "".join(f'\n                    <div class="cs-fact"><span class="lab">{e(k)}</span>{e(v)}</div>'
                         for k, v in facts)
    related = ""
    if p.get("related"):
        r = next(x for x in PAGES if x["slug"] == p["related"])
        related = (f'\n            <a class="cs-related" href="../../systems/{r["slug"]}/">'
                   f'<span>full case study →</span>{e(r["title"])}</a>\n')
    body = (ROOT / "content" / section / f'{p["slug"]}.html').read_text().strip()
    body = "\n".join(("                " + line) if line.strip() else "" for line in body.split("\n"))
    nav_prev = (f'<a class="cs-pn" href="../{prev_p["slug"]}/"><span>← previous</span>{e(prev_p["title"])}</a>'
                if prev_p else "<span></span>")
    nav_next = (f'<a class="cs-pn cs-pn-next" href="../{next_p["slug"]}/"><span>next →</span>{e(next_p["title"])}</a>'
                if next_p else "<span></span>")
    title = f'{p["title"]} · Syed Mahad Ehsan'
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- generated by tools/build_systems.py; edit content/systems/{p["slug"]}.html instead -->
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{e(p["description"])}" />
    <meta name="author" content="Syed Mahad Ehsan" />
    <meta name="theme-color" content="#0A0E14" />
    <link rel="canonical" href="{url}" />
    <title>{e(title)}</title>

    <meta property="og:type" content="article" />
    <meta property="og:title" content="{e(title)}" />
    <meta property="og:description" content="{e(p["description"])}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:site_name" content="Syed Mahad Ehsan" />
    <meta property="og:image" content="{SITE}/images/og-image.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{e(title)}" />
    <meta name="twitter:description" content="{e(p["description"])}" />
    <meta name="twitter:image" content="{SITE}/images/og-image.png" />

    <link rel="icon" href="{FAVICON}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
        rel="stylesheet" />
    <link rel="stylesheet" href="../../styles.css" />
</head>

<body class="cs-page">

    <div class="sidebar" aria-label="Social links">
        <a href="https://linkedin.com/in/syed-mahad-ehsan" target="_blank" rel="noopener" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24"><path d="{ICONS["linkedin"]}" /></svg>
        </a>
        <a href="https://github.com/SyedMahad" target="_blank" rel="noopener" aria-label="GitHub">
            <svg viewBox="0 0 24 24"><path d="{ICONS["github"]}" /></svg>
        </a>
    </div>

    <button class="theme-toggle" aria-label="Toggle light/dark mode">
        <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" /></svg>
        <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5" /><line x1="12" y1="1" x2="12" y2="3" /><line x1="12" y1="21" x2="12" y2="23" /><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" /><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" /><line x1="1" y1="12" x2="3" y2="12" /><line x1="21" y1="12" x2="23" y2="12" /><line x1="4.22" y1="19.78" x2="5.64" y2="18.36" /><line x1="18.36" y1="5.64" x2="19.78" y2="4.22" /></svg>
    </button>

    <nav>
        <div class="nav-inner">
            <a href="../../#top" class="brand"><span class="tag">SME</span> Syed Mahad Ehsan</a>
            <div class="nav-links">
                <a href="../../#work">/work</a>
                <a href="../../#systems">/systems</a>
                <a href="../../#fixes">/fixes</a>
                <a href="../../#stack">/stack</a>
                <a href="../../#contact">/contact</a>
                <span class="nav-sep"></span>
                <a class="ext" href="https://github.com/SyedMahad" target="_blank" rel="noopener">github</a>
                <a class="ext" href="https://linkedin.com/in/syed-mahad-ehsan" target="_blank" rel="noopener">linkedin</a>
            </div>
        </div>
    </nav>

    <main class="cs-main">
        <div class="wrap cs-wrap">
            <a class="cs-back" href="../../#{section}">← /{section}</a>

            <header class="cs-head">
                <div class="case-signal"><span class="dot"></span>{e(p["signal"])}</div>
                <h1>{e(p["title"])}</h1>
                <div class="cs-facts">{facts_html}
                </div>
                <div class="case-tech">{chips}</div>
            </header>

            <article class="cs-body">
{body}
            </article>
{related}
            <div class="cs-prevnext">{nav_prev}{nav_next}</div>

            <div class="cs-cta">
                <span>{"Want to talk about this system?" if section == "systems" else "Want to talk about this fix?"}</span>
                <a class="btn btn-primary" href="mailto:mahad.ehsan@gmail.com">→ get in touch</a>
            </div>
        </div>
    </main>

    <footer>
        <div class="wrap">
            <div class="foot-inner">
                <span>© 2026 Syed Mahad Ehsan · Karachi, PK</span>
                <div class="foot-links">
                    <a href="mailto:mahad.ehsan@gmail.com">email</a>
                    <a href="https://github.com/SyedMahad" target="_blank" rel="noopener">github</a>
                    <a href="https://linkedin.com/in/syed-mahad-ehsan" target="_blank" rel="noopener">linkedin</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="../../script.js"></script>
</body>

</html>
'''


def build_section(section, items, go):
    for i, p in enumerate(items):
        prev_p = items[i - 1] if i > 0 else None
        next_p = items[i + 1] if i + 1 < len(items) else None
        out = ROOT / section / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(p, prev_p, next_p, section))
        print("wrote", out.relative_to(ROOT))
    index = ROOT / "index.html"
    html = index.read_text()
    start, end = f"<!-- {section}:cards:start -->", f"<!-- {section}:cards:end -->"
    a, b = html.index(start) + len(start), html.index(end)
    cards = "\n".join(card(p, section, go) for p in items)
    html = html[:a] + "\n            <div class=\"sys-grid\">\n" + cards + "\n            </div>\n            " + html[b:]
    index.write_text(html)
    print(f"refreshed {section} cards in index.html")


def main():
    build_section("systems", PAGES, "read case study →")
    build_section("fixes", FIXES, "read write-up →")

if __name__ == "__main__":
    main()
