import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

# Carregar os dados
dados = pd.read_csv('dados_treinamento.csv')

# Converter dados categóricos em números usando LabelEncoder
le = LabelEncoder()
dados['Gênero'] = le.fit_transform(dados['Gênero'])
dados['Nível_Educação'] = le.fit_transform(dados['Nível_Educação'])
dados['Comprou_Curso'] = le.fit_transform(dados['Comprou_Curso'])

# Separar características (X) e rótulos (y)
X = dados.drop('Comprou_Curso', axis=1)
y = dados['Comprou_Curso']

# Criar uma instância SMOTE
smote = SMOTE(random_state=42)

# Aplicar oversampling aos dados
X_resampled, y_resampled = smote.fit_resample(X, y)

# Criar um DataFrame com os dados balanceados
df_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns),
                          pd.DataFrame(y_resampled, columns=['Comprou_Curso'])],
                          axis=1)

# Salvar os dados balanceados em um arquivo CSV
df_resampled.to_csv('dados_treinamento_balanceados.csv', index=False)
