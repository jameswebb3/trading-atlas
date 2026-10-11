#!/usr/bin/env python3
"""Validate that every public catalog entry has a completed, pinned source review."""

import datetime
import json
import re
from pathlib import Path

from build_index import render, render_area_pages
from build_explored import render_index as render_explored_index, render_area_pages as render_explored_areas

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
UNPINNED_BLOB = re.compile(r"github\.com/[^/]+/[^/]+/blob/(?:HEAD|main|master|develop)/")
FIT_CAP = {"direct": 5, "transferable": 3, "adjacent": 2}


def main() -> None:
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    assert set(data) == {"schema_version", "areas", "reviews"}
    assert data["schema_version"] == 4
    areas = {area["slug"] for area in data["areas"]}
    assert len(areas) == len(data["areas"]) == 10
    assert all(area["description"].strip() and "|" not in area["description"] for area in data["areas"])

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    pages = render_area_pages()
    highlights = json.loads((ROOT / "homepage-highlights.json").read_text(encoding="utf-8"))
    assert set(highlights) == {"updated_at", "items"}
    update_date = datetime.date.fromisoformat(highlights["updated_at"])
    by_repo = {review["repo"]: review for review in data["reviews"]}
    assert 1 <= len(highlights["items"]) <= 5
    highlight_repos = set()
    for entry in highlights["items"]:
        assert set(entry) == {"repo", "kind", "summary"}
        assert entry["repo"] in by_repo
        assert entry["repo"] not in highlight_repos
        highlight_repos.add(entry["repo"])
        assert entry["kind"] in ("finding", "correction")
        assert 1 <= len(entry["summary"].split()) <= 40
        assert "\n" not in entry["summary"] and "|" not in entry["summary"]
        assert datetime.date.fromisoformat(by_repo[entry["repo"]]["reviewed_at"]) <= update_date
    assert "in-depth reviews" not in readme
    assert "Recent findings & corrections" in readme

    seen_repos = set()
    seen_paths = set()
    mention_orders = {}
    counts = {area: 0 for area in areas}

    for review in data["reviews"]:
        repo = review["repo"]
        relative_path = review["path"]
        commit = review["source_commit"]
        slug = review["primary_area"]
        assert REPO.fullmatch(repo), repo
        assert SHA.fullmatch(commit), repo
        assert slug in areas, repo
        assert review["review_depth"] in (2, 3), repo
        assert review["trading_fit"] in FIT_CAP, repo
        assert isinstance(review["rating"], int) and 1 <= review["rating"] <= FIT_CAP[review["trading_fit"]], repo
        if review["rating"] == 5:
            assert review["review_depth"] == 3, repo
        assert review["rating_reason"].strip() and "|" not in review["rating_reason"], repo
        assert review["display_name"].strip(), repo
        assert review["short_verdict"].strip() and "|" not in review["short_verdict"], repo
        assert len(review["short_verdict"].split()) <= 55, repo
        assert review["key_check"].strip() and "|" not in review["key_check"], repo
        assert len(review["key_check"].split()) <= 35, repo
        assert review["declared_license"], repo
        assert review["question"].strip().endswith("?"), repo
        datetime.date.fromisoformat(review["reviewed_at"])
        assert repo not in seen_repos, repo
        assert relative_path not in seen_paths, relative_path
        seen_repos.add(repo)
        seen_paths.add(relative_path)
        counts[slug] += 1

        assert "honorable_mention_question" not in review, repo
        description = review.get("honorable_mention_description")
        source = review.get("honorable_mention_source")
        order = review.get("honorable_mention_order")
        assert (description is None) == (order is None) == (source is None), repo
        if description is not None:
            assert description.strip().endswith(".") and "?" not in description and "|" not in description, repo
            assert len(description.split()) <= 50, repo
            assert source.startswith(f"https://github.com/{repo}/blob/{commit}/"), repo
            assert re.search(r"#L\d+(?:-L\d+)?$", source), repo
            assert isinstance(order, int) and order >= 0, repo
            mention_orders.setdefault(slug, []).append(order)

        path = ROOT / relative_path
        assert path.is_file() and path.resolve().is_relative_to(ROOT), relative_path
        body = path.read_text(encoding="utf-8")
        assert commit in body, repo
        assert f"https://github.com/{repo}/blob/{commit}/" in body, repo
        assert re.search(rf"github\.com/{re.escape(repo)}/blob/{commit}/[^\s)]+#L\d+", body), repo
        assert f"| Trading-system value | {review['rating']}/5 |" in body, repo
        assert review["rating_reason"] in body, repo
        assert not UNPINNED_BLOB.search(body), repo
        assert relative_path in readme or f"../{relative_path}" in pages[slug], repo

    assert len(seen_paths) == len(list((ROOT / "reviews").glob("*.md"))), "Uncataloged review file"
    for slug, orders in mention_orders.items():
        assert len(orders) <= 3 and len(orders) == len(set(orders)), slug
        assert counts[slug] >= 8, slug

    assert readme == render(), "README index is out of date"
    for slug, body in pages.items():
        path = ROOT / "areas" / f"{slug}.md"
        assert path.is_file() and path.read_text(encoding="utf-8") == body, path
        assert f"areas/{slug}.md" in readme or counts[slug] <= 6, slug
    explored = json.loads((ROOT / "explored.json").read_text(encoding="utf-8"))
    assert set(explored) == {"schema_version", "snapshot_date", "projects"}
    assert explored["schema_version"] == 1
    datetime.date.fromisoformat(explored["snapshot_date"])
    all_items = explored["projects"]
    assert len(all_items) == len({item["repo"].casefold() for item in all_items})
    assert {item["repo"].casefold() for item in all_items if item["status"] == "reviewed"} == {repo.casefold() for repo in seen_repos}
    statuses = {"reviewed", "source-note", "source-pointer", "documentation-screen", "scope-screen", "unresolved"}
    for item in all_items:
        expected_fields = {"repo", "primary_area", "focus", "status", "stars_recorded", "record_date", "public_source"}
        if item["status"] == "unresolved":
            expected_fields.add("open_question")
        assert set(item) == expected_fields, item["repo"]
        assert REPO.fullmatch(item["repo"]), item["repo"]
        assert item["primary_area"] in areas, item["repo"]
        assert item["status"] in statuses, item["repo"]
        assert item["focus"].strip() and "|" not in item["focus"], item["repo"]
        assert item["stars_recorded"] is None or isinstance(item["stars_recorded"], int) and item["stars_recorded"] >= 0, item["repo"]
        datetime.date.fromisoformat(item["record_date"])
        if item["status"] == "reviewed":
            assert item["public_source"] is None, item["repo"]
        if item["status"] == "source-pointer":
            assert item["public_source"], item["repo"]
        if item["status"] == "unresolved":
            assert item["open_question"] in {"Current versioning implementation not verified", "Original GitHub repository unavailable on last check"}
        url = item["public_source"]
        if url:
            assert url.lower().startswith(f"https://github.com/{item['repo'].lower()}/blob/"), item["repo"]
            assert re.search(r"/blob/[0-9a-f]{40}/", url), item["repo"]
            assert not UNPINNED_BLOB.search(url), item["repo"]
    assert (ROOT / "PROJECTS.md").read_text(encoding="utf-8") == render_explored_index()
    for slug, body in render_explored_areas().items():
        path = ROOT / "explored" / f"{slug}.md"
        assert path.is_file() and path.read_text(encoding="utf-8") == body, path
    print(f"Catalog OK: {len(data['reviews'])} full reviews and {len(all_items)} clearly tiered project records across {len(areas)} areas")


if __name__ == "__main__":
    main()
