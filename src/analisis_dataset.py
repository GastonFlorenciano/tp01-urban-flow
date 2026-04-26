
import pandas as pd

#Clase para el analisis de multas de exceso de velocidad.
class FineAnalyzer:
  def __init__(self, df: pd.DataFrame) -> None:
    self._df = df.copy()

#Retorna el ranking top 5 patentes con más multas.
  def top_patentes(self) -> pd.DataFrame:
    ranking = (
        self._df['patente']
        .value_counts()
        .head(5)
        .reset_index()
    )
    ranking.columns = ['patente', 'cantidad_multas']
    ranking.index = pd.RangeIndex(start=1, stop=len(ranking) + 1)
    return ranking

#Retorna el ranking top 5 de horas con más multas.
  def top_horas(self) -> pd.DataFrame:
    ranking = (
        self._df['hora']
        .value_counts()
        .head(5)
        .reset_index()
    )
    ranking.columns = ['hora', 'cantidad_multas']
    ranking.index = pd.RangeIndex(start=1, stop=len(ranking) + 1)
    return ranking

#Retorna el exceso promedio de velocidad
  def exceso_promedio(self) -> float:
    return self._df['exceso_velocidad_real'].mean()

#Retorna el exceso promedio de velocidad legal
  def exceso_promedio_legal(self) -> float:
    return float(self._df['exceso_velocidad'].mean())

#Retorna el exceso real promedio de velocidad.
  def exceso_real_promedio(self) -> float:
    return float(self._df['exceso_velocidad_real'].mean())

#Retorna cantidad de multas por ubicación
  def multas_por_ubicacion(self) -> pd.DataFrame:
    resultado = (
        self._df['ubicacion']
        .value_counts()
        .reset_index()
    )
    resultado.columns = ['ubicacion', 'cantidad_multas']
    return resultado.sort_values(by='ubicacion')
