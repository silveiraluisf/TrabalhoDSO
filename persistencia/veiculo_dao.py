from persistencia.DAO import DAO
from entidade.veiculo.veiculo import Veiculo 

class VeiculoDAO(DAO):
    def __init__(self):
        super().__init__('veiculo.pkl')

    def add(self, veiculo: Veiculo):
        if (veiculo is not None) \
                and isinstance(veiculo, Veiculo):
            super().add(veiculo.placa, veiculo)

    def get(self, veiculo: Veiculo):
        if (veiculo is not None) \
                and isinstance(veiculo, Veiculo):
            return super().get(veiculo.placa)

    def remove(self, veiculo: Veiculo):
        if (veiculo is not None) \
                and isinstance(veiculo, Veiculo):
            super().remove(veiculo.placa)