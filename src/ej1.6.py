#
#Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#

articuloConIVA = float(input("El precio del artículo con IVA es: "))

articuloSinIVA = (articuloConIVA / 1.1)

IVApagado = (articuloConIVA - articuloSinIVA)

print (f"El precio sin IVA es: {articuloSinIVA:.2f} y el IVA pagado es {IVApagado:.2f} ")