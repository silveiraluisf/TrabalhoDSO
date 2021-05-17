import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText

class TelaPesquisarVeiculo():

    def __init__(self):
        self.__window = None

    def init_components(self):
        layout = [[sg.Text('Digite a placa do veículo')],
                  [sg.Text('Placa', size=(15, 1)), sg.InputText(key='placa')],
                  [sg.Submit()]]

        self.__window = sg.Window('Pesquisar veículo').Layout(layout)


    def pesquisar_veiculo_placa(self):
        self.init_components()
        button, values = self.__window.Read()
        self.__window.Close()
        return values['placa']