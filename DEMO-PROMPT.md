You are doing an unattended MAKEOVER of the existing River Inn at Seaside demo in this folder. Do not wait for confirmation. Overwrite the current static site in place. Do not git push and do not create a new repo.

Curtis rejected the current demo. A visitor should actually prefer this rebuild over the live original. The original already looks good. Our demo does not.

LIVE ORIGINAL (fetch pages yourself; this is the look/feel to honor and beat):
https://www.riverinnatseaside.com/

CURRENT DEMO (this is what to replace — teal+tomato cookie cutter):
https://cjessup.github.io/river-inn-at-seaside/
Local files in this folder are that same demo (Fraunces+Outfit, --sunset tomato #c45e32, teal chrome).

WSR-52: https://kestrelintegrations.youtrack.cloud/issue/WSR-52

WHY THE CURRENT DEMO FAILED
- Cookie-cutter lodge template: tomato sunset CTAs + deep teal chrome, not this inn
- Fraunces + Outfit identity instead of the original deco wordmark + tracked-caps Lato
- Text-on-hero with a dark scrim over the photo
- No scroll motion (original fadeInUp / slide-in on scroll)
- Photos have a teal grade
- Weak connection to the original brand

MUST — PALETTE (from original, not the lodge template)
- Nav/chrome: #48545A slate
- Primary CTA: #B79661 brass, hover ~#A5854F
- Blush: #EDDDDD
- Sand: #E8E1D4
- Text: #463939
- Headings: #363636
- Page: #F7F7F7
- DROP --sunset tomato / deep teal as brand colors
- Teal #3B6F84 only as a tiny accent if at all (Tripadvisor-attribution color is ok as tiny accent, not chrome)

MUST — TYPE
- Deco wordmark lockup: RIVER / INN stacked like the original (SVG or image). White on slate in the header.
- Tracked-caps sans for nav, eyebrows, section labels: Lato or similar, letter-spacing ~.3em, uppercase
- Body: Source Sans Pro or equivalent
- Do NOT keep Fraunces+Outfit as the identity

MUST — MOTION
- IntersectionObserver fade-up reveals as sections enter view (~500ms, stagger ~80ms)
- prefers-reduced-motion: reduce disables the motion
- Optional light hero parallax on desktop only
- This is the original's "slide in on scroll"

MUST — HERO
- Full-bleed uncovered blue-hour exterior (minimal/no dark scrim)
- Headline in a WHITE BLOCK BELOW the photo, centered, with a tracked-caps eyebrow above
- Keep Book / Call / Directions but restyle brass primary + slate outline
- Do not put the main headline as white text on the photo

MUST — LAYOUT
- Airier bands: white text → full-width photo → blush/sand reviews → white
- More vertical padding than the current demo
- Gold-ribbon or brass dividers ok if they match original
- Compact chips ok; NEVER fat white bubbles / large padded white cards

KEEP CONVERSION WINS (restyle brass/slate)
- Sticky header: wordmark, tel, brass Book
- Sticky mobile Call | Book bar restyled brass/slate
- homepage tel:+15037175744 everywhere a phone appears
- per-room Book + Call
- Cloudbeds availability https://hotels.cloudbeds.com/reservation/pVXpz4 (keep existing room rid query params if still valid)
- "call the desk" for choosing rooms
- Do NOT invent nightly rates

PHOTOGRAPHY
- Warm high-contrast, match original blue-hour exterior + bright interiors
- If you generate or regrade images, STRIP the teal grade
- Do not scrape copyrighted photos from the live original. Generate original images or regrade the existing local assets/ files toward warm blue-hour / bright interiors
- Replace assets/logo.svg with a deco RIVER/INN stacked lockup

HONESTY
- Facts only: 531 Avenue A, Seaside, Oregon; (503) 717-5744; info@riverinnatseaside.com; 48 rooms; check-in 4:00 PM; check-out 12:00 PM; 24/7 desk
- No invented rates, reviews, amenities, or awards
- Guest quotes only if they already exist on the live original (Tripadvisor guest quotes on the original homepage are fair to reuse if you fetch them)
- Do not contact the business

DO NOT COPY from original
- Cookie banner / cookie widget
- a11y overlay widget
- Duda "Add your custom HTML here" leaks
- "Powered by Cloudbeds" footer chrome as a vendor badge is optional; Cloudbeds is the book engine, not a brand lock-in

DELIVERABLE
Overwrite this folder's static brochure (index, rooms, amenities, about, nearby, book, privacy, 404). Keep relative asset paths for GitHub Pages at /river-inn-at-seaside/. Include .nojekyll, robots.txt, sitemap.xml.
Prefer HTML/CSS/JS. Folder root is the site root.
When done, update BUILD-NOTES.md: what changed vs the rejected teal/tomato demo, palette/type/motion, facts used vs omitted, conversion chrome kept.
Print a short summary to stdout.
Do not git commit or git push.
