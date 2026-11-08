#!/usr/bin/env python3
"""Check v2.5 source preservation, coverage, links and documentation integrity.

This is a TEXT/STRUCTURE validator. It does not certify economic balance,
migrations, streaming API permissions, creative assets or running software.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "v2.5"
FAIL: list[str] = []


def check(ok: bool, message: str) -> None:
    if not ok:
        FAIL.append(message)


def read(path: Path) -> str:
    if not path.is_file():
        FAIL.append("Missing file: " + str(path.relative_to(ROOT)))
        return ""
    return path.read_text(encoding="utf-8")


INDEX_LINE = re.compile(
    r"^\|\s*(\d{2})\s*\|\s*\[[^\]]+\]\((docs\/[^)]+)\)\s*\|",
    flags=re.MULTILINE,
)
ARCHIVE_HEADER = re.compile(
    r"\n---\n\n## Fuente (\d{2}) — " + r"\x60([^\x60]+)\x60" +
    r"\n\n\*\*Blob (?:de origen|original):\*\* \x60([0-9a-f]{40})\x60\.\n\n",
)
REL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")


def volume_for(number: int) -> str:
    start = ((number - 1) // 8) * 8 + 1
    end = min(start + 7, 67)
    return f"FUENTES_{start:02}_{end:02}.md"


def main() -> int:
    contents = read(ROOT / "DOCS_INDEX_v2.3.md")
    entries = [(int(n), p) for n, p in INDEX_LINE.findall(contents)]
    check(len(entries) == 67, f"Expected 67 indexed chapters, found {len(entries)}")
    check([n for n, _ in entries] == list(range(1, 68)),
          "Chapter numbering should be exactly 1..67")
    expected_paths = {n: p for n, p in entries}
    expected_source_text = {n: read(ROOT / p) for n, p in entries}

    volume_paths = sorted((BASE / "fuentes").glob("FUENTES_*.md"))
    check(len(volume_paths) == 9, f"Expected 9 source volumes, found {len(volume_paths)}")
    archived = {}
    for volume in volume_paths:
        text = read(volume)
        headers = list(ARCHIVE_HEADER.finditer(text))
        check(len(headers) > 0, f"No source sections detected in {volume.name}")
        for i, match in enumerate(headers):
            number = int(match.group(1))
            source_path = match.group(2)
            original_blob_sha = match.group(3)
            start_body = match.end()
            end_body = headers[i + 1].start() if i + 1 < len(headers) else len(text)
            archive_body = text[start_body:end_body]
            check(number not in archived,
                  f"Chapter {number} included twice")
            archived[number] = (volume.name, source_path)
            check(source_path == expected_paths.get(number),
                  f"Chapter {number} source path drift: {source_path}")
            check(volume.name == volume_for(number),
                  f"Chapter {number} in incorrect archive volume")
            check(len(original_blob_sha) == 40,
                  f"Chapter {number} invalid source blob SHA")
            original = expected_source_text.get(number, "")
            # Original heading levels were indented by one to embed chapters
            # inside volumes. This is reversible; no prose/data is omitted.
            nested = re.sub(r"^#", "##", original, flags=re.MULTILINE)
            check(archive_body.rstrip("\n") == nested.rstrip("\n"),
                  f"Chapter {number} text differs from source (excluding heading nesting)")
    check(set(archived) == set(range(1, 68)),
          "Archived chapters do not cover the whole 1..67 set")

    decisions = json.loads(read(ROOT / "data/legacy_user_decisions_1_92.json"))
    data = decisions.get("decisions", [])
    check(len(data) == 92 and [d.get("number") for d in data] == list(range(1, 93)),
          "Historical decision register must retain exactly 92 ordered entries")
    decisions_copy = read(BASE / "fuentes/DECISIONES_1_92.md")
    numbers = [int(x) for x in re.findall(r"^\|\s*(\d{1,2})\s*\|\s*[A-Z_]+\s*\|", decisions_copy, re.MULTILINE)]
    check(numbers == list(range(1, 93)),
          "v2.5 human readable decision archive missing a decision")

    original_21 = read(ROOT / "PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v2.1.md")
    archive_21 = read(BASE / "fuentes/COMPENDIO_HISTORICO_INTEGRO_v2.1.md")
    check(archive_21.endswith(original_21),
          "Historical v2.1 master not fully preserved")

    manifest = json.loads(read(ROOT / "data/content_manifest.v2.3.json"))
    catalogs = manifest.get("files", [])
    check(len(catalogs) == 15, "Expected original 15 game catalog manifest entries")
    for x in catalogs:
        p = ROOT / x.get("path", "")
        check(p.is_file(), f"Manifest catalog absent: {p}")
        if p.is_file():
            try:
                json.loads(read(p))
            except json.JSONDecodeError as e:
                FAIL.append(f"Invalid catalog JSON {p}: {e}")

    master = read(BASE / "ESPECIFICACION_MAESTRA_v2.5.md")
    registry = read(BASE / "REGISTRO_DE_CONSOLIDACION_v2.5.md")
    coverage = read(BASE / "INDICE_DE_COBERTURA_v2.5.md")
    for n in range(18):
        check(re.search(rf"^## {n}\.", master, flags=re.MULTILINE) is not None,
              f"Master missing normative section {n}")
    check("26" in registry and "V25-26" in registry,
          "Reconciliation record not complete")
    check(len(re.findall(r"^\|\s*\d{2}\s*\|", coverage, re.MULTILINE)) == 67,
          "Coverage table must enumerate 67 chapters")
    for n, source_path in entries:
        check(source_path in coverage, f"Coverage index missing {source_path}")
    for path in (BASE / "ESPECIFICACION_MAESTRA_v2.5.md",
                 BASE / "REGISTRO_DE_CONSOLIDACION_v2.5.md",
                 BASE / "INDICE_DE_COBERTURA_v2.5.md"):
        text = read(path)
        for raw_link in REL_LINK.findall(text):
            if "://" in raw_link or raw_link.startswith(("mailto:", "/")):
                continue
            target = (path.parent / raw_link).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                FAIL.append(f"Link outside repo in {path.name}: {raw_link}")
                continue
            check(target.is_file() or target.is_dir(),
                  f"Dead local link in {path.name}: {raw_link}")

    if FAIL:
        print(f"FAIL v2.5 consolidation: {len(FAIL)} problems")
        for issue in FAIL:
            print(" - " + issue)
        return 1
    print("PASS: 67 full source chapters, 92 decisions, v2.1 historical "
          "master, 15 catalogs and normative v2.5 links/structure.")
    print("NOTE: implementation, financial, legal, art and LIVE APIs NOT validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
