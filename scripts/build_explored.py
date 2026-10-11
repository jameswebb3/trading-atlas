#!/usr/bin/env python3
"""Render the public project ledger without changing the completed-review catalog."""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATUS = {
    "reviewed": "Full review",
    "source-note": "Source reading",
    "source-pointer": "Source pointer",
    "documentation-screen": "Documentation screen",
    "scope-screen": "Scope screen",
    "unresolved": "Unresolved",
}
ORDER = tuple(STATUS)

def load():
    explored = json.loads((ROOT / "explored.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    return explored, catalog

def _source_link(url):
    if not url:
        return "Public citation pending"
    parts = urlsplit(url)
    components = parts.path.split("/")[5:]
    label = "/".join(components[-2:]) or "Source"
    if parts.fragment.startswith("L"):
        label += "#" + parts.fragment.split("-", 1)[0]
    if len(label) > 48:
        label = "..." + label[-45:]
    return f"[{label}]({url})"

def _row(item, review):
    repo = item["repo"]
    project = f"[{repo}](https://github.com/{repo})"
    stars = str(item["stars_recorded"]) if item["stars_recorded"] is not None else "\u2014"
    focus = item["focus"]
    status = item["status"]
    if review:
        rating = review["rating"]
        glyph = "\u2605" * rating + "\u2606" * (5 - rating)
        record = f"[Full review](../{review['path']}) {glyph} ({rating}/5)"
        detail = f"{review['short_verdict']} {review['key_check']}"
    elif status == "source-note":
        record = "Source reading"
        detail = _source_link(item["public_source"])
    elif status == "source-pointer":
        record = "Source pointer"
        detail = _source_link(item["public_source"])
    elif status == "documentation-screen":
        record = "Documentation screen"
        detail = _source_link(item["public_source"])
    elif status == "scope-screen":
        record = "Scope screen"
        detail = _source_link(item["public_source"]) if item["public_source"] else "No source inspection"
    else:
        record = "Unresolved"
        detail = item["open_question"] + ("; " + _source_link(item["public_source"]) if item["public_source"] else "")
    return f"| {project} | {record} | {focus} | {stars} | {item['record_date']} | {detail} |"

def render_index():
    explored, catalog = load()
    items = explored["projects"]
    reviews = {item["repo"].casefold(): item for item in catalog["reviews"]}
    by_area = Counter(item["primary_area"] for item in items)
    by_status = Counter(item["status"] for item in items)
    lines = [
        "# Every project considered",
        "",
        f"**{len(items):,} repository records on the research ledger; {len(reviews):,} have a completed source-backed review.**",
        "",
        "This is the broad search record, not a list of recommendations. Each project has an upstream link,",
        "a discovery lens, a review status, and any public evidence link recorded at the time.",
        "Completed reviews add a rated mechanism and its limitation. The other records have no trading-system rating.",
        "",
        "GitHub star counts are historical values recorded during the search; they are not live and do not set the order.",
        "A discovery lens explains why a repository entered the search. It is not a claim that its whole product fits that area.",
        "",
        "[Back to the curated Atlas](README.md) \u00b7 [How review ratings work](METHODOLOGY.md)",
        "",
        "## Evidence status",
        "",
        "| Status | Projects | Meaning |",
        "| --- | ---: | --- |",
        f"| Full review | {by_status['reviewed']} | README, implementation, pinned commit, license and original assessment are public. |",
        f"| Source reading | {by_status['source-note']} | A code reading is recorded; a full public assessment has not passed the publication gate. A public citation is linked where retained. |",
        f"| Source pointer | {by_status['source-pointer']} | A public source link was found during discovery; the code was not reviewed for this catalog. |",
        f"| Documentation screen | {by_status['documentation-screen']} | Documentation was screened; no code mechanism is rated here. |",
        f"| Scope screen | {by_status['scope-screen']} | Initial fit check only; the repository has not been evaluated in code. |",
        f"| Unresolved | {by_status['unresolved']} | Current source or claimed implementation could not be verified. |",
        "",
        "## Browse every project",
        "",
        "| Area | Projects considered | Completed reviews |",
        "| --- | ---: | ---: |",
    ]
    for area in catalog["areas"]:
        slug = area["slug"]
        n_reviews = sum(item["primary_area"] == slug for item in catalog["reviews"])
        lines.append(f"| [{area['name']}](explored/{slug}.md) | {by_area[slug]} | {n_reviews} |")
    lines += [
        "",
        f"Each area page lists every project assigned to that discovery area exactly once. The {len(reviews):,} completed reviews",
        "retain the full assessments and ratings in the [curated area pages](README.md#explore-by-area).",
        "",
    ]
    return "\n".join(lines)

def render_area_pages():
    explored, catalog = load()
    reviews = {item["repo"].casefold(): item for item in catalog["reviews"]}
    pages = {}
    project_total = len(explored["projects"])
    for area in catalog["areas"]:
        slug = area["slug"]
        members = [item for item in explored["projects"] if item["primary_area"] == slug]
        members.sort(key=lambda item: (
            ORDER.index(item["status"]),
            -reviews[item["repo"].casefold()]["rating"] if item["status"] == "reviewed" else 0,
            item["repo"].casefold(),
        ))
        counts = Counter(item["status"] for item in members)
        lines = [
            f"# {area['name']}: every project considered",
            "",
            area["description"],
            "",
            f"**{len(members)} projects:** {counts['reviewed']} full reviews, {counts['source-note']} source readings, "
            f"{counts['source-pointer']} source pointers, {counts['documentation-screen']} documentation screens, "
            f"{counts['scope-screen']} scope screens, "
            f"{counts['unresolved']} unresolved.",
            "",
            "Only completed reviews have a trading-system rating. GitHub star counts are historic search snapshots.",
            "A discovery lens is a search label, not a product-wide assessment.",
            "",
            f"[All {project_total:,} projects](../PROJECTS.md) \u00b7 [Curated area reviews](../areas/{slug}.md) "
            "\u00b7 [Rating methodology](../METHODOLOGY.md)",
            "",
            "| Project | Review status | Discovery lens | GitHub stars at scan | Record date | Detail / public evidence |",
            "| --- | --- | --- | ---: | --- | --- |",
        ]
        for item in members:
            lines.append(_row(item, reviews.get(item["repo"].casefold())))
        lines.append("")
        pages[slug] = "\n".join(lines)
    return pages

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render_index()
    pages = render_area_pages()
    outputs = {ROOT / "PROJECTS.md": expected}
    outputs.update({ROOT / "explored" / f"{slug}.md": body for slug, body in pages.items()})
    if args.check:
        for path, body in outputs.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != body:
                raise SystemExit(f"Out of date: {path}")
        print(f"Project ledger current: {len(load()[0]['projects'])} projects")
        return
    for path, body in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    print(f"Project ledger rendered: {len(load()[0]['projects'])} projects")

if __name__ == "__main__":
    main()
