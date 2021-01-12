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
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, 
        "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)

class moto(vehiculo):
    hcaballo=""
    def caballito(self):
        self.hcaballo="Voy haciendo el caballo"
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, 
        "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\n", self.hcaballo)

class furgo(vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.ruedas=ruedas
    
    def cargar(self, cargar):
        self.cargar=cargar
        if self.cargar:
            return "Cargada"
        else:
            return "No se ha cargado"

class vElectrico(vehiculo):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autono=autonomia

    def cargarEner(self):
        self.cargando=True

class biciElec(vElectrico):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo, autonomia)



