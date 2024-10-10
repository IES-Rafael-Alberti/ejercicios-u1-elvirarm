#
#   - ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
#


def main():
    articulo_sin_iva = float(input("Introduzca el importe sin IVA:"))
    tipo_iva = int(input("Introduzca el tipo de IVA a aplicar:"))
    print (f"{articulo_sin_iva}, {tipo_iva}")

if __name__ == "__main__":
       main()