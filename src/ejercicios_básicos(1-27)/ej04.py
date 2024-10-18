#
# Ejercicio 1.2.4¶
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

tempCelsius =  float(input("Dame una temperatura en grados Celsius:"))

tempFahrenheit = ((tempCelsius * 9/5)+32)

print (f"La temperatura en grados Farenheit es: {tempFahrenheit}ºF ({tempCelsius}ºC)")