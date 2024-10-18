#
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#
num_telefono = input("Escribe un número de teléfono con el siguiente formato: +34-XXXXXXXXX-XX:")
num_telefono_separado = num_telefono.split('-')
#EXPLICACIÓN PARA RECORDAR YO MISMA - ignorar :( - Con el split se separa por guiones (porque he puesto un guion entre ', sino se pone nada se cogen los espacios por defecto)
if len(num_telefono_separado) == 3 and (num_telefono_separado)[0] == "+34":
    #En linea 7 está comprobado que hay 3 partes, la parte del principio, la de en medio y la del final. Además estoy comprobando que el prefijo sea +34, cuidado que tengo que poner la cadena de texto entre comillas porque está leyendo texto.
    numerofinal = num_telefono_separado [1]
    #Con los corchetes estamos seleccionando la parte que queremos coger. Empieza por 0, entonces la parte 0 es la del principio, la 1 es la del medio y la 2 la final, según mis pruebas
    print (numerofinal)
else:
    print ("**ERROR**. El prefijo tiene que ser +34")



    
