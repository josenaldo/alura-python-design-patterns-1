from datetime import date

import pytest

from src.item import Item
from src.nota_fiscal import NotaFiscal


class TestNotaFiscal:

    @pytest.fixture
    def razao_social(self):
        return "Berimbau Wireless LTDA"

    @pytest.fixture
    def cnpj(self):
        return "22568575000148"

    @pytest.fixture
    def itens(self):
        itens = [Item("ITEM A", 100), Item("ITEM B", 200)]
        return itens

    @pytest.fixture
    def nota_fiscal(self, razao_social, cnpj, itens):
        nota_fiscal = NotaFiscal(
            razao_social=razao_social,
            cnpj=cnpj,
            itens=itens,
            data_de_emissao=date.today(),
            detalhes='Peças de berimbau wireless'
        )

        return nota_fiscal

    def test_detalhe_da_nota_nao_pode_ter_mais_de_100_caracteres(self, razao_social, cnpj, itens):

        with pytest.raises(ValueError):
            NotaFiscal(
                razao_social,
                cnpj,
                itens,
                date.today(),
                "Peças para fabricação de um berimbau wireless do "
                "tamanho de um transformer, com cabaça de côco do himalaia"
            )

    def test_nota_criada_sem_data_de_emissao_tem_a_data_de_hoje(self, razao_social, cnpj, itens):
        nota_fiscal = NotaFiscal(
            cnpj=cnpj,
            razao_social=razao_social,
            itens=itens,
            detalhes='Peças de berimbau wireless'
        )

        hoje = date.today()

        assert nota_fiscal.data_de_emissao == hoje