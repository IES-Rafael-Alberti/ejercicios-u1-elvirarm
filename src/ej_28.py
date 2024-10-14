#
# Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
# El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
# Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".
#


num1= int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))



if num1 == num2:
    print("**ERROR** Los números no pueden ser iguales")



elif num1 < num2:
    for i in range(num1,num2):
        i = num2 - num1
    print(f"El número menor es el {num1} y entre ellos existen {i} números enteros")
    

elif num2 < num1:
    for i in range(num2,num1):
        i = num1 - num2
    print(f"El número menor es {num2} y entre ellos existen {i} números enteros")