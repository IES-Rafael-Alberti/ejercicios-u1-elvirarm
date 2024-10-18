#
#Escribir un programa que determine si un número es primo
#

def es_primo_basico_2(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Introduzca un número: "))
    if es_primo_basico_2(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

if __name__ == "__main__":
    main()