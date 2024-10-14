#
#Formatear la salida de los grados Farenheit a dos posiciones decimales.
#Mostrar en pantalla:
#La temperatura en grados Farenheit es 0.00ºF (0.00ºC)
#
tempCelsius =  float(input("Dame una temperatura en grados Celsius:"))
tempFahrenheit = ((tempCelsius * 9/5)+32)
print (f"La temperatura en grados Farenheit es: {tempFahrenheit:.2f}ºF ({tempCelsius:.2f}ºC)")