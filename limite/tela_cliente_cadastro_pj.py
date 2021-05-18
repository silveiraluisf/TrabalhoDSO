import PySimpleGUI as sg

class TelaCadastroPJ():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Insira os dados do cliente')],
                  [sg.Text('Código', size=(15, 1)), sg.InputText('Informe aqui o código do cliente', key='codigo')],
                  [sg.Text('Nome', size=(15, 1)), sg.InputText('Informe aqui o nome do cliente', key='nome')],
                  [sg.Text('Telefone', size=(15, 1)), sg.InputText('Informe aqui o telefone do cliente', key='telefone')],
                  [sg.Text('Endereço', size=(15, 1)), sg.InputText('Informe aqui o endereço do cliente', key='endereco')],
                  [sg.Text('Data de Fundação:', size=(15, 1)), sg.InputText('Informe aqui a data de fundação do cliente', key='data_fundacao')],
                  [sg.Text('CNPJ', size=(15, 1)), sg.InputText('Informe aqui o CNPJ do cliente', key='cnpj')],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Dados do Cliente PJ').Layout(layout)

    def coleta_dados_cliente(self):

        self.init_components()

        button, values = self.__window.Read()

        self.fechar_tela()

        return {"codigo": values['codigo'], "nome": values['nome'], "telefone": values['telefone'], "endereco": values['endereco'],
                "data_fundacao": values['data_fundacao'], "cnpj": values['cnpj']}

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
