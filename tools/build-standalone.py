#!/usr/bin/env python3
"""
build-standalone.py
===================
Regenera el archivo player-standalone.html para TODOS los escenarios
del repositorio, embebiendo scenario.json + rubric.json + debrief.json
directamente en el HTML (sin necesidad de servidor HTTP).

Uso:
    python3 tools/build-standalone.py

Ejecutar desde la RAÍZ del repositorio (donde está index.html).

Requisitos: Python 3.6+, sin dependencias externas.
"""

import json
import re
import os
import sys
from pathlib import Path

# ── Configuración ─────────────────────────────────────────────────
SCENARIOS_DIR  = Path("scenarios")
PLAYER_TEMPLATE = Path("scenarios/diag-comunitario-vmt/player.html")
OUTPUT_NAME    = "player-standalone.html"
# ──────────────────────────────────────────────────────────────────


def build_standalone(scenario_dir: Path, player_html: str) -> bool:
    """
    Construye player-standalone.html para un escenario dado.
    Devuelve True si tuvo éxito, False si faltó algún archivo.
    """
    scenario_json = scenario_dir / "scenario.json"
    rubric_json   = scenario_dir / "rubric.json"
    debrief_json  = scenario_dir / "debrief.json"

    missing = [f for f in [scenario_json, rubric_json, debrief_json] if not f.exists()]
    if missing:
        print(f"  ⚠  Archivos faltantes en {scenario_dir.name}: "
              f"{', '.join(m.name for m in missing)} — omitiendo.")
        return False

    scenario_txt = scenario_json.read_text(encoding="utf-8")
    rubric_txt   = rubric_json.read_text(encoding="utf-8")
    debrief_txt  = debrief_json.read_text(encoding="utf-8")

    # Validar JSON antes de incrustar
    for label, txt in [("scenario.json", scenario_txt),
                        ("rubric.json",   rubric_txt),
                        ("debrief.json",  debrief_txt)]:
        try:
            json.loads(txt)
        except json.JSONDecodeError as e:
            print(f"  ✗  JSON inválido en {scenario_dir.name}/{label}: {e}")
            return False

    inline = f"""
const __SCENARIO__ = {scenario_txt};
const __RUBRIC__   = {rubric_txt};
const __DEBRIEF__  = {debrief_txt};

async function loadData(){{
  scenario = __SCENARIO__; rubric = __RUBRIC__; debrief = __DEBRIEF__;
  LANG = scenario.meta.language_default || "es";
  setLang(LANG, true);
  initSCORM();
  renderExpediente();
  renderRubricGrid();
  currentNodeId = scenario.nodes[0].id;
  history = [{{nodeId:currentNodeId, optId:null, points:0}}];
  renderNode();
  updateScore();
  document.getElementById("credits").textContent = bi(scenario.meta.credits);
}}
""".strip()

    pattern = re.compile(r"async function loadData\(\)\{.*?\n\}\n", re.S)
    output = pattern.sub(inline + "\n", player_html, count=1)

    if output == player_html:
        print(f"  ✗  No se encontró la función loadData() en player.html — "
              f"¿el template es correcto?")
        return False

    out_path = scenario_dir / OUTPUT_NAME
    out_path.write_text(output, encoding="utf-8")

    # Verificación rápida
    sc = json.loads(scenario_txt)
    title = sc.get("meta", {}).get("title", {}).get("es", scenario_dir.name)
    size_kb = round(len(output) / 1024, 1)
    print(f"  ✓  {scenario_dir.name}  →  {OUTPUT_NAME}  ({size_kb} KB)  |  {title[:55]}")
    return True


def main():
    # Asegurarse de estar en la raíz del repositorio
    if not SCENARIOS_DIR.is_dir():
        print(f"\n✗  No se encontró la carpeta '{SCENARIOS_DIR}'.")
        print("   Ejecuta este script desde la RAÍZ del repositorio:\n")
        print("       cd simulaciones-ucsur/")
        print("       python3 tools/build-standalone.py\n")
        sys.exit(1)

    if not PLAYER_TEMPLATE.exists():
        print(f"\n✗  No se encontró el template en '{PLAYER_TEMPLATE}'.")
        print("   El escenario 'diag-comunitario-vmt' debe existir como referencia del motor.\n")
        sys.exit(1)

    player_html = PLAYER_TEMPLATE.read_text(encoding="utf-8")

    # Buscar todos los directorios con scenario.json
    scenario_dirs = sorted([
        d for d in SCENARIOS_DIR.iterdir()
        if d.is_dir() and (d / "scenario.json").exists()
    ])

    if not scenario_dirs:
        print("\n⚠  No se encontraron escenarios en la carpeta 'scenarios/'.\n")
        sys.exit(0)

    print(f"\n{'='*58}")
    print(f"  build-standalone.py — Repositorio Simulaciones UCSUR")
    print(f"{'='*58}")
    print(f"  Template: {PLAYER_TEMPLATE}")
    print(f"  Escenarios encontrados: {len(scenario_dirs)}\n")

    ok = 0
    fail = 0
    for d in scenario_dirs:
        result = build_standalone(d, player_html)
        if result:
            ok += 1
        else:
            fail += 1

    print(f"\n{'='*58}")
    print(f"  Completado: {ok} exitosos, {fail} con errores.")
    if ok > 0:
        print(f"\n  Archivos generados en cada carpeta de escenario:")
        print(f"  scenarios/<id>/{OUTPUT_NAME}")
    print(f"{'='*58}\n")


if __name__ == "__main__":
    main()
