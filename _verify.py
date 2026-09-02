"""Static checks for the River Inn at Seaside demo. Not shipped."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).parent
HTML = list(ROOT.glob("*.html"))
TEL = "tel:+15037175744"
CLOUDBEDS = "https://hotels.cloudbeds.com/reservation/pVXpz4"
BANNED = (
    "738-9581",
    "738.9581",
    "amadoka",
    "saltline",
    "user-scalable=0",
    "user-scalable=no",
    "Slide title",
    "Add your custom HTML here",
    "Write your caption here",
)

ASSET_RE = re.compile(r"""(?:src|href)=["'](assets/[^"']+)["']""")


def main():
    errors = []
    for path in HTML:
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        if 'name="viewport"' not in text or "width=device-width" not in text:
            errors.append(f"{path.name}: missing/bad viewport")
        if "user-scalable=no" in low or "user-scalable=0" in low:
            errors.append(f"{path.name}: pinch zoom blocked")
        if TEL not in text:
            errors.append(f"{path.name}: missing desk tel")
        if CLOUDBEDS not in text:
            errors.append(f"{path.name}: missing Cloudbeds")
        for token in BANNED:
            if token.lower() in low:
                errors.append(f"{path.name}: banned token {token}")
        if 'href="/' in text or 'src="/' in text:
            errors.append(f"{path.name}: root-absolute path")
        if "LodgingBusiness" not in text:
            errors.append(f"{path.name}: missing JSON-LD")
        if 'class="mobile-cta"' not in text:
            errors.append(f"{path.name}: missing sticky bar")
        if "Call</a>" not in text or ">Book</a>" not in text:
            errors.append(f"{path.name}: missing Call/Book labels")
        if "header-actions" not in text or f'class="tel" href="{TEL}"' not in text:
            errors.append(f"{path.name}: header Call missing")
        if "531 Avenue A" not in text:
            errors.append(f"{path.name}: missing street NAP")
        m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', text, re.S)
        if m:
            try:
                data = json.loads(m.group(1))
            except json.JSONDecodeError as err:
                errors.append(f"{path.name}: JSON-LD parse {err}")
            else:
                if data.get("telephone") != "+15037175744":
                    errors.append(f"{path.name}: JSON-LD phone")
                addr = data.get("address") or {}
                if addr.get("streetAddress") != "531 Avenue A":
                    errors.append(f"{path.name}: JSON-LD street")
        for asset in ASSET_RE.findall(text):
            if not (ROOT / asset).exists():
                errors.append(f"{path.name}: missing {asset}")

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    if index.lower().count("tel:+15037175744") < 4:
        errors.append("index.html: too few homepage tel links")

    for required in (".nojekyll", "robots.txt", "sitemap.xml", "BUILD-NOTES.md", "css/styles.css", "js/main.js"):
        if not (ROOT / required).exists():
            errors.append(f"missing {required}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"OK {len(HTML)} html files, viewport+tel+Cloudbeds+JSON-LD+sticky+NAP")


if __name__ == "__main__":
    main()
