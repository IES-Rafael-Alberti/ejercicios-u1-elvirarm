#
#ej04 => NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.
#

def grados_farenheit():
    temp_farenheit = float(input("Introduzca una temperatura en Farenheit con dos decimales: "))
    temp_celsius = ((temp_farenheit - 32) * 5/9)
    total = (f"{temp_celsius:.2f}ºC ({temp_farenheit:.2f}ºF)")
    return total


def main():
    print(grados_farenheit())


if __name__ == "__main__":
    main()
