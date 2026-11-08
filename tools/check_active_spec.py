#!/usr/bin/env python3
"""Guard de una sola especificación actual. Git conserva el historial."""
from __future__ import annotations
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS: list[str] = []

def check(ok: bool, message: str) -> None:
    if not ok:
        PROBLEMS.append(message)

def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def main() -> int:
    spec = ROOT / "docs/ESPECIFICACION.md"
    index = ROOT / "docs/INDICE.md"
    check(spec.is_file(), "Falta norma única docs/ESPECIFICACION.md")
    check(index.is_file(), "Falta índice único docs/INDICE.md")
    check(not (ROOT / "CURRENT.md").exists(), "CURRENT.md es una copia normativa duplicada")
    check(not (ROOT / "docs/CURRENT_SPEC.md").exists(), "CURRENT_SPEC.md es copia obsoleta")
    check(not (ROOT / "data/active_documentation.json").exists(), "Puntero de versiones documentales obsoleto")
    check(not any(ROOT.glob("DOCS_INDEX_v*.md")), "Índice paralelo versionado")
    check(not any(ROOT.glob("MANIFIESTO_DOCUMENTAL_v*.md")), "Manifiesto histórico duplicado")
    check(not any(ROOT.glob("PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v*.md")),
          "Compendio histórico paralelo")
    check(not any(p.is_dir() for p in ROOT.iterdir() if re.fullmatch(r"v\d+(?:\.\d+)*", p.name)),
          "Carpeta versionada de documentos")
    if not spec.exists():
        return report()
    txt = spec.read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check(len(txt) > 30000, "Especificación consolidada parece truncada")
    check("## Anexo: decisiones de consolidación" in txt and "V25-26" in txt,
          "Decisiones de consolidación no integradas")
    check("docs/ESPECIFICACION.md" in readme and "Git" in readme,
          "README no declara la norma única y Git como histórico")
    rules = load("data/ruleset.json")
    command = {x["id"]: x for x in load("data/commands.json")["commands"]}
    schema = load("contracts/ruleset.schema.json")
    check(rules.get("sourcePriority", [None, None])[1] == "docs/ESPECIFICACION.md",
          "Ruleset apunta a documento de versión obsoleta")
    check(rules["citizens"]["activeHumanWorkersSoftCapScope"] ==
          "PER_NATION_TOTAL",
          "Cuota humana debe ser una sola por nación")
    check(rules["citizens"]["humanQuotaAssignment"] ==
          "deterministic_hash_rotation_nation_live_600s",
          "La cuota nacional debe rotar de forma reproducible cada 600s LIVE")
    check(rules["citizens"]["humanWorkXpEligibility"] ==
          "accepted_effective_work_only",
          "XP no puede concederse por trabajo no aceptado")
    for field in ("activeHumanWorkersSoftCapScope", "humanQuotaAssignment",
                  "humanWorkXpEligibility"):
        check(field in schema["properties"]["citizens"]["required"],
              f"Schema no exige {field}")
    check(command["join"]["precondition"] == "authenticated_provider_identity",
          "!join requiere identidad autenticada, no ciudadano previo")
    check(command["work"]["precondition"] == "registered_citizen",
          "!work requiere ciudadanía")
    check("2.500 activos efectivos" in txt and "600 segundos" in txt and "XP laboral" in txt,
          "Reglas de cuota nacional y XP no sincronizadas con la especificación")
    delta = load("contracts/nation_delta.schema.json")
    check(delta["properties"]["nationId"].get("format") == "uuid",
          "NationId público UUID en diseño actual")
    check(set(delta["properties"]["factionId"]["enum"]) ==
          {"micelios", "runicos", "ferrinos"}, "FactionId no es slug separado")
    manifest = load("data/content_manifest.json")
    check(manifest["status"] == "DESIGN_CANDIDATE_NOT_HASHED_OR_RELEASED",
          "No confundir catálogos de diseño con una release")
    check(len(manifest["files"]) == 15, "Manifiesto activo debe cubrir los 15 catálogos")
    for entry in manifest["files"]:
        check((ROOT / entry["path"]).is_file(), "Catálogo ausente " + entry["path"])
    return report()

def report() -> int:
    if PROBLEMS:
        print(f"FAIL: {len(PROBLEMS)} problemas de autoridad")
        for x in PROBLEMS:
            print(" - " + x)
        return 1
    print("PASS: especificación única, reglas, ciudadanía, cuota e identidad actuales")
    return 0

if __name__ == "__main__":
    sys.exit(main())
