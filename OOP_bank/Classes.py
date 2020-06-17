from abc import ABC,abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    @property
    def nome (self):
        return self.nome 

    @property
    def idade (self):
        return self.idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


class Conta(ABC):
    def __init__ (self, agencia, conta, saldo = 0):
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
    def __init__ (self, agencia, conta, saldo = 0):
        super().__init__(agencia, conta, saldo = 0)

    def saque (self, valor):
        pass

class Corrente (Conta):
    def __init__ (self, agencia, conta, saldo = 0, limite = 100):
        super().__init__(agencia, conta, saldo = 0)
        self.limite = limite



    





