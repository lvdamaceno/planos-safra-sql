def cria_insert(descricao, faixa, tamanho_faixa):
    for posicao in range(tamanho_faixa):
        plano = f"({faixa}, 'EG SAFRA - {descricao} PLAN {faixa}'),"
        print(plano)
        faixa += 1


if __name__ == '__main__':
    print('INSERT INTO TGFPLA (CODPLANO, NOMEPLANO) VALUES')
    categorias = ['ADEGA',
                  'BEBEDOURO DE ÁGUA ELÉTRICO',
                  'CENTRÍFUGA DE ROUPA',
                  'CENTRÍFUGA DE ROUPA -24 MESES DE GARANTIA DE FÁBRICA',
                  'COIFA / EXAUSTOR',
                  'CONDICIONADOR DE AR CONVENCIONAL',
                  'CONDICIONADOR DE AR CONVENCIONAL - 24 MESES DE GARANTIA DE FÁBRICA',
                  'CONDICIONADOR DE AR CONVENCIONAL - 36 MESES DE GARANTIA DE FÁBRICA',
                  'CONDICIONADOR DE AR SPLIT + PORTATIL',
                  'CONDICIONADOR DE AR SPLIT + PORTATIL - 24 MESES DE GARANTIA DE FÁBRICA',
                  'CONDICIONADOR DE AR SPLIT + PORTATIL - 36 MESES DE GARANTIA DE FÁBRICA',
                  'FOGÃO',
                  'FOGÃO - 24 MESES DE GARANTIA DE FÁBRICA',
                  'FOGÃO COOKTOP / FOGÃO ELÉTRICO',
                  'FORNO A GÁS',
                  'FORNO A GÁS - 24 MESES DE GARANTIA DE FÁBRICA',
                  'FREEZER',
                  'FREEZER - 24 MESES DE GARANTIA DE FÁBRICA',
                  'LAVADORA DE ROUPA',
                  'LAVADORA DE ROUPA - 24 MESES DE GARANTIA DE FÁBRICA',
                  'LAVADORA DE LOUÇA',
                  'MÁQUINA DE COSTURA',
                  'MICROONDAS',
                  'REFRIGERADOR 1 PORTA +  REFRIGERADOR 2 PORTAS + FRIGOBAR',
                  'REFRIGERADOR 1 PORTA +  REFRIGERADOR 2 PORTAS + FRIGOBAR - 24 MESES DE GARANTIA DE FÁBRICA',
                  'REFRIGERADOR SIDE-BY-SIDE',
                  'TANQUINHO',
                  'TANQUINHO - 24 MESES DE GARANTIA DE FÁBRICA',
                  'ANTENA PARABÓLICA',
                  'ÁUDIO SYSTEM | CAIXA AMPLIFICADA I AMPLIFICADOR DE SOM',
                  'DVD PLAYER CONVENCIONAL + DVD PLAYER COM BLU-RAY',
                  'DVD PLAYER CONVENCIONAL + DVD PLAYER COM BLU-RAY - 24 MESES DE GARANTIA DE FÁBRICA',
                  'HOME THEATER DIGITAL COM DVD + BLU-RAY',
                  'TELEVISOR LCD + LED + QLED + 4K',
                  'COMPUTADOR LAPTOP / NOTEBOOK',
                  'COMPUTADOR DESKTOP',
                  'IMPRESSORA JATO DE TINTA + LASER',
                  'MULTIFUNCIONAL + SCANNER',
                  'MONITOR DE LCD + LED',
                  'TABLET + IPAD',
                  'TELEFONE CELULAR',
                  'BICICLETA (CONVENCIONAL ARO) 3 MESES DE GTA E 21 MESES DE GARANTIA ESTENDIDA',
                  'FITNESS ELÍPTICO / ESTEIRA / ERGOMÉTRICA /  PLATAFORMA VIBRATÓRIA / FITNESS REMO /  APARELHO ABDOMINAL / STEPPER',
                  'FERRAMENTAS',
                  'FERRAMENTAS - 24 MESES DE GARANTIA DE FÁBRICA',
                  'CARRINHO DE BEBE',
                  'PEQUENO PORTE',
                  'PEQUENO PORTE - 24 MESES DE GARANTIA DE FÁBRICA',
                  'EQUIPAMENTOS DE SEGURANÇA',
                  'MOVEIS  / MÓVEIS ESTOFADOS',
                  'COLCHÃO']
    faixas = [10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400,
              11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900,
              13000, 13100, 13200, 13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400,
              14500, 14600, 14700, 14800, 14900, 15000]
    tamanho = [29, 8, 5, 5, 14, 19, 19, 19, 19, 19, 19, 20, 20, 15, 20, 20, 15, 15, 22, 22, 13, 13, 13, 29, 29, 29, 8,
               8, 7, 37, 16, 16, 22, 44, 27, 15, 14, 14, 15, 20, 27, 13, 25, 12, 12, 17, 22, 22, 22, 42, 24]

    for categoria in categorias:
        index = categorias.index(categoria)
        cria_insert(categoria, faixas[index], tamanho[index])
