#
#Ejercicio 1.2.5¶
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#

precioSinIVA =  float(input("Introduzca el precio del producto sin IVA:"))

tipoIVA =  float(input("Introduzca el tipo de IVA a aplicar:"))

precio_final = (precioSinIVA * (1+ (tipoIVA/100)))
print (precio_final)