# CONCLUSOES:

## 1.1 A STRING nao pode ser vazia
## 1.2 Precisa ter no minimo 2 caracteres distintos (atendendo ao conceito de conjunto)
## 1.3 NAO podemos obter um palindrome com numero de casas menor do que 3  
## 1.4 Formatar os caracteres - talvez Python faca diferenca, pois para ser Palindrome NAO FAZ DIFERECA misturar letras (maiuscula e minuscula).
## 1.5 Precisa checar na expressao as LETRAS e NUMEROS (??descobrir como fazer para remover caracteres nao alfanumericos) 
## 1.6 O chamado SANITIZAR | NORMALIZAR, usar o metodo de EXPRESSAO REGULAR (?? descobrir como fazer??)
## 1.7 Duvida: sera que seria interessante checar total de caracteres para ver se eh PAR ou IMPAR () % ) ??
## 1.8 Para melhor explicar ao usuario, O código inclui algumas instruções de impressão (print) que ajudam a entender 
## 1.9 FLUXO do programa eh AMIGAVEL ao usuario e util para DEPURACAO.  

## TUDO EM PYTHON EH UM OBJETO, GERALMENTE DENTRO DOS OBJETOS TEMOS METODOS!
## OS METODOS SAO ACOES -> OBJETOS SAO ACOES (PODEM FAZER ALGUNS ACOES)

## INDENTIFICADOR : BLOCO CONDICAO (em Python nao existe nda que defina fim do modulo ou ponto e virgula)
## MODULO -> DEF
def testando_palindrome():
    global expressao_teste

## Expressao escolhida: ## "Socorram-me, subi no ônibus em Marrocos."

    expressao_teste = "SOCORRAM ME SUBI NO ONIBUS EM MARROCOS" 
    print('2. Testando: a expressao e a condicao do bloco (logica) -> ', expressao_teste)
    
    testando_fatiamento = expressao_teste
    print(testando_fatiamento[::-1])
    print()

## Bloco de codigo para verificar as extremidades da expressao: INICIO [0] e FIM [-1]
## INICIO -> positivos 0123456789  FIM -> negativos -987654321
    if(testando_fatiamento[0] != testando_fatiamento[-1]):

## Entao, aqui o algorithmo deveria (poderia ser) um palindrome
        print('3. A expressao tinha todas as condicoes para, mas, infelizmente nao eh um PALINDROME.')
        return False
    else: testando_fatiamento = testando_fatiamento[1:-1]
        
## Todas as condicoes foram FALSE, sera executada a condicao acima mencionados.  
    print('3. Apos verificaco, a expressao eh um PALINDROME!')   
    return True

## BLOCO PRINCIPAL - PALINDROME ESCOLHIDO PARA TESTES
expressao_teste = "STRING vazia!"
print('1. Comecamos o teste sem nenhuma expressao escolhida, ', expressao_teste)
print()

answer_modulo_testando = testando_palindrome()
print(f'4. Quando testei, {expressao_teste}, a expressao o resultado foi -> ', answer_modulo_testando)
print()

## TESTANDO

palin1 = 'OMO'
palin1 = (len(palin1) % 2 == 0)
print(palin1)

palin2 = "HANNAH"
check = (palin2 == palin2[::-1])
print(palin2)

## Conceito de conjunto (SET) para verificar se há caracteres distintos na STRING.
## Converte a STRING para minúsculas (ou maiuscula, padronizando a expressao) 
## Usar a funcao LEN para retornar a quantidade de caracter da STRING

## PRINCIPAIS METODOS PARA MANIPULACAO DO TIPO LIST DESCRICAO
## append()  adiciona um elemento ao final da lista
## clear()   remove todos os elementos da lista
## copy()    retorna uma copia da lista
## count()   retorna o numero de vezes em que o elemento aparece na lista
## extend()  adiciona os elementos de uma lista ou iteravel ao final da lista
## index()   retorna o indice do primeiro elemento igual ao valor especificado
## insert()  insere o elemento na posicao especificada
## pop()     remove e retorna o elemento da posicao especifica, se nao for especificado um indice, remove e retorna o ultimo elemento da lista
## remove()  remove o primeiro elemento igual ao valor especificado
## reverse() inverte a ordem dos elementos na lista
## sort()    ordena os elementos da lista em ordem ascendente (quando comparaveis e mesmo tipo, parametro REVERSE=TRUE, ordena descendente)  
"""""

## import re
## def lendo_palindrome(str):
    ## Função comeca verificando se a ENTRADA é de fato uma STRING e, caso contrário, levanta um ERRO..
    ## NAO SEI COMO FAZER analise de ERRO 
    # if not str (expressao_usuario):
    # print(ERRO)

    ## BLOCO DE CONDICAO para verificar as condicoes MINIMAS da expressao, possibilita ser um PALINDROME 
    size = len(str)
    if (size == 0) or (size < 2) or (len(expressao_teste) < 3):
        return False
    
    ## Expressao Regular | Sanitizar - ESTA LINHA DE CODIGO EU (ainda) NAO ENTENDI, fonte livro
    ##str = re.sub('[^a-za-Z0-9]+','', (normalize('NFKD', str)).encode('ASCII','ignoner').decode('ASCII').lower)
    new_size = len(str)
    
    ## RODRIGO ENSINOU -> Como resolver o ponto de "sanitizacao" !!!
    ## import string
    ## from unidecode import unidecode

    ## text = "Socorram-me, subi no ônibus em Marrocos"
    ## text_lower = text.lower()
    ## text_with_no_ponctuations = text_lower.translate(str.maketrans('', '', string.punctuation))
    ## text_with_no_accents = unidecode(text_with_no_ponctuations)
    ## clean_text = text_with_no_accents.replace(' ', '')

    ## Usar BLOCO DE CONDICAO -> FOR auxiliar IN dentro RANGE da variavel MODULO_ANALISE que recebeu o parametro
    for i in range(0, new_size // 2):
        if str[i] != str[new_size: - i: -1]: ## Condicao do bloco, encontrei DIFERENCA parar de rodar 
            return False
    return True
"""
