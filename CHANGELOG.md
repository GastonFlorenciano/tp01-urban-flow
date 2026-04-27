
## [Día 1] - Ejercicio 01 -Inicialización de Git y Estructura de Carpetas.
### Cambiado
- Creación de repositorio.
- Creación de estructura de carpetas.
- Creación de directorios `data/raw`, `data/interim/plots` y `data/processed`.
- Implementación de verificaciones de existencia (`os.path.exists`) para evitar redundancia en el Runtime.

## [Día 2] - Ejercicio 02
### Agregado
- Ingesta exitosa del dataset `speeding_fines.csv` en la carpeta `raw`.
- Análisis exploratorio inicial mediante visualización de cabecera (`head`), tipos de datos (`dtypes`) y detección de nulos (`isnull`).
### Observaciones Técnicas
- Se detectaron valores nulos significativos en las columnas `patente`, `velocidad_registrada` y `radar_id`.
- Se identificaron textos de error como 'invalid_date' e 'invalid_hour' en las primeras filas de las columnas de tiempo.
- Se observó que las columnas de fecha y hora se cargaron como objetos de texto.

## [Día 3] - Ejercicio 03
### Cambiado
- Fechas a ISO 8601 (YYYY-MM-DD) y horas a formato 24h.
- Limpieza de caracteres especiales mediante Regex y estandarización a mayúsculas en 'ubicacion' y 'patente'.
### Agregado
- Valores predeterminados para fechas (1932-01-01) y horas (00:00) inválidas.
- Eliminación de registros con nulos en dimensiones críticas como patente, velocidades.
- Remoción de outliers en 'velocidad_registrada' mediante el método de Rango Intercuartílico IQR.
- Creación de columnas 'exceso_velocidad_real' y 'exceso_velocidad' incluyendo margen técnico del 5%.
- Eliminación de registros que no constituyen infracción bajo el umbral legal.
- Almacenamiento del dataset procesado en 'data/interim/'.

## Día 4
- Análisis de infracciones por ubicación completado.

## Día 4
- Calculo de exceso de velocidad.
- Creacion de la clase FineAnalyzer.
- Creacion de los rankings.

## Día 4
- Análisis de infracciones por ubicación completado.
- Calculo de exceso de velocidad.
- Creacion de la clase FineAnalyzer.
- Creacion de los rankings.

## Día 4
- Calculo de exceso de velocidad.
- Creacion de la clase FineAnalyzer.
- Creacion de los rankings.

## Día 5
- Creación de gráficos de barras (meses), torta (horas) e histogramas (patentes).
- Implementación de gráficos de líneas para análisis de variabilidad en datos recuperados.
- Validación de infracciones reales (velocidad registrada > permitida) en los gráficos de líneas.
- Exportación automática de visualizaciones a la carpeta interim/plots.

## Día 6
- Cálculo del porcentaje de infracciones con fecha de error (1932-01-01).
- Cálculo del porcentaje de infracciones ocurridas a las 00:00.
