class Empleado:
    def __init__(self, id_empleado = 1, nombre = "fsfs", direccion = ""):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__direccion = direccion
    
    @property
    def id_empleado(self):
        return self.__id_empleado
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    def guardar(self):
        archivo = open("empleado.txt", "a")
        archivo.write("hola")

archivo = open("empleado.txt", "a")
archivo.write("hola")
archivo.close()
