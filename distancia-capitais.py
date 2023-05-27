## Inicio com a MATRIZ DE DISTANCIA ##
matriz_distancias = [[0, 524, 521, 882],
                     [524, 0, 434, 586],
                     [521, 434, 0, 429 ],
                     [882, 586, 429, 0]
                     ]

## vetores STRING com os nomes das cidades ##
vetor_cidades = ['Vitoria', 'Belo Horizonte', 'Rio de Janeiro', 'Sao Paulo']

contador_origem = 0 ## linha
contador_destino = 1 ## coluna
while contador_origem != contador_destino:
    print('''\nMENU de opcoes de viagem:
    0 = Vitoria
    1 = Belo horizonte
    2 = Rio de Janeiro
    3 = Sao Paulo ''')

    ## PRECISO TRATAR O 'OUT OF RANGE' ##

    usuario_origem = input('\nDigite o numero da cidade ORIGEM: ')
    contador_origem = int(usuario_origem)
    usuario_destino = input('Digite agora a cidade DESTINO: ')
    contador_destino = int(usuario_destino)

    print(f'\nA distancia entre {vetor_cidades[contador_origem]} e {vetor_cidades[contador_destino]} e igual a {matriz_distancias[contador_origem][contador_destino]} km.')
