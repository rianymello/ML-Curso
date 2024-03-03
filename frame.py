import pandas as pd
import numpy as np

# Gerando novos registros de treinamento com valores aleatórios
n_train_records = 200
train_data = []
for _ in range(n_train_records):
    idade = np.random.randint(18, 50)
    genero = np.random.choice(['Masculino', 'Feminino'])
    nivel_educacao = np.random.choice(['Graduação', 'Ensino Médio', 'Pós-graduação'])
    renda = np.random.randint(800, 5000)  

    # Ajustando a probabilidade de compra com base no nível de educação e renda
    if nivel_educacao == 'Ensino Médio':
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado
    elif nivel_educacao == 'Graduação':
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado
    else:
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado

    # Ajustando a probabilidade de compra com base na renda
    if renda >= 3000:
        probabilidade_compra *= 0.8  # Aumenta a probabilidade se a renda for alta

    # Ajustando a probabilidade de compra com base no gênero
    if genero == 'Feminino':
        probabilidade_compra *= 0.8  # Aumenta a probabilidade se for feminino

    # Ajustando a probabilidade de compra com base na experiência em programação
    if np.random.rand() < 0.4:  # 40% de chance de ter experiência em programação
        probabilidade_compra *= 0.5  # Reduz a probabilidade se tiver experiência em programação

    comprou_curso = np.random.choice(['Sim', 'Não'], p=[probabilidade_compra, 1 - probabilidade_compra])

    train_data.append([idade, genero, nivel_educacao, renda, comprou_curso])

# Gerando novos registros de teste com valores aleatórios
n_test_records = 50
test_data = []
for _ in range(n_test_records):
    idade = np.random.randint(18, 50)
    genero = np.random.choice(['Masculino', 'Feminino'])
    nivel_educacao = np.random.choice(['Graduação', 'Ensino Médio', 'Pós-graduação'])
    renda = np.random.randint(800, 5000)  

    # Ajustando a probabilidade de compra com base no nível de educação e renda
    if nivel_educacao == 'Ensino Médio':
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado
    elif nivel_educacao == 'Graduação':
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado
    else:
        probabilidade_compra = np.random.choice([0.5, 0.5])  # Equilibrado

    # Ajustando a probabilidade de compra com base na renda
    if renda >= 3000:
        probabilidade_compra *= 0.8  # Aumenta a probabilidade se a renda for alta

    # Ajustando a probabilidade de compra com base no gênero
    if genero == 'Feminino':
        probabilidade_compra *= 0.8  # Aumenta a probabilidade se for feminino

    # Ajustando a probabilidade de compra com base na experiência em programação
    if np.random.rand() < 0.4:  # 40% de chance de ter experiência em programação
        probabilidade_compra *= 0.5  # Reduz a probabilidade se tiver experiência em programação

    comprou_curso = np.random.choice(['Sim', 'Não'], p=[probabilidade_compra, 1 - probabilidade_compra])

    test_data.append([idade, genero, nivel_educacao, renda, comprou_curso])

# Convertendo os dados em DataFrames
df_train = pd.DataFrame(train_data, columns=['Idade', 'Gênero', 'Nível_Educação', 'Renda', 'Comprou_Curso'])
df_test = pd.DataFrame(test_data, columns=['Idade', 'Gênero', 'Nível_Educação', 'Renda', 'Comprou_Curso'])

# Salvando os dados de treinamento e teste em arquivos CSV separados
df_train.to_csv('dados_treinamento.csv', index=False)
df_test.to_csv('dados_teste.csv', index=False)
