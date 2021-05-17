import PySimpleGUI as sg

class TelaMostrarVeiculo():
    
    def __init__(self):
        self.__window = None

    def init_components(self, veiculos):
            layout = [[sg.Text('Dados do veículo')],
                      [sg.Listbox(values= veiculos, size=(60,10))],
                      [sg.Submit()]]

            self.__window = sg.Window('Lista dos veiculos').Layout(layout)

    
    def mostrar_veiculos(self, veiculos):
        self.init_components(veiculos)
        button, values = self.__window.Read()
        self.__window.Close() 
        return button, values