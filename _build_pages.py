#!/usr/bin/env python3
"""Write the River Inn at Seaside static pages with shared chrome."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

CLOUDBEDS = "https://hotels.cloudbeds.com/reservation/pVXpz4"
TEL = "tel:+15037175744"
PHONE = "(503) 717-5744"
EMAIL = "info@riverinnatseaside.com"
ADDRESS = "531 Avenue A, Seaside, OR 97138"
MAPS = "https://www.google.com/maps/search/?api=1&query=River+Inn+at+Seaside+531+Avenue+A+Seaside+OR+97138"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=531+Avenue+A,+Seaside,+OR+97138"
EMBED = "https://maps.google.com/maps?q=531+Avenue+A,+Seaside,+OR+97138&output=embed"
TRIPADVISOR = "https://www.tripadvisor.com/Hotel_Review-g52061-d6485212-Reviews-River_Inn_at_Seaside-Seaside_Oregon.html"
YELP = "https://www.yelp.com/biz/river-inn-at-seaside-seaside"
INSTAGRAM = "https://instagram.com/riverinnatseaside/"
FACEBOOK = "https://facebook.com/RiverInnatSeaside"
LIVE = "https://www.riverinnatseaside.com/"
PAGES = "https://kestrelintegrations.github.io/river-inn-at-seaside"
SEASIDEOR = "https://www.seasideor.com/"

RID = {
    "king": "461415",
    "king-river": "461418",
    "ada": "461420",
    "queens": "461422",
    "queens-river": "461424",
    "king-suite": "461426",
    "queen-suite": "461428",
}

NAV = [
    ("index.html", "Home"),
    ("rooms.html", "Rooms"),
    ("amenities.html", "Stay"),
    ("nearby.html", "Seaside"),
    ("about.html", "About"),
    ("book.html", "Book"),
]


def cb(rid=None):
    if rid:
        return f"{CLOUDBEDS}?rid={RID[rid]}"
    return CLOUDBEDS


def json_ld():
    return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LodgingBusiness",
    "name": "River Inn at Seaside",
    "description": "Independent 48-room inn on the Necanicum River at 531 Avenue A, Seaside, Oregon. One block from downtown, two blocks from the beach. Indoor saltwater pool and spa, complimentary breakfast, 24-hour front desk.",
    "url": "{LIVE}",
    "telephone": "+15037175744",
    "email": "{EMAIL}",
    "image": "{PAGES}/assets/hero.jpg",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "531 Avenue A",
      "addressLocality": "Seaside",
      "addressRegion": "OR",
      "postalCode": "97138",
      "addressCountry": "US"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 45.99213791,
      "longitude": -123.92525482
    }},
    "checkinTime": "16:00",
    "checkoutTime": "12:00",
    "petsAllowed": true,
    "amenityFeature": [
      {{"@type": "LocationFeatureSpecification", "name": "Indoor saltwater pool and spa"}},
      {{"@type": "LocationFeatureSpecification", "name": "Complimentary deluxe continental breakfast"}},
      {{"@type": "LocationFeatureSpecification", "name": "Free Wi-Fi"}},
      {{"@type": "LocationFeatureSpecification", "name": "Free on-site parking"}},
      {{"@type": "LocationFeatureSpecification", "name": "24-hour front desk"}},
      {{"@type": "LocationFeatureSpecification", "name": "Ready-to-borrow bikes"}},
      {{"@type": "LocationFeatureSpecification", "name": "Fitness center"}},
      {{"@type": "LocationFeatureSpecification", "name": "Electric vehicle charging station"}}
    ],
    "sameAs": [
      "{TRIPADVISOR}",
      "{YELP}",
      "{INSTAGRAM}",
      "{FACEBOOK}",
      "{CLOUDBEDS}"
    ]
  }}
  </script>"""


def head(title, description, path, extra=""):
    slug = "" if path == "index.html" else path
    canonical = f"{PAGES}/{slug}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#16343c">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{PAGES}/assets/hero.jpg">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;700&amp;family=Outfit:wght@400;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
{json_ld()}
{extra}</head>
"""


def header(active):
    links = []
    for href, label in NAV:
        cls = ' class="is-active"' if href == active else ""
        links.append(f'        <a href="{href}"{cls}>{label}</a>')
    nav = "\n".join(links)
    return f"""<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="util-bar">
    <div class="wrap">
      <span>48 rooms · Necanicum River · 2 blocks to the Prom</span>
      <span>Desk 24/7 · In 4:00 PM · Out 12:00 PM · <a href="{TEL}">{PHONE}</a></span>
    </div>
  </div>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="logo" href="index.html">
        <img src="assets/logo.svg" alt="">
        <span class="logo-text">
          <strong>River Inn</strong>
          <span>at Seaside</span>
        </span>
      </a>
      <nav id="site-nav" class="site-nav" aria-label="Primary">
{nav}
      </nav>
      <div class="header-actions">
        <a class="tel" href="{TEL}"><span>{PHONE}</span></a>
        <a class="btn" href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Book</a>
      </div>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
  </header>
  <div class="book-bar">
    <form class="wrap" action="book.html" method="get">
      <div>
        <label for="checkin">Check-in</label>
        <input id="checkin" name="checkin" type="date" required>
      </div>
      <div>
        <label for="checkout">Check-out</label>
        <input id="checkout" name="checkout" type="date" required>
      </div>
      <div>
        <label for="guests">Guests</label>
        <select id="guests" name="guests">
          <option value="1">1</option>
          <option value="2" selected>2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
        </select>
      </div>
      <button class="btn" type="submit">Check availability</button>
    </form>
  </div>
"""


def footer():
    return f"""  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <h2>River Inn at Seaside</h2>
        <div class="nap">
          <span>531 Avenue A</span>
          <span>Seaside, OR 97138</span>
          <a href="{TEL}">{PHONE}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
        <p class="note">Front desk open 24/7. Check-in 4:00 PM. Check-out 12:00 PM. This property only — no sister hotels on this page.</p>
      </div>
      <div>
        <h2>Stay</h2>
        <div class="footer-links">
          <a href="rooms.html">Rooms</a>
          <a href="amenities.html">Amenities</a>
          <a href="nearby.html">Seaside</a>
          <a href="about.html">About</a>
          <a href="book.html">Book / Contact</a>
          <a href="privacy.html">Privacy</a>
        </div>
      </div>
      <div>
        <h2>Book</h2>
        <p>Live rates and inventory are on Cloudbeds. Call the desk if you want help choosing a room.</p>
        <div class="footer-links">
          <a href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Cloudbeds</a>
          <a href="{DIRS}" rel="noopener noreferrer" target="_blank">Directions</a>
          <a href="{TRIPADVISOR}" rel="noopener noreferrer" target="_blank">Tripadvisor</a>
          <a href="{YELP}" rel="noopener noreferrer" target="_blank">Yelp</a>
        </div>
      </div>
    </div>
    <div class="wrap fine">
      <p>© <span data-year></span> River Inn at Seaside. Demo brochure — original generated photos, not the inn’s camera roll. <a href="{LIVE}" rel="noopener noreferrer">Live site</a>.</p>
    </div>
  </footer>
  <div class="mobile-cta" aria-label="Call or book">
    <a class="ghost" href="{TEL}">Call</a>
    <a href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Book</a>
  </div>
  <script src="js/main.js"></script>
</body>
</html>
"""


def room_card(title, img, alt, tags, blurb, rid, extra_class=""):
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""        <article class="room-card{extra_class}">
          <img src="assets/{img}" alt="{alt}">
          <div>
            <h3>{title}</h3>
            <div class="room-meta">{tags_html}</div>
            <p>{blurb}</p>
            <div class="room-actions">
              <a class="btn" href="{cb(rid)}" rel="noopener noreferrer" target="_blank">Book</a>
              <a class="btn btn-outline" href="{TEL}">Call</a>
            </div>
          </div>
        </article>
"""


ROOMS_ALL = [
    room_card(
        "King",
        "room-king.jpg",
        "King guest room with sofa sleeper, microwave, and mini fridge",
        ["1 King + queen sofa sleeper", "Sleeps 4", "City-side", "Pets on request"],
        "King bed, queen-sized sofa sleeper, single-pod coffee maker, snack-size refrigerator, and microwave. 100% non-smoking.",
        "king",
    ),
    room_card(
        "King River View",
        "room-king-river.jpg",
        "King room with sofa sleeper and balcony over a tidal river",
        ["1 King + queen sofa sleeper", "Sleeps 4", "River balcony", "Pets on request"],
        "King bed, queen sofa sleeper, Keurig, snack fridge, microwave, and a private balcony overlooking the Necanicum River.",
        "king-river",
    ),
    room_card(
        "Two Queens",
        "room-queens.jpg",
        "Guest room with two queen beds",
        ["2 Queen beds", "Sleeps 4", "City-side", "Pets on request"],
        "Two queen beds, coffee maker, snack-size refrigerator, and microwave. Cribs upon request and availability.",
        "queens",
    ),
    room_card(
        "Two Queens River View",
        "room-queens-river.jpg",
        "Two queen beds with a river-view balcony",
        ["2 Queen beds", "Sleeps 4", "River balcony", "Pets on request"],
        "Two queen beds, Keurig, snack fridge, microwave, and a private balcony overlooking the Necanicum River.",
        "queens-river",
    ),
    room_card(
        "Queen River View Accessible",
        "room-ada.jpg",
        "Accessible queen room with walk-in shower and river balcony",
        ["1 Queen", "ADA", "Walk-in shower", "River balcony"],
        "Wheelchair-accessible queen room with a walk-in shower, Keurig, snack fridge, microwave, and a private balcony over the river.",
        "ada",
    ),
    room_card(
        "Two Queen Suite River View",
        "suite.jpg",
        "One-bedroom suite with kitchenette, sofa sleeper, and river balcony",
        ["2 Queens + sofa sleeper", "Sleeps 6", "Full kitchen", "2 river balconies"],
        "Two queen beds in the bedroom, queen sofa sleeper in the living area, full kitchen, table for three to four, and two private balconies over the Necanicum River.",
        "queen-suite",
    ),
    room_card(
        "King Suite River View",
        "suite.jpg",
        "One-bedroom king suite with kitchenette and river balconies",
        ["1 King + 2 sofa sleepers", "Sleeps 6", "Full kitchen", "2 river balconies"],
        "King bed in the bedroom, two queen sofa sleepers, full kitchen, table for three to four, and two private balconies overlooking the river.",
        "king-suite",
    ),
]


def write(name, html):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


def index():
    featured = "".join(ROOMS_ALL[i] for i in (1, 3, 4, 5))
    return (
        head(
            "River Inn at Seaside | Necanicum River, two blocks from the Prom",
            "48-room inn at 531 Avenue A, Seaside, OR. Indoor saltwater pool, complimentary breakfast, 24/7 desk. Call (503) 717-5744 or book on Cloudbeds.",
            "index.html",
        )
        + header("index.html")
        + f"""  <main id="main">
    <section class="hero">
      <img class="hero-bg" src="assets/hero.jpg" alt="Dusk view of a shingled coastal inn beside a tidal river">
      <div class="hero-overlay"></div>
      <div class="wrap hero-copy">
        <p class="kicker">531 Avenue A · Seaside, Oregon</p>
        <h1>48 rooms on the Necanicum River, two blocks from the beach.</h1>
        <p>Independent inn one block from downtown Seaside. Indoor saltwater pool and spa, complimentary breakfast, bikes to borrow, and a 24/7 desk. Book live rooms on Cloudbeds, or call {PHONE}.</p>
        <div class="hero-actions">
          <a class="btn" href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Book on Cloudbeds</a>
          <a class="btn btn-ghost hero-call" href="{TEL}">Call {PHONE}</a>
          <a class="btn btn-ghost" href="{DIRS}" rel="noopener noreferrer" target="_blank">Directions</a>
        </div>
      </div>
    </section>
    <div class="wrap">
      <ul class="chips">
        <li><strong>48</strong> <span>rooms &amp; suites</span></li>
        <li><strong>Pool</strong> <span>&amp; spa</span></li>
        <li><strong>Breakfast</strong> <span>included</span></li>
        <li><strong>2 blocks</strong> <span>to the Prom</span></li>
        <li><strong>24/7</strong> <span>desk</span></li>
        <li><a href="{TEL}"><strong>Call</strong> <span>{PHONE}</span></a></li>
      </ul>
    </div>
    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">The stay</p>
          <h2>River on one side. Town and sand on the other.</h2>
          <p class="lede">River Inn at Seaside sits along the Necanicum River. Downtown is one block. The beach and the 1.5-mile Promenade are two blocks. Rooms run city-side or river-view, with suites that sleep up to six.</p>
          <p>Complimentary deluxe continental breakfast, freshly baked cookies in the lobby each afternoon, and a saltwater indoor heated pool and spa. Pets are welcome in guest rooms on request — nightly pet fee applies.</p>
          <div class="cta-row">
            <a class="btn" href="rooms.html">See rooms</a>
            <a class="btn btn-outline" href="amenities.html">Amenities</a>
          </div>
        </div>
        <img src="assets/pool.jpg" alt="Indoor saltwater pool and spa with coastal windows">
      </div>
    </section>
    <section class="section alt">
      <div class="wrap">
        <p class="eyebrow">Rooms</p>
        <h2>Pick a bed, a view, then Book or Call.</h2>
        <p class="lede">Bed type, occupancy, river or city-side, balcony and pet notes as printed on the inn’s rooms page and Cloudbeds listing. This demo does not quote a nightly rate — Cloudbeds is the live inventory.</p>
        <div class="room-grid">
{featured}        </div>
        <div class="cta-row">
          <a class="btn btn-outline" href="rooms.html">All room types</a>
        </div>
      </div>
    </section>
    <section class="section dark">
      <div class="wrap">
        <p class="eyebrow">Book direct</p>
        <h2>Cloudbeds for dates. Desk for questions.</h2>
        <p class="lede">Check availability on Cloudbeds. Call {PHONE} if you want a river-view, an accessible room, a pet room, or a group of 10 or more. This site does not invent a price.</p>
        <div class="cta-row">
          <a class="btn" href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Open Cloudbeds</a>
          <a class="btn btn-ghost" href="{TEL}">Call the desk</a>
          <a class="btn btn-ghost" href="book.html">Hold / contact</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <img src="assets/prom.jpg" alt="Wooden beach promenade along a wide sandy Oregon coast">
        <div>
          <p class="eyebrow">Place</p>
          <h2>Walk to the Prom. Bike the town.</h2>
          <p>Seaside is a walkable Oregon-coast town: carousel mall, aquarium, outlets, and a long sandy beach. The inn lists complimentary bikes to borrow. Cannon Beach is about 12 miles south; Astoria about 25 miles north.</p>
          <div class="miles">
            <div class="mile"><span>Downtown Seaside</span><strong>1 block</strong></div>
            <div class="mile"><span>Beach / Promenade</span><strong>2 blocks</strong></div>
            <div class="mile"><span>Seaside Carousel Mall</span><strong>walk</strong></div>
            <div class="mile"><span>Seaside Aquarium</span><strong>walk</strong></div>
          </div>
          <div class="cta-row">
            <a class="btn btn-outline" href="nearby.html">Area guide</a>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def rooms():
    cards = "".join(ROOMS_ALL)
    return (
        head(
            "Rooms | River Inn at Seaside",
            "King, two queens, accessible queen, and river-view suites. Sleeps 4 to 6. Book on Cloudbeds or call (503) 717-5744.",
            "rooms.html",
        )
        + header("rooms.html")
        + f"""  <main id="main">
    <header class="page-hero rooms">
      <div class="wrap">
        <p class="kicker">48 rooms &amp; suites</p>
        <h1>City-side or river balcony. Suites sleep six.</h1>
        <p>Facts from the inn’s rooms page and the public Cloudbeds listing. No invented rates.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <ul class="chips">
          <li><strong>King</strong> <span>+ sofa</span></li>
          <li><strong>2 Queens</strong></li>
          <li><strong>ADA</strong> <span>queen</span></li>
          <li><strong>Suites</strong> <span>kitchen</span></li>
          <li><strong>Pets</strong> <span>on request</span></li>
        </ul>
        <p class="lede">Every listed room includes air conditioning, heater, work desk, iron, free Wi-Fi, DVD player with complimentary rentals, flat-screen cable TV, hair dryer, coffee maker, snack fridge, and microwave. Property is 100% non-smoking. Cribs upon request and availability. Pet-friendly upon request with an additional fee.</p>
        <div class="room-grid">
{cards}        </div>
        <p class="note">Cloudbeds room links open the inn’s live booking engine. Occupancy: standard rooms sleep 4; river-view suites sleep up to 6 (printed on the rooms page and Cloudbeds).</p>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def amenities():
    return (
        head(
            "Amenities | River Inn at Seaside",
            "Indoor saltwater pool and spa, complimentary breakfast, bikes, playground, game room, fitness room, EV charging, 24/7 lobby. Pets on request.",
            "amenities.html",
        )
        + header("amenities.html")
        + f"""  <main id="main">
    <header class="page-hero stay">
      <div class="wrap">
        <p class="kicker">On site</p>
        <h1>Pool, breakfast, bikes, and a 24-hour lobby.</h1>
        <p>Copied from the inn’s printed amenity list — nothing added from OTAs.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <ul class="chips">
          <li><strong>Saltwater</strong> <span>pool &amp; spa</span></li>
          <li><strong>Breakfast</strong></li>
          <li><strong>Bikes</strong></li>
          <li><strong>Playground</strong></li>
          <li><strong>EV</strong> <span>charging</span></li>
        </ul>
        <div class="feature-grid">
          <article class="feature">
            <img src="assets/pool.jpg" alt="Indoor pool and spa">
            <div>
              <h3>Indoor saltwater pool &amp; spa</h3>
              <p>Heated indoor saltwater pool and spa, listed on the inn’s amenities page.</p>
            </div>
          </article>
          <article class="feature">
            <img src="assets/breakfast.jpg" alt="Continental breakfast table">
            <div>
              <h3>Complimentary breakfast</h3>
              <p>Deluxe continental breakfast, plus freshly baked cookies each afternoon in the lobby.</p>
            </div>
          </article>
          <article class="feature">
            <img src="assets/bikes.jpg" alt="Cruiser bikes parked beside a river inn">
            <div>
              <h3>Ready-to-borrow bikes</h3>
              <p>Complimentary bikes to borrow for town and Prom rides.</p>
            </div>
          </article>
          <article class="feature">
            <img src="assets/playground.jpg" alt="Fenced playground beside marsh grass">
            <div>
              <h3>Fenced playground</h3>
              <p>Fenced kids’ playground and patio, plus an indoor game room.</p>
            </div>
          </article>
          <article class="feature">
            <img src="assets/firepit.jpg" alt="Stone fire pit with Adirondack chairs">
            <div>
              <h3>On-site fire pits</h3>
              <p>Outdoor fire pits for evening sit-downs. S’mores kits are a paid add-on with 24-hour notice.</p>
            </div>
          </article>
          <article class="feature">
            <img src="assets/lobby.jpg" alt="Small inn lobby with a plate of cookies">
            <div>
              <h3>24-hour lobby</h3>
              <p>Front desk open 24/7. Business center with printing. Complimentary DVDs to borrow.</p>
            </div>
          </article>
        </div>
        <h2>Hotel amenities</h2>
        <ul class="amenity-grid">
          <li>Complimentary deluxe continental breakfast</li>
          <li>Saltwater indoor heated pool &amp; spa</li>
          <li>On-site fitness center</li>
          <li>24-hour lobby</li>
          <li>Complimentary Wi-Fi</li>
          <li>Free on-site parking</li>
          <li>Ready-to-borrow bikes</li>
          <li>Fenced kids’ playground</li>
          <li>Indoor game room</li>
          <li>Coin laundry</li>
          <li>On-site fire pits</li>
          <li>24-hour business center with printing</li>
          <li>Complimentary DVDs to borrow</li>
          <li>Freshly baked cookies each afternoon</li>
          <li>Pet-friendly rooms (additional fee)</li>
          <li>On-site EV charging station</li>
          <li>Elevator (Cloudbeds listing)</li>
          <li>Table tennis / ping pong (Cloudbeds listing)</li>
        </ul>
        <div class="callout">
          <p><strong>Pets:</strong> Guest rooms are pet-friendly upon request. The inn’s packages page lists <strong>$25 per pet, per night</strong>, with a welcome bag (water dish, bags, treats, pet sheet and towel). Call ahead so the desk can set it up.</p>
        </div>
        <div class="cta-row">
          <a class="btn" href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Book on Cloudbeds</a>
          <a class="btn btn-outline" href="{TEL}">Call {PHONE}</a>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def nearby():
    return (
        head(
            "Seaside | River Inn at Seaside",
            "One block from downtown Seaside, two blocks from the Promenade and beach. Carousel mall, aquarium, outlets, Cannon Beach and Astoria day trips.",
            "nearby.html",
        )
        + header("nearby.html")
        + f"""  <main id="main">
    <header class="page-hero">
      <div class="wrap">
        <p class="kicker">Seaside, Oregon</p>
        <h1>Prom, river, and a walkable downtown.</h1>
        <p>Distances below are from the inn’s own destination page.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">From the door</p>
          <h2>Two blocks to sand. One block to Broadway.</h2>
          <p>The inn is at 531 Avenue A, along the Necanicum River. Seaside’s 1.5-mile Promenade, Miss Oregon Pageant, and 4th of July fireworks are the town’s printed calling cards. Portland is listed as about 90 minutes inland.</p>
          <div class="miles">
            <div class="mile"><span>Downtown / Broadway</span><strong>1 block</strong></div>
            <div class="mile"><span>Beach &amp; Promenade</span><strong>2 blocks</strong></div>
            <div class="mile"><span>Seaside Carousel Mall</span><strong>walk</strong></div>
            <div class="mile"><span>Seaside Aquarium</span><strong>walk</strong></div>
            <div class="mile"><span>Factory Outlet Center</span><strong>short drive</strong></div>
            <div class="mile"><span>Cannon Beach</span><strong>12 mi S</strong></div>
            <div class="mile"><span>Warrenton</span><strong>12 mi N</strong></div>
            <div class="mile"><span>Astoria</span><strong>25 mi N</strong></div>
          </div>
        </div>
        <img src="assets/prom.jpg" alt="Seaside-style wooden promenade beside the Pacific">
      </div>
    </section>
    <section class="section alt">
      <div class="wrap">
        <h2>Printed nearby list</h2>
        <p class="lede">From the inn’s destination page. We did not add sister properties or invented walk times.</p>
        <ul class="rules">
          <li>Seaside Carousel Mall — 300 Broadway St</li>
          <li>Seaside Aquarium — 200 North Promenade</li>
          <li>Turnaround at Seaside — 1 Broadway St</li>
          <li>Seaside Civic &amp; Convention Center — 415 First Avenue</li>
          <li>Seaside Factory Outlet Center — 1111 N Roosevelt Dr (listed open 10:00 AM–6:00 PM; stores may vary)</li>
          <li>Seaside Antique Mall — 726 Broadway St</li>
          <li>Funland Entertainment — 201 Broadway St</li>
          <li>Seaside Inverted — 111 Broadway St</li>
          <li>Tillamook Head Traverse / Indian Beach Trailhead</li>
          <li>Camp 18 Museum — 42362 Highway 26</li>
          <li>Ecola State Park — Cannon Beach</li>
        </ul>
        <h3>Restaurants the inn lists nearby</h3>
        <ul class="rules">
          <li>Beach N’ Brew — 405 Avenue A</li>
          <li>Doogers Seafood &amp; Grill — 505 Broadway St</li>
          <li>Dundee’s Donuts — 418 Broadway St</li>
          <li>Fultano’s Pizza Seaside — 215 Broadway St</li>
        </ul>
        <p><a href="{SEASIDEOR}" rel="noopener noreferrer" target="_blank">Seaside visitor guide</a></p>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def about():
    return (
        head(
            "About | River Inn at Seaside",
            "48-room inn on the Necanicum River. Groups of 10+, Necanicum meeting room, and printed stay packages. Call (503) 717-5744.",
            "about.html",
        )
        + header("about.html")
        + f"""  <main id="main">
    <header class="page-hero about">
      <div class="wrap">
        <p class="kicker">This property only</p>
        <h1>A 48-room inn on Avenue A — not a boutique collection.</h1>
        <p>531 Avenue A, Seaside, OR 97138. Desk {PHONE}.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap prose">
        <p class="eyebrow">Place</p>
        <h2>River, town, and overnight demand on the Prom.</h2>
        <p>River Inn at Seaside is an independent lodging property with 48 rooms and suites. The inn’s own copy places it along the Necanicum River, one block from downtown and two blocks from the beach. Contact on this demo is 531 Avenue A and (503) 717-5744 only.</p>
        <p>The live brochure still shows unfinished placeholder blocks and sends booking out to Cloudbeds. This rebuild keeps Cloudbeds as the live engine and puts Call + Book on every page, including the homepage.</p>
        <p>Photos on this demo are original generated images of a coastal river inn, not scraped from the property.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="wrap">
        <p class="eyebrow">Groups</p>
        <h2>Ten rooms or more. Small meeting space.</h2>
        <p class="lede">The inn offers group rates year-round for reunions, company gatherings, and similar stays. Call {PHONE} or email {EMAIL}.</p>
        <ul class="rules">
          <li><strong>Necanicum meeting space</strong> — 315 sq. ft., capacity 25–30 guests.</li>
          <li>Projector and screen upon request, table and chair set-up, wall-mounted TV, coffee and tea. Outside catering welcomed.</li>
          <li>Looking for 10 rooms or more? You may qualify for group rates.</li>
        </ul>
        <div class="cta-row">
          <a class="btn" href="book.html">Request a hold</a>
          <a class="btn btn-outline" href="{TEL}">Call groups</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <p class="eyebrow">Packages</p>
        <h2>Add-ons printed on the specials page</h2>
        <p class="note">Provide 24 hours’ advance notice for package add-ons.</p>
        <div class="pkg"><strong>S’mores package — $15</strong><span>Kit for 4 (makes 8 s’mores): marshmallows, chocolate, graham crackers, roasting sticks.</span></div>
        <div class="pkg"><strong>Birthday package — $30</strong><span>Banner, candy-filled water bottle, saltwater taffy, towel elephant on the bed.</span></div>
        <div class="pkg"><strong>Romance package — $40</strong><span>Sparkling cider, rose petals, chocolate truffles, late checkout 1:00 PM, towel swans.</span></div>
        <div class="pkg"><strong>Pet stay — $25 per pet, per night</strong><span>Reusable bag with water dish, bags, treats, pet sheet and towel for the stay.</span></div>
        <p class="note">Gift cards are offered on the live site. Room night rates are not printed there; use Cloudbeds.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="wrap prose">
        <h2>House notes (from Terms)</h2>
        <ul class="rules">
          <li>Check-in 4:00 PM · Check-out 12:00 PM. Front desk open 24/7.</li>
          <li>Cancellation: 48 hours (by 4:00 PM two days before arrival). Inside 48 hours, a fee totaling the full booking may apply. Third-party reservations follow that site’s rules.</li>
          <li>The stay is charged the morning of scheduled arrival. Tell the hotel if you will arrive after 6:00 PM.</li>
          <li>Guests must be 18 or older to check in. Photo ID matching the payment card is required.</li>
          <li>One complementary parking pass per reservation, except rooms with occupancy of 6 or more. Extra vehicles park off site.</li>
        </ul>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def book():
    return (
        head(
            "Book &amp; contact | River Inn at Seaside",
            "Book River Inn at Seaside on Cloudbeds or call (503) 717-5744. 531 Avenue A, Seaside, OR 97138. 24/7 desk.",
            "book.html",
        )
        + header("book.html")
        + f"""  <main id="main">
    <header class="page-hero book">
      <div class="wrap">
        <p class="kicker">Reservations</p>
        <h1>Check dates on Cloudbeds. Call the desk if you want a hand.</h1>
        <p>Live inventory is Cloudbeds. This page does not quote a nightly rate.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <p class="callout" data-date-recap>Use the date bar above, then open Cloudbeds for live availability. Call {PHONE} for river-view, ADA, pets, or groups.</p>
        <div class="cta-row">
          <a class="btn" data-cloudbeds href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Open Cloudbeds</a>
          <a class="btn btn-outline" href="{TEL}">Call {PHONE}</a>
        </div>
        <p class="note">Direct-book path is the inn’s Cloudbeds engine (<code>hotels.cloudbeds.com/reservation/pVXpz4</code>). A hold form below is a message to the desk, not a confirmed reservation.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="wrap split">
        <div>
          <p class="eyebrow">This property only</p>
          <h2>531 Avenue A</h2>
          <div class="nap">
            <strong>River Inn at Seaside</strong>
            <span>531 Avenue A</span>
            <span>Seaside, OR 97138</span>
            <a href="{TEL}">{PHONE}</a>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
          <ul class="rules">
            <li>Front desk open 24/7</li>
            <li>Check-in 4:00 PM · Check-out 12:00 PM</li>
            <li>Advise the desk if arriving after 6:00 PM</li>
            <li>18+ to check in · photo ID matching the card</li>
          </ul>
          <div class="cta-row">
            <a class="btn btn-outline" href="{DIRS}" rel="noopener noreferrer" target="_blank">Directions</a>
            <a class="btn btn-outline" href="{MAPS}" rel="noopener noreferrer" target="_blank">Map</a>
          </div>
        </div>
        <iframe class="map-frame" title="Map of River Inn at Seaside" src="{EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Ask the desk to hold dates</h2>
        <p class="lede">Saved on this device only. You still need to call {PHONE} or finish on Cloudbeds to confirm.</p>
        <form id="hold-form" class="form-grid" novalidate>
          <div class="field">
            <label for="name">Name</label>
            <input id="name" name="name" autocomplete="name" required>
            <div class="field-error"></div>
          </div>
          <div class="field">
            <label for="phone">Phone</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" required>
            <div class="field-error"></div>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
            <div class="field-error"></div>
          </div>
          <div class="field">
            <label for="roomType">Room</label>
            <select id="roomType" name="roomType">
              <option value="">No preference</option>
              <option value="King">King</option>
              <option value="King River View">King River View</option>
              <option value="Two Queens">Two Queens</option>
              <option value="Two Queens River View">Two Queens River View</option>
              <option value="Queen River View Accessible">Queen River View Accessible</option>
              <option value="Two Queen Suite River View">Two Queen Suite River View</option>
              <option value="King Suite River View">King Suite River View</option>
            </select>
          </div>
          <div class="field">
            <label for="notes">Notes (pets, group, late arrival)</label>
            <textarea id="notes" name="notes"></textarea>
          </div>
          <button class="btn" type="submit">Send hold request</button>
        </form>
        <div id="hold-success" class="success">
          <p><strong>Request saved on this device.</strong></p>
          <p data-hold-recap></p>
          <div class="cta-row">
            <a class="btn" href="{TEL}">Call {PHONE} to confirm</a>
            <a class="btn btn-outline" data-cloudbeds href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Finish on Cloudbeds</a>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def privacy():
    return (
        head(
            "Privacy | River Inn at Seaside",
            "Privacy notes for this static demo of River Inn at Seaside.",
            "privacy.html",
        )
        + header("privacy.html")
        + f"""  <main id="main">
    <header class="page-hero">
      <div class="wrap">
        <h1>Privacy</h1>
        <p>This is a static brochure demo. It is not the inn’s live booking system.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap prose">
        <p>Reservations run on Cloudbeds at hotels.cloudbeds.com. This demo does not process payments.</p>
        <p>The hold form stores your name, phone, email, and dates in this browser’s localStorage only. Nothing is emailed to the inn from this page. Call {PHONE} or use Cloudbeds to actually book.</p>
        <p>Maps are loaded from Google when you open the Book page. Fonts load from Google Fonts.</p>
        <p>The inn’s own privacy statement is on the <a href="{LIVE}privacy" rel="noopener noreferrer">live site</a>.</p>
        <p>Contact for this property only: 531 Avenue A, Seaside, OR 97138 · <a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </div>
    </section>
  </main>
"""
        + footer()
    )


def four04():
    return (
        head(
            "Page not found | River Inn at Seaside",
            "That page is missing. Call (503) 717-5744 or book on Cloudbeds.",
            "404.html",
        )
        + header("404.html")
        + f"""  <main id="main">
    <header class="page-hero">
      <div class="wrap">
        <h1>That page washed out.</h1>
        <p>Use the menu, call the desk, or open Cloudbeds.</p>
        <div class="cta-row">
          <a class="btn" href="index.html">Home</a>
          <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
          <a class="btn btn-ghost" href="{CLOUDBEDS}" rel="noopener noreferrer" target="_blank">Book</a>
        </div>
      </div>
    </header>
  </main>
"""
        + footer()
    )


def extras():
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /

Sitemap: {PAGES}/sitemap.xml
""",
        encoding="utf-8",
    )
    pages = [
        "",
        "rooms.html",
        "amenities.html",
        "nearby.html",
        "about.html",
        "book.html",
        "privacy.html",
    ]
    urls = "\n".join(
        f"  <url><loc>{PAGES}/{p}</loc></url>" for p in pages
    )
    (ROOT / "sitemap.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""",
        encoding="utf-8",
    )
    print("wrote extras")


if __name__ == "__main__":
    write("index.html", index())
    write("rooms.html", rooms())
    write("amenities.html", amenities())
    write("nearby.html", nearby())
    write("about.html", about())
    write("book.html", book())
    write("privacy.html", privacy())
    write("404.html", four04())
    extras()
