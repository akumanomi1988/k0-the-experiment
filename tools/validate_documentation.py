#!/usr/bin/env python3
"""Documentary integrity: stable filenames and a single normative master.

No external services, no documentation generation, no rewriting of historical copies.
Git itself preserves previous versions.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "ESPECIFICACION_MAESTRA.md"
INDEX = ROOT / "DOCS_INDEX.md"
FAILURES: list[str] = []
LINKS = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DOC_ROW = re.compile(r"^\|\s*(\d{2})\s*\|\s*\[[^\]]+\]\((docs/[^)]+\.md)\)\s*\|$", re.M)
OBSOLETE_SUFFIX = re.compile(r"(?:_v\d+(?:\.\d+)?|\.v\d+(?:\.\d+)?)\.md$", re.I)

def check(condition: bool, reason: str) -> None:
    if not condition:
        FAILURES.append(reason)

def main() -> int:
    required = (
        "README.md", "ESPECIFICACION_MAESTRA.md", "DOCS_INDEX.md",
        "REGISTRO_DE_DECISIONES.md", "COBERTURA_DOCUMENTAL.md",
        "data/legacy_user_decisions_1_92.json",
    )
    for name in required:
        check((ROOT / name).is_file(), f"Missing canonical file: {name}")
    if FAILURES:
        return report()

    markdowns = sorted(ROOT.rglob("*.md"))
    actual = {str(p.relative_to(ROOT)).replace("\\", "/") for p in markdowns}
    check(not any(re.fullmatch(r"v\d+(?:\.\d+)?", p.name)
                  for p in ROOT.iterdir() if p.is_dir()),
          "Versioned documentation directory must not be recreated")
    check(not any(OBSOLETE_SUFFIX.search(p) for p in actual),
          "Version suffix found in Markdown filenames")
    check(not any(p.startswith("v2.5/fuentes/") for p in actual),
          "Duplicate historical volumes still present")
    check(not any(p.startswith("MANIFIESTO_DOCUMENTAL_") or
                  p.startswith("PROJECT_CHAOS_DOCUMENTACION_MAESTRA_")
                  or re.match(r"DOCS_INDEX_v\d+", p) for p in actual),
          "Duplicate top-level Markdown documents remain")

    index = INDEX.read_text(encoding="utf-8")
    master = MASTER.read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("(ESPECIFICACION_MAESTRA.md)" in readme, "README lacks master")
    check("(ESPECIFICACION_MAESTRA.md)" in index, "Index lacks master")
    check(master.startswith("# K0:"), "Master heading missing")
    for n in range(18):
        check(re.search(rf"^## {n}\.", master, re.M) is not None,
              f"Master missing section {n}")

    rows = DOC_ROW.findall(index)
    check(len(rows) == 67, f"Expected 67 indexed chapters, got {len(rows)}")
    check([int(n) for n, _ in rows] == list(range(1, 68)),
          "Chapter numbering must be contiguous 01..67")
    chapters = {path for _, path in rows}
    docs = {p for p in actual if re.match(r"docs/\d{2}_.*\.md$", p)}
    check(chapters == docs, f"Chapter index mismatch: absent={sorted(docs-chapters)}, extra={sorted(chapters-docs)}")
    banner = "> **Documento de detalle.** La fuente normativa vigente es"
    for path in chapters & docs:
        check((ROOT / path).read_text(encoding="utf-8").startswith(banner),
              f"{path}: missing master authority notice")

    historical = json.loads((ROOT / "data/legacy_user_decisions_1_92.json").read_text(encoding="utf-8"))
    decisions = historical.get("decisions", [])
    check(len(decisions) == 92 and [d.get("number") for d in decisions] == list(range(1,93)),
          "Original 92 decisions are not intact")
    # All local markdown links in actively tracked Markdown must resolve after moves.
    # This detects stale numbered filenames and deleted volume references.
    for doc in markdowns:
        content = doc.read_text(encoding="utf-8")
        for match in LINKS.finditer(content):
            dest = match.group(1).strip()
            if not dest or dest.startswith(("#", "/", "mailto:", "data:")) or "://" in dest:
                continue
            raw = unquote(urlsplit(dest).path)
            if not raw:
                continue
            destpath = (doc.parent / raw).resolve()
            if not destpath.is_relative_to(ROOT.resolve()):
                FAILURES.append(f"{doc.relative_to(ROOT)}: link escapes repository: {dest}")
                continue
            check(destpath.exists(), f"{doc.relative_to(ROOT)}: broken link: {dest}")
    return report()

def report() -> int:
    if FAILURES:
        print(f"FAIL documentary integrity: {len(FAILURES)} problems")
        for message in FAILURES[:100]:
            print(" -", message)
        return 1
    print("PASS: one canonical master, one index, 67 chapters, 92 decisions, no duplicate versions and valid Markdown links.")
    print("NOTE: not evidence of a deployed game, provider authorization or integration testing.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
