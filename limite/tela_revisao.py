class TelaRevisao():

    def tela_opcoes(self):
        print("-------- Revisao ---------")
        print("Escolha sua opcao")
        print("1 - Criar item de revisao")
        print("2 - Listar itens de revisao")
        print("3 - Excluir item de revisao")
        print("4 - Editar item de revisao")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

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
