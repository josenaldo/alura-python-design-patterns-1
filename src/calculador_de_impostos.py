from src.orcamento import Orcamento
from src.impostos import ISS, ICMS


class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    calculador_de_impostos = CalculadorDeImpostos()

    orcamento = Orcamento(500)
    
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
