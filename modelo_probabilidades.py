import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


# 1. CARGAR TODAS LAS ESTACIONES

carpeta = r"C:\Users\marim\OneDrive\Documentos\Universidad\Probabilidad\PIF Probabilidad\Tablas procesadas"

estaciones = {
    file.replace(".csv",""): pd.read_csv(
        os.path.join(carpeta, file),
        index_col=0,
        parse_dates=True
    )
    for file in os.listdir(carpeta) if file.endswith(".csv")
}

print("Estaciones cargadas:", list(estaciones.keys()))

variables_clima = ['HAire10', 'P', 'TMPR AIR 10CM', 'VViento']


# 3. FUNCIÓN PARA INTERPRETAR COEFICIENTES

def interpretar_coeficientes(modelo, variables):
    
    coeficientes = modelo.coef_[0]
    resultados = []

    for var, beta in zip(variables, coeficientes):
        odds_ratio = np.exp(beta)
        cambio = (odds_ratio - 1) * 100

        resultados.append({
            "Variable": var,
            "Coef": round(beta, 4),
            "Odds Ratio": round(odds_ratio, 4),
            "% Cambio": round(cambio, 2)
        })

    return pd.DataFrame(resultados)


# 4. ENTRENAR MODELO POR ESTACIÓN

resultados_modelo = {}

for nombre, df in estaciones.items():

    print(f"\n📍 Estación: {nombre}")

    # Verificación básica
    if 'evento' not in df.columns:
        print("❌ No tiene variable 'evento'")
        continue

    if df.shape[0] == 0:
        print("❌ DataFrame vacío")
        continue

    # Variables
    X = df[variables_clima]
    y = df['evento']

    # División temporal
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.3
    )

    # Escalado
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Modelo
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)

    # Evaluación
    accuracy = modelo.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.3f}")

    # Probabilidades
    prob_evento = modelo.predict_proba(X_test)[:, 1]

    # DataFrame de resultados
    df_resultados = pd.DataFrame({
        "evento_real": y_test.values,
        "prob_evento": prob_evento,
        "prediccion": modelo.predict(X_test)
    }, index=y_test.index)

    print(df_resultados.head())

    # Interpretación
    interpretacion = interpretar_coeficientes(modelo, variables_clima)
    print("\nInterpretación:")
    print(interpretacion)

    # Guardar resultados
    resultados_modelo[nombre] = {
        "modelo": modelo,
        "accuracy": accuracy,
        "interpretacion": interpretacion,
        "resultados": df_resultados
    }

# 5. GUARDAR RESULTADOS

carpeta_resultados = os.path.join(carpeta, "Resultados modelo")
os.makedirs(carpeta_resultados, exist_ok=True)

for nombre, data in resultados_modelo.items():
    data["resultados"].to_csv(os.path.join(carpeta_resultados, f"{nombre}_resultados.csv"))
    data["interpretacion"].to_csv(os.path.join(carpeta_resultados, f"{nombre}_coeficientes.csv"))

print("\n✅ Modelos entrenados y resultados guardados")