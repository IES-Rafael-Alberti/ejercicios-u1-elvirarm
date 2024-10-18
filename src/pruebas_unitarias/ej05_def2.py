#
#ej05_def2.py => La función calcula_precio(importe: float, iva: float) -> str recibe el importe y el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> "El precio final del artículo con IVA (21.00) es 121.00€."
#
def calcula_precio(importe: float, iva: float) -> str:
    if iva <= 0 or iva >= 100:
        importe = importe + (0.21 * importe)
        return f"El precio final del artículo con IVA 21.00 es {importe:.2f}."
    else:
        importe = importe + ((iva/100) * importe)
        return f"El precio final del artículo con IVA {iva:.2f} es {importe:.2f}."

def main():
    importe = float(input("Introduce el importe: "))
    iva = float(input("Introduce el iva a aplicar: "))

    print(calcula_precio(importe, iva))

       
if __name__ == "__main__":
    main()