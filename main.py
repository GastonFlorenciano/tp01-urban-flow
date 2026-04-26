import pandas as pd
from pathlib import Path
from src import (
  analizar_dataset, 
  normalizar_datos, 
  limpiar_dataset, 
  calcular_infracciones
)

def main():
  ruta_raw = Path("data/raw/speeding_fines.csv")
  df = pd.read_csv(ruta_raw)

  # Análisis inicial
  analizar_dataset(df)
    
  # Normalización
  print("--- Normalizacion del Dataframe --- ")
  df = normalizar_datos(df)

  # Limpieza
  print("--- Limpieza del Dataframe")
  print(f"Filas originales: {len(df)}")
  df_limpio = limpiar_dataset(df)
  print(f"Filas tras limpieza: {len(df_limpio)}")
  
  # Infracciones
  print("--- Cálculo de Infracciones ---")
  df_infracciones = calcular_infracciones(df_limpio)
  
  print("\n--- 10 primeras patentes y exceso legal ---")
  print(df_infracciones[['patente', 'exceso_velocidad']].head(10))
  
  # Persistimos a interim el Dataframe
  ruta_salida = Path("data/interim/speeding_fines_final.csv")
  df_infracciones.to_csv(ruta_salida, index=False)

if __name__ == "__main__":
  main()
