#!/usr/bin/env python3
"""Integridad del árbol documental actual: sin archivos versionados ni enlaces rotos."""
from __future__ import annotations
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
CHAPTER = re.compile(r"docs/\d\d_[^/]+\.md$")
VERSIONED = re.compile(r"(?:[_.-]v\d+(?:\.\d+)*)\.(?:md|json|yaml)$", re.I)

def check(ok: bool, msg: str) -> None:
    if not ok: ERRORS.append(msg)

def main() -> int:
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    relative = {p.relative_to(ROOT).as_posix() for p in files}
    for path in sorted(relative):
        check(not VERSIONED.search(path), "Archivo versionado duplicable: " + path)
        check(not re.match(r"^v\d+(?:\.\d+)?/", path),
              "Carpeta de documentación por versión: " + path)
    docs = {x for x in relative if CHAPTER.fullmatch(x)}
    check(len(docs) == 67, f"Se esperan 67 documentos por tema, existen {len(docs)}")
    index_path = ROOT / "docs/INDICE.md"
    if index_path.is_file():
        index = index_path.read_text(encoding="utf-8")
        listed = set(re.findall(r"\]\((\d\d_[^)]+\.md)\)", index))
        expected = {p.removeprefix("docs/") for p in docs}
        check(listed == expected,
              f"Índice desactualizado: faltan {sorted(expected-listed)} / sobran {sorted(listed-expected)}")
    else:
        ERRORS.append("docs/INDICE.md no existe")

    for name in sorted(x for x in relative if x.endswith(".md")):
        doc = ROOT / name
        text = doc.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            raw = raw.strip().split(" ", 1)[0].strip("<>")
            if not raw or raw.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
            if not target: continue
            resolved = (doc.parent / target).resolve()
            inside = resolved.is_relative_to(ROOT.resolve())
            check(inside, f"{name}: enlace escapa del repositorio: {raw}")
            if inside:
                check(resolved.exists(), f"{name}: enlace roto: {raw}")
    decisions = ROOT / "data/legacy_user_decisions_1_92.json"
    if decisions.is_file():
        records = json.loads(decisions.read_text(encoding="utf-8")).get("decisions", [])
        check(len(records) == 92, "Faltan decisiones originales")
    else:
        ERRORS.append("Falta catálogo canónico de 92 decisiones")
    if ERRORS:
        print(f"FAIL: {len(ERRORS)} errores de documentación")
        for x in ERRORS[:120]: print(" - " + x)
        return 1
    print(f"PASS: {len(docs)} capítulos, enlaces válidos, una norma y ninguna copia versionada")
    return 0

if __name__ == "__main__":
    sys.exit(main())
