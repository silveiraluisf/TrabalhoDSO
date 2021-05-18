import PySimpleGUI as sg

class TelaCadastroPF():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Insira os dados do cliente')],
                  [sg.Text('Código', size=(15, 1)), sg.InputText('Informe aqui o código do cliente', key='codigo')],
                  [sg.Text('Nome', size=(15, 1)), sg.InputText('Informe aqui o nome do cliente', key='nome')],
                  [sg.Text('Telefone', size=(15, 1)), sg.InputText('Informe aqui o telefone do cliente', key='telefone')],
                  [sg.Text('Endereço', size=(15, 1)), sg.InputText('Informe aqui o endereço do cliente', key='endereco')],
                  [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('Informe aqui a data de nascimento do cliente', key='data_nascimento')],
                  [sg.Text('CPF', size=(15, 1)), sg.InputText('Informe aqui o CPF do cliente', key='cpf')],
                  [sg.Text('RG', size=(15, 1)), sg.InputText('Informe aqui o RG do cliente', key='rg')],
                  [sg.Text('Órgão Emissor', size=(15, 1)), sg.InputText('Informe aqui o Órgão Emissor', key='orgao_emissor')],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Dados do Cliente PF').Layout(layout)

    def coleta_dados_cliente(self):

        self.init_components()

        button, values = self.__window.Read()

        self.fechar_tela()

        return {"codigo": values['codigo'], "nome": values['nome'], "telefone": values['telefone'], "endereco": values['endereco'],
                "data_nascimento": values['data_nascimento'], "cpf": values['cpf'], "rg": values['rg'], "orgao_emissor": values['orgao_emissor']}

    def fechar_tela(self):
        self.__window.Close()



        # while True:
        #     try:
        #         codigo = int(input("Defina um Código para o Cliente: "))
        #
        #     except ValueError:
        #         print("Conteúdo Inválido. Digite o conteúdo correto.")
        #     else:
        #         break
        #
        # nome = input("Nome: ")
        #
        # while True:
        #     try:
        #         telefone = int(input("Telefone: "))
        #     except ValueError:
        #         print("Conteúdo Inválido. Digite o conteúdo correto.")
        #     else:
        #         break
        #
        # endereco = input("Endereço: ")
        # data_nascimento = input("Data de Nascimento: ")
        # cpf = input("CPF: ")
        # rg = input("R.G.: ")
        # orgao_emissor = input("Órgão Emissor: ")
        #
        # return {"codigo": codigo, "nome": nome, "telefone": telefone, "endereco": endereco,
        #         "data_nascimento": data_nascimento, "cpf": cpf, "rg": rg, "orgao_emissor": orgao_emissor}
        #
