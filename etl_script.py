import pandas as pd

# **Transformação**

# 1. Carregar o arquivo CSV
df = pd.read_csv('dados_clientes.csv')

# 2. Limpeza de Dados
# Removendo registros onde o valor_gasto possa ser NaN ou negativo
df = df[df['valor_gasto'] > 0]

# 3. Categorização dos Gastos
def categorizar_gastos(valor):
    if valor < 1000:
        return 'Baixo'
    elif valor < 2000:
        return 'Médio'
    else:
        return 'Alto'

df['categoria_gasto'] = df['valor_gasto'].apply(categorizar_gastos)

# 4. Cálculo de Progresso
df['progresso_meta'] = (df['valor_gasto'] / 2500) * 100

# 5. Recomendações Santander
def gerar_recomendacoes(categoria):
    if categoria == 'Baixo':
        return 'Considere a Conta Poupança Santander para economizar mais!'
    elif categoria == 'Médio':
        return 'Você está no caminho certo! Considere o Cartão Santander Viagens para recompensas!'
    else:
        return 'Ótimo trabalho! Veja nossos investimentos para maximizar seus rendimentos!'

df['recomendacao_santander'] = df['categoria_gasto'].apply(gerar_recomendacoes)

# **Exibição dos resultados**

print("Resultados de Transformação e Recomendações:")
print("-" * 60)

for index, row in df.iterrows():
    print(f"ID do Cliente: {row['id_cliente']}")
    print(f"Nome: {row['nome']}")
    print(f"Valor Gasto: R${row['valor_gasto']:.2f}")
    print(f"Categoria de Gasto: {row['categoria_gasto']}")
    print(f"Progresso da Meta: {row['progresso_meta']:.2f}%")
    print(f"Recomendação Santander: {row['recomendacao_santander']}")
    print("-" * 60)

