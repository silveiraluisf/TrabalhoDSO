import PySimpleGUI as sg

class TelaOS:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('ORDEM DE SERVIÇO', justification='center', size=(30, 1))],
                  [sg.Button('Criar ordem de serviço', key='1', size=(30, 1))],
                  [sg.Button('Editar ordem de serviço', key='2', size=(30, 1))],
                  [sg.Button('Listar ordens de serviço', key='3', size=(30, 1))],
                  [sg.Button('Excluir ordem de serviço', key='4', size=(30, 1))],
                  [sg.Button('Pesquisar ordem de serviço', key='5', size=(30, 1))],
                  [sg.Button('Voltar', key='0', size=(30, 1))]]
                  
        self.__window = sg.Window('Tela Cliente').Layout(layout)

    def tela_opcoes(self):
        self.init_components()    
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0

        self.fechar_tela()

        return int(botao)

    def fechar_tela(self):
        self.__window.Close()

    def coleta_data(self):

        while True:
            try:
                data = str(input("Informe a data da OS: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return data


    def listar_os(self, os):

        print("")
        print("NÚMERO:", os["numero"])
        print("DATA DA OS:", os["data"])
        print("VEÍCULO:", os["veiculo"])
        print("PLACA:", os["placa"])
        print("CÓDIGO:", os["codigo"])
        print("KM:", os["quilometragem"])
        print("VERIFICAÇÃO:", os["verificacao"])
        print("SUBSTITUIÇÃO:", os["substituicao"])
        print("")

    def exibir_os(self, os):

        print("")
        print("NÚMERO:", os.numero)
        print("DATA DA OS:", os.data)
        print("VEÍCULO:", os.veiculo.modelo)
        print("PLACA:", os.veiculo.placa)
        print("CÓDIGO:", os.revisao.codigo)
        print("KM:", os.revisao.quilometragem)
        print("VERIFICAÇÃO:", os.revisao.verificacao)
        print("SUBSTITUIÇÃO:", os.revisao.substituicao)
        print("")

    def pesquisar_numero_os(self):
        print("")
        print("------ DIGITE O CODIGO DA ------")
        print("--------ORDEM DE SERVIÇO--------")
        print("")

        codigo = int(input("Codigo da OS: "))

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