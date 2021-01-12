import pickle
'''
lista_nom=["Pedro", "Ana", "María", "Isabel"]
fichero=open("Lista_nombres", "wb")
pickle.dump(lista_nom, fichero)
fichero.close()
del(fichero)
'''
fichero=open("Lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista)