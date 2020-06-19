from abc import ABC,abstractmethod



class Conta(ABC):
    def __init__ (self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = float(saldo)

    #@property
    #def saldo (self):
    #    return self.saldo
    
    def deposito (self, valor):
        self.saldo += valor

    @abstractmethod
    def saque (self, valor):
        pass


class Poupanca (Conta):
    def __init__ (self, nome, agencia, conta, saldo, limite = 0):
        super().__init__(nome, agencia, conta, saldo)
        self.limite = 0
    def saque (self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente !')
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')


class Corrente (Conta):
    def __init__ (self, nome, agencia, conta, saldo, limite = 100):
        super().__init__(nome, agencia, conta, saldo)
        self.limite = limite
    
    def saque (self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente !')
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')




    





