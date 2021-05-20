class Video:
    def __init__(self, id_video = 1, nombre = "Como hacer", url = "https://ejemplo.com", fecha_publicacion = "12/03/2020"):
        self.__id_video = id_video
        self.__nombre = nombre
        self.__url = url
        self.__fecha_publicacion = fecha_publicacion

    @property
    def id_video(self):
        return self.__id_video
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def url(self):
        return self.__url
    
    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion

    def guardar(self):
        archivo = open("video.txt", "a")
        archivo.write(self.id_video)
        archivo.write("|")
        archivo.write(self.nombre)
        archivo.write("|")
        archivo.write(self.url)
        archivo.write("|")
        archivo.write(self.fecha_publicacion)
        archivo.write("\n")
        archivo.close()

    def consultar_todo():
        archivo = open("video.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            print(datos[0],datos[1],datos[2],datos[3])
        archivo.close()

    def consultar_por_id(self, id_buscadoVideo):
        archivo = open("video.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            if datos[0] == id_buscadoVideo:
                print(datos[0],datos[1],datos[2],datos[3])
        archivo.close()