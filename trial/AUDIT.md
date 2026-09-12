# Homepage audit and premium trial

## Second-pass update — 12 September 2026

The original audit below describes the first trial. Following feedback, the trial now retains a live GitHub calendar near the opening, including 6-month/year controls and honest loading, empty and error states. Order Visualizer links to a full-width public showcase with the supplied LinkedIn embed. The normal homepage also receives this embed and a direct LinkedIn fallback; its GitHub chart remains unchanged.

The Profitably reference was inspected through its public HTML and CSS: oversized tightly tracked headings, strong product-led sections and large whitespace inform this revision. The original trial hero remains; subsequent headings, feature scale and the lime contact section are stronger. No reference brand assets were copied.

New chart DOM-stub checks cover 365-day and 183-day totals, period selection, month labels, empty data and fetch failure. JavaScript syntax and diff whitespace checks pass. Both pages contain the provided embed URL and a descriptive iframe title; trial local references and anchors resolve. The four pre-existing missing images elsewhere on the normal homepage remain outside this change. No browser is available; actual LinkedIn playback and rendered layouts remain unverified. These are local changes, not a deployment.

---

## Scope and evidence

Reviewed the current `index.html`, `css/site.css`, `js/main.js`, project assets, local navigation destinations, and repository guidance. Built an isolated alternative at `/trial/`. Original homepage, shared styles and shared scripts are unchanged. This is a source and interaction-logic audit; visual browser verification remains outstanding because the browser runtime reported no available browsers.

## What already works

The direct builder positioning is memorable. Real projects and concrete evidence (30 colleagues, 104 matches, an approximately one-hour build) make the portfolio credible. Existing case studies give visitors useful depth. The warm palette and limited typography already give the site a recognizable personality. Static delivery keeps maintenance simple.

## Findings and changes

| Area | Finding | Priority | Trial response |
| --- | --- | --- | --- |
| First impression | The hero is capped at 48px and the content container at 880px. The page reads as a compact project directory, leaving little scope for an XXL impression. | High | Wider 1320px maximum layout, up to 145px headline, deliberate serif/sans contrast, large typographic composition. |
| Primary action | The hero’s only content action is the latest blog post; seeing projects requires navigation or scrolling past GitHub activity. | High | Explicit Explore the work button with a secondary GitHub link. |
| Reading order | Contribution graph sits between the introduction and the featured project. It prioritizes activity over useful outcomes. | High | Introduction → featured result and projects → building philosophy/activity link → writing → contact. |
| Card density | Long descriptions, implementation details, badges, screenshots and actions all occupy the same cards. Scanning takes work. | High | One featured case study, concise visual project cards, compact secondary project rows; implementation detail lives in case studies or dialogs. |
| Missing assets | Four referenced files do not exist: `stock-dashboard-jj.png`, `master-insights.png`, `taskflow.png`, `sidequests.png`. | High | Verified images only; two clearly labeled CSS concept visuals and intentionally typographic secondary cards. |
| Click affordance | All original cards lift on hover, including internal-tool cards without destinations. | Medium | Internal tools open real detail dialogs. Linked cards navigate to actual project pages. |
| Image handling | Original placeholders rely on JavaScript to disappear even when a screenshot exists. Uniform shallow crops also limit image readability. | Medium | No overlay placeholders; isolated image containers with explicit dimensions. |
| CTA hierarchy | Small mono text CTAs compete with many outlined badges and repeated heavy shadows. | Medium | Filled pill buttons for primary actions, restrained text links for secondary navigation, arrow feedback on cards. |
| Contact placement | Contact is available in navigation but no closing invitation follows the project story. | Medium | Dedicated closing contact panel with a direct contact-page destination. |
| Mobile controls | Existing theme button drops to 30×30px on mobile. Small navigation and tightly packed metadata reduce comfort. | Medium | 44px theme/filter controls, responsive single-column projects, simplified small-screen navigation. |
| Motion accessibility | Existing smooth scrolling and animations have no reduced-motion override. | Medium | CSS reduced-motion support; no autoplay or continuous motion. |
| Keyboard interaction | No explicit homepage skip link or custom focus treatment in the existing shared stylesheet. | Medium | Skip link, visible focus, native dialog with Escape support, focus restoration, semantic buttons and links. |
| Information freshness | Latest post is repeated separately from older blog entries; homepage activity depends on a third-party request. | Medium | Latest three posts in one writing section; static link to the existing activity page. No invented live statistics. |
| Isolation | Shared styles affect multiple existing pages. | High | Dedicated `trial.css` and `trial.js`; independent theme preference; no shared-file edits. |

## Design direction

Warm ivory, restrained forest-black panels, and electric lime for selected moments. Big type creates the first impression; whitespace and consistent alignment provide the premium feel. The tilted featured-project frame and interactive stamp add personality without obscuring project content. Small decorative dashboard charts are explicitly labeled as concept visuals, not product screenshots or current data.

Interactions include hover/press feedback, project image movement, theme switching, category filters with announced counts, and internal-tool dialogs. Filters sit before their results to avoid hiding content above the controls and shifting their position. All eight original project entries remain represented. Daily tools contains four entries; experiments contains the featured World Cup pool and three secondary projects.

## Verification

- JavaScript syntax check passed.
- Every local image, stylesheet, script and navigation destination in the trial exists.
- No duplicate IDs, missing image alt attributes or unresolved internal anchor targets.
- DOM-stub interaction checks passed for both theme states, all three filter counts (8 / 4 / 4), each of three detail dialogs, closing, and focus restoration. These checks do not establish browser rendering or native dialog behavior.
- Calculated principal contrast ratios: ink on paper 14.29:1; muted text on paper 5.18:1; ink on lime 13.26:1; featured body text on dark panel 8.56:1; dark-theme muted text 8.27:1. These are token checks, not a complete rendered accessibility certification.
- Local preview returned HTTP 200.
- HTML, CSS and JavaScript total approximately 31 KB before compression, excluding existing images. No additional packages or external font requests.
- Trial includes `noindex,nofollow` and does not add analytics.

## Remaining visual review

A browser must still confirm layouts at approximately 375px, 768px and 1440px, screenshot crops, horizontal overflow, native modal focus trapping/Escape, touch interaction and reduced-motion behavior. External destinations have not been checked for live availability. Existing case study pages retain their current design, so following those links intentionally leaves the new visual direction.

## Preview

With the local server running, open `http://localhost:8000/trial/`. Use the bottom “View original” switch to compare with the current homepage. Nothing has been published. To start another preview session later, run `python3 -m http.server 8000` from the repository root.
