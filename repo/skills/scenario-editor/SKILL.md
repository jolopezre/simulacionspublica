---
name: scenario-editor
description: >
  Use this skill to create or modify the no-code visual "scenario wizard"
  — an HTML form-based editor that lets faculty without programming
  experience build and edit branching virtual-simulation scenarios
  (CAN-Sim style) and export/import the resulting scenario.json. Trigger
  when the user asks to "edit a scenario", "create a new case", "add a
  decision point", "change the branching/endings", "build the editor", or
  "let teachers create their own scenarios". Always produces/consumes the
  same scenario.json schema used by the scenario-dashboard skill, so
  edited scenarios drop directly into the repo-builder catalog.
license: Internal use - UCSUR Public Health Simulation Project
---

# Scenario Editor — No-Code Visual Wizard

## Purpose

Provide a **form-based, step-by-step wizard** (single HTML file,
`editor.html`) so instructors (e.g., UCSUR Salud Pública / APS faculty)
can author or edit branching scenarios without touching JSON directly,
while always producing a valid `scenario.json` compatible with the
`scenario-dashboard` player and the `repo-builder` catalog.

## Wizard structure (steps)

1. **Metadatos** — title (ES/EN), stage (diagnóstico / promoción /
   planificación), competencies (free-text tags, pre-filled with
   syllabus competency list if provided), duration, access level
   (público/restringido), language default.
2. **Tablero de datos (Expediente)** — add reference tables, simple
   charts (bar/line — enter label+value pairs, the wizard renders an SVG
   preview live), and reference documents (title + short summary + link).
   This becomes `dashboard_data`.
3. **Mapa de decisiones (branching graph)** — visual node list:
   - Add a node → choose type: *Narrativa + Decisión*, *Reflexión
     abierta*, or *Final (ending)*.
   - For *Narrativa + Decisión*: narrative text, prompt, and 2–4 options;
     each option has correct/incorrect flag, feedback text, and a
     dropdown to select the **next node** (populated from existing node
     ids) — this is how multiple paths/endings are wired without writing
     graph syntax.
   - For *Reflexión abierta*: prompt + optional guidance text + next
     node.
   - For *Final*: label + summary text shown to the learner.
   - A live **mini graph preview** (simple SVG boxes + arrows, generated
     from the node list and `next` links) shows the branching structure
     so instructors can visually verify there are no orphan/dead nodes.
4. **Rúbrica de autoevaluación** — one row per learning outcome, with
   the three CAN-Sim descriptor levels (Competente / Intermedio /
   Novato) and the Likert 1–6 scale pre-configured. Produces
   `rubric.json`.
5. **Preguntas de debriefing** — three text areas (Defusing / Discovery
   / Deepening), pre-populated with CAN-Sim's sample questions as
   editable placeholders. Produces `debrief.json`.
6. **Revisión y exportación** — preview the full scenario in an embedded
   `scenario-dashboard` player (iframe), then export three files:
   `scenario.json`, `rubric.json`, `debrief.json` (download as a zip or
   individually). Also supports **import**: load an existing
   `scenario.json` to continue editing.

## Validation rules (run before export)

- Every `next` reference must point to an existing node id, or to
  `"end"`.
- Every branch must eventually reach a node of `type: "ending"` — warn
  (don't block) if a path seems to loop indefinitely.
- At least one `ending` node must exist.
- Bilingual fields: warn if `en` is empty when `language_default` !=
  "en" and the project requires bilingual content (default: warn, not
  block, so instructors can fill English later).
- Rubric: each learning outcome row must have non-empty descriptors for
  all three levels.

## Implementation notes

- Single self-contained `editor.html` (inline CSS/JS), no backend —
  state lives in the page; export via `Blob` + `<a download>` (this
  works in Claude.ai artifacts and in any static hosting).
- Reuse the exact same bilingual `{es, en}` field convention and node
  schema documented in the `scenario-dashboard` skill — do not invent a
  parallel schema.
- The "live preview" step should literally instantiate the
  scenario-dashboard player engine with the in-progress JSON (e.g., via
  `postMessage` to an iframe, or by re-rendering the same render
  function in-page) so instructors see exactly what students will see.
- Keep the graph preview lightweight: simple boxes positioned in a
  grid/columns by depth-from-start, arrows as SVG lines — no external
  graph library.

## Do / Don't

- DO pre-fill new scenarios with the CAN-Sim 3-D debrief sample
  questions and a blank rubric matching the scenario's stated learning
  outcomes (one row per outcome).
- DO let instructors duplicate an existing node as a starting point for
  a new branch (common pattern: copy a decision node, change the
  options/feedback, rewire `next`).
- DON'T allow export if validation finds zero `ending` nodes — that
  would produce an unplayable scenario.
- DON'T require instructors to understand JSON, node ids, or graphs as
  prerequisites — all of that should be generated/managed by the wizard
  UI (the visible node ids can be simple labels like "Decisión 1",
  "Final A").
