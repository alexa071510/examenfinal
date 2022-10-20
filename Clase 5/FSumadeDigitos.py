
"""
2.Crear una funcion donde el usuario ingresará el numero 0,en este caso el programa se detendrá.
Requisitos:
-Crear logica dentro de la funcion
-Mostrar la suma de digito
"""
def sumarDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=int(numero/10)
        print("digito:{}".format(digito))
        print("suma de digitos:{}".format(suma))
    return suma

num=int(input("Ingrese numero a procesar:"))
while num!=0:
         print("Suma:{}".format(sumarDigitos(num)))
         num=int(input("Ingrese nuevo procesar:"))