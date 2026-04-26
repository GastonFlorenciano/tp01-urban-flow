#@title Limpieza de Datos
import pandas as pd
from typing import List


def limpiar_dataset(df: pd.DataFrame) -> pd.DataFrame:
  """Limpia nulos en columnas relevantes y elimina outliers."""
  cols_relevantes = ["patente", "velocidad_registrada", "velocidad_maxima"]
  
  # Limpieza de Nulos (Requerimiento específico)
  registros_iniciales = len(df)
  df = df.dropna(subset=cols_relevantes)
  
  eliminados_nulos = registros_iniciales - len(df)
  print(f"\nSe eliminaron {eliminados_nulos} filas con valores vacíos.")
  print("Columnas observadas:")
  for col in cols_relevantes:
    print(f" - {col}")

  # Limpieza de Outliers (IQR)
  registros_antes_outliers = len(df)
  q1 = df["velocidad_registrada"].quantile(0.25)
  q3 = df["velocidad_registrada"].quantile(0.75)
  iqr = q3 - q1
  limite_inferior = q1 - 1.5 * iqr
  limite_superior = q3 + 2.5 * iqr
  
  df = df[(df["velocidad_registrada"] >= limite_inferior) & 
          (df["velocidad_registrada"] <= limite_superior)]
          
  print(f"\nSe eliminaron {registros_antes_outliers - len(df)} filas por outliers.")
  print("Columnas observadas:\n - velocidad_registrada")
  
  return df
