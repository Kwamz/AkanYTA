# Akan's YTA Program — Phase 1 front-end prototype

A static HTML/CSS/JS build of the design in `akans-yta-website-build-prompt.md`. It is a starting point: it settles the design system, copy structure and components before the WordPress block theme is built.

## Run it

Open `index.html` in a browser. No build step is needed to view it.

To regenerate pages after editing copy, nav or the header/footer:

```
python3 scripts/build.py
```

The header, footer, nav and icons are defined once in `scripts/build.py`. Styles are in `assets/css/styles.css` and use the brief's design tokens. Fonts (Manrope, Inter) are self-hosted in `assets/fonts/`.

## What is built

All 8 primary pages (with anchors for the sub-pages proposed in the kickoff deck, e.g. `about.html#mission`, `resources.html#helplines`, `contact.html#location`), plus Referral, Events and updates (calendar), Volunteer, Stories and Donate pages (layout only, no payments), Privacy Policy, Accessibility Statement and 404. Components: buttons, nav, mobile menu, hero, service cards, step lists, statement band, CTA band, resource filter, form with errors, footer, placeholder style. The optional quick exit is off by default.

## Not built yet

- **WordPress block theme, companion plugin and seed content** (brief deliverables 1 to 3). The next step is porting these pages into `theme.json`, templates and block patterns.
- **Calendar data.** The calendar reads `window.YTA_EVENTS` in `events.html`, which is empty. In WordPress this becomes an `event` post type.
- **Social media.** Footer links are placeholders. No feeds are embedded, so nothing sets cookies before consent.
- **Real form handling.** The contact and referral forms validate in the browser and send nothing. The server handler (nonce, honeypot, email to `[Program email]`) belongs in the plugin.
- **Donations.** `donate.html` has the structure, but no payment form. Payments need the parent organization, a processor and receipt rules.
- **Analytics.** None is loaded.
- **Accessibility audit** (axe or WAVE, keyboard run-through) and **Lighthouse**. Only a layout check at 360 and 1440 px has been done. No page overflows horizontally at 360 px.
- **Logo.** `assets/yta-logo.png` is the supplied file, unmodified (about 940 KB). Compress a copy for production.

See `PLACEHOLDERS.md` for everything that still needs a stakeholder decision.
