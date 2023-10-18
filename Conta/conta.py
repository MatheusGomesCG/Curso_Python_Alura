class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        saldo_conta = f"Olá {self.titular} seu sado é R$ {self.saldo:.2f}"
        print(saldo_conta.replace(".",","))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor