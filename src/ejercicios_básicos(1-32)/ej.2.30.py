#
# Escribir un programa que determine si un número es primo
#

def pedir_numero():
    numero = int(input("Introduce un número: "))
    return numero

def comprobar_primo(numero):
    #Investigar fórmula de cómo saber si un número es primo :((

def main():
    numero = pedir_numero()
    if not comprobar_primo(numero):
        print ("No es un número primo")
    else:
        print ("Es un número primo")

if __name__ == "__main__":
    main()