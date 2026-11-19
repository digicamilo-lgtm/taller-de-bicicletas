# Revisión técnica — Acta MasterBikes, versión de 3 integrantes (equipo Natalia Martínez)

> ⚠️ **Reemplazada (2026-11-19).** Esta revisión corresponde a la versión de 3 integrantes, hoy en [05_Borradores/Acta_Constitucion_version_3_integrantes_NM.docx](../05_Borradores/Acta_Constitucion_version_3_integrantes_NM.docx). El acta oficial del equipo (Maximiliano Montoya y otros) se revisa en [REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md), donde se retoman las mismas observaciones (OBS-xx).

- **Documento revisado:** [Acta_Constitucion_version_3_integrantes_NM.docx](../05_Borradores/Acta_Constitucion_version_3_integrantes_NM.docx)
  (nombre original: `informes/Acta_del_Proyectoahora siq ue si.docx`)
- **Revisado contra:** caso MasterBikes, instrucciones TI3V23_U2_S5_AS, Escala de Apreciación N°1 (C1–C10) y material del curso (Scrum, planificación).
- **Fecha:** 2026-11-19 · **Hito:** H1

---

## 1. Veredicto

**Es un acta muy sólida, por sobre el nivel que se espera de esta evaluación.** Todas las secciones de la plantilla están
completas, son coherentes con el caso y la planificación tiene un rigor poco común: verifiqué con un script que las 12
semanas calzan exactamente (lun 23-nov-2026 → vie 12-feb-2027), que los feriados (8-dic, 25-dic, 1-ene) están bien
ubicados y que **las horas de cada integrante suman exactamente su capacidad en los 7 períodos** (15 / 27 / 27 / 27 / 30 / 30 / 15 h).

Hay **un error de fondo** (OBS-01) y varias inconsistencias de trazabilidad que conviene corregir antes de entregar.

> ⚠️ **Lo más importante:** el acta vale como máximo **30 de 60 puntos** (C1–C10). La Carta Gantt (C11–C15) y el tablero
> Trello (C16–C20) suman los otros 30 y **no están en la carpeta**. Solo con el acta el resultado sería 50 %, bajo el 60 %
> de exigencia. Además, sin el formato de informe INACAP el trabajo **no se evalúa**.

## 2. Puntaje estimado (criterios C1–C10)

| # | Criterio | Hoy | Tras v1.1 | Comentario |
|---|---|---|---|---|
| C1 | Alcance consistente con los requerimientos del cliente | 2 | 3 | Falta el registro de ventas (OBS-01) y hay funciones sin RF (OBS-02). |
| C2 | Objetivo principal | 3 | 3 | Bien formulado: qué, plazo, metodología y para qué. |
| C3 | Al menos 3 objetivos específicos | 3 | 3 | Hay 6 objetivos y están ligados a sprints. Falta que sean medibles (OBS-03). |
| C4 | Stakeholders impactados | 3 | 3 | 14 stakeholders, internos y externos, con rol e impacto. |
| C5 | Grupos afectados (+ y −) | 3 | 3 | Incluye impactos negativos con su acción de mitigación. Muy bien. |
| C6 | Roles según Scrum | 3 | 3 | Bien justificado para un equipo de 3. Ver OBS-08. |
| C7 | Tareas según rol y funciones | 3 | 3 | Coherente: Scrum Master + frontend, PO + QA y documentación, Developer en backend. |
| C8 | Tareas específicas para el proyecto | 3 | 3 | Las tareas nombran los módulos reales del caso. |
| C9 | Tareas acordes a la capacidad | 3 | 3 | Calculado y verificado (punto fuerte). |
| C10 | Apoyo entre integrantes | 3 | 3 | La tabla de apoyo cubre suplencias y sobrecarga. |
| | **Total acta** | **29/30** | **30/30** | |

*Estimación propia; el puntaje final depende del criterio del docente.*

## 3. Fortalezas

1. **Delimitación clara** entre lo que el proyecto incluye y lo que no (pago en línea, imagen corporativa, hardware, facturación).
2. **Requerimientos no funcionales medibles:** menos de 3 s por página, menos de 5 s en la consulta a SHIMANO con reintento, 50 usuarios simultáneos, 99 % de disponibilidad y respaldo diario.
3. **Planificación de capacidad realista:** 15 h por semana por estudiante y descuento de 3 h en las semanas con feriado.
4. **Stack actual y coherente:** Django 5.2 LTS (soporte hasta 2028), PostgreSQL 17, Ubuntu 24.04 LTS y Bootstrap 5.3.
5. **Detalles que muestran comprensión del caso:** una tablet con funda para el taller (reemplaza las carpetas que se manchan), aviso y reintento si SHIMANO no responde, y atención presencial para los clientes poco digitales.

## 4. Observaciones

Severidad: 🔴 Alta (afecta el puntaje o la coherencia) · 🟠 Media · 🟢 Baja (pulido)

### 🔴 OBS-01 — Falta el requerimiento de registro de pedidos y ventas
- **Dónde:** tabla de Funciones (RF-01 a RF-10), Objetivo general y Sprints.
- **Problema:** el objetivo general dice "digitalice los procesos de **venta**", y RF-10 (resúmenes de ventas) y RF-08
  (traza desde la "toma del pedido") **necesitan que la venta quede registrada en el sistema**. Sin embargo, ningún RF ni
  tarea reemplaza la hoja de pedido en papel del mesón. Tal como está, el supervisor no tendría datos de venta para su reporte.
- **Corrección:** agregar un RF de "Registro digital del pedido y la venta en el mesón": productos, accesorios, cargo por
  traslado a domicilio, estados (solicitado → vendido → pagado) y solicitud a bodega. Ubicarlo **antes del Sprint 5** y
  redistribuir horas para que la capacidad siga cuadrando.

### 🟠 OBS-02 — Funciones planificadas sin código RF (trazabilidad rota)
- **Dónde:** Sprints 1, 2 y 5; Características de los usuarios (rol Administrador); Alcance ("10 funcionalidades").
- **Problema:**
  - Sprint 1 rotula el catálogo como "RF-09 base", pero RF-09 corresponde a ofertas por correo.
  - Sprint 2 rotula insumos y SHIMANO como "(RF-05)", pero RF-05 es solo la consulta de stock.
  - Las funciones de catálogo, administración de insumos, consulta a SHIMANO y administración (usuarios, roles, productos, ofertas) no tienen RF propio, aunque son objetivos explícitos del caso.
- **Corrección:** crear RF-12 a RF-15, actualizar el alcance a "RF-01 a RF-15" y agregar una **matriz de trazabilidad RF ↔ OE ↔ Sprint**.

### 🟠 OBS-03 — Los objetivos específicos no son medibles
- **Dónde:** Objetivos específicos OE1–OE6.
- **Problema:** las instrucciones piden objetivos "**medibles** y basados en los entregables". Los OE están basados en
  entregables, pero no tienen indicador ni meta.
- **Corrección:** agregar indicador y meta a cada uno. Ejemplo: *"OE1 … Indicador: el 100 % de las historias de RF-01 y
  RF-12 aceptadas por la PO en la Sprint Review del 11-12-2026"*. Opcional: agregar KPIs a los objetivos del negocio
  (por ejemplo, 0 hojas de pedido en papel al cierre).

### 🟠 OBS-04 — "Procesos de fabricación" sin cobertura explícita
- **Dónde:** Solución y Objetivo general.
- **Problema:** se promete "mejorar los procesos de fabricación", pero solo el módulo de insumos los toca. La aprobación o
  rechazo del supervisor sobre las bicicletas armadas no está ni incluida ni excluida.
- **Corrección:** precisar que la mejora de fabricación se hace **a través de la administración de insumos** y agregar
  "control de calidad del armado" a la lista de lo que el proyecto no incluye (o crear un RF pequeño, si el equipo lo prefiere).

### 🟠 OBS-05 — Falta Trello en las herramientas
- **Dónde:** Especificaciones Técnicas – Herramientas.
- **Problema:** la evaluación exige una plataforma colaborativa (C16–C20), pero la tabla solo menciona Excel como "gestión ágil".
- **Corrección:** agregar *Trello — tablero Kanban con las columnas Documentación / Por Hacer / En Proceso / Hecho* y la herramienta de la Carta Gantt.

### 🟠 OBS-06 — El Sprint 2 termina en feriado (vie 25-dic)
- **Dónde:** Tiempos asociados, Sprint 2.
- **Problema:** la Sprint Review con el cliente y la Retrospective caerían en Navidad. Además, entre diciembre y febrero
  hay vacaciones de verano, lo que afecta la disponibilidad del personal de MasterBikes para validar cada sprint.
- **Corrección:** indicar que la Review y la Retro del Sprint 2 se hacen el jueves 24-dic, y agregar como supuesto o riesgo
  la disponibilidad del cliente en verano.

### 🟢 OBS-07 — Datos pendientes y sección de aprobación
- Queda el marcador `[correo institucional]` y faltan los contactos de los demás integrantes.
- "VERSIÓN 1.0" no tiene fecha de emisión ni tabla de control de cambios.
- Un acta de constitución normalmente cierra con la **aprobación del patrocinador** (nombre, cargo, firma y fecha). Agregarla.

### 🟢 OBS-08 — Matices de roles Scrum
- En Scrum **no existe el rol de jefe de proyecto**. La plantilla lo pide, así que conviene aclarar en una línea que "la
  Scrum Master actúa como punto de coordinación del proyecto, sin autoridad jerárquica sobre el equipo". Así se evita un
  descuento en C6.
- La PO también diseña y ejecuta las pruebas, y luego acepta los incrementos que ella misma probó. La prueba cruzada ya
  declarada lo mitiga; conviene mencionarlo de forma explícita.
- La suplente de la Scrum Master es la PO (acumula roles). Es aceptable en un equipo de 3, pero conviene justificarlo.

### 🟢 OBS-09 — Marco legal de datos personales
- Se cita la Ley 19.628. Conviene agregar la **Ley 21.719**, que la modifica y entra en vigencia el 1-dic-2026, es decir,
  dentro del período del proyecto.

### 🟢 OBS-10 — Supuesto sobre el hardware
- La compra de equipos está fuera del alcance, pero la interfaz de hardware asume tablets, impresoras y PCs. Agregar el
  supuesto: "MasterBikes provee los equipos indicados en la Interfaz de Hardware".

### 🟢 OBS-11 — Nombre del archivo ✅ (resuelto en H0)
- Se renombró a `Acta_Constitucion_MasterBikes_v1.0.docx`.

### ℹ️ OBS-12 — Explicitar el cálculo de los eventos Scrum (sugerencia)
- Las 5 h por sprint de eventos son coherentes: 10 Daily × 15 min (2,5 h) + Planning (1 h) + Review (1 h) + Retro (0,5 h).
  Escribir este desglose refuerza C9.

## 5. Próximo paso

Aplicar OBS-01 a OBS-10 en el **H2 (Acta v1.1)**. OBS-01 y OBS-02 cambian el alcance y las horas, así que el equipo debe validarlos antes.
