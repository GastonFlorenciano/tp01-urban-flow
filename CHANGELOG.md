
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
