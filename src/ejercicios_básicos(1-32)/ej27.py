#
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
#

def main():
    nombre = input("Introduce el nombre de un producto: ")
    precio = float(input("Introduce el precio del producto: "))
    numero = int(input("Introduce el número de unidades:"))
    precio_redondeado = (f"{precio:6.2f}")
    numero_redondeado = (f"{numero:3.0f}")
    total = precio * numero
    total_redondeado = ("total:08.2f")
    frase = (f"{nombre},{precio_redondeado} ,{numero_redondeado},{total}")
    print (frase)

if __name__ == "__main__":
    main()