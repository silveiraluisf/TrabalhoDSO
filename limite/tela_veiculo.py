import PySimpleGUI as sg

class TelaVeiculo():

    def __init__(self):
        self.__window = None
        self.init_components_tela_opcoes()
        self.init_components_pega_dados_veiculo()

    def init_components_tela_opcoes(self):
        layout = [[sg.Text('VEÍCULO', justification='center', size=(30, 1))],
                  [sg.Button('Criar Veiculo', key='1', size=(30, 1))],
                  [sg.Button('Listar Veiculo', key='2', size=(30, 1))],
                  [sg.Button('Pesquisar Veiculo Pela Placa', key='3', size=(30, 1))],
                  [sg.Button('Editar Veiculo', key='4', size=(30, 1))],
                  [sg.Button('Excluir Veiculo', key='5', size=(30, 1))],
                  [sg.Button('Voltar', key='6', size=(30, 1))]]
                  
        self.__window = sg.Window('Tela Veiculo').Layout(layout)

    def tela_opcoes(self):
        self.init_components_tela_opcoes()    
        botao, valores = self.__window.Read()
        return int(botao)

    def fechar_tela(self):
        self.__window.close()

    def init_components_pega_dados_veiculo(self):
        layout = [[sg.Text('Insira os dados do veículo')],
        [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo')],
        [sg.Text('Placa', size=(15, 1)), sg.InputText(key='placa')],
        [sg.Text('Ano', size=(15, 1)), sg.InputText(key='ano')],
        [sg.Text('Quilometragem', size=(15, 1)), sg.InputText(key='quilometragem')],
        [sg.Submit(), sg.Cancel()]]
        
        self.__window = sg.Window('Dados do veículo').Layout(layout)


    def pega_dados_veiculo(self):
        self.init_components_pega_dados_veiculo()
        button, values = self.__window.Read()
        return {"modelo": values['modelo'], "placa": values['placa'], "ano": values['ano'], "quilometragem": values['quilometragem']}

    def mostrar_veiculos(self, dados_veiculo):
        print("")
        print("--------DADOS DO VEÍCULO---------")
        print("MODELO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    def pesquisar_veiculo_placa(self):
        print("")
        print("------ DIGITE A PLACA DO VEÍCULO: -------")
        print("")
        print("")

        placa = input("Placa do veículo: ")
        
        return placa

    def resultado_veiculo_placa(self, dados_veiculo):
        print("====== RESULTADO DA PESQUISA: ======")
        print("")
        print("MODELO DO VEICULO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    def falha(self):
        print("")
        print("")
        print("------- NÃO FOI POSSÍVEL -------")
        print("----- CONCLUIR A OPERAÇÃO! -----")

    def sucesso(self):
        print("")
        print("")
        print("------ OPERAÇÃO REALIZADA ------")
        print("--------- COM SUCESSO !! -------")
