
def onze_caracteres():
    if len (cpf) != 11:
        return False
    else:
        return True


def validacao (cpf):
    x = 0 
    soma1 = 0
    digito1 = 0 # Digito 1
    for d in range(10,1,-1):
        soma1 += (d * int(cpf[x]))
        x += 1
    x = 0
    digito1 = 11 - (soma1 % 11) 

    if digito1 > 9:
        digito1 = 0
    else:
        digito1 = digito1
    
    soma2 = 0
    digito2 = 0  # Digito 2
    for d in range(11,2,-1):
        soma2 += (d * int(cpf[x]))
        x += 1
    soma2 += (2 * digito1)

    digito2 = 11 - (soma2 % 11) 
    
    if digito2 > 9:
        digito2 = 0
    else:
        digito2 = digito2
    
    return digito1, digito2



while True:
    while True:
        cpf = str(input('Digite apenas os numeros do CPF: '))
        if cpf.isnumeric():
            break 
        else: 
            print('Digite o CPF sem pontos e travessão')
    print(cpf)
    if onze_caracteres():
        break
    else:
        print('O CPF precisa ter 11 numeros')
            
digito1,digito2 = validacao (cpf)

if cpf[9] == str(digito1) and cpf[10] == str(digito2):
    print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} está válido e pode ser usado!')
else:
    print(f'O CPF {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} está inválido e não pode ser usado!')


   








