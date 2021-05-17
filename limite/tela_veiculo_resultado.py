import PySimpleGUI as sg

class TelaVeiculoResultado():

    def __init__(self):
        self.__window = None 
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Digite a placa do veículo')],
                  [sg.Text('Placa', size=(15, 1)), sg.InputText()],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Pesquisar veículo').Layout(layout)

    def resultado_veiculo_placa(self, dados_veiculo):
        self.init_components()
        button, values = self.__window.Read()
        return str(values)