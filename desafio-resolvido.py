# 39784835134
storage_cpf = [] 
# cria uma lista vazia para armazenar os números 
 
cpf_user = input('Digite números de CPF (sem traço ou ponto): ')
# entrada CPF do STRING (INTERAVEL)
 
cpf_user = cpf_user.replace(".", "").replace("-", "")
# caso haja, vai sanitizer  pontos e traços
 
cpf_str = str(cpf_user)
 
cpf_lista = []
# cria uma nova lista para armazenar os dígitos do CPF como inteiros
 
for digito in cpf_str:
    digito_int = int(digito)
    # converte o número do CPF em uma lista de numeros inteiros.
    cpf_lista.append(digito_int)
    # adiciona o dígito à nova lista de cpf (que estava vazia)

# adiciona cada dígito do CPF na lista Bd 
storage_cpf.extend(cpf_lista)
print(storage_cpf) 
 
# calcula o primeiro dígito verificador
contador = 0
resultado = 0
controlador = 10
 
for numero in storage_cpf[:9]:
    resultado = numero * controlador
    contador += resultado
    controlador -= 1
    
contador = ((contador * 10) % 11)
 
if contador == 10:
    contador = 0
 
if contador == storage_cpf[9]:
    contador = contador
else:
    print('CPF inválido!')
    exit()

storage_cpf.append(contador)
# adiciona o primeiro dígito verificador à lista 
 
# calcula o segundo dígito verificador
acumulador2 = 0
resultado2 = 0
controlador2 = 11
 
for numeros in storage_cpf[:10]:
    resultado2 = numeros * controlador2
    acumulador2 += resultado2
    controlador2 -= 1
 
acumulador2 = ((acumulador2 * 10) % 11)
 
if acumulador2 == 10:
    acumulador2 = 0
 
if acumulador2 == storage_cpf[10]:
    print('CPF válido!')
else:
    print('CPF inválido!')