import PySimpleGUI as sg

class TelaClientePFResultado():

    def __init__(self):
        self.__window = None

    def init_components(self, cliente):
        layout = [[sg.Text('Cliente', size=(15, 1)), sg.Text(str(cliente.nome))],
                  [sg.Submit()]]

        self.__window = sg.Window('Resultado da Pesquisa').Layout(layout)

    def listar_resultado(self, cliente):

        self.init_components(cliente)

        button, values = self.__window.Read()

        self.__window.Close()
