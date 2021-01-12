class carro():
    def desplazo(self):
        print("me desplazo con 4 ruedas")

class moto():
    def desplazo(self):
        print("me desplazo con 2 ruedas")

class camion():
    def desplazo(self):
        print("me desplazo con 6 ruedas")

vehiculo=moto()
vehiculo.desplazo()

def desplazami(vehiculo):
    vehiculo.desplazo()

vehiculo=camion()
desplazami(vehiculo)