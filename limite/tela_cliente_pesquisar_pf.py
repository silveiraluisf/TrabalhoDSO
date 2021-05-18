import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText

class TelaPesquisarClientePF():

    def __init__(self):
        self.__window = None

    def init_components(self):
        layout = [[sg.Text('Digite o campo a ser pesquisado')],
                  [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome')],
                  [sg.Submit()]]

        self.__window = sg.Window('Pesquisar cliente PF').Layout(layout)



    def pesquisar_nome_pf(self):

        self.init_components()

        button, values = self.__window.Read()

        self.__window.Close()

        return values['nome']