# Syed Mahad Ehsan · Portfolio

[![Live Site](https://img.shields.io/badge/Live%20Site-mahadehsan.com-F5A524?style=flat-square&logo=googlechrome&logoColor=white)](https://mahadehsan.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-syed--mahad--ehsan-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/syed-mahad-ehsan)
[![GitHub](https://img.shields.io/badge/GitHub-SyedMahad-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SyedMahad)

> Senior Backend Software Engineer — Python · Django · DRF · Celery · Redis · AWS

![Portfolio preview](images/og-image.png)

---

## What's in here

Personal portfolio site for [mahadehsan.com](https://mahadehsan.com). Single-page, fully static — no framework, no build step.

```
.
├── index.html          # markup
├── styles.css          # all styling, including light/dark theme
├── script.js           # scroll reveal, pipeline animation, contact form, theme toggle
└── images/
    └── og-image.png    # social card (1200×630)
```

---

## Features

- **Dark / light mode** — toggles via button, persists to `localStorage`, respects OS preference on first visit
- **Animated request pipeline** — signals sweep through `client → api → cache → queue → db` in sync
- **Scroll-reveal animations** — respects `prefers-reduced-motion`
- **Contact form** — powered by [Formspree](https://formspree.io), with honeypot spam protection
- **Sticky social sidebar** — LinkedIn and GitHub always reachable
- **Zero dependencies** — no npm, no bundler, no framework. Drop the files and it works.

---

## Sections

| Route | Content |
|---|---|
| `/work` | 3 roles across 5+ years, with specific metrics |
| `/systems` | 3 case studies — problem, approach, outcome |
| `/fixes` | AI-generated code I diagnosed and fixed, with before/after numbers |
| `/capabilities` | What I own: API design, async, caching, real-time, CI/CD, reliability |
| `/projects` | Side projects: facial recognition auth, therapy CRUD app, image-to-PDF utility |
| `/stack` | Full toolkit, education, certifications |
| `/contact` | Contact form + direct links |

---

## Deploy

**GitHub Pages** (already live):

```bash
git add .
git commit -m "update"
git push
```

GitHub Pages serves `index.html` at the repo root automatically. The custom domain is configured in repo Settings → Pages.

**Formspree** — to receive form submissions in your inbox, replace `YOUR_FORM_ID` in `index.html` with your real form ID:

```html
<form class="cform" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

Then set **Restrict to Domain → mahadehsan.com** in your Formspree dashboard to block off-domain submissions.

---

## Tech

Built with vanilla HTML, CSS, and JavaScript. Design system uses CSS custom properties for theming — the entire light/dark switch is a single class toggle on `<html>`.

```css
/* switching is this simple */
document.documentElement.classList.toggle('light');
```

Fonts loaded from Google Fonts: [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) · [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) · [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono).

---

## Contact

**mahad.ehsan@gmail.com** · [mahadehsan.com](https://mahadehsan.com)