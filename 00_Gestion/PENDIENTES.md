# Pendientes — punto de partida de la próxima sesión

> **Actualizado:** 2026-11-19, al cierre de la 2ª sesión.
> **Al retomar:** responder las preguntas de la sección 1 (aunque sea en parte) y seguir con la sección 2 en el orden indicado.
> Detalle técnico de cada OBS-xx en [REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md).

## Estado

- **Acta oficial v1.0** (equipo MM, GA, CS y LS): revisada. Estimo **29–30 de 30 pts** en C1–C10.
- **La entrega no está lista.** Faltan la **Carta Gantt** (C11–C15, 15 pts) y el **tablero Trello** (C16–C20, 15 pts); el anexo
  del acta tiene los espacios vacíos. Falta también el **formato de informe INACAP**, que es condición para ser evaluado.
- **Puntaje:** si la Gantt y el Trello no existen, la entrega queda en ≈ 29/60, bajo el mínimo de 36. Con H2–H5 completos se
  puede llegar a 60/60.

---

## 1. Preguntas para el equipo (responder al empezar)

| # | Pregunta | Por qué importa | Bloquea |
|---|---|---|---|
| P1 | ¿Ya existen la Carta Gantt y el tablero Trello? ¿Dónde están? | Valen 30 de 60 pts (R-01) | H3, H4 |
| P2 | ¿El PO (Gianni) aprueba OBS-01, OBS-02 y OBS-16? | Cambian el alcance y las horas del Sprint 4 | Parte de H2 y H3 |
| P3 | ¿De quién es la versión de 3 integrantes (equipo Natalia Martínez)? | Comparte el 81 % del texto con la nuestra (R-03) | La entrega |
| P4 | ¿Cuál es la fecha exacta de entrega (semana 5 de clases)? | Define cuánto tiempo hay y en qué orden trabajar | Todo |
| P5 | ¿Tienen la plantilla oficial del informe INACAP? | Sin el formato no se evalúa (R-02) | H5 |
| P6 | ¿Cuál es el correo institucional de Maxi? (y del resto, opcional) | Reemplaza "Contacto: pendiente de confirmar" (OBS-07) | H2 |
| P7 | ¿Quién crea el tablero Trello? ¿Cuál es el nombre o correo del docente para invitarlo? | Criterio C16 | H4 |

---

## 2. Trabajo pendiente, en orden

> **Si la entrega está muy cerca:** responder P2 → hacer H3 (Gantt) → H4 (Trello) → aplicar las correcciones rápidas de H2 → H5.
> La Gantt y Trello valen 30 pts; el pulido del acta, como mucho 1. La Gantt debe coincidir con las tareas del acta (C15), por eso
> P2 va primero.

### H2 — Acta v1.1 · Claude · ≈ 1 sesión
**Correcciones rápidas (no cambian el alcance, se pueden hacer sin esperar P2):**
- [ ] OBS-14 — Pasar a lenguaje formal las 9 frases informales (la tabla está en la revisión).
- [ ] OBS-03 — Agregar indicador y meta a OE1–OE6.
- [ ] OBS-15 — Agregar el "para qué" al objetivo general.
- [ ] OBS-04 — Cambiar a "apoye la fabricación mediante la administración de insumos" y excluir el control de calidad del armado.
- [ ] OBS-05 — Agregar Trello y la Carta Gantt a la tabla de herramientas.
- [ ] OBS-06 — Pasar la Review y la Retro del Sprint 2 al jue 24-dic y agregar el riesgo de las vacaciones de verano.
- [ ] OBS-07 — Contacto (P6), fecha de la versión y fecha de aprobación **27-11-2026** (cierre del Sprint 0).
- [ ] OBS-08 — Aclarar que el Scrum Master no es jefe jerárquico y reescribir "Coordina con la Gerencia y los stakeholders".
- [ ] OBS-09 — Agregar la Ley 21.719 (vigente desde el 1-dic-2026).
- [ ] OBS-10 — Agregar el supuesto "MasterBikes provee los equipos de la Interfaz de Hardware".
- [ ] OBS-12 — Escribir el desglose de las 5 h de eventos Scrum por sprint.

**Con la aprobación del PO (P2):**
- [ ] OBS-01 — Agregar RF-12 *Reservas y venta en el local* en el Sprint 4:
  CS = Estados 6 · Historial 6 · Reservas y venta 6 · Pruebas 7 · Eventos 5 = 30 h ·
  LS = Seguimiento 12 · Despacho 8 · Panel de reservas y ventas 5 · Eventos 5 = 30 h.
- [ ] OBS-02 — Crear RF-11 a RF-15, cambiar el alcance a "RF-01 a RF-15", ajustar los rótulos de los sprints y agregar la matriz RF ↔ OE ↔ Sprint.
- [ ] OBS-16 — Agregar "Actualizar Trello y % de la Gantt (MM, 1 h)" en los Sprints 2–5, descontando 1 h de "Revisión de código".

**Cierre de H2:** `python -I 00_Gestion/scripts/verificar_horas.py <acta v1.1> MM,GA,CS,LS` debe dar **TODO CUADRA**.
Guardar como `Acta_Constitucion_MasterBikes_v1.1.docx`, sin tocar la v1.0.

### H3 — Carta Gantt de 12 semanas · Claude · ≈ 1 sesión · depende de P2
- [ ] Desglose de tareas (EDT) por sprint: Sprint 0, Sprints 1–5 y Cierre.
- [ ] Gantt en Excel: tareas 1:1 con el acta, con responsable, inicio, término, barras de S1 a S12 y feriados marcados.
- [ ] Columna de **% de avance simulado** (C14) y comparación entre línea base y avance real.
- [ ] Captura para el anexo del acta.

### H4 — Tablero Trello · Claude prepara, el equipo lo arma · depende de H3
- [ ] (Claude) Guía y lista de tarjetas con título, descripción, responsable y fecha límite.
- [ ] (Equipo) Crear el tablero con las 4 columnas exactas: Documentación · Por Hacer · En Proceso · Hecho.
- [ ] (Equipo) Invitar a los 4 integrantes **y al docente** (C16).
- [ ] (Equipo) Crear las tarjetas de Documentación: Enunciado, Asignación de Roles y Carta Gantt (C18).
- [ ] (Equipo) Que cada responsable mueva sus tarjetas hasta el fin del semestre (C20).
- [ ] (Equipo) Pasar el link y una captura del tablero para el anexo.

### H5 — Informe en formato INACAP · Claude · depende de H2–H4 y P5
- [ ] Portada, índice, introducción, desarrollo (acta, Gantt y Trello), conclusión y bibliografía.
- [ ] Llenar el anexo del acta con el link y las capturas (cierra OBS-13).

### H6 — Autoevaluación antes de entregar · Claude y equipo
- [ ] Revisar C1–C20 con su evidencia. Meta: **54 o más de 60** y ningún criterio en "Insuficiente".

---

## 3. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Acta oficial | [04_Entregables/Unidad2/Acta_Constitucion_MasterBikes_v1.0.docx](../04_Entregables/Unidad2/Acta_Constitucion_MasterBikes_v1.0.docx) |
| Revisión con todas las observaciones | [REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md) |
| Plan de hitos y su estado | [HITOS.md](HITOS.md) |
| Historial de sesiones | [BITACORA.md](BITACORA.md) |
| Pauta (20 criterios) | [01_Enunciado/Pauta_Escala_Apreciacion_U2.png](../01_Enunciado/Pauta_Escala_Apreciacion_U2.png) |
| Scripts de verificación | [scripts/](scripts/) |
