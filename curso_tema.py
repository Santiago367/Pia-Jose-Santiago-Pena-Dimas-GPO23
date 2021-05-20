class Tema_curso:
    def __init__(self, id_CT = 1, id_curso = 1, id_tema = 1):
        self.__id_CT = id_CT
        self.__id_curso = id_curso
        self.__id_tema = id_tema

    @property
    def id_CT(self):
        return self.__id_CT
    
    @property
    def id_curso(self):
        return self.__id_curso
    
    @property
    def id_tema(self):
        return self.__id_tema

    