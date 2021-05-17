import PySimpleGUI as sg

class TelaMostrarVeiculo():
    
    def __init__(self):
        self.__window = None

    def init_components_mostrar_veiculo(self, veiculo):
        layout = [[sg.Text('Dados do veículo')],
                  [sg.Listbox(values= {"modelo": veiculo.modelo, 
            "placa": veiculo.placa, "ano": veiculo.ano, "quilometragem": veiculo.quilometragem }, size=(60,10))],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Lista dos veiculos').Layout(layout)

    
    def mostrar_veiculos(self, veiculo):
        self.init_components_mostrar_veiculo(veiculo)
        button, values = self.__window.Read()
        self.__window.Close() 
        return button, values