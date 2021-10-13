from unittest.mock import patch

from src.calculador_de_impostos import CalculadorDeImpostos
from src.impostos import ICMS, ISS
from src.orcamento import Orcamento, Item


@patch('builtins.print')
class TestCalculadorDeImposto:

    def test_deve_calcular_o_iss(self, mock_print):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 100))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ISS()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(10.0)

    def test_deve_calcular_o_icms(self, mock_print):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 100))
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICMS()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(6.0)
