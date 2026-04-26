# @title Normalizacion de Datos
import pandas as pd 

def normalizar_datos(df: pd.DataFrame) -> pd.DataFrame:
  """
  Normaliza las columnas fecha, hora, ubicacion y patente del dataset.
  """
  # Normalización de fecha
  df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)
  df["fecha"] = df["fecha"].fillna(pd.Timestamp("1932-01-01"))
  print('--------- FECHA ---------')
  print(df['fecha'].dt.strftime('%Y-%m-%d').head(10))

  # Normalización de hora
  df["hora"] = pd.to_datetime(
    df["hora"], errors="coerce", format="mixed"
  ).dt.strftime("%H:%M")
  df["hora"] = df["hora"].fillna("00:00")
  print('\n--------- HORAS ---------')
  print(df['hora'].head(10))


  # Normalización por Regex (ubicación)
  df["ubicacion"] = (
    df["ubicacion"].astype(str).str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)
    .str.upper()
  )
  print('\n--------- UBICACION ---------')
  print(df['ubicacion'].head(10))

  # Normalización de patente
  df["patente"] = (
    df["patente"].astype(str).str.upper()
    .str.replace(r"[^A-Z0-9]", "", regex=True)
  )
  df["patente"] = df["patente"].replace("", pd.NA)
  print('\n--------- PATENTE ---------')
  print(df['patente'].tail(10))

  return df
