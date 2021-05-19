from empleado import Empleado

empleado3 = Empleado("5","ejemplo4","Avenida23")

idej = "12"
nomej = "lolo"
direj = "democr"

while not salir:
 
    print ("1. Administrar Empleados")
    print ("7. Salir")

    print ("Elige una opcion")
    opcion = input()
 
    if opcion == 1:
        print("Empleados")
        print("1. Registrar Empleado")
        print("2. Mostrar todos los empleados")
        print("3. Buscar empleado por id")

        opcion_empleados = input()
        if opcion_empleados == 1:
            print("ingrese el id del Empleado: ")
            id_del_empleado = input()
            print("Ingrese el nombre del Empleado: ")
            nombre_del_empleado = input()
            print("Ingrese la direccion del Empleado: ")
            direccion_del_empleado = input()

            crear_empleado = Empleado(id_del_empleado,nombre_del_empleado,direccion_del_empleado)
            crear_empleado.guardar()
    elif opcion == 7:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

crear_empleado = Empleado(idej,nomej,direj)

crear_empleado.guardar()
Empleado.consultar_por_id(Empleado, "5")
