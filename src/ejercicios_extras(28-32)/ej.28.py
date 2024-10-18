#
# Calcular el área de un triángulo a partir de tres lados
#
import math

def pedir_lados():
    lado1, lado2, lado3 = int(input("Introduce lado 1 del triángulo:")), int(input("Introduce lado 2 del triángulo:")), int(input("Introduce lado 3 del triángulo:"))
    
    return lado1, lado2, lado3

def calcular_semiperimetro(lado1, lado2, lado3):
    semiperimetro = float((lado1 + lado2 + lado3) / 2)
    return semiperimetro

def calcular_area (lado1, lado2, lado3, semiperimetro):
    area = math.sqrt(semiperimetro*((semiperimetro - lado1)*(semiperimetro - lado2)*(semiperimetro - lado3)))
    return area


def main():
    lado1, lado2, lado3 = pedir_lados()
    semiperimetro = calcular_semiperimetro(lado1, lado2, lado3)
    area = calcular_area(lado1, lado2, lado3, semiperimetro)
    print (round(area,2))


if __name__ == "__main__":
    main()   