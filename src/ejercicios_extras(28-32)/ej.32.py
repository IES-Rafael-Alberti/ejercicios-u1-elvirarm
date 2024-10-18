#
# Calcular la serie de Fibonacci hasta un número dado
#


def fibonacci(hasta):
    num1 = 0
    num2 = 1

    serie = ""

    if hasta >= 0:
        serie += str(num1) + " "
    if hasta >= 1:
        serie += str(num2) + " "

    suma = num1 + num2

    while suma <= hasta:
        serie += str(suma) + " "
        num1, num2 = num2, suma
        suma = num1 + num2

    return serie.strip()

def main():
    num_fin = int(input("Introduzca el número final de la serie Fibonacci: "))
    print(fibonacci(num_fin))

if __name__ == "__main__":
    main()