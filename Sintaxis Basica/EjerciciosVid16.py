#Ejercicio 1
for i in range(100):
    if i%2:
        print(i, end=" ")

print("----------------------------")
#Ejercicio 2
contra = input("Ingrese una contraseña: ")
print(contra)
valid = True
if len(contra)>=8:
    for i in contra:
        if i == " ":
            valid=False
else:
    print("Contraseña erronea")
    valid=False

if valid:
    print("Contraseña OK")
else:
    print("Contraseña erronea")



        