class Video:
    def __init__(self, id_video = 1, nombre = "fsfs", url = "Calle", fecha_publicacion = "12/03/2020"):
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