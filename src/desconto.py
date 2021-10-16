import decimal
from decimal import Decimal

class SemDesconto:
    def __init__(self, proximo_desconto=None):
        self._proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        return 0

    def calcula_proximo_desconto(self, orcamento):
        if self._proximo_desconto:
            return self._proximo_desconto.calcula(orcamento)
        else:
            return 0


# noinspection PyMethodMayBeStatic
class DescontoPorCincoItens(SemDesconto):

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:

            return orcamento.valor * Decimal("0.10")
        else:
            return self.calcula_proximo_desconto(orcamento)


# noinspection PyMethodMayBeStatic
class DescontoPorMaisDeQuinhentosReais(SemDesconto):

    def calcula(self, orcamento):
        if orcamento.valor > Decimal("500"):

            return orcamento.valor * Decimal("0.07")
        else:
            return self.calcula_proximo_desconto(orcamento)
