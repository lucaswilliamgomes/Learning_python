from random import randint

def print_menu ():
    print(f'\n      CNPJ\n')
    print(' 1 - GERAR CNPJ')
    print(' 2 - VALIDAR CNPJ')
    print(f' 3 - Sair \n')

def valid_option (option):
    if option.isnumeric():
        if int(option) >= 1 and int(option) <= 3:
            return True
        else:
            return False
    else:
        False

def remove_caracteres(cnpj):
    cnpj = cnpj.replace('.','')
    cnpj = cnpj.replace(' ','')
    cnpj = cnpj.replace('/','')
    cnpj = cnpj.replace('-','')
    return cnpj

def random_numbers ():
    cnpj = ''
    for x in range(0,8):
        cnpj += str(randint(1,9))
    cnpj += '0001'
    return cnpj

def digits (cnpj,var):

    cont = 0
    soma = 0
    for x in range(var,1,-1):
        soma += (x * int(cnpj[cont]))
        cont += 1
    for x in range(9,1,-1):
        soma += (x * int(cnpj[cont]))
        cont += 1
    digit = 11 - (soma % 11)
    if digit > 9:
        digit = 0
    valid_cnpj = cnpj + str(digit)
    soma = 0
    cont = 0 
    return valid_cnpj
    
    
    



            
