from curso_tema import Tema_curso
from curso_tema_video import Tema_video
from empleado import Empleado
from curso import Curso
from video import Video
from tema import Tema

def agregar_empleado():
    print("ingrese el id del Empleado: ")
    id_del_empleado = input()
    print("Ingrese el nombre del Empleado: ")
    nombre_del_empleado = input()
    print("Ingrese la direccion del Empleado: ")
    direccion_del_empleado = input()

    crear_empleado = Empleado(id_del_empleado,nombre_del_empleado,direccion_del_empleado)
    crear_empleado.guardar()

def agregar_curso():
    print("ingrese el id del curso: ")
    id_del_curso = input()
    print("Ingrese la descripcion del curso: ")
    descripcion_del_curso = input()
    print("Ingrese la id del Empleado: ")
    id_del_empleado = input()

    crear_curso = Curso(id_del_curso,descripcion_del_curso,id_del_empleado)
    crear_curso.guardar()

def agregar_video():
    print("ingrese el id del video: ")
    id_del_video = input()
    print("Ingrese el nombre del video: ")
    nombre_del_video = input()
    print("Ingrese la url del video: ")
    url_del_video = input()
    print("Ingrese la fecha de publicacion del video: ")
    fechapublicacion_del_video = input()

    crear_video = Video(id_del_video,nombre_del_video,url_del_video,fechapublicacion_del_video)
    crear_video.guardar()

def agregar_tema():
    print("ingrese el id del tema: ")
    id_del_tema = input()
    print("Ingrese el nombre del tema: ")
    nombre_del_tema = input()

    crear_tema = Tema(id_del_tema,nombre_del_tema)
    crear_tema.guardar()

def agregar_temaVideo():
    print("ingrese el id del tema del video: ")
    id_del_temaVideo = input()
    print("Ingrese el id del tema del curso: ")
    id_del_temaCurso = input()
    print("Ingrese el id del video: ")
    id_del_Video = input()

    crear_temaVideo = Tema_video(id_del_temaVideo, id_del_temaCurso, id_del_Video)
    crear_temaVideo.guardar()

def agregar_temaCurso():
    print("ingrese el id del tema del curso: ")
    id_del_temaCurso = input()
    print("Ingrese el id del curso: ")
    id_del_Curso = input()
    print("Ingrese el id del tema: ")
    id_del_Tema = input()

    crear_temaCurso = Tema_curso(id_del_temaCurso,id_del_Curso,id_del_Tema)
    crear_temaCurso.guardar()

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
            agregar_empleado()
            break
        elif opcion_empleados == 2:
            Empleado.consultar_todo()
            break
        elif opcion_empleados == 3:
            print("??Cual es la id del empleado que desea buscar?")
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
            agregar_curso()
            break
        elif opcion_cursos == 2:
            Curso.consultar_todo()
            break
        elif opcion_cursos == 3:
            print("??Cual es la id del curso que desea buscar?")
            id_curso_buscar = input()
            Curso.consultar_por_id(Curso, id_curso_buscar)
            break
    
    elif opcion == 3:
        print("Videos")
        print("1. Registrar video")
        print("2. Mostrar todos los videos")
        print("3. Buscar video por id")

        opcion_videos = int(input())

        if opcion_videos == 1:
            agregar_video()
            break
        elif opcion_cursos == 2:
            Video.consultar_todo()
            break
        elif opcion_cursos == 3:
            print("??Cual es la id del video que desea buscar?")
            id_video_buscar = input()
            Video.consultar_por_id(Video, id_video_buscar)
            break

    elif opcion == 4:
        print("Temas")
        print("1. Registrar tema")
        print("2. Mostrar todos los temas")
        print("3. Buscar tema por id")

        opcion_temas = int(input())

        if opcion_temas == 1:
            agregar_tema()            
            break
        elif opcion_temas == 2:
            Tema.consultar_todo()
            break
        elif opcion_temas == 3:
            print("??Cual es la id del tema que desea buscar?")
            id_tema_buscar = input()
            Video.consultar_por_id(Video, id_tema_buscar)
            break
    
    elif opcion == 5:
        print("Temas del video del curso")
        print("1. Registrar tema del video")
        print("2. Mostrar todos los temas de los videos")
        print("3. Buscar tema del video por id")

        opcion_temas_videos = int(input())

        if opcion_temas_videos == 1:
            agregar_temaVideo()            
            break
        elif opcion_temas_videos == 2:
            Tema_video.consultar_todo()
            break
        elif opcion_temas_videos == 3:
            print("??Cual es la id del tema de video que desea buscar?")
            id_temaVideo_buscar = input()
            Tema_video.consultar_por_id(Tema_video, id_temaVideo_buscar)
            break

    elif opcion == 6:
        print("Temas del curso")
        print("1. Registrar tema del curso")
        print("2. Mostrar todos los temas de los cursos")
        print("3. Buscar tema del curso por id")

        opcion_temas_cursos = int(input())

        if opcion_temas_cursos == 1:
            agregar_temaCurso()()            
            break
        elif opcion_temas_cursos == 2:
            Tema_curso.consultar_todo()
            break
        elif opcion_temas_cursos == 3:
            print("??Cual es la id del tema del curso que desea buscar?")
            id_temaCurso_buscar = input()
            Tema_curso.consultar_por_id(Tema_curso, id_temaCurso_buscar)
            break

    elif opcion == 7:
        salir = True
        break
    
