# Placeholders

Every unknown fact on the site is a bracketed placeholder, shown with a dashed gold outline (`.ph`). Search the HTML or `scripts/build.py` for `ph(` to find them. Do not replace one until the decision it depends on is confirmed.

| Placeholder | Where it appears | Depends on |
| --- | --- | --- |
| [Parent organization name] | Footer, About Us, Organization schema | Parent organization confirmed |
| [Parent organization details — pending] | About Us | Approved wording about the parent organization |
| [Mission statement — pending approval] | About Us | Approved program descriptions |
| [Program phone] | Footer, Contact, schema | Official contact information |
| [Program email] | Footer, Contact, Accessibility, schema, form recipient | Official contact information |
| [Office address] / [Office hours] | Footer, Contact | Official contact information |
| [Website URL] | Organization schema | Domain decision |
| [Eligibility criteria — pending approval] | The YTA Program, How It Works | Approved eligibility wording |
| [Self-referral — pending confirmation] | Home, How It Works | Whether youth can self-refer, and consent rules |
| [Intake details / Intake steps — pending] | Home, How It Works | Approved intake process |
| [Referral criteria / method / response timeline / transition steps] | How It Works (professionals) | Approved referral process |
| [Approved description, 2 to 3 sentences — pending] | Each of the 8 services | Approved program descriptions |
| [Ways to collaborate — pending] | Get Involved | Partnership approach |
| [Resource name N], [Short description], [URL], [Phone] | Resources directory | Verified resource list from staff |
| [Crisis and helpline numbers — staff must verify before launch] | Resources | Staff verification |
| [Photo — consent required] | Home | Licensed images or documented consent |
| [Approved privacy policy] | Privacy Policy | Parent organization privacy policy |
| [Safeguarding statement — pending] | Footer, Privacy Policy | Parent organization safeguarding requirements |
| [Analytics approach — pending] | Privacy Policy | Analytics choice and consent approach |
| [Test results and date] | Accessibility Statement | Completed accessibility audit |

## Settings that need a stakeholder decision

- **Quick exit button:** off by default. Set `quickExit: true` in `assets/js/main.js` once approved.
- **Form submission storage:** the prototype stores nothing and sends nothing.

## Open stakeholder decisions (from the kickoff deck)

All eight are pending approval, and every owner is still "[To be assigned]". The "needed by" column is the deck's proposal.

| # | Decision | Needed by |
| --- | --- | --- |
| 1 | Confirm parent organization and website ownership | Discovery |
| 2 | Approve the program's digital branding approach | UX/UI design |
| 3 | Confirm domain and hosting arrangements | Discovery |
| 4 | Provide official organizational contact information | Development |
| 5 | Approve program descriptions and eligibility information | Development |
| 6 | Identify authorized content approvers | Discovery |
| 7 | Confirm privacy and safeguarding requirements | Discovery |
| 8 | Identify who is responsible for website maintenance | Before launch |

Project dates, phase durations and the launch date are "[to be agreed with stakeholders]". Do not publish any.

## Scope reminder (kickoff deck)

- **Phase 1:** responsive site, program and service pages, resource directory, contact and enquiry forms, SEO, analytics, WCAG 2.2 AA, privacy and security safeguards.
- **Later:** participant portal (potential only), secure online referral intake, news and events, consented youth stories.

## Donate page (added after the original brief)

Donations were out of scope for Phase 1 in the brief. The page `donate.html` was added on request, with no payment processing.

| Placeholder | Depends on |
| --- | --- |
| [Donation form — not connected] | Parent organization confirmed, payment processor chosen and approved |
| [Receipt and registration wording] | Parent organization's legal and charitable status. Never describe the program as its own registered charity. |
| [How gifts are used] | Approved wording from the program |
| [Donations email], [Details and link] for each "other ways to help" card | Which giving options are actually offered |
| [Program numbers] | Real, approved figures only. None are shown. |

## Pages added from the second round of requests

Events, community updates, testimonials and donations were out of scope for Phase 1 in the brief. They were added on request. Treat each as layout only until approved.

| Placeholder | Where | Depends on |
| --- | --- | --- |
| [Figure], [What it measures] | Home, Community impact | Real, approved program data. None are shown. |
| [Quote], [Name, role, year] | Stories | Documented consent (guardian or agency for minors) |
| [Consent process and withdrawal wording] | Stories | Parent organization approval |
| [Date], [Update headline], [Short summary] | Events and updates | Approved news content |
| Event list | Events (`window.YTA_EVENTS` in `events.html`) | Real events from staff. The list is empty. |
| [Volunteer role N], [Screening, training and age requirements] | Volunteer | Parent organization safeguarding rules |
| [Consent requirements for youth, guardians and agencies] | Referral | Referral and consent policy |
| [What happens after you refer, and the response time] | Referral | Approved referral process |
| [Family involvement and consent] | Home (family path) | Family involvement policy |
| [Instagram / Facebook / LinkedIn / YouTube link] | Footer | Which accounts exist and are approved |

## Donate page, second version

The page now follows the order of the reference donate page. The donation card is a disabled layout preview that cannot be submitted.

| Placeholder | Depends on |
| --- | --- |
| [Amount] x4, frequency toggle, "Donate (coming soon)" button | Payment processor and approved amounts |
| [Campaign title], [Short campaign description] | An actual approved campaign |
| [Figure] x4, [Year] | Real, approved program data |
| [Approved details] on each "other ways" card | Which giving options the program offers |
| [Charitable status and registration wording] | Parent organization. Never describe the program as its own registered charity. |

## Donation form, third version (matches the supplied form screenshot)

The form is interactive but connects to no payment system. "Next" shows a prototype message and nothing is charged or sent.

| Item | Status |
| --- | --- |
| Suggested amounts $50, $75, $150, $200 | Taken from the reference form. **Pending approval** by the program. |
| "Focus my gift" areas | The eight confirmed support areas |
| [Approved impact wording] | Parent organization and program to approve |
| Payment step after "Next" | Needs a payment processor and receipt rules |

## Filled from the supplied donation copy

The Donate page now uses the supplied wording for: the hero, the intro, "Why Your Support Matters" and its six outcomes, "Be Part of Their Journey" (three cards), "Interested in Making a Contribution?" and the closing "Together, We Can Build Brighter Tomorrows" band. The same copy filled "Ways to collaborate" on Get Involved and "Why volunteer" on Volunteer.

These earlier placeholders no longer apply: [How gifts are used], [Approved impact wording], [Approved details] on the "other ways" cards, and [Ways to collaborate]. The guessed giving options (monthly, legacy, in memory, workplace) were removed.

Still open on the Donate page: [Program phone], [Donations email], the featured campaign, the four "by the numbers" figures, the receipt and charitable-status wording, and the suggested gift amounts. The giving form is a preview only, and the page says donation arrangements are still being finalized.

## Donate page hero photo

`assets/images/hero-donate.jpg` was supplied by the site owner and replaces the "[Photo — consent required]" block in the Donate hero.

| Item | Status |
| --- | --- |
| Licence or consent for the photo | **Not confirmed.** Confirm who owns it and that it may be used on this site. |
| Whether the people shown are program participants | Unknown. The page does not say they are. Do not caption it as such unless it is true and consent is documented. |
| Visible school name on the student's jersey | Consider whether this is acceptable, or crop or replace the photo. |
| Credit line, if the licence requires one | Add once known |

## Home hero photo

`assets/images/hero-home.jpg` (supplied by the site owner) replaces the logo card in the home hero. The logo is still in the header and footer.

| Item | Status |
| --- | --- |
| Licence for the photo and any credit line | **Not confirmed.** It looks like a professionally shot stock image, so check the licence covers this use. |
| Whether the people shown are program participants | They do not appear to be. The page does not say they are. The brief forbids stock photos that imply real participants, so do not caption it as the program, and consider swapping it for approved photos of the program once consent is in place. |

Update: the home hero photo is now a full-width background behind the headline, with a dark green gradient for text legibility. If the photo is swapped for a brighter or busier one, re-check that the white and gold text stay readable.
