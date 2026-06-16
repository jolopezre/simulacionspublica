# Biblioteca de referencia — Simulaciones virtuales en salud pública

Catálogo de buenas prácticas y ejemplos externos que sirven como modelo
para el repositorio UCSUR. Usar como guía de diseño (no copiar contenido
con derechos reservados; adaptar estructura y enfoque pedagógico).

## 1. CAN-Sim — Public Health Nursing VSG Series
**https://can-sim.ca/phn/**
Serie de 3 juegos (Evaluación comunitaria, Promoción de la salud,
Planificación y evaluación de programas) sobre seguridad alimentaria en
una comunidad ficticia. Estructura: video narrativo → decisión clínica de
opción múltiple → retroalimentación embebida (rationale correcto/
incorrecto) → avance condicionado a la respuesta correcta. Duración ~20
min por juego. Requiere Chrome/Firefox y audio. In Game 1 a reporter interviews a parent volunteer who expresses concern about the lack of school nutrition programs during the summer months in a city, and the public health nursing team decides to complete a community assessment using primary and secondary data sources.

**Modelo a replicar:**
- Caso narrativo continuo entre los 3 juegos (mismo escenario, distintas
  etapas del ciclo de salud comunitaria).
- Retroalimentación inmediata por decisión (no esperar al final).
- Pre-brief estandarizado (rol del facilitador, expectativas, lecturas
  previas, términos clave) antes de cada juego.

## 2. CAN-Sim — Companion Guide (Feb 2022)
**Developing Public Health Nursing Competencies through Virtual
Simulation Games – Companion Guide**
Documento marco que define: estándares INACSL (pre-briefing,
facilitación, debriefing, integridad profesional), modelos de debriefing
(3-D, 3-Fase, Multi-fase), rúbrica de autoevaluación tipo Likert 1–6 con
tres niveles descriptores (Competente/Intermedio/Novato), y mapeo de
competencias CASN por juego (Apéndice B).

**Adaptación para UCSUR:** sustituir el mapeo CASN por las competencias
del sílabo de Salud Pública/APS de UCSUR; mantener intacta la estructura
de pre-brief, debrief 3-D y rúbrica Likert.

## 3. CAN-Sim — Virtual Simulation Games (Open Source)
**https://can-sim.ca/virtual-simulation-games-open-source/**
Catálogo de VSGs cortas (5–20 min) de acceso libre sin membresía, en
áreas como antirracismo, vacunación, atención postparto con enfoque
trauma-informado, y la propia serie de seguridad alimentaria. A virtual simulation in which the learner assumes the role of a public health nurse conducting a community assessment that explores food insecurity as a population health issue, followed by a second simulation continuing that role to develop a population-based health promotion intervention with community partners.

**Relevancia:** confirma el patrón de "una comunidad, múltiples juegos
encadenados por etapa" — recomendado para el repositorio UCSUR (un caso
ancla con 3 escenarios: diagnóstico → promoción → planificación).

## 4. Schofield et al. (2023) — Public Health Nursing (Wiley)
*Developing simulation games to advance public health nursing
competence in baccalaureate education.*
Describe el desarrollo colaborativo entre 3 escuelas de enfermería
canadienses + CASN + CAN-Sim. The three games foster clinical reasoning and collaborative, community decision-making in response to population health issues during community assessment, evidence-informed health promotion planning, and evaluation processes.

**Relevancia metodológica:** valida el enfoque de "razonamiento clínico +
toma de decisiones colaborativa" como eje del diseño instruccional —
aplica directamente al componente de "reflexión abierta" del dashboard.

## 5. Revisión de literatura — Virtual Simulations in Community Health
Nursing Education (Springer)
Best practices in simulation development indicate that a framework should guide design, implementation, and evaluation, though further research is needed on assessment techniques and learning outcomes.

**Relevancia:** justifica incluir, desde el diseño inicial, instrumentos
de evaluación explícitos (rúbrica + debrief) y no solo la mecánica de
juego — coherente con el enfoque "paquete completo" del proyecto.

## 6. Otros catálogos CAN-Sim relevantes como inspiración de formato
- **Toolbox de heridas (wound care)**: 4 VSGs de duración variable +
  pre/post quiz — modelo de evaluación de conocimientos antes/después,
  aplicable como complemento a la rúbrica de autoevaluación.
- **Serie sobre racismo en entornos clínicos**: módulos cortos con
  preguntas reflexivas adicionales — modelo para nodos de tipo
  `open_reflection`.
- **Módulos sobre atención postparto trauma-informada**: ejemplo de cómo
  integrar un enfoque de equidad/determinantes sociales dentro de la
  narrativa de decisiones — relevante para escenarios de Salud Pública/
  APS en contextos de vulnerabilidad (Lima Metropolitana).

## Principios transversales extraídos para el repositorio UCSUR
1. **Ciclo narrativo continuo** (un caso, múltiples etapas/juegos).
2. **Feedback embebido inmediato** por decisión, con justificación breve.
3. **Pre-brief y debrief estandarizados** (3-D Model) en cada escenario.
4. **Rúbrica de autoevaluación Likert 1–6** mapeada a resultados de
   aprendizaje del sílabo.
5. **Acceso híbrido**: catálogo abierto + escenarios restringidos a
   curso/Moodle.
6. **Independencia tecnológica**: HTML autónomo, sin dependencias
   externas obligatorias, exportable a SCORM 1.2.

## Nota sobre vigencia de enlaces
CAN-Sim indica que sus simulaciones permanecerán alojadas y mantenidas
"hasta 2027" en su sitio (ver Companion Guide, sección "Optimizing
Simulation-Based Learning"). Para referencias externas en
`scenario.json`, preferir enlazar a páginas de aterrizaje
(`can-sim.ca/phn/`, `can-sim.ca/virtual-simulation-games-open-source/`)
en lugar de URLs profundas que puedan caducar.
