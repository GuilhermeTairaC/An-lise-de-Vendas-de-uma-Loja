import pandas as pd
import math
import matplotlib



df = pd.read_excel("C:\\Users\\guilh\\Downloads\\dados_vendas.xlsx")
# Convertendo a coluna 'DATA' para datetime
df ['Data'] = pd.to_datetime(df['Data'])
# Quantidade de produtos
Tquantidade_A = len(df[(df['Produto'] == "Produto A")])

Tquantidade_B = len(df[(df['Produto'] == "Produto B")])

Tquantidade_C = len(df[(df['Produto'] == "Produto C")])

# Preço dos produtos
Preço_A = df[(df['Produto'] == "Produto A")]['Preço'].unique()

Preço_B = df[(df['Produto'] == "Produto B")]['Preço'].unique()

Preço_C = df[(df['Produto'] == "Produto C")]['Preço'].unique()

# Quantidade vendida por cada produto
Total_vendido_A = sum(df[(df['Produto'] == "Produto A")]['Quantidade Vendida'])

Total_vendido_B = sum(df[(df['Produto'] == "Produto B")]['Quantidade Vendida'])

Total_vendido_C = sum(df[(df['Produto'] == "Produto C")]['Quantidade Vendida'])


# Receita Total por produto
Receita_total_A =  Preço_A * Total_vendido_A
Receita_total_B =  Preço_B * Total_vendido_B
Receita_total_C =  Preço_C * Total_vendido_C

# Vendas por mês
    # Janeiro
Vendas_1 = sum(df[(df['Data'].dt.month == 1)]['Quantidade Vendida'])
Lucro_1 = sum(df[(df['Data'].dt.month == 1)]['Quantidade Vendida'] * df[(df['Data'].dt.month == 1)]['Preço'])
    # Fevereiro
Vendas_2 = sum(df[(df['Data'].dt.month == 2)]['Quantidade Vendida']) + df[(df['Data'].dt.month == 2)]['Preço']
Lucro_2 = sum(df[(df['Data'].dt.month == 2)]['Quantidade Vendida'] * df[(df['Data'].dt.month == 2)]['Preço'])
    # Março
Vendas_3 = sum(df[(df['Data'].dt.month == 3)]['Quantidade Vendida'])
Lucro_3 = sum(df[(df['Data'].dt.month == 3)]['Quantidade Vendida'] * df[(df['Data'].dt.month == 3)]['Preço'])
    # Abril
Vendas_4  = sum(df[(df['Data'].dt.month == 4)]['Quantidade Vendida'])
Lucro_4 = sum(df[(df['Data'].dt.month == 4)]['Quantidade Vendida'] * df[(df['Data'].dt.month == 4)]['Preço'])
    # Maio
Vendas_5 = sum(df[(df['Data'].dt.month == 5)]['Quantidade Vendida'])
Lucro_5 = sum(df[(df['Data'].dt.month == 5)]['Quantidade Vendida'] * df[(df['Data'].dt.month == 5)]['Preço'])

# Regiões com maiores vendas

Região_Norte = sum(df[(df['Região'] ==  'Norte')]['Quantidade Vendida'])
Região_Sul = sum(df[(df['Região'] ==  'Sul')]['Quantidade Vendida'])
Região_Leste = sum(df[(df['Região'] ==  'Leste')]['Quantidade Vendida'])
Regiao_Oeste = sum(df[(df['Região'] ==  'Oeste')]['Quantidade Vendida'])










# ANÁLISE DOS DADOS

# Região com maior vendas
Regiões = {'Norte': Região_Norte, 'Sul':Região_Sul, 'Leste':Região_Leste, 'Oeste':Regiao_Oeste}
Região_maior_venda = max(Regiões)
print(f'A região com maior venda é {Região_maior_venda}')

# Mês com maior lucro
Lucros = {1:Lucro_1, 2:Lucro_2, 3:Lucro_3, 4:Lucro_4, 5:Lucro_5}
Mes_Lucro_max = max(Lucros)
print(f'O mês com maior lucro é {Mes_Lucro_max} com o total de {Lucros[Mes_Lucro_max]}')
# Mês com menor lucro
Mes_Lucro_min= min(Lucros)
print(f'O mês com menor lucro é {Mes_Lucro_min} com o total de {Lucros[Mes_Lucro_min]}')


























