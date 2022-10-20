"""DICCIONARIOS EN PYTHON"""
"""Obtener elemento de una lista :paises"""

paises=[]
paises.append("Uruguay")
paises.append("Peru")
paises.append("España")
paises.append("Canada")

print("Mi lista actual es:{}".format(paises))
print("El pais de mi item 1 es:{}".format(paises[1]))
print("El pais de mi item 3 es:{}".format(paises[3]))

edades=[13,13,11,13,11,13,13,13]
print("El indice de mi edad erronea es:{}".format(edades[2]))
actualizar=edades[2]+2
edades[2]=13

print("Mi lista actualizada de edades es:{}".format(edades))