"""Playwright pass against the local static server."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SHOT = ROOT / "_shots"
SHOT.mkdir(exist_ok=True)
BASE = "http://127.0.0.1:8765"
PAGES = [
    "/",
    "/rooms.html",
    "/amenities.html",
    "/nearby.html",
    "/about.html",
    "/book.html",
    "/privacy.html",
    "/404.html",
]
TEL = "tel:+15037175744"
JS_BROKEN = """() => [...document.images]
  .filter(img => img.getAttribute('src') && (!img.complete || img.naturalWidth === 0))
  .map(img => img.src)"""


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        for path in PAGES:
            page.goto(BASE + path, wait_until="networkidle", timeout=30000)
            name = "home" if path == "/" else path.strip("/").replace(".html", "")
            page.screenshot(path=str(SHOT / f"desk-{name}.png"), full_page=True)
            vp = page.locator('meta[name="viewport"]').get_attribute("content") or ""
            tels = page.locator(f'a[href="{TEL}"]').count()
            header_call = page.locator(".header-actions a.tel").count()
            header_book = page.locator(".header-actions a.btn").count()
            broken = page.evaluate(JS_BROKEN)
            print(f"desktop {path}: title={page.title()!r} vp={vp!r} tel={tels} header={header_call}/{header_book} broken={broken}")
            assert "width=device-width" in vp
            assert "user-scalable=0" not in vp
            assert "user-scalable=no" not in vp
            assert tels >= 1
            assert header_call >= 1 and header_book >= 1
            assert not broken, broken
            html = page.content()
            assert "738-9581" not in html
            assert "amadoka" not in html.lower()
            assert "hotels.cloudbeds.com/reservation/pVXpz4" in html
            assert page.locator(".header-actions a.tel").is_visible()
            assert page.locator(".header-actions .btn").is_visible()

        page.set_viewport_size({"width": 390, "height": 844})
        for path in ["/", "/rooms.html", "/book.html", "/amenities.html"]:
            page.goto(BASE + path, wait_until="networkidle", timeout=30000)
            name = "home" if path == "/" else path.strip("/").replace(".html", "")
            page.screenshot(path=str(SHOT / f"mobile-{name}.png"), full_page=True)
            bar = page.locator(".mobile-cta")
            assert bar.is_visible(), path
            labels = [t.strip() for t in bar.locator("a").all_inner_texts()]
            print("mobile sticky", path, labels)
            assert labels == ["Call", "Book"], labels
            heights = bar.locator("a").evaluate_all(
                "els => els.map(e => e.getBoundingClientRect().height)"
            )
            print(" sticky heights", heights)
            assert all(h >= 44 for h in heights), heights
            assert page.locator(".header-actions a.tel").is_visible()
            assert page.locator(".header-actions .btn").is_visible()

        page.goto(BASE + "/", wait_until="networkidle")
        page.locator(".nav-toggle").click()
        assert page.locator("#site-nav").evaluate("el => el.classList.contains('is-open')")
        page.screenshot(path=str(SHOT / "mobile-menu.png"))
        page.locator('#site-nav a[href="rooms.html"]').click()
        page.wait_for_url("**/rooms.html")
        print("nav to rooms ok")
        assert page.locator(".room-card").count() >= 7
        page.locator(".room-card .btn").first.click()
        # Cloudbeds is external; don't wait on it — just confirm the href
        page.goto(BASE + "/rooms.html", wait_until="networkidle")
        href = page.locator(".room-card .btn").first.get_attribute("href")
        assert "cloudbeds.com/reservation/pVXpz4" in (href or "")
        print("room book href", href)

        page.goto(BASE + "/book.html?checkin=2026-09-10&checkout=2026-09-12&guests=2", wait_until="networkidle")
        recap = page.locator("[data-date-recap]").inner_text()
        print("date recap", recap)
        assert "2026-09-10" in recap
        page.locator("#name").fill("Test Guest")
        page.locator("#phone").fill("5037175744")
        page.locator("#email").fill("test@example.com")
        page.locator("#roomType").select_option("King River View")
        page.locator("#notes").fill("Pet on request, late arrival after 6.")
        page.locator('#hold-form button[type="submit"]').click()
        page.wait_for_selector("#hold-success.is-visible")
        page.screenshot(path=str(SHOT / "mobile-book-success.png"), full_page=True)
        print("hold form success")

        # date bar GET
        page.goto(BASE + "/", wait_until="networkidle")
        page.locator("#checkin").fill("2026-09-18")
        page.locator("#checkout").fill("2026-09-20")
        page.locator(".book-bar button[type='submit']").click()
        page.wait_for_url("**/book.html?**")
        print("date bar ->", page.url)
        assert "checkin=2026-09-18" in page.url

        browser.close()
        print("OK browser pass")


if __name__ == "__main__":
    main()
