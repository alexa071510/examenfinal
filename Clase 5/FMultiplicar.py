"""Programacion funcional en Python"""

def multiplicar(a,b):
    resultado=a*b
    return resultado

print("El resultado es :{}".format(multiplicar(3,4)))

def multiplicar2(a,b,c=100):
    resultado=a*b*c
    return resultado

print("El resultado es :{}".format(multiplicar2(40,3)))

"""
1.Solicitar a un usuario  ingresar su direccion email.
Imprimir un mensaje que indique si es valido o no el email mediante una funcion.
NOTA:La direccion email se considera valida si contiene el simbolo:'@'
"""

def validar(email):
    caracterBuscado = "@"
    emailValido = False
    for c in email:
        if c == caracterBuscado:
            return True
    return False


direccion = input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")