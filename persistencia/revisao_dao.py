from persistencia.DAO import DAO
from entidade.revisao.revisao import Revisao 

class RevisaoDAO(DAO):
    def __init__(self):
        super().__init__('revisao.pkl')

    def add(self, revisao: Revisao):
        if (revisao is not None) \
                and isinstance(revisao, Revisao):
            super().add(revisao.quilometragem, revisao)

    def get(self, revisao: Revisao):
        if (revisao is not None) \
                and isinstance(revisao, Revisao):
            return super().get(revisao.quilometragem)

    def remove(self, revisao: Revisao):
        if (revisao is not None) \
                and isinstance(revisao, Revisao):
            super().remove(revisao.quilometragem)