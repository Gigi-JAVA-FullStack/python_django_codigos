## SANITIZE CODE: Este código foi refatorado
## 1) def main(): funcao que chama todas as outras e realiza a lógica MAIN.
## 2) Função chamada def sanitize_cpf(cpf): sanitiza o CPF string removendo pontos e tracos. 
## 3) Função chamada def convert_cpf_list(cpf): converter CPF STRING em uma list[] de INTEGERS.
## 4) Função chamada def validate_cpf(cpf_list): validar cpf usando a primeira e segunda verificacao de DIGITOS -> Return = True if CPF = is valid, else, Return = False.
## 5) Função chamada get_numeric_input(): solicita a entrada do usuário e valida que apenas números sejam inseridos. 
## Ele usa o método isdigit para verificar se a entrada consiste apenas em dígitos. 
## Se a entrada for inválida, o usuário será solicitado novamente até que uma entrada válida seja fornecida.
## Ao utilizar esta função, garanto que a entrada do CPF seja composta apenas por números, proporcionando melhor experiência e evitando erros no processamento posterior do CPF.

def sanitize_cpf(cpf):
    """
    Sanitizar o CPF STRING removendo pontos e tracos.
    """
    return cpf.replace(".", "").replace("-", "")

def convert_cpf_list(cpf):
    """
    Converter CPF STRING em uma list[] de INTEGERS.
    """
    cpf_list = []
    for digito in cpf:
        digito_int = int(digito)
        cpf_list.append(digito_int)
    return cpf_list

def validate_cpf(cpf_list):
    """
    Validar cpf usando a primeira e segunda verificacao de DIGITOS -> Return = True if CPF = is valid, else, Return = False.
    """
    # Calcular primeira verificacao de DIGIT.
    i = 0
    control = 10

    for number in cpf_list[:9]:
        result = number * control
        i += result
        control -= 1

    i = ((i * 10) % 11)

    if i == 10:
        i = 0

    if i != cpf_list[9]:
        return False

    # Calcular segunda verificacao de DIGIT.
    j = 0
    control = 11

    for number in cpf_list[:10]:
        result = number * control
        j += result
        control -= 1

    j = ((j * 10) % 11)

    if j == 10:
        j = 0

    if j != cpf_list[10]:
        return False
    return True

def get_numeric_input(prompt):
    """
    PROMPT USER para INPUT e VALIDACAO, apenas permite entrada de numeros. 
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("\nInvalido. Por favor, digite apenas numeros.")

def main():
    storage_cpf = []
    cpf_user_input = get_numeric_input('\nDigite números de CPF (sem traço ou ponto): ')
    cpf_user = sanitize_cpf(cpf_user_input)
    cpf_list = convert_cpf_list(cpf_user)
    storage_cpf.extend(cpf_list)

    if validate_cpf(storage_cpf):
        print('\nCPF válido!')
    else:
        print('\nCPF inválido!')

if __name__ == "__main__":
    main()
