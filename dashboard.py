import streamlit as st
import pandas as pd
import os

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------
st.set_page_config(
    page_title="Dashboard Calidad del Aire - Medellín",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos estéticos
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2c3e50; font-family: 'Inter', sans-serif; }
    h2, h3 { color: #34495e; font-family: 'Inter', sans-serif; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

st.title("🌫️ Dashboard de Calidad del Aire - Medellín")
st.markdown("**Análisis temporal de Ozono (O3) y PM10 frente a variables meteorológicas por estación.**")

@st.cache_data
def cargar_datos():
    carpeta = r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tablas procesadas"
    archivos = {
        "Almacen EPM": "Almacen EPM.csv",
        "Politecnico Jaime Isaza": "Politecnico Jaime Isaza.csv",
        "Tanques de la Ye": "Tanques_Ye.csv",
        "Universidad CES": "Universidad CES.csv",
        "UdeM": "UdeM.csv"
    }
    
    dfs = []
    for nombre, archivo in archivos.items():
        ruta = os.path.join(carpeta, archivo)
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            df['Fecha inicial'] = pd.to_datetime(df['Fecha inicial'], errors='coerce')
            df['Año'] = df['Fecha inicial'].dt.year
            df['Mes'] = df['Fecha inicial'].dt.month
            df['Día'] = df['Fecha inicial'].dt.day
            df['Estación'] = nombre
            
            # Identificar si tiene O3 o PM10
            if 'PM10' in df.columns:
                df['Contaminante'] = 'PM10'
                df['Valor Contaminante'] = df['PM10']
            elif 'O3' in df.columns:
                df['Contaminante'] = 'O3'
                df['Valor Contaminante'] = df['O3']
                
            dfs.append(df)
            
    df_total = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    return df_total

df_total = cargar_datos()

if df_total.empty:
    st.error("No se encontraron los datos procesados en la carpeta 'Tablas procesadas'. Ejecuta Tablas.py primero.")
    st.stop()

# -------------------------------
# SIDEBAR (FILTROS)
# -------------------------------
st.sidebar.header("🔎 Filtros de Tiempo y Estación")

estaciones_disp = sorted(df_total["Estación"].unique())
estacion_sel = st.sidebar.selectbox("Selecciona una estación", ["Todas"] + estaciones_disp)

años = sorted(df_total["Año"].dropna().unique().astype(int))
años_sel = st.sidebar.multiselect("📅 Selecciona años", años, default=años)

meses = sorted(df_total["Mes"].dropna().unique().astype(int))
meses_es = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
meses_sel = st.sidebar.multiselect("📅 Selecciona meses", meses, default=meses, format_func=lambda x: meses_es.get(x, x))

dias = sorted(df_total["Día"].dropna().unique().astype(int))
dias_sel = st.sidebar.multiselect("📅 Selecciona días", dias, default=dias)

# -------------------------------
# APLICAR FILTROS
# -------------------------------
df_filtrado = df_total[
    (df_total["Año"].isin(años_sel)) &
    (df_total["Mes"].isin(meses_sel)) &
    (df_total["Día"].isin(dias_sel))
]

if estacion_sel != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Estación"] == estacion_sel]

if df_filtrado.empty:
    st.warning("No hay datos disponibles para los filtros seleccionados.")
    st.stop()

# -------------------------------
# KPIs
# -------------------------------
st.subheader(f"📊 Indicadores Generales - {estacion_sel}")

col1, col2, col3, col4 = st.columns(4)
promedio_contaminante = df_filtrado["Valor Contaminante"].mean()
max_contaminante = df_filtrado["Valor Contaminante"].max()
promedio_temp = df_filtrado["TMPR AIR 10CM"].mean()
promedio_humedad = df_filtrado["HAire10"].mean()

tipo_cont = "PM10 / O3" if estacion_sel == "Todas" else df_filtrado["Contaminante"].iloc[0]

col1.metric(f"Promedio {tipo_cont}", f"{promedio_contaminante:.2f}")
col2.metric(f"Máximo {tipo_cont}", f"{max_contaminante:.2f}")
col3.metric("Temperatura Promedio", f"{promedio_temp:.2f} °C")
col4.metric("Humedad Promedio", f"{promedio_humedad:.2f} %")

# -------------------------------
# VISTAS TEMPORALES
# -------------------------------
st.markdown("---")
st.subheader("📈 Evolución en el tiempo: Contaminante vs Meteorología")

# Agrupar por fecha y contaminante para separar PM10 y O3
df_time_cont = df_filtrado.groupby(["Fecha inicial", "Contaminante"], as_index=False).agg({
    "Valor Contaminante": "mean"
}).sort_values("Fecha inicial")

df_time_cont_pivot = df_time_cont.pivot(index="Fecha inicial", columns="Contaminante", values="Valor Contaminante").reset_index()
df_time_cont_pivot.rename(columns={"Fecha inicial": "Fecha"}, inplace=True)

# Agrupar variables meteorológicas por fecha
df_time_meteo = df_filtrado.groupby("Fecha inicial", as_index=False).agg({
    "TMPR AIR 10CM": "mean",
    "HAire10": "mean",
    "P": "mean",
    "VViento": "mean"
}).sort_values("Fecha inicial")

df_time_meteo = df_time_meteo.rename(columns={
    "Fecha inicial": "Fecha",
    "TMPR AIR 10CM": "Temperatura",
    "HAire10": "Humedad",
    "P": "Precipitaciones",
    "VViento": "Velocidad Viento"
})

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Contaminantes", "Temperatura", "Humedad", "Precipitaciones y Viento", "Correlación Temporal"])

with tab1:
    st.markdown("**Evolución de Contaminantes (PM10 y O3)**")
    y_cols = [c for c in ["PM10", "O3"] if c in df_time_cont_pivot.columns and not df_time_cont_pivot[c].isnull().all()]
    colores_map = {"PM10": "#8e44ad", "O3": "#27ae60"}
    y_colors = [colores_map[c] for c in y_cols]
    
    if y_cols:
        st.line_chart(df_time_cont_pivot, x="Fecha", y=y_cols, color=y_colors)
    else:
        st.info("No hay datos de contaminantes en la selección actual.")

with tab2:
    st.markdown("**Evolución de la Temperatura (°C)**")
    st.line_chart(df_time_meteo, x="Fecha", y="Temperatura", color="#f39c12")

with tab3:
    st.markdown("**Evolución de la Humedad (%)**")
    st.line_chart(df_time_meteo, x="Fecha", y="Humedad", color="#3498db")

with tab4:
    st.markdown("**Evolución de Precipitaciones y Velocidad del Viento**")
    st.line_chart(df_time_meteo, x="Fecha", y=["Precipitaciones", "Velocidad Viento"])

with tab5:
    st.markdown("**Correlación Temporal: Contaminante vs Variable Meteorológica**")
    
    var_meteo_sel = st.selectbox("Selecciona la variable meteorológica a correlacionar", ["Temperatura", "Humedad", "Precipitaciones", "Velocidad Viento"])
    
    if estacion_sel == "Todas":
        est_corr_sel = st.selectbox("Selecciona una estación específica para el análisis de correlación", estaciones_disp)
        df_corr = df_filtrado[df_filtrado["Estación"] == est_corr_sel].copy()
    else:
        est_corr_sel = estacion_sel
        df_corr = df_filtrado.copy()
        
    if df_corr.empty:
        st.warning("No hay suficientes datos para la estación seleccionada.")
    else:
        df_corr_time = df_corr.groupby("Fecha inicial", as_index=False).mean(numeric_only=True).sort_values("Fecha inicial")
        
        map_vars = {
            "Temperatura": "TMPR AIR 10CM",
            "Humedad": "HAire10",
            "Precipitaciones": "P",
            "Velocidad Viento": "VViento"
        }
        col_meteo = map_vars[var_meteo_sel]
        contam = df_corr["Contaminante"].iloc[0]
        
        # Normalización Min-Max para comparar escalas (0 a 1)
        min_c, max_c = df_corr_time["Valor Contaminante"].min(), df_corr_time["Valor Contaminante"].max()
        min_m, max_m = df_corr_time[col_meteo].min(), df_corr_time[col_meteo].max()
        
        df_norm = pd.DataFrame()
        df_norm["Fecha"] = df_corr_time["Fecha inicial"]
        df_norm[f"{contam} (Normalizado)"] = (df_corr_time["Valor Contaminante"] - min_c) / (max_c - min_c) if max_c != min_c else 0
        df_norm[f"{var_meteo_sel} (Normalizado)"] = (df_corr_time[col_meteo] - min_m) / (max_m - min_m) if max_m != min_m else 0
        df_norm = df_norm.set_index("Fecha")
        
        st.line_chart(df_norm)
        
        corr_val = df_corr_time["Valor Contaminante"].corr(df_corr_time[col_meteo])
        st.info(f"El coeficiente de correlación de Pearson entre **{contam}** y **{var_meteo_sel}** en la estación **{est_corr_sel}** es: **{corr_val:.2f}**")

# -------------------------------
# COMPARACIÓN ENTRE ESTACIONES
# -------------------------------
if estacion_sel == "Todas":
    st.markdown("---")
    st.subheader("🏭 Comparación Promedio por Estación")
    df_est = df_filtrado.groupby(["Estación", "Contaminante"], as_index=False)["Valor Contaminante"].mean()
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("**PM10 por Estación**")
        df_pm10 = df_est[df_est["Contaminante"]=="PM10"]
        if not df_pm10.empty:
            st.bar_chart(df_pm10.set_index("Estación")["Valor Contaminante"], color="#8e44ad")
        else:
            st.info("No hay datos de PM10 en esta selección.")
            
    with col_e2:
        st.markdown("**O3 por Estación**")
        df_o3 = df_est[df_est["Contaminante"]=="O3"]
        if not df_o3.empty:
            st.bar_chart(df_o3.set_index("Estación")["Valor Contaminante"], color="#27ae60")
        else:
            st.info("No hay datos de O3 en esta selección.")


# -------------------------------
# EVENTOS
# -------------------------------
st.markdown("---")
st.subheader("⚠️ Análisis de Eventos (Superación del umbral)")
eventos_totales = df_filtrado["evento"].sum()
dias_totales = len(df_filtrado)
porcentaje_eventos = (eventos_totales / dias_totales) * 100 if dias_totales > 0 else 0

st.info(f"Se registraron **{eventos_totales} eventos** de alerta en el periodo seleccionado ({porcentaje_eventos:.1f}% de los registros diarios filtrados).")

# -------------------------------
# TABLA DE DATOS
# -------------------------------
st.markdown("---")
st.subheader("📄 Datos Filtrados")
columnas_mostrar = ["Estación", "Fecha inicial", "Contaminante", "Valor Contaminante", "TMPR AIR 10CM", "HAire10", "P", "VViento", "evento"]
st.dataframe(df_filtrado[columnas_mostrar].sort_values("Fecha inicial").head(200), use_container_width=True)