class Tema:
    def __init__(self, id_tema = 1, nombre = "Tema ejemplo"):
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

    def consultar_todo():
        archivo = open("tema.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            print(datos[0],datos[1])
        archivo.close()

    def consultar_por_id(self, id_buscadoTema):
        archivo = open("tema.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            if datos[0] == id_buscadoTema:
                print(datos[0],datos[1])
        archivo.close()