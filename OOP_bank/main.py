import Classes
from time import sleep


def validate_int (receptor, key, pergunta):
    
    while True:
        receptor[key] = input (pergunta).strip()
        if receptor[key].isdigit() and len(receptor[key]) == 4:
            break
        else:
            print('Error')
    return receptor[key]




def menu ():
    print(""" 
            BANCO
        
        1 - Cadastrar conta 
        2 - Login em conta existente 
        3 - Sair  

        """)


def cadastrar_conta ():
    usuarios.append (dict())
    index = len(usuarios) - 1
    usuarios [index] ['Nome'] = input ('Digite o nome do dono da conta: ')
    usuarios [index] ['Agencia'] = validate_int( usuarios [index], 'Agencia' , 'Digite o numero da agencia de cadastro [4 digitos]: ' )
    usuarios [index] ['Conta'] = validate_int( usuarios [index], 'Conta' , 'Digite o numero da conta de cadastro [4 digitos]: ' )

    usuarios [index] ['Saldo'] = input ('Digite o valor do deposito inicial: ')
    usuarios [index] ['Tipo'] = input ('Digite o tipo de conta [Poupanca ou Corrente]: ').lower().strip()
 
    return usuarios




def menu_login():
    print ()
    print('     Login')
    print()
    agencia = input ('  Agencia: ')
    conta = input ('  Conta: ')
    tipo = input ('  Tipo da conta [Poupanca ou Corrente]: ').lower().strip()
    return agencia, conta, tipo

def login (menu):
    agencia, conta, tipo = menu()

    cliente = None
    for index in usuarios:
        if index['Agencia'] == agencia and index['Conta'] == conta and index['Tipo'] == tipo:
            cliente = index

    if cliente == None:
        print ('    Cliente não encontrado no banco de dados')
        sleep (0.8)

    else:
        if cliente['Tipo'] == 'corrente':
            usuario = Classes.Corrente (cliente['Nome'], cliente['Agencia'], cliente['Conta'], cliente['Saldo'])
    
        else:
            usuario = Classes.Poupanca (cliente['Nome'], cliente['Agencia'], cliente['Conta'], cliente['Saldo'])
        
        while True:
            print()
            print(f'    Nome: {usuario.nome}')
            if usuario.limite == 0:
                print('    Conta poupança')
            else:
                print('    Conta Corrente')
                print(f'    Limite = {usuario.limite}')
            print(''' 
        1 - visualizar informações da conta 
        2 - Depositar
        3 - Sacar
        4 - Sair da conta
                ''')
            op = input ('Digite sua escolha [1~4]: ')

            if op == '1':
                print()
                print(f'  Nome : {usuario.nome}')
                print(f'  Agencia : {usuario.agencia}')
                print(f'  Conta: {usuario.conta}')
                print(f'  Saldo : {usuario.saldo}')
                print(f'  Limite : {usuario.limite}')
                print()
        
            elif op == '2':
                print()
                print(f'Saldo atual: {usuario.saldo}')
                print()
                valor = float(input ('Digite o valor a ser depositado: '))
                usuario.deposito(valor)
                print('Deposito realizado com sucesso !')
                print(f'Saldo: {usuario.saldo}')
                
          

            elif op == '3':
                print()
                print(f'Saldo atual: {usuario.saldo}')
                print()
                valor = float(input ('Digite o valor a ser sacado: '))
                usuario.saque(valor)
                print(f'Saldo: {usuario.saldo}')
              
            elif op == '4':
                print()
                print('Voce saiu da conta')
                break

            else:
                print('Escolha invalida')
      



if __name__ == "__main__":
    usuarios = list ()

    while True:

        menu()
        resp = input ('Digite sua escolha [1~3]: ')

        if resp == '1':
            usuarios = cadastrar_conta()
        
        elif resp == '2':
            login (menu_login)


        elif resp == '3':
            print('Saindo do app BANCO ...')
            sleep (1)
            break

        else:
            print('Escolha invalida')
            

