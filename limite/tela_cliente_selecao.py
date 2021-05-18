import PySimpleGUI as sg


class TelaSelecaoCliente():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Selecione o tipo de cliente:', justification='center', size=(30, 1))],
            [sg.Button('Pessoa Física', key='1', size=(30, 1))],
            [sg.Button('Pessoa Jurídica', key='2', size=(30, 1))],
            [sg.Button('Voltar', key='0', size=(30, 1))]
        ]

        self.__window = sg.Window('Tipo de Cliente').Layout(layout)

    def tela_selecao_cliente(self):

        self.init_components()

        botao, valores = self.__window.Read()

        if botao is None:
            botao = 0

        return int(botao)