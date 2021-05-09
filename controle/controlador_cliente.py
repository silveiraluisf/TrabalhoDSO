from limite.tela_cliente import TelaCliente
from entidade.cliente.abstractCliente import AbstractCliente
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica
from persistencia.cliente_dao_pf import ClientePFDAO
from persistencia.cliente_dao_pj import ClientePJDAO
from entidade.veiculo.veiculo import Veiculo

class ControladorCliente():

    def __init__(self, controlador_sistema):
        self.__dao_pf = ClientePFDAO()
        self.__dao_pj = ClientePJDAO() 
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema
        
    def cadastrar_cliente(self):

        # Método para definir se vai cadastrar pessoa física ou jurídica

        lista_tipos_cliente = {1: self.cadastra_pessoa_fisica, 2: self.cadastra_pessoa_juridica, 0: self.voltar}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()
    
    def cadastra_pessoa_fisica(self):

        # Método para fazer o cadastro de cliente pessoa física

        dados_cliente = self.__tela_cliente.coleta_dados_pessoa_fisica()
        
        dados_veiculo = self.__controlador_sistema.pegar_veiculo()

        cliente = ClientePessoaFisica(int(dados_cliente["codigo"]), dados_cliente["nome"], 
        dados_cliente["telefone"], dados_cliente["endereco"], dados_cliente["data_nascimento"], 
        dados_cliente["cpf"], dados_cliente["rg"], dados_cliente["orgao_emissor"], dados_veiculo)
        
        self.__dao_pf.add(cliente)

        self.__tela_cliente.sucesso()

        self.abre_tela()


    def cadastra_pessoa_juridica(self):

        # Método para fazer o cadastro de cliente pessoa física

        dados_cliente = self.__tela_cliente.coleta_dados_pessoa_juridica()
        
        dados_veiculo = self.__controlador_sistema.pegar_veiculo()

        cliente = ClientePessoaJuridica(dados_cliente["codigo"], dados_cliente["nome"], dados_cliente["telefone"], 
        dados_cliente["endereco"], dados_cliente["data_fundacao"], dados_cliente["cnpj"], dados_veiculo)

        self.__dao_pj.add(cliente)

        self.__tela_cliente.sucesso()

        self.abre_tela()

    def remover_cliente(self):
        escolher_tipo_cliente = {1: self.remover_cliente_pf_pelo_nome, 2: self.remover_cliente_pj_pelo_nome, 0: self.voltar_tela_cliente}

        continua_tela_cliente = True

        while continua_tela_cliente:
            escolher_tipo_cliente[self.__tela_cliente.tipo_de_cliente()]()

    def remover_cliente_pf_pelo_nome(self):

        nome = self.__tela_cliente.pesquisar_cliente_pf_pelo_nome()

        for cliente in self.__dao_pf.get_all():

            if nome != cliente.nome:
                pass

            else:
                self.__dao_pf.remove(cliente)
                self.__tela_cliente.sucesso()
                self.abre_tela()

        self.__tela_cliente.falha()
        self.remover_cliente_pf_pelo_nome()

    def remover_cliente_pj_pelo_nome(self):

        nome = self.__tela_cliente.pesquisar_cliente_pj_pelo_nome()

        for cliente in self.__dao_pj.get_all():

            if nome != cliente.nome:
                pass

            else:
                self.__dao_pj.remove(cliente)
                self.__tela_cliente.sucesso()
                self.abre_tela()

        self.__tela_cliente.falha()
        self.remover_cliente_pf_pelo_nome()

    def editar_cliente(self):
        escolher_tipo_cliente = {1: self.editar_cliente_pf, 2: self.editar_cliente_pj, 0: self.voltar_tela_cliente}

        continua_tela_cliente = True

        while continua_tela_cliente:
            escolher_tipo_cliente[self.__tela_cliente.tipo_de_cliente()]()

    def editar_cliente_pf(self):

        nome = self.__tela_cliente.pesquisar_cliente_pf_pelo_nome()

        for cliente in self.__dao_pf.get_all():

            if nome == cliente.nome:

                novas_infos_cliente = self.__tela_cliente.coleta_dados_pessoa_fisica()

                novo_veiculo = self.__controlador_sistema.pegar_veiculo()

                cliente_editado = ClientePessoaFisica(int(novas_infos_cliente["codigo"]), novas_infos_cliente["nome"],
                                                      novas_infos_cliente["telefone"],
                                                      novas_infos_cliente["endereco"],
                                                      novas_infos_cliente["data_nascimento"],
                                                      novas_infos_cliente["cpf"],
                                                      novas_infos_cliente["rg"], novas_infos_cliente["orgao_emissor"],
                                                      novo_veiculo)

                self.__dao_pf.remove(cliente)
                self.__dao_pf.add(cliente_editado)
                break
        else:
                print("Cliente não encontrado")

    def editar_cliente_pj(self):

        nome = self.__tela_cliente.pesquisar_cliente_pj_pelo_nome()

        for cliente in self.__dao_pj.get_all():

            if nome == cliente.nome:

                novas_infos_cliente = self.__tela_cliente.coleta_dados_pessoa_juridica()

                novo_veiculo = self.__controlador_sistema.pegar_veiculo()

                cliente_editado = ClientePessoaJuridica(novas_infos_cliente["codigo"], novas_infos_cliente["nome"],
                                                        novas_infos_cliente["telefone"], novas_infos_cliente["endereco"],
                                                        novas_infos_cliente["data_fundacao"], novas_infos_cliente["cnpj"],
                                                        novo_veiculo)

                self.__dao_pj.remove(cliente)
                self.__dao_pj.add(cliente_editado)
                break
        
        else:
                print("Cliente não encontrado")

    def listar_clientes(self):

        lista_tipos_cliente = {1: self.listar_clientes_pf, 2: self.listar_clientes_pj, 0: self.voltar_tela_cliente}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()
 
    def listar_clientes_pf(self):

        self.__tela_cliente.inicio_de_lista()

        for cliente in self.__dao_pf.get_all():
            self.__tela_cliente.listar_clientes_pf({'codigo': cliente.codigo, "nome": cliente.nome, 
            "telefone": cliente.telefone, "endereco": cliente.endereco, "data_nascimento": cliente.data_nascimento, 
            "cpf": cliente.cpf, "rg": cliente.rg, "orgao_emissor": cliente.orgao_emissor, 
            "veiculo": cliente.veiculo.modelo, "placa": cliente.veiculo.placa})

        self.__tela_cliente.fim_de_lista()

        self.abre_tela()

    def listar_clientes_pj(self):

        self.__tela_cliente.inicio_de_lista()

        for cliente in self.__dao_pj.get_all():
            self.__tela_cliente.listar_clientes_pj({"codigo": cliente.codigo, "nome": cliente.nome, 
            "telefone": cliente.telefone, "endereco": cliente.endereco, "data_fundacao": cliente.data_fundacao, 
            "cnpj": cliente.cnpj, "veiculo": cliente.veiculo.modelo, "placa": cliente.veiculo.placa})

        self.__tela_cliente.fim_de_lista()

        self.abre_tela()

    def pesquisar_cliente_pelo_nome(self):

        lista_tipos_cliente = {1: self.pesquisar_cliente_pf_pelo_nome, 2: self.pesquisar_cliente_pj_pelo_nome, 0: self.voltar_tela_cliente}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()

    def pesquisar_cliente_pf_pelo_nome(self):

        nome = self.__tela_cliente.pesquisar_cliente_pf_pelo_nome()

        for cliente in self.__dao_pf.get_all():

            if nome == cliente.nome:

                self.__tela_cliente.resultado_cliente_pf_pelo_nome(
                    {'codigo': cliente.codigo, "nome": cliente.nome, "telefone": cliente.telefone,
                     "endereco": cliente.endereco, "data_nascimento": cliente.data_nascimento, "cpf": cliente.cpf,
                     "rg": cliente.rg, "orgao_emissor": cliente.orgao_emissor, "veiculo": cliente.veiculo.modelo,
                     "placa": cliente.veiculo.placa})

                return cliente

        self.__tela_cliente.falha()
        self.pesquisar_cliente_pf_pelo_nome()



    def pesquisar_cliente_pj_pelo_nome(self):

        nome = self.__tela_cliente.pesquisar_cliente_pj_pelo_nome()

        for cliente in self.__dao_pj.get_all():

            if nome == cliente.nome:

                self.__tela_cliente.resultado_cliente_pj_pelo_nome(
                    {"codigo": cliente.codigo, "nome": cliente.nome, "telefone": cliente.telefone,
                     "endereco": cliente.endereco, "data_fundacao": cliente.data_fundacao, "cnpj": cliente.cnpj,
                     "veiculo": cliente.veiculo.modelo, "placa": cliente.veiculo.placa})

                return cliente

        self.__tela_cliente.falha()
        self.pesquisar_cliente_pj_pelo_nome()

    def pegar_cliente_pf(self):
        nome = self.__tela_cliente.pesquisar_cliente_pf_pelo_nome()

        for cliente in self.__dao_pf.get_all():
            if nome != cliente.nome:
                pass

            else:
                self.__dao_pf.get(cliente.nome)
                return cliente 

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.remover_cliente, 3: self.editar_cliente, 4: self.listar_clientes, 5: self.pesquisar_cliente_pelo_nome, 0: self.voltar}

        continua = True
        while continua:
   
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def voltar_tela_cliente(self):
        self.abre_tela()

    def abrir_area_em_contrucao(self):
        
        voltar = {0: self.voltar}

        while True:
            voltar[self.__tela_cliente.area_em_construcao()]()
