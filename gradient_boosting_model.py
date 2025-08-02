
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Carregar a base de dados
df = pd.read_csv("../data/call_center_data.csv")

# Pré-processamento
# Converter DATA para datetime
df["DATA"] = pd.to_datetime(df["DATA"])

# Extrair features de data
df["ANO"] = df["DATA"].dt.year
df["MES"] = df["DATA"].dt.month
df["DIA_DO_MES"] = df["DATA"].dt.day
df["DIA_DA_SEMANA"] = df["DATA"].dt.dayofweek

# Codificar variáveis categóricas
le_login = LabelEncoder()
df["LOGIN_ENCODED"] = le_login.fit_transform(df["LOGIN"])

le_nome_indicado = LabelEncoder()
df["NOME_INDICADO_ENCODED"] = le_nome_indicado.fit_transform(df["NOME_INDICADO"])

le_grupo_agente = LabelEncoder()
df["GRUPO_AGENTE_ENCODED"] = le_grupo_agente.fit_transform(df["GRUPO_AGENTE"])

# Selecionar features e targets
features = ["ANO", "MES", "DIA_DO_MES", "DIA_DA_SEMANA", "LOGIN_ENCODED", "NOME_INDICADO_ENCODED", "GRUPO_AGENTE_ENCODED"]
targets = ["NUMERADOR", "DENOMINADOR"]

X = df[features]
y_numerador = df["NUMERADOR"]
y_denominador = df["DENOMINADOR"]

# Dividir os dados em treino e teste
X_train, X_test, y_numerador_train, y_numerador_test = train_test_split(X, y_numerador, test_size=0.2, random_state=42)
_, _, y_denominador_train, y_denominador_test = train_test_split(X, y_denominador, test_size=0.2, random_state=42)

# Modelo para Numerador
gbr_numerador = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbr_numerador.fit(X_train, y_numerador_train)
y_numerador_pred = gbr_numerador.predict(X_test)

print("\n--- Avaliação do Modelo para NUMERADOR ---")
print(f"Erro Quadrático Médio (MSE): {mean_squared_error(y_numerador_test, y_numerador_pred):.2f}")
print(f"R2 Score: {r2_score(y_numerador_test, y_numerador_pred):.2f}")

# Modelo para Denominador
gbr_denominador = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbr_denominador.fit(X_train, y_denominador_train)
y_denominador_pred = gbr_denominador.predict(X_test)

print("\n--- Avaliação do Modelo para DENOMINADOR ---")
print(f"Erro Quadrático Médio (MSE): {mean_squared_error(y_denominador_test, y_denominador_pred):.2f}")
print(f"R2 Score: {r2_score(y_denominador_test, y_denominador_pred):.2f}")



