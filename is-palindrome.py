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

# Function to check if the user wants to continue
def ask_continue():
    play_again = input("Deseja jogar novamente? (s/n): ")
    return play_again.lower() == 's'

def main():
    while True:
        sentence = input("\nDigite a sentenca: ")
        result = encontra_palindromes(sentence)
        if result:
            print("Palindrome foi encontrado: ")
            for palavra in result:
                print(palavra)
        else:
            print("Nenhum palindrome encontrado.")

        if not ask_continue():
            print("Voce encerrou o jogo! Ate a proxima!")
            break

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

