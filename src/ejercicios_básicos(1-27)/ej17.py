#
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
#
nombre_usuario = input ("¿Cómo te llamas?: ")
num_entero = int(input("Escribe un número entero: "))
for i in range (0, num_entero):
    print (nombre_usuario)
