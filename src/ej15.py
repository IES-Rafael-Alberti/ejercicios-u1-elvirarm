#
#Ejercicio 1.2.15¶
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#
#Calcula el interés: capital * (1 + interes)
#

dineroInicial = int(input("Escribe el dinero inicial: "))
ahorrado_año1 = (dineroInicial * (1 + 4/100))
ahorrado_año2 = (ahorrado_año1 * (1 + 4/100))
ahorrado_año3 = (ahorrado_año2 * (1 + 4/100))
print ("{:.2f},{:.2f},{:.2f}".format(ahorrado_año1,ahorrado_año2,ahorrado_año3))