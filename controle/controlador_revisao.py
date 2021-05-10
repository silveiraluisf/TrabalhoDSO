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

        revisao = Revisao(dados_revisao["codigo"], dados_revisao["quilometragem"], 
        dados_revisao["verificacao"], dados_revisao["substituicao"])

        self.__dao.add(revisao)
        self.__tela_revisao.sucesso()
        self.abre_tela()

    def listar_itens_revisao(self):
        for revisao in self.__dao.get_all():
            self.__tela_revisao.listar_revisoes({'codigo':revisao.codigo, 'quilometragem': revisao.quilometragem,
            'verificacao': revisao.verificacao, 'substituicao': revisao.substituicao})

        self.abre_tela()

    def excluir_item_revisao(self):
        
        codigo = self.__tela_revisao.pesquisar_revisao_codigo()

        for revisao in self.__dao.get_all():
            if codigo != revisao.codigo:
                pass
            else: 
                self.__dao.remove(revisao)
                self.__tela_revisao.sucesso()
                self.abre_tela()

    def editar_item_revisao(self):

        codigo = self.__tela_revisao.pesquisar_revisao_codigo()

        for revisao in self.__dao.get_all():
            if codigo == revisao.codigo:
                nova_revisao = self.__tela_revisao.pega_dados_revisao()

                revisao_editada = Revisao(nova_revisao["codigo"], nova_revisao["quilometragem"], 
                nova_revisao["verificacao"], nova_revisao["substituicao"])

                self.__dao.remove(revisao)
                self.__dao.add(revisao_editada)
                self.__tela_revisao.sucesso()
                break 

            else:
                self.__tela_revisao.falha()  

    def pesquisar_revisao_codigo(self):

        codigo = self.__tela_revisao.pesquisar_revisao_codigo()

        for revisao in self.__dao.get_all():
            if codigo == revisao.codigo:
                return codigo

    def incluir_revisão(self, codigo):

        for revisao in self.__dao.get_all():
            if revisao.codigo != codigo:
                pass
            else:
                return revisao

    def voltar(self):
        self.__controlador_sistema.abre_tela()  
