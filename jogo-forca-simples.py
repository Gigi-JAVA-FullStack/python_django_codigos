## DESAFIO 03 ## 
## 1) O programa usa uma lista de palavras e de forma aleatoria (RANDOM) escolhe uma
## das palavra dentro da lista para comecar a brincadeira.
## 2) O jogador (usuario) tem cinco tentativas para adivinhar a palavra corretamente. 
## 3) O programa acompanhará se as letras foram adivinhadas atraves de um LACO DE REPETICA.
## Exibirá na tela o estado atual das adivinhacoes mostrando espaços vazios _ _ _ _ para as
## letras que ainda não foram adivinhadas pelo usuario. 
## 4) O jogador tem 5 oportunidades para inserir uma letra e o programa ira respondendo,
## atraves de uma ESTRUTURA CONDICIONAL, usando IF ELIF ELSE, com a logica dentro do LOOPING.

import random
## Precisamos importar o módulo RANDOM em Python, que fornece funções para gerar números 
# aleatórios e selecionar elementos de uma sequência (exemplo: uma lista de palavras).

def enforcado():
    lista = ["banana", "laranja", "morango", "maracuja", "caju", "abacaxi", "jaca", "manga",
                      "abacate", "goiaba", "carambola", "kiwi", "coco"]
## A escolha_randomica conterá uma única palavra que foi escolhida aleatoriamente
## da lista, mas a própria lista deve permanecer com todas as palavras guardadas,
## para referência futura ou para recomecar o jogo, se for o desejo do jogador (usuario).

    escolha_randomica = random.choice(lista)
    ## CHOICE() choose a random word (element) from a non-empty list (sequence).
    letra_adivinhou = []
    tentativas = 5

    print('+++++++++++++++++++++++++++++++++++++')
    print("  Bem-vindo ao 'Jogo do Enforcado'!")
    print('+++++++++++++++++++++++++++++++++++++\n')

    print("Voce tera", tentativas, "tentativas para adivinhar a palavra escondida, ok?")
    print("Nesta rodada a palavra escolhida tem", len(escolha_randomica), "letras. Vamos comecar?")
    print()


    while tentativas > 0:
# Esta etapa ajuda a revelar as letras adivinhadas corretamente em suas posições 
# correspondentes dentro da palavra.
        palavra_escondida = ""
## FOR vai passar por cada letra, uma por uma, executando um LOOP cada iteração das letras.
        for letra in escolha_randomica:
            if letra in letra_adivinhou:
                palavra_escondida += letra
## A instrução IF verifica se a letra atual já foi adivinhada e está presente na coleção letra.
## Nesse caso, a letra é adicionada à string palavra_escondida. 
            else:
                palavra_escondida += "_"
## SENAO, caso contrario, se a letra ainda não foi adivinhada corretamente, nesse caso, 
# um sublinhado (_) é adicionado à string hidden_word. 
# Esta etapa mantém a natureza oculta das letras não adivinhadas (palavra escondida).
                print(palavra_escondida)

# No final do LOOP a palavra_escondida será uma STRING representando a escolha randomica, 
# mas, com sublinhados para todas as letras que ainda não foram adivinhadas. 
## Neste print vai aparecer na tela apenas a quantidade de sublinhados (_) para preencher.

        print("\nPalavra:", palavra_escondida)
        print("Numero de tentativas restantes:", tentativas)
        print()

## Segue o looping...
        if palavra_escondida == escolha_randomica:
            print("Uepa! Voce adivinhou a palavra corretamente.\n")
            break

        adivinha = input("Digite uma letra:").lower()
        print()

        if adivinha.isalpha() and len(adivinha) == 1:
## O método ISALPHA() é um método de STRING em Python que verifica se todos os caracteres
## em STRING são alfabéticos (letras). Retorna booleano TRUE se caracteres forem letras ou
# FALSE caso contrário.

## Funcao LEN(adivinha) == 1 verifica se o comprimento da STRING do palpite é exatamente == 1.
## Essa condição garante que a entrada do usuário seja um único caractere (letra) em vez de
## uma palavra ou frase. Se o comprimento não for 1, a condição será avaliada como FALSE.
            if adivinha in letra_adivinhou:
                print("Voce ja adivinhou esta letra...")
            elif adivinha in escolha_randomica:
                print("Oba, voce acertou a letra!")
                letra_adivinhou.append(adivinha)
## O programa imprime feedback positivo sobre todos os palpites corretos. 
## A letra adivinhada é então anexada à LISTA com o METODO letra_adivinhou.append(adivinha).
            else:
                print("Que pena, tentativa errada!")
                tentativas -= 1
                letra_adivinhou.append(adivinha)
## O programa oferece feedback negativo: "Letra errada!" para indicar que a letra escolhida
# não faz parte da palavra randomica. A variavel TENTATIVAS recebe -= 1 (é entao decrementada).
## diminuído em 1 a cada LOOPING para reduzir o número de tentativas (ate chegar ao limite). 
        else:
## SENAO, caso o usuário digite algo diferente de uma letra ou se inserir vários caracteres, 
## a condição será avaliada como FALSE. Isso ajuda a garantir que a entrada do usuário seja 
## uma única letra válida.
            print("Invalido! Por favor, digite apenas uma letra, ok?.")
    else:
        print("Como dizem: \'GAME IS OVER!' Voce usou as 5 tentativas do jogo.")
        print("A palavra escolhida era:", escolha_randomica)
    print('+++++++++++++++++++++++++++++++++++++')
## No geral, esse trecho de código lida com a lógica relacionada à verificação da exatidão
## da letra adivinhada (ou nao) e fornece os feedbacks apropriado ao jogador (usuario).
# No final existe a opcao do programa REINICIAR, atraves do LOOP da variavel "play_again".

    play_again = input("Deseja jogar novamente? (s/n): ")
    if play_again.lower() != 's':
        ## se digitar qualquer coisa diferente de S, vai sair...
        exit()
    else:
        enforcado()

enforcado()
