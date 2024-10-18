#
#ej04_def2.py => La función grados_celsius(farenheit: float) -> float recibe los grados farenheit (redondeados a dos posiciones decimales) y retorna los grados celsius (redondeados a dos posiciones).
#

def grados_celsius(farenheit: float)-> float:
    celsius = ((farenheit - 32) * 5/9)
    return celsius

def grado_farenheit ():
    farenheit = float(input("Introduzca una temperatura en farenheit: "))
    return farenheit

def main():
    farenheit = grado_farenheit()
    celsius = grados_celsius(farenheit)

    print(f"{celsius:.2f}ºC ({farenheit:.2f}ºF)")


if __name__ == "__main__":
    main()
