"""POP"""

"""Listas(pop):Quitar un elemento indicando su indice"""
lista=["Dia del descubrimiento de America",True,1000,20.8]

print("1er valor de mi lista:{}".format(lista[0]))
print("2do valor de mi lista:{}".format(lista[1]))

lista.append(False)
lista.append(800)

print("Mi lista actualizada tiene los siguientes datos:{}".format(lista))

lista.pop(1)
print("Mi lista actualizada tiene los siguientes datos:{}".format(lista))

lista.pop(0)
print("Mi lista actualizada tiene los siguientes datos:{}".format(lista))