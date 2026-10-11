#!/usr/bin/env python3
"""Build the curated review index and link the separately marked project ledger."""

import argparse
import json
from collections import Counter
from pathlib import Path

from build_assets import render_all

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = "{{CATALOG}}"


def _sorted_reviews(reviews: list[dict], slug: str) -> list[dict]:
    return sorted(
        (item for item in reviews if item["primary_area"] == slug),
        key=lambda item: (-item["rating"], item["display_name"].casefold()),
    )


def _review_row(item: dict, relative_prefix: str = "") -> str:
    score = item["rating"]
    stars = chr(0x2605) * score + chr(0x2606) * (5 - score)
    return (
        f"| [{item['display_name']}](https://github.com/{item['repo']}) · "
        f"[Review]({relative_prefix}{item['path']}) | "
        f"{stars} ({score}/5) | "
        f"{item['short_verdict']} {item['key_check']} |"
    )


def _rating(item: dict) -> str:
    score = item["rating"]
    return chr(0x2605) * score + chr(0x2606) * (5 - score) + f" ({score}/5)"


def _render_highlights(data: dict) -> str:
    highlights = json.loads((ROOT / "homepage-highlights.json").read_text(encoding="utf-8"))
    by_repo = {item["repo"]: item for item in data["reviews"]}
    lines = [
        '<a id="recent-findings-and-corrections"></a>',
        "## Recent findings & corrections",
        "",
        f"**Updated {highlights['updated_at']}.** Selected observations from new and updated reviews.",
        "",
    ]
    for entry in highlights["items"]:
        item = by_repo[entry["repo"]]
        label = "Correction" if entry["kind"] == "correction" else "Finding"
        lines.append(
            f"- **[{item['display_name']}]({item['path']})** — "
            f"{'Correction: ' if label == 'Correction' else ''}{entry['summary']}"
        )
    lines += ["", "[See all additions and corrections](CHANGELOG.md)."]
    return "\n".join(lines)


def _render_questions(data: dict) -> str:
    questions = json.loads((ROOT / "homepage-questions.json").read_text(encoding="utf-8"))
    by_repo = {item["repo"]: item for item in data["reviews"]}
    cells = []
    for entry in questions["items"]:
        links = [
            f'<a href="{by_repo[repo]["path"]}">{by_repo[repo]["display_name"]}</a> {by_repo[repo]["rating"]}/5'
            for repo in entry["repos"]
        ]
        if entry["guide"]:
            links.append(f'<a href="{entry["guide"]}">Comparison guide</a>')
        cells.append(f'<td valign="top" width="33%"><b>{entry["question"]}</b><br><br>{"<br>".join(links)}</td>')
    lines = [
        '<a id="start-with-your-problem"></a>',
        "## Start with your problem",
        "",
        "Common ways trading systems go wrong, and the reviews that show how real projects handle them.",
        "",
        "<table>",
    ]
    for start in range(0, len(cells), 3):
        lines += ["<tr>", *cells[start:start + 3], "</tr>"]
    lines.append("</table>")
    return "\n".join(lines)


def _render_example(data: dict) -> str:
    questions = json.loads((ROOT / "homepage-questions.json").read_text(encoding="utf-8"))
    item = next(review for review in data["reviews"] if review["repo"] == questions["example"])
    area = next(area["name"] for area in data["areas"] if area["slug"] == item["primary_area"])
    return "\n".join([
        "## What a review gives you",
        "",
        "Every review asks one engineering question, answers it from the source code, and states the limit.",
        "",
        f"> **[{item['display_name']}](https://github.com/{item['repo']})** · {_rating(item)} · {area}",
        ">",
        f"> **The question.** {item['question']}",
        ">",
        f"> **What it gets right.** {item['short_verdict']}",
        ">",
        f"> **The catch.** {item['key_check']}",
        ">",
        f"> [Read the full review, with links to the exact lines →]({item['path']})",
    ])


def _render_shortlist(data: dict) -> str:
    top = [item for item in data["reviews"] if item["rating"] >= 4]
    lines = [
        '<a id="top-rated"></a>',
        f"## Top-rated: {len(top)} reviews scored 4/5 or higher",
        "",
        "Directly relevant trading mechanisms, visible in code, with their limits stated. "
        f"Only {round(100 * len(top) / len(data['reviews']))}% of reviews reach this score.",
        "",
    ]
    for area in data["areas"]:
        members = _sorted_reviews(top, area["slug"])
        if not members:
            continue
        lines += [
            "<details>",
            f"<summary><b>{area['name']}</b> · {len(members)} projects</summary>",
            "",
        ]
        lines += [f"- **[{item['display_name']}]({item['path']})** — {item['short_verdict']}" for item in members]
        lines += ["", "</details>", ""]
    return "\n".join(lines).rstrip()


def render() -> str:
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    template = (ROOT / "README_TEMPLATE.md").read_text(encoding="utf-8")
    for token in (PLACEHOLDER, "{{REVIEW_COUNT}}", "{{PROJECT_COUNT}}", "{{HIGHLIGHTS}}",
                  "{{QUESTIONS}}", "{{SHORTLIST}}", "{{TOP_COUNT}}", "{{EXAMPLE}}",
                  "{{UNRATED_COUNT}}", "{{SOURCE_NOTE_COUNT}}",
                  "{{DOCUMENTATION_SCREEN_COUNT}}", "{{SCOPE_SCREEN_COUNT}}",
                  "{{UNRESOLVED_COUNT}}"):
        if template.count(token) < 1:
            raise ValueError(f"README template must contain {token}")

    areas = data["areas"]
    reviews = data["reviews"]
    explored = json.loads((ROOT / "explored.json").read_text(encoding="utf-8"))
    counts = Counter(item["primary_area"] for item in reviews)
    explored_counts = Counter(item["primary_area"] for item in explored["projects"])
    status_counts = Counter(item["status"] for item in explored["projects"])
    guides = {
        "market-data-ingestion": ("guides/on-chain-data.md", "On-chain data: from blocks to usable observations"),
        "execution-exchange-integration": ("guides/order-completion.md", "Order completion and fill evidence"),
    }
    lines = [
        "## Explore by area",
        "",
        f"**{len(reviews)} source-backed reviews across {len(areas)} areas.** Each area page lists its reviews "
        "ordered by rating. Ratings apply to the mechanism covered in each review; "
        "[see the scoring criteria](METHODOLOGY.md).",
        "",
        "<table>",
    ]
    cards = []
    for area in areas:
        slug = area["slug"]
        members = _sorted_reviews(reviews, slug)
        picks = sorted((item for item in members if item.get("honorable_mention_description")),
                       key=lambda item: item["honorable_mention_order"])
        card = [
            f'<td valign="top" width="50%"><a id="{slug}"></a><h3><a href="areas/{slug}.md">{area["name"]}</a></h3>',
            f"{area['description']}<br><br>",
            f'<b>{len(members)} reviews</b> · <a href="explored/{slug}.md">{explored_counts[slug]} projects considered</a>',
        ]
        if picks:
            card.append("<br>Editor's picks: " + " · ".join(
                f'<a href="{item["path"]}">{item["display_name"]}</a>' for item in picks))
        if slug in guides:
            card.append(f'<br>Guide: <a href="{guides[slug][0]}">{guides[slug][1]}</a>')
        card.append("</td>")
        cards.append("".join(card))
    for start in range(0, len(cards), 2):
        lines += ["<tr>", *cards[start:start + 2], "</tr>"]
    lines += ["</table>", "", "<details>", "<summary><b>Why these picks?</b> What each editor's pick offers</summary>", ""]
    for area in areas:
        picks = sorted((item for item in _sorted_reviews(reviews, area["slug"]) if item.get("honorable_mention_description")),
                       key=lambda item: item["honorable_mention_order"])
        if not picks:
            continue
        lines += [f"**{area['name']}**", "", "| Project | Review rating | What it offers |", "| --- | --- | --- |"]
        for item in picks:
            lines.append(f"| [{item['display_name']}](https://github.com/{item['repo']}) · [Review]({item['path']}) | "
                         f"{_rating(item)} | {item['honorable_mention_description']} |")
        lines.append("")
    lines += ["</details>", ""]

    return (
        template.replace(PLACEHOLDER, "\n".join(lines).rstrip())
        .replace("{{REVIEW_COUNT}}", f"{len(reviews):,}")
        .replace("{{PROJECT_COUNT}}", f"{len(explored["projects"]):,}")
        .replace("{{UNRATED_COUNT}}", f"{len(explored["projects"]) - len(reviews):,}")
        .replace("{{SOURCE_NOTE_COUNT}}", str(status_counts["source-note"]))
        .replace("{{DOCUMENTATION_SCREEN_COUNT}}", str(status_counts["documentation-screen"]))
        .replace("{{SCOPE_SCREEN_COUNT}}", str(status_counts["scope-screen"]))
        .replace("{{UNRESOLVED_COUNT}}", str(status_counts["unresolved"]))
        .replace("{{AREA_COUNT}}", str(len(areas)))
        .replace("{{HIGHLIGHTS}}", _render_highlights(data))
        .replace("{{QUESTIONS}}", _render_questions(data))
        .replace("{{EXAMPLE}}", _render_example(data))
        .replace("{{MID_SHARE}}", str(round(100 * sum(item["rating"] in (2, 3) for item in reviews) / len(reviews))))
        .replace("{{SHORTLIST}}", _render_shortlist(data))
        .replace("{{TOP_COUNT}}", str(sum(item["rating"] >= 4 for item in reviews)))
    )


def render_area_pages() -> dict[str, str]:
    """Render each area using only completed reviews."""
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    pages = {}
    for area in data["areas"]:
        slug = area["slug"]
        members = _sorted_reviews(data["reviews"], slug)
        lines = [
            f"# {area['name']}",
            "",
            area["description"],
            "",
            f"**{len(members)} source-backed reviews.** Ratings assess the inspected mechanism, not every feature of the project.",
            "",
            f"[← Back to the Atlas](../README.md) · [All projects examined in this area](../explored/{slug}.md) · [How ratings work](../METHODOLOGY.md)",
            "",
            "| Project | Review rating | Assessment |",
            "| --- | ---: | --- |",
        ]
        for item in members:
            lines.append(_review_row(item, "../"))
        lines.append("")
        pages[slug] = "\n".join(lines)
    return pages


def render_assets() -> dict[str, str]:
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    explored = json.loads((ROOT / "explored.json").read_text(encoding="utf-8"))
    return render_all(data, explored)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated pages differ")
    args = parser.parse_args()
    target = ROOT / "README.md"
    expected = render()
    pages = render_area_pages()
    area_dir = ROOT / "areas"
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            print("README is out of date; run scripts/build_index.py")
            return 1
        for slug, body in pages.items():
            path = area_dir / f"{slug}.md"
            if not path.is_file() or path.read_text(encoding="utf-8") != body:
                print(f"{path} is out of date; run scripts/build_index.py")
                return 1
        for relative, body in render_assets().items():
            if not (ROOT / relative).is_file() or (ROOT / relative).read_text(encoding="utf-8") != body:
                print(f"{relative} is out of date; run scripts/build_index.py")
                return 1
        print("README and reviewed-only area pages are current")
        return 0
    area_dir.mkdir(exist_ok=True)
    target.write_text(expected, encoding="utf-8")
    for slug, body in pages.items():
        (area_dir / f"{slug}.md").write_text(body, encoding="utf-8")
    for relative, body in render_assets().items():
        (ROOT / relative).parent.mkdir(exist_ok=True)
        (ROOT / relative).write_text(body, encoding="utf-8")
    print("README and reviewed-only area pages rebuilt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
