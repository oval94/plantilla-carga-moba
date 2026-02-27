import pandas as pd

# Cargar archivo
df = pd.read_excel("Elementos.xlsx")

# Tipos de contenedor y sus columnas asociadas
tipos = [
    ("RESTO", "UDES. RESTO"),
    ("ENVASES", "UDES. ENVASES"),
    ("PAPEL", "UDE.PAPEL"),
    ("VIDRIO", "UDES.VIDRIO"),
    ("OTRO", "UDES.OTRO"),
    ("ACEITE", "UDES.ACEITE"),
    ("TEXTIL", "UDES.TEXTIL"),
    ("ESPECIALES", "UDES.ESPECIALES")
]

filas = []

for _, row in df.iterrows():
    for tipo, col_unidades in tipos:
        modelo = row.get(tipo)
        unidades = row.get(col_unidades)

        if pd.notna(modelo) and pd.notna(unidades) and unidades > 0:
            for i in range(1, int(unidades) + 1):
                nueva_fila = {
                    "ISLA": row["ISLA"],
                    "SITIO": row["SITIO"],
                    "CALLE": row["CALLE"],
                    "NUM": row["NUM"],
                    "INFO ADICIONAL": row["INFO ADICIONAL"],
                    "TIPO_RESIDUO": tipo,
                    "MODELO_CONTENEDOR": modelo,
                    "UNIDAD": i,
                    "LONGITUD": row["LONGITUD"],
                    "LATITUD": row["LATITUD"]
                }
                filas.append(nueva_fila)

# Crear nuevo dataframe
df_final = pd.DataFrame(filas)

# Guardar resultado
df_final.to_excel("Elementos_normalizado.xlsx", index=False)

print("Proceso terminado. Archivo generado: Elementos_normalizado.xlsx")