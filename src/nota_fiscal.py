class NotaFiscal:
    def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise ValueError("Detalhes da nota não pode ter mais do que 20 caracteres")
        self.__detalhes = detalhes

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def itens(self):
        return self.__itens

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes
