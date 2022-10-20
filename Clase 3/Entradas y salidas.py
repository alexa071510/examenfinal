"""Entradas y salidas """

usuario=input("Ingrese su nombre de usuario:")
nombre= input("Ingrese su nombre:")
edad=input("Ingrese su edad:")

print("Bienvenido/a:{}".format(nombre))

telefono=input("Ingrese su telefono:")

print("Usted tiene el siguiente numero telefonico:{}".format(telefono))

#actualizacion=edad+10 esto no se puede porque siempre sale como STRING
actualizacion=int(edad)+10
print(actualizacion)