#!/usr/bin/env python3
"""Comprobación documental/declarativa de K0. No valida motor ni permisos LIVE."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = "MANIFIESTO_DOCUMENTAL_v2.2.md"
ROW = re.compile(r"^\| \x60([^\x60]+)\x60 \| (\d+) \| \x60([a-f0-9]{64})\x60 \|$", re.M)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
errors = []
count = 0

def check(ok, message):
    global count
    count += 1
    if not ok:
        errors.append(message)

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def tracked():
    p = subprocess.run(["git", "ls-files", "--cached"], cwd=ROOT, text=True,
                       capture_output=True, check=True)
    return sorted(x for x in p.stdout.splitlines() if x != MANIFEST)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def manifest_text():
    paths = tracked()
    counts = Counter(Path(p).suffix for p in paths)
    types = "{" + ", ".join(f"{k!r}: {counts[k]}" for k in sorted(counts)) + "}"
    tick = chr(96)
    lines = [f"| {tick}{p}{tick} | {(ROOT/p).stat().st_size} | {tick}{digest(ROOT/p)}{tick} |"
             for p in paths]
    return ("# Inventario documental activo — K0 v2.2\n\n"
            "**Inventario de bytes; no certificación funcional, visual ni legal.** "
            "El manifiesto v2.1 es histórico.\n\n"
            f"Archivos enumerados (sin este manifiesto): {len(paths)}. Tipos: {types}.\n\n"
            "| Archivo | Tamaño (bytes) | SHA-256 |\n|---|---:|---|\n"
            + "\n".join(lines) + "\n")

def verify_manifest():
    listed = {}
    for path, size, sha in ROW.findall((ROOT/MANIFEST).read_text(encoding="utf-8")):
        check(path not in listed, f"Manifiesto duplica {path}")
        listed[path] = (int(size), sha)
    actual = set(tracked())
    check(set(listed) == actual, f"Manifiesto: faltan {sorted(actual-set(listed))}; sobran {sorted(set(listed)-actual)}")
    for path in sorted(actual & set(listed)):
        check((ROOT/path).stat().st_size == listed[path][0], f"Manifiesto tamaño obsoleto {path}")
        check(digest(ROOT/path) == listed[path][1], f"Manifiesto SHA obsoleto {path}")

def verify_links():
    chapters = {p for p in tracked() if re.fullmatch(r"docs/\d\d_[^/]+\.md", p)}
    check(len(chapters) == 62, "El repositorio no tiene 62 capítulos numerados")
    index = (ROOT/"DOCS_INDEX_v2.2.md").read_text(encoding="utf-8")
    indexed = set(re.findall(r"\]\((docs/\d\d_[^)#]+\.md)(?:#[^)]*)?\)", index))
    check(indexed == chapters, f"Índice: faltan {sorted(chapters-indexed)}; sobran {sorted(indexed-chapters)}")
    for path in tracked():
        if not path.endswith(".md"):
            continue
        for dest in LINK.findall((ROOT/path).read_text(encoding="utf-8")):
            dest = dest.strip().split(" ", 1)[0].strip("<>")
            if not dest or dest.startswith(("http://", "https://", "#", "mailto:", "data:")):
                continue
            name = unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if not name:
                continue
            target = ((ROOT/path).parent/name).resolve()
            inside = target.is_relative_to(ROOT.resolve())
            check(inside, f"{path}: enlace fuera del repositorio {dest}")
            if inside:
                check(target.exists(), f"{path}: enlace roto {dest}")

def verify_schemas():
    import jsonschema
    import yaml
    for file in (ROOT/"contracts").glob("*.schema.json"):
        jsonschema.Draft202012Validator.check_schema(json.loads(file.read_text(encoding="utf-8")))
    sources = {
        "contracts/ruleset.schema.json": ["data/ruleset.v2.json"],
        "contracts/channel_binding.schema.json": ["data/channel_bindings.example.json"] +
            [f"data/channel_presets/{p.name}" for p in sorted((ROOT/"data/channel_presets").glob("*.json"))],
    }
    for schema_path, paths in sources.items():
        validator = jsonschema.Draft202012Validator(load(schema_path))
        for path in paths:
            for problem in validator.iter_errors(load(path)):
                errors.append(f"{path}: {problem.json_path}: {problem.message}")
    # Public SignalR event contracts are explicit and deny unknown fields,
    # including provider identities and unmoderated text.
    event_schema = load("contracts/signalr_events.v2.2.schema.json")
    event_validator = jsonschema.Draft202012Validator(
        event_schema, format_checker=jsonschema.FormatChecker())
    for example in sorted((ROOT/"contracts/examples").glob("*.json")):
        event = json.loads(example.read_text(encoding="utf-8"))
        for problem in event_validator.iter_errors(event):
            errors.append(f"{example.relative_to(ROOT)}: {problem.message}")
        leaked = dict(event)
        leaked["providerUserId"] = "should-not-be-allowed"
        check(not event_validator.is_valid(leaked),
              f"SignalR schema exposes provider identity for {example.name}")
    api = yaml.safe_load((ROOT/"contracts/openapi.v2.yaml").read_text(encoding="utf-8"))
    check(api.get("info", {}).get("version") == "2.2.0",
          "OpenAPI should advertise its additive 2.2.0 design contract")
    check(str(api.get("openapi", "")).startswith("3.1."), "OpenAPI debe ser 3.1.x")
    check(bool(api.get("paths")), "OpenAPI sin rutas")
    def refs(node):
        if isinstance(node, dict):
            if "$ref" in node:
                yield node["$ref"]
            for val in node.values():
                yield from refs(val)
        if isinstance(node, list):
            for val in node:
                yield from refs(val)
    for ref in refs(api):
        if not isinstance(ref, str) or not ref.startswith("#/"):
            continue
        cur = api
        for part in ref[2:].split("/"):
            part = part.replace("~1", "/").replace("~0", "~")
            if not isinstance(cur, dict) or part not in cur:
                errors.append(f"OpenAPI referencia inexistente: {ref}")
                break
            cur = cur[part]

def verify_catalogs():
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            check(True, f"JSON válido {path}")
        except json.JSONDecodeError as exc:
            errors.append(f"JSON inválido {path.relative_to(ROOT)}: {exc}")
    rules = load("data/ruleset.v2.json")
    eras = load("data/eras.v2.json")["eras"]
    building = load("data/buildings.v2.json")["buildingCatalog"]
    strategic = load("data/strategic_projects.v2.json")
    tech = load("data/technologies.v2.json")["technologies"]
    milestones = load("data/milestones.v2.json")["milestones"]
    units = load("data/combat_units.v2.2.json")["units"]
    professions = load("data/professions.v2.json")["professions"]
    catalogs = {
        "eras": (eras, 13), "buildings": (building, 130),
        "projects": (strategic["projects"], 39), "wonders": (strategic["wonders"], 13),
        "technologies": (tech, 39), "milestones": (milestones, 65),
        "skills": (load("data/skills.v2.json")["choices"], 30),
        "units": (units, 39), "governments": (load("data/governments.v2.json")["candidates"], 9),
        "professions": (professions, 5),
    }
    era_ids, tech_ids, building_ids = ({e["id"] for e in eras},
                                       {t["id"] for t in tech},
                                       {b["id"] for b in building})
    for name, (items, size) in catalogs.items():
        check(len(items) == size, f"{name}: esperado {size}, observado {len(items)}")
        key = "characterId" if name == "governments" else "id"
        ids = [i[key] for i in items]
        check(len(set(ids)) == len(ids), f"{name}: IDs duplicados")
        for item in items:
            if "eraId" in item:
                check(item["eraId"] in era_ids, f"{name}/{item.get('id')}: era inexistente")
    check(len(load("data/legacy_user_decisions_1_92.json")["decisions"]) == 92, "Faltan decisiones originales")
    check(set(rules["nations"]["factionIds"]) == {"micelios", "runicos", "ferrinos"}, "Facciones incorrectas")
    for b in building:
        dep = b.get("requiresTechId")
        check(dep is None or dep in tech_ids, f"{b['id']}: tecnología no encontrada")
        if b["family"] in ("workshop", "research"):
            check(dep == "tech_" + b["eraId"], f"{b['id']}: requiere troncal incorrecta")
        check(b["cost"].get("gold", 0) == 0, f"{b['id']}: oro prohibido")
    graph = {t["id"]: t.get("requires", []) for t in tech}
    for t in tech:
        for dep in t.get("requires", []):
            check(dep in tech_ids, f"{t['id']}: prerequisito inexistente {dep}")
        for dest in t.get("unlocks", []):
            check(dest in building_ids, f"{t['id']}: unlock inexistente {dest}")
    visited, active = set(), set()
    def visit(node):
        if node in active:
            errors.append(f"Ciclo tecnológico: {node}")
            return
        if node in visited:
            return
        active.add(node)
        for dep in graph[node]:
            if dep in graph:
                visit(dep)
        active.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)
    for era in eras:
        e = era["id"]
        subset = [m for m in milestones if m["eraId"] == e]
        check(len(subset) == 5 and sum(m["points"] for m in subset) == 100, f"{e}: hitos != 5/100")
        check(len([b for b in building if b["eraId"] == e]) == 10, f"{e}: edificios != 10")
        check(len([t for t in tech if t["eraId"] == e]) == 3, f"{e}: tecnologías != 3")
        check(len([u for u in units if u["eraId"] == e]) == 3, f"{e}: unidades != 3")
    for item in strategic["projects"] + strategic["wonders"]:
        check(item["cost"].get("gold", 0) == 0, f"{item['id']}: oro != 0")
        check(item.get("historicalPoints", 0) == 0, f"{item['id']}: puntos históricos indebidos")
    check({u["role"] for u in units} == {"guard", "scout", "heavy"}, "Roles de unidades incoherentes")
    for u in units:
        check(set(u["factionSkins"]) == set(rules["nations"]["factionIds"]), f"{u['id']}: skins")
    manifest = load("data/content_manifest.v2.json")
    check(manifest["rulesetHash"] == digest(ROOT/"data/ruleset.v2.json"), "Hash ruleset desincronizado")
    for path in manifest["contentFiles"]:
        check((ROOT/"data"/path).is_file(), f"Falta archivo de contenido {path}")
    # Contrato: SHA-256 de pares ordenados [filename, objeto JSON], con claves
    # ordenadas recursivamente y JSON compacto UTF-8. No ordenar arrays.
    payload = [[name, load("data/" + name)] for name in manifest["contentFiles"]]
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False,
                           separators=(",", ":")).encode("utf-8")
    check(hashlib.sha256(canonical).hexdigest() == manifest["contentHash"],
          "data/content_manifest: contentHash no coincide con 16 catálogos canónicos")

def verify_regressions():
    forbidden = {
        "docs/05_EDIFICIOS_Y_MAPA.md": "Si el voto pierde financiación por reverso oro",
        "docs/19_MAQUINAS_DE_ESTADO_Y_ERRORES.md": "RESOLVED → PAYMENT_BLOCKED",
        "architecture/02_TRANSACTIONS_Y_INVARIANTES.md": "ningún Consejo se confirma",
        "docs/43_EJERCITOS_Y_COMBATE_AUTOMATICO_v2.2.md": "guardia→explorador→especialista",
    }
    for path, phrase in forbidden.items():
        check(phrase not in (ROOT/path).read_text(encoding="utf-8"),
              f"Regla histórica obsoleta: {path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_manifest:
        (ROOT/MANIFEST).write_text(manifest_text(), encoding="utf-8")
        print("Manifiesto actualizado")
    for phase in (verify_links, verify_schemas, verify_catalogs, verify_regressions, verify_manifest):
        try:
            phase()
        except Exception as exc:
            errors.append(f"{phase.__name__}: {type(exc).__name__}: {exc}")
    if errors:
        print(f"FAIL: {len(errors)} errores / {count} comprobaciones")
        for msg in errors:
            print(" - " + msg)
        return 1
    print(f"PASS: {count} comprobaciones declarativas. No valida D2–D4.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
