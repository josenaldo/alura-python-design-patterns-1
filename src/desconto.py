from decimal import Decimal


class SemDesconto:
    def __init__(self, proximo_desconto=None):
        self._proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        return Decimal("0.00")

    def calcula_proximo_desconto(self, orcamento):
        if self._proximo_desconto:
            return self._proximo_desconto.calcula(orcamento)
        else:
            return Decimal("0.00")


class DescontoPorCincoItens(SemDesconto):

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:

            return orcamento.valor * Decimal("0.10")
        else:
            return self.calcula_proximo_desconto(orcamento)


class DescontoPorMaisDeQuinhentosReais(SemDesconto):

    def calcula(self, orcamento):
        if orcamento.valor > Decimal("500"):

            return orcamento.valor * Decimal("0.07")
        else:
            return self.calcula_proximo_desconto(orcamento)
