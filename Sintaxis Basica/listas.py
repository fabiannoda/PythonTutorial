lista=[1, 5, True, "puto"]
lista.append("hola puto")
#Imprimir toda la lista
print(lista[:])
#Imprimir un elemnto en especifico
print(lista.__getitem__(4))
#imprimir  el ultimo elemento
print(lista.__getitem__(len(lista)-1))
#imprimir de atras para adelante
print(lista[-3])
#imprimir una porcion de lista
print(lista[0:2])
#Insertar en un punto especifico
lista.insert(2, "puto")
print(lista[:])
#insertar varios elementos
lista.extend(["hoa", "ana", "y lucia"])
print(lista[:])
#Encontrar el index de un elemento
print(lista.index("puto"))
#comprobar si el elemnto existe
print(True in lista)
#remover
lista.remove("ana")
print(lista[:])
#remover el ultimo elemento
lista.pop()
print(lista[:])
#Unir 2 listas
lista2=["sandra", "Angel"]
lista3=lista+lista2
print(lista3[:])
#Repetir una lista # de veces
lista2=lista2 * 3
print(lista2[:])