#
#Ejercicio 1.2.16¶
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
#
 
PRECIO_PAN = 3.49
num_pan_antiguo = int(input("¿Cuántas barras de pan que no son del día se han vendido?: "))
print (f"El precio habitual de las barras de pan es: {PRECIO_PAN} euros")
Descuento_pan = (PRECIO_PAN *0.60)
print("El descuento que se le aplicará será de {:.2f} euros".format (PRECIO_PAN - Descuento_pan))
precio_final_barrasAntiguas = num_pan_antiguo * Descuento_pan
print("El coste final de todas las barras no frescas es: {:.2f} euros.".format(precio_final_barrasAntiguas))