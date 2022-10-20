"""DICCIONARIOS EN PYTHON"""

diccionario={"nombre":"Python","tipo":"backend"}

print("Nuestro primer diccionario tiene este contenido:{}".format(diccionario))

"""Para eliminar valores de nuestro diccionario usamos: del"""

del diccionario["tipo"]
print("Mi diccionario actualizado es:{}".format(diccionario))

del diccionario["nombre"]
print("Mi diccionario actualizado es:{}".format(diccionario))