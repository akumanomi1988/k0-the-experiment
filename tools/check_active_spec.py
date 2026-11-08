#!/usr/bin/env python3
"""Read-only CI guard for the active K0 design. --write refreshes CURRENT.md only."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    p = (ROOT / path).resolve()
    if not p.is_relative_to(ROOT.resolve()):
        raise ValueError("Path outside repository: " + path)
    return p.read_text(encoding="utf-8")

def load(path):
    return json.loads(read(path))

def current(pointer, rules, manifest):
    version = pointer["documentationVersion"]
    lines = [
        "# Documentación vigente — K0: The Experiment",
        "",
        "<!-- GENERADO: python3 tools/check_active_spec.py --write -->",
        "",
        "**Especificación documental activa: v" + version + ".** Diseño no implementado ni certificado para LIVE.",
        "",
        "- Norma: [" + pointer["master"] + "](" + pointer["master"] + ")",
        "- Enmiendas: [" + pointer["registry"] + "](" + pointer["registry"] + ")",
        "- Cobertura histórica: [" + pointer["coverage"] + "](" + pointer["coverage"] + ")",
        "- Índice histórico: [" + pointer["index"] + "](" + pointer["index"] + ")",
        "- Ruleset: " + pointer["ruleset"] + " (schema " + rules["schemaVersion"] + ")",
        "- Manifiesto de catálogos: " + pointer["manifest"] + " (schema " + manifest["schemaVersion"] + ")",
        "- Cuota humana: " + rules["citizens"]["activeHumanWorkersSoftCapScope"],
        "- Rotación: " + rules["citizens"]["humanQuotaAssignment"],
        "- XP de trabajo: " + rules["citizens"]["humanWorkXpEligibility"],
        "",
        "Contratos v2.5: nationId es UUID; factionId es slug independiente. El comando !join no requiere ciudadanía previa.",
        "",
        "Los 67 capítulos originales y otras versiones son fuentes históricas, no normas paralelas.",
        "Para actualizar este archivo: python3 tools/check_active_spec.py --write. La CI ejecuta --check.",
        "Esta CI no valida motor, arte, autorizaciones de proveedores, migraciones reales ni balance global.",
        "",
    ]
    return "\n".join(lines)

def validate(write=False):
    errs=[]
    def check(ok,msg):
        if not ok: errs.append(msg)
    ptr=load("data/active_documentation.json")
    version=ptr["documentationVersion"]
    master=ptr["master"]
    check(master == "v" + version + "/ESPECIFICACION_MAESTRA_v" + version + ".md",
          "Active master path/version mismatch")
    check(ptr["registry"].startswith("v"+version+"/"), "Active registry version mismatch")
    check(ptr["coverage"].startswith("v"+version+"/"), "Active coverage version mismatch")
    check(ptr["index"] == "DOCS_INDEX_v"+version+".md", "Active index version mismatch")
    dirs = [tuple(int(x) for x in match.groups()) for d in ROOT.iterdir()
            if d.is_dir() and (match := re.fullmatch(r"v(\d+)\.(\d+)", d.name))]
    check(bool(dirs) and version == ".".join(map(str,max(dirs))),
          "Newer documentation version exists: update active pointer")
    for field in ("master","registry","coverage","index","ruleset","manifest"):
        try:
            read(ptr[field])
        except (OSError,ValueError) as exc:
            errs.append(field + " missing/unsafe: " + str(exc))
    if errs:
        return errs
    master_text=read(master)
    readme=read("README.md")
    rules=load(ptr["ruleset"])
    schema=load("contracts/ruleset.schema.json")
    manifest=load(ptr["manifest"])
    commands={x["id"]:x for x in load("data/commands.v2.json")["commands"]}
    delta=load("contracts/nation_delta.schema.json")
    check("v"+version in master_text[:350], "Master title is not active version")
    check("("+master+")" in readme and "(CURRENT.md)" in readme,
          "README does not lead to current normative version")
    check("v"+version in rules["sourcePriority"][1],
          "Ruleset priority still names superseded documentation")
    citizens=rules["citizens"]
    check(citizens["activeHumanWorkersSoftCapScope"] ==
          "PER_PROFESSION_PER_NATION_DESIGN_CANDIDATE", "Quota scope drift")
    check(citizens["humanQuotaAssignment"] ==
          "deterministic_hash_rotation_per_profession_live_600s", "Quota rotation drift")
    check(citizens["humanWorkXpEligibility"] == "accepted_effective_work_only",
          "Phantom XP policy drift")
    required=schema["properties"]["citizens"]["required"]
    check(all(key in required for key in
              ("activeHumanWorkersSoftCapScope","humanQuotaAssignment",
               "humanWorkXpEligibility")), "JSON schema does not require quota/XP semantics")
    check("600 segundos" in master_text and "por profesión" in master_text,
          "Master lacks quota rotation semantics")
    check("XP de trabajo" in master_text,
          "Master lacks accepted-effective-work XP semantics")
    check(commands["join"]["precondition"] == "authenticated_provider_identity",
          "!join circular prereq: citizenship should not be required")
    check(commands["work"]["precondition"] == "registered_citizen",
          "!work must require prior citizen registration")
    check(delta["properties"]["nationId"].get("format") == "uuid",
          "Public nationId must be UUID in v2.5")
    check(set(delta["properties"]["factionId"]["enum"]) ==
          {"micelios","runicos","ferrinos"}, "Public factionId enum drift")
    check(manifest["status"] == "DESIGN_CANDIDATE_NOT_HASHED_OR_RELEASED",
          "Unreleased manifest must remain marked design candidate")
    expected=current(ptr,rules,manifest)
    target=ROOT/"CURRENT.md"
    observed=target.read_text(encoding="utf-8") if target.exists() else ""
    if observed != expected:
        if write:
            target.write_text(expected,encoding="utf-8")
            print("UPDATED CURRENT.md")
        else:
            errs.append("CURRENT.md stale: run python3 tools/check_active_spec.py --write")
    return errs

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--write",action="store_true")
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    errors=validate(args.write)
    if errors:
        for error in errors: print("FAIL:",error)
        raise SystemExit(1)
    print("PASS: current version authority, citizenship, quota, XP and ID contracts")
    print("NOTE: no runtime or provider access verified")
