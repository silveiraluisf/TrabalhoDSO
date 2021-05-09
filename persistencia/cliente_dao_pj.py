from persistencia.DAO import DAO
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica

class ClientePJDAO(DAO):
    def __init__(self):
        super().__init__('clientepj.pkl')
    
    def add(self, cliente: ClientePessoaJuridica):
        if (cliente is not None) \
                and isinstance(cliente, ClientePessoaJuridica):
            super().add(cliente.cnpj, cliente)

    def get(self, cliente: ClientePessoaJuridica):
        if (cliente is not None) \
                and isinstance(cliente, ClientePessoaJuridica):
            return super().get(cliente.cnpj)

    def remove(self, cliente: ClientePessoaJuridica):
         if (cliente is not None) \
                  and isinstance(cliente, ClientePessoaJuridica):
            super().remove(cliente.cnpj)