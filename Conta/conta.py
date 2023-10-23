class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        saldo_conta = f"Olá {self.__titular} seu sado é R$ {self.__saldo:.2f}"
        print(saldo_conta.replace(".",","))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor