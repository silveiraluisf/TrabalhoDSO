from dao.dao import DAO
from entidade.veiculo import Veiculo

class VeiculoDAO(DAO):
    def __init__(self):
        super().__init__('veiculo.pkl')

    def add(self, veiculo: Veiculo):
        if (isinstance(veiculo.placa, int)) and (veiculo is not None) and \
        isinstance(veiculo, Veiculo):
            super().add(veiculo.placa, veiculo)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        return super().remove(key) 