"""Usando las propiedades de cadena"""

"""METODOS DE STRING"""

cadena="Conexion a Base de Datos con Python"

cadena2=cadena.replace(cadena[0:6],"ccc")

print("Cadena con reemplazos ,tiene el siguiente valor actualizado:{}".format(cadena2))

"""Eliminando espacios en blanco de mi cadena (despues)"""

cadena3="Conexion a base de datos con Python                     "
cadena4=cadena3.rstrip()

print("Mi cadena de espacios en blanco eliminación:{}".format(cadena4))

"""Eliminando espacios en blanco de mi cadena (antes)"""
cadena5="             Conexion a base de datos con Python"
cadena6=cadena5.lstrip()

print("Mi cadena de espacios en blanco eliminación:{}".format(cadena6))

