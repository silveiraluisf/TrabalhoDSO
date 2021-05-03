from limite.tela_veiculo import TelaVeiculo
from entidade.veiculo.veiculo import Veiculo 

class ControladorVeiculo():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_veiculo = TelaVeiculo()
        self.__veiculos = []

    def cadastrar_veiculo(self):
        dados_veiculo = self.__tela_veiculo.pega_dados_veiculo()

        #Precisar fazer com que os veiculos criados caiam numa lista 
        veiculo = Veiculo(dados_veiculo["modelo"], dados_veiculo["ano"], dados_veiculo["placa"], 
        dados_veiculo["quilometragem"])

        self.__veiculos.append(veiculo)

    #def editar_veiculo(self):
      
    #    novo_modelo = input("Informe o novo modelo:")
    #    self.__veiculo.modelo = novo_modelo

    #   novo_ano = input("Informe o novo ano:")
    #    self.__veiculo.ano = novo_ano

    #    nova_placa = input("Informe a nova placa:")
    #    self.__veiculo.placa = nova_placa

    #    nova_quilometragem = input("Informe a nova quilometragem:")
    #    self.__veiculo.quilometragem = nova_quilometragem

    #    novo_veiculo = Veiculo(novo_modelo, novo_ano, nova_placa, nova_quilometragem)
    #    self.__veiculo = novo_veiculo

    def listar_veiculos(self):
        for veiculo in self.__veiculos:
            self.__tela_veiculo.mostrar_veiculos({"modelo": veiculo.modelo, "ano": veiculo.ano, 
            "placa": veiculo.placa, "quilometragem": veiculo.quilometragem })

    #def excluir_veiculo(self):
    #  veiculo = self.__veiculo 
    # del (veiculo)
        
    #def mostrar_veiculo(self):
    #  veiculo = self.__veiculo
    #  self.__tela_veiculo.mostrar_dados(veiculo)
       
    def voltar(self):
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_veiculo, 2: self.listar_veiculos, 0: self.voltar}

        lista_opcoes[self.__tela_veiculo.tela_opcoes()]()

