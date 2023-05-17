## DESAFIO 03 ## 
## (1) O programa usa uma lista de palavras e de forma aleatoria (RANDOM) escolhe uma
## das palavra dentro da lista para comecar a brincadeira. Ou o jogo pergunta se o jogador 
## deseja escolher sua propria palavra. Menu com um looping IF ELIF ELSE.
## (2) O jogador (usuario) tem cinco tentativas para adivinhar a palavra corretamente. 
## (3) O programa acompanhará se as letras foram adivinhadas, usando um LACO DE REPETICA.
## Exibirá na tela o estado atual das adivinhacoes mostrando espaços vazios _ _ _ _ para as
## letras que ainda não foram adivinhadas pelo usuario. Na rodada do LOOPING acrescenta letras (ou nao).
## (4) O jogador tem 5 oportunidades para inserir uma letra e o programa ira respondendo,
## atraves de uma ESTRUTURA CONDICIONAL, IF ELIF ELSE, com a logica dentro do LOOPING.

import random
## Em Python precisamos importar o module RANDOM, que fornece funções para gerar números 
# aleatórios e selecionar elementos de uma sequência (jogo: uma lista de palavras).

def enforcado():
    lista = ["banana", "laranja", "morango", "maracuja", "caju", "abacaxi", "jaca", "manga",
                      "abacate", "goiaba", "carambola", "kiwi", "coco"]
## A escolha_randomica conterá uma única palavra que foi escolhida aleatoriamente na lista,
## mas a própria lista deve permanecer com todas as palavras guardadas,  para referência 
## futura ou para recomecar o jogo, se for o desejo do jogador (usuario).

    print('\n+++++++++++++++++++++++++++++++++++++')
    print("  Bem-vindo ao 'Jogo do Enforcado'!")
    print('+++++++++++++++++++++++++++++++++++++\n')
     # Prompt para usuario escolher entre uma palavra da LISTA existente ou inserir NOVA palavra.
    escolha_jogar = input("\nMENU: Escolha '1' para o PROGRAMA escolher a palavra ou '2' para VOCE digitar a palavra: ").lower()
    ## CHOICE() choose a random word (element) from a non-empty list (sequence).
    if escolha_jogar == '1':
        escolha_randomica = random.choice(lista)
    elif escolha_jogar == '2':
        escolha_randomica = input("Escolha e digite uma UNICA palavra: ").lower()
    else:
        print("Invalido. Por favor, tente novamente, digite 1 ou 2 e vamos jogar...")
        return

    letra_adivinhou = []
    tentativas = 5

    print("Voce tera", tentativas, "tentativas para adivinhar a palavra escondida, ok?")
    print("Nesta rodada a palavra escolhida tem", len(escolha_randomica), "letras. Vamos comecar?")
    print()


    while tentativas > 0:
## Esta etapa ajuda a revelar as letras que foram adivinhadas e em suas posições correspondentes.
        palavra_escondida = ""
## O laco FOR vai passar por cada letra, uma por uma, executando um LOOP cada iteração das letras.
        for letra in escolha_randomica:
            if letra in letra_adivinhou:
                palavra_escondida += letra
## A instrução IF verifica se a letra atual já foi adivinhada e está presente na coleção letra.
## Nesse caso, a letra é adicionada à string palavra_escondida, acontecendo um INCREMENTO. 
            else:
                palavra_escondida += "_"
## SENAO, caso contrario, se a letra ainda não foi adivinhada, nesse caso um sublinhado (_)
#  é adicionado à string. Esta etapa mantém a natureza oculta das letras não adivinhadas.
                print(palavra_escondida)
# Final do LOOP a palavra_escondida será uma STRING representando a escolha randomica, mas,
#  com sublinhados para todas as letras que ainda não foram adivinhadas. 
## Neste PRINT() vai aparecer tela apenas a quantidade de sublinhados (_) para preencher...
        print("\nPalavra:", palavra_escondida)
        print("Numero de tentativas restantes:", tentativas)
        print()
## Segue o looping...
        if palavra_escondida == escolha_randomica:
            print("Uepa! Voce adivinhou a palavra corretamente.\n")
            break
        adivinha = input("Digite uma letra:").lower()
        print()
## Em Python, funcao ISALPHA() é um método de STRING em Python que verifica se os caracteres,
## as STRINGs, são alfabéticos (letras) e retorna bool TRUE se caracteres forem letras ou
# FALSE no caso contrário.
        if adivinha.isalpha() and len(adivinha) == 1:
## A funcao LEN(adivinha) == 1 vai verificar se o comprimento STRING palpite é exatamente == um.
## Essa condição garante que a entrada do usuário seja UM único caractere (letra) em vez de
## uma palavra ou frase. Se o comprimento não for == 1, a condição será avaliada como FALSE, 
# nao entrara no proximo laco IF ELIF ELSE, que analisa se o jogador adivinhou a letra.
            if adivinha in letra_adivinhou:
                print("Voce ja adivinhou esta letra...")
            elif adivinha in escolha_randomica:
                print("Oba, voce acertou a letra!")
                letra_adivinhou.append(adivinha)
## O programa eh amigavel, imprime feedback positivo sobre todos os palpites corretos. 
## ENTAO, a letra adivinhada é anexada à LISTA com o metodo letra_adivinhou.APPEND(adivinha).
            else:
                print("Que pena, tentativa errada!")
                tentativas -= 1
                letra_adivinhou.append(adivinha)
## O programa oferece feedback negativo: "Letra errada!" para indicar que a letra escolhida
# não faz parte da palavra randomica. A variavel TENTATIVAS recebe -= 1 (DECREMENTO),
# as tentativa diminuem em 1 passo a cada LOOPING (ate chegar ao condicao limite >0 =5). 
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
        print("Voce encerrou o jogo! Ate a proxima.")
        exit()
    else:
        enforcado()

enforcado()
