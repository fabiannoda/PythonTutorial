dicci={"Alemania":"Berlín", "Francia":"París", "Colombia":"Bogotá", "España":"Madrid"}
print(dicci["Francia"])
#Agregar mas elemnetos
dicci["Italia"]="Lisboa"
print(dicci)
#MOdificar
dicci["Italia"]="Roma"
print(dicci)
#Eliminar
del dicci["Italia"]
print(dicci)
#Diccionario con distintos tipos de datos
dicci2={"Nombre":"Angel", "Fecha":291099, 5:True}
print(dicci2)
#Convertir tupla en dicc
tupla=("España", "Francia", "Alemania")
dicc3={tupla[0]:"Madrid", tupla[1]:"Paris", tupla[2]:"Berlín"}
print(dicc3)
#Imprimir el valor asociado a una  clave 
print(dicc3["España"])
#Almacenar una tupla en un dicc
dicc4={23:"Jordan", "Nombre":"Michael", "Activo": False, "Anillos":[1991, 1992, 1993, 1996, 1997]}
print(dicc4["Anillos"])
#Dicc dentro de otro dicc
dicc5={23:"Jordan", "Nombre":"Michael", "Activo": False, "Anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997]}}
print(dicc5)
#llaves de un dicc
print(dicc5.keys())
#Valores
print(dicc5.values())
#length
print(len(dicc5))