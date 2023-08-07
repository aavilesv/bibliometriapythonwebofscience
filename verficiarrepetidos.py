import bibtexparser

archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_12799.bib'
archivo_salida = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_unic.bib'

with open(archivo_bib, 'r', encoding='utf-8') as archivo:
    bib_database = bibtexparser.load(archivo)

claves_vistas = set()
entradas_unicas = []

for entrada in bib_database.entries:
    clave = entrada['ID']
    if clave not in claves_vistas:
        entradas_unicas.append(entrada)
        claves_vistas.add(clave)

# Crear un nuevo objeto BibDatabase con solo las entradas únicas
bib_database_unico = bibtexparser.bibdatabase.BibDatabase()
bib_database_unico.entries = entradas_unicas

# Guardar las entradas únicas en un nuevo archivo
with open(archivo_salida, 'w', encoding='utf-8') as archivo:
    bibtexparser.dump(bib_database_unico, archivo)

print(f"Las entradas únicas se han guardado en {archivo_salida}.")