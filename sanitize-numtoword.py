def create_numero_list():
    numero = [] # list of numero
    for i in range(0, 201):
        numero.append(i)
    return numero

def num_por_extenso(num):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['cem', 'cento', 'duzentos']  # 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos'

    if num < 10:
        return unidades[num]
    elif num < 20:
        return dezenas1[num - 10]
    elif num < 100:
        dezena, unidade = divmod(num, 10)
        if unidade == 0:
            return dezenas2[dezena - 2]
        else:
            return dezenas2[dezena - 2] + ' e ' + unidades[unidade]
    elif num == 100:
        return centenas[0]
    else:
        centena, resto = divmod(num, 100)
        if resto == 0:
            return centenas[centena]
        else:
            if resto < 10:
                return centenas[centena] + ' e ' + unidades[resto]
            elif resto < 20:
                return centenas[centena] + ' e ' + dezenas1[resto - 10]
            else:
                dezena, unidade = divmod(resto, 10)
                if unidade == 0:
                    return centenas[centena] + ' e ' + dezenas2[dezena - 2]
                else:
                    return centenas[centena] + ' e ' + dezenas2[dezena - 2] + ' e ' + unidades[unidade]

def main():
    num = int(input('\nDigite um número, entre 0 e 200: '))
    if num >= 0 and num <= 200:
        print('\nVOCE DIGITOU: ', num_por_extenso(num))
    else:
        print('\nEntrada inválida!')
    while True:
        num_input = input('\nDigite número inteiro entre 0 e 200 (ou "fim"): ')
        if num_input.lower() == 'fim':
            print('Encerrando o programa, até a próxima!')
            break
        if num_input.isdigit():
            num = int(num_input)
            if 0 <= num <= 200:
                print('\nVOCE DIGITOU:', num_por_extenso(num))
            else:
                print('\nEntrada inválida!')
        else:
            print('\nEntrada inválida! Digite um número inteiro ou "fim".')

if __name__ == '__main__':
    main()

## Ao encapsular o código dentro da função main() e usar if __name__ == '__main__': main(), garantimos que o código dentro da
#  função main() seja executado somente quando o script for executado diretamente e não quando for importado como um módulo.

