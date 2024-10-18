#
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
#

def main():

    nombre = input("Introduce el nombre de un producto:")
    nombre = nombre.strip()
    precio = input("Introduce el precio del producto:")
    
    precio = float(precio)

    numero = input("Introduce el número de unidades:")
    
    numero = float(numero)
    
    total = (precio * numero)

    frase = (f"{nombre}, {precio:.2f}, {numero:.2f}, {total:.2f}")
    

    print (frase)

if __name__ == "__main__":
    main()