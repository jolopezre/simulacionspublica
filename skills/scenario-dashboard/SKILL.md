---
name: scenario-dashboard
description: >
  Use this skill to design and generate the interactive "scenario player"
  for a public-health virtual simulation game: a dashboard-style,
  decision-based simulation that combines (a) multiple-choice clinical/
  community decisions with immediate embedded feedback, (b) open-ended
  written-analysis prompts, and (c) a live mini-dashboard of
  epidemiological/community data the learner must interpret. Trigger when
  the user asks to "build the simulation dashboard", "create the scenario
  player", "make the case interactive", "design the decision flow", or
  references a specific case/scenario by name. Aligned to UCSUR's Salud
  Pública / APS syllabus (community diagnosis → priorization → planning →
  evaluation cycle) and to the CAN-Sim 3-D debrief model (Defusing,
  Discovery, Deepening).
license: Internal use - UCSUR Public Health Simulation Project
---

# Scenario Dashboard — Simulation Player Generator

## Purpose

Generate an intuitive, dashboard-style HTML player for a single
simulation scenario (`scenarios/<id>/player.html` +
`scenarios/<id>/scenario.json`), combining three interaction modes in one
coherent experience, per the project's decision: a hybrid of (1)
multiple-choice decisions with embedded feedback (CAN-Sim style), (2)
open-ended written justification, and (3) a community/epidemiological
data dashboard the learner consults before deciding.

## UCSUR Salud Pública / APS alignment

Structure every scenario around the **community health nursing /
community diagnosis cycle**, which mirrors both CAN-Sim's three games and
the typical UCSUR APS syllabus sequence:

| Stage | CAN-Sim equivalent | UCSUR APS competency focus |
|---|---|---|
| 1. Diagnóstico comunitario | Game 1 – Community Assessment | Recolección y análisis de datos primarios/secundarios, determinantes de salud, enfoque poblacional |
| 2. Priorización y promoción | Game 2 – Health Promotion | Selección de estrategias de promoción, participación comunitaria, enfoque de equidad |
| 3. Planificación y evaluación | Game 3 – Program Planning & Evaluation | Modelo lógico, marco de planificación, indicadores de evaluación |
| 4. Preparación y gobernanza en salud global | (extensión propia, no CAN-Sim) | Enfermedades infecciosas emergentes (EID), vigilancia transfronteriza, cooperación regional, cuyo marco de referencia es el ciclo de prospectiva estratégica (foresight) — ver `stage: "gobernanza"` |

A single scenario may cover one stage in depth (recommended for the
pilot) or all three as a multi-act simulation.

### Stage 4 — Preparación y Gobernanza (extensión foresight/APEC)

Esta etapa adapta el ciclo de prospectiva estratégica usado en talleres
de foresight (ej. APEC Center for Technology Foresight) a un escenario
de decisión jugable. Estructura narrativa híbrida recomendada:

1. **Acto local** (nodos `narrative_decision`/`open_reflection`): un
   caso clínico-comunitario concreto (brote zoonótico, evento centinela)
   que el estudiante diagnostica y notifica, igual que en stage
   `diagnostico`.
2. **Acto de escalamiento** (nodos posteriores en el mismo grafo): el
   caso se convierte en una decisión de gobernanza — el estudiante pasa
   de rol clínico a rol de delegado/asesor en un comité de cooperación
   regional, y debe decidir entre opciones que reflejan los tres pilares
   de EID (Enfermedades Infecciosas Emergentes):
   - **Clima-Ambiente-Zoonosis**: vigilancia de interfase
     humano-animal-ambiente.
   - **Tecnología-Vigilancia-Respuesta**: IA para pronóstico, diagnóstico
     rápido, plataformas de vacunas, salud digital.
   - **Gobernanza-Economía-Cooperación regional**: compartición de
     datos, confianza institucional, equidad, estabilidad económica.
3. **Matriz de escenarios 2×2** (opcional, como nodo `ending` múltiple):
   en vez de un solo final, se pueden definir hasta 4 finales que
   representen los cuadrantes de una matriz de incertidumbres críticas
   (ej. eje X: alta/baja confianza institucional; eje Y: alta/baja
   inversión en vigilancia tecnológica), replicando la metodología de
   matriz de escenarios 2×2 usada en talleres de foresight.

## Dashboard layout (the "intuitive, dashboard-type" requirement)

The player screen is divided into persistent regions so learners always
know where they are:

```
┌─────────────────────────────────────────────────────────┐
│  HEADER: scenario title · stage indicator · progress bar │
├───────────────┬─────────────────────────┬───────────────┤
│ LEFT PANEL     │  MAIN STAGE              │ RIGHT PANEL   │
│ "Expediente"   │  - Video/narrative card  │ "Mi Bitácora" │
│ - Case summary │  - Decision prompt       │ - Decisions   │
│ - Key terms    │  - Options (radio cards) │   log so far  │
│ - Data sources │  - Open-text reflection  │ - Self-rubric │
│   (mini charts,│  - Embedded feedback     │   live scores │
│    tables,     │    panel (slide-in)      │ - Notes       │
│    maps)       │                          │   (learner's  │
│                │                          │    own notes) │
├───────────────┴─────────────────────────┴───────────────┤
│ FOOTER: Atrás | Guardar y continuar | Ver Debrief         │
└─────────────────────────────────────────────────────────┘
```

- **Left panel ("Expediente")**: static reference material for the
  current stage — windshield-survey notes, Statistics/INEI-equivalent
  data tables, small bar/line charts (rendered with inline SVG, no
  external libs), maps or images. This is the "mini-dashboard" the
  learner must read before deciding.
- **Main stage**: the narrative (text-based scene description or
  embedded video placeholder), the decision node (multiple choice as
  selectable cards, each with a short rationale shown after selection —
  embedded debrief), AND/OR an open-text textarea for written
  justification (stored in the learner's session, optionally exported).
- **Right panel ("Mi Bitácora")**: running log of the learner's choices
  and a live self-assessment rubric (Likert 1–6 sliders per learning
  outcome) that updates as they progress — operationalizing CAN-Sim's
  Option 2 (self-debrief) continuously rather than only at the end.
- **Footer**: navigation + a "Ver Debrief" button that opens the 3-D
  model debrief questions (Defusing / Discovery / Deepening) as a modal
  at the end of the scenario.

## Data model (`scenario.json`)

```json
{
  "meta": {
    "id": "diag-comunitario-seguridad-alimentaria",
    "title": {"es": "Diagnóstico comunitario: seguridad alimentaria",
              "en": "Community diagnosis: food security"},
    "stage": "diagnostico",
    "competencies": ["..."],
    "duration_min": 25,
    "access": "public",
    "language_default": "es"
  },
  "dashboard_data": {
    "tables": [ {"title": {...}, "columns": [...], "rows": [...]} ],
    "charts": [ {"type": "bar", "title": {...}, "data": [...]} ],
    "documents": [ {"title": {...}, "summary": {...}, "link": "..."} ]
  },
  "nodes": [
    {
      "id": "n1",
      "type": "narrative_decision",
      "narrative": {"es": "...", "en": "..."},
      "prompt": {"es": "...", "en": "..."},
      "options": [
        {"id": "a", "text": {...}, "correct": true,
         "feedback": {"es": "...", "en": "..."}, "next": "n2"},
        {"id": "b", "text": {...}, "correct": false,
         "feedback": {...}, "next": "n1b"}
      ]
    },
    {
      "id": "n2",
      "type": "open_reflection",
      "prompt": {"es": "...", "en": "..."},
      "guidance": {"es": "Considere: ...", "en": "..."},
      "next": "n3"
    },
    {"id": "end_a", "type": "ending", "label": {...}, "summary": {...}}
  ],
  "rubric_ref": "rubric.json",
  "debrief_ref": "debrief.json"
}
```

- `nodes` form a **directed graph** (supports branching with multiple
  endings, per the project's requirement). `next` can point to
  different nodes depending on the option chosen — this is how
  multiple paths/endings are implemented.
- `type: "narrative_decision"` → embedded-feedback decision (CAN-Sim
  Option 1).
- `type: "open_reflection"` → free-text box; not scored automatically,
  but flagged in the bitácora for instructor review / self-debrief.
- `type: "ending"` → terminal node; triggers the debrief modal and
  rubric summary.

## Rendering rules

- Build `player.html` as a **single self-contained file** (inline
  CSS/JS, no external CDN dependencies) so it works offline, inside an
  `<iframe>`, or packaged in SCORM.
- Charts: simple inline SVG bar/line/pie generated from
  `dashboard_data.charts` — no charting library required, to keep the
  file portable.
- State: keep all learner state in memory (no `localStorage`); on
  reaching an `ending` node, render a printable summary (decisions +
  rubric self-scores + reflections) the learner can save as PDF via
  browser print.
- Bilingual toggle: a small ES/EN switch in the header swaps all
  `{es, en}` text fields live.
- Accessibility: every decision option is a `<button>`/`<label>` with
  visible focus states; color is never the only signal for
  correct/incorrect (use icon + text too).

## Debrief integration (`debrief.json`)

```json
{
  "defusing": {"es": ["¿Cómo se sintió durante...?", "..."], "en": [...]},
  "discovery": {"es": [...], "en": [...]},
  "deepening": {"es": [...], "en": [...]}
}
```
Shown as a modal triggered from any `ending` node, following the 3-D
Model (Zigmont, Kappus & Sudikoff, 2011) as used throughout the CAN-Sim
Companion Guide.

## Do / Don't

- DO design for a 20–30 minute session (CAN-Sim's stated benchmark).
- DO let every decision branch lead somewhere meaningful — avoid
  "dead-end" wrong answers that just loop back without new information.
- DON'T require a backend; everything must run from static files.
- DON'T mix languages within a single rendered string — always pull
  from the active language key.
