# @title Dataset Raw Analisis
import pandas as pd

def analizar_dataset(df: pd.DataFrame) -> None:
  """
  Realiza un análisis exploratorio básico del DataFrame.
  
  Args:
    df (pd.DataFrame): El DataFrame a analizar.
  """
  print("--- Análisis del Dataset ---")
  print(f"Dimensiones (filas, columnas): {df.shape}")
  print("\nPrimeras 5 filas:")
  print(df.head())
  print("\nTipos de datos:")
  print(df.dtypes)
  print("\nValores nulos por columna:")
  print(df.isnull().sum())
  print("----------------------------")
