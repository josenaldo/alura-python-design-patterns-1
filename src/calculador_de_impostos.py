# noinspection PyMethodMayBeStatic
class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(f"{imposto.nome} = {imposto_calculado:.2f}")
