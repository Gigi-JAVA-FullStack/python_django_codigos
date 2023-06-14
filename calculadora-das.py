import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def divmod(a, b):
    if b != 0:
        return a % b
    else:
        return "Erro: divisão por zero!"

# Function to check if the user wants to continue
def ask_continue():
    resposta = input("Deseja continuar? (s/n): ")
    return resposta.lower() == 's'

# Main code global variables
def main():
    while True:

        print('''\nDigite a operacão desejada:
        1 -> Soma
        2 -> Subtracão
        3 -> Multiplicacão
        4 -> Divisão
        5 -> Modulo da Divisão''')

        prompt_user = input("\nEscolha uma opcao (1-5): ")
        if prompt_user in ["1", "2", "3", "4", "5"]:
            user_number1 = int(input("Digite um numero: "))
            user_number2 = int(input("Digite outro numero: "))
                
            if prompt_user == '1':
                print(f'\nNumero {user_number1} + {user_number2} =  {add(user_number1, user_number2)}')
            elif prompt_user == '2':
                print(f'\nNumero {user_number1} - {user_number2} =  {subtract(user_number1, user_number2)}')
            elif prompt_user == '3':
                print(f'\nNumero {user_number1} * {user_number2} = {multiply(user_number1, user_number2)} ')
            elif prompt_user == '4':
                print(f'\nNumero {user_number1} / {user_number2} = {divide(user_number1, user_number2)} ')
            elif prompt_user == '5':
                print(f'\nNumero {user_number1} % {user_number2} = {divmod(user_number1, user_number2)} ')
        else:
            print("Opcao invalida!")

        if not ask_continue():
            break

if __name__ == '__main__':
    main()

