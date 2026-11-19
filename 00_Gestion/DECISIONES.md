# Registro de decisiones

> Cada decisión relevante del proyecto, con su motivo, para no volver a discutirla.
> Estado: Vigente · Reemplazada (indicar por cuál) · Propuesta (pendiente de validación del equipo).

| ID | Fecha | Decisión | Motivo | Estado |
|---|---|---|---|---|
| D-001 | 2026-11-19 | Estructura de carpetas numerada: `00_Gestion`, `01_Enunciado`, `02_Material_Curso`, `03_Plantillas`, `04_Entregables/<Unidad>`, `05_Borradores`. | Separar las fuentes (lo que entrega el docente) de lo que produce el equipo y del registro. | Vigente |
| D-002 | 2026-11-19 | Los entregables se nombran `<Documento>_MasterBikes_vX.Y.<ext>` y **no se sobrescriben** versiones anteriores. | Trazabilidad y posibilidad de volver atrás. Un nombre como "ahora sí que sí" no permite saber cuál es la última versión. | Vigente |
| D-003 | 2026-11-19 | El registro de gestión se lleva en Markdown dentro de `00_Gestion` (hitos, bitácora, decisiones y revisiones). | Es liviano, legible en VS Code y queda junto a los documentos. | Vigente |
| D-004 | 2026-11-19 | Se trabaja por hitos definidos de antemano (H0–H9) y cada hito tiene una Definición de Terminado (DoD). | Lo pidió el equipo; ordena el trabajo y da visibilidad del avance. | Vigente |
| D-005 | 2026-11-19 | Los hitos de la Unidad 2 se derivan de los 20 criterios de la pauta: Acta C1–C10, Gantt C11–C15 y Trello C16–C20. | Maximizar el puntaje cubriendo cada criterio con evidencia explícita. | Vigente |
| D-006 | 2026-11-19 | Agregar RF-11 *Catálogo, cotización y reserva*, RF-12 *Reservas y venta en el local* (Sprint 4), RF-13 *Insumos*, RF-14 *Consulta a SHIMANO* y RF-15 *Administración* (OBS-01 y OBS-02 del acta oficial). | Sin el registro de la venta, RF-10 y RF-08 no tienen datos de origen; sin RF propios se pierde la trazabilidad. | **Propuesta** (la aprueba el PO, GA) |
| D-007 | 2026-11-19 | El acta oficial es la del **equipo de 4** (MM, GA, CS, LS): `04_Entregables/Unidad2/Acta_Constitucion_MasterBikes_v1.0.docx`. La versión de 3 integrantes (equipo Natalia Martínez) pasa a `05_Borradores/`. | El usuario indicó que esa es el acta de la entrega. La otra versión tiene otro equipo y su origen no está confirmado. | Vigente |
| D-008 | 2026-11-19 | Las verificaciones automáticas se guardan en `00_Gestion/scripts/` y se ejecutan con `python -I`. | Toda cifra del acta (horas, fechas) se comprueba de forma repetible antes de cerrar un hito. | Vigente |
| D-009 | 2026-11-19 | Versionar el proyecto con git en el repositorio **público** `digicamilo-lgtm/taller-de-bicicletas` (rama `main`) y publicar la carpeta completa, sin exclusiones. | Lo decidió el usuario. Se le advirtió antes del primer push que el repo incluye el acta de otro equipo con sus nombres, material del docente y el acta propia, que el curso podría copiar. | Vigente |
