'''
lista = [1, 2, 3, "Invierno"]
for i in range(len(lista)):
    print("puto")

for etaciones in ["Primavera", "Verano", "Otoño", "Invierno"]:  
    print(etaciones, end=" ")
corr = "fabian@nodarse@gmail.com"
email = True
contador_a = 0
contador_p=0
for i in corr:
    if i == "@":
        contador_a+=1
    if i == ".":
        contador_p+=1

if contador_a<2 and contador_p>0:
    print("email correcto")
else:
    print("email incorrecto")

for i in range(5,50,3):
    print(f"valor de repeticion {i}")

valor = 1
while valor<=10:
    valor+=1
    print(valor)

edad=15
valid=True
while valid:
    #edad=int(input("Introduzca su edad"))
    if edad<0:
        print("Su edad no es correcta")
    elif edad>100:
        print("NO mames")
    else:
        valid=False

import math
valid=True
intentos = 0
while valid:
    numero = int(input("Introce el numero: "))
    if intentos>3:
        print("Has consumido demasiados intentos")
        break
    elif numero<0:
        print("No se puede sacar la raiz de un numero negativo")
        intentos+=1
    else:
        sol=math.sqrt(numero)
        print(str(sol))
'''

for letra in "python":
    if letra=="h":
        continue
    print(letra)


nomb="pildoras Informáticas"
suma=0
for i in nomb:
    if i==" ":
        continue
    suma+=1

print(suma)

email="fabiannodarsegmail.com"
arroba=False
for i in email:
    if i=="@":
        arroba=True
        break       
else:
    arroba=False

print(arroba)