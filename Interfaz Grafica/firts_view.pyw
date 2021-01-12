from tkinter import *

raiz = Tk()
#titulo de la ventana
raiz.title("Ventana de pruebas")
#evitar que se pueda cambiar el tamaño
raiz.resizable(0,0)
#que se pueda dimensionar
raiz.resizable(1,1)
#cambiar el icono de la ventana
#raiz.iconbitmap('ima.ico')
#poner tamaño
raiz.geometry("650x350")
#cambiar el color de fondo
raiz.config(bg="green")
raiz.mainloop()