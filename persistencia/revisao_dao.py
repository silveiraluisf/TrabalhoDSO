#from persistencia.DAO import DAO
#from entidade.revisao.revisao import Revisao 

#class RevisaoDAO(DAO):
#    def __init__(self):
#        super().__init__('revisao.pkl')

#    def add(self, revisao: Revisao):
#        if (isinstance(revisao.codigo, int)) and (revisao is not None) \
#                and isinstance(revisao, Revisao):
#            super().add(revisao.codigo, revisao)

#    def get(self, key: int):
#        if isinstance(key, int):
#            return super().get(key)

#    def remove(self, key: int):
#        return super().remove(key) 