#!/usr/bin/env python3
"""Build the credential-free Pages demo using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import shutil
from package_skill import package_skill

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"src", "href", "data-page"} and value:
                self.links.append(value)


def build():
    if OUTPUT.is_symlink():
        raise SystemExit("Refusing to replace a symlink at _site")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(ROOT / "docs", OUTPUT)
    assets = OUTPUT / "assets"
    assets.mkdir(exist_ok=True)
    for name in ["demo-map.png", "demo-handbook.jpg", "demo-food.jpg", "demo-city.jpg"]:
        shutil.copy2(ROOT / "assets" / name, assets / name)
    package_skill(OUTPUT / "downloads/marco-polo.zip")

    errors = []
    for file in OUTPUT.rglob("*"):
        if not file.is_file():
            continue
        relative = file.relative_to(OUTPUT)
        if file.name.startswith(".env") or file.name in {"config.local.js", "config.json"}:
            errors.append(f"Private configuration in output: {relative}")
        if file.suffix in {".html", ".js", ".json", ".md"} and "vendor" not in relative.parts:
            text = file.read_text(encoding="utf-8")
            if re.search(r"\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,})\b", text):
                errors.append(f"Possible credential in {relative}")
            if re.search(r"(?:jsapiKey|securityJsCode|webServiceKey)\s*:\s*['\"][^'\"]+", text):
                errors.append(f"Map credential in {relative}")
        if file.suffix != ".html":
            continue
        parser = LocalLinks()
        parser.feed(file.read_text(encoding="utf-8"))
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            # Relative URLs must work below /marco-polo.skill/ on GitHub Pages.
            if url.path.startswith("/"):
                errors.append(f"Domain-root URL in {relative}: {link}")
                continue
            target = (file.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(OUTPUT.resolve()):
                errors.append(f"Link escapes site in {relative}: {link}")
            elif not target.exists():
                errors.append(f"Missing local target in {relative}: {link}")
    if errors:
        raise SystemExit("\n".join(errors))
    count = sum(1 for path in OUTPUT.rglob("*") if path.is_file())
    print(f"Built {count} public files in {OUTPUT}; local links and configuration checks passed.")


if __name__ == "__main__":
    build()
