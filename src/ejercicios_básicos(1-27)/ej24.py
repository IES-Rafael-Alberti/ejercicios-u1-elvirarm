#
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
#

precio = input("Introduce un precio con dos decimales:")
partes = precio.split(".")
precio_euros = int(partes[0])
precio_centimos = (partes[1])
if len(precio_centimos) == 2:
    print (f"El precio es de {precio_euros} euros y {precio_centimos} céntimos")
while len(precio_centimos) != 2:
    error = input ("**ERROR** Los céntimos tienen que tener dos decimales, inténtalo de nuevo:")
    partes_error = error.split(".")
    error_euros = int(partes_error[0])
    error_decimales = (partes_error[1])
    if len(error_decimales) == 2:
        print (f"El precio es de {error_euros} euros y {error_decimales} céntimos")
        break
