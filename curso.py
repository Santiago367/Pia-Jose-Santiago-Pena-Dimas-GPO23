class Curso:
    def __init__(self, id_curso = 1, descripcion = "Descripcion de ejemplo", id_empleado = "1"):
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
    
    def consultar_todo():
        archivo = open("curso.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            print(datos[0],datos[1],datos[2])
        archivo.close()

    def consultar_por_id(self, id_buscadoCurso):
        archivo = open("curso.txt", "r")
        for linea in archivo:
            datos = linea.strip().split('|')
            if datos[0] == id_buscadoCurso:
                print(datos[0],datos[1],datos[2])
        archivo.close()