"""DEL"""

"""Listas(del):eliminar un dato de la lista indicando el indice"""

lista=[]
lista.append(2022)
lista.append("Setiembre")
lista.append("Modulo 1")
lista.append(40)

print(lista)

del lista[2]
print("Mi lista actualizada es:{}".format(lista))

""""""
del lista[6]