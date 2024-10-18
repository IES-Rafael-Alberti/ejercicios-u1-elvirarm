
def recibir_numero(num1,num2):
    num1 = int(input("Introduce número 1: "))
    num2 = int(input("Introduce número 2: "))
    return num1,num2

def comprobar_numero (num1,num2):
    if num1 > num2:
        return (num1)
    if num2 > num1:
        return (num2)
    if num1 == num2:
        return ("0")



def main():
    num1 = 0
    num2 = 0
    num1, num2 = recibir_numero(num1,num2)
    print(comprobar_numero(num1,num2))


if __name__ == "__main__":
    main()
