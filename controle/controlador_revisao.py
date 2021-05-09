from limite.tela_revisao import TelaRevisao
from entidade.revisao.revisao import Revisao
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica
from entidade.veiculo.veiculo import Veiculo 

class ControladorRevisao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_revisao = TelaRevisao()
        

    def abre_tela(self):
        lista_opcoes = {1: self.iniciar_revisao_pf, 0: self.voltar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_revisao.tela_opcoes()]()

    def iniciar_revisao_pf(self): 
        dados_veiculo = self.__controlador_sistema.pegar_veiculo()
        dados_cliente = self.__controlador_sistema.pegar_cliente_pf()
        self.__tela_revisao.listar_revisoes(Revisao.lista_substituicoes, Revisao.lista_verificacoes, dados_veiculo, dados_cliente) 
        pass 

    def voltar(self):
        self.__controlador_sistema.abre_tela()  
 

     