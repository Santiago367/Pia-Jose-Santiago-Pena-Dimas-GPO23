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
