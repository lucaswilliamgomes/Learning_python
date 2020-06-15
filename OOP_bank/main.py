from CP import ContaPoupanca
from CC import ContaCorrente

conta1 = ContaPoupanca(3436, 79786, 1000)
conta2 = ContaCorrente(3436, 90182, 120)
conta1.view()

conta2.saque(3000)
conta2.view()
conta2.depositar(1000)
conta2.view()
conta1.view()
