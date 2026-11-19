# Bitácora del proyecto

> Registro cronológico de cada sesión de trabajo (la entrada más reciente va arriba).
> Formato: fecha · hito · qué se hizo · resultado · pendientes.

---

## 2026-11-19 (3ª sesión) · Repositorio en GitHub

**Qué se hizo**
- Se creó el repositorio [digicamilo-lgtm/taller-de-bicicletas](https://github.com/digicamilo-lgtm/taller-de-bicicletas)
  y se vinculó a esta carpeta (`origin`, rama `main`). Se creó privado y, a pedido del usuario, se cambió a **público** antes del primer push.
- El usuario decidió publicar **todo**, incluidos el acta del otro equipo (`05_Borradores/`) y el material del docente (D-009).
- Se agregó un `.gitignore` para archivos temporales de Office (`~$*`), del sistema y de Python.
- Primer commit con todo el proyecto: registro, enunciado, material, plantillas, entregables y borradores.

**Pendientes:** siguen los de [PENDIENTES.md](PENDIENTES.md). Si el equipo necesita acceso, invitarlo como colaborador.

---

## 2026-11-19 (2ª sesión) · H1 rehecho para el acta oficial

**Qué se hizo**
- Llegó `ahora siq ue si.docx`: es **el acta oficial del equipo de 4** (MM = Maximiliano Montoya, Scrum Master y jefe de proyecto;
  GA = Gianni Antonietti, Product Owner; CS = Camilo Sepúlveda; LS = Logan Silva). Según Maxi, la entrega ya estaba lista con esa acta.
- Se corrigió el registro: el acta revisada en la 1ª sesión (Natalia Martínez y otras 2 integrantes) **no es la del equipo**.
  Se movió a `05_Borradores/` (origen por confirmar) y su revisión quedó marcada como reemplazada.
- Se revisó el acta oficial: [REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md). Resultado: acta **29–30/30**, pero la **entrega no está
  lista**, porque el anexo de la Gantt y de Trello sigue vacío (30 de 60 pts).
- Se verificó con script: horas de 4 integrantes × 7 períodos = OK; formato carta; 16 páginas; similitud del 81 % con la versión de 3 integrantes.
- Se guardaron los scripts en [scripts/](scripts/) (`verificar_horas.py` y `extraer_docx.py`).

**Resultado:** H1 ✅ (rehecho)

**Pendientes y bloqueos**
- [ ] Equipo: ¿existen la Carta Gantt y el tablero Trello? (R-01)
- [ ] Equipo: ¿de quién es la versión de 3 integrantes? (R-03)
- [ ] Equipo (PO GA): aprobar OBS-01, OBS-02 y OBS-16 (cambian alcance y horas).
- [ ] Equipo: fecha de entrega, plantilla del informe INACAP y correo de contacto de MM.

**Cierre de sesión:** se creó [PENDIENTES.md](PENDIENTES.md) con las preguntas abiertas (P1–P7) y las tareas de H2–H6 en orden.
**La próxima sesión parte desde ese archivo.**

---

## 2026-11-19 · H0 + H1

**Qué se hizo**
- Se leyeron todos los documentos de la carpeta: el caso MasterBikes, las instrucciones de la evaluación U2, la pauta
  (escala de apreciación), la plantilla del acta, el acta llena v1.0, la plantilla de historias de usuario y las
  presentaciones de Scrum y Planificación.
- Se ordenó la carpeta en `00_Gestion` … `05_Borradores` y se renombraron los archivos (ver la tabla en el [README](../README.md)).
- Se creó el sistema de registro: README, CLAUDE.md, HITOS, BITACORA y DECISIONES.
- Se definieron los hitos H0–H9 antes de desarrollarlos.
- Se revisó el acta v1.0 ([REVISION_ACTA_v1.0.md](REVISION_ACTA_v1.0.md)): 12 observaciones y un puntaje estimado de 29/30 en C1–C10.
- Se verificó con un script: las fechas del cronograma, los feriados y que las horas cuadran con la capacidad en todos los sprints.

**Resultado:** H0 ✅ · H1 ✅

**Pendientes y bloqueos**
- [ ] Equipo: confirmar la **fecha de entrega** (semana 5 de clases).
- [ ] Equipo: indicar si ya existe la Carta Gantt o el tablero Trello fuera de esta carpeta.
- [ ] Equipo: conseguir la **plantilla oficial del informe INACAP** (es necesaria para H5).
- [ ] Equipo: correos de contacto de los integrantes (OBS-07).
- [ ] Equipo: validar el cambio de alcance de OBS-01 y OBS-02 antes de iniciar H2.
