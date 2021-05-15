from abc import ABC, abstractmethod  
import pickle

class DAO(ABC):

    @abstractmethod
    def __init__(self, datasource = ''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()

        except FileNotFoundError:
            self.__dumb()

    def __dumb(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj # se não mudar a chave, não precisa de utilizar o remove
        self.__dumb()

    def get(self, key):
        try: 
            return self.__cache[key]
        except KeyError:
            pass 

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dumb()
        except KeyError:
            pass 

    def get_all(self):
        return self.__cache.values()