import random 
import re # module re (suport for regular expression)
import unicodedata # biblioteca para comparar palavras sem acentos

## função unicodedata.normalize() é usada para normalizar a STRING adivinha.
def remover_acento(adivinha): ## Funcao sera CHAMADA retorna o parametro linha 27
    adivinha = unicodedata.normalize('NFD', adivinha) ## NFD: normalização será feita utilizando a forma de decomposição canônica (ou seja, forma mais basica)
    adivinha = adivinha.encode('ascii', 'ignore').decode('utf-8') ## encode() BYTES, decode() STRING é decodificada novamente para UTF-8, voltando a ser uma string.
    ## utiliza codificação ASCII + ignore: caracteres que não são representáveis na codificação ASCII.
    return adivinha

## função útil para normalizar e limpar palavra antes de comparar ou processar.
def limpa_palavra(adivinha): ## Funcao sera CHAMADA retorna o parametro linha 55 e 89
    adivinha = remover_acento(adivinha) # chamada da funcao REMOVER_ACENTO(string advinha como parametro), retorna a mesma string, mas com os acentos removidos).
    adivinha = re.sub(r'[^A-Za-z-%&*]', '_', adivinha) ## Regex #Função re.sub do módulo re para substituir (sub) padrões em uma string. # notação r'(string bruta/raw string) Python
    return adivinha.lower()

def enforcado():

    lista_programa = ["banana", "mamão-papaia", "limão siciliano", "laranja", "morango", "maracujá", 
                      "castanha de caju", "abacaxi", "jaca", "manga", "abacate", "goiba", "carambola", "kiwi", "coco", "tomate"]
    print('\n+++++++++++++++++++++++++++++++++++++')
    print("  Bem-vindo ao 'Jogo do Enforcado'!")
    print('+++++++++++++++++++++++++++++++++++++\n')
    print("Vamos adivinhar palavras ou frases!")
    print()
## ESTRUTURA DE REPETICAO ##
    while True: 
        print("Primeiro escolha uma opcao no \nMENU:")
        print("1 -> Deixar o programa escolher a palavra/frase.")
        print("2 -> Voce vai digitar a sua propria palavra/frase.")
        print("3 -> Sair do jogo.")

        menu_escolhido = input("Digite a sua escolha, vamos de 1, 2 ou 3?...: ")
        ## ESTRUTURA DE SELECAO ##
        if menu_escolhido == "1":
            opcao_usuario = random.choice(lista_programa)
            copia_opcao_usuario = opcao_usuario[:]
            opcao_usuario = limpa_palavra(opcao_usuario)
            print("O programa escolheu a palavra/frase para adivinhar, vamos jogar.")
            break ## LOOP sera interrompido, saira, não executa restante iteracoes.
        elif menu_escolhido == "2":
            opcao_usuario = input("Digite sua palavra/frase a ser adivinhada: ")
            copia_opcao_usuario = opcao_usuario[:]
            opcao_usuario = limpa_palavra(opcao_usuario)
            print("Voce escolheu a sua palavra/frase para adivinhar, vamos jogar.")
            if opcao_usuario == "": ## se escolher 2, mas nao digitar nada...
                print("Invalido! Por favor, digite a palavra/frase.")
                continue ## pula, vai para a próxima iteração DENTRO do loop.
            break ## loop vai interromper (aceitar a palavra/frase digitada). 
        elif menu_escolhido == "3":
            print("Voce encerrou o jogo! Ate a proxima jogada!")
            return
        else: ## SE todas as opoes anteriores forem FALSE, entao...
            print("Escolha invalida! Por favor, digite a opcao do MENU: 1, 2 ou 3.")
    
    letra_adivinhou = []
    tentativa_maximo = 5
## estrutura REPETICAO com VARIAVEL DE CONTROLE ##  
    while tentativa_maximo > 0: ## ENQUANTO for TRUE variavel tentativa > 0 =5:
        palavra_escondida = ""
        for letra in opcao_usuario: ## PARA cada letra EM opcao_usuario: FACA (execute a estrutura selecao IF ELIF ELSE) ##
            if letra in letra_adivinhou: ## IF TRUE THEN
                palavra_escondida += letra
            elif letra == " ":
                palavra_escondida += " "
            else:
                palavra_escondida += "_"
        print(palavra_escondida)
        ## print("A palavra/frase escondida: ", copia_opcao_usuario)
        print(f'Restam {tentativa_maximo} tentativa(s).')
        print()

        if palavra_escondida == opcao_usuario: ## IF TRUE
            print("Wow! Voce adivinhou a palavra/frase corretamente!")
            break ## loop interrompido, codigo saira, não executando restante iteracoes. 
        adivinhando_letra = input("Digite apenas UMA letra: ")
        adivinhando_letra = limpa_palavra(adivinhando_letra) ## chamando a FUNCTION 

        if adivinhando_letra == "":
            print("Invalido! Por favor, digite apenas UMA letra, ok?")
            continue ## pula, vai para a próxima iteração dentro deste loop. 

        if adivinhando_letra in letra_adivinhou:
            print("Voce ja adivinhou esta letra... Vamos tentar outra: ")
        elif adivinhando_letra in opcao_usuario:
            print("Oba, voce acertou a letra!")
            letra_adivinhou.append(adivinhando_letra)
        else:
            print("Que pena, invalido e perdeu uma tentativa.")
            tentativa_maximo -= 1
            letra_adivinhou.append(adivinhando_letra)
    else: 
        print("Como dizem: \'GAME IS OVER!' Voce usou todas as tentativas.")

    print("\nA palavra escolhida era:", copia_opcao_usuario)
    play_again = input("Deseja jogar novamente? (s/n): ")
    if play_again.lower() == 's':
        enforcado()
    else:
        print("Voce encerrou o jogo do ENFORCADO! Ate a proxima!")

enforcado()
