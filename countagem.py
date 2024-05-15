import pandas as pd

df = pd.read_csv('SAFRA.csv')

produtos = df['PRODUTOS']

produtos_list = []

for produto in produtos:
    produtos_list.append(produto)

my_dict = {i:produtos_list.count(i) for i in produtos_list}

# filtra faixas
produtos_list = []

for produto in produtos:
    if produto not in produtos_list:
        produtos_list.append(produto)

# for produto in produtos_list:
#     print(f"{produto}: {my_dict[produto]}")


for item in my_dict:
    print(f'{my_dict[item]},', end = " ")