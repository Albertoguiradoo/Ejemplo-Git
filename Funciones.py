'''
edad = 5

edad_como_texto = str(edad)
edad= int(edad_como_texto)

print(edad/5)

print(len("Juan"))

edad2 = int(input("Dime tu edad:"))
'''

#Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola ",nombre,apellido)

imprimirHola("Juan", "Zamora")


def imprimirSuma(num1:int, num2:int):
    #print("La suma de", num1, "+", num2,"=", num1+num2)
    return num1+num2

suma=imprimirSuma(2,3)
print("La suma es de: ", suma)