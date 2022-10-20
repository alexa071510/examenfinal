"""Uso del condicional life"""

var1=int(input("Ingrese su primer valor numerico:"))
var2=int(input("Ingrese su segundo valor numerico:"))

edad= int(input(":Cual es su edad:"))

if 0<edad<18:
    print("El valor de var1 es mayor que la segunda variable ingresada")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 100 >= edad >65:
    print("Usted es una persona de tercera edad")
else:
    print("El valor de var1 no es mayor que la segunda variable ingresada")

