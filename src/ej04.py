#
# Ejercicio 1.2.4¶
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

tempcelsius = int(input("Dame una temperatura en grados Celsius: "))
tempfahrenheit = ((tempcelsius * 9/5)+32)
print (f"La temperatura convertida es: {tempfahrenheit}")