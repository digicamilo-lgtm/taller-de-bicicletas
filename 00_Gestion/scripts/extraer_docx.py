# Extrae todo el texto de un .docx, incluidas las tablas anidadas, para revisarlo o compararlo.
# Uso: python -I extraer_docx.py <archivo.docx> > salida.txt
import sys; sys.stdout.reconfigure(encoding="utf-8")
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

def walk(el, parent, depth):
    ind = "  " * depth
    for child in el.iterchildren():
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            p = Paragraph(child, parent)
            t = p.text.strip()
            if t:
                print(f"{ind}{t}")
        elif tag == 'tbl':
            tbl = Table(child, parent)
            print(f"{ind}<<TABLE {len(tbl.rows)}x{len(tbl.columns)}>>")
            for ri, row in enumerate(tbl.rows):
                prev = None
                for ci, c in enumerate(row.cells):
                    if c._tc is prev: continue
                    prev = c._tc
                    print(f"{ind}  [r{ri}c{ci}]")
                    walk(c._tc, c, depth + 2)
            print(f"{ind}<<END TABLE>>")

d = docx.Document(sys.argv[1])
walk(d.element.body, d, 0)
print("=== SECTIONS / HEADERS ===")
for s in d.sections:
    for p in s.header.paragraphs:
        if p.text.strip(): print("HEADER:", p.text)
    for p in s.footer.paragraphs:
        if p.text.strip(): print("FOOTER:", p.text)
print("images:", len(d.inline_shapes))
