import Classes
from time import sleep


def menu ():
    print(""" 
            BANCO
        
        1 - Cadastrar conta 
        2 - Login em conta existente 
        3 - Sair  

        """)


def cadastrar_conta ():
    usuarios.append (dict())
    print(usuarios)
    index = len(usuarios) - 1
    usuarios [index] ['Nome'] = input ('Digite o nome do dono da conta: ')
    usuarios [index] ['Agencia'] = input ('Digite o numero da agencia de cadastro [4 digitos]: ')
    usuarios [index] ['Conta'] = input ('Digite o numero da conta de cadastro [4 digitos]: ')
    usuarios [index] ['Saldo'] = input ('Digite o valor do deposito inicial: ')
    usuarios [index] ['Tipo'] = input ('Digite o tipo de conta [Poupanca ou Corrente]:').lower().strip()
 
    with open ('users', 'a+') as users:
        users.write(str(usuarios[-1]))
        users.write('\n')
    
    return usuarios




def menu_login():
    print ()
    print('     Login')
    print()
    agencia = input ('  Agencia: ')
    conta = input ('  Conta: ')
    tipo = input ('    Tipo da conta [Poupança ou Corrente]: ').lower().strip()
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
        
        print(f'Nome: {usuario.nome}')
        print(f'Agencia: {usuario.agencia}')
        print(f'Conta: {usuario.conta}')
        print(f'Saldo: {usuario.saldo}')




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
            

