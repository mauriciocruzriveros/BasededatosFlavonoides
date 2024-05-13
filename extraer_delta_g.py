import pandas as pd
import os

# Rutas de trabajo
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_trabajo = os.path.join(directorio_actual, "docking_ucp2_flavonoids")

# Para guardar la información
information = []

# Función para extraer valores delta g más óptimos y combinarlos con la columna de interés
def processing_archive(archive, carpet_name):
    line27_values = None
    with open(archive, 'r') as f:
        for num_line, line in enumerate(f, 1):
            if num_line == 27:
                line27_values = line.strip().split()  # Divide la línea en una lista de valores
                break                                       
    if line27_values is None or len(line27_values) != 4:
        return None  # Si no se encuentran valores o no hay exactamente 4 valores, retorna None
    
    # Combina el resultado de delta G con la columna de interés "ChEBI ID"
    return {"ChEBI ID": carpet_name, "deltag": line27_values[1]}

for carpet, _, multiple_archive in os.walk(ruta_trabajo):
    for archive in multiple_archive:
        if archive == "log.txt":
            full_route = os.path.join(carpet, archive)
            archive_dates = processing_archive(full_route, os.path.basename(carpet))
            if archive_dates:  # Verifica si se obtuvo un diccionario válido
                information.append(archive_dates)

# Crear DataFrame con los resultados de delta G
df = pd.DataFrame(information)

# Convertir la columna "ChEBI ID" a int64 en el DataFrame df
df['ChEBI ID'] = df['ChEBI ID'].astype('int64')

# Definir la ruta del archivo CSV original de los flavonoides y el archivo final
flavonoids_csv_path = os.path.join(directorio_actual, "flavonoids_data.csv")
output_csv_path = os.path.join(directorio_actual, "flavonoids_data_final.csv")

# Cargar los datos del archivo CSV original de los flavonoides en un DataFrame
flavonoids_df = pd.read_csv(flavonoids_csv_path)

# Fusionar los DataFrames en función de la columna correcta ("ChEBI ID")
merged_df = pd.merge(flavonoids_df, df, on='ChEBI ID', how='left')

# Guardar el DataFrame fusionado en el nuevo archivo CSV
merged_df.to_csv(output_csv_path, index=False)
print(f"Se han traspasado los datos desde csv.prueba al nuevo archivo {output_csv_path}.")



