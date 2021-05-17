import PySimpleGUI as sg

class TelaCadastroVeiculo():
    
    def __init__(self):
        self.__window = None
        self.init_components() 

    def init_components(self):
        layout = [[sg.Text('Insira os dados do veículo')],
                  [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo')],
                  [sg.Text('Placa', size=(15, 1)), sg.InputText(key='placa')],
                  [sg.Text('Ano', size=(15, 1)), sg.InputText(key='ano')],
                  [sg.Text('Quilometragem', size=(15, 1)), sg.InputText(key='quilometragem')],
                  [sg.Submit(), sg.Cancel()]]
        
        self.__window = sg.Window('Dados do veículo').Layout(layout)


    def pega_dados_veiculo(self):
        self.init_components()
        button, values = self.__window.Read()
        self.fechar_tela()
        return {"modelo": values['modelo'], "placa": values['placa'], "ano": values['ano'], "quilometragem": values['quilometragem']}

    def fechar_tela(self):
        self.__window.Close()