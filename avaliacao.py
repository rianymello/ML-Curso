import pandas as pd

# Carregar dados
dados = pd.read_csv('dados_treinamento.csv')

# Contar ocorrências de cada classe
distribuicao_classes = dados['Comprou_Curso'].value_counts()

print("Distribuição das Classes:")
print(distribuicao_classes)
