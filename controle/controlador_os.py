
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

        data = self.__tela_os.coleta_data()

        dados_cliente = self.__controlador_sistema.retornar_cliente()

        veiculo = self.__controlador_sistema.pegar_veiculo()

        codigo_revisao = self.verifica_km(veiculo.quilometragem)

        revisao = Revisao(20,20000, [1, 2], [6, 7]) #self.incluir_revisão(codigo_revisao)

        os = OS(data, dados_cliente, veiculo, revisao)

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

    def verifica_km(self, quilometragem: Veiculo.quilometragem) -> int:

        if 0 <= quilometragem <= 10000:
            return 10
        elif 10001 <= quilometragem <= 20000:
            return 20
        elif 20001 <= quilometragem <= 30000:
            return 30
        elif 30001 <= quilometragem <= 40000:
            return 40
        elif 40001 <= quilometragem <= 50000:
            return 50
        elif 50001 <= quilometragem <= 60000:
            return 60
        elif 60001 <= quilometragem <= 70000:
            return 70
        elif 70001 <= quilometragem <= 80000:
            return 80
        elif 80001 <= quilometragem <= 90000:
            return 90
        elif 90001 <= quilometragem <= 100000:
            return 100
        elif 100001 >= quilometragem:
            return 110

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_revisao(self, codigo):
        self.__controlador_sistema.incluir_revisao(codigo)