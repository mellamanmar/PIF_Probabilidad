#!/usr/bin/env python3
"""
Script para generar gráfico simplificado de precipitaciones
Ejecutar: python grafico_precipitaciones_simple.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generar_grafico_precipitaciones_simple():
    """Genera gráfico de precipitaciones con etiquetas mínimas"""

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    estaciones = [
        'Universidad de Medellin',
        'Universidad CES',
        'Politecnico Jaime Isaza',
        'Tanques de la Ye',
        'Almacen general de EPM'
    ]

    datos_por_estacion = []
    etiquetas_estaciones = []

    print("Procesando datos de precipitaciones...")

    for estacion in estaciones:
        folder_path = os.path.join(BASE_DIR, estacion)
        ruta = None

        # Buscar archivo
        posibles = [
            f'reporte_sisaire Precipitaciones {estacion}.csv',
            f'Precipitaciones {estacion}.csv'
        ]

        for p in posibles:
            ruta_completa = os.path.join(folder_path, p)
            if os.path.exists(ruta_completa):
                ruta = ruta_completa
                break

        if ruta:
            try:
                df = pd.read_csv(ruta, sep=',', engine='python')
                datos = df['P'].astype(float).dropna()
                datos_por_estacion.append(datos)
                etiquetas_estaciones.append(estacion)
                print(f'✓ {estacion}: {len(datos)} datos, media={datos.mean():.1f}')
            except Exception as e:
                print(f'✗ Error con {estacion}: {e}')
        else:
            print(f'✗ No se encontró archivo para {estacion}')

    if not datos_por_estacion:
        print("No se encontraron datos de precipitaciones")
        return

    # Crear boxplot simplificado
    fig, ax = plt.subplots(figsize=(14, 8))
    bp = ax.boxplot(datos_por_estacion, tick_labels=etiquetas_estaciones, patch_artist=True,
                   boxprops=dict(facecolor='#87CEEB', color='black', linewidth=2),
                   medianprops=dict(color='red', linewidth=3),
                   whiskerprops=dict(color='black', linewidth=2),
                   capprops=dict(color='black', linewidth=2),
                   flierprops=dict(marker='o', color='red', markersize=6, alpha=0.7))

    # Añadir solo etiquetas simples de media
    for i, datos in enumerate(datos_por_estacion):
        media = np.mean(datos)
        q1 = np.percentile(datos, 25)
        q3 = np.percentile(datos, 75)

        # Etiqueta simple solo con media
        label_y = q3 + (q3 - q1) * 0.15 if q3 != q1 else media * 1.02
        ax.text(i+1, label_y, f'μ={media:.1f}', ha='center', va='bottom',
               fontsize=10, fontweight='bold', color='darkblue',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

    # Configurar gráfico
    ax.set_title('Comparativa: Precipitaciones (mm) por Estación', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Precipitaciones (mm)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Estaciones de Monitoreo', fontsize=13, fontweight='bold')

    # Mejorar visualización
    ax.grid(alpha=0.3, axis='y', linestyle='--', linewidth=0.7)
    ax.set_axisbelow(True)
    plt.xticks(rotation=30, ha='right', fontsize=11)
    ax.tick_params(axis='y', labelsize=11)
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')

    # Explicación corta
    ax.text(0.02, 0.98, 'Comparación de precipitaciones entre estaciones', transform=ax.transAxes,
           fontsize=10, va='top', ha='left',
           bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='gray', pad=8, boxstyle='round,pad=0.3'))

    plt.tight_layout()

    # Crear directorio si no existe
    out_dir = os.path.join(BASE_DIR, 'graficos')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Guardar gráfico
    save_path = os.path.join(out_dir, 'comparativa_precipitaciones_mm_simplificado.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"✓ Gráfico simplificado guardado en: {save_path}")
    print("Este gráfico tiene solo las medias mostradas para mejor visibilidad del boxplot")

if __name__ == "__main__":
    generar_grafico_precipitaciones_simple()