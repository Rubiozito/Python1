class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        

    def extrato(self):
        print("Saldo: {} , \n Titular: ".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        if not valor<=0:
            self.__saldo += valor
            return True
        return False
    
    def saca(self, valor):
        if not valor>self.__saldo:
            self.__saldo -= valor
            return True
        return False