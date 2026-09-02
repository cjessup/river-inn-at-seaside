# Build notes — River Inn at Seaside demo

Unattended first demo for WSR-52. Live brochure: https://www.riverinnatseaside.com/ (Duda). Live booking: https://hotels.cloudbeds.com/reservation/pVXpz4. The business was not contacted.

## Stack

Plain HTML / CSS / JS at folder root (GitHub Pages–ready at `/river-inn-at-seaside/`). Holiday Motel Bend v2 guidelines were a starting point (date bar, lodge type, compact chips, LodgingBusiness JSON-LD). No Astro: Cloudbeds is the real engine, so a fake inventory app would be the wrong delta. `_build_pages.py` stamps shared chrome.

Photos are original generated assets of a coastal river inn, not scraped from the live site. Logo/favicon are original SVG.

## Pages

Home, Rooms, Amenities (`amenities.html`), Seaside (`nearby.html`), About, Book/contact (`book.html`), Privacy, 404. Plus `.nojekyll`, `robots.txt`, `sitemap.xml`.

Relative asset paths. Sticky header Call + Book on every page (including homepage). Mobile bottom Call / Book. Viewport allows pinch zoom (`width=device-width, initial-scale=1, viewport-fit=cover`; no `user-scalable=0`).

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

## Facts omitted (on purpose)

- **Nightly room rates.** Not printed on the live brochure. Cloudbeds is the price path. No demo “from $X”.
- **Sister-property phone `(503) 738-9581`** and Inn at Seaside / SaltLine addresses. Never used.
- **`info@amadoka.com`** in the live header “Connect” block — Duda leftover. Desk email only.
- **Specific awards.** Live copy says “award-winning” without naming an award. Not restated as a verified trophy.
- **Guest review quotes** on the Duda homepage (attributed “Tripadvisor Guest”). Linked Tripadvisor/Yelp instead of copying quotes.
- **OTA-only extras** (Priceline/Kayak scores, “yoga mats in every room”, “cookie at check-in” from third-party blurbs) unless also on the inn’s own pages. Cookies in the lobby *are* on the inn’s amenity list.
- **Copyrighted property photos.** Not scraped.

## Issues fixed vs the live Duda brochure

| Live gap | This demo |
| --- | --- |
| Homepage had no `tel:` / no phone digits in the hero | Sticky header Call + Book on every page; hero Call; chips include the number |
| Desk number easy to miss; conversion buried | Date bar → Book page → Cloudbeds; mobile sticky Call / Book |
| Duda placeholders (“Slide title”, “Button”, “Add your custom HTML here”) | None |
| Weak room presentation | Room cards with bed, occupancy, view, balcony/pet, closing Book + Call |
| Contact bleed risk / no dedicated contact | Book page is this NAP only |
| Cloudbeds as the only book path, unlabeled | Labeled external Cloudbeds + “call the desk” beside it |

## Design

Tide / river / sunset motor-lodge palette (Necanicum + Prom, not Bend-forest clone and not luxury chrome). Fraunces + Outfit. Compact dark chips — no fat white bubbles. Large tap targets.

## Serve

```
python -m http.server 8080
```

GitHub project Pages path: `/river-inn-at-seaside/`. Update `sitemap.xml` / `robots.txt` host if the Pages origin is not `kestrelintegrations.github.io`.
