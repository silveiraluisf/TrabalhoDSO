from persistencia.DAO import DAO
from entidade.os.os import OS

class OSDAO(DAO):
    def __init__(self):
        super().__init__('os_dao.pkl')

    def add(self, os: OS):
        if (os is not None) \
                and isinstance(os, OS):
            super().add(os.numero, os)

    def get(self, os: OS):
        if (os is not None) \
                and isinstance(os, OS):
            return super().get(os.numero)

    def remove(self, os: OS):
         if (os is not None) \
                  and isinstance(os, OS):
            super().remove(os.numero)





