from decimal import Decimal

import pytest

from src.estados_de_orcamento import EmAprovacao, Aprovado, Reprovado, Finalizado
from src.orcamento import Orcamento, Item


class TestOrcamento:
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

    def test_orcamento_deve_ser_criado_no_estado_em_aprovacao(self, orcamento):
        assert orcamento.estado_atual == EmAprovacao()

    def test_orcamento_em_aprovacao_pode_passar_para_aprovado(self, orcamento):
        orcamento.aprova()
        assert orcamento.estado_atual == Aprovado()

    def test_orcamento_em_aprovacao_pode_passar_para_reprovado(self, orcamento):
        orcamento.reprova()
        assert orcamento.estado_atual == Reprovado()

    def test_orcamento_em_aprovacao_nao_pode_passar_para_finalizado(self, orcamento):
        with pytest.raises(Exception):
            orcamento.finaliza()

    def test_orcamento_aprovado_so_pode_passar_para_finalizado(self, orcamento):
        orcamento.aprova()

        with pytest.raises(Exception):
            orcamento.reprova()

        orcamento.finaliza()

        assert orcamento.estado_atual == Finalizado()

    def test_orcamento_reprovado_so_pode_passar_para_finalizado(self, orcamento):
        orcamento.reprova()
        assert orcamento.estado_atual == Reprovado()

        with pytest.raises(Exception):
            orcamento.aprova()
        assert orcamento.estado_atual == Reprovado()

        orcamento.finaliza()
        assert orcamento.estado_atual == Finalizado()

    def test_orcamento_finalizado_nao_pode_mudar_de_estado(self, orcamento):
        orcamento.aprova()
        orcamento.finaliza()

        with pytest.raises(Exception):
            orcamento.aprova()

        with pytest.raises(Exception):
            orcamento.reprova()

        with pytest.raises(Exception):
            orcamento.finaliza()

        assert orcamento.estado_atual == Finalizado()

    def test_orcamento_deve_retornar_o_numero_de_itens(self, orcamento, itens_baratos):
        orcamento.adiciona_itens(itens_baratos)
        assert orcamento.total_itens == len(itens_baratos)

    def test_orcamento_deve_retornar_a_soma_dos_valores_dos_itens(self, orcamento, itens_baratos):
        orcamento.adiciona_itens(itens_baratos)
        assert orcamento.valor == Decimal(450.00)
