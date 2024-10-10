#
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
#
frase_derecho = input("Escribe una frase:")
frase_girada = ""
for i in frase_derecho:
    frase_girada = i + frase_girada
print(frase_girada)