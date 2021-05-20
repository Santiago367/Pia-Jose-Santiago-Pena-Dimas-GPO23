class Tema:
    def __init__(self, id_tema = 1, nombre = "fsfs", direccion = "Calle"):
        self.__id_tema = id_tema
        self.__nombre = nombre

    @property
    def id_tema(self):
        return self.__id_tema
    
    @property
    def nombre(self):
        return self.__nombre

    