'''
def FuncionPares(limite):
    num=1
    lista=[]
    for i in range(limite):
        lista.append(num*2)
        num+=1
    
    return lista

print(FuncionPares(10))

def generaPares(limite):
    num=1
    for i in range(limite):
        yield num*2
        num+=1
    
pares=generaPares(10)

print(next(pares))
print(" ")
print(next(pares))
'''
def ciudades(*ciudades):
    for i in ciudades:
        #for j in i:
        yield from i

ciudadesD=ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesD))