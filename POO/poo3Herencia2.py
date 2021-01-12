class persona():
    def __init__(self, nombre, edad, direccion):
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion
    
    def descrip(self):
        return "Nombre: "+ self.nombre+ "\nEdad: "+str(self.edad)+"\nDireccion: "+self.direccion

class empleado(persona):
    def __init__(self, nombre, edad, direccion, salario, antigue):
        super().__init__(nombre, edad, direccion)
        self.salario=salario
        self.anti=antigue
    
    def descrip(self):
        return super().descrip()+"\nSalario: "+str(self.salario)+"\nAntigüedad: "+str(self.anti)


antonio=empleado("Antonio", 55, "Tu puta madre", 1500, 5)
manuel=persona("manuel", 45, "lkasjfkgoefw")
print(antonio.descrip())
print(issubclass(empleado, persona))
print(isinstance(antonio, persona))
print(isinstance(manuel, empleado))