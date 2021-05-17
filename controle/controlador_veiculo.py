from limite.tela_veiculo import TelaVeiculo
from limite.tela_veiculo_cadastro import TelaCadastroVeiculo
from limite.tela_veiculo_mostrar import TelaMostrarVeiculo
from limite.tela_veiculo_pesquisar import TelaPesquisarVeiculo
from limite.tela_veiculo_resultado import TelaVeiculoResultado
from entidade.veiculo.veiculo import Veiculo
from persistencia.veiculo_dao import VeiculoDAO 

class ControladorVeiculo():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__dao = VeiculoDAO() 
        self.__tela_veiculo = TelaVeiculo()
        self.__tela_veiculo_cadastro = TelaCadastroVeiculo()
        self.__tela_veiculo_mostrar = TelaMostrarVeiculo()
        self.__tela_veiculo_pesquisar = TelaPesquisarVeiculo()
        self.__tela_veiculo_resultado = TelaVeiculoResultado

    def cadastrar_veiculo(self):
        dados_veiculo = self.__tela_veiculo_cadastro.pega_dados_veiculo()

        veiculo = Veiculo(dados_veiculo["modelo"], dados_veiculo["placa"], dados_veiculo["ano"], 
        dados_veiculo["quilometragem"])

        self.__dao.add(veiculo)

        self.abre_tela()

    def listar_veiculos(self):
        veiculos = list() 
        for veiculo in self.__dao.get_all():
            veiculos.append(
                str('Modelo:') + str(veiculo.modelo) + ' | ' +
                str('Placa:') + str(veiculo.placa) + ' | ' +
                str('Ano:') + str(veiculo.ano) + ' | ' +
                str('Quilometragem:') + str(veiculo.quilometragem))
            
        self.__tela_veiculo_mostrar.mostrar_veiculos(veiculos)
            

        self.abre_tela()

    def pesquisar_veiculo_placa(self):
        #metodo que permite encontrar um veiculo especifico pela placa
        placa = self.__tela_veiculo_pesquisar.pesquisar_veiculo_placa()
        
        for veiculo in self.__dao.get_all():
            if placa == veiculo.placa:
                self.__tela_veiculo_resultado.resultado_veiculo_placa({"modelo": veiculo.modelo, "placa": veiculo.placa, "ano": veiculo.ano, "quilometragem": veiculo.quilometragem})

        return veiculo 

    def editar_veiculo(self):

        placa = self.__tela_veiculo_pesquisar.pesquisar_veiculo_placa()

        for veiculo in self.__dao.get_all():
            if placa == veiculo.placa:
                novo_veiculo = self.__tela_veiculo_cadastro.pega_dados_veiculo()

                veiculo_editado = Veiculo(novo_veiculo["modelo"], novo_veiculo["placa"], novo_veiculo["ano"], novo_veiculo["quilometragem"])

                self.__dao.remove(veiculo)
                self.__dao.add(veiculo_editado)
                self.__tela_veiculo.sucesso()
                break

        else: 
            self.__tela_veiculo.falha()

        self.abre_tela()

    def excluir_veiculo(self):
        placa = self.__tela_veiculo_pesquisar.pesquisar_veiculo_placa()

        for veiculo in self.__dao.get_all():
            if placa == veiculo.placa:
                self.__dao.remove(veiculo) 
                self.__tela_veiculo.sucesso()
                break 
        else: 
            self.__tela_veiculo.falha()

        self.abre_tela()

    def pegar_veiculo(self):
        placa = self.__tela_veiculo_pesquisar.pesquisar_veiculo_placa()

        for veiculo in self.__dao.get_all():
            if placa != veiculo.placa:
                pass
            else:
                self.__dao.get(veiculo.placa)
                return veiculo
        
        #else: 
        #    print("Veiculo não encontrado")
         
    def voltar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_veiculo, 2: self.listar_veiculos, 3: self.pesquisar_veiculo_placa, 
        4: self.editar_veiculo, 5: self.excluir_veiculo, 0: self.voltar}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_opcoes[self.__tela_veiculo.tela_opcoes()]()

