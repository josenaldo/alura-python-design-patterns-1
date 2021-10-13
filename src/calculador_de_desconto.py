from src.desconto import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais


# noinspection PyMethodMayBeStatic
class CalculadorDeDesconto:
    def calcula(self, orcamento):

        desconto = DescontoPorCincoItens().calcula(orcamento)

        if desconto == 0:
            desconto = DescontoPorMaisDeQuinhentosReais().calcula(orcamento)

        return desconto
