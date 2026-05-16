import functions
import os

#Politécnico Jaime Isaza
pm10 = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Politecnico Jaime Isaza\reporte_sisaire PM10 Politecnico Jaime Isaza.csv")
humedad = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Politecnico Jaime Isaza\reporte_sisaire Humedad relativa del aire Politecnico Jaime Isaza.csv")
precipitaciones = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Politecnico Jaime Isaza\reporte_sisaire Precipitaciones Politecnico Jaime Isaza.csv")
temperatura = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Politecnico Jaime Isaza\reporte_sisaire Temperatura Politecnico Jaime Isaza.csv")
vviento = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Politecnico Jaime Isaza\reporte_sisaire Velocidad del viento Politecnico Jaime Isaza.csv")

table_Politecnico_Jaime_Isaza = functions.crear_tabla (pm10, 'PM10', humedad, precipitaciones, temperatura, vviento, 'Politecnico Jaime Isaza')


#Almacen general de EPM
pm10 = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Almacen general de EPM\reporte_sisaire PM10 Almacen EPM.csv")
humedad = functions.leer_ruta (r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Almacen general de EPM\reporte_sisaire Humedad relativa del aire Almacen EPM.csv")
precipitaciones = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Almacen general de EPM\reporte_sisaire Precipitaciones Almacen EPM.csv")
temperatura = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Almacen general de EPM\reporte_sisaire Temperatura Almacen EPM.csv")
vviento = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Almacen general de EPM\reporte_sisaire Velocidad del viento Almacen EPM.csv")

table_Almacen_EPM = functions.crear_tabla (pm10, 'PM10', humedad, precipitaciones, temperatura, vviento, 'Almacen General EPM')

#Tanques de la Ye
ozono = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tanques de la Ye\reporte_sisaire Ozono Tanques de la Ye.csv")
humedad = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tanques de la Ye\reporte_sisaire Humedad relativa del aire Tanques de la Ye.csv")
precipitaciones = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tanques de la Ye\Precipitaciones Tanques de la Ye.csv")
temperatura = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tanques de la Ye\reporte_sisaire Temperatura Tanques de la Ye.csv")
vviento = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tanques de la Ye\reporte_sisaire Velocidad del viento Tanques de la Ye.csv")

table_Tanques_Ye = functions.crear_tabla (ozono, 'O3', humedad, precipitaciones, temperatura, vviento, 'Tanques de la Ye')

#Universidad CES
ozono = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad CES\reporte_sisaire Ozono Uni CES.csv")
humedad = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad CES\reporte_sisaire Humedad relativa del aire Uni CES.csv")
precipitaciones = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad CES\reporte_sisaire Precipitaciones Uni CES.csv")
temperatura = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad CES\reporte_sisaire Temperatura Uni CES.csv")
vviento = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad CES\reporte_sisaire Velocidad del viento Uni CES.csv")

table_Universidad_CES = functions.crear_tabla (ozono, 'O3', humedad, precipitaciones, temperatura, vviento, 'Universidad CES')


#Universidad de Medellin
ozono = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad de Medellin\reporte_sisaire Ozono Universidad de Medellin.csv")
humedad = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad de Medellin\reporte_sisaire Humedad relativa del aire Universidad de Medellin.csv")
precipitaciones = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad de Medellin\reporte_sisaire Precipitaciones Universidad de Medellin.csv")
temperatura = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad de Medellin\reporte_sisaire Temperatura Universidad de Medellin.csv")
vviento = functions.leer_ruta(r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Universidad de Medellin\reporte_sisaire Velocidad del viento Universidad de Medellin.csv")

table_Universidad_Medellin = functions.crear_tabla (ozono, 'O3', humedad, precipitaciones, temperatura, vviento, 'Universidad de Medellín')

#Se agrega la columna 'evento' para determinar cuándo está dentro de la norma mínima y cuándo no

Almacen_EPM = functions.definir_evento(table_Almacen_EPM, 'PM10')
Politecnico_Jaime_Isaza = functions.definir_evento(table_Politecnico_Jaime_Isaza, 'PM10')
Tanques_Ye = functions.definir_evento(table_Tanques_Ye, 'O3')
Universidad_CES = functions.definir_evento(table_Universidad_CES, 'O3')
Universidad_Medellin = functions.definir_evento(table_Universidad_Medellin, 'O3')

estaciones = {
    "Almacen EPM": Almacen_EPM,
    "Politecnico Jaime Isaza": Politecnico_Jaime_Isaza,
    "Tanques_Ye": Tanques_Ye,
    "Universidad CES": Universidad_CES,
    "UdeM": Universidad_Medellin
}

for nombre, df in estaciones.items():
    print(nombre, len(df))



carpeta = r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tablas procesadas"
os.makedirs(carpeta, exist_ok=True)

for nombre, df in estaciones.items():
    df.to_csv(os.path.join(carpeta, f"{nombre}.csv"))

print("Archivos guardados en:", carpeta)