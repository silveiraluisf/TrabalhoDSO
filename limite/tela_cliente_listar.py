import PySimpleGUI as sg

class TelaLisatrClientes():

    def __init__(self):
        self.__window = None

    def init_components(self, lista_clientes):

        layout = [
            [sg.Text('Dados do cliente')],
            [sg.Listbox(values=lista_clientes, size=(60, 10))],
            [sg.Submit()]
        ]

        self.__window = sg.Window('Lista de clientes').Layout(layout)

    def lista_clientes(self, lista_clientes):

        self.init_components(lista_clientes)

        button, values = self.__window.Read()

        self.__window.Close()

        return button, values

