
"""
3.Crear una funcion donde el usuario ingresa un numero entero.
Requisitos:
-La función debe indicar si el numero ingresado es primo o no.
-Retornar True si el numero es primo si no retornar False.
"""
def primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True

num=int(input("Ingrese el numero a evaluar:"))
if primo(num):
    print("El numero {} es primo".format(num))
else:
    print("El numero {} no es primo".format(num))