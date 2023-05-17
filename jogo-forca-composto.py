## DESAFIO 03 "JOGO DO ENFORCADO ## 
## O programa eh amigavel, imprime feedback positivo sobre todos os palpites corretos. 
## No geral, o trecho final do código lida com a lógica (condicoes) relacionada à verificação da
## exatidão da LETRA adivinhada (ou nao) e fornece FEEDBACKs apropriados ao jogador.
## O programa oferece feedback negativo: "Letra errada!" para indicar que a letra escolhida
## não faz parte da palavra randomica. A variavel TENTATIVAS recebe -= 1 (DECREMENTO),
## as tentativa diminuem em 1 passo a cada LOOPING (ate chegar ao condicao limite >0 =5). 

import random

def enforcado():
    lista = ["banana", "laranja", "morango", "maracuja", "caju", "abacaxi", "jaca", "manga",
            "abacate", "goiaba", "carambola", "kiwi", "coco", "tomate"]

    print('\n+++++++++++++++++++++++++++++++++++++')
    print("  Bem-vindo ao 'Jogo do Enforcado'!")
    print('+++++++++++++++++++++++++++++++++++++\n')

    escolha_jogar = input("\nMENU: Escolha '1' para o PROGRAMA escolher a palavra ou '2' para VOCE digitar sua ecolha: ").lower()
    if escolha_jogar == '1':
        escolha_usuario = random.choice(lista)
## CHOICE() choose a random word (element) from a non-empty list (sequence).
    elif escolha_jogar == '2':
        escolha_usuario = input("Escolha e, por favor, use UNDERLINE (_) entre as palavra: ").lower()
    else:
        print("Invalido. Por favor, tente novamente, digite 1 ou 2 e vamos jogar...")
        return
    letra_adivinhou = []
    tentativas = 5

    print("Voce tera", tentativas, "tentativas para adivinhar a palavra escondida, ok?")
    print("Nesta rodada a palavra escolhida tem", len(escolha_usuario), "letras. Vamos comecar?")
    print()

    while tentativas > 0:
        palavra_escondida = ""
        for letra in escolha_usuario:
            if letra in letra_adivinhou:
                palavra_escondida += letra
            else:
                palavra_escondida += "_"
                print(palavra_escondida)
        print("\nPalavra:", palavra_escondida)
        print("Numero de tentativas restantes:", tentativas)
        print()
        if palavra_escondida == escolha_usuario:
            print("Uepa! Voce adivinhou a palavra corretamente.\n")
            break
        adivinhando_letra = input("Digite uma letra:").lower()
        print()
        if adivinhando_letra.isalpha() and len(adivinhando_letra) == 1 and adivinhando_letra != (" ", ""):
            if adivinhando_letra in letra_adivinhou:
                print("Voce ja adivinhou esta letra...")
            elif adivinhando_letra in escolha_usuario:
                print("Oba, voce acertou a letra!")
                letra_adivinhou.append(adivinhando_letra)
            else:
                print("Que pena, tentativa errada!")
                tentativas -= 1
                ## Lembrando que a variavel LETRA_ADIVINHOU era uma variavel VAZIA...
                letra_adivinhou.append(adivinhando_letra)
        else:
            print("Invalido! Por favor, digite apenas uma letra, ok?.")
    else:
        print("Como dizem: \'GAME IS OVER!' Voce usou as 5 tentativas do jogo.")
        print("A palavra escolhida era:", escolha_usuario)
    # No final existe a opcao do programa REINICIAR, atraves do LOOP da variavel "play_again".
    print('+++++++++++++++++++++++++++++++++++++')
    play_again = input("Deseja jogar novamente? (s/n): ")
    if play_again.lower() != 's':
        print("Voce encerrou o jogo! Ate a proxima.")
        exit()
    else:
        enforcado()

enforcado()
