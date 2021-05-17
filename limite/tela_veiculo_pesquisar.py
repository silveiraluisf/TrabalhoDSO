import PySimpleGUI as sg

class TelaPesquisarVeiculo():

    def __init__(self):
        self.__window = None

    def init_components_pesquisar_veiculo_placa(self):
        layout = [[sg.Text('Digite a placa do veículo')],
                  [sg.Text('Placa', size=(15, 1)), sg.InputText()],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Pesquisar veículo').Layout(layout)


    def pesquisar_veiculo_placa(self):
        self.init_components_pesquisar_veiculo_placa()
        button, values = self.__window.Read()
        return str(values)