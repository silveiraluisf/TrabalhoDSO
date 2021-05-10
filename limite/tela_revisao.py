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
        quilometragem = input("Quilometragem: ")
        return {"quilometragem": quilometragem}


    

#    def listar_revisoes(self, dados_cliente, lista_substituicoes, lista_verificacoes, dados_veiculo):
#        print("====== CÓDIGO CLIENTE: ", dados_cliente.codigo,"======")
#        print("")        
#        print("NOME CLIENTE: ", dados_cliente.nome)
#        print("FONE CLIENTE: ", dados_cliente.telefone)
#        print("END CLIENTE: ", dados_cliente.endereco)
#        print("DATA NASC.: ", dados_cliente.data_nascimento)
#        print("CPF: ", dados_cliente.cpf)
#        print("R.G.: ", dados_cliente.rg)
#        print("ÓRGÃO EMISSOR: ", dados_cliente.orgao_emissor)
#        print("")
#        print("")
#        print("--------DADOS DO VEÍCULO---------")
#        print("MODELO: ", dados_veiculo.modelo)
#        print("PLACA: ", dados_veiculo.placa)
#        print("ANO: ", dados_veiculo.ano)
#       print("QUILOMETRAGEM: ", dados_veiculo.quilometragem, "km")
#        print("")
#        print("")        
#        print("")
#        print("------- LISTA DOS ITENS DE REVISÃO: ---------")

#        for i in lista_substituicoes:
#            print("[  ] ", i.descricao)
        
#        print("----------------------")

#        for v in lista_verificacoes:
#            print("[  ] ", v.descricao)
        
