import pickle
from serialiObjet import vehiculo

file=open("Lista_objetos", "rb")
miscoches=pickle.load(file)
file.close()
for i in miscoches:
    print(i)