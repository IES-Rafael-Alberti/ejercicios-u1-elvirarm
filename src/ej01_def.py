#
# ej01 => recibe un nombre y retorna una cadena de caracteres con el resultado.
#

def main():
    nombre = input ("Escribe tu nombre:")
    saludos = "Hola, "

    frase = saludos + nombre + "."

    return frase 

print(main())
