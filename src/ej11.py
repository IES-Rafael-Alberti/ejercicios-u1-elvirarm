#
#Ejercicio 1.2.11
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
#
n = int(input("Escribe un número: "))
sumaNumeros = 0
for i in range (1,n+1):
    sumaNumeros = sumaNumeros + i
    print (sumaNumeros)
comprobacion = (n*(n+1))/2
print (int(comprobacion))

n = int(input("Escribe el número: "))

#ESCRIBIR DE NUEVO _ rehacer

num = int(input("Dame un número: "))
suma = int(num * (num + 1) / 2)
print("La suma de los números del 1 al ", num, "es", suma)