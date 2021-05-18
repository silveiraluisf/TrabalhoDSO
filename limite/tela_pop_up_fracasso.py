import PySimpleGUI as sg

class PopUpFracasso():

    def __init__(self):
        self._window = None 

    def init_components(self):

        self.__window = sg.Popup('FALHA','Operação não realizada!')

    def falha(self):
        self.init_components()
