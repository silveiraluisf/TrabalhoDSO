import PySimpleGUI as sg 

class PopUpSucesso():

    def __init__(self):
        self.__window = None

    def init_components(self):

        self.__window = sg.Popup('SUCESSO','Operação realizada com sucesso!')

    def sucesso(self):
        self.init_components()
      


