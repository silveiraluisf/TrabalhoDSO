class TelaVeiculo():

    def tela_opcoes(self):
        print("-------- Veiculo ---------")
        print("Escolha sua opcao")
        print("1 - Criar veiculo")
        print("2 - Listar veiculos")
        print("3 - Pesquisar veiculo pela placa")
        print("4 - Editar veiculo")
        print("5 - Excluir veiculo")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opcao: "))
        
            except ValueError:
                print("Comando inválido. Digite um comando válido")
            
            else:
                return opcao

    def pega_dados_veiculo(self):
        print("")
        print("------- INSIRA OS DADOS DO VEÍCULO: -------")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        ano = input("Ano: ")
        quilometragem = int(input("Quilometragem: "))

        return {"modelo": modelo, "placa": placa, "ano": ano, "quilometragem": quilometragem}

    def mostrar_veiculos(self, dados_veiculo):
        print("")
        print("--------DADOS DO VEÍCULO---------")
        print("MODELO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    def pesquisar_veiculo_placa(self):
        print("")
        print("------ DIGITE A PLACA DO VEÍCULO: -------")
        print("")
        print("")

        placa = input("Placa do veículo: ")
        
        return placa

    def resultado_veiculo_placa(self, dados_veiculo):
        print("====== RESULTADO DA PESQUISA: ======")
        print("")
        print("MODELO DO VEICULO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    def falha(self):
        print("")
        print("")
        print("------- NÃO FOI POSSÍVEL -------")
        print("----- CONCLUIR A OPERAÇÃO! -----")

    def sucesso(self):
        print("")
        print("")
        print("------ OPERAÇÃO REALIZADA ------")
        print("--------- COM SUCESSO !! -------")
