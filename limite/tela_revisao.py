import PySimpleGUI as sg

class TelaRevisao():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('REVISAO', justification='center', size=(30, 1))],
                  [sg.Button('Criar Revisao', key='1', size=(30, 1))],
                  [sg.Button('Listar Revisao', key='2', size=(30, 1))],
                  [sg.Button('Pesquisar Revisao Pela Placa', key='3', size=(30, 1))],
                  [sg.Button('Editar Revisao', key='4', size=(30, 1))],
                  [sg.Button('Excluir Revisao', key='5', size=(30, 1))],
                  [sg.Button('Voltar', key='0', size=(30, 1))]]
                  
        self.__window = sg.Window('Tela Revisao').Layout(layout)

    def tela_opcoes(self):
        self.init_components()    
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0

        self.fechar_tela()

        return int(botao)

    def fechar_tela(self):
        self.__window.Close()

    def pega_dados_revisao(self):
        print("")
        print("------- INSIRA OS DADOS DA REVISÃO: -------")
        codigo = input("Codigo: ")
        quilometragem = input("Quilometragem: ")
        verificacao = [input("Itens de verificação: ")]
        substituicao = [input("Itens de substituicao: ")]
        return {"codigo": codigo, "quilometragem": quilometragem, "verificacao": verificacao, "substituicao": substituicao}

    def listar_revisoes(self, revisao):
        print("")
        print("CODIGO:", revisao["codigo"])
        print("QUILOMETRAGEM:", revisao["quilometragem"])
        print("ITENS DE VERIFICACAO:", revisao["verificacao"])
        print("ITENS DE SUBSTITUICAO:", revisao["substituicao"])
        print("")

    def pesquisar_revisao_codigo(self):
        print("")
        print("------ DIGITE O CODIGO DA REVISAO ------ ")
        print("")
        print("")

        codigo = input("Codigo da revisão: ")

        return codigo

    def sucesso(self):
        print("")
        print("")
        print("------ OPERAÇÃO REALIZADA ------")
        print("--------- COM SUCESSO !! -------")

    def falha(self):
        print("")
        print("")
        print("------- NÃO FOI POSSÍVEL -------")
        print("----- CONCLUIR A OPERAÇÃO! -----")
