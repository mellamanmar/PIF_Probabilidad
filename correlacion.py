import os
import sys
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Forzar salida UTF-8 en consola Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# =====================================================
# BUSCAR AUTOMÁTICAMENTE TODOS LOS CSV
# =====================================================

ruta_actual = os.path.dirname(__file__)

archivos_csv = glob.glob(
    os.path.join(ruta_actual, "**", "*.csv"),
    recursive=True
)

if len(archivos_csv) == 0:
    print("No se encontraron archivos CSV")
    exit()

# =====================================================
# AGRUPAR CSV POR ESTACIÓN (CARPETA)
# =====================================================

estaciones_archivos = {}

for archivo in archivos_csv:
    nombre_estacion = os.path.basename(os.path.dirname(archivo))
    if nombre_estacion not in estaciones_archivos:
        estaciones_archivos[nombre_estacion] = []
    estaciones_archivos[nombre_estacion].append(archivo)

# =====================================================
# CREAR CARPETA DE RESULTADOS
# =====================================================

carpeta_resultados = os.path.join(ruta_actual, "correlaciones")
os.makedirs(carpeta_resultados, exist_ok=True)

# =====================================================
# PROCESAR CADA ESTACIÓN
# =====================================================

variables_posibles = ["PM10", "O3", "TMPR AIR 10CM", "HAire10", "VViento", "P"]

for estacion, archivos in estaciones_archivos.items():

    print(f"\n=== Procesando estación: {estacion} ===")

    # ==========================================
    # LEER CADA CSV Y HACER JOIN POR FECHA
    # Cada CSV tiene solo una variable con su
    # propia columna → unirlos por "Fecha inicial"
    # ==========================================

    df_merged = None

    for archivo in archivos:
        try:
            try:
                df = pd.read_csv(archivo, encoding="utf-8-sig")
            except UnicodeDecodeError:
                df = pd.read_csv(archivo, encoding="latin-1")
            except Exception as read_err:
                print(f"  No se pudo leer: {os.path.basename(archivo)} ({type(read_err).__name__})")
                continue

            # Identificar columna de variable (la que no es Estacion/Fecha)
            cols_meta = ["Estacion", "Fecha inicial", "Fecha final"]
            cols_var = [c for c in df.columns if c not in cols_meta and c in variables_posibles]

            if len(cols_var) == 0:
                print(f"  Sin variable reconocida en: {os.path.basename(archivo)}")
                continue

            # Convertir la variable a numérica
            for col in cols_var:
                df[col] = pd.to_numeric(
                    df[col].astype(str).str.replace(",", ".", regex=False).str.strip(),
                    errors="coerce"
                )

            # Seleccionar solo fecha + variable
            df_sub = df[["Fecha inicial"] + cols_var].copy()
            df_sub["Fecha inicial"] = pd.to_datetime(df_sub["Fecha inicial"], errors="coerce")

            # Agregar por fecha (promedio si hay duplicados)
            df_sub = df_sub.groupby("Fecha inicial", as_index=False).mean(numeric_only=True)

            print(f"  {os.path.basename(archivo)} -> variable(s): {cols_var}, filas: {len(df_sub)}")

            # Merge con el dataframe acumulado
            if df_merged is None:
                df_merged = df_sub
            else:
                df_merged = pd.merge(df_merged, df_sub, on="Fecha inicial", how="outer")

        except Exception as e:
            print(f"  Error procesando {os.path.basename(archivo)}: {type(e).__name__}")

    # ==========================================
    # VALIDAR QUE HAY DATOS
    # ==========================================

    if df_merged is None:
        print(f"  Sin datos para {estacion}")
        continue

    # Quitar columna de fecha
    df_corr = df_merged.drop(columns=["Fecha inicial"], errors="ignore")

    # Quedarse solo con variables posibles disponibles
    cols_disponibles = [c for c in variables_posibles if c in df_corr.columns]

    if len(cols_disponibles) < 2:
        print(f"  No hay suficientes variables en {estacion}")
        continue

    df_corr = df_corr[cols_disponibles]

    # ==========================================
    # DIAGNÓSTICO
    # ==========================================

    print(f"  Filas totales tras merge: {len(df_corr)}")
    print(f"  Filas completas (sin NaN): {df_corr.dropna().shape[0]}")
    print(f"  Nulos por columna:\n{df_corr.isnull().sum().to_string()}")

    # ==========================================
    # CALCULAR MATRIZ DE CORRELACIÓN
    # min_periods=10 → mínimo de pares válidos
    # ==========================================

    corr = df_corr.corr(numeric_only=True, min_periods=10)

    print("\n  Matriz de correlación:")
    print(corr.to_string())

    # ==========================================
    # CONFIGURAR FIGURA
    # ==========================================

    n_vars = len(corr.columns)
    fig_size = max(8, n_vars * 1.6)
    plt.figure(figsize=(fig_size, fig_size * 0.85))

    # ==========================================
    # CREAR HEATMAP — MAPA DE CALOR COMPLETO
    # ==========================================

    sns.heatmap(
        corr,
        annot=True,
        cmap="RdYlGn",
        vmin=-1,
        vmax=1,
        linewidths=0.8,
        linecolor="white",
        fmt=".2f",
        annot_kws={"size": 11, "weight": "bold"},
        square=True,
        cbar_kws={
            "shrink": 0.8,
            "label": "Coeficiente de Pearson"
        }
    )

    # ==========================================
    # TÍTULO Y ETIQUETAS
    # ==========================================

    plt.title(
        f"Mapa de Calor de Correlación — Estación {estacion}",
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    plt.xlabel("Variables", fontsize=12, labelpad=10)
    plt.ylabel("Variables", fontsize=12, labelpad=10)

    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(rotation=0, fontsize=10)

    plt.tight_layout()

    # ==========================================
    # GUARDAR IMAGEN
    # ==========================================

    nombre_archivo = estacion.replace(" ", "_")
    ruta_guardado = os.path.join(carpeta_resultados, f"{nombre_archivo}.png")

    plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"\n  Heatmap guardado en: {ruta_guardado}")

# =====================================================
# FINALIZAR
# =====================================================

print("\nProceso completado correctamente.")