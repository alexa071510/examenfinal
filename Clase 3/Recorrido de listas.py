"""DICCIONARIOS EN PYTHON"""

"""Recorrido de una lista"""

sueldos=[1000,1500,2000,4000,5000,8000,9000]

print("Tamaño de mi lista es:{}".format(len(sueldos)))

for i in range(len(sueldos)):
    print(sueldos[i])
    sueldos[i]=sueldos[i]*2

print("Tamaño de mi lista es:{}".format(sueldos))