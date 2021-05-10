class TelaOS():

    def tela_opcoes(self):
        #exibe as informações da tela de cliente
        print("")
        print("")
        print("====================================")
        print("========= ORDEM DE SERVIÇO =========")
        print("====================================")
        print("")
        print("--------- Selecione a opção: -------")
        print("")
        print("1 - Criar Ordem de Serviço")
        print("2 - Editar Ordem de Serviço")
        print("3 - Listar Ordens de Serviço")
        print("4 - Excluir Ordem de Serviço")
        print("5 - Pesquisiar Ordem de Serviço")
        print("0 - Voltar")
        print("")
        print("")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return opcao

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