#
#Ejercicio 1.2.14¶
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#
pesoPayaso = 112 #gramos
pesoMuñeca = 75 #gramos
numPayasos = int(input("Escribe el número de payasos vendidos en el último pedido: "))
numMuñecas = int(input("Escribe el número de muñecas vendidas en el último pedido: "))
total_payasos = pesoPayaso * numPayasos
total_muñecas = pesoMuñeca * numMuñecas
print(f"Se han vendido {total_payasos} payasos y {total_muñecas} muñecas.")