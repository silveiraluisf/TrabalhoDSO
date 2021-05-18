import PySimpleGUI as sg

class TelaVeiculo():

    def __init__(self):
        self.__window = None
        self.init_components_tela_opcoes()

    def init_components_tela_opcoes(self):
        layout = [[sg.Text('VEÍCULO', justification='center', size=(30, 1))],
                  [sg.Button('Criar Veiculo', key='1', size=(30, 1))],
                  [sg.Button('Listar Veiculo', key='2', size=(30, 1))],
                  [sg.Button('Pesquisar Veiculo Pela Placa', key='3', size=(30, 1))],
                  [sg.Button('Editar Veiculo', key='4', size=(30, 1))],
                  [sg.Button('Excluir Veiculo', key='5', size=(30, 1))],
                  [sg.Button('Voltar', key='0', size=(30, 1))]]
                  
        self.__window = sg.Window('Tela Veiculo').Layout(layout)

    def tela_opcoes(self):

        self.init_components_tela_opcoes()

        botao, valores = self.__window.Read()

        if botao is None:
            botao = 0

        self.fechar_tela()

        return int(botao)

    def fechar_tela(self):
        self.__window.Close()

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
