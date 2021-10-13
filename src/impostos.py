# noinspection PyMethodMayBeStatic
class ISS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


# noinspection PyMethodMayBeStatic
class ICMS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
