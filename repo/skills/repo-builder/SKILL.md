---
name: repo-builder
description: >
  Use this skill to scaffold, structure, and deploy a public-health virtual
  simulation game (VSG) repository that runs in online environments
  (web browser, LMS/SCORM package, or static hosting). Trigger when the
  user asks to "create the repository", "set up the simulation site",
  "package for the LMS/Moodle", "build the catalog of scenarios", or
  "deploy/export the simulation games". Produces a hybrid deliverable:
  a self-contained interactive HTML site (catalog + player) AND a SCORM
  1.2-compatible export for institutional LMS (e.g., UCSUR Moodle).
  Follows CAN-Sim (can-sim.ca) conventions for game structure, pre-brief,
  embedded debrief, and self-assessment rubrics.
license: Internal use - UCSUR Public Health Simulation Project
---

# Repo Builder — Public Health Simulation Repository

## Purpose

Build and maintain a repository of virtual simulation games (VSGs) for
public health / community health nursing & public health education,
modeled on the CAN-Sim framework (Companion Guide, Feb 2022) and adapted
for the UCSUR Salud Pública / APS (Atención Primaria de Salud) syllabus.

The repository must work in **online environments** with no special
infrastructure required:

1. **Static catalog site** — a single `index.html` (or small set of
   files) listing all available scenarios as cards, filterable by
   competency domain, topic, and difficulty. Built with plain HTML/CSS/JS
   so it can be hosted on GitHub Pages, Netlify, an institutional web
   server, or opened locally.
2. **SCORM export** — each scenario can be packaged as a SCORM 1.2
   `.zip` (imsmanifest.xml + HTML player) so it can be uploaded directly
   into UCSUR's Moodle as a SCORM activity, with completion/score
   tracked via `window.parent.API` (SCORM 1.2 `LMSSetValue`).
3. **Embeddable widget** — each scenario's player is also a standalone
   HTML file that can be embedded via `<iframe>` in any LMS page (mixed
   access model: public catalog + restricted scenarios behind LMS login).

## Repository structure (canonical)

```
/repo
  /index.html              <- catalog (public)
  /assets/
    /css/styles.css
    /js/catalog.js
    /img/...
  /scenarios/
    /<scenario-id>/
      scenario.json         <- single source of truth (see scenario-editor skill)
      player.html            <- standalone interactive player
      rubric.json            <- self-assessment rubric (CAN-Sim style)
      debrief.json            <- 3-D model debrief questions
      manifest.xml           <- SCORM 1.2 manifest (generated)
      README.md               <- scenario summary, learning outcomes, credits
  /docs/
    teacher-guide.md          <- companion guide for instructors
    student-guide.md
  /templates/
    scenario-template.json
    rubric-template.json
```

Each scenario is **self-contained**: `scenario.json` is the only file
that needs editing (via the `scenario-editor` skill's visual wizard);
`player.html` is a generic rendering engine that loads `scenario.json`
at runtime.

## Workflow

1. **Scaffold**: create the folder structure above. If it already
   exists, only add what's missing — never overwrite `scenario.json`
   files without confirmation.
2. **Catalog generation**: scan `/scenarios/*/scenario.json`, extract
   `meta` block (title, competencies, domain, duration, language,
   access level), and regenerate `index.html`'s card grid + filters.
   Access levels: `public` (catalog visible + playable without login)
   vs `restricted` (catalog card visible, "Abrir en Moodle" / login
   required to play).
3. **Player generation**: copy the generic `player.html` engine into
   each scenario folder (or reference a shared one via relative path
   `../../assets/js/player-engine.js`), pointing it at the scenario's
   `scenario.json`.
4. **SCORM packaging** (on request): generate `imsmanifest.xml` per
   scenario using the SCORM 1.2 template below, zip
   `player.html + scenario.json + assets` into
   `<scenario-id>-scorm12.zip`.
5. **Validation**: check that every scenario referenced in the catalog
   has the required files (`scenario.json`, `player.html`,
   `rubric.json`); report missing pieces instead of failing silently.

## SCORM 1.2 manifest template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="COM_{{SCENARIO_ID}}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-{{SCENARIO_ID}}">
    <organization identifier="ORG-{{SCENARIO_ID}}">
      <title>{{SCENARIO_TITLE}}</title>
      <item identifier="ITEM-1" identifierref="RES-1">
        <title>{{SCENARIO_TITLE}}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco"
      href="player.html">
      <file href="player.html"/>
      <file href="scenario.json"/>
      <file href="rubric.json"/>
    </resource>
  </resources>
</manifest>
```

The `player.html` engine must call, when running inside an LMS frame:
- `LMSInitialize("")` on load
- `LMSSetValue("cmi.core.lesson_status", "completed")` when the
  scenario reaches an ending node
- `LMSSetValue("cmi.core.score.raw", <rubric_self_score>)` if the
  self-assessment rubric is completed
- `LMSFinish("")` on unload

Wrap all SCORM calls in try/catch so the player degrades gracefully
when opened standalone (no LMS present) — this is what enables the
"public catalog" mode.

## Access model (hybrid public / restricted)

- `meta.access: "public"` → catalog links directly to
  `scenarios/<id>/player.html` (works standalone, no login).
- `meta.access: "restricted"` → catalog shows a description card with
  a button "Disponible en el curso (Moodle)" linking to the LMS course
  URL placeholder (`meta.lms_url`). Never bundle restricted scenario
  content into the public static site.

## Conventions inherited from CAN-Sim

- Every scenario has: **Case Summary**, **Learning Outcomes** (mapped to
  competency framework — for UCSUR use the course's syllabus
  competencies; for nursing-aligned content, CASN domains as in the
  Companion Guide Appendix B), **Pre-Brief** checklist, **Instructions**
  (how the game works — video/decision/feedback loop), **Embedded
  Debrief** (immediate feedback per decision, per CAN-Sim Option 1),
  and a **Self-Assessment Rubric** (Likert 1–6, Competent/Intermediate/
  Novice descriptors, per CAN-Sim Option 2).
- Maintain bilingual fields (`es` / `en`) for all user-facing text in
  `scenario.json` — see `templates/scenario-template.json`.
- Reference CAN-Sim's hosting note: resources are intended to remain
  freely accessible "until 2027" per their Companion Guide — when in
  doubt about external links, prefer linking to `can-sim.ca` landing
  pages over deep links that may rot.

## Do / Don't

- DO keep `player.html` engine generic — never hardcode scenario
  content into the player; everything content-related lives in
  `scenario.json`.
- DO regenerate the catalog after any scenario is added/edited.
- DON'T duplicate rubric/debrief content inside `scenario.json` if it's
  already in `rubric.json`/`debrief.json` — reference by scenario id.
- DON'T invent CASN/competency mappings — use the ones supplied by the
  user's syllabus or the CAN-Sim Companion Guide Appendix B as a base
  and clearly mark any adaptation.
