from account import Conta

class ContaCorrente (Conta):
    
    def saque (self, valor):
        limite = 100
        if not isinstance(valor, (int, float)):
            raise ValueError ("Valor do saque deve apresentar apenas números")
        else:
            if (self._saldo + limite) - valor < 0:
                print('Saldo insuficiente para saque') 
            else: 
                self._saldo -= valor
                print('Saque realizado com sucesso')
