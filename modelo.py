import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar dados de arquivos .csv com valores separados por vírgula
dados_treinamento = pd.read_csv('dados_balanceados.csv')
dados_teste = pd.read_csv('dados_teste.csv')

# Separar características (X) e rótulos (y) nos dados de treinamento e teste
X_treino = dados_treinamento.drop('Comprou_Curso', axis=1)
y_treino = dados_treinamento['Comprou_Curso']

X_teste = dados_teste.drop('Comprou_Curso', axis=1)
y_teste = dados_teste['Comprou_Curso']

# Converter variáveis categóricas em variáveis dummy
X_treino = pd.get_dummies(X_treino)
X_teste = pd.get_dummies(X_teste)

# Garantir que as colunas nos dados de teste correspondam às colunas nos dados de treinamento
# Adicionar colunas ausentes aos dados de teste, preenchendo com zeros
for coluna in X_treino.columns:
    if coluna not in X_teste.columns:
        X_teste[coluna] = 0

# Reordenar as colunas dos dados de teste para que estejam na mesma ordem dos dados de treinamento
X_teste = X_teste[X_treino.columns]

# Inicializar e treinar o modelo de árvore de decisão
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_treino, y_treino)

# Fazer previsões com o conjunto de teste
previsoes = modelo.predict(X_teste)

# Avaliar o desempenho do modelo
print("Matriz de Confusão:")
print(confusion_matrix(y_teste, previsoes))
print("\nRelatório de Classificação:")
print(classification_report(y_teste, previsoes))
