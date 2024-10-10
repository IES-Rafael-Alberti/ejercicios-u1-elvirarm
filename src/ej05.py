#
#Ejercicio 1.2.5¶
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#

precioSinIVA = float (input("Introduzca el precio del producto sin IVA:"))
tipoIVA = float (input ("Introduzca el tipo de IVA a aplicar:"))
if tipoIVA == 21:
        precioConIVA = float (precioSinIVA * 1.21)
        print (f"Este es el precio con IVA: {precioConIVA}")
if tipoIVA == 10:
        precioConIVA = float (precioSinIVA * 1.1)
        print (f"Este es el precio con IVA: {precioConIVA}")
if tipoIVA == 4:
        precioConIVA = float (precioSinIVA * 1.04)
        print (f"Este es el precio con IVA: {precioConIVA}")