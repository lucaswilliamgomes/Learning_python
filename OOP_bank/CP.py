from account import Conta


class ContaPoupanca (Conta):
    def saque (self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError ("Valor do saque deve apresentar apenas números")
        else:
            if self._saldo - valor < 0:
                print('Saldo insuficiente para saque') 
            else: 
                self._saldo -= valor
                print('Saque realizado com sucesso')


    
