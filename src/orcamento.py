from decimal import Decimal
from src.estados_de_orcamento import EmAprovacao


class Orcamento:
    def __init__(self):
        self.__itens = []
        self.__estado_atual = EmAprovacao()
        self.__desconto_extra = Decimal(0.00)

    @property
    def valor(self):
        return sum(item.valor for item in self.__itens) - self.__desconto_extra

    @property
    def estado_atual(self):
        return self.__estado_atual

    @estado_atual.setter
    def estado_atual(self, value):
        self.__estado_atual = value

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)
        
    def adiciona_itens(self, itens):
        for item in itens:
            self.adiciona_item(item)

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_disconto_extra(self):
        if self.__desconto_extra == Decimal("0.00"):
            self.estado_atual.aplica_desconto_extra(self)
        else:
            raise Exception("O desconto extra não pode ser aplicado duas vezes.")

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto
