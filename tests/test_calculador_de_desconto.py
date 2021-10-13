from src.calculador_de_desconto import CalculadorDeDesconto
from src.orcamento import Orcamento, Item


class TestCalculadorDeDesconto:
    def test_tem_desconto_de_10_porcento_se_tiver_mais_de_5_itens(self):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 100))
        orcamento.adiciona_item(Item("b", 200))
        orcamento.adiciona_item(Item("c", 100))
        orcamento.adiciona_item(Item("d", 100))
        orcamento.adiciona_item(Item("e", 300))
        orcamento.adiciona_item(Item("e", 200))

        calculador_de_desconto = CalculadorDeDesconto()

        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == 100.0

    def test_tem_desconto_de_7_porcento_se_somatorio_do_preco_for_maior_que_500(self):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 400))
        orcamento.adiciona_item(Item("b", 400))
        orcamento.adiciona_item(Item("c", 200))

        calculador_de_desconto = CalculadorDeDesconto()

        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == 70.0

    def test_tem_desconto_de_10_porcento_se_tiver_mais_de_5_itens_mesmo_se_o_somatorio_for_menor_que_500(self):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 10))
        orcamento.adiciona_item(Item("b", 20))
        orcamento.adiciona_item(Item("c", 10))
        orcamento.adiciona_item(Item("d", 10))
        orcamento.adiciona_item(Item("e", 30))
        orcamento.adiciona_item(Item("e", 20))

        calculador_de_desconto = CalculadorDeDesconto()

        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == 10.0

    def test_nao_tem_desconto_se_o_orcamento_tem_menos_de_5_itens_e_se_o_valor_do_orcamento_eh_menor_que_500(self):
        orcamento = Orcamento()
        orcamento.adiciona_item(Item("a", 10))
        orcamento.adiciona_item(Item("b", 20))

        calculador_de_desconto = CalculadorDeDesconto()

        desconto = calculador_de_desconto.calcula(orcamento)
        assert desconto == 0
