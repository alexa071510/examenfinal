"""Manejo de impresión de valores de una cadena de caracteres"""
"""Tercera manera de imprimir valores"""

nombre=input("Ingrese su nombre:")
edad=input("Ingrese su edad:")

print(f"Bienvenido {nombre} usted tiene {edad} años")

"""Cuarta manera de imprimir valores"""

print("Bienvenido {nombre} usted tiene {edad} años".format(nombre=nombre,edad=edad))
