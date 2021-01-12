import pickle
class vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True
    
    def __str__(self):
        return ""+self.marca+"\n"+self.modelo+"\n"+str(self.enMarcha)+"\n"+str(self.acelera)+"\n"+str(self.frena)

c1=vehiculo("Mazda","MX9")
c2=vehiculo("Renault","Optus")
c3=vehiculo("Chevrolet","Captiva")
coches=[c1, c2, c3]
file=open("Lista_objetos", "wb")
pickle.dump(coches, file)
file.close()
del(file)

