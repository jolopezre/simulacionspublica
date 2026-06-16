# Manual Docente — Repositorio de Simulaciones Virtuales de Salud Pública (UCSUR)

**Curso:** Salud Comunitaria y Atención Primaria de Salud (APS)
**Marco pedagógico:** adaptado de CAN-Sim (*Developing Public Health
Nursing Competencies through Virtual Simulation Games*, Companion Guide,
2022)
**Idiomas:** Español / English

---

## 1. ¿Qué es este repositorio?

Un conjunto de simulaciones virtuales interactivas ("juegos de
simulación") que permiten a los estudiantes practicar el ciclo de
trabajo en salud comunitaria y APS — diagnóstico, promoción y
planificación/evaluación — a través de casos narrativos con decisiones
ramificadas, retroalimentación inmediata, datos epidemiológicos/
comunitarios para analizar, y un modelo de debriefing estructurado.

Cada simulación dura entre 20 y 30 minutos y puede usarse:

- **De forma autónoma**, como tarea asincrónica antes/después de una
  clase o práctica.
- **En clase**, proyectada y discutida en grupo (especialmente útil para
  el debriefing).
- **Integrada en Moodle**, como actividad SCORM con seguimiento de
  finalización.

## 2. Estructura pedagógica (modelo CAN-Sim)

Cada escenario sigue cuatro fases:

1. **Pre-Brief** (a cargo del docente, ver sección 4): orienta al
   estudiante sobre el caso, términos clave, y expectativas.
2. **Juego interactivo**: el estudiante navega el "Expediente" (panel
   de datos), toma decisiones con retroalimentación inmediata, y
   responde una pregunta de reflexión abierta.
3. **Autoevaluación continua**: una rúbrica Likert 1–6 (panel "Mi
   Bitácora") se actualiza en vivo mientras el estudiante avanza.
4. **Debriefing 3-D** (Defusing → Discovery → Deepening): preguntas que
   el estudiante puede responder individualmente o, idealmente, discutir
   en grupo con facilitación docente.

## 3. Cómo usar el repositorio

### 3.1 Acceso

- Abrir `index.html` (catálogo) en un navegador, o publicarlo en
  GitHub Pages / servidor institucional (ver sección 6, "Hosting").
- Cada tarjeta del catálogo indica la etapa (Diagnóstico / Promoción /
  Planificación), duración estimada y competencias.
- Escenarios marcados como **"Disponible en el curso (Moodle)"** son de
  acceso restringido — el botón dirige al curso correspondiente.

### 3.2 Asignar una simulación

1. Seleccione el escenario alineado con la sesión de clase.
2. Comparta el enlace directo (`scenarios/<id>/player.html` o
   `player-standalone.html`) o publíquelo como actividad SCORM en
   Moodle (ver sección 6).
3. Indique a los estudiantes la duración estimada y si deberán entregar
   evidencia (ej. captura del resumen final, ver 3.4).

### 3.3 Durante la simulación

El estudiante interactúa con tres paneles:

- **Expediente** (izquierda): datos que debe consultar antes de decidir
  — tablas de indicadores, gráficos, documentos de referencia.
- **Pantalla principal** (centro): narrativa, preguntas de decisión con
  retroalimentación inmediata, y preguntas de reflexión abierta.
- **Mi Bitácora** (derecha): registro de decisiones tomadas y
  autoevaluación Likert en vivo.

Al llegar a un final, se habilita el botón **"Ver Debrief"** (preguntas
3-D) y **"Imprimir/Guardar resumen"** (decisiones + reflexiones +
puntajes de autoevaluación, en una ventana imprimible/PDF).

### 3.4 Evidencia de aprendizaje

Si se requiere evidencia de finalización:

- **Modo autónomo**: pedir al estudiante que use "Imprimir/Guardar
  resumen" y entregue el PDF/captura.
- **Modo SCORM/Moodle**: la plataforma registra automáticamente el
  estado "completado" y un puntaje (0–100) basado en el promedio de la
  autoevaluación Likert. Revisar en el libro de calificaciones del curso.

## 4. Pre-Brief sugerido (antes de la simulación)

Adaptar este guion breve (5 minutos) antes de asignar cualquier
escenario:

> "Van a participar en una simulación interactiva ambientada en
> [contexto del caso]. Tomarán el rol de [rol del estudiante en la
> narrativa]. No existe una única respuesta 'correcta absoluta' en
> términos de juicio profesional, pero el escenario está diseñado para
> guiarles hacia el proceso más coherente con el enfoque de APS visto en
> clase: [mencionar 1-2 conceptos clave de la sesión]. Tómense su tiempo
> para revisar los datos del 'Expediente' antes de decidir. Al finalizar,
> respondan las preguntas de debriefing — las discutiremos en la próxima
> sesión."

## 5. Facilitación del Debriefing (modelo 3-D)

Si el debriefing se realiza en grupo (recomendado, INACSL):

- **Defusing** (5 min): permitir que los estudiantes expresen cómo se
  sintieron, sin juzgar respuestas. Objetivo: bajar la guardia antes del
  análisis.
- **Discovery** (15-20 min): explorar qué decisiones tomaron, por qué,
  y qué conocimientos previos aplicaron. Usar las preguntas de
  `debrief.json` como guía, pero permitir desviaciones si surgen temas
  relevantes.
- **Deepening** (10 min): cerrar conectando el caso con la práctica real
  — "¿Cómo aplicarían esto en su próxima práctica de internado/APS?"

Evitar corregir frontalmente a quienes eligieron la opción "incorrecta"
en el juego — la retroalimentación embebida ya cumplió ese rol; el
debriefing es para profundizar el razonamiento, no para repetir la
calificación.

## 6. Hosting y despliegue (propuesta)

Dado el modelo de acceso híbrido (catálogo público + escenarios
restringidos), se propone:

1. **Catálogo público (`index.html` + escenarios con `access:"public"`)**
   → publicar en **GitHub Pages** (gratuito, sin backend, ideal para
   contenido estático). Pasos: subir la carpeta `/repo` a un repositorio
   de GitHub, activar GitHub Pages en la rama principal. El catálogo
   queda disponible en `https://<usuario>.github.io/<repo>/`.
   Alternativa institucional: cualquier servidor web estático de UCSUR.
2. **Escenarios restringidos (`access:"restricted"`)** → empaquetar como
   SCORM 1.2 (`imsmanifest.xml` + `player-standalone.html` +
   `scenario.json`/`rubric.json`/`debrief.json`, comprimidos en `.zip`)
   y subir como actividad SCORM en el curso correspondiente del Moodle
   UCSUR. El campo `meta.lms_url` del catálogo debe apuntar a esa
   actividad.
3. **Embebido vía iframe**: cualquier escenario público puede insertarse
   en una página de Moodle con
   `<iframe src="https://<usuario>.github.io/<repo>/scenarios/<id>/player-standalone.html" ...></iframe>`.

## 7. Edición y creación de nuevos escenarios

Use el **editor visual** (`editor.html`, raíz del repositorio) — no
requiere conocimientos de programación:

1. Abra `editor.html` en el navegador.
2. Complete los 6 pasos: Metadatos → Expediente → Mapa de decisiones →
   Rúbrica → Debriefing → Revisión y exportación.
3. En el Paso 3, use el menú "Siguiente nodo" de cada opción para crear
   ramificaciones y finales múltiples; la vista previa del grafo y el
   mensaje de validación le indicarán si falta conectar algo.
4. En el Paso 6, genere la vista previa interactiva, y descargue
   `scenario.json`, `rubric.json` y `debrief.json`.
5. Cree una carpeta `scenarios/<nuevo-id>/`, copie los 3 archivos
   descargados junto con `player.html`/`player-standalone.html`
   (copiados de un escenario existente — el motor es genérico).
6. Añada una entrada en el array `CATALOG` de `index.html` (ver
   `skills/repo-builder/SKILL.md` para el formato).

Para escenarios complejos o dudas sobre el mapeo de competencias,
consultar `docs/biblioteca-referencias.md` (principios CAN-Sim) y los
archivos `skills/*/SKILL.md` (especificaciones técnicas completas).

## 8. Soporte y mantenimiento

- **Vigencia de enlaces externos**: los documentos de referencia en
  `dashboard_data.documents` que enlazan a CAN-Sim permanecerán
  disponibles según su sitio "hasta 2027"; revisar periódicamente.
- **Compatibilidad**: los simuladores son HTML/CSS/JS puro, sin
  dependencias externas — funcionan en Chrome, Firefox, Edge y Safari
  recientes, en escritorio y tablets.
- **Idioma**: todo el contenido es bilingüe (ES/EN) mediante el switch
  ES/EN en el encabezado; al crear contenido nuevo, complete ambos
  idiomas para mantener la accesibilidad del repositorio para
  estudiantes de intercambio.
