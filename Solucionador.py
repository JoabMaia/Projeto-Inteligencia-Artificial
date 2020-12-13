#Solucionador.py
from GeradorMatrizAutomatica import funcaoMatrizAutomatica

#matriz - teste e utilizada na interface
matriz_automatica = funcaoMatrizAutomatica()

#Quantidade de jogadas realizadas pelo algoritmo
lista_quantidade_jogadas_algoritmo = []
def quantidade_jogadas_algoritmo():
    contador_de_jogadas_algoritmo = 0
    contador_de_jogadas_algoritmo += 1
    lista_quantidade_jogadas_algoritmo.append(contador_de_jogadas_algoritmo)
    return len(lista_quantidade_jogadas_algoritmo)


#funcao para verificar se a posicao onde estamos tentando inserir e valida
def valida(bo, num, pos):
    # valida linha
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # valida coluna
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # valida caixa
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


#funcao para encontrar posicao vazia no tabuleiro
def encontrar_vazio(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


#funcao recursiva - algoritmo backtracking
def resolver(bo):

    for linha in bo:
        print(linha)
    encontrar = encontrar_vazio(bo)

    if not encontrar:
        return True
    else:
        linha, coluna = encontrar
    candidatos = []

    for i in range(1, 10):
        if valida(bo, i, (linha, coluna)):
            candidatos.append(i)
    print("Candidatos para posição (" + str(linha) + ", " + str(coluna) + "):", candidatos)

    for i in candidatos:
        bo[linha][coluna] = i
        print("Colocando o valor " + str(bo[linha][coluna]) + " na posicao (" + str(linha) + ", " + str(coluna) + ")")
        quantidade_jogadas_algoritmo()
        if resolver(bo):
            return True
        bo[linha][coluna] = 0

    return False

#funcao para saber total de jogadas realizadas pelo algoritmo
def totaljogadasalgoritmo():
    resolver(matriz_automatica)
    return quantidade_jogadas_algoritmo()


#funcao para verificar tamanho da lista que armazena a quantidade de jogadas do algoritmo
def quantidadedojogadasalgoritmo():
    return len(lista_quantidade_jogadas_algoritmo)


#resolver(matriz_automatica)
print("Quantidade de Jogadas do algoritmo: ", quantidadedojogadasalgoritmo())
