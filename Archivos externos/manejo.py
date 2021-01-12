from io import open
#write w--read r--append a--write and read r+
archivo=open("textito.txt","r+")
archivo.write("comienzo del texto")
lista_texto=archivo.readlines()
lista_texto[2]="Esta linea ha sido incluidad desde el exterior \n"
archivo.seek(0)
archivo.writelines(lista_texto)
archivo.close()
#print(archivo.readlines())
#archivo.seek(len(archivo.read())/2)
#print(archivo.read())

#print(archivo.read(20))
#archivo.seek(20)
#print(archivo.read())
'''
archivo.write("\nsigo funcionando")
archivo.close()
''''''
lineas=archivo.readlines()
archivo.close()
print(lineas)
''''''
txto=archivo.read()
archivo.close()
print(txto)
'''
#frase="hola mundo en otro archivo \n vamossssss \n funcione puto"
#archivo.write(frase)
#archivo.close()