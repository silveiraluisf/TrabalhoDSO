
from limite.tela_os import TelaOS
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica
from entidade.veiculo.veiculo import Veiculo
from entidade.revisao.revisao import Revisao
from entidade.os.os import OS
from controle.controlador_cliente import ControladorCliente
from persistencia.os_dao import OSDAO

class ControladorOS():
    def __init__(self, controlador_sistema):
        self.__dao_os = OSDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_os = TelaOS()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_os, 2: self.editar_os, 3: self.listar_os,
                        4: self.excluir_os, 5: self.pesquisar_os, 0: self.voltar}

        continua = True

        while continua:
            lista_opcoes[self.__tela_os.tela_opcoes()]()

    def criar_os(self):
        # gerar o número
        # data
        # cliente
        # veiculo
        # tratar a quilometragem
        # pegar a revisão correta
        # confirmar se foi feito

        data = self.__tela_os.coleta_data()

        dados_cliente = self.__controlador_sistema.retornar_cliente()

        veiculo = self.__controlador_sistema.pegar_veiculo()

        os = OS(data, dados_cliente, veiculo)

        analise_revisao = self.verifica_km(veiculo.quilometragem)

        self.incluir_revisão()

        self.__dao_os.add(os)

        self.__tela_os.sucesso()

        self.abre_tela()

    def editar_os(self):
        pass

    def listar_os(self):
        pass

    def excluir_os(self):
        pass

    def pesquisar_os(self):
        pass

    def verifica_km(self, quilometragem: Veiculo.quilometragem):
        pass

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_revisao(self, revisao: Revisao):
        pass