#
#   - ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
#


def main():
       precio_sin_iva = int(input("Introduce el precio del artículo sin iva: "))
       tipo_iva = int (input("Introduzca el tipo de IVA a aplicar: "))
       precio_con_iva = precio_sin_iva * (tipo_iva / 100)
       precio_final = precio_sin_iva - precio_con_iva
       print (f"El precio con IVA es: {precio_final}")

if __name__ == "__main__":
       main()