#
#Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#

precioSinIVA = float (input("Introduzca el precio del producto sin IVA:"))
tipoIVA = float (input ("Introduzca el tipo de IVA a aplicar:"))

if tipoIVA == 21:
        precioConIVA = float (precioSinIVA * 1.21)
        print (f"Este es el precio con IVA: {precioConIVA:.2f}")

if tipoIVA == 10:
        precioConIVA = float (precioSinIVA * 1.1)
        print (f"Este es el precio con IVA: {precioConIVA:.2f}")
        
if tipoIVA == 4:
        precioConIVA = float (precioSinIVA * 1.04)
        print (f"Este es el precio con IVA: {precioConIVA:.2f}")