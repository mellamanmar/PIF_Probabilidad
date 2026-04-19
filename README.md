# PIF_Probabilidad - Análisis de Calidad del Aire Medellín

Proyecto de análisis estadístico y probabilístico de datos de calidad del aire recolectados en 5 estaciones de monitoreo de Medellín.

## 📊 Estaciones de Monitoreo

1. **Universidad de Medellín**
2. **Universidad CES**
3. **Politécnico Jaime Isaza**
4. **Tanques de la Ye**
5. **Almacén General de EPM**

---

## 📈 Variables Monitoreadas

### 1. **Humedad Relativa (%)**
**Rango típico:** 30-100%  
**Factores a comparar entre estaciones:**
- **Media**: Indica el promedio de humedad en cada ubicación
- **Mediana**: Valor típico sin influencia de extremos
- **Moda**: Valor que se repite más frecuentemente
- **Desviación Estándar**: Variabilidad - mayor valor = cambios más abruptos
- **Rango IQR**: Concentración del 50% de datos
- **Asimetría**: Positiva = picos de humedad alta

---

### 2. **Ozono (O₃)**
**Rango típico:** 0-100 ppb  
**Factores a comparar entre estaciones:**
- **Media**: Concentración promedio de contaminación
- **Moda**: Valor que se repite más frecuentemente
- **Máximo**: Picos de contaminación más críticos
- **Curtosis**: Valores > 3 indican colas pesadas (eventos extremos frecuentes)

---

### 3. **PM10 (Partículas Suspendidas)**
**Rango típico:** 0-250 µg/m³  
**Factores a comparar entre estaciones:**
- **Media**: Exposición promedio a partículas
- **Moda**: Valor que se repite más frecuentemente
- **Q3 (75%)**: Umbrales superiores de calidad del aire
- **Varianza**: Consistencia de la contaminación
- **Mínimo vs Máximo**: Amplitud de fluctuaciones diarias

---

### 4. **Precipitaciones (mm)**
**Rango típico:** 0-50+ mm/día  
**Factores a comparar entre estaciones:**
- **Media**: Promedio de lluvia
- **Moda**: Valor que se repite más frecuentemente
- **Mediana**: Lluvia típica (mejor para datos sesgados)
- **Asimetría**: Positiva alta = lluvias intensas puntuales
- **Q1-Q3**: Rango de lluvia normal

---

### 5. **Temperatura (°C)**
**Rango típico:** 10-35°C  
**Factores a comparar entre estaciones:**
- **Media**: Temperatura promedio
- **Moda**: Valor que se repite más frecuentemente
- **Rango (Max-Min)**: Amplitud térmica
- **Desviación Estándar**: Variabilidad de temperatura

---

### 6. **Velocidad del Viento (m/s)**
**Rango típico:** 0-20 m/s  
**Factores a comparar entre estaciones:**
- **Media**: Velocidad promedio
- **Moda**: Valor que se repite más frecuentemente
- **Mediana**: Velocidad típica
- **Q3**: Vientos más fuertes del 25% de los datos
- **Curtosis**: Colas pesadas = ráfagas extremas frecuentes

---

## 🔍 Guía de Lectura de Gráficos

Cada gráfico boxplot muestra para cada estación:

```
         *  ← Valores atípicos (outliers)
    ┌────┐
    │    │  ← Q3 (75%) - Cuartil superior
    ├────┤  ← MEDIANA (línea roja)
    │    │  ← Q1 (25%) - Cuartil inferior
    └────┘
      ⬤ μ  ← MEDIA (valor mostrado con etiqueta)
```

- **Caja** (IQR): 50% de los datos
- **Línea roja** (Mediana): Valor central
- **Etiqueta μ**: Media
- **Texto numérico adicional**: muestra Media, Mediana, Moda y Desviación Estándar directamente en el gráfico
- **Moda**: valor más repetido en la muestra, útil para comparar tendencias comunes entre estaciones
- **Puntos rojos**: Datos atípicos

---

## 📊 Estadísticos Comparables

| Estadístico | Significado | Comparación |
|---|---|---|
| **Media (μ)** | Promedio | Estación con media MÁS ALTA = condiciones MÁS EXTREMAS |
| **Mediana** | Valor central | Diferencia con media = presencia de datos extremos |
| **Desv. Est. (σ)** | Variabilidad | Mayor σ = condiciones MÁS VARIABLES |
| **Rango (Max-Min)** | Amplitud | Mayor rango = fluctuaciones más extremas |
| **IQR** | Concentración central | Mayor IQR = datos MÁS DISPERSOS |
| **Asimetría** | Sesgos en datos | Positiva = extremos altos; Negativa = extremos bajos |
| **Curtosis** | Colas pesadas | > 3 = picos extremos más frecuentes |

---

## 🎯 Cómo Usar Este Análisis

1. **Ejecutar análisis:**
   ```bash
   python Analisis.py
   ```

2. **Para gráfico de precipitaciones simplificado:**
   ```bash
   python grafico_precipitaciones_simple.py
   ```

2. **Generados:**
   - Gráficos en `graficos/` con nombres `comparativa_*.png`
   - Reportes comparativos en `graficos/comparativa_*.txt`
   - Reportes por estación en `graficos/resumen_*.txt`

3. **Interpretación:**
   - Compara números (μ, Mediana) entre estaciones en los gráficos
   - Revisa reportes .txt para estadísticos completos
   - Identifica patrones: ¿Qué estación tiene mejor/peor calidad?
   - Para precipitaciones: usa `comparativa_precipitaciones_mm_simplificado.png` si el texto interfiere con la visualización

---

## 📁 Estructura de Datos

```
├── Analisis.py              # Script principal
├── grafico_precipitaciones_simple.py  # Gráfico simplificado de precipitaciones
├── BD.py                    # Procesamiento de datos
├── README.md                # Este archivo
├── graficos/                # Gráficos y reportes generados
│   ├── comparativa_*.png    # Gráficos por variable
│   ├── comparativa_*.txt    # Reportes comparativos
│   └── resumen_*.txt        # Reportes por estación
└── [Estaciones]/            # Datos CSV por ubicación
    ├── reporte_sisaire *.csv
    └── ...
```
