# 🌫️ PIF Probabilidad — Análisis de Calidad del Aire en Medellín

Herramienta de análisis estadístico de datos de calidad del aire y variables meteorológicas recolectados en 5 estaciones de monitoreo de Medellín.

---

## 📋 Requisitos previos

Antes de usar cualquier script, instala las dependencias necesarias:

```bash
pip install pandas numpy matplotlib seaborn streamlit tabulate
```

---

## 📁 Estructura del Proyecto

```
PIF_Probabilidad 1/
│
├── 📂 Almacen general de EPM/       ← Datos CSV de esta estación
├── 📂 Politecnico Jaime Isaza/      ← Datos CSV de esta estación
├── 📂 Tanques de la Ye/             ← Datos CSV de esta estación
├── 📂 Universidad CES/              ← Datos CSV de esta estación
├── 📂 Universidad de Medellin/      ← Datos CSV de esta estación
│
├── 📂 graficos/                     ← Gráficos generados (se crea automáticamente)
├── 📂 correlaciones/                ← Mapas de calor generados (se crea automáticamente)
│
├── Analisis_boxplot.py              ← Boxplots comparativos entre estaciones
├── Analisis_descriptivo.py          ← Histogramas y estadísticos por estación
├── Analisis_grafico.py              ← Versión alternativa de histogramas
├── correlacion.py                   ← Mapas de calor de correlación de Pearson
├── dashboard.py                     ← Dashboard interactivo (Streamlit)
├── grafico_precipitaciones_simple.py← Gráfico simplificado de precipitaciones
└── Tablas.py                        ← Preprocesamiento para el dashboard
```

---

## 🗂️ Formato de los datos CSV

Cada carpeta de estación debe contener **un archivo CSV por variable**, con el siguiente formato de nombre:

```
reporte_sisaire [Variable] [Sufijo estación].csv
```

**Ejemplo:**
```
reporte_sisaire PM10 Almacen EPM.csv
reporte_sisaire Humedad relativa del aire Almacen EPM.csv
reporte_sisaire Temperatura Almacen EPM.csv
```

> ⚠️ **Importante:** Todos los archivos de la misma estación deben cubrir el **mismo rango de fechas**. Si una variable tiene fechas distintas, su correlación con las demás saldrá vacía (`NaN`).

**Variables soportadas y su nombre en el CSV:**

| Variable | Nombre columna en CSV |
|---|---|
| PM10 | `PM10` |
| Ozono | `O3` |
| Temperatura | `TMPR AIR 10CM` |
| Humedad relativa | `HAire10` |
| Velocidad del viento | `VViento` |
| Precipitaciones | `P` |

---

## 🚀 Cómo usar cada script

### 1️⃣ `Analisis_boxplot.py` — Boxplots comparativos entre estaciones

Genera un boxplot por variable comparando las 5 estaciones simultáneamente.

```bash
python Analisis_boxplot.py
```

**Qué hace:**
- Crea un gráfico por cada variable (PM10, O3, Temperatura, Humedad, Precipitaciones, Viento)
- Cada gráfico muestra las 5 estaciones lado a lado
- Incluye en el gráfico: Media (μ), Mediana, Moda y Desviación estándar
- Guarda los gráficos en `graficos/comparativa_[variable].png`
- Genera reportes de texto en `graficos/comparativa_[variable].txt`

**Resultado esperado:** Una ventana con el gráfico se abre. Ciérrala para continuar con la siguiente variable.

---

### 2️⃣ `Analisis_descriptivo.py` — Histogramas por estación

Genera un panel de histogramas para **cada estación** con todas sus variables.

```bash
python Analisis_descriptivo.py
```

**Qué hace:**
- Procesa cada estación de forma individual
- Muestra hasta 6 histogramas en una sola figura (una por variable)
- Marca la media (línea roja) y la mediana (línea verde) en cada histograma
- Guarda las figuras en `graficos/resumen_[estacion].png`

**Resultado esperado:** Una ventana por estación. Ciérrala para pasar a la siguiente.

---

### 3️⃣ `correlacion.py` — Mapas de calor de correlación de Pearson

Calcula y visualiza la correlación entre todas las variables para cada estación.

```bash
python correlacion.py
```

**Qué hace:**
- Lee automáticamente todos los CSV de las subcarpetas
- Hace un *join* por fecha para alinear las variables correctamente
- Calcula la matriz de correlación de Pearson (valores entre -1 y 1)
- Genera un mapa de calor completo para cada estación
- Guarda los resultados en `correlaciones/[Estacion].png`

**Interpretación del mapa de calor:**
- 🟢 **Verde (+1):** Correlación positiva fuerte (suben juntas)
- 🔴 **Rojo (-1):** Correlación negativa fuerte (cuando una sube, la otra baja)
- 🟡 **Amarillo (0):** Sin correlación

**Diagnóstico si salen celdas vacías (`NaN`):** Las variables de esa estación tienen rangos de fechas distintos en sus archivos CSV. Verifica que todos los archivos de la carpeta cubran el mismo período.

---

### 4️⃣ `dashboard.py` — Dashboard interactivo web

Interfaz visual e interactiva para explorar los datos. Requiere haber ejecutado `Tablas.py` primero.

**Paso 1:** Ejecuta el preprocesamiento (solo la primera vez o cuando cambien los datos):
```bash
python Tablas.py
```
Esto genera los archivos procesados en la carpeta `Tablas procesadas/`.

**Paso 2:** Lanza el dashboard:
```bash
streamlit run dashboard.py
```

Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

**Qué puedes hacer en el dashboard:**
- **Filtros** (barra lateral): Filtra por estación, año, mes y día
- **Pestaña Contaminantes:** Evolución temporal de PM10 y O3
- **Pestaña Temperatura:** Serie temporal de temperatura
- **Pestaña Humedad:** Serie temporal de humedad relativa
- **Pestaña Precipitaciones y Viento:** Ambas variables juntas
- **Pestaña Correlación Temporal:** Selecciona una variable meteorológica y ve su evolución normalizada junto al contaminante, con el coeficiente de Pearson calculado automáticamente
- **Comparación entre estaciones:** Barras comparativas de PM10 y O3 (visible cuando se selecciona "Todas" las estaciones)
- **Eventos de alerta:** Número y porcentaje de días que superaron el umbral de contaminación
- **Tabla de datos:** Los datos crudos filtrados

---

### 5️⃣ `grafico_precipitaciones_simple.py` — Gráfico simplificado de precipitaciones

Versión alternativa del gráfico de precipitaciones sin anotaciones de texto superpuestas.

```bash
python grafico_precipitaciones_simple.py
```

Útil cuando el gráfico de `Analisis_boxplot.py` para precipitaciones se ve sobrecargado de texto.

---

## 🔍 Flujo de trabajo recomendado

```
1. Verificar que los CSV están en sus carpetas con fechas coincidentes
         ↓
2. python Analisis_boxplot.py     → Comparar variables entre estaciones
         ↓
3. python Analisis_descriptivo.py → Ver distribución por estación
         ↓
4. python correlacion.py          → Analizar relaciones entre variables
         ↓
5. python Tablas.py               → Preparar datos para el dashboard
         ↓
6. streamlit run dashboard.py     → Explorar interactivamente
```

---

## 🏭 Estaciones de monitoreo

| Estación | Contaminante principal |
|---|---|
| Almacén General de EPM | PM10 |
| Politécnico Jaime Isaza | PM10 |
| Tanques de la Ye | O3 (Ozono) |
| Universidad CES | O3 (Ozono) |
| Universidad de Medellín | O3 (Ozono) |

---

## ❓ Problemas comunes

| Problema | Causa probable | Solución |
|---|---|---|
| Celdas NaN en mapa de calor | Fechas diferentes entre variables de la misma estación | Volver a descargar el CSV con el mismo rango de fechas |
| `No se encontraron archivos CSV` | El script no encuentra los datos | Verifica que los CSV estén en subcarpetas dentro del directorio del proyecto |
| El dashboard dice que faltan datos | No se ejecutó `Tablas.py` | Ejecuta `python Tablas.py` antes de lanzar el dashboard |
| Gráfico se abre pero no avanza | Hay que cerrar manualmente cada ventana | Cierra la ventana del gráfico para que el script continúe |
