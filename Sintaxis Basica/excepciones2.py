'''
def divide():
    try:
        op1=float(input())
        op2=float(input())
        print(str(op1/op2))
    except ValueError:  
        print("Es bobo o que")
    except ZeroDivisionError:
        print("Es bobo o solo se hace")
    finally:
        print("se hizo")
    

divide()
'''
'''
def evaluaEdad(edad):
    if edad<0:      
        raise TypeError("NO sea maricon")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres mafuro"
    elif edad<100:
        return "Cuidate..."

print(evaluaEdad(15))
'''
import math
def calcula(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=int(input())
try:
    print(calcula(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

