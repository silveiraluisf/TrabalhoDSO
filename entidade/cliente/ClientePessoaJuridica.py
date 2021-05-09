from entidade.cliente.abstractCliente import AbstractCliente
from entidade.veiculo.veiculo import Veiculo
 
class ClientePessoaJuridica(AbstractCliente):
        
    def __init__(self, codigo: int, nome: str, telefone: int,endereco: str, data_fundacao: str, cnpj: str, veiculo: Veiculo):
            super().__init__(codigo, nome, telefone, endereco)
            self.__data_fundacao = data_fundacao
            self.__cnpj = cnpj
            self.__veiculo = veiculo

    @property
    def data_fundacao(self):
        return self.__data_fundacao

    @data_fundacao.setter
    def data_fundacao(self, data_fundacao: str):
        if isinstance(data_fundacao,str):
            self.__data_fundacao = data_fundacao
            
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.cnpj = cnpj

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

