import functions as fun


if __name__ == '__main__':
    while True:
        fun.print_menu()
        option = input('Digite sua opção: ')
        while True:
            if fun.valid_option(option):
                break
            else:
                option = input (f'Opção invalida\nDigite sua opção novamente: ')
        option = int(option)
            
        if option == 1:
            new_cnpj = fun.random_numbers()
            new_cnpj = fun.digits(new_cnpj,5)
            new_cnpj = (fun.digits(new_cnpj,6))
            print(f'O cnpj gerado foi {new_cnpj[0]}{new_cnpj[1]}.{new_cnpj[2]}{new_cnpj[3]}{new_cnpj[4]}.{new_cnpj[5]}{new_cnpj[6]}{new_cnpj[7]}/{new_cnpj[8]}{new_cnpj[9]}{new_cnpj[10]}{new_cnpj[11]}-{new_cnpj[12]}{new_cnpj[13]}')

        if option == 2:
            cnpj = str (input ('Digite o CNPJ para a verificação: '))
            cnpj = fun.remove_caracteres(cnpj)
            cnpj_valid = cnpj[:-2]
            cnpj_valid = fun.digits(cnpj_valid,5)
            cnpj_valid = fun.digits(cnpj_valid,6)
            if cnpj == cnpj_valid:
                print('CNPJ válido')
            else:
                print('CNPJ Inválido')

        if option == 3:
            print('Saindo')
            break
