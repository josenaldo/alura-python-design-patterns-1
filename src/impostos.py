from abc import ABCMeta, abstractmethod


class Imposto(metaclass=ABCMeta):
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
        
    @abstractmethod
    def calcula(self, orcamento):
        pass


class ImpostoSimples(Imposto):

    def __init__(self, nome, aliquota):
        super(ImpostoSimples, self).__init__(nome)
        self.__aliquota = aliquota

    @property
    def nome(self):
        return self.__nome

    @property
    def aliquota(self):
        return self.__aliquota

    def calcula(self, orcamento):
        return orcamento.valor * self.aliquota


class ImpostoCondicional(Imposto, metaclass=ABCMeta):

    def __init__(self, nome, aliquota_minima, aliquota_maxima):
        super(ImpostoCondicional, self).__init__(nome)
        self.__aliquota_minima = aliquota_minima
        self.__aliquota_maxima = aliquota_maxima

    @property
    def aliquota_minima(self):
        return self.__aliquota_minima

    @property
    def aliquota_maxima(self):
        return self.__aliquota_maxima

    def calcula(self, orcamento):
        if self.deve_usar_a_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento)
        else:
            return self.taxacao_minima(orcamento)

    @abstractmethod
    def deve_usar_a_taxacao_maxima(self, orcamento):
        pass

    def taxacao_minima(self, orcamento):
        return orcamento.valor * self.aliquota_minima

    def taxacao_maxima(self, orcamento):
        return orcamento.valor * self.aliquota_maxima


class ISS(ImpostoSimples):
    def __init__(self):
        super(ISS, self).__init__("ISS", 0.1)


class ICMS(ImpostoSimples):
    def __init__(self):
        super(ICMS, self).__init__("ICMS", 0.06)


class ICPP(ImpostoCondicional):
    def __init__(self):
        super(ICPP, self).__init__("ICPP", 0.05, 0.07)

    def deve_usar_a_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500


class IKCV(ImpostoCondicional):
    def __init__(self):
        super(IKCV, self).__init__("IKCV", 0.06, 0.1)

    def deve_usar_a_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def __tem_item_maior_que_100_reais(self, orcamento):
        """
        Esse método pode ter uma implementação bem mais simples, com um if::

            for item in orcamento.obter_itens():
                if(item.valor > 100):
                    return True
                return False

        Ou uma implementação usando filter::

            maiores_que_100 = list(filter(lambda x: x.valor > 100, orcamento.obter_itens()))
            return len(maiores_que_100) > 0

        :param orcamento: Orçamento
        :return: True, se o orçamento tiver algum item com valor maior que 100
        """

        maiores_que_100 = [item for item in orcamento.obter_itens() if item.valor > 100]
        return len(maiores_que_100) > 0
