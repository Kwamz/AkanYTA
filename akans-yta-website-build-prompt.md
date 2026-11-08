# Akan's YTA Program — Website Build Prompt

Copy everything below the line into Claude Code, Cursor, or another AI coding tool. Attach the Akan's YTA logo file along with it.

---

## ROLE

Act as a senior WordPress developer, front-end engineer, and UX/UI designer who builds accessible, privacy-conscious websites for youth-serving organizations.

Build the Phase 1 website for **Akan's Youth Transitions to Adulthood (YTA) Program**, based in Edmonton, Alberta, Canada. Use the brief, structure, brand system, and constraints below. When something is not specified, choose the simpler and more accessible option, and leave a clearly marked placeholder rather than inventing details.

## 1. PROJECT CONTEXT

**About the program (confirmed)**

- Akan's YTA supports young people aged **15–22** as they move into independent adulthood.
- It serves youth who are leaving foster care or group care, or who are navigating adulthood without consistent family support.
- Dedicated youth workers give one-on-one, youth-centred support, built around each participant's own goals.
- Support areas:
  - independent living and life skills
  - housing and accommodation
  - financial literacy and budgeting
  - employment readiness and career development
  - education planning
  - access to community resources
  - healthy relationships and support networks
  - connections to mental health and addiction services when needed
- Tagline: **Supporting Youth. Building Brighter Tomorrows.**
- Brand message: **Stronger. Brighter. Independent. Together.**

**Project vision**

> Create a welcoming, accessible and informative digital platform that connects young people, referral partners and community stakeholders with the resources and support offered by Akan's YTA Program.

The goal is to move from a basic online presence to a structured information and engagement platform.

**Confirmed constraints. Do not contradict these.**

- Akan's YTA is a **program operating under a parent organization**. Never present it as an independent registered charity or nonprofit.
- The website's primary purpose is **informational**.
- A private participant portal is a **possible future phase only**. Do not build it. You may leave the architecture open for it.
- Official contact information has **not been established**.
- Domain ownership and selection are **undecided**.

**Never invent:**

- parent organization details
- staff names
- phone numbers, emails, or addresses
- statistics
- testimonials or youth stories
- budgets
- launch dates
- eligibility rules beyond "ages 15–22"

Use bracketed placeholders instead, for example `[Parent organization name]`, `[Program phone]`, `[Program email]`, `[Office address]`, and `[Eligibility criteria — pending approval]`. List every placeholder in a `PLACEHOLDERS.md` file.

## 2. AUDIENCES AND THEIR PRIMARY ACTIONS

| Audience | What they need | Primary action |
| --- | --- | --- |
| Young people aged 15–22 | What the program is, in plain language; what support looks like; whether they are eligible | Reach out to the program |
| Social workers, case managers and referral professionals | Scope of services, eligibility criteria, how referral works | Make a referral or enquiry |
| Community organizations and partners | Mission and approach, how YTA complements their work, ways to collaborate | Connect to partner |

**Writing tone:**

- For youth: warm, direct, plain language, written in the second person ("you"). Aim for a Grade 6–8 reading level.
- For professionals: precise and scannable.
- Avoid jargon, deficit framing, and childish language.

## 3. WEBSITE OBJECTIVES (use as acceptance criteria)

1. Inform and educate: explain what YTA is and how it helps.
2. Explain program eligibility for youth and referrers.
3. Showcase the support services clearly and consistently.
4. Simplify access to information: a logical structure that is quick to scan on any device.
5. Build stakeholder trust: credible, consistent, professional.
6. Encourage contact and referrals: a clear call to action on every page.

## 4. SITEMAP AND PAGE REQUIREMENTS

The primary navigation, in this order: **Home · About Us · The YTA Program · Our Services · How It Works · Resources · Get Involved · Contact Us**.

The header always shows a "Contact" button in gold. The sub-pages listed below are proposed. Build them as sections or anchors on the parent page unless the content clearly needs its own page.

**Home**

1. Header and navigation, with a persistent Contact call to action.
2. Hero on deep teal:
   - Eyebrow: "Youth Transitions to Adulthood"
   - Headline: "Your future. Your journey. Your possibilities."
   - Supporting line: "We're here to help you build the skills, confidence and support network for independent living."
   - Primary button: "Discover the YTA Program →"
   - Secondary link: "Make a referral"
3. Program introduction: a short paragraph and a link to The YTA Program.
4. Services overview: cards for the eight support areas, each linking to Our Services.
5. How it works: 3–4 steps, linking to How It Works.
6. Youth-centred message band: "Stronger. Brighter. Independent. Together."
7. Community and partnerships section, linking to Get Involved.
8. Contact call-to-action band in gold: "Ready to talk? Get in touch."
9. Footer:
   - Logo
   - Tagline
   - Quick links
   - Contact placeholders
   - Privacy policy link
   - "A program of [Parent organization name]"

**About Us**

- Mission and youth-centred approach.
- Parent organization section, with a placeholder only.

**The YTA Program**

- Who it's for: ages 15–22, leaving care or without consistent family support.
- What participants can expect from one-on-one support with a youth worker.
- Eligibility, marked `[pending approval]`.

**Our Services**

- One section per support area (the eight areas above). Each has a heading, a 2–3 sentence description placeholder, and an icon.

**How It Works**

- Referral process: steps with placeholders, for professionals.
- What to expect: written for youth.
- Self-referral versus professional referral: placeholder until confirmed.

**Resources**

- Community resource directory. This is a CMS-managed list with:
  - name
  - category
  - short description
  - website
  - phone (optional)
- Users can filter it by category on the client side.
- Crisis and helpline section. Use only clearly marked placeholders, which the program staff must verify before launch.

**Get Involved**

- Partner organizations: how to collaborate.
- Referral partners: how to refer.
- An enquiry call to action.

**Contact Us**

- Secure general enquiry form. It collects only:
  - name (or "preferred name")
  - email or phone
  - "I am a…" (young person / professional / organization / other)
  - message
  - consent checkbox
- A notice telling visitors not to share sensitive personal details in the form.
- Contact details and location as placeholders.

**Also build:**

- Privacy Policy page (placeholder text to be supplied by the parent organization)
- Accessibility Statement page
- 404 page

## 5. BRAND AND DESIGN SYSTEM

Use the attached logo as supplied. Do not redraw, recolour, crop, or distort it. Use the full logo in the footer and on About Us. For the header, use the logo at a small size, or a wordmark ("AKAN'S YTA PROGRAM") in Manrope 800 in deep teal.

**Design tokens**

```css
:root {
  /* Colour */
  --color-evergreen: #175451;   /* primary: header, footer, hero, headings */
  --color-growth:    #0F7771;   /* secondary: buttons, links, icons */
  --color-gold:      #F3BD58;   /* highlights and primary CTAs (charcoal text only) */
  --color-sage-blue: #789798;   /* decorative: dividers, secondary accents (not for text) */
  --color-charcoal:  #1B2124;   /* body text */
  --color-white:     #F5F7F4;   /* main page background */
  --color-sage:      #E6EEEA;   /* cards and alternating sections */
  --color-muted:     #4E5B5E;   /* secondary text */

  /* Type */
  --font-heading: "Manrope", system-ui, sans-serif;  /* headings, nav, buttons */
  --font-body:    "Inter", system-ui, sans-serif;    /* body, forms */

  /* Shape and space */
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-pill: 999px;
  --space-section: clamp(4rem, 8vw, 7rem);
  --container: 1200px;
}
```

**Colour proportion (approximate)**

| Colour | Share |
| --- | --- |
| Soft white | 45% |
| Evergreen | 25% |
| Growth teal | 12% |
| Gold | 8% |
| Blue sage | 5% |
| Charcoal | 5% |

**Colour accessibility rules**

- Use evergreen or charcoal text on light backgrounds.
- Use white text on evergreen or growth teal.
- Use charcoal text on gold.
- Never use gold as text on white.
- Never place small text over photos.
- Blue sage is for decoration only. Never use it for text.

**Design principles**

- Modern, welcoming, and youth-friendly.
- Professional and trustworthy.
- Spacious layouts.
- Clear calls to action.

**Visual direction**

- Rounded cards.
- Gold accent bars.
- Deep teal statement sections.
- Simple line icons (for example, Lucide).
- No cartoons, heavy gradients, or overly childish styling.

**Photography**

- Use authentic, diverse photos of young adults that are licensed or used with consent.
- Until real images are approved, use neutral placeholder blocks labelled `[Photo — consent required]`.
- Never use stock photos that imply they are real participants.

**Components to build and reuse:**

- buttons (primary gold, secondary teal, text link)
- navigation
- mobile menu
- hero
- service card
- step list
- statement band
- CTA band
- resource directory item and filter
- form fields with errors
- footer
- placeholder notice style

## 6. TECHNICAL REQUIREMENTS

The final stack will be confirmed in technical discovery. Build to this proposed direction:

- **CMS:** WordPress, latest stable version. Authorized staff must be able to update pages, services, resources, and contact details without a developer.
- **Theme:** a custom, lightweight, responsive block theme.
  - Use `theme.json` for the design tokens.
  - Use block patterns for each homepage section, so staff can rearrange content safely.
  - Do not use a heavy page builder.
- **Styling:** modern CSS. Use Tailwind CSS only where it fits a build step, and keep the output small.
- **Content model:**
  - Custom post type `resource`, with a `resource_category` taxonomy and fields for URL and phone. Use native meta or ACF.
  - Custom post type `service`, or a structured page.
  - A site options area for contact details, so they can be updated in one place.
- **Forms:**
  - A secure enquiry form with server-side validation, nonce/CSRF protection, honeypot or privacy-friendly spam protection, and minimal data collection.
  - Email notification to `[Program email]`.
  - Do not store submissions in the database unless this is approved. Make storage configurable.
- **Security:**
  - HTTPS/SSL.
  - Least-privilege user roles: Administrator and Editor/Content Approver.
  - Support for multi-factor authentication (MFA) on admin accounts.
  - Login hardening.
  - Automated backups, documented.
  - Disable XML-RPC and file editing in the admin.
  - Keep plugins to a vetted minimum.
- **Analytics:**
  - A privacy-conscious option (for example, Plausible, Matomo, or GA4 with consent mode).
  - Load it only after consent where required.
- **Hosting:** managed WordPress hosting approved by the parent organization. Provide environment-agnostic configuration through `wp-config` constants or environment variables.
- **SEO:**
  - Semantic HTML.
  - Unique titles and meta descriptions.
  - Open Graph tags.
  - XML sitemap.
  - Schema.org `Organization` markup, using placeholder fields only.
  - Clean, readable URLs.
- **Performance:**
  - Responsive images (WebP/AVIF, `srcset`, lazy loading).
  - Self-hosted Manrope and Inter fonts with `font-display: swap`.
  - Minimal JavaScript.
  - Target a Lighthouse score of 90+ in every category.

## 7. ACCESSIBILITY (WCAG 2.2 AA, required)

- Semantic landmarks and a logical heading order: one `h1` per page.
- A skip link and full keyboard navigation, including the mobile menu.
- Visible focus indicators: a 3px gold or teal outline that meets contrast requirements.
- Text contrast of at least 4.5:1 (3:1 for large text and UI components).
- Touch targets of at least 24×24 px (aim for 44×44).
- Form labels, instructions, error messages announced with `aria-live`, and no reliance on colour alone.
- Respect `prefers-reduced-motion`.
- Alt text for every meaningful image. Empty alt for decorative images.
- Readable at 200% zoom and 320 px width, with no horizontal scrolling.
- Test with axe or WAVE and with keyboard-only navigation. Document the results.

## 8. PRIVACY AND SAFEGUARDING

Many people this site serves are minors or in vulnerable circumstances.

- **Data minimization:** collect only what is needed to respond.
- **Form notice:** "Please don't include private details like health information or case numbers. We'll follow up to learn more."
- **Consent:** do not use participant names, photos, or stories without documented consent (including guardian or agency consent for minors).
- **Placeholders:** add placeholders for the parent organization's approved privacy policy and safeguarding statement.
- **Third-party scripts:** no tracking pixels or social embeds that set cookies before consent.
- **Quick exit:** add an optional "Quick exit" button to the header, behind a setting. It is off by default and can be enabled if stakeholders approve.

## 9. OUT OF SCOPE FOR PHASE 1

Do not build:

- a participant login or portal
- online case intake that stores personal information
- donations or e-commerce
- news or events
- multilingual content

Structure the code so that these can be added later.

## 10. DELIVERABLES

1. A custom WordPress block theme, including:
   - `theme.json`
   - templates
   - template parts
   - block patterns
   - styles
2. A small companion plugin, kept separate from the theme, that registers the custom post types, taxonomies, the site options page, and the enquiry form handler.
3. Seed content: all pages with draft copy written to this brief and every unknown marked as a placeholder.
4. `README.md` covering:
   - local setup (wp-env or Docker)
   - build steps
   - deployment notes
   - recommended plugins (security, backups, MFA, SEO, analytics)
   - roles and permissions
   - a backup and update routine
5. `PLACEHOLDERS.md`: every placeholder, and the stakeholder decision it depends on.
6. `CONTENT-EDITING-GUIDE.md`: plain-language instructions for staff to edit pages, add resources, and update contact details.
7. An accessibility and QA checklist with results.

## 11. HOW TO WORK

Build in this order and check in after each step:

1. **Plan.** Confirm the file structure, the content model, and the plugin list. Ask questions only where an answer would change the architecture.
2. **Foundations.** `theme.json` tokens, typography, colours, spacing, buttons, header, footer, and mobile navigation.
3. **Homepage.** Build every section as a block pattern. It must be responsive at 360, 768, 1024, and 1440 px.
4. **Inner pages.** Build them in sitemap order.
5. **Content model and form.** The resource directory, the enquiry form, and the options page.
6. **Hardening.** Security, SEO, analytics consent, and performance.
7. **QA.** Accessibility audit, cross-browser and device checks, and Lighthouse. Fix any issues, then write the docs.

Keep the code clean, commented, and maintainable by a small team. Prefer WordPress core features over plugins.

## 12. STAKEHOLDER DECISIONS THAT ARE STILL OPEN

Design around these decisions without assuming the answers:

- parent organization name and website ownership
- approval of the digital branding
- domain and hosting
- official contact information
- approved program descriptions and eligibility wording
- authorized content approvers
- privacy and safeguarding requirements
- who maintains the website after launch

**Success criteria:**

- A young person can understand the program and know how to reach out within two clicks of the homepage.
- A referral professional can find eligibility and referral information within two clicks.
- Staff can update content on their own.
