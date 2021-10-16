import logging
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
        mock_print.assert_called_once_with("ISS = 10.00")

    def test_deve_calcular_o_icms(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICMS()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("ICMS = 6.00")

    def test_deve_calcular_o_icpp_para_menos_de_500_reais(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICPP()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("ICPP = 5.00")

    def test_deve_calcular_o_icpp_para_mais_de_500_reais(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 900))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICPP()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("ICPP = 70.00")

    def test_deve_calcular_o_ikcv_para_orcamento_com_um_item_maior_que_100_reais_e_valor_maior_que_500(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 900))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("IKCV = 100.00")

    def test_deve_calcular_o_ikcv_para_orcamento_sem_um_item_maior_que_100_reais_e_valor_maior_que_500(self, mock_print, orcamento):

        for i in range(0, 10):
            orcamento.adiciona_item(Item("b", 90))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("IKCV = 60.00")

    def test_deve_calcular_o_ikcv_para_orcamento_com_um_item_maior_que_100_reais_e_valor_menor_que_500(self, mock_print, orcamento):
        orcamento.adiciona_item(Item("b", 300))

        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("IKCV = 24.00")

    def test_deve_calcular_o_ikcv_para_orcamento_sem_um_item_maior_que_100_reais_e_valor_menor_que_500(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = IKCV()

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("IKCV = 6.00")

    def test_deve_calcular_imposto_icms_e_iss_composto(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICMS(ISS())

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("ICMS+ISS = 16.00")

    def test_deve_calcular_imposto_icms_iss_icpp_ikcv_compostos(self, mock_print, orcamento):
        calculador_de_imposto = CalculadorDeImpostos()
        imposto = ICMS(ISS(ICPP(IKCV())))

        calculador_de_imposto.realiza_calculo(orcamento, imposto)
        mock_print.assert_called_once_with("ICMS+ISS+ICPP+IKCV = 27.00")
