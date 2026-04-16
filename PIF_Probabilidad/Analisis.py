import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# =============================================================================
# CONFIGURACIÓN GLOBAL
# =============================================================================
BASE_DIR = r"C:\Users\Carmelo\Desktop\PIF\PIF_Probabilidad"

# Mapeo de sedes: { Nombre Carpeta: Sufijo Archivo }
ESTACIONES_CONFIG = {
    "Universidad de Medellin": "Universidad de Medellin",
    "Universidad CES": "Uni CES",
    "Politecnico Jaime Isaza": "Politecnico Jaime Isaza",
    "Tanques de la Ye": "Tanques de la Ye",
    "Almacen general de EPM": "Almacen EPM"
}

# Definición de variables posibles y sus columnas correspondientes
VARIABLES_MAESTRAS = [
    {"archivo": "Humedad relativa del aire", "columna": "HAire10", "titulo": "Humedad Relativa (%)"},
    {"archivo": "Ozono", "columna": "O3", "titulo": "Ozono (O3)"},
    {"archivo": "PM10", "columna": "PM10", "titulo": "PM10"},
    {"archivo": "Precipitaciones", "columna": "P", "titulo": "Precipitaciones (mm)"},
    {"archivo": "Temperatura", "columna": "TMPR AIR 10CM", "titulo": "Temperatura (°C)"},
    {"archivo": "Velocidad del viento", "columna": "VViento", "titulo": "Velocidad del Viento (m/s)"}
]

# =============================================================================
# FUNCIONES DE SOPORTE
# =============================================================================
def encontrar_archivo(folder_path, nombre_parcial, suffix):
    """Busca el archivo en la carpeta con y sin el prefijo 'reporte_sisaire'."""
    posibles = [
        f"reporte_sisaire {nombre_parcial} {suffix}.csv",
        f"{nombre_parcial} {suffix}.csv"
    ]
    for p in posibles:
        ruta = os.path.join(folder_path, p)
        if os.path.exists(ruta):
            return ruta
    return None

def generar_analisis_subplot(ruta_csv, columna, titulo, ax):
    """Calcula estadísticas y grafica en un subplot dado."""
    try:
        df = pd.read_csv(ruta_csv, sep=",", engine="python")
        datos = df[columna].astype(float).dropna()
    except Exception as e:
        ax.set_visible(False)
        return None

    # Cálculos
    stats = {
        "Media": np.mean(datos),
        "Mediana": np.median(datos),
        "Moda": datos.mode()[0],
        "Varianza": np.var(datos, ddof=1),
        "Desviación Est.": np.std(datos, ddof=1),
        "Mínimo": np.min(datos),
        "Máximo": np.max(datos),
        "Rango": np.max(datos) - np.min(datos),
        "Q1 (25%)": np.percentile(datos, 25),
        "Q2 (50%)": np.percentile(datos, 50),
        "Q3 (75%)": np.percentile(datos, 75),
        "IQR": np.percentile(datos, 75) - np.percentile(datos, 25),
        "Asimetría": datos.skew(),
        "Curtosis": datos.kurt()
    }

    # Gráfico
    ax.hist(datos, bins=25, color='skyblue', edgecolor='white', alpha=0.7, density=True)
    ax.axvline(stats['Media'], color='red', linestyle='--', linewidth=1.2, label=f"Media: {stats['Media']:.2f}")
    ax.axvline(stats['Mediana'], color='green', linestyle='-', linewidth=1.2, label=f"Mediana: {stats['Mediana']:.2f}")
    ax.set_title(titulo, fontsize=10, fontweight='bold')
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)
    
    return stats

# =============================================================================
# EJECUCIÓN DEL BUCLE AUTOMÁTICO
# =============================================================================
if __name__ == "__main__":
    plt.style.use('bmh')
    
    for estacion_nombre, suffix in ESTACIONES_CONFIG.items():
        print(f"\n" + "="*60)
        print(f" PROCESANDO SEDE: {estacion_nombre.upper()} ")
        print("="*60)
        
        folder_path = os.path.join(BASE_DIR, estacion_nombre)
        if not os.path.exists(folder_path):
            print(f"AVISO: La carpeta {estacion_nombre} no existe.")
            continue

        # Crear figura (2 filas x 3 columnas para hasta 6 variables)
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 10))
        fig.suptitle(f"Reporte Estadístico Unificado: {estacion_nombre}", fontsize=16, fontweight='bold')
        axes_flat = axes.flatten()
        
        idx = 0
        for var in VARIABLES_MAESTRAS:
            ruta = encontrar_archivo(folder_path, var['archivo'], suffix)
            if ruta:
                print(f"-> Analizando {var['titulo']}...")
                stats = generar_analisis_subplot(ruta, var['columna'], var['titulo'], axes_flat[idx])
                
                # Imprimir tabla resumida en consola
                if stats:
                    resumen_txt = f"   [M] {stats['Media']:.2f} | [Med] {stats['Mediana']:.2f} | [Asim] {stats['Asimetría']:.2f}"
                    print(resumen_txt)
                    idx += 1
        
        # Ocultar ejes sobrantes
        for j in range(idx, len(axes_flat)):
            axes_flat[j].set_visible(False)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Guardar imagen
        out_root = os.path.join(BASE_DIR, "graficos")
        if not os.path.exists(out_root): os.makedirs(out_root)
        save_name = os.path.join(out_root, f"resumen_{estacion_nombre.replace(' ', '_').lower()}.png")
        plt.savefig(save_name)
        
        print(f"\nFINALIZADO: Resumen guardado en {save_name}")
        print("Cierra la ventana del gráfico para continuar con la siguiente sede...")
        
        plt.show() # Bloqueante: espera a que el usuario cierre la ventana

    print("\n" + "#"*60)
    print(" ANÁLISIS GLOBAL COMPLETADO CON ÉXITO ")
    print("#"*60)