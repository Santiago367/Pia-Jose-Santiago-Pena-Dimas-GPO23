class Tema:
    def __init__(self, id_tema = 1, nombre = "fsfs"):
        self.__id_tema = id_tema
        self.__nombre = nombre

    @property
    def id_tema(self):
        return self.__id_tema
    
    @property
    def nombre(self):
        return self.__nombre

    def guardar(self):
        archivo = open("tema.txt", "a")
        archivo.write(self.id_tema)
        archivo.write("|")
        archivo.write(self.nombre)
        archivo.write("\n")
        archivo.close()