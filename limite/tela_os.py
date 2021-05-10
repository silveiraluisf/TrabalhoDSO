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