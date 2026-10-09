# Public demo notes

The Nanjing handbook is adapted from an earlier Marco Polo trip example. Its dates, fares, opening hours, booking rules, and train times are historical example content, not current travel advice. Accommodation is represented by an area reference point, and no booking is made by opening this demo.

## Map

The planning skill uses Amap to research locations and transport. This public website uses **MapLibre GL JS 5.6.0** and **OpenFreeMap** (OpenStreetMap data) so visitors do not need an API key and no private Amap configuration is published.

The example's Amap coordinates are GCJ-02. The display converts them to WGS84 before drawing them on the OSM map. Lines connect visits in order; they are not surveyed paths or turn-by-turn navigation. The original template in `assets/amap-html-template/` remains the Amap template used by the skill.

MapLibre is distributed under its [BSD 3-Clause license](vendor/maplibre/LICENSE.txt). OpenFreeMap provides the public basemap without registration or API keys: https://openfreemap.org/. Keep attribution to OpenFreeMap, OpenMapTiles, and OpenStreetMap contributors visible. Map data licensing: https://www.openstreetmap.org/copyright.

## Images

The food and city pages retain their original remote image URLs and source links. Those third-party photographs remain subject to their owners' rights; the project's code license, if present, does not grant rights to them. Remote images may be unavailable, in which case the pages display a visual fallback.

The README screenshots show the original Amap version. The public demo preserves its layout and trip content while using a different basemap for public access.

## Deployment

Run `python3 scripts/build_site.py` to assemble only the public site in `_site/`. It copies `docs/` plus the four existing showcase images from `assets/`, avoiding a second tracked copy of the screenshots. It also builds `downloads/marco-polo.zip` from the explicit runtime file list in `scripts/package_skill.py`. The Pages workflow validates PRs and deploys only from `main`; changes to the skill and its bundled resources refresh the install package.

Keep private configuration, orders, raw trip folders, and local credentials out of this directory.
