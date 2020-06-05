from random import randint

while True:
    def penultimos_digitos (cpf):
        y = 0
        soma1 = 0
        digito1 = 0 # Digito 1
        for d in range(10,1,-1):
            soma1 += (d * int(cpf[y]))
            y += 1
        y = 0
        digito1 = 11 - (soma1 % 11) 
        if digito1 > 9:
            digito1 = 0

        soma2 = 0
        digito2 = 0  # Digito 2
        for d in range(11,2,-1):
            soma2 += (d * int(cpf[y]))
            y += 1
        soma2 += (2 * digito1)
        digito2 = 11 - (soma2 % 11) 
        
        if digito2 > 9:
            digito2 = 0

        return digito1, digito2

    x = 0
    cpf = str ()
    while x < 9:
        cpf += str (randint(0, 9))
        x += 1
    digito1, digito2 = penultimos_digitos(cpf)

    cpf += str(digito1)
    cpf += str(digito2)

    print('=' * 30)
    print(         'GERADOR DE CPF')
    print('=' * 30)
    print(f'CPF = {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
    print('=' * 30)
    resp = str (input('Deseja gerar outro CPF [S/N]? ')).upper()
    if resp[0] == 'N':
        print('PROGRAMA ENCERRADO')
        break

