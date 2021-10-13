from unittest.mock import patch

import pytest

from src.calculador_de_impostos import CalculadorDeImpostos
from src.impostos import ICMS, ISS, ICPP, IKCV
from src.orcamento import Orcamento, Item


@patch('builtins.print')
class TestCalculadorDeImposto:

    @pytest.fixture
    def orcamento(self):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 100))

        return orcamento

    def test_deve_calcular_o_iss(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ISS()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(10.0)

    def test_deve_calcular_o_icms(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICMS()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(6.0)

    def test_deve_calcular_o_icpp_para_menos_de_500_reais(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICPP()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(5.0)

    def test_deve_calcular_o_icpp_para_mais_de_500_reais(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 900))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICPP()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(70.0)

    def test_deve_calcular_o_ikcv_para_orcamento_com_um_item_maior_que_100_reais_e_valor_maior_que_500(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 900))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(100.0)

    def test_deve_calcular_o_ikcv_para_orcamento_sem_um_item_maior_que_100_reais_e_valor_maior_que_500(self, mock_print, orcamento):

        for i in range(0, 10):
            orcamento.adiciona_item(Item("b", 90))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(60.0)

    def test_deve_calcular_o_ikcv_para_orcamento_com_um_item_maior_que_100_reais_e_valor_menor_que_500(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 300))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(24.0)

    def test_deve_calcular_o_ikcv_para_orcamento_sem_um_item_maior_que_100_reais_e_valor_menor_que_500(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with(6.0)