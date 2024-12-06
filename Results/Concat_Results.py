import os
import pandas as pd

# Llamar y concatenar archivos de la carpeta "Results"
folder_path = r"C:\Users\fsanc\OneDrive - Universidad EAFIT\Documentos\Pipe\OneDrive - Universidad EAFIT\Maestría\Trabajo de Grado\Results"
dataframes = []

for file in os.listdir(folder_path):
    if file.endswith(".csv"): 
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)  # Cargar sólo archivos CSV
        dataframes.append(df)

concatenated_df = pd.concat(dataframes, ignore_index=True)
concatenated_df['model_type'] = concatenated_df['model_name'].apply(
    lambda x: "Machine Learning" if x in ["RandomForestRegressor", "XGBRegressor"] else "Estadístico Tradicional"
)
concatenated_df = concatenated_df.sort_values(by='model_type', key=lambda x: x.map({
    "Estadístico Tradicional": 0,
    "Machine Learning": 1
}))
columns_order = ['model_type'] + [col for col in concatenated_df.columns if col != 'model_type']
concatenated_df = concatenated_df[columns_order]

# Generar nuevo archivo
output_path = os.path.join(folder_path, "Resultados.xlsx")
concatenated_df.to_excel(output_path, index=False, header=True)

print(f"Archivo generado exitosamente: {output_path}")