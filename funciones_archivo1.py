import csv

class Libro:

    def __init__(self,id,titulo,genero,ISBN,editorial,autores):
        self.id        = id
        self.titulo    = titulo  
        self.genero    = genero
        self.ISBN      = ISBN
        self.editorial = editorial
        self.autores   = autores

    def leerLibros():
        with open("libros.csv") as f:
            leer = csv.reader(f)
            next(leer)
            num=0
            for i in leer: 
                num+=1
                print("Id:{0}, Titulo:{1}, Genero:{2}, ISBN:{3}, Editorial:{4}, Autores:{5}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                if num>2:
                    break
        print("\n")