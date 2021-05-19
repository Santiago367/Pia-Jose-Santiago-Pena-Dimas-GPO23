class Empleado:
    def __init__(self, id_curso = 1, descripcion = "fsfs", id_empleado = "Calle"):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado

    @property
    def id_curso(self):
        return self.__id_curso
    
    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def id_empleado(self):
        return self.__id_empleado

    def guardar(self):
        archivo = open("curso.txt", "a")
        archivo.write(self.id_curso)
        archivo.write("|")
        archivo.write(self.descripcion)
        archivo.write("|")
        archivo.write(self.id_empleado)
        archivo.write("\n")
        archivo.close()