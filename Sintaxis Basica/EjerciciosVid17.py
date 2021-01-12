#Ejercicio 1
'''
ante=int(input("Ingrese el primer numero: "))
sig=int(input("Ingrese el siguiente numero: "))
while ante<sig:
    ante=sig
    sig=int(input("Ingrese el siguiente numero: "))
'''
#Ejercico 2
flag=True
lista=[]
while flag:
    nume=int(input())
    if nume>0:
        lista.append(nume)
    else:
        break
suma=0
for i in range(len(lista)):
    suma+=lista[i]

print(suma)
