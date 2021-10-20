class Pokemon:
    def __init__(self, id, tipo, nome):
        self.__id   = int(id)
        self.__tipo = str(tipo)
        self.__nome = str(nome)

    @property
    def id(self):
        return self.__id

    @property
    def tipo(self):
        return self.__tipo

    @property
    def nome(self):
        return self.__nome
