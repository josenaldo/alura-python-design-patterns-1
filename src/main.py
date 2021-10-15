import logging

from src.calculador_de_impostos import CalculadorDeImpostos
from src.impostos import IKCV
from src.orcamento import Orcamento, Item

logging.basicConfig(level=logging.DEBUG)

orcamento = Orcamento()
orcamento.adiciona_item(Item("a", 100))
orcamento.adiciona_item(Item("b", 300))

calculador_de_imposto = CalculadorDeImpostos()
imposto = IKCV()

calculador_de_imposto.realiza_calculo(orcamento, imposto)
