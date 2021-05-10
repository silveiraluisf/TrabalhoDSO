class Revisao():
    def __init__(self, codigo: int, quilometragem: int, verificacao: [], substituicao: []):
        self.__codigo = codigo 
        self.__quilometragem = quilometragem
        self.__verificacao = verificacao
        self.__substituicao = substituicao

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def quilometragem(self) -> int:
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, quilometragem: int):
        if isinstance(quilometragem, int):
            self.__quilometragem = quilometragem

    @property
    def verificacao(self) -> []:
        return self.__verificacao

    @verificacao.setter
    def verificacao(self, verificacao: []):
        if isinstance(verificacao, []):
            self.__verificacao = verificacao

    @property
    def substituicao(self) -> []:
        return self.__substituicao

    @substituicao.setter
    def substituicao(self, substituicao: []):
        if isinstance(substituicao, []):
            self.__substituicao = substituicao


