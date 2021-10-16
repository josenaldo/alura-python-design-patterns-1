from abc import abstractmethod, ABCMeta
from decimal import Decimal


class EstadoDeOrcamento(metaclass=ABCMeta):

    def __eq__(self, other):
        return self.__class__ == other.__class__

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoDeOrcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * Decimal("0.02"))

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Orçamento em aprovação não podem ir para finalizado")


class Aprovado(EstadoDeOrcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * Decimal("0.05"))

    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento aprovados não podem ser reprovados')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoDeOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser reprovado novamente')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoDeOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser aprovados novamente')

    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser reprovados')

    def finaliza(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser finalizados novamente')
