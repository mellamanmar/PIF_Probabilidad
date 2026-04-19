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

**Interpretación:** Estaciones con media más alta = ambientes más húmedos (posible niebla/condensación)

---

### 2. **Ozono (O₃)**
**Rango típico:** 0-100 ppb  
**Factores a comparar entre estaciones:**
- **Media**: Concentración promedio de contaminación
- **Moda**: Valor que se repite más frecuentemente
- **Máximo**: Picos de contaminación más críticos
- **Curtosis**: Valores > 3 indican colas pesadas (eventos extremos frecuentes)

**Interpretación:** Mayor media = mayor contaminación; Curtosis alta = eventos extremos más frecuentes

---

### 3. **PM10 (Partículas Suspendidas)**
**Rango típico:** 0-250 µg/m³  
**Factores a comparar entre estaciones:**
- **Media**: Exposición promedio a partículas
- **Moda**: Valor que se repite más frecuentemente
- **Q3 (75%)**: Umbrales superiores de calidad del aire
- **Varianza**: Consistencia de la contaminación
- **Mínimo vs Máximo**: Amplitud de fluctuaciones diarias

**Interpretación:** Media elevada = zona con mayor contaminación; Gran rango = días limpios vs. sucios alternados

---

### 4. **Precipitaciones (mm)**
**Rango típico:** 0-50+ mm/día  
**Factores a comparar entre estaciones:**
- **Media**: Promedio de lluvia
- **Moda**: Valor que se repite más frecuentemente
- **Mediana**: Lluvia típica (mejor para datos sesgados)
- **Asimetría**: Positiva alta = lluvias intensas puntuales
- **Q1-Q3**: Rango de lluvia normal

**Interpretación:** Media vs Mediana muy diferentes = presencia de lluvias intensas puntuales

---

### 5. **Temperatura (°C)**
**Rango típico:** 10-35°C  
**Factores a comparar entre estaciones:**
- **Media**: Temperatura promedio
- **Moda**: Valor que se repite más frecuentemente
- **Rango (Max-Min)**: Amplitud térmica
- **Desviación Estándar**: Variabilidad de temperatura

**Interpretación:** Mayor desviación estándar = zona más variable/montañosa; Menor rango = clima más estable

---

### 6. **Velocidad del Viento (m/s)**
**Rango típico:** 0-20 m/s  
**Factores a comparar entre estaciones:**
- **Media**: Velocidad promedio
- **Moda**: Valor que se repite más frecuentemente
- **Mediana**: Velocidad típica
- **Q3**: Vientos más fuertes del 25% de los datos
- **Curtosis**: Colas pesadas = ráfagas extremas frecuentes

**Interpretación:** Media alta = dispersión mejor de contaminantes; Media baja = acumulación de contaminantes

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

## 📈 Análisis de Gráficos Generados

### 🔍 Interpretación de Boxplots Comparativos

Cada gráfico muestra la distribución de una variable ambiental en las 5 estaciones de Medellín. Los números clave aparecen directamente en cada caja:

#### **Patrones a Identificar:**

**1. Diferencias en Niveles Promedio (Media/Moda)**
- **Humedad Relativa**: Estaciones con μ > 80% = zonas muy húmedas (posible niebla frecuente)
- **Ozono**: μ > 50 ppb = contaminación atmosférica significativa
- **PM10**: μ > 50 µg/m³ = calidad del aire deteriorada
- **Temperatura**: Diferencias > 2°C = microclimas locales
- **Precipitaciones**: μ > 5 mm/día = zonas más lluviosas
- **Viento**: μ > 2 m/s = buena dispersión de contaminantes

**2. Variabilidad (Desviación Estándar σ)**
- **σ alto**: Condiciones muy variables (cambios abruptos)
- **σ bajo**: Condiciones estables y predecibles
- Ejemplo: Temperatura con σ > 3°C = zona montañosa o expuesta

**3. Valores Extremos (Outliers)**
- Puntos rojos = mediciones atípicas
- Muchos outliers = eventos extremos frecuentes
- Ejemplo: Ozono con outliers altos = episodios de smog

**4. Asimetría en la Distribución**
- Caja desplazada hacia arriba = valores altos más frecuentes
- Caja desplazada hacia abajo = valores bajos predominantes
- Ejemplo: Precipitaciones asimétricas positivas = lluvias intensas puntuales

#### **Comparaciones Entre Estaciones:**

**Zonas Urbanas vs Rurales:**
- **PM10 y Ozono más altos** en zonas urbanas (contaminación vehicular)
- **Humedad más variable** en zonas con vegetación
- **Temperatura más estable** en centros urbanos

**Influencia Geográfica:**
- **Viento más fuerte** en zonas elevadas o abiertas
- **Temperatura más baja** en universidades de altura
- **Precipitaciones más altas** en zonas con relieve

**Patrones Temporales:**
- **Moda similar** entre estaciones = influencia climática regional
- **Moda diferente** = microclimas locales
- **Rango amplio** = variabilidad estacional pronunciada

#### **Ejemplos de Interpretación:**

**Si PM10 es alto en una estación:**
- Compara con velocidad del viento (menor viento = acumulación)
- Revisa humedad (alta humedad = partículas más pesadas)
- Identifica si es contaminación local o regional

**Si temperatura varía mucho:**
- Posible zona montañosa o expuesta al sol
- Compara con humedad (temperaturas variables suelen correlacionar con humedad variable)

**Si ozono es alto:**
- Busca correlación con radiación solar
- Compara con viento (baja dispersión = acumulación)

**Si precipitaciones son irregulares:**
- Asimetría positiva = lluvias intensas puntuales
- Compara con humedad (lluvias irregulares afectan humedad)

#### **Recomendaciones de Análisis:**

1. **Empieza por la media**: Identifica qué estación tiene los valores más extremos
2. **Compara modas**: Valores similares = influencia regional; diferentes = factores locales
3. **Analiza variabilidad**: σ alta = zona inestable; σ baja = zona predecible
4. **Busca correlaciones**: Variables relacionadas (viento-PM10, temperatura-humedad)
5. **Identifica outliers**: Pueden indicar eventos especiales o errores de medición

#### **Uso Práctico de los Gráficos:**

**Archivos generados:**
- `comparativa_humedad_relativa_%.png` - Comparación de humedad entre estaciones
- `comparativa_ozono_o3.png` - Niveles de ozono contaminante
- `comparativa_pm10.png` - Partículas suspendidas
- `comparativa_precipitaciones_mm.png` - Distribución de lluvias (con etiquetas detalladas)
- `comparativa_precipitaciones_mm_simplificado.png` - Distribución de lluvias (versión limpia, solo medias)
- `comparativa_temperatura_°c.png` - Variaciones térmicas
- `comparativa_velocidad_del_viento_m_s.png` - Patrones de viento

**Lectura rápida:**
- **Etiqueta blanca**: Media (μ), Mediana (Med), Moda, Desviación (σ)
- **Etiqueta amarilla**: Mediana adicional para referencia
- **Caja azul**: Rango intercuartílico (50% central de datos)
- **Línea roja**: Mediana exacta
- **Bigotes**: Rango típico (sin outliers)
- **Puntos rojos**: Valores atípicos/extremos
- **Versión simplificada**: Para precipitaciones, disponible sin texto superpuesto para mejor visibilidad del boxplot

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

## 📌 Patrones a Buscar

### Si PM10 es alto en cierta estación:
- Busca correlación con vientos bajos (Wind)
- Compara con Humedad (PM10 cae con lluvia)

### Si Temperatura varía mucho:
- Estación en zona montañosa
- Mayor influencia de cambios estacionales

### Si Ozono es alto:
- Correlacionar con radiación solar
- Buscar patrón de contaminación urbana

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

---

**Última actualización:** 2026-04-18