import numpy as np
import pandas as pd

pd.options.display.width = 0
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = pd.read_csv('SAFRA.csv')


def insert_sql(produto, start_codplano):
    servicos = [110010723, 110011513, 110011514]
    list_codplano = []
    list_servicos = []

    df_faixa = df.query(f'Produtos == "{produto}"')
    qtd_faixa = len(df_faixa.index)

    df_faixa_3_times = df_faixa.loc[df_faixa.index.repeat(3)]

    for i in range(qtd_faixa):
        j = 3
        while j > 0:
            codplano = start_codplano + i
            list_codplano.append(codplano)
            j = j - 1

    df_faixa_3_times.insert(0, "CODPLANO", list_codplano, True)

    for i in range(qtd_faixa):
        for servico in servicos:
            list_servicos.append(servico)

    df_faixa_3_times.insert(1, "CODGAR", list_servicos, True)

    df_trat_1 = df_faixa_3_times[["CODPLANO", "CODGAR", "Inicial", "Final", "Premio1", "Premio2", "Premio3"]]

    # Renomeia as colunas
    df_trat_1 = df_trat_1.rename(columns={"Inicial": "VLRMIN", "Final": "VLRMAX", "Premio1": "PRECO"})

    # Criar um índice exclusivo para evitar problemas de repetição de índices
    df_trat_1.reset_index(drop=True, inplace=True)

    # Substituir valores na coluna 'PRECO' de acordo com o índice da linha
    # Substituir pelo 'Premio2' na segunda linha do mesmo grupo de 'CODPLANO'
    df_trat_1.loc[df_trat_1.index % 3 == 1, 'PRECO'] = df_trat_1['Premio2']
    # Substituir pelo 'Premio3' na terceira linha do mesmo grupo de 'CODPLANO'
    df_trat_1.loc[df_trat_1.index % 3 == 2, 'PRECO'] = df_trat_1['Premio3']

    df_trat_2 = df_trat_1[["CODPLANO", "CODGAR", "VLRMIN", "VLRMAX", "PRECO"]]
    print(df_trat_2)

    df_trat_3 = df_trat_2.dropna()
    df_trat_3.to_csv('df_trat_3.csv', mode='a', index=False, header=False)


categorias = ['BICICLETA (CONVENCIONAL ARO) 3 MESES DE GTA E 21 MESES DE GARANTIA ESTENDIDA',
              'FITNESS ELÍPTICO / ESTEIRA / ERGOMÉTRICA /  PLATAFORMA VIBRATÓRIA / FITNESS REMO /  APARELHO ABDOMINAL / STEPPER',
              'FERRAMENTAS',
              'FERRAMENTAS - 24 MESES DE GARANTIA DE FÁBRICA',
              'PEQUENO PORTE - 24 MESES DE GARANTIA DE FÁBRICA']
faixas = [14100, 14200, 14300, 14400, 14700]

for categoria in categorias:
    index = categorias.index(categoria)
    insert_sql(categoria, faixas[index])
