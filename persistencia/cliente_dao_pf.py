from persistencia.DAO import DAO
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica

class ClientePFDAO(DAO):
    def __init__(self):
        super().__init__('clientepf.pkl')

    def add(self, cliente: ClientePessoaFisica):
        if (cliente is not None) \
                and isinstance(cliente, ClientePessoaFisica):
            super().add(cliente.cpf, cliente)

    def get(self, cliente: ClientePessoaFisica):
        if (cliente is not None) \
                and isinstance(cliente, ClientePessoaFisica):
            return super().get(cliente.cpf)

    def remove(self, cliente: ClientePessoaFisica):
         if (cliente is not None) \
                  and isinstance(cliente, ClientePessoaFisica):
            super().remove(cliente.cpf)





