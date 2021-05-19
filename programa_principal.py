from empleado import Empleado

salir = False

while not salir:
 
    print ("1. Administrar Empleados")
    print ("7. Salir")

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
    
    elif opcion == 7:
        salir = True
        break
    


