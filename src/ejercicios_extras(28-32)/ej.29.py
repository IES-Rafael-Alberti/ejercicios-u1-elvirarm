#
# Cálculo de un número aleatorio entre dos valores
#

import random

def dame_un_numero_aleatorio(min,max):
    return random.randint(min,max)

def main():
    min = int(input("Dame el mínimo: "))
    max = int(input("Dame el máximo: "))
    dame_un_numero_aleatorio(min,max)
    print (dame_un_numero_aleatorio(min,max))


if __name__ == "__main__":
    main()