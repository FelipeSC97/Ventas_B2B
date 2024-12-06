import os
import pandas as pd

# Llamar y concatenar archivos de la carpeta "Results"
folder_path = r"C:\Users\fsanc\OneDrive - Universidad EAFIT\Documentos\Pipe\OneDrive - Universidad EAFIT\Maestría\Trabajo de Grado\Results"
dataframes = []

for file in os.listdir(folder_path):
    if file.endswith(".csv"):  # Verificar que el archivo sea un CSV
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)  # Cargar el archivo CSV
        dataframes.append(df)

concatenated_df = pd.concat(dataframes, ignore_index=True)

output_path = os.path.join(folder_path, "Resultados.xlsx")
concatenated_df.to_excel(output_path, index=False, header=True)

print(f"Archivo generado exitosamente: {output_path}")
