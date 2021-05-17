import PySimpleGUI as sg 

class TelaSistema:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('SISTEMA DE CONTROLE DE SERVIÇOS VEICULARES', justification='center', size=(20, 1))],
                  [sg.Button('Veiculos', key='1', size=(20, 1))],
                  [sg.Button('Revisao', key='2', size=(20, 1))],
                  [sg.Button('Clientes', key='3', size=(20, 1))],
                  [sg.Button('Ordem de Serviço', key='4', size=(20, 1))],
                  [sg.Button('Sair', key='0', size=(20, 1))]]
                  
        self.__window = sg.Window('Sistema Veiculo').Layout(layout)

    def tela_opcoes(self):
        self.init_components()    
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        return int(botao)

    def fechar_tela(self):
        self.__window.Close()

