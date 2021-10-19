from unittest.mock import patch

import pytest

from src.item import Item
from src.nota_fiscal import NotaFiscal


@pytest.fixture
def razao_social():
    return "Berimbau Wireless LTDA"


@pytest.fixture
def cnpj():
    return "22568575000148"


@pytest.fixture
def itens():
    itens = [Item("ITEM A", 100), Item("ITEM B", 200)]
    return itens


@patch("src.observadores.imprime")
@patch("src.observadores.envia_por_email")
@patch("src.observadores.salva_no_banco")
def test_criar_uma_nota_fiscal_deve_invocar_os_metodos_dos_observadores(
        mock_salva_no_banco, mock_envia_por_email, mock_imprime, razao_social, cnpj, itens):

    observadores = [mock_imprime, mock_envia_por_email, mock_salva_no_banco]

    nota_fiscal = NotaFiscal(
        razao_social=razao_social,
        cnpj=cnpj,
        itens=itens,
        observadores=observadores
    )

    mock_imprime.assert_called_once_with(nota_fiscal)
    mock_envia_por_email.assert_called_once_with(nota_fiscal)
    mock_salva_no_banco.assert_called_once_with(nota_fiscal)
