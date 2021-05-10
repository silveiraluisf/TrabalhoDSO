from limite.tela_revisao import TelaRevisao
from entidade.revisao.revisao import Revisao
from persistencia.revisao_dao import RevisaoDAO

class ControladorRevisao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__dao = RevisaoDAO()
        self.__tela_revisao = TelaRevisao()
        

    def abre_tela(self):
        lista_opcoes = {1: self.criar_item_revisao, 2: self.listar_itens_revisao, 3: self.excluir_item_revisao,
        4: self.editar_item_revisao, 0: self.voltar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_revisao.tela_opcoes()]()

    def criar_item_revisao(self):
        dados_revisao = self.__tela_revisao.pega_dados_revisao()

        revisao = Revisao(dados_revisao["quilometragem"], dados_revisao["verificacao"], dados_revisao["substituicao"])

        self.__dao.add(revisao)

        self.abre_tela()

    def listar_itens_revisao(self):
        pass

    def excluir_item_revisao(self):
        pass

    def editar_item_revisao(self):
        pass 

    #def iniciar_revisao_pf(self): 
    #    dados_veiculo = self.__controlador_sistema.pegar_veiculo()
    #    dados_cliente = self.__controlador_sistema.pegar_cliente_pf()
    #    self.__tela_revisao.listar_revisoes(dados_cliente, Revisao.lista_substituicoes, Revisao.lista_verificacoes, dados_veiculo)  

    def voltar(self):
        self.__controlador_sistema.abre_tela()  
 

     