#@title Exceso de Velocidad y Persistencia
import pandas as pd

def calcular_infracciones(df: pd.DataFrame) -> pd.DataFrame:
  """Calcula excesos de velocidad, muestra resultados y filtra infracciones."""
  
  # Exceso real
  df["exceso_velocidad_real"] = df["velocidad_registrada"] - df["velocidad_maxima"]
  print("\n--- 10 primeras patentes y exceso real ---")
  print(df[["patente", "exceso_velocidad_real"]].head(10))

  # Exceso legal (tolerancia 5%)
  df["exceso_velocidad"] = df["velocidad_registrada"] - (df["velocidad_maxima"] * 1.05)
  print("\n--- 10 primeras patentes y exceso legal (5% margen) ---")
  print(df[["patente", "exceso_velocidad"]].head(10))

  # Filtrado de infracciones y reporte
  filas_antes = len(df)
  df_infracciones = df[df["exceso_velocidad"] > 0].copy()
  
  filas_eliminadas = filas_antes - len(df_infracciones)
  print(f"\nSe eliminaron {filas_eliminadas} filas que no cometieron infracciones.")
  
  return df_infracciones
