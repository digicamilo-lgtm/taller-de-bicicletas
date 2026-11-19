# Verifica que las horas de cada integrante sumen la capacidad de cada sprint en la tabla de "Tiempos Asociados" del acta.
# Uso: python -I verificar_horas.py <acta.docx> MM,GA,CS,LS
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
import docx
from docx.table import Table

d = docx.Document(sys.argv[1])
members = sys.argv[2].split(",")
main = d.tables[0]

def find_sprint_table(tbl):
    for row in tbl.rows:
        for c in row.cells:
            for t in c.tables:
                if t.rows[0].cells[0].text.strip().startswith("Sprint / fechas"):
                    return t
                r = find_sprint_table(t)
                if r: return r
    return None

st = find_sprint_table(main)
ok_all = True
for row in st.rows[1:]:
    name = " ".join(row.cells[0].text.split()[:2])
    text = row.cells[2].text
    tot = {m: 0 for m in members}
    for m, h in re.findall(r"\((%s), (\d+) h" % "|".join(members), text):
        tot[m] += int(h)
    for h in re.findall(r"apoyo (%s) (\d+) h" % "|".join(members), text):
        tot[h[0]] += int(h[1])
    ev = re.findall(r"\(tod[oa]s, (\d+) h c/u\)", text)
    for m in members: tot[m] += int(ev[0]) if ev else 0
    cap = re.findall(r"capacidad (\d+) h", text)
    cap = int(cap[0]) if cap else None
    ok = all(v == cap for v in tot.values())
    ok_all &= ok
    print(f"{name:10s} cap={cap}  " + "  ".join(f"{m}={v}" for m, v in tot.items()) + ("  OK" if ok else "  <-- NO CUADRA"))
print("TODO CUADRA" if ok_all else "HAY DIFERENCIAS")
