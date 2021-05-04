class TelaVeiculo():

    def tela_opcoes(self):
        print("-------- Veiculo ---------")
        print("Escolha sua opcao")
        print("1 - Criar veiculo")
        print("2 - Listar veiculos")
        print("3 - Pesquisar veiculo pela placa")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_veiculo(self):
        print("-------Incluir Veiculo-------")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        ano = input("Ano: ")
        quilometragem = input("Quilometragem: ")

        return {"modelo": modelo, "placa": placa, "ano": ano, "quilometragem": quilometragem}

    def mostrar_veiculos(self, dados_veiculo):
        print("--------DADOS DO VEÍCULO---------")
        print("MODELO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    def pesquisar_veiculo_placa(self):
        print("")
        print("------ Pesquisa de veiculo pela placa:-------")
        print("")
        print("")

        placa = input("Digite a placa a ser pesquisada: ")
        
        return placa

    def resultado_veiculo_placa(self, dados_veiculo):
        print("====== RESULTADO DA PESQUISA: ======")
        print("")
        print("MODELO DO VEICULO: ", dados_veiculo["modelo"])
        print("PLACA: ", dados_veiculo["placa"])
        print("ANO: ", dados_veiculo["ano"])
        print("QUILOMETRAGEM: ", dados_veiculo["quilometragem"], "km")
        print("")

    #def mostrar_dados(self, veiculo):
    #    print("Modelo do veiculo: ", veiculo.modelo)
    #    print("Ano do veiculo: ", veiculo.ano)
    #    print("Placa do veiculo: ", veiculo.placa)
    #    print("Quilometragem do veiculo: ", veiculo.quilometragem)