from datetime import date

import pytest

from src.criador_de_nota_fiscal import CriadorDeNotaFiscal
from src.item import Item


class TestCriadorDeNotaFiscal:

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

    def test_criador_nao_pode_criar_nota_fiscal_sem_razao_social(self, cnpj, itens):
        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_cnpj(cnpj).com_itens(itens).constroi()

    def test_criador_nao_pode_criar_nota_fiscal_sem_cnpf(self, razao_social, itens):
        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_razao_social(razao_social).com_itens(itens).constroi()

    def test_criador_nao_pode_criar_nota_com_cnpj_invalido(self, razao_social, cnpj, itens):
        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj("12345534223").com_itens(itens).constroi()

        nota_fiscal = CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).com_itens(itens).constroi()
        assert nota_fiscal.cnpj == cnpj

    def test_criador_nao_pode_criar_nota_fiscal_sem_itens(self, razao_social, cnpj):
        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).constroi()

        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).com_itens([]).constroi()

        with pytest.raises(ValueError):
            CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).com_itens(list()).constroi()

    def test_criador_pode_criar_nota_fiscal_sem_passar_data_de_emissao(self, razao_social, cnpj, itens):
        nota_fiscal = CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).com_itens(itens).constroi()
        hoje = date.today()

        assert nota_fiscal.data_de_emissao == hoje

    def test_criador_pode_criar_nota_fiscal_sem_passar_detalhes(self, razao_social, cnpj, itens):
        nota_fiscal = CriadorDeNotaFiscal().com_razao_social(razao_social).com_cnpj(cnpj).com_itens(itens).constroi()

        assert nota_fiscal.detalhes == ''
