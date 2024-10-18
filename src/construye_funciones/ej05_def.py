#
#   - ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
#

def main():
       precio_sin_iva = input("Introduce el precio del artículo sin iva: ")
       tipo_iva = input("Introduzca el tipo de IVA a aplicar: ")
       calcular_iva(precio_sin_iva, tipo_iva)


def calcular_iva(precio_sin_iva, tipo_iva):
       precio_sin_iva = int(precio_sin_iva)
       tipo_iva = int (tipo_iva)
       precio_con_iva = precio_sin_iva * (1 + (tipo_iva / 100))

       print (f"El precio con IVA es: {precio_con_iva}")


if __name__ == "__main__":
       main()