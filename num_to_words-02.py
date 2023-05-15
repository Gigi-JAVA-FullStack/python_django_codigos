## DESAFIO 02 - Gerar um programa, em Python, que:
## A) receba um numero inteiro positivo, dentro do limite 0 a 200.
## B) apresente na tela o resultado por extenso.
## C) pergunte ao usuario se deseja continuar o processo.
## D) Looping, vai exibindo os resultados parciais (positivo) ou encerrar o script (negativo).

## Testando a BIBLIOTECA, para iniciar o script primeiro INSTALL
## Biblioteca <num2words> que reverte os numeros para palavras. 
## Intalar atraves do terminal, usando o comando: $ pip install biblioteca
## Apos, primeira linha do codigo, IMPORT a biblioteca para o script: $ from MODULE import FUNCTION.

from num2words import num2words

numero_usuario = input('Digite um numero entre 0 e 200: ')
num_ptbr = num2words(numero_usuario, lang='ptbr')
print(f'Voce digitou: {num_ptbr}')
print('Imprimindo resultado biblioteca.')
print('etapa testes num2words')

## Testando cria listas com o FOR IN RANGE // num = list(range(0, 201))
## Declarar a variavel NUMERO, que sera uma LISTA vazia
## Preencher a LISTA usando o looping FOR IN funcao RANGE(), para iterar sobre cada número inteiro 
## A variavel NUMERO vai receber o intervalo de inteiros 0 a 200 (inclusive)
## Lembrar que a funcao RANGE() ignora o ultimo valor do intervalo, pois isso se faz necessario 201.

numero = []
for i in range(0, 201):
    ## A cada iteração do loop FOR IN RANGE, a variavel NUMERO recebe dentro da LISTA mais um numero
    ## usando o método APPEND() -> object to the end of the list
    numero.append(i)


## INICIO PROGRAMA - ## DESAFIO 02:
## Declarar as variaveis que recebem os INPUTs do USER
## A funcao INPUT vai converter a entrada STRING em inteiro utilizando a funcao INT.
## Declarar as variaveis que recebem os valores para converter em palavras (num por extenso). 

## INICIO:
## Definir a funcao DEF chamada NUM_POR_EXTENSO que recebe o argumento NUM.
def num_por_extenso(num):

    ## Declarar as listas que recebem os nomes dos numeros, (indices serao utilizados na logica).
        ## lista de UNIDADES -> representa os nomes dos números de 1 dígito.
        ## lista de DEZENAS 1 simples  -> representa os nomes dos números de 10 a 19 (inclusivo).
        ## lista de DEZENAS 2 composta -> representa os nomes dos múltiplos de DEZ de VINTE a NOVENTA.
        ## lista de CENTENAS -> representa os nomes das centenas de 100 a 200 (podendo ir ate 900).

    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['cem', 'cento', 'duzentos'] ## 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos'

## Ao descompactar a LISTA -> retornada nas variáveis DEZENA e UNIDADE, assim o programa é capaz
## de extrair as DEZENAS (simples e composta) e as UNIDADES para o argumento NUM.
## Depois, pode usá-los nas declarações ESTRUTURAS DE REPETICAO (condicional) subsequentes para 
## determinar a representação textual correspondente do número digitado pelo usuario.
## ESTUDANDO PYTHON:
## Extraindo a unidade: ## unidade = numero % 10
## Eliminando a unidade de nosso número: ## numero = (numero - unidade)/10
## Extraindo a dezena: ## dezena = numero % 10
## Resumindo, em Python, fica assim:
## numero = (numero - unidade) / 10 ## Passa de 123 pra 123-3 = 120 / 10 = 12
## dezena = numero % 10  ## dezena = 12 % 10 = 2

## IMPORTANTE (REVISAO aulas 2.grau): 
## O programa precisa saber que: 
## o DIVIDENDO pode ser qualquer valor REAL, enquanto o DIVISOR deve ser diferente de ZERO.
## DIVIDENDO é o número que é dividido. O número do qual o dividendo é dividido é chamado de DIVISOR. 

## 1) Se NUM for menor que 10, a função retorna o nome correspondente (index) da lista de UNIDADES.
    if num < 10: 
        return unidades[num] ## NUM esta na posicao número do indice de UNIDADES.
## 2) Se NUM estiver entre 10 e 19 (INCLUSIVE), a função retorna o nome correspondente da lista DEZENAS1.
    elif num < 20:
        return dezenas1[num - 10] ## [NUM - 10] resulta no local do INDICE na lista DEZENAS1.
## 3) Se NUM estiver entre 20 e 99 (INCLUSIVE), a função determina a casa das DEZENAS e UNIDADES do número.
## Por exemplo, SE ENTAO a variavel NUM receber 56, entao a lista: DEZENA seria 5 .and. a UNIDADE seria 6.
    elif num < 100:
        dezena, unidade = divmod(num, 10) ## DIVMOD(87, 10) return: NUM 87 // DIV 10 = 8,7 (8 dezena, 7 unidade). 
        ## A função DIVMOD() recebe dois ARGUMENTOS, NUM (dividendo) e o numero 10 (divisor),
        ## e retorna uma LISTA contendo dois valores:
            ## o QUOCIENTE (o resultado da divisão inteira entre NUM e 10)
            ## o RESTO (o resultado de a operação do módulo % entre NUM e 10).
## Nesse caso, DIVMOD(NUM, 10) é chamado com NUM como dividendo e 10 como divisor. 
## A função DIVMOD() realiza a divisão inteira de NUM por 10 e retorna uma TUPLA contendo o QUOCIENTE e o RESTO.
    ## EXEMPLO: Suponha que tenhamos NUM recebendo 87. 
    # Entramos no bloco elif porque 87 é menor que 100.
    ## elif num < 100:
        ## dezena, unidade = divmod(num, 10)
        # Aqui, num = 87
        # divmod(87, 10) return (8, 7) -> onde 8 é o quociente (DEZENA) e 7 é o resto (UNIDADE)
        # Então, dezena = 8 e unidade = 7
## A TUPLA resultado (8, 7) significa que o quociente DEZENA é 8 (que representa a casa das dezenas de 87)
## e o resto UNIDADE é 7 (que representa a casa das unidades de 87).
## Após a chamada da função DIVMOD(), o código pode utilizar as variáveis da lista DEZENA e UNIDADE 
## para continuar processando o número de acordo com a lógica desejada, no laco de repeticao IF ELSE, abaixo:
        
# Se a posição das unidades for 0, podemos acessar diretamente o nome da dezena correspondente
        if unidade == 0: ## se a dezena é 3 (indice de 40), [dezena - 2] == [1] -> indice de 30 (trinta) lista DEZENA2.
            return dezenas2[dezena - 2]
        ## EXPLICACAO:
        # SE a posição das UNIDADE for ZERO, retorna o nome correspondente da lista dezenas2.
        ## Como: subtraindo 2 de dezena, assim, o código alinha o índice corretamente para acessar o nome
        ## das dezenas correspondente na lista de dezenas2. Por exemplo, quando dezena é 3, dezena - 2 seria 1. 
        ## Assim, acessamos o elemento de INDICE [1] na lista dezenas2, que corresponde à string 'TRINTA'.
        ## O objetivo de subtrair 2 é alinhar o índice com a posição correta do nome das DEZENAS
        ## correspondentes na lista DEZENAS2 (composta).
        ## Suponha que dezena seja 3, se usarmos diretamente dezena como o índice para acessar a lista dezenas2,
        ## isso levaria a um resultado incorreto porque os índices da lista começam em 0.
        ## No entanto, os valores na lista dezenas2 começam em 20, ao subtrair 2 de dezena, ajustamos o índice
        ## para corresponder à posição correta na lista de dezenas2.
        
## Senao, se a posição das unidades não for 0, concatenamos o nome das dezenas + e o nome das unidades.
        else:
        # SENAO, caso contrário, combina os nomes das DEZENAS e UNIDADES com a conjunção 'E' (+ concatenação).
            return dezenas2[dezena - 2] + ' e ' + unidades[unidade]
        
## 4) Se NUM for exatamente 100, a função retorna o nome 'cem', no indice 0, da lista de CENTENAS.
## Essa lógica garante que a função manipule corretamente os números:
## no intervalo de 100 a 999, dividindo o número restante em dezenas e unidades e combinando-os com o nome de CENTENA apropriado.

## Este bloco de código é executado quando o número de entrada (NUM) é maior ou igual a 100.
## Trata o caso em que o número está no intervalo de 100 a 200 (inclusive podemos ir ate 999).
    elif num == 100:
        return centenas[0]
## 5) SENAO, caso contrario, se o NUM for maior que 100, a função determina a casa das CENTENAS em (centena)
    ## e o resto (resto) depois de dividir por 100.
    else:
        centena, resto = divmod(num, 100) ## divmod(180, 10) return: num 180 // div 10 = 18,0 (18 dezena, 0 unidade).
        ## Para (18 dezena -> novamente: num - 10 resulta no local do INDICE em dezenas e unidades.) 
        ## Em programação Python, eliminando a dezena do número original, fica a centena:
        ## numero = (numero - dezena)/10
        ## centena = numero
        
        if resto == 0: ## Se o RESTO for ZERO, retorna o nome correspondente da lista de CENTENAS.
            return centenas[centena]
        ## Se o RESTO for menor que 10, combina o nome da casa das CENTENAS, 
        ## com a conjunção 'E' (+ concatenação) com o nome da casa das UNIDADES.
        else:
            if resto < 10:
                return centenas[centena] + ' e ' + unidades[resto]
            ## SE o restante estiver entre 10 e 19 (INCLUSIVE) combina o nome da casa das CENTENAS, 
            ## com a conjunção 'E' (+ concatenação) e o nome do número da lista DEZENAS1.
            elif resto < 20:
                return centenas[centena] + ' e ' + dezenas1[resto - 10]
            ## SENAO, caso contrário, ele determina a posição das DEZENAS e UNIDADES 
            ## do restante (RESTO) e combina os nomes de acordo.
            else:
                dezena, unidade = divmod(resto, 10)
                ## dezena, unidade = divmod(resto, 10): 
                # A função DIVMOD() é usada para dividir o número restante (RESTO) por 10 
                # e retornar tanto o QUOCIENTE (dezena) quanto o RESTANTE (unidade). 
                # Esta operação separa a casa das DEZENAS e UNIDADES do número restante.
                if unidade == 0:
                    return centenas[centena] + ' e ' + dezenas2[dezena - 2]
                ## Se UNIDADE == 0: significa que se o resto (unidade) for 0, 
                # o número restante (RESTO) é um múltiplo de 10 (por exemplo, 100, 200, 300 etc.). 
                # Neste caso, a função retorna a concatenação do nome da centena correspondente
                #  (centenas[centena]) + com o nome da casa das dezenas (dezenas2[dezena - 2]), 
                # indicando que não há unidades presentes.
                
                else:
                ## Se o resto (unidade) NAO for 0, significa que há unidades presentes no número restante.
                    return centenas[centena] + ' e ' + dezenas2[dezena - 2] + ' e ' + unidades[unidade]
                ## Neste caso, a função retorna a concatenação do nome da centena correspondente 
                # (centenas[centena]), o nome de o lugar das dezenas (dezenas2[dezena - 2]), 
                # e o nome do lugar das unidades (unidades[unidade]) e, para uma representação completa,
                # concatena com 'E' entre as palavras. 

## BLOCO PRINCIPAL ##
## primeiro IDENTIFICADOR = segundo COERCAO DO TIPO(terceiro funcao INPUT(msg: string que aparecera na tela))
num = int(input('Digite novamente um número, entre 0 e 200: '))
# Bloco condicional, IF ELIF ELSE,
# se a entrada não for um número inteiro válido, uma mensagem de ERRO será impressa na tela.
if num >= 0 and num <= 200:
    print('Voce digitou: ', num_por_extenso(num))
    ## SE o usuário informar um número inteiro válido de 0 a 200 (INCLUSIVE), o código chama
    ## a função num_por_extenso para converter o número em sua representação textual.
    ## A string retornada é então impressa no console.
    print('etapa1, antes do LOOP, bloco principal')
    print()
else:
    print('Entrada inválida!')
    ## Se o usuário inserir um número inválido (fora do intervalo ou não for um número inteiro), 
    ## uma mensagem de erro será impressa no console.
    print('etapa2, antes do LOOP, bloco principal')
    print()
# O loop (abaixo) vai repetir a partir da etapa 3, solicitando ao usuário uma NOVA entrada ou a opcao de FIM.

## LOOPING INFINITO ##
## Usando verificações condicionais e o metodo booleano -> STR.ISDIGIT() 
## para determinar se a entrada é um número inteiro válido.
## Inicia um loop WHILE que continua a executar indefinidamente.
while True:
    # Dentro do loop, pedimos ao usuário para inserir um número usando a função INPUT().
    num_input = input('Digite um número inteiro entre 0 e 200 (ou "fim"): ')
    if num_input.lower() == 'fim':
        print('Encerrando o programa, ate a próxima!')
    ## Se o usuário inserir a string "fim", o loop será encerrado usando a instrução break.
        break
## O método STR.ISDIGIT() é usado para verificar se a string de entrada consiste apenas em dígitos,
## indicando que pode ser convertido em um número inteiro sem gerar uma exceção.
    if num_input.isdigit():
        num = int(num_input)
    ## Se a entrada for um número inteiro válido, o programa vai converter NUM_INPUT em NUM e, 
    ## em seguida, verificado as condicoes IF ELSE, em relação ao intervalo válido, 
    ## repetindo as vericacoes e print no console.
        if 0 <= num <= 200:
            print('Voce digitou:', num_por_extenso(num))
            print('etapa3.1, LOOPING, bloco principal')
        else:
            print('Entrada inválida!')
            print('etapa3.2, LOOPING, do bloco principal')
    else:
        print('Entrada inválida! Digite um número inteiro ou "fim".')
        print('etapa3.3, LOOPING, do bloco principal')
