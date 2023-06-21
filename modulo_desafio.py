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

import re
import unicodedata

## Amor a Roma. 
## Lava esse aval. 
## Anotaram a data da maratona. 
## A cara rajada da jararaca.
## Eva, asse essa ave!
## Olé! Maracujá, caju, caramelo!
## Socorram-me, subi no ônibus em Marrocos! 

def confirm_palindrome(palavra):
    limpando_palavra = palavra.lower().replace(" ", "")
    return limpando_palavra == limpando_palavra[::-1]

def remover_acento(adivinha):
    adivinha = unicodedata.normalize('NFD', adivinha)
    adivinha = adivinha.encode('ascii', 'ignore').decode('utf-8')
    return adivinha

def limpa_palavra(adivinha):
    adivinha = remover_acento(adivinha)
    adivinha = re.sub(r'[^A-Za-z-%&*!~]', '_', adivinha)
    return adivinha.lower()

def encontra_palindromes(sentence):
    palavras = sentence.split()
    palindromes = []
    for palavra in palavras:
        if confirm_palindrome(palavra) and remover_acento(palavra) and limpa_palavra(palavra):
            palindromes.append(palavra)
    return palindromes

def main():
    sentence = input("\nDigite a sentenca: ")
    result = encontra_palindromes(sentence)
    if result:
        print("Palindrome foi encontrado: ")
        for palavra in result:
            print(palavra)
    else:
        print("Nenhum palindrome encontrado.")

    while True:
        play_again = input("Deseja jogar novamente? (s/n): ")
        if play_again.lower() == 's':
            main()
        else:
            print("Voce encerrou o jogo! Ate a proxima!")

if __name__ == "__main__":
    main()


## BLOCO DE CONDICAO para verificar as condicoes MINIMAS da expressao, possibilita ser um PALINDROME 
##  size = len(str)
##  if (size == 0) or (size < 2) or (len(expressao_teste) < 3):
#       return False
    
## Expressao Regular | Sanitizar - ESTA LINHA DE CODIGO EU (ainda) NAO ENTENDI, fonte livro
##  str = re.sub('[^a-za-Z0-9]+','', (normalize('NFKD', str)).encode('ASCII','ignoner').decode('ASCII').lower)
##  new_size = len(str)
    
## RODRIGO ENSINOU -> Como resolver o ponto de "sanitizacao" !!!
## import string
## from unidecode import unidecode

## text = "Socorram-me, subi no ônibus em Marrocos"
## text_lower = text.lower()
## text_with_no_ponctuations = text_lower.translate(str.maketrans('', '', string.punctuation))
## text_with_no_accents = unidecode(text_with_no_ponctuations)
## clean_text = text_with_no_accents.replace(' ', '')

## Usar BLOCO DE CONDICAO -> FOR auxiliar IN dentro RANGE da variavel MODULO_ANALISE que recebeu o parametro
##  for i in range(0, new_size // 2):
##      if str[i] != str[new_size: - i: -1]: ## Condicao do bloco, encontrei DIFERENCA parar de rodar 
##          return False
#       return True

