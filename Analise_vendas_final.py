import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np



df = pd.read_excel("C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Projetos\\Analise vendas\\dados_vendas.xlsx")
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
Receita_total_A =  (Preço_A) * Total_vendido_A
Receita_total_B =  (Preço_B) * Total_vendido_B
Receita_total_C =  (Preço_C) * Total_vendido_C


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

# Gráficos

# Lucros no decorrer do ano 
df['Mês'] = df['Data'].dt.month
Meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio'}
df['Mês'] = Meses
Lucros = {1:Lucro_1, 2:Lucro_2, 3:Lucro_3, 4:Lucro_4, 5:Lucro_5}
plt.figure(figsize=(10,8))
plt.subplot(221)
plt.title('Análise do ano')
sns.set_theme(style='darkgrid')
sns.lineplot(y=Lucros, x=df['Mês'])
plt.ylabel('Lucros')

# Produtos mais vendidos
Produtos = ['Produto A', 'Produto B', 'Produto C']
Total_vendido = [Total_vendido_A, Total_vendido_B, Total_vendido_C]
plt.subplot(222)
plt.title('Quantidade de produtos vendidos')
plt.pie(Total_vendido, labels=Produtos, autopct='%1.0f%%', shadow=True,startangle=90)
plt.axis('equal')



# Lucro cada produto
P = np.array([Receita_total_A, Receita_total_B, Receita_total_C])
Receita = [valor.item() for valor in P]
plt.subplot(223)
plt.title('Receita por produto')
plt.bar(Produtos, Receita, color='green')
plt.ylabel('Receita')

# Quantidade de vendas por Região
Total_Região = [Região_Norte, Região_Sul, Região_Leste, Regiao_Oeste]
plt.subplot(224)
plt.title('Vendas por Região')
plt.bar(['Região Norte', 'Região Sul', 'Região Leste', 'Regiao Oeste'], Total_Região)
plt.ylabel('Vendas')

plt.tight_layout() # Não sobrepor os gráficos
plt.show() # Mostrar os gráficos

# Conclusão

# Produto com maior vendas
Total_vendido = {'Produto A': Total_vendido_A,'Produto B': Total_vendido_B,'Produto C': Total_vendido_C}
Produto_mais_vendido = max(Total_vendido, key=Total_vendido.get)
print(f'O produto com mais vendas é {Produto_mais_vendido} com {Total_vendido[Produto_mais_vendido]} vendas')

# Produto com menor vendas
Total_vendido = {'Produto A': Total_vendido_A,'Produto B': Total_vendido_B,'Produto C': Total_vendido_C}
Produto_menos_vendido = min(Total_vendido, key=Total_vendido.get)
print(f'O produto com menos vendas é {Produto_menos_vendido} com {Total_vendido[Produto_menos_vendido]} vendas')

# Mês com maior lucro
Meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio'}
Lucros = {1:Lucro_1, 2:Lucro_2, 3:Lucro_3, 4:Lucro_4, 5:Lucro_5}
Mes_Lucro_max = max(Lucros)
print(f'O mês com maior lucro é {Meses[Mes_Lucro_max]} com o total de {Lucros[Mes_Lucro_max]}')

# Mês com menor lucro
Meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio'}
Lucros = {1:Lucro_1, 2:Lucro_2, 3:Lucro_3, 4:Lucro_4, 5:Lucro_5}
Mes_Lucro_min= min(Lucros)
print(f'O mês com menor lucro é {Meses[Mes_Lucro_min]} com o total de {Lucros[Mes_Lucro_min]}')

# Região com maior vendas
Regiões = {'Norte': Região_Norte, 'Sul':Região_Sul, 'Leste':Região_Leste, 'Oeste':Regiao_Oeste}
Região_maior_venda = max(Regiões, key=Regiões.get)
print(f'A região com maior venda é {Região_maior_venda}')

# Região com menor vendas
Regiões = {'Norte': Região_Norte, 'Sul':Região_Sul, 'Leste':Região_Leste, 'Oeste':Regiao_Oeste}
Região_menor_venda = min(Regiões, key=Regiões.get)
print(f'A região com menor venda é {Região_menor_venda}')

# Lucro por canal de venda
Online_A = sum(df[(df['Canal de Vendas'] == "Online") & (df['Produto'] == "Produto A")] ['Quantidade Vendida'])
Online_B = sum(df[(df['Canal de Vendas'] == "Online") & (df['Produto'] == "Produto B")] ['Quantidade Vendida'])
Online_C= sum(df[(df['Canal de Vendas'] == "Online") & (df['Produto'] == "Produto C")] ['Quantidade Vendida'])

Fisica_A = sum(df[(df['Canal de Vendas'] == "Loja Física") & (df['Produto'] == "Produto A")] ['Quantidade Vendida'])
Fisica_B = sum(df[(df['Canal de Vendas'] == "Loja Física") & (df['Produto'] == "Produto B")] ['Quantidade Vendida'])
Fisica_C = sum(df[(df['Canal de Vendas'] == "Loja Física") & (df['Produto'] == "Produto C")] ['Quantidade Vendida'])

Lucro_Online = (Preço_A*Online_A) + (Preço_B*Online_B) + (Preço_C*Online_C)
Lucro_Loja_Fisica = (Preço_A*Fisica_A) + (Preço_B*Fisica_B) + (Preço_C*Fisica_C)

if Lucro_Online > Lucro_Loja_Fisica:
    print('O canal de venda que mais trouxe benefício e lucro é o Online')
else: 
    print('O canal de venda que mais trouxe benefício é o da Loja Física')
