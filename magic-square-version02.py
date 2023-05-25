import random

def resulta_quadrado_magico(matriz_quadrada_num):

    ## TODO Objetivo: checar se o quadrado em analise e (ou nao) magico.

    soma_alvo = sum(matriz_quadrada_num[0])
    # Checar linhas
    for linhas in matriz_quadrada_num:
        if sum(linhas) != soma_alvo:
            return False
    # Checar colunas
    for colunas in range(len(matriz_quadrada_num)):
        soma_colunas = sum(linhas[colunas] for linhas in matriz_quadrada_num)
        if soma_colunas != soma_alvo:
            return False
    # Checar a diagonal do quadrado.
    soma_diagonal = sum(matriz_quadrada_num[indice][indice] for indice in range(len(matriz_quadrada_num)))
    if soma_diagonal != soma_alvo:
        return False
    # Checar a diagonal secundaria do quadrado.
    soma_diagonal_aux = sum(matriz_quadrada_num[indice][len(matriz_quadrada_num) - indice - 1] for indice in range(len(matriz_quadrada_num)))
    if soma_diagonal_aux != soma_alvo:
        return False
    return True

def gerando_quadrado_magico(n_dimensao):
    """
    Gerar um quadrado magico do tamanho N x N usando voltando atras.
    """
    def voltar_passo(matriz_quadrada_num, fila, coluna):
        if fila == n_dimensao:
            if resulta_quadrado_magico(matriz_quadrada_num):
                return matriz_quadrada_num
            return None
        for numeros in range(1, n_dimensao ** 2 + 1):
            if numeros not in num_usados:
                matriz_quadrada_num[fila][coluna] = numeros
                num_usados.add(numeros)
                if coluna == n_dimensao - 1:
                    prox_linha = fila + 1
                    prox_coluna = 0
                else:
                    prox_linha = fila
                    prox_coluna = coluna + 1
                resultado = voltar_passo(matriz_quadrada_num, prox_linha, prox_coluna)
                if resultado:
                    return resultado
                matriz_quadrada_num[fila][coluna] = 0
                num_usados.remove(numeros)
        return None

    quadrado = [[0] * n_dimensao for _ in range(n_dimensao)]
    num_usados = set()
    return voltar_passo(quadrado, 0, 0)

def print_square(matriz_quadrada_num):
    """
    Apresentando em tela o quadrado magico (caso haja).
    """
    for linhas in matriz_quadrada_num:
        print(" ".join(str(numeros) for numeros in linhas))
while True:
    tamanho = int(input("Digite a dimensao do quadrado magico: "))
    quadrado_magico = gerando_quadrado_magico(tamanho)
    if quadrado_magico:
        print("Oba! Foi gerado um quadrado magico: ")
        print_square(quadrado_magico)
        if resulta_quadrado_magico(quadrado_magico):
            print("Wow! Gerado um quadrado magico valido.")
        else:
            print("Oops! Nao e quadrado magico.")
    else:
        print(f"Oh! {tamanho}x{tamanho} quadrado magico nao encontrado...")
    continuar_opcao = input("Deseja continuar? (s/n): ")
    if continuar_opcao.lower() != "s":
        break
