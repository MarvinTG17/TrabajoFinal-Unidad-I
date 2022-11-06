from funciones_archivo1 import *

def menu_principal():
    print("\n--------MENU DE BIENVENIDA--------")
    print("\nEscoga un numero del menu:")
    print("Opcion 1 : Leer archivo")
    print("Opcion 2 : Listar libro")
    print("Opcion 3 : Agregar libro")
    print("Opcion 4 : Eliminar libro")
    print("Opcion 5 : Buscar libro por ISBN o por título.")
    print("Opcion 6 : Ordenar libros por titulo")
    print("Opcion 7 : Buscar libros por autor, editorial o género.")
    print("Opción 8 : Buscar libros por número de autores.")
    print("Opcion 9 : Editar o actualizar datos de un libro")
    print("Opcion 10: Guardar libros en archivo.")
    print("Opcion 0 : Salir")

    opcion = input("\nIngresar la opcion de su preferencia: ")

    return opcion

while True:
    op = menu_principal()

    if op == "1":
        #print("Leer archivo")
        Libro.leerLibros()
        break
    elif op == "2":
            print("\nLISTAR TODOS LOS LIBROS\n")
            Libro.listarLibros()

    elif op == "3":
        print("\nAGREGAR UN LIBRO A LA LISTA")
        titulo    = input("\nIngresar titulo: ")
        genero    = input("\nIngresar genero: ")
        ISBN      = input("\nIngresar ISBN: ")
        editorial = input("\nIngresar editorial: ")
        autores   = input("\nIngresar autor: ")

        if titulo=="" or genero=="" or ISBN=="" or editorial=="" or autores=="":
            print("\nERROR: Ingreso un dato vacio.")
        else:
            ide = Libro.enumerarID()
            resultado = Libro(ide,titulo,genero,ISBN,editorial,autores)
            resultado.agregarLibro()
            Libro.listarLibros()

    elif op == "4":
        print("\nELIMINAR UN LIBRO\n")
        Libro.listarLibros()
        id =  input("\nElegir el ID para eliminar un libro completo: ")
        resp = Libro(id,"","","","","")
        resp.eliminarLibro()
        print("\n")
        Libro.listarLibros()

    elif op == "5":
        print("\nBUSCAR LIBRO POR ISBN O POR TITULO\n")
        print("Opcion 1 : Buscar por ISBN")
        print("Opcion 2 : Buscar por titulo")
        opc = input("\nEscoge el numero de opcion: ")
        if opc == "1":
            isbn=input("\nIngresar nombre de ISBN:")
            rpta = Libro("","","",isbn,"","")
            rpta.buscarLibroTI()
        elif opc == "2":
            titulo=input("\nIngresar nombre de titulo:")
            rpta = Libro("",titulo,"","","","")
            rpta.buscarLibroTI()
        else: 
            print("\nERROR: opcion erronea o dato vacio.")
        
    elif op == "6":
        print("\nORDENAR LIBROS POR TITULO\n")
        Libro.ordenarLibro()