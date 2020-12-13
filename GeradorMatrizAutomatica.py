#MatrizAutomatica.py

#funcao para gerar tabuleiros validos do sudoku
def funcaoMatrizAutomatica():

    matriz_conhecida = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],

                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],

                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]

    import random
    from random import sample
    grupos = [p // 27 * 3 + p % 9 // 3 for p in range(81)]
    colunaNumeros = [set(range(1, 10)) for _ in range(9)]
    LinhaNumeros = [set(range(1, 10)) for _ in range(9)]
    grupoNumeros = [set(range(1, 10)) for _ in range(9)]
    sudoku = [[0] * 9 for _ in range(9)]
    for pos in range(81):
        linha, coluna, group = pos // 9, pos % 9, grupos[pos]
        fixed = matriz_conhecida[linha][coluna]
        if fixed:
            sudoku[linha][coluna] = fixed
            colunaNumeros[coluna].discard(fixed)
            LinhaNumeros[linha].discard(fixed)
            grupoNumeros[group].discard(fixed)

    pos = 0
    tried = [set() for _ in range(81)]
    while pos in range(81):
        linha, coluna, group = pos // 9, pos % 9, grupos[pos]
        number = sudoku[linha][coluna]
        fixed = matriz_conhecida[linha][coluna]
        if number != 0 and not fixed:
            sudoku[linha][coluna] = 0
            colunaNumeros[coluna].add(number)
            LinhaNumeros[linha].add(number)
            grupoNumeros[group].add(number)
        available = {fixed} if fixed else colunaNumeros[coluna] & LinhaNumeros[linha] & grupoNumeros[group]
        available -= tried[pos]
        if available:
            number = fixed or random.choice(list(available))
            if not fixed:
                sudoku[linha][coluna] = number
                colunaNumeros[coluna].discard(number)
                LinhaNumeros[linha].discard(number)
                grupoNumeros[group].discard(number)
            tried[pos].add(number)
            pos += 1
        else:
            tried[pos] = set()
            pos -= 1

    if pos < 81:
        print("Falhou!")
    else:
        print("Matriz gerada!")
        # for r,line in  enumerate(sudoku):
        # print(*[line[i:][:3] for i in range(0,9,3)],"\n"*(r%3==2))

    len(sudoku)
    lista_posicoes_escolhidas = []

    '''print("Matriz original")
    for i in range(0, len(sudoku)):
        print(sudoku[i])'''

    '''print("Posições")'''
    for i in range(0, 9):
        posicoes_preenchidas = sample(range(3, 6), 1)
        #3,6
        quant_posicoes_preenchidas = posicoes_preenchidas[0]

        posicoes_escolhidas = sample(range(0, 9), quant_posicoes_preenchidas)
        '''print(posicoes_escolhidas)'''
        lista = []
        for i in range(0, len(posicoes_escolhidas)):
            lista.append(posicoes_escolhidas[i])
        lista_posicoes_escolhidas.append(lista)

    lista_posicoes_escolhidas_ordenada = sorted(lista_posicoes_escolhidas)

    lista_numeros = []

    for i in range(len(lista_posicoes_escolhidas)):
        for j in range(len(lista_posicoes_escolhidas[i])):
            sudoku[i][lista_posicoes_escolhidas[i][j]] = 0

    '''print("Matriz alterada")
    print(sudoku)
    print("Retorno")'''''
    return sudoku
