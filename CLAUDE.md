# CLAUDE.md — Proyecto MasterBikes (TI3V23, INACAP)

## Contexto
- Proyecto académico de **documentación** (sin programación) con Scrum y Kanban, sobre el caso "Fábrica San Diego → MasterBikes".
- Todo se escribe en **español de Chile**. El usuario pide que actúe como ingeniero experto (ciencia de datos, computación, informática y metodologías ágiles).
- Las fuentes de verdad son el caso ([01_Enunciado/Caso_MasterBikes.docx](01_Enunciado/Caso_MasterBikes.docx)), las instrucciones y la pauta
  ([01_Enunciado/Pauta_Escala_Apreciacion_U2.png](01_Enunciado/Pauta_Escala_Apreciacion_U2.png): 20 criterios × 3 pts, exigencia 60 %).

## Forma de trabajo (obligatoria)
1. **Trabajar por hitos.** Al iniciar cada sesión, leer [00_Gestion/PENDIENTES.md](00_Gestion/PENDIENTES.md) (punto de partida)
   y [00_Gestion/HITOS.md](00_Gestion/HITOS.md), y trabajar solo el hito acordado.
   Si aparece trabajo nuevo, se define como hito o se agrega a uno existente **antes** de ejecutarlo.
2. Un hito se cierra solo cuando cumple su DoD.
3. **Al terminar cada sesión:** agregar una entrada en [00_Gestion/BITACORA.md](00_Gestion/BITACORA.md), actualizar el estado
   en HITOS.md, registrar las decisiones en [00_Gestion/DECISIONES.md](00_Gestion/DECISIONES.md) y dejar al día PENDIENTES.md.
4. Nunca sobrescribir un entregable: crear `vX.Y` nueva en `04_Entregables/<Unidad>/`. No editar `01_Enunciado/` ni `03_Plantillas/`.
5. Verificar con un script todo número que se afirme: fechas, días de la semana, sumas de horas contra la capacidad.

## Datos clave del plan (acta oficial v1.0)
- Equipo (4): MM = Maximiliano Montoya ("el Maxi", Scrum Master y jefe de proyecto + integraciones y despliegue),
  GA = Gianni Antonietti (Product Owner + QA y documentación), CS = Camilo Sepúlveda (Developer backend y BD),
  LS = Logan Silva (Developer frontend y UX/UI).
- La versión de 3 integrantes (Natalia Martínez y otras) en `05_Borradores/` **no es la del equipo**: no usarla como fuente.
- Proyecto simulado del lun 23-11-2026 al vie 12-02-2027: Sprint 0 (1 sem) + 5 sprints × 2 sem + Cierre (1 sem).
- Capacidad: 15 h/semana por integrante (60 h por semana el equipo); 27 h por sprint con feriado (8-dic, 25-dic, 1-ene) y 30 h sin feriado.
- Verificar las horas con `python -I 00_Gestion/scripts/verificar_horas.py <acta.docx> MM,GA,CS,LS`.

## Herramientas locales
- Python 3.14 con `python-docx`, `openpyxl` y `python-pptx` disponibles para leer y generar .docx, .xlsx y .pptx.
- Al usar Python con `-I`, configurar la salida en UTF-8 (`sys.stdout.reconfigure(encoding="utf-8")`), porque la consola usa cp1252.
