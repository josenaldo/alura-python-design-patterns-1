from datetime import date
from validate_docbr import CNPJ


class NotaFiscal:
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=None, detalhes='', observadores=None):

        if razao_social is None:
            raise ValueError("É preciso fornecer uma razão social")
        else:
            self.__razao_social = razao_social

        if cnpj is None:
            raise ValueError("É preciso fornecer um CNPJ")
        elif not self.__cnpj_eh_valido(cnpj):
            raise ValueError("CNPJ inválido")
        else:
            self.__cnpj = cnpj

        if itens is None:
            raise ValueError("É preciso fornecer os itens da nota")
        elif len(itens) == 0:
            raise ValueError("A nota fiscal precisa ter ao menos um item")
        else:
            self.__itens = itens

        self.__data_de_emissao = data_de_emissao or date.today()

        if len(detalhes) <= 100:
            self.__detalhes = detalhes
        else:
            raise ValueError("Detalhes da nota não pode ter mais do que 20 caracteres")

        if observadores:
            for observador in observadores:
                observador(self)


    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    def __cnpj_eh_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    @property
    def itens(self):
        return self.__itens

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes
