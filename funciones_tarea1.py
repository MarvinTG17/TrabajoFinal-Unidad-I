import csv
import pandas as pd
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

    def listarLibros():
        with open("libros.csv") as f:
            listar = csv.reader(f)
            next(listar)
            for i in listar:
                print("Id:{0}, Titulo:{1}, Genero:{2}, ISBN:{3}, Editorial:{4}, Autores:{5}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
    

    def enumerarID():
        with open("libros.csv") as f:
            file = list(csv.reader(f))
            longitud = len(file)-1
            i = 0 #columna que queremos obtener
            columna = [fila[i] for fila in file]
            id = int(columna[longitud])+1
            return id

    def agregarLibro(self):
        with open("libros.csv","a",newline='') as f:
            agregar = csv.writer(f)
            datos = [self.id,self.titulo,self.genero,self.ISBN,self.editorial,self.autores]
            agregar.writerow(datos)
        print("\nSe agrego correctamente a la ultima fila.\n")

    def eliminarLibro(self):
        with open("libros.csv") as f:
            data = list(csv.reader(f))

        with open("libros.csv", "w",newline='') as f:
            writer = csv.writer(f)
            for row in data:
                if row[0] != self.id:
                    writer.writerow(row) 

    def buscarLibroTI(self):
        datos = pd.read_csv("libros.csv")
        df = pd.DataFrame(datos)
        if self.ISBN:
            condicion = df["ISBN"]==self.ISBN
            if condicion.any():
                print(df[condicion])
            else:
                print("\nEl dato ingresado no se encuentra en la lista de libros")
        elif self.titulo:
            condicion = df["titulo"]==self.titulo
            if condicion.any():
                print(df[condicion])
            else:
                print("\nEl dato ingresado no se encuentra en la lista de libros")
        
    def ordenarLibro():
        datos = pd.read_csv("libros.csv")
        orden = datos.sort_values(by="titulo")
        print(orden)
    
    def buscarLibroGEA(self):
        datos = pd.read_csv("libros.csv")
        df = pd.DataFrame(datos) 
        condicion = []
        if self.genero:
            condicion = df.genero.isin([self.genero])
            if condicion.any():
                print(df[condicion])
            else:
                 print("\nEl dato ingresado no se encuentra en la lista de libros")
        elif self.editorial:
            condicion = df.editorial.isin([self.editorial])  
            if condicion.any():
                print(df[condicion])
            else:
                 print("\nEl dato ingresado no se encuentra en la lista de libros") 
        elif self.autores:
            condicion = df.autores.isin([self.autores]) 
            if condicion.any():
                print(df[condicion])
            else:
                 print("\nEl dato ingresado no se encuentra en la lista de libros")

    def existeIdEditar(self):
        datos = pd.read_csv("libros.csv")
        df = pd.DataFrame(datos)
        condicion = df["id"]==self.id
        if condicion.any() == False:
            return 0
        else:
            return 1

    def editarLibro(self):
        datos = pd.read_csv("libros.csv")
        df = pd.DataFrame(datos)
        condicion = df["id"]==self.id
        df.loc[condicion, "titulo"]    = self.titulo
        df.loc[condicion, "genero"]    = self.genero
        df.loc[condicion, "ISBN"]      = self.ISBN
        df.loc[condicion, "editorial"] = self.editorial
        df.loc[condicion, "autores"]   = self.autores
        df.to_csv("libros.csv",index=None)
        print("\nEditado correctamente.")

    def guardarLibro():
        datos = pd.read_csv("libros.csv")
        df = pd.DataFrame(datos)
        df.to_csv('LibroExportado.csv',index=None)
        print("\nSe realizo una copia del archivo libro correctamente")
        print("con el nombre de LibroExportado")
                    