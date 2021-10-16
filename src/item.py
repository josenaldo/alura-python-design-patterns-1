from decimal import Decimal


class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = Decimal(valor)

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor
