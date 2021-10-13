# noinspection PyMethodMayBeStatic
class DescontoPorCincoItens:

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return 0


# noinspection PyMethodMayBeStatic
class DescontoPorMaisDeQuinhentosReais:

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return 0
