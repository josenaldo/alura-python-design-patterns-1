from src.nota_fiscal import NotaFiscal


class CriadorDeNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__data_de_emissao = None
        self.__detalhes = ""

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):

        nota_fiscal = NotaFiscal(
            cnpj=self.__cnpj,
            razao_social=self.__razao_social,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes
        )

        return nota_fiscal
