#
# Mostrar todos los divisores de un número
#

def pedir_numero():
    num = int(input("Introduce un número: "))
    return num

def comprobar_divisores(num):
    divisores = ""
    for i in range (1,num+1):
        if num % i == 0:
            divisores += str(i) + ","
    
    return divisores[:-1]

def main():
    num = pedir_numero()
    divisores = comprobar_divisores(num)
    print (divisores)



if __name__ == "__main__":
    main()
