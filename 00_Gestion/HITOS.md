# Plan de Hitos — Proyecto MasterBikes

> Registro maestro del trabajo. Cada hito se **define antes de desarrollarse** y solo se cierra cuando cumple su
> *Definición de Terminado (DoD)*. El estado se actualiza al final de cada sesión de trabajo (ver [BITACORA.md](BITACORA.md)).
> **Lo que falta, en orden y con las preguntas abiertas:** [PENDIENTES.md](PENDIENTES.md).

**Leyenda de estado:** ⬜ Pendiente · 🟦 En curso · ✅ Terminado · ⏸️ Bloqueado (requiere acción del equipo)

**Pauta:** Escala de Apreciación N°1, 20 criterios × 3 pts = **60 pts**. Exigencia 60 % → **36 pts = nota 4,0**.
Ver [Pauta_Escala_Apreciacion_U2.png](../01_Enunciado/Pauta_Escala_Apreciacion_U2.png).

| Bloque de la pauta | Criterios | Puntos | Hito que lo cubre |
|---|---|---|---|
| Acta de constitución | C1 – C10 | 30 | H1, H2 |
| Carta Gantt | C11 – C15 | 15 | H3 |
| Plataforma colaborativa (Trello) | C16 – C20 | 15 | H4 |
| Formato informe INACAP | condición para ser evaluado | — | H5 |

---

## Resumen

| ID | Hito | Bloque | Estado | Responsable |
|---|---|---|---|---|
| H0 | Organización del proyecto y sistema de registro | Gestión | ✅ | Claude |
| H1 | Revisión técnica del Acta v1.0 (equipo de 4) | Unidad 2 | ✅ | Claude |
| H2 | Acta de Constitución v1.1 (aplicar observaciones) | Unidad 2 | ⬜ | Claude + validación del equipo |
| H3 | EDT y Carta Gantt de 12 semanas con % de avance | Unidad 2 | ⬜ | Claude |
| H4 | Tablero Trello (Kanban) y tarjetas | Unidad 2 | ⬜ | Claude prepara · **Equipo crea en Trello** |
| H5 | Informe grupal en formato INACAP | Unidad 2 | ⬜ | Claude |
| H6 | Control de calidad y autoevaluación previa a la entrega | Unidad 2 | ⬜ | Claude + equipo |
| H7 | Product Backlog: épicas e historias de usuario | Unidad 3 (tentativo) | ⬜ | Claude |
| H8 | Priorización, estimación y Release Plan | Unidad 3 (tentativo) | ⬜ | Claude |
| H9 | Seguimiento hasta el fin del semestre (Gantt + Trello) | Continuo | ⬜ | Equipo, con apoyo |

---

## Detalle de hitos

### H0 — Organización del proyecto y sistema de registro ✅
- **Objetivo:** dejar la carpeta ordenada y un sistema de registro que permita retomar el trabajo en cualquier sesión.
- **Entregables:** estructura de carpetas `00_`–`05_`, [README.md](../README.md), [CLAUDE.md](../CLAUDE.md), este archivo,
  [BITACORA.md](BITACORA.md), [DECISIONES.md](DECISIONES.md).
- **DoD:** todos los archivos originales ubicados y renombrados con nombre claro; tabla de nombres originales en el README.

### H1 — Revisión técnica del Acta v1.0 ✅
- **Objetivo:** evaluar el acta del equipo (MM, GA, CS, LS) contra la pauta (C1–C20), el caso MasterBikes y buenas prácticas de Scrum.
- **Entregable:** [REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md), con 16 observaciones (OBS-xx) y 3 riesgos de entrega (R-xx).
  Antes se había revisado la versión de 3 integrantes: [REVISION_ACTA_version_3_integrantes.md](REVISION_ACTA_version_3_integrantes.md) (reemplazada).
- **DoD:** cada criterio tiene un puntaje estimado; cada observación tiene ubicación, estado y corrección propuesta; las horas se verificaron con script.

### H2 — Acta de Constitución v1.1 ⬜
- **Objetivo:** subir C1–C10 al máximo aplicando las observaciones de H1.
- **Entregable:** `04_Entregables/Unidad2/Acta_Constitucion_MasterBikes_v1.1.docx` (la v1.0 se conserva).
- **Alcance:**
  - *Correcciones rápidas, sin cambio de alcance:* OBS-03 (indicadores), OBS-04, OBS-05 (Trello y Gantt en herramientas),
    OBS-06 (Review del 24-dic), OBS-07, OBS-08, OBS-09 (Ley 21.719), OBS-10, OBS-12, OBS-14 (lenguaje formal) y OBS-15.
  - *Con aprobación del equipo, porque cambian el alcance o las horas:* OBS-01 (RF de reservas y venta en el local, en el Sprint 4),
    OBS-02 (RF-11 a RF-15 y matriz RF ↔ OE ↔ Sprint) y OBS-16 (horas de seguimiento del Scrum Master).
    En Scrum, el cambio de alcance lo aprueba el Product Owner (GA).
- **DoD:** `scripts/verificar_horas.py` da "TODO CUADRA"; no quedan marcadores pendientes, salvo los del anexo (se completan
  en H5); el equipo aprueba los cambios.
- **Depende de:** H1. **Requiere del equipo:** el correo de contacto de MM y la aprobación de OBS-01, OBS-02 y OBS-16.

### H3 — EDT y Carta Gantt de 12 semanas ⬜
- **Objetivo:** cubrir C11–C15.
- **Entregable:** `04_Entregables/Unidad2/Carta_Gantt_MasterBikes.xlsx` con:
  - EDT por fase y sprint (Sprint 0, Sprints 1–5, Cierre), tareas con responsable, inicio, término y duración.
  - Barras semanales S1–S12 que respetan la secuencia y los feriados.
  - Columna de **% de avance simulado** (C14), línea base comparada con lo real e hitos marcados.
- **DoD:** las tareas y horas coinciden 1:1 con el acta v1.1; cada tarea tiene responsable (MM, GA, CS o LS); las fechas son
  consecutivas sin solapes ilógicos; se genera la captura para el anexo del acta (OBS-13).
- **Depende de:** H2.

### H4 — Tablero Trello (Kanban) ⬜
- **Objetivo:** cubrir C16–C20.
- **Entregable:** `04_Entregables/Unidad2/Trello_Guia_y_Tarjetas.md` (y un CSV de apoyo) con:
  - Las 4 columnas exactas: Documentación · Por Hacer · En Proceso · Hecho.
  - Las tarjetas de Documentación: Enunciado, Asignación de Roles y Carta Gantt (con sus adjuntos).
  - Las tarjetas de tareas con Título, Descripción, Responsable/s y Fecha límite, derivadas de la Gantt.
  - Un plan de movimiento de tarjetas por responsable y una lista de evidencias (capturas) para el informe.
- **DoD:** el tablero está creado, con todos los integrantes **y el docente** invitados (⚠️ esto lo hace el equipo; Claude no tiene acceso a Trello).
- **Depende de:** H3.

### H5 — Informe grupal formato INACAP ⬜
- **Objetivo:** cumplir la condición de formato (si no se cumple, no se evalúa).
- **Entregable:** `04_Entregables/Unidad2/Informe_U2_MasterBikes.docx`: portada, índice, introducción, desarrollo
  (acta, roles, tareas, Gantt y evidencia de Trello), conclusión y bibliografía.
- **DoD:** sigue el formato oficial de informe INACAP (⚠️ **se necesita la plantilla oficial**, que no está en la carpeta);
  el anexo del acta tiene el link y las capturas del tablero y de la Gantt (cierra OBS-13).
- **Depende de:** H2, H3, H4.

### H6 — Control de calidad y autoevaluación ⬜
- **Objetivo:** llegar a la entrega con evidencia de cada criterio.
- **Entregable:** `00_Gestion/AUTOEVALUACION_U2.md`: cada criterio C1–C20 con su evidencia, puntaje estimado y brechas.
- **DoD:** el puntaje estimado es de 54 o más sobre 60 y no hay criterios en "Insuficiente".
- **Depende de:** H5.

### H7 — Product Backlog: épicas e historias de usuario ⬜ *(tentativo, Unidad 3)*
- **Entregable:** `Historias_Usuario_MasterBikes.xlsx`, sobre la plantilla oficial ([Plantilla_Historias_Usuario.xlsx](../03_Plantillas/Plantilla_Historias_Usuario.xlsx)).
- **Contenido:** épicas por módulo; historias con ID `E#-H#`, rol, funcionalidad, razón y 2–4 escenarios de aceptación (contexto / evento / resultado), con trazabilidad a los RF.
- ⚠️ Se confirma cuando esté disponible la pauta de la Unidad 3.

### H8 — Priorización, estimación y Release Plan ⬜ *(tentativo, Unidad 3)*
- **Contenido:** priorización por valor (MoSCoW), estimación (story points con Planning Poker), velocidad, Release Plan y Sprint Backlog.

### H9 — Seguimiento continuo ⬜
- **Contenido:** mover las tarjetas de Trello y actualizar el % de avance de la Gantt hasta el término del semestre (C14 y C20).
