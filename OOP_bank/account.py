from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo = 0):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def saldo (self):
        return self._saldo

    @saldo.getter
    def saldo (self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError ("Valor do saldo deve apresentar apenas números")

        self._saldo = valor

    def depositar (self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError ("Valor do saldo deve apresentar apenas números")
        self._saldo += valor 

    @abstractmethod
    def saque (self, valor):
        pass

    def view (self):
        print('==== DADOS ===')
        print(f'Agencia = {self._agencia}')
        print(f'Conta = {self._conta}')
        print(f'Saldo = {self._saldo}')


