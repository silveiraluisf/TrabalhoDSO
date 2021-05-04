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
        veiculo = Veiculo(dados_veiculo["modelo"], dados_veiculo["placa"], dados_veiculo["ano"], 
        dados_veiculo["quilometragem"])

        self.__veiculos.append(veiculo)

        self.abre_tela()

    def listar_veiculos(self):
        for veiculo in self.__veiculos:
            self.__tela_veiculo.mostrar_veiculos({"modelo": veiculo.modelo, 
            "placa": veiculo.placa, "ano": veiculo.ano, "quilometragem": veiculo.quilometragem })

        self.abre_tela()

    def pesquisar_veiculo_placa(self):
        
        placa = self.__tela_veiculo.pesquisar_veiculo_placa()

        for veiculo in self.__veiculos:
            if placa == veiculo.placa:
                self.__tela_veiculo.resultado_veiculo_placa({"modelo": veiculo.modelo, "placa": veiculo.placa, "ano": veiculo.ano, "quilometragem": veiculo.quilometragem})

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

    #def excluir_veiculo(self):
    #  veiculo = self.__veiculo 
    # del (veiculo)
        
    #def mostrar_veiculo(self):
    #  veiculo = self.__veiculo
    #  self.__tela_veiculo.mostrar_dados(veiculo)
       
    def voltar(self):
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_veiculo, 2: self.listar_veiculos, 3: self.pesquisar_veiculo_placa, 0: self.voltar}

        lista_opcoes[self.__tela_veiculo.tela_opcoes()]()

