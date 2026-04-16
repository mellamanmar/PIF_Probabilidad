from Normalizar_datos import preparar_dataset 
import os

# =============================================================================
# CONFIGURACIÓN DE RUTAS Y ESTACIÓN
# =============================================================================
BASE_DIR = r"C:\Users\Carmelo\Desktop\PIF\PIF_Probabilidad"
ESTACION = "Universidad de Medellin"

# Mapeo de sufijos de archivos según la estación
ESTACIONES_SUFFIX = {
    "Universidad de Medellin": "Universidad de Medellin",
    "Universidad CES": "Uni CES",
    "Politecnico Jaime Isaza": "Politecnico Jaime Isaza",
    "Tanques de la Ye": "Tanques de la Ye",
    "Almacen general de EPM": "Almacen EPM"
}

SUFFIX = ESTACIONES_SUFFIX.get(ESTACION, ESTACION)
FOLDER_PATH = os.path.join(BASE_DIR, ESTACION)

def obtener_ruta(nombre_parcial):
    posibles_nombres = [
        f"reporte_sisaire {nombre_parcial} {SUFFIX}.csv",
        f"{nombre_parcial} {SUFFIX}.csv"
    ]
    for nombre in posibles_nombres:
        ruta = os.path.join(FOLDER_PATH, nombre)
        if os.path.exists(ruta):
            return ruta
    return None

# =============================================================================
# DEFINICIÓN DE RUTAS DINÁMICAS
# =============================================================================
ruta_humedad_aire = obtener_ruta("Humedad relativa del aire")
ruta_ozono = obtener_ruta("Ozono")
ruta_precipitaciones = obtener_ruta("Precipitaciones")
ruta_temperatura = obtener_ruta("Temperatura")
ruta_velocidad_viento = obtener_ruta("Velocidad del viento")

# =============================================================================
# PROCESAMIENTO
# =============================================================================
if __name__ == "__main__":
    print(f"Preparando datasets para la sede: {ESTACION}")
    
    if ruta_velocidad_viento:
        preparar_dataset(ruta_velocidad_viento, columna_valor="VViento")
    else:
        print("AVISO: No se encontró el archivo de Velocidad del Viento.")

    # Descomentar según necesidad:
    # if ruta_humedad_aire: preparar_dataset(ruta_humedad_aire, columna_valor="HAire10")
    # if ruta_ozono: preparar_dataset(ruta_ozono, columna_valor="O3")
    # if ruta_precipitaciones: preparar_dataset(ruta_precipitaciones, columna_valor="P")
    # if ruta_temperatura: preparar_dataset(ruta_temperatura, columna_valor="TMPR AIR 10CM")