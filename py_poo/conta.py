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
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, novo_limite):
        self.__limite = novo_limite