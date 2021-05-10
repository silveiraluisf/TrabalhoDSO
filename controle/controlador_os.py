
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
        self.__dao = OSDAO()
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

        km_tratado = self.verifica_km(veiculo.quilometragem)

        revisao = self.incluir_revisao(km_tratado)

        os = OS(data, dados_cliente, veiculo, revisao)

        self.__dao.add(os)

        self.__tela_os.sucesso()

        self.abre_tela()

    def editar_os(self):

        numero = self.__tela_os.pesquisar_numero_os()

        data = self.__tela_os.coleta_data()

        dados_cliente = self.__controlador_sistema.retornar_cliente()

        veiculo = self.__controlador_sistema.pegar_veiculo()

        km_tratado = self.verifica_km(veiculo.quilometragem)

        revisao = self.incluir_revisao(km_tratado)

        nova_os = {"data": data, "dados_cliente": dados_cliente, "veiculo": veiculo,
                 "revisao": revisao}

        for os in self.__dao.get_all():
            if numero == os.numero:

                os_editada = OS(nova_os["data"], nova_os["dados_cliente"],
                nova_os["veiculo"], nova_os["revisao"])

                self.__dao.remove(numero)
                self.__dao.add(os_editada)
                self.__tela_os.sucesso()
                break

            else:
                self.__tela_os.falha()

    def listar_os(self):
        for os in self.__dao.get_all():
            self.__tela_os.listar_os({'numero': os.numero, 'data': os.data,
                                      'cliente': os.cliente.nome, 'veiculo': os.veiculo.modelo,
                                      'placa': os.veiculo.placa,
                                      'codigo': os.revisao.codigo,
                                      'quilometragem': os.revisao.quilometragem,
                                      'verificacao': os.revisao.verificacao,
                                      'substituicao': os.revisao.substituicao})

        self.__tela_os.sucesso

        self.abre_tela()

    def excluir_os(self):

        numero = self.__tela_os.pesquisar_numero_os()

        for os in self.__dao.get_all():
            if numero == os.numero:
                self.__dao.remove(os)
                self.__tela_os.sucesso
                self.abre_tela()


    def pesquisar_os(self):
        numero = self.__tela_os.pesquisar_numero_os()

        for os in self.__dao.get_all():
            if os.numero == numero:
                self.__tela_os.exibir_os(os)

    def verifica_km(self, quilometragem: Veiculo.quilometragem):
        if 0 <= quilometragem <= 10000:
            return str(10)
        elif 10001 <= quilometragem <= 20000:
            return str(20)
        elif 20001 <= quilometragem <= 30000:
            return str(30)
        elif 30001 <= quilometragem <= 40000:
            return str(40)
        elif 40001 <= quilometragem <= 50000:
            return str(50)
        elif 50001 <= quilometragem <= 60000:
            return str(60)
        elif 60001 <= quilometragem <= 70000:
            return str(70)
        elif 70001 <= quilometragem <= 80000:
            return str(80)
        elif 80001 <= quilometragem <= 90000:
            return str(90)
        elif 90001 <= quilometragem <= 100000:
            return str(100)
        elif 100001 >= quilometragem:
            return str(110)

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_revisao(self, codigo):
        return self.__controlador_sistema.incluir_revisao(codigo)