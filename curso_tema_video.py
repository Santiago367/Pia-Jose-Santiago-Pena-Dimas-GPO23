class Tema_video:
    def __init__(self, id_CTV = 1, id_CT = 1, id_video = 1):
        self.__id_CTV = id_CTV
        self.__id_CT = id_CT
        self.__id_video = id_video
    
    @property
    def id_CTV(self):
        return self.__id_CTV
    
    @property
    def id_CT(self):
        return self.__id_CT
    
    @property
    def id_video(self):
        return self.__id_video

    def guardar(self):
        archivo = open("curso_tema_video.txt", "a")
        archivo.write(self.id_CTV)
        archivo.write("|")
        archivo.write(self.id_CT)
        archivo.write("|")
        archivo.write(self.id_video)
        archivo.write("\n")
        archivo.close()

    def consultar_todo():
        archivo = open("curso_tema_video.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            print(datos[0],datos[1],datos[2])
        archivo.close()

    def consultar_por_id(self, id_buscadoTemaVideo):
        archivo = open("curso_tema_video.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            if datos[0] == id_buscadoTemaVideo:
                print(datos[0],datos[1],datos[2])
        archivo.close()