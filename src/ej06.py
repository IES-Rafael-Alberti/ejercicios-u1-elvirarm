#
#Ejercicio 1.2.6¶
#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)
#
articuloConIVA = float(input("El precio del artículo con IVA es: "))
articuloSinIVA = (articuloConIVA / 1.1)
IVApagado = (articuloConIVA - articuloSinIVA)
print (f"El IVA pagado es: {round(IVApagado,2)}")
print (f"El precio sin IVA es: {round(articuloSinIVA,2)}")