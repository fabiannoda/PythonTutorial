def evaluacion(nota):
    if nota>=3:
        print("Aprobado")
    else:
        print("Suspenso")

#nota=input("meta la nota")
#evaluacion(float(nota))

#edad=int(input("Introduce tu edad "))
#USO DE ELIF
'''
edad=0
if edad<18:
    print("No puede pasar")
elif edad>100:
    print("No te la creo")
else:
    print("Puedes pasar")
'''
#CONCATENACION DE OPERADORES
'''
edad=10
if 0<edad<100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

'''

'''
presi=int(input("Salario del presidente: "))
print("Salario presidente: "+str(presi))
dire=int(input())
jefe=int(input())
admin=int(input())
if admin<jefe<dire<presi:   
    print("todo va bien")
else:
    print("ALgo va mal")
    
'''
#Operadores Logicos and y or
'''
distancia = 10
herma = 5
sala = 1500
if distancia>40 and herma>2 or sala<2000:      
    print("Tiene beca wapo")
else:
    print("buscate el dinero puta")
'''
#operador in
valor = "Software 2"

if valor.lower() in ("software 2", "puto el que lo lea"):
    print("puedes inscribir")
else:
    print("no wapo")
'''
for i in range(6):
    print(i)
    evaluacion(i)
'''