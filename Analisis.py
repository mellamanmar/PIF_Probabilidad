import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta_humedad = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Humedad relativa del aire Universidad de Medellin.csv"

df = pd.read_csv(ruta_humedad, sep=",", engine="python")

datos = df["HAire10"].astype(float)

print("\n========== ESTADÍSTICA DESCRIPTIVA ==========\n")

# Medidas de tendencia central
media = np.mean(datos)
mediana = np.median(datos)
moda = datos.mode()[0]

# Medidas de dispersión
varianza = np.var(datos, ddof=1)
desviacion = np.std(datos, ddof=1)
minimo = np.min(datos)
maximo = np.max(datos)
rango = maximo - minimo

# Cuartiles
q1 = np.percentile(datos, 25)
q2 = np.percentile(datos, 50)
q3 = np.percentile(datos, 75)

# Coeficiente de variación
coef_var = desviacion / media

print("Cantidad de datos:", len(datos))
print("\n--- Tendencia Central ---")
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

print("\n--- Dispersión ---")
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Rango:", rango)
print("Coeficiente de variación:", coef_var)

print("\n--- Cuartiles ---")
print("Q1 (25%):", q1)
print("Q2 (50%):", q2)
print("Q3 (75%):", q3)

print("\n=============================================\n")

# Histograma
plt.hist(datos, bins=20)
plt.title("Histograma - Humedad Relativa")
plt.xlabel("Humedad (%)")
plt.ylabel("Frecuencia")
plt.show()



#---------------------------------------------------------------------------
ruta_ozono = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Ozono Universidad de Medellin.csv"

df = pd.read_csv(ruta_ozono, sep=",", engine="python")

datos = df["O3"].astype(float)

print("\n========== ESTADÍSTICA DESCRIPTIVA OZONO (O3) ==========\n")

print("Cantidad de datos:", len(datos))

print("\n--- Medidas de Tendencia Central ---")
print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Moda:", datos.mode()[0])

print("\n--- Medidas de Dispersión ---")
print("Varianza:", np.var(datos, ddof=1))
print("Desviación estándar:", np.std(datos, ddof=1))
print("Mínimo:", np.min(datos))
print("Máximo:", np.max(datos))
print("Rango:", np.max(datos) - np.min(datos))
print("Coeficiente de variación:", np.std(datos, ddof=1) / np.mean(datos))

print("\n--- Cuartiles ---")
print("Q1 (25%):", np.percentile(datos, 25))
print("Q2 (50%):", np.percentile(datos, 50))
print("Q3 (75%):", np.percentile(datos, 75))

print("\n========================================================\n")

# Histograma
plt.figure(figsize=(8,5))
plt.hist(datos, bins=20)
plt.title("Histograma - Ozono (O3)")
plt.xlabel("Concentración de O3")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
#---------------------------------------------------------------------------
ruta_precipitacion = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Precipitaciones Universidad de Medellin.csv"

df = pd.read_csv(ruta_precipitacion, sep=",", engine="python")

datos = df["P"].astype(float)

print("\n========== ESTADÍSTICA DESCRIPTIVA PRECIPITACIÓN (P) ==========\n")

print("Cantidad de datos:", len(datos))

print("\n--- Medidas de Tendencia Central ---")
print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Moda:", datos.mode()[0])

print("\n--- Medidas de Dispersión ---")
print("Varianza:", np.var(datos, ddof=1))
print("Desviación estándar:", np.std(datos, ddof=1))
print("Mínimo:", np.min(datos))
print("Máximo:", np.max(datos))
print("Rango:", np.max(datos) - np.min(datos))
print("Coeficiente de variación:", np.std(datos, ddof=1) / np.mean(datos))

print("\n--- Cuartiles ---")
print("Q1 (25%):", np.percentile(datos, 25))
print("Q2 (50%):", np.percentile(datos, 50))
print("Q3 (75%):", np.percentile(datos, 75))

print("\n===============================================================\n")

# Histograma
plt.figure(figsize=(8,5))
plt.hist(datos, bins=20)
plt.title("Histograma - Precipitación (P)")
plt.xlabel("Precipitación")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
#---------------------------------------------------------------------------
ruta_temp = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Temperatura Universidad de Medellin.csv"

df = pd.read_csv(ruta_temp, sep=",", engine="python")

datos = df["TMPR AIR 10CM"].astype(float)

print("\n========== ESTADÍSTICA DESCRIPTIVA TEMPERATURA ==========\n")

print("Cantidad de datos:", len(datos))

print("\n--- Tendencia Central ---")
print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Moda:", datos.mode()[0])

print("\n--- Dispersión ---")
print("Varianza:", np.var(datos, ddof=1))
print("Desviación estándar:", np.std(datos, ddof=1))
print("Mínimo:", np.min(datos))
print("Máximo:", np.max(datos))
print("Rango:", np.max(datos) - np.min(datos))
print("Coeficiente de variación:", np.std(datos, ddof=1) / np.mean(datos))

print("\n--- Cuartiles ---")
print("Q1:", np.percentile(datos, 25))
print("Q2:", np.percentile(datos, 50))
print("Q3:", np.percentile(datos, 75))

#HISTOGRAMA
plt.figure(figsize=(8,5))
plt.hist(datos, bins=20)
plt.title("Histograma - Temperatura")
plt.xlabel("Temperatura")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
#---------------------------------------------------------------------------
ruta_viento = r"C:\Users\jhoad\OneDrive\Documentos\Pif_Probabilidad\reporte_sisaire Velocidad del viento Universidad de Medellin.csv"

df = pd.read_csv(ruta_viento, sep=",", engine="python")

datos = df["VViento"].astype(float)

print("\n========== ESTADÍSTICA DESCRIPTIVA VELOCIDAD DEL VIENTO ==========\n")

print("Cantidad de datos:", len(datos))

print("\n--- Tendencia Central ---")
print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Moda:", datos.mode()[0])

print("\n--- Dispersión ---")
print("Varianza:", np.var(datos, ddof=1))
print("Desviación estándar:", np.std(datos, ddof=1))
print("Mínimo:", np.min(datos))
print("Máximo:", np.max(datos))
print("Rango:", np.max(datos) - np.min(datos))
print("Coeficiente de variación:", np.std(datos, ddof=1) / np.mean(datos))

print("\n--- Cuartiles ---")
print("Q1:", np.percentile(datos, 25))
print("Q2:", np.percentile(datos, 50))
print("Q3:", np.percentile(datos, 75))

plt.figure(figsize=(8,5))
plt.hist(datos, bins=20)
plt.title("Histograma - Velocidad del Viento")
plt.xlabel("Velocidad del viento")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()