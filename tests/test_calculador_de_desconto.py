from decimal import Decimal

import pytest

from src.calculador_de_desconto import CalculadorDeDesconto
from src.orcamento import Orcamento, Item


class TestCalculadorDeDesconto:

    @pytest.fixture
    def calculador_de_desconto(self):
        return CalculadorDeDesconto()

    @pytest.fixture
    def orcamento(self):
        orcamento = Orcamento()
        return orcamento

    @pytest.fixture
    def itens_baratos(self):
        """
        Total: 450
        """
        itens = [
            Item("a", 10.00),
            Item("b", 20.00),
            Item("c", 30.00),
            Item("d", 40.00),
            Item("e", 50.00),
            Item("e", 60.00),
            Item("e", 70.00),
            Item("e", 80.00),
            Item("e", 90.00),
        ]

        return itens

    @pytest.fixture
    def itens_caros(self):
        """
        Total: 4500
        """
        itens = [
            Item("a", 100.00),
            Item("b", 200.00),
            Item("c", 300.00),
            Item("d", 400.00),
            Item("e", 500.00),
            Item("e", 600.00),
            Item("e", 700.00),
            Item("e", 800.00),
            Item("e", 900.00),
        ]

        return itens

    def test_tem_desconto_de_10_porcento_se_tiver_mais_de_5_itens(
            self, calculador_de_desconto, orcamento, itens_baratos):

        orcamento.adiciona_itens(itens_baratos)
        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == Decimal(45.00)

    def test_tem_desconto_de_7_porcento_se_somatorio_do_preco_for_maior_que_500(
            self, calculador_de_desconto, orcamento, itens_caros):

        orcamento.adiciona_itens(itens_caros[6:])
        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == Decimal(168.00)

    def test_tem_desconto_de_10_porcento_se_tiver_mais_de_5_itens_mesmo_se_o_somatorio_for_menor_que_500(
            self, calculador_de_desconto, orcamento, itens_baratos):

        orcamento.adiciona_itens(itens_baratos)
        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == Decimal(45.00)

    def test_nao_tem_desconto_se_o_orcamento_tem_menos_de_5_itens_e_se_o_valor_do_orcamento_eh_menor_que_500(
            self,calculador_de_desconto, orcamento, itens_baratos):
        orcamento.adiciona_itens(itens_baratos[0:3])
        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == Decimal(0.00)
