total_infracciones = len(df_infracciones)
infracciones_fecha_error = len(df_infracciones[df_infracciones['fecha'] == '1932-01-01'])

if total_infracciones > 0:
    porcentaje_fecha_error = (infracciones_fecha_error / total_infracciones) * 100
    print(f"Porcentaje de infracciones en la fecha '1932-01-01': {porcentaje_fecha_error:.2f}%")
else:
    print("No hay infracciones registradas para calcular el porcentaje.")

    infracciones_hora_00 = len(df_infracciones[df_infracciones['hora'] == '00:00'])

if total_infracciones > 0:
    porcentaje_hora_00 = (infracciones_hora_00 / total_infracciones) * 100
    print(f"Porcentaje de infracciones a las 00:00: {porcentaje_hora_00:.2f}%")
else:
    print("No hay infracciones registradas para calcular el porcentaje.")
