mitupla=(1, 2 , "angel", True, 1, 1)
print(mitupla.__getitem__(0))
lista1=[12, 58, "angelito", False]
tupla2=tuple(lista1)
milista=list(mitupla)
#print(milista)
#print(tupla2)
#Metodo para saber si un elemento esta en una tupla
print("angel" in mitupla)
#Cuantas veces se encuentra un elemento en una tupla
print(mitupla.count(1))
#.length()
print(len(mitupla))
#Tupla unitaria
tupla3=("Angel",)
print(len(tupla3))
#se puede escribir una tupla sin parentesis (Empaquetando de tupla)
tupla4="angel", True, 58, 25
#Desempaquetado de tupla
tupla5=("Angel", 16, 7, 2020)
nombre, dia, mes, agno=tupla5
print(nombre)
print(agno)
#Busqueda de index
print(tupla5.index("Angel"))
