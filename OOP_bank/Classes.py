from abc import ABC,abstractmethod



class Conta(ABC):
    def __init__ (self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #@property
    #def saldo (self):
    #    return self.saldo
    
    def deposito (self, valor):
        self.saldo += valor

    @abstractmethod
    def saque (self, valor):
        pass


class Poupanca (Conta):
    def __init__ (self, nome, agencia, conta, saldo):
        super().__init__(nome, agencia, conta, saldo)

    def saque (self, valor):
        pass

class Corrente (Conta):
    def __init__ (self, nome, agencia, conta, saldo, limite = 100):
        super().__init__(nome, agencia, conta, saldo)
        self.limite = limite
    
    def saque (self, valor):
        pass



    





