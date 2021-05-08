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
        #metodo que permite encontrar um veiculo especifico pela placa 
        placa = self.__tela_veiculo.pesquisar_veiculo_placa()

        for veiculo in self.__veiculos:
            if placa == veiculo.placa:
                self.__tela_veiculo.resultado_veiculo_placa({"modelo": veiculo.modelo, "placa": veiculo.placa, "ano": veiculo.ano, "quilometragem": veiculo.quilometragem})

            return veiculo 

    def editar_veiculo(self):

        veiculo_pesquisado = self.pesquisar_veiculo_placa()

        for veiculo in range(len(self.__veiculos)):
            if self.__veiculos[veiculo].placa == veiculo_pesquisado.placa:
                novo_veiculo = self.__tela_veiculo.pega_dados_veiculo()

                veiculo_editado = Veiculo(novo_veiculo["modelo"], novo_veiculo["placa"], novo_veiculo["ano"], novo_veiculo["quilometragem"])

                self.__veiculos[veiculo] = veiculo_editado

                self.abre_tela()

    def excluir_veiculo(self):
        placa = self.__tela_veiculo.pesquisar_veiculo_placa()

        for veiculo in self.__veiculos:
            if placa == veiculo.placa:
                self.__veiculos.remove(veiculo) 
                print("----OK: Veículo removido! ----")
        else: 
            print("Veiculo não encontrado")
       
    def voltar(self):
        self.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_veiculo, 2: self.listar_veiculos, 3: self.pesquisar_veiculo_placa, 
        4: self.editar_veiculo, 5: self.excluir_veiculo, 0: self.voltar}

        lista_opcoes[self.__tela_veiculo.tela_opcoes()]()

