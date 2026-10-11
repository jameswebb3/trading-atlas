#!/usr/bin/env python3
"""Render the homepage banner and the at-a-glance chart as static SVG, in light and dark variants.

The SVGs are generated from catalog.json and explored.json so their numbers never drift from the index.
"""

from collections import Counter
from html import escape

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Surfaces match GitHub's light and dark canvases. The rating ramp is one blue hue (ordinal, validated
# with the dataviz palette script): darker = higher rating on light, lighter = higher rating on dark.
THEMES = {
    "light": {
        "surface": "#ffffff", "panel": "#f6f8fa", "rule": "#d1d9e0",
        "text": "#1f2328", "muted": "#59636e", "accent": "#2a78d6",
        "ramp": ("#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#0d366b"),
    },
    "dark": {
        "surface": "#0d1117", "panel": "#151b23", "rule": "#3d444d",
        "text": "#f0f6fc", "muted": "#9198a1", "accent": "#3987e5",
        "ramp": ("#256abf", "#3987e5", "#6da7ec", "#9ec5f4", "#cde2fb"),
    },
}


def _svg(width: int, height: int, title: str, body: list[str]) -> str:
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'role="img" aria-label="{escape(title)}" font-family="{FONT}">',
        f"<title>{escape(title)}</title>",
        *body,
        "</svg>",
        "",
    ])


def render_hero(data: dict, explored: dict, mode: str) -> str:
    t = THEMES[mode]
    reviews = data["reviews"]
    projects = explored["projects"]
    unrated = len(projects) - len(reviews)
    top = sum(item["rating"] >= 4 for item in reviews)
    stats = [
        (f"{len(reviews):,}", "source-backed reviews"),
        (f"{unrated:,}", "unrated projects"),
        (f"{len(projects):,}", "projects considered"),
        (f"{top}", "rated 4/5 or higher"),
        (f"{len(data['areas'])}", "coverage areas"),
    ]
    body = [
        f'<rect width="1200" height="380" rx="16" fill="{t["panel"]}"/>',
        f'<rect x="64" y="64" width="6" height="104" rx="3" fill="{t["accent"]}"/>',
        f'<text x="92" y="84" font-size="17" font-weight="600" letter-spacing="2.4" fill="{t["accent"]}">'
        "OPEN-SOURCE TRADING TOOLS, READ AT THE SOURCE</text>",
        f'<text x="90" y="138" font-size="54" font-weight="700" fill="{t["text"]}">Trading Systems Atlas</text>',
        f'<text x="92" y="203" font-size="17" font-weight="600" fill="{t["muted"]}">By James Webb 3</text>',
        f'<text x="92" y="174" font-size="23" fill="{t["muted"]}">'
        "What each project gets right, and the catch that costs money, down to the line of code.</text>",
        f'<line x1="64" y1="222" x2="1136" y2="222" stroke="{t["rule"]}" stroke-width="1"/>',
    ]
    column = (1136 - 64) / len(stats)
    for index, (value, label) in enumerate(stats):
        x = 64 + index * column + (18 if index else 0)
        if index:
            body.append(f'<line x1="{64 + index * column:.0f}" y1="250" x2="{64 + index * column:.0f}" y2="330" '
                        f'stroke="{t["rule"]}" stroke-width="1"/>')
        body += [
            f'<text x="{x:.0f}" y="296" font-size="45" font-weight="700" fill="{t["text"]}">{value}</text>',
            f'<text x="{x:.0f}" y="326" font-size="18" fill="{t["muted"]}">{escape(label)}</text>',
        ]
    return _svg(1200, 380, f"Trading Systems Atlas: {len(reviews):,} source-backed reviews, {unrated:,} unrated projects, {len(projects):,} considered", body)


def render_areas(data: dict, mode: str) -> str:
    t = THEMES[mode]
    ratings = sorted({item["rating"] for item in data["reviews"]})
    counts = {area["slug"]: Counter(item["rating"] for item in data["reviews"] if item["primary_area"] == area["slug"])
              for area in data["areas"]}
    biggest = max(sum(c.values()) for c in counts.values())
    left, right, top, row = 360, 1140, 84, 48
    scale = (right - 60 - left) / biggest
    height = top + row * len(data["areas"]) + 16
    body = [f'<rect width="1200" height="{height}" rx="16" fill="{t["panel"]}"/>',
            f'<text x="40" y="44" font-size="20" font-weight="600" fill="{t["text"]}">Review rating</text>']
    x = 196
    for rating in ratings:
        body += [f'<rect x="{x}" y="30" width="18" height="18" rx="4" fill="{t["ramp"][rating - 1]}"/>',
                 f'<text x="{x + 26}" y="45" font-size="20" fill="{t["muted"]}">{rating}/5</text>']
        x += 92
    body.append(f'<text x="{right}" y="45" font-size="20" text-anchor="end" fill="{t["muted"]}">'
                "Number of reviews per area</text>")
    for index, area in enumerate(data["areas"]):
        y = top + index * row
        mid = y + row / 2
        body.append(f'<text x="{left - 16}" y="{mid + 7:.0f}" font-size="20" text-anchor="end" '
                    f'fill="{t["text"]}">{escape(area["name"])}</text>')
        cursor = left
        present = [r for r in ratings if counts[area["slug"]][r]]
        for rating in present:
            width = counts[area["slug"]][rating] * scale
            seg = max(width - 2, 1)  # 2px surface gap between adjacent fills
            fill = t["ramp"][rating - 1]
            if rating == present[-1]:
                # Round only the data end; the baseline end stays square.
                r = min(4, seg / 2)
                body.append(
                    f'<path d="M{cursor:.1f},{mid - 10:.1f} h{seg - r:.1f} a{r},{r} 0 0 1 {r},{r} v{20 - 2 * r:.1f} '
                    f'a{r},{r} 0 0 1 -{r},{r} h-{seg - r:.1f} z" fill="{fill}"><title>{escape(area["name"])}: '
                    f'{counts[area["slug"]][rating]} rated {rating}/5</title></path>')
            else:
                body.append(f'<rect x="{cursor:.1f}" y="{mid - 10:.1f}" width="{seg:.1f}" height="20" fill="{fill}">'
                            f'<title>{escape(area["name"])}: {counts[area["slug"]][rating]} rated {rating}/5</title></rect>')
            cursor += width
        body.append(f'<text x="{cursor + 10:.1f}" y="{mid + 7:.0f}" font-size="20" font-weight="600" '
                    f'fill="{t["text"]}">{sum(counts[area["slug"]].values())}</text>')
    return _svg(1200, height, "Completed reviews per area, split by review rating", body)


def render_all(data: dict, explored: dict) -> dict[str, str]:
    assets = {}
    for mode in THEMES:
        assets[f"assets/hero-{mode}.svg"] = render_hero(data, explored, mode)
        assets[f"assets/areas-{mode}.svg"] = render_areas(data, mode)
    return assets
