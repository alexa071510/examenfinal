"""Importando libreria Random"""
"""RANDOM: manejor de numeros aleatorios"""

import  random
lisaNumeros=[]

#En el parantesis:que empiece de 1 y vaya hasta 20
for indice in range(1,20):
    #lisaNumeros.append(indice)
    lisaNumeros.append(random.randint(1,20))
print(lisaNumeros)
