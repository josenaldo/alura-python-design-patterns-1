# noinspection PyMethodMayBeStatic
class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)
