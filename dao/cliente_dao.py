
class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('cliente.pkl')

    def add(self, cliente: ClientePessoaFisica):
        if (isinstance(cliente.cpf, int)) and (cliente is not None) and \
        isinstance((cliente, ClientePessoaFisica) or (cliente, ClientePessoaJuridica)):
            super().add(cliente.cpf, cliente)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        return super().remove(key)

    