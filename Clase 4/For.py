"""Uso del for"""

ingenierias=["Software","Sistemas","Industrial","Quimica"]

nombre=input("Ingrese su primer nombre:")
i=0

print("El tamaño de mi lista es:{},y el programa fue creado por:{}".format(len(ingenierias),nombre))

for ingenieria in ingenierias:
    print(ingenieria)
    i=i+1
    print("Esta es la vuelta numero:{}".format(i))