import PySimpleGUI as sg

class TelaCliente:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('CLIENTE', justification='center', size=(30, 1))],
                  [sg.Button('Cadastrar Cliente', key='1', size=(30, 1))],
                  [sg.Button('Remover Cliente', key='2', size=(30, 1))],
                  [sg.Button('Editar Cliente', key='3', size=(30, 1))],
                  [sg.Button('Excluir Cliente', key='4', size=(30, 1))],
                  [sg.Button('Pesquisar Cliente Pelo Nome', key='5', size=(30, 1))],
                  [sg.Button('Voltar', key='0', size=(30, 1))]]
                  
        self.__window = sg.Window('Tela Cliente').Layout(layout)

    def tela_opcoes(self):
        self.init_components()    
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        return int(botao)

    def fechar_tela(self):
        self.__window.Close()


    def coleta_dados_pessoa_fisica(self):

        # coleta dados de cliente pessoa física

        print("--------- Coleta de dados ----------")
        print("------------- Cliente --------------")
        print("---------- PESSOA FÍSICA -----------")
        
        #gera o código automaticamente (verificar como fazer isso"
        
        while True:
            try:
                codigo = int(input("Defina um Código para o Cliente: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                break

        nome = input("Nome: ")
        
        while True:
            try:
                telefone = int(input("Telefone: "))
            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                break                
            
        endereco = input("Endereço: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        rg = input("R.G.: ")
        orgao_emissor = input("Órgão Emissor: ")

        return {"codigo": codigo, "nome": nome, "telefone": telefone, "endereco": endereco, "data_nascimento": data_nascimento, "cpf": cpf, "rg": rg, "orgao_emissor": orgao_emissor}



    def coleta_dados_pessoa_juridica(self):

        # coleta dados de cliente pessoa jurídica
        
        print("--------- Coleta de dados ----------")
        print("------------- Cliente --------------")
        print("--------- PESSOA JURÍDICA ----------")
        
        #gera o código automaticamente (verificar como fazer isso) - DE REPENTE COM SINGLETON, com atributo na classe

        while True:
            try:
                codigo = int(input("Defina um Código para o Cliente: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                break

        nome = input("Razão Social: ")

        while True:
            try:
                telefone = int(input("Telefone: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                break

        endereco = input("Endereço: ")
        data_fundacao = input("Data de Fundação: ")
        cnpj = input("CNPJ: ")

        return {"codigo":codigo, "nome": nome, "telefone": telefone, "endereco": endereco, "data_fundacao": data_fundacao, "cnpj": cnpj}

    def tipo_de_cliente(self):
        # escolhe se é cliente pessoa física ou jurídica
        print("")
        print("--- Selecione o tipo de cliente: ---")
        print("")
        print("1 - Pessoa Física")
        print("2 - Pessoa Jurídica")
        print("0 - Voltar")
        print("")
        print("")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))

            except ValueError: #tratar erro KeyError para escolher entr 1, 2 e 0
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return opcao
 
    
    def listar_clientes_pf(self, dados_cliente):
        print("====== CÓDIGO CLIENTE: ", dados_cliente["codigo"],"======")
        print("")        
        print("NOME CLIENTE: ", dados_cliente["nome"])
        print("FONE CLIENTE: ", dados_cliente["telefone"])
        print("END CLIENTE: ", dados_cliente["endereco"])
        print("DATA NASC.: ", dados_cliente["data_nascimento"])
        print("CPF: ", dados_cliente["cpf"])
        print("R.G.: ", dados_cliente["rg"])
        print("ÓRGÃO EMISSOR: ", dados_cliente["orgao_emissor"])
        print("VEÍCULO: ", dados_cliente["veiculo"])
        print("PLACA: ", dados_cliente["placa"])
        print("")


    def listar_clientes_pj(self, dados_cliente):
        print("====== CÓDIGO CLIENTE: ", dados_cliente["codigo"],"======")
        print("")
        print("RAZÃO SOCIAL CLIENTE: ", dados_cliente["nome"])
        print("FONE CLIENTE: ", dados_cliente["telefone"])
        print("END CLIENTE: ", dados_cliente["endereco"])
        print("DATA FUND..: ", dados_cliente["data_fundacao"])
        print("CNPJ: ", dados_cliente["cnpj"])
        print("VEÍCULO: ", dados_cliente["veiculo"])
        print("PLACA: ", dados_cliente["placa"])
        print("")

    def pesquisar_cliente_pf_pelo_nome(self):
        print("")
        print("------ Pesquisa de cliente PF:-------")
        print("")
        print("")

        nome = input("Digite o nome: ")


        return nome

    def pesquisar_cliente_pj_pelo_nome(self):
        print("")
        print("------ Pesquisa de cliente PJ:-------")
        print("")
        print("")

        nome = input("Digite a razão social: ")

        return nome

    def resultado_cliente_pf_pelo_nome(self, dados_cliente):
        print("====== RESULTADO DA PESQUISA: ======")
        print("====== CÓDIGO CLIENTE: ", dados_cliente["codigo"],"======")
        print("")
        print("NOME CLIENTE: ", dados_cliente["nome"])
        print("FONE CLIENTE: ", dados_cliente["telefone"])
        print("END CLIENTE: ", dados_cliente["endereco"])
        print("DATA NASC.: ", dados_cliente["data_nascimento"])
        print("CPF: ", dados_cliente["cpf"])
        print("R.G.: ", dados_cliente["rg"])
        print("ÓRGÃO EMISSOR: ", dados_cliente["orgao_emissor"])
        print("VEÍCULO: ", dados_cliente["veiculo"])
        print("PLACA: ", dados_cliente["placa"])
        print("")


    def resultado_cliente_pj_pelo_nome(self, dados_cliente):
        print("====== RESULTADO DA PESQUISA: ======")
        print("====== CÓDIGO CLIENTE: ", dados_cliente["codigo"],"======")
        print("")
        print("RAZÃO SOCIAL CLIENTE: ", dados_cliente["nome"])
        print("FONE CLIENTE: ", dados_cliente["telefone"])
        print("END CLIENTE: ", dados_cliente["endereco"])
        print("DATA FUND..: ", dados_cliente["data_fundacao"])
        print("CNPJ: ", dados_cliente["cnpj"])
        print("VEÍCULO: ", dados_cliente["veiculo"])
        print("PLACA: ", dados_cliente["placa"])
        print("")

    def inicio_de_lista(self):
        print("")
        print("")
        print("--------------------------------")
        print("------ INÍCIO DA LISTAGEM ------")
        print("--------------------------------")
        print("")
        print("")

    def fim_de_lista(self):
        print("")
        print("")
        print("--------------------------------")
        print("------- FIM DA LISTAGEM --------")
        print("--------------------------------")
        print("")

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

    def area_em_construcao(self):
        print("================ Opa! =================")
        print("-- ESTA ÁREA AINDA ESTÁ EM CONTRUÇÃO --")
        print("--- Pressione 0 (zero) para retornar ---")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            except KeyError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return opcao