#!/usr/bin/env python3
"""Package only the files needed to use Marco Polo, using the standard library."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/outputs.md",
    "assets/amap-html-template/map.html",
    "assets/amap-html-template/config.local.example.js",
)


def package_skill(destination=None):
    destination = Path(destination) if destination else ROOT / "_site/downloads/marco-polo.zip"
    contents = {}
    for name in FILES:
        source = ROOT / name
        if source.is_symlink() or not source.resolve().is_relative_to(ROOT):
            raise ValueError(f"Package source must be a regular repository file: {name}")
        contents[name] = source.read_bytes()

    # Catch references to files that would be missing after installation.
    for name, data in contents.items():
        if not name.endswith(".md"):
            continue
        for link in re.findall(r"\]\(([^\s)]+)\)", data.decode("utf-8")):
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (ROOT / name).parent / unquote(url.path)
            if not target.resolve().is_relative_to(ROOT):
                raise ValueError(f"Reference escapes the package: {name}: {link}")
            relative = target.resolve().relative_to(ROOT).as_posix()
            if relative not in contents:
                raise ValueError(f"Missing packaged reference: {name}: {link}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w") as archive:
        for name, data in contents.items():
            # Stable timestamps make the download reproducible across builds.
            entry = zipfile.ZipInfo("marco-polo/" + name)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise ValueError("Package integrity check failed")
    print(f"Packaged {len(contents)} skill files ({destination.stat().st_size:,} bytes): {destination}")
    return destination


if __name__ == "__main__":
    package_skill()
