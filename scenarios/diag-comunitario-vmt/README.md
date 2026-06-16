# Diagnóstico Comunitario: Seguridad Alimentaria en VMT

**Etapa:** 1 — Diagnóstico Comunitario
**Curso:** Salud Comunitaria y APS — UCSUR
**Duración estimada:** 25 minutos
**Acceso:** Público (no requiere login)
**Idiomas:** Español (predeterminado) / English

## Resumen del caso

Una/un interno(a) de enfermería en el Centro de Salud Las Palmeras (AAHH
Las Palmeras, Villa María del Triunfo, Lima) forma parte del equipo de
APS que debe responder ante el cierre de comedores escolares durante el
receso vacacional, en un contexto de alta inseguridad alimentaria. El
escenario guía al estudiante a través del proceso de diagnóstico
comunitario: identificación de un marco apropiado, integración de
fuentes primarias y secundarias, análisis de determinantes/fortalezas, y
comunicación participativa de resultados.

## Resultados de aprendizaje (mapeados a rubric.json)

1. Identifica una herramienta/marco apropiado para el diagnóstico
   comunitario con enfoque de seguridad alimentaria.
2. Recopila información de fuentes secundarias (INEI, ENDES, reportes
   municipales) para identificar tendencias epidemiológicas y
   determinantes de la salud.
3. Recopila información de fuentes primarias (visita comunitaria,
   entrevistas a informantes clave, mesas de trabajo) para identificar
   percepciones comunitarias.
4. Analiza la información recolectada para identificar fortalezas y
   necesidades comunitarias relacionadas con la inseguridad alimentaria.
5. Comunica el proceso y resultados del diagnóstico a actores clave para
   orientar la priorización en APS.

## Estructura del escenario

- 6 nodos de decisión/reflexión, 2 finales posibles (rama "diagnóstico
  participativo completo" vs. "diagnóstico técnico sin partenariado").
- 1 nodo de reflexión abierta (análisis de determinantes y fortalezas a
  partir de los datos del Expediente).
- Panel "Expediente": tabla de indicadores, gráfico de inseguridad
  alimentaria por grupo etario, 2 documentos de referencia.
- Debrief 3-D (Defusing / Discovery / Deepening) al finalizar.
- Rúbrica de autoevaluación Likert 1–6, 5 resultados de aprendizaje.

## Archivos

| Archivo | Función |
|---|---|
| `scenario.json` | Fuente única de verdad (narrativa, datos, grafo de decisiones) |
| `rubric.json` | Rúbrica de autoevaluación |
| `debrief.json` | Preguntas de debriefing 3-D |
| `player.html` | Motor del simulador (carga los JSON vía `fetch` — usar en hosting HTTP) |
| `player-standalone.html` | Versión autónoma con datos embebidos (usar para abrir directamente, sin servidor, o como recurso SCORM) |
| `imsmanifest.xml` | Manifest SCORM 1.2 (apunta a `player-standalone.html`) |

## Cómo editar este escenario

Usar el editor visual (`/editor.html` en la raíz del repositorio) para
modificar narrativa, decisiones, datos del expediente, rúbrica o
preguntas de debriefing sin tocar JSON directamente. Ver
`skills/scenario-editor/SKILL.md`.

## Créditos

Adaptado del marco CAN-Sim (*Developing Public Health Nursing
Competencies through Virtual Simulation Games*, Companion Guide, 2022)
para el curso de Salud Pública / APS, UCSUR. Caso ficticio ambientado en
Lima Metropolitana — cualquier semejanza con personas o instituciones
reales es coincidental.
