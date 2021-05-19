from empleado import Empleado
from curso import Curso

salir = False

while not salir:
 
    print("1. Administrar Empleados")
    print("2. Administrar Cursos")
    print("7. Salir")

    print ("Elige una opcion2")
    opcion = int(input())
 
    if opcion == 1:
        print("Empleados")
        print("1. Registrar Empleado")
        print("2. Mostrar todos los empleados")
        print("3. Buscar empleado por id")

        opcion_empleados = int(input())
        if opcion_empleados == 1:
            print("ingrese el id del Empleado: ")
            id_del_empleado = input()
            print("Ingrese el nombre del Empleado: ")
            nombre_del_empleado = input()
            print("Ingrese la direccion del Empleado: ")
            direccion_del_empleado = input()

            crear_empleado = Empleado(id_del_empleado,nombre_del_empleado,direccion_del_empleado)
            crear_empleado.guardar()
            break
        elif opcion_empleados == 2:
            Empleado.consultar_todo()
            break
        elif opcion_empleados == 3:
            print("¿Cual es la id que desea buscar?")
            id_empleado_buscar = input()
            Empleado.consultar_por_id(Empleado, id_empleado_buscar)
            break
        break

    elif opcion == 2:
        print("Cursos")
        print("1. Registrar curso")
        print("2. Mostrar todos los cursos")
        print("3. Buscar curso por id")

        opcion_cursos = int(input())

        if opcion_cursos == 1:
            print("ingrese el id del curso: ")
            id_del_curso = input()
            print("Ingrese la descripcion del curso: ")
            descripcion_del_curso = input()
            print("Ingrese la id del Empleado: ")
            id_del_empleado = input()

            crear_curso = Curso(id_del_curso,descripcion_del_curso,id_del_empleado)
            crear_curso.guardar()
            break
        elif opcion_cursos == 2:
            Curso.consultar_todo()
            break
        elif opcion_cursos == 3:
            print("¿Cual es la id que desea buscar?")
            id_curso_buscar = input()
            Curso.consultar_por_id(Curso, id_curso_buscar)
            break
    elif opcion == 7:
        salir = True
        break
    


