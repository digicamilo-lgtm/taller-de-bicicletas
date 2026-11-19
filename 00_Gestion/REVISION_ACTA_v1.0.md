# Revisión técnica — Acta de Constitución MasterBikes v1.0 (equipo de 4 integrantes)

- **Documento revisado:** [Acta_Constitucion_MasterBikes_v1.0.docx](../04_Entregables/Unidad2/Acta_Constitucion_MasterBikes_v1.0.docx)
  (nombre original: `ahora siq ue si.docx`). Equipo: MM = Maximiliano Montoya · GA = Gianni Antonietti · CS = Camilo Sepúlveda · LS = Logan Silva.
- **Revisado contra:** caso MasterBikes, instrucciones TI3V23_U2_S5_AS, Escala de Apreciación N°1 (C1–C20) y material del curso.
- **Fecha:** 2026-11-19 · **Hito:** H1 · **Revisión anterior:** [versión de 3 integrantes](REVISION_ACTA_version_3_integrantes.md) (se mantienen los números OBS-xx).

---

## 1. Veredicto

**El acta está lista en su contenido; la entrega todavía no.**

- **Acta (C1–C10):** estimo **29–30 de 30 puntos**. Es un documento completo, coherente con el caso y con una planificación
  verificada.
- **Entrega completa (C1–C20):** el anexo de evidencias tiene **3 marcadores sin llenar**: el link del tablero, la captura
  del tablero y la captura de la Carta Gantt. Esos elementos respaldan **30 de los 60 puntos** (Gantt C11–C15 y Trello C16–C20).
  Si la Gantt y el tablero aún no existen, la entrega queda en unos 29 de 60 puntos (48 %), bajo el mínimo de 36 (60 %).
- **Formato:** si el docente exige el *formato de informe INACAP*, el acta sola no basta, porque le faltan portada, índice,
  introducción, conclusión y bibliografía. Según las instrucciones, sin ese formato el trabajo **no se evalúa**.

**Verificado con script** ([scripts/verificar_horas.py](scripts/verificar_horas.py)):
- Las horas de los 4 integrantes suman exactamente su capacidad en los 7 períodos (15 / 27 / 27 / 27 / 30 / 30 / 15 h).
- El proyecto dura 12 semanas exactas (lun 23-nov-2026 al vie 12-feb-2027) y los feriados están bien ubicados.
- Formato del documento: tamaño carta, márgenes de 2,5 cm (superior e inferior) y 3 cm (laterales), fuentes consistentes y 16 páginas.

## 2. Qué mejoró respecto de la versión de 3 integrantes

1. **Roles mejor repartidos:** backend (CS) y frontend (LS) quedan separados, y el Scrum Master suma integraciones y despliegue.
2. **Tareas más concretas:** modelo entidad-relación, diccionario de datos, ambiente de pruebas (staging), migraciones, pruebas unitarias y carga inicial de datos.
3. **Alcance de la venta aclarado:** el cliente cotiza y reserva en línea, y paga y cierra la compra en el local. La pasarela de pago queda para una etapa futura.
4. Si falta el Scrum Master, lo reemplaza CS y no el Product Owner (antes había conflicto de roles).
5. **Pruebas cruzadas explícitas:** "nadie valida su propio desarrollo".
6. Se agregaron una **sección de aprobación con firmas** y un **anexo de evidencias** pensado para C11–C20.
7. "Contraseñas con *hash*" es más correcto técnicamente que "cifradas".

## 3. Puntaje estimado

| # | Criterio | Estimado | Comentario |
|---|---|---|---|
| C1 | Alcance consistente con lo que pide el cliente | 2–3 | Es el criterio con más riesgo: el flujo de venta queda a medias (OBS-01) y hay funciones sin código RF (OBS-02). |
| C2 | Objetivo principal | 3 | Bien planteado. Le falta el "para qué" (OBS-15). |
| C3 | Al menos 3 objetivos específicos | 3 | Hay 6, ligados a sprints. Les faltan indicadores medibles (OBS-03). |
| C4 | Stakeholders | 3 | 14 stakeholders, con su tipo, rol e impacto. |
| C5 | Grupos afectados (+ y −) | 3 | Incluye impactos negativos con acciones de mitigación. |
| C6 | Roles Scrum | 3 | 4 roles claros. Ver el detalle de OBS-08. |
| C7 | Tareas según rol | 3 | Cada tarea corresponde a la especialidad de quien la tiene asignada. |
| C8 | Tareas específicas | 3 | Las tareas nombran los módulos reales del caso. |
| C9 | Tareas acordes a la capacidad | 3 | Verificado con script. |
| C10 | Apoyo entre integrantes | 3 | 7 situaciones de apoyo, incluidas suplencias. |
| C11–C15 | Carta Gantt | **0–15** | **Depende de que exista la Gantt** (falta la captura en el anexo). |
| C16–C20 | Trello | **0–15** | **Depende de que exista el tablero con el docente invitado.** |

## 4. Estado de las observaciones

| OBS | Tema | Severidad | Estado en esta versión |
|---|---|---|---|
| OBS-13 | Anexo con marcadores sin completar (Gantt y Trello) | 🔴 | **Nueva** |
| OBS-01 | Flujo de venta incompleto | 🟠 | Parcial |
| OBS-02 | Funciones sin código RF | 🟠 | Persiste |
| OBS-03 | Objetivos específicos sin indicadores | 🟠 | Persiste |
| OBS-14 | Lenguaje informal y en primera persona | 🟠 | **Nueva** |
| OBS-04 | "Digitalizar la fabricación" sin funciones que lo respalden | 🟠 | Persiste (se acentuó) |
| OBS-05 | Trello y Gantt no aparecen en la tabla de herramientas | 🟠 | Persiste |
| OBS-06 | El Sprint 2 cierra el 25-dic (feriado) | 🟠 | Persiste |
| OBS-07 | Datos pendientes (contacto, fecha) | 🟢 | Parcial: se agregó la aprobación |
| OBS-08 | Matices de roles Scrum | 🟢 | Parcial: se corrigió la suplencia |
| OBS-09 | Ley 21.719 | 🟢 | Persiste |
| OBS-10 | Supuesto de hardware | 🟢 | Persiste |
| OBS-11 | Nombre del archivo | 🟢 | Resuelta (se renombró) |
| OBS-12 | Desglose de los eventos Scrum | ℹ️ | Persiste |
| OBS-15 | El objetivo general perdió el "para qué" | 🟢 | **Nueva** |
| OBS-16 | El seguimiento del Scrum Master no tiene horas | 🟢 | **Nueva** |

## 5. Detalle

### 🔴 OBS-13 — Anexo de evidencias vacío
Quedan sin llenar `[Insertar link del tablero con acceso para el docente]`, "Pegar aquí la captura de pantalla del tablero
colaborativo…" y "Pegar aquí la captura de pantalla de la Carta Gantt…". Así como está, el documento se ve inconcluso y no
respalda 30 puntos de la pauta. **Corrección:** hacer la Gantt (H3) y el tablero (H4), y luego pegar las evidencias.

### 🟠 OBS-01 — El flujo de venta quedó a medias
El cliente puede cotizar y reservar en línea, pero **ningún RF, tarea ni panel permite al vendedor ver la reserva, cerrar la
venta o registrar una venta presencial**. El mismo documento supone que esa función existe:
- Cajeros: "Se adaptan al nuevo flujo de venta con pedidos ya registrados" (¿quién los registra?).
- Vendedores: "el pedido en papel cambia" (¿por qué cambia?).
- RF-10, resúmenes de ventas: no tiene de dónde sacar las ventas que se cierran en el local.
- El objetivo general dice "digitalice la venta".
- La reserva solo aparece como tarea de frontend ("Catálogo… con cotización y reserva", LS 8 h). La lógica de backend
  (apartar stock y hacer vencer la reserva) no tiene responsable.

**Corrección propuesta:** agregar el RF "Gestión de reservas y registro de la venta en el local" (vendedor y cajero) y llevarlo al
**Sprint 4**, que es donde comienza la traza del despacho ("toma del pedido"). La capacidad se mantiene sin recortar pruebas:

| Integrante | Sprint 4 hoy | Sprint 4 propuesto |
|---|---|---|
| CS | Estados 9 · Historial 9 · Pruebas unitarias 7 · Eventos 5 = **30** | Estados 6 · Historial 6 · **Reservas y venta (lógica) 6** · Pruebas unitarias 7 · Eventos 5 = **30** |
| LS | Vistas de seguimiento 15 · Panel de despacho 10 · Eventos 5 = **30** | Vistas de seguimiento 12 · Panel de despacho 8 · **Panel de reservas y ventas 5** · Eventos 5 = **30** |

### 🟠 OBS-02 — Funciones planificadas sin código RF
El alcance dice "10 funcionalidades (RF-01 a RF-10)", pero el plan también incluye el catálogo con cotización y reserva
(Sprint 1, rotulado solo "RF-01"), insumos y SHIMANO (Sprint 2, rotulado "RF-05", que es solo la consulta de stock) y la
administración (rol Administrador). **Corrección:** crear RF-11 *Catálogo, cotización y reserva*, RF-12 *Reservas y venta en el
local* (OBS-01), RF-13 *Administración de insumos*, RF-14 *Consulta a SHIMANO* y RF-15 *Administración de usuarios, productos y
ofertas*. Luego actualizar el alcance a "RF-01 a RF-15" y los rótulos de los sprints, y agregar una matriz RF ↔ OE ↔ Sprint.
*Nota técnica:* Django trae incluido su sitio de administración, así que RF-15 casi no suma horas.

### 🟠 OBS-03 — Objetivos específicos sin indicadores
Las instrucciones piden objetivos "medibles". Ejemplo de redacción: *"OE3. Implementar el arriendo en línea… **Indicador:** el
100 % de los criterios de aceptación de RF-02 aprobados por el Product Owner en la Sprint Review del 08-01-2027."*

### 🟠 OBS-14 — Lenguaje informal en un documento formal
Un acta de constitución se redacta en tercera persona impersonal. Frases a corregir:

| Dice | Sugerencia |
|---|---|
| "Somos un equipo chico, así que…" | "Dado que el equipo es reducido (4 integrantes), …" |
| "Hoy la empresa no da abasto con la demanda" | "Actualmente la empresa no logra satisfacer la demanda" |
| "más o menos 3 h diarias" | "aproximadamente 3 h diarias" |
| "Partimos con un Sprint 0… seguimos con… y cerramos…" | "El proyecto se organiza en un Sprint 0…, cinco sprints… y una semana de cierre" |
| "contamos 27 h por persona" | "se consideran 27 h por integrante" |
| "Con el arriendo pasa lo mismo" | "El mismo criterio se aplica al arriendo" |
| "Proponemos una plataforma web" | "Se propone una plataforma web" |
| "De lunes a viernes hacemos una Daily" | "De lunes a viernes se realiza una Daily Scrum" |
| "evidencias de cómo planificamos y seguimos" | "evidencias de la planificación y el seguimiento" |

### 🟠 OBS-04 — "Digitalice la fabricación"
La sección Solución promete digitalizar la fabricación, pero solo el módulo de insumos la toca. **Corrección:** cambiarlo por
"apoye la fabricación mediante la administración de insumos" y agregar "control de calidad del armado" a la lista de lo que el proyecto no incluye.

### 🟠 OBS-05 — Faltan Trello y la Gantt en las herramientas
El anexo menciona el tablero colaborativo y la "Carta Gantt en Excel", pero la tabla de herramientas no los nombra. **Corrección:**
agregar *Trello — tablero Kanban (Documentación / Por Hacer / En Proceso / Hecho)* y extender el uso de Excel a "Product Backlog,
historias de usuario y Carta Gantt".

### 🟠 OBS-06 — Cierre del Sprint 2 en feriado
El Sprint 2 termina el vie 25-dic. **Corrección:** indicar que la Review y la Retrospective se hacen el jue 24-dic, y agregar como
supuesto o riesgo la disponibilidad del personal de MasterBikes en las vacaciones de verano.

### 🟢 Pulido
- **OBS-07:** sigue el texto "Contacto: pendiente de confirmar". Faltan la fecha de la versión y la fecha de aprobación; esta puede ser el **27-11-2026**, cierre del Sprint 0, donde el plan ubica la aprobación del acta.
- **OBS-08:** aclarar en una línea que en Scrum el Scrum Master no es un jefe jerárquico (la plantilla pide "Jefe de Proyecto"). Además, "Coordina con la Gerencia y los stakeholders" se cruza con el Product Owner, que es quien representa al cliente. Sugerencia: "Facilita la colaboración entre el equipo, el Product Owner y los stakeholders".
- **OBS-09:** agregar la **Ley 21.719**, que modifica la Ley 19.628 y entra en vigencia el 1-dic-2026, dentro del proyecto.
- **OBS-10:** agregar el supuesto "MasterBikes provee los equipos indicados en la Interfaz de Hardware".
- **OBS-12:** escribir el desglose de las 5 h de eventos: 10 Daily × 15 min (2,5 h) + Planning (1 h) + Review (1 h) + Retro (0,5 h).
- **OBS-15:** recuperar el propósito del objetivo general, como en la versión anterior: "…para satisfacer la demanda actual de sus clientes y mejorar su competitividad".
- **OBS-16:** "Llevar el seguimiento del avance y de los impedimentos" (MM) solo tiene horas en el Sprint 1, y la pauta evalúa el % de avance (C14) y el movimiento de tarjetas (C20). **Propuesta:** agregar "Actualizar Trello y el % de avance de la Gantt (MM, 1 h)" en los Sprints 2–5 y bajar 1 h a "Revisión de código". El total no cambia.

## 6. Riesgos para la entrega

| ID | Riesgo | Impacto | Acción |
|---|---|---|---|
| R-01 | La Gantt y/o el tablero no existen | Hasta −30 pts | H3 y H4 antes que cualquier pulido |
| R-02 | No cumplir el formato de informe INACAP | No se evalúa | Conseguir la plantilla oficial (H5) |
| R-03 | El acta comparte el **81 % del texto** con la versión de 3 integrantes (equipo Natalia Martínez) y la mitad de sus líneas son idénticas | Si esa versión es de otro grupo del curso, el docente podría considerarlas copiadas | Aclarar con el equipo el origen de esa versión antes de entregar |

## 7. Orden recomendado para dejarla lista
1. **H2 (corto):** aplicar las correcciones rápidas (OBS-03, 04, 05, 06, 07, 08, 09, 10, 12, 14, 15) y, **con la aprobación del equipo**, OBS-01, OBS-02 y OBS-16, que cambian el alcance y las horas.
2. **H3:** Carta Gantt, coherente 1:1 con el acta.
3. **H4:** tablero Trello. Claude prepara las tarjetas y el equipo crea el tablero e invita al docente.
4. Pegar las evidencias en el anexo (OBS-13), armar el informe INACAP (H5) y hacer la autoevaluación (H6).
