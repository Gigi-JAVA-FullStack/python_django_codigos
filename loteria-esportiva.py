## Um cartao da Caixa com a loteria de FUTEBOL, com a possibilidade de preencher:
## vitoria do time da cidade, coluna 1, empate coluna do meio, vitoria do outro time, coluna 3.
## Declaracao da matriz construida:
vetor_jogos = [0] * 14
matriz_jogos = [['x', ' ', 'x'],
                ['x', ' ', ' '],
                [' ', 'x', ' '],
                ['x', ' ', ' '],
                ['x', ' ', 'x'],
                ['x', ' ', ' '],
                [' ', ' ', 'x'],
                [' ', 'x', 'x'],
                ['x', 'x', ' '],
                ['x', ' ', 'x'],
                [' ', 'x', ' '],
                [' ', 'x', 'x'],
                ['x', ' ', ' '],
                ['x', 'x', 'x']]

vetor_tipo_jogo = ['Simples', 'Duplo', 'Triplo']

vitoria_simples = 0
vitoria_dupla = 0
vitoria_tripla = 0

for i in range(14):
    aposta_primeiro_vetor = 0
    for j in range(3):
        if matriz_jogos[i][j] == 'x':
            aposta_primeiro_vetor += 1
    if aposta_primeiro_vetor == 1:
        vitoria_simples += 1
    elif aposta_primeiro_vetor == 2:
        vitoria_dupla += 1
    else:
        vitoria_tripla += 1
    print(f'Jogo de apostas {i+1:2}: {matriz_jogos[i]} e um {vetor_tipo_jogo[aposta_primeiro_vetor -1]}')
print('\nJogos simples: ', vitoria_simples)
print('Jogo duplo: ', vitoria_dupla)
print('Jogo triplo: ', vitoria_tripla)
