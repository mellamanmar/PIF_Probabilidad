from Normalizar_datos import preparar_dataset 

ruta_humedad_aire = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Humedad relativa del aire Universidad de Medellin.csv"
ruta_ozono = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Ozono Universidad de Medellin.csv"
ruta_precipitaciones = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Precipitaciones Universidad de Medellin.csv"
ruta_temperatura = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Temperatura Universidad de Medellin.csv"
ruta_velocidad_viento = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Velocidad del viento Universidad de Medellin.csv"

# preparar_dataset(ruta_humedad_aire, columna_valor= "HAire10")
# preparar_dataset(ruta_ozono, columna_valor= "O3")
# preparar_dataset(ruta_precipitaciones, columna_valor= "P")
# preparar_dataset(ruta_temperatura, columna_valor= "TMPR AIR 10CM")
preparar_dataset(ruta_velocidad_viento, columna_valor= "VViento")