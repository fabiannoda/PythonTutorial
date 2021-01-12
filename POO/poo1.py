#Construcciones Basicas
class carro():
    def __init__(self):
        self.__largo=250
        self.__ancho=120
        self.__ruedas=4
        self.__enMarcha=False

    #Métodos
    def Arrancar(self, arrancamos):
        if arrancamos:
            chequeo=self.__chequeo()
        self.__enMarcha=arrancamos
        if self.__enMarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enMarcha and chequeo==False:
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"

    def __chequeo(self):
        print("Realizando Chequeo")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="Cerradas"

        if self.gasolina=="ok" and self.puertas=="Cerradas" and self.aceite=="ok":
            return True
        else:
            return False


renau=carro()
print(renau.Arrancar(True))


chevro=carro()
print(chevro.Arrancar(False))
