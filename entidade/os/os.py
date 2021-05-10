
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica
from entidade.veiculo.veiculo import Veiculo
from entidade.revisao.revisao import Revisao

class OS:
    __numero = 1

    @classmethod
    def atualiza(cls, delta=1):
        cls.__numero += delta

    def __init__(self, data: str, cliente: ClientePessoaFisica or ClientePessoaJuridica,
                 veiculo: Veiculo, revisao: Revisao):

        self.__numero = OS.__numero
        OS.atualiza()
        self.__data = data
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__revisao = revisao

    @property
    def numero(self):
        return self.__numero

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: ClientePessoaFisica or ClientePessoaJuridica):
        self.__cliente = cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        self.__veiculo = veiculo

    @property
    def revisao(self):
        return self.__revisao

    @revisao.setter
    def revisao(self, revisao: Revisao):
        self.__revisao = revisao

