# Build notes — River Inn at Seaside demo (makeover)

Unattended makeover for WSR-52 after the first teal/tomato lodge demo was rejected. Live brochure: https://www.riverinnatseaside.com/ (Duda). Live booking: https://hotels.cloudbeds.com/reservation/pVXpz4. The business was not contacted. No git commit or push.

## What changed vs the rejected teal/tomato demo

The first demo used a cookie-cutter lodge template: Fraunces + Outfit, `--sunset` tomato `#c45e32` CTAs, deep-teal chrome (`#16343c` / `#2f6a78`), text-on-hero with a dark scrim, and a teal color grade on photos. It did not look like this inn.

This rebuild honors the live original’s identity and tries to beat it on conversion and motion:

| Rejected demo | This makeover |
| --- | --- |
| Tomato CTAs + teal header | Brass `#B79661` CTAs + slate `#48545A` chrome |
| Fraunces + Outfit | Deco Cinzel RIVER/INN lockup + Lato tracked caps + Source Sans 3 |
| Headline as white type on a darkened photo | Full-bleed uncovered blue-hour photo; headline in a white block below |
| No scroll motion | IntersectionObserver fade-up (~500ms, stagger ~80ms); `prefers-reduced-motion: reduce` disables it; light desktop-only hero parallax |
| Teal-graded, dingy interiors | Warm blue-hour exterior + bright interiors, original generated photos |
| Dark compact chips on teal | Tiny tracked-caps chips, no fat white bubbles or padded cards |

## Palette

From the live original, not the lodge template:

- Nav/chrome: `#48545A` slate
- Primary CTA: `#B79661` brass, hover `#A5854F`
- Blush: `#EDDDDD` (review band)
- Sand: `#E8E1D4` (date bar, alt sections)
- Text: `#463939` · Headings: `#363636` · Page: `#F7F7F7`
- Teal `#3B6F84` only as a tiny Tripadvisor-attribution accent
- Tomato `--sunset` and deep teal dropped as brand colors

## Type

- Deco stacked wordmark: RIVER / brass diamond rule / INN (Cinzel in the header; `assets/logo.svg` is the same lockup)
- Tracked-caps Lato (~.22–.32em) for nav, eyebrows, buttons, section labels
- Body: Source Sans 3
- Fraunces + Outfit are gone

## Motion

- `.reveal` elements fade/slide up as they enter view (IntersectionObserver, 500ms, 80ms stagger)
- `prefers-reduced-motion: reduce` shows content immediately and disables parallax
- Optional hero parallax on desktop only (`min-width: 820px`)

## Layout

Airier bands: white copy → full-width photo → blush reviews → white → slate book band → Prom photo. More vertical padding than the rejected demo. Brass ribbon dividers. Compact chips. Room rows are hairline lists, not fat cards.

Homepage hero: uncovered blue-hour exterior, then a centered white block with tracked eyebrow, headline, Book / Call / Directions (brass primary + slate outline).

## Conversion chrome kept (restyled brass/slate)

- Sticky header: wordmark, `tel:+15037175744`, brass Book
- Sticky mobile Call | Book bar
- Homepage phone everywhere a phone appears
- Per-room Book + Call
- Cloudbeds `https://hotels.cloudbeds.com/reservation/pVXpz4` with existing room `rid` query params
- “Call the desk” for choosing rooms
- Date bar → Book page → Cloudbeds
- Hold form on Book (localStorage only; not a confirmed reservation)
- No invented nightly rates

## Stack

Plain HTML / CSS / JS at folder root (GitHub Pages at `/river-inn-at-seaside/`). `_build_pages.py` stamps shared chrome. `.nojekyll`, `robots.txt`, `sitemap.xml`. Canonical host: `cjessup.github.io`.

Photos are original generated assets of a coastal river inn, not scraped from the live site. Logo/favicon are original SVG.

## Pages

Home, Rooms, Amenities (`amenities.html`), Seaside (`nearby.html`), About, Book/contact (`book.html`), Privacy, 404.

## Facts used (confirmed from live pages + Cloudbeds JSON-LD)

| Fact | Source |
| --- | --- |
| Name: River Inn at Seaside | live home, Cloudbeds |
| 531 Avenue A, Seaside, Oregon 97138 | live footer on every page |
| Desk `(503) 717-5744` → `tel:+15037175744` | live footer / rooms / groups |
| Email `info@riverinnatseaside.com` | live footer |
| Cloudbeds `https://hotels.cloudbeds.com/reservation/pVXpz4` | live Book Now |
| Check-in 4:00 PM, check-out 12:00 PM, 24/7 desk | live header strip |
| 48 rooms and suites; 1 block downtown, 2 blocks to beach | live home + rooms intro |
| Geo 45.99213791, −123.92525482 | Cloudbeds LodgingBusiness |
| King (1 king + queen sofa sleeper); King river view + balcony; Two queens; Two queens river view + balcony; Queen river view accessible (walk-in shower, ADA); Two queen suite (kitchen, 2 balconies, sleeps 6); King suite (2 sofa sleepers, kitchen, 2 balconies, sleeps 6) | live `/rooms-and-amenities` + Cloudbeds `containsPlace` |
| Occupancy 4 on standard rooms, 6 on suites | Cloudbeds occupancy + rooms copy “sleep up to 6” |
| Indoor saltwater heated pool & spa; complimentary deluxe continental breakfast; bikes; playground; game room; fitness; fire pits; cookies; DVDs; business center; coin laundry; free parking; free Wi-Fi; EV charging; pets on request | live amenities list |
| Elevator; table tennis | Cloudbeds amenityFeature |
| Pet fee $25 / pet / night + welcome kit | live `/specials` |
| S’mores $15, birthday $30, romance $40; 24-hour notice | live `/specials` |
| Groups 10+; Necanicum meeting room 315 sq ft, 25–30 guests | live `/groups-and-meetings` + rooms “10 rooms or more” |
| Cancellation 48 hours by 4 PM two days before; 18+ check-in; charge morning of arrival; notify if after 6 PM; one parking pass except occupancy 6+ | live `/terms-and-conditions` |
| Nearby list, restaurants, 12 mi Cannon Beach / Warrenton, 25 mi Astoria, ~90 min Portland | live `/destination` |
| Social: Instagram, Facebook, Tripadvisor, Yelp | live footer |
| Three Tripadvisor guest quotes on the live homepage | reused on this homepage, attributed “Tripadvisor Guest” |

## Facts omitted (on purpose)

- **Nightly room rates.** Not printed on the live brochure. Cloudbeds is the price path. No demo “from $X”.
- **Sister-property phone `(503) 738-9581`** and Inn at Seaside / SaltLine addresses. Never used.
- **`info@amadoka.com`** in the live header “Connect” block — Duda leftover. Desk email only.
- **Specific awards.** Live copy says “award-winning” without naming an award. Not restated as a verified trophy.
- **OTA-only extras** (Priceline/Kayak scores, “yoga mats in every room”) unless also on the inn’s own pages. Cookies in the lobby *are* on the inn’s amenity list.
- **Copyrighted property photos.** Not scraped.
- Cookie banner, a11y overlay, Duda “Add your custom HTML here” leaks — not copied.

## Issues fixed vs the live Duda brochure (kept from v1, restyled)

| Live gap | This demo |
| --- | --- |
| Homepage had no `tel:` / no phone digits in the hero | Sticky header Call + Book on every page; hero Call; chips include the number |
| Desk number easy to miss; conversion buried | Date bar → Book page → Cloudbeds; mobile sticky Call / Book |
| Duda placeholders (“Slide title”, “Button”, “Add your custom HTML here”) | None |
| Weak room presentation | Room rows with bed, occupancy, view, balcony/pet, closing Book + Call |
| Contact bleed risk / no dedicated contact | Book page is this NAP only |
| Cloudbeds as the only book path, unlabeled | Labeled external Cloudbeds + “call the desk” beside it |

## Serve

```
python -m http.server 8080
```

GitHub project Pages path: `/river-inn-at-seaside/`. Update `sitemap.xml` / `robots.txt` host if the Pages origin is not `cjessup.github.io`.
