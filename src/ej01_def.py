#
# ej01 => recibe un nombre y retorna una cadena de caracteres con el resultado.
#

def introduce_nombre(nombre):
    frase = f"Hola, {nombre}."
    return frase


def main():
    nombre = input("Introduce tu nombre: ")
    print(introduce_nombre(nombre))



if __name__ == "__main__":
    main()