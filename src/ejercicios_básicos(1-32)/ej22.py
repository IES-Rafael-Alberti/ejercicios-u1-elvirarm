#
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
#


frase_vocal = input("Introduce una frase y una vocal: ")
separacion = frase_vocal.split (" ")
frase = separacion [0]
vocal = separacion[1]
vocal_mayuscula = vocal.replace(vocal, vocal.upper())
frase_final = ' '.join([frase,vocal_mayuscula]) #.join se utiliza para unir elementos, lo primero que hay que escribir es cómo quieres que esos elementos estén separados, luego se escribe .join () y en mitad de los paréntesis, entre corchetes se mete lo que quieres unir (separado de ,)
print(frase_final)



