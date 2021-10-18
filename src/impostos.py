import logging
from decimal import Decimal
from abc import ABCMeta, abstractmethod


def logador_de_imposto(invocavel):
    def wrapper(self, orcamento):
        imposto = invocavel(self, orcamento)
        logging.debug(f"Imposto: {self.nome} | Valor: R$ {imposto:.2f}")
        return imposto
    return wrapper


class Imposto(metaclass=ABCMeta):
    def __init__(self, nome, outro_imposto=None):
        self.__nome = nome
        self.__outro_imposto = outro_imposto

    @property
    def nome(self):
        if self.__outro_imposto is None:
            return self.__nome
        else:
            return f"{self.__nome}+{self.__outro_imposto.nome}"

    @abstractmethod
    def calcula(self, orcamento):
        pass

    def calcula_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)


class ImpostoSimples(Imposto):

    def __init__(self, nome, aliquota, outro_imposto=None):
        super(ImpostoSimples, self).__init__(nome, outro_imposto)
        self.__aliquota = Decimal(aliquota)

    @property
    def aliquota(self):
        return self.__aliquota

    @logador_de_imposto
    def calcula(self, orcamento):
        return (orcamento.valor * self.aliquota) + self.calcula_outro_imposto(orcamento)


class ImpostoCondicional(Imposto, metaclass=ABCMeta):

    def __init__(self, nome, aliquota_minima, aliquota_maxima, outro_imposto=None):
        super(ImpostoCondicional, self).__init__(nome, outro_imposto)
        self.__aliquota_minima = Decimal(aliquota_minima)
        self.__aliquota_maxima = Decimal(aliquota_maxima)

    @property
    def aliquota_minima(self):
        return self.__aliquota_minima

    @property
    def aliquota_maxima(self):
        return self.__aliquota_maxima

    @logador_de_imposto
    def calcula(self, orcamento):
        if self.deve_usar_a_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento) + self.calcula_outro_imposto(orcamento)
        else:
            return self.taxacao_minima(orcamento) + self.calcula_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_a_taxacao_maxima(self, orcamento):
        pass

    def taxacao_minima(self, orcamento):
        return orcamento.valor * self.aliquota_minima

    def taxacao_maxima(self, orcamento):
        return orcamento.valor * self.aliquota_maxima


class ISS(ImpostoSimples):
    def __init__(self, outro_imposto=None):
        super(ISS, self).__init__("ISS", 0.10, outro_imposto)


class ICMS(ImpostoSimples):
    def __init__(self, outro_imposto=None):
        super(ICMS, self).__init__("ICMS", 0.06, outro_imposto)


class ICPP(ImpostoCondicional):
    def __init__(self, outro_imposto=None):
        super(ICPP, self).__init__("ICPP", 0.05, 0.07, outro_imposto)

    def deve_usar_a_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500


class IKCV(ImpostoCondicional):
    def __init__(self, outro_imposto=None):
        super(IKCV, self).__init__("IKCV", 0.06, 0.10, outro_imposto)

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
