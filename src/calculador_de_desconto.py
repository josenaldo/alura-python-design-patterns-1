from src.desconto import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais


# noinspection PyMethodMayBeStatic
class CalculadorDeDesconto:
    def __init__(self):
        self.cadeia_de_descontos = DescontoPorCincoItens(DescontoPorMaisDeQuinhentosReais())

    def calcula(self, orcamento):

        desconto = self.cadeia_de_descontos.calcula(orcamento)

        return desconto
