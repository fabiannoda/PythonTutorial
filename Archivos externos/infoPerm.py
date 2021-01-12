import pickle
class persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas():
    personas=[]
    def __init__(self):
        file_personas=open("Fichero_de_Personas", "ab+")
        file_personas.seek(0)
        try:
            self.personas=pickle.load(file_personas)
            print("Se cargaron {} personas".format(len(self.personas)))
        except:
            print("El fichero esta vacío")
        finally:
            file_personas.close()
            del(file_personas)
        

    def agregarPer(self, p):
        self.personas.append(p)
        self.insertarFicher()

    def insertarFicher(self):
        file_personas=open("Fichero_de_Personas", "wb")
        pickle.dump(self.personas, file_personas)
        file_personas.close()
        del(file_personas)
    def mostrarPer(self):
        for i in self.personas:
            print(i)
    def __str__(self):
        hola=""
        for i in self.personas:
            hola+=""+i.__str__()+"\n"
        return hola 

milista=listaPersonas()
print(milista)
'''
p=persona("Angel", "Male", 20)
milista.agregarPer(p)
p=persona("Felipe", "Male", 22)
milista.agregarPer(p)
p=persona("Sara", "Female", 40)
milista.agregarPer(p)'''


