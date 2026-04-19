import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tabulate import tabulate

# =============================================================================
# CONFIGURACIÓN GLOBAL
# =============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

# Explicaciones para cada variable
EXPLICACIONES = {
    "Humedad Relativa (%)": "La humedad relativa del aire indica el porcentaje de vapor de agua presente en el aire comparado con la cantidad máxima que el aire puede contener a esa temperatura. Una media alta sugiere condiciones húmedas, lo que puede influir en la comodidad térmica y la formación de niebla. La mediana representa el valor central de las mediciones, mientras que la desviación estándar mide la variabilidad de los datos. Valores extremos pueden indicar cambios climáticos o errores en las mediciones.",
    "Ozono (O3)": "El ozono es un gas que puede ser beneficioso en la estratosfera pero perjudicial a nivel del suelo. Las concentraciones se miden en partes por millón. Una media elevada puede indicar contaminación atmosférica. La asimetría positiva sugiere valores atípicos altos, posiblemente debido a eventos de smog. Monitorear estos niveles es crucial para la salud pública.",
    "PM10": "Las partículas PM10 son partículas suspendidas en el aire con un diámetro menor a 10 micrómetros. Altos niveles pueden afectar la calidad del aire y la salud respiratoria. La media y la mediana ayudan a entender la exposición promedio, mientras que el rango indica la variabilidad diaria. Valores por encima de los estándares pueden requerir medidas de control de emisiones.",
    "Precipitaciones (mm)": "Las precipitaciones se miden en milímetros y representan la cantidad de lluvia caída. La media indica el promedio de lluvia, útil para estudios hidrológicos. La mediana es menos afectada por valores extremos. La asimetría puede mostrar patrones de lluvias intensas. Estos datos son esenciales para la gestión del agua y la predicción de inundaciones.",
    "Temperatura (°C)": "La temperatura del aire se mide en grados Celsius. La media representa la temperatura promedio, mientras que la mediana es el valor central. La desviación estándar indica la variabilidad térmica. Cambios en estos estadísticos pueden reflejar patrones climáticos estacionales o tendencias de calentamiento global.",
    "Velocidad del Viento (m/s)": "La velocidad del viento se mide en metros por segundo. Una media alta indica condiciones ventosas, lo que puede dispersar contaminantes. La mediana es el valor típico. La curtosis puede indicar la frecuencia de vientos extremos. Estos datos son importantes para la modelación de la dispersión de contaminantes y la planificación urbana."
}

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
    ax.boxplot(datos, vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'), flierprops=dict(marker='o', color='red', markersize=3))
    ax.set_title(titulo, fontsize=10, fontweight='bold')
    ax.grid(alpha=0.3)

    # Añadir resumen estadístico en el gráfico
    resumen = (
        f"Media: {stats['Media']:.2f}\n"
        f"Mediana: {stats['Mediana']:.2f}\n"
        f"Desv. Est.: {stats['Desviación Est.']:.2f}\n"
        f"Min: {stats['Mínimo']:.2f}\n"
        f"Max: {stats['Máximo']:.2f}\n"
        f"Asimetría: {stats['Asimetría']:.2f}"
    )
    ax.text(
        0.02,
        0.98,
        resumen,
        transform=ax.transAxes,
        fontsize=8,
        va='top',
        ha='left',
        bbox=dict(facecolor='white', alpha=0.95, edgecolor='black', pad=6)
    )
    
    return stats


def imprimir_resumen_descriptivo(estacion_nombre, estadisticas, carpeta_salida):
    """Imprime y guarda un reporte con estadísticas descriptivas por variable."""
    textos = [f"Análisis descriptivo - {estacion_nombre}", "=" * (22 + len(estacion_nombre)), ""]
    for variable, valores in estadisticas.items():
        textos.append(f"{variable}")
        # Crear tabla de estadísticas
        table = [[clave, f"{valor:.2f}"] for clave, valor in valores.items()]
        tabla_str = tabulate(table, headers=['Estadístico', 'Valor'], tablefmt='grid')
        textos.append(tabla_str)
        textos.append("")
        textos.append(f"Explicación: {EXPLICACIONES.get(variable, 'No hay explicación disponible.')}")
        textos.append("")

    reporte = "\n".join(textos)
    print(reporte)

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    ruta_txt = os.path.join(carpeta_salida, f"resumen_{estacion_nombre.replace(' ', '_').lower()}.txt")
    with open(ruta_txt, 'w', encoding='utf-8') as f:
        f.write(reporte)

    print(f"Reporte descriptivo guardado en {ruta_txt}")
    return ruta_txt

# =============================================================================
# EJECUCIÓN DEL BUCLE AUTOMÁTICO
# =============================================================================
if __name__ == "__main__":
    plt.style.use('bmh')
    
    # Iterar por cada variable para crear gráficos comparativos entre estaciones
    for var in VARIABLES_MAESTRAS:
        print(f"\n" + "="*60)
        print(f" PROCESANDO VARIABLE: {var['titulo'].upper()} ")
        print("="*60)
        
        datos_por_estacion = []
        etiquetas_estaciones = []
        todas_las_stats = {}
        
        # Recolectar datos de todas las estaciones para esta variable
        for estacion_nombre, suffix in ESTACIONES_CONFIG.items():
            folder_path = os.path.join(BASE_DIR, estacion_nombre)
            ruta = encontrar_archivo(folder_path, var['archivo'], suffix)
            
            if ruta:
                try:
                    df = pd.read_csv(ruta, sep=",", engine="python")
                    datos = df[var['columna']].astype(float).dropna()
                    
                    # Debug especial para precipitaciones
                    if var['titulo'] == "Precipitaciones (mm)":
                        print(f"DEBUG Precipitaciones - {estacion_nombre}:")
                        print(f"  Archivo: {ruta}")
                        print(f"  Número de datos: {len(datos)}")
                        print(f"  Rango: {datos.min():.2f} - {datos.max():.2f}")
                        print(f"  Media: {datos.mean():.2f}")
                        print(f"  Valores únicos primeros 5: {datos.head().values}")
                    
                    datos_por_estacion.append(datos)
                    etiquetas_estaciones.append(estacion_nombre)
                    
                    # Calcular estadísticas
                    stats = {
                        "Media": np.mean(datos),
                        "Mediana": np.median(datos),
                        "Moda": datos.mode()[0] if len(datos.mode()) > 0 else np.nan,
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
                    todas_las_stats[estacion_nombre] = stats
                    print(f"-> {estacion_nombre}: Media={stats['Media']:.2f}, Mediana={stats['Mediana']:.2f}")
                except Exception as e:
                    print(f"   Error procesando {estacion_nombre}: {e}")
        
        # Crear boxplot comparativo si hay datos
        if datos_por_estacion:
            # Crear figura con mejor tamaño
            fig, ax = plt.subplots(figsize=(16, 9))
            
            # Definir colores para las cajas
            colores = ['#87CEEB', '#87CEEB', '#87CEEB', '#87CEEB', '#87CEEB']
            
            bp = ax.boxplot(datos_por_estacion, tick_labels=etiquetas_estaciones, patch_artist=True,
                           boxprops=dict(facecolor='#87CEEB', color='black', linewidth=1.5),
                           medianprops=dict(color='red', linewidth=2.5),
                           whiskerprops=dict(color='black', linewidth=1.5),
                           capprops=dict(color='black', linewidth=1.5),
                           flierprops=dict(marker='o', color='red', markersize=5, alpha=0.6))
            
            # Ajuste especial para precipitaciones si los valores son muy similares
            if var['titulo'] == "Precipitaciones (mm)":
                all_data = np.concatenate(datos_por_estacion)
                data_range = np.max(all_data) - np.min(all_data)
                data_mean = np.mean(all_data)
                
                print(f"Precipitaciones - Rango total: {data_range:.2f}, Media: {data_mean:.2f}")
                
                if data_range < 10:  # Si el rango es muy pequeño
                    margin = max(data_range * 0.5, 1.0)  # Al menos 1 unidad de margen
                    ax.set_ylim(data_mean - margin, data_mean + margin)
                    print(f"Ajustando escala Y: {data_mean - margin:.2f} - {data_mean + margin:.2f}")
                    
                    # Añadir grid más denso para mejor visualización
                    ax.grid(alpha=0.5, axis='y', linestyle='--', linewidth=0.7)
                    
                    # Hacer las cajas más visibles
                    for patch in bp['boxes']:
                        patch.set_linewidth(2.0)
                    
                    # Ajustar tamaño de los puntos outliers
                    if 'fliers' in bp:
                        for flier in bp['fliers']:
                            flier.set_markersize(8)
                            flier.set_alpha(0.8)
            
            # Añadir valores numéricos en el gráfico
            for i, datos in enumerate(datos_por_estacion):
                media = np.mean(datos)
                mediana = np.median(datos)
                moda = datos.mode()[0] if len(datos.mode()) > 0 else np.nan
                desv = np.std(datos, ddof=1)
                q1 = np.percentile(datos, 25)
                q3 = np.percentile(datos, 75)
                rango = np.max(datos) - np.min(datos)
                max_val = np.max(datos)
                min_val = np.min(datos)
                
                # Para precipitaciones, usar etiquetas más simples para no sobrecargar el gráfico
                if var['titulo'] == "Precipitaciones (mm)":
                    # Solo mostrar media y mediana, sin la etiqueta adicional
                    label_text = f'μ={media:.1f}'
                    label_y = q3 + (q3 - q1) * 0.1 if q3 != q1 else media * 1.02
                    ax.text(i+1, label_y, label_text, ha='center', va='bottom',
                           fontsize=9, fontweight='bold', color='darkblue',
                           bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
                else:
                    # Etiqueta completa para otras variables
                    label_text = (
                        f'μ={media:.1f}\n'
                        f'Med={mediana:.1f}\n'
                        f'Moda={moda:.1f}\n'
                        f'σ={desv:.2f}'
                    )
                    label_y = q3 + (q3 - q1) * 0.08 if q3 != q1 else media * 1.05
                    ax.text(i+1, label_y, label_text, ha='center', va='bottom',
                           fontsize=8, fontweight='bold', color='black',
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85))
                
                # Etiqueta de mediana (solo para variables que no sean precipitaciones)
                if var['titulo'] != "Precipitaciones (mm)":
                    ax.text(i+1, mediana, f'Med:{mediana:.1f}', ha='center', va='top',
                           fontsize=8, color='darkred',
                           bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow', alpha=0.7))
            
            # Configurar título y etiquetas con mejor tamaño
            ax.set_title(f"Comparativa: {var['titulo']} por Estación", 
                        fontsize=16, fontweight='bold', pad=20)
            ax.set_ylabel(var['titulo'], fontsize=13, fontweight='bold')
            ax.set_xlabel("Estaciones de Monitoreo", fontsize=13, fontweight='bold')
            
            # Mejorar grid
            ax.grid(alpha=0.3, axis='y', linestyle='--', linewidth=0.7)
            ax.set_axisbelow(True)
            
            # Rotar etiquetas del eje X para mejor legibilidad
            plt.xticks(rotation=30, ha='right', fontsize=11)
            ax.tick_params(axis='y', labelsize=11)
            
            # Añadir fondo sutil
            ax.set_facecolor('#f8f9fa')
            fig.patch.set_facecolor('white')
            
            # Añadir explicación en el gráfico (más corta para precipitaciones)
            if var['titulo'] == "Precipitaciones (mm)":
                explicacion_texto = "Comparación de precipitaciones entre estaciones"
            else:
                explicacion_texto = EXPLICACIONES.get(var['titulo'], '')[:120]
            
            ax.text(0.02, 0.98, explicacion_texto, transform=ax.transAxes, 
                   fontsize=9, va='top', ha='left',
                   bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='gray', 
                            pad=8, boxstyle='round,pad=0.3'))
            
            plt.tight_layout()
            
            # Guardar imagen con mejor calidad
            out_root = os.path.join(BASE_DIR, "graficos")
            if not os.path.exists(out_root):
                os.makedirs(out_root)
            save_name = os.path.join(out_root, f"comparativa_{var['titulo'].replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_').lower()}.png")
            plt.savefig(save_name, dpi=300, bbox_inches='tight', facecolor='white')
            print(f"Gráfico guardado en {save_name}")
            
            # Guardar reporte comparativo
            textos = [f"Análisis Comparativo: {var['titulo']}", "=" * (22 + len(var['titulo'])), ""]
            textos.append(EXPLICACIONES.get(var['titulo'], 'No hay explicación disponible.'))
            textos.append("")
            textos.append("="*80)
            textos.append("")
            
            for estacion_nombre, stats in todas_las_stats.items():
                textos.append(f"{estacion_nombre}")
                table = [[clave, f"{valor:.2f}"] for clave, valor in stats.items()]
                tabla_str = tabulate(table, headers=['Estadístico', 'Valor'], tablefmt='grid')
                textos.append(tabla_str)
                textos.append("")
            
            reporte = "\n".join(textos)
            print(reporte)
            
            ruta_txt = os.path.join(out_root, f"comparativa_{var['titulo'].replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_').lower()}.txt")
            with open(ruta_txt, 'w', encoding='utf-8') as f:
                f.write(reporte)
            print(f"Reporte comparativo guardado en {ruta_txt}")
            print("\n" + "="*60)
            print(f"📊 Gráfico: {var['titulo'].upper()}")
            print("👉 Cierra la ventana del gráfico para continuar con la siguiente variable")
            print("="*60 + "\n")
            
            plt.show(block=True)  # Mantiene el gráfico abierto hasta que lo cierres
        else:
            print(f"No se encontraron datos para {var['titulo']}")

    print("\n" + "#"*60)
    print(" ANÁLISIS GLOBAL COMPLETADO CON ÉXITO ")
    print("#"*60)