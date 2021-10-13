from unittest.mock import patch
import pytest

from src.calculador_de_impostos import CalculadorDeImpostos
from src.impostos import ICMS, ISS
from src.orcamento import Orcamento


@patch('builtins.print')
class TestCalculadorDeImposto:
    def test_deve_calcular_o_ISS(self, mock_print):
        orcamento = Orcamento(100)
        calculadorDeImposto = CalculadorDeImpostos()
        imposto = ISS()

        calculadorDeImposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(10.0)

    def test_deve_calcular_o_ICMS(self, mock_print):
        orcamento = Orcamento(100)
        calculadorDeImposto = CalculadorDeImpostos()
        imposto = ICMS()

        calculadorDeImposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(6.0)



