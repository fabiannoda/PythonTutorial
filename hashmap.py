stra=hash("hola123.")
str2=hash(input())
lista=["hola123/", "angel15/"]
flag=True
while flag:
    if stra==str2:
        print(lista)
        flag=False
    else:
        print("contraseña erronea")
        str2=hash(input())