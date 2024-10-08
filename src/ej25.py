#
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
#
nacimiento_dos_digitos = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa:")
partes_nacimiento = nacimiento_dos_digitos.split('/')
dia = partes_nacimiento [0]
mes = partes_nacimiento [1]
año = partes_nacimiento [2]
if (len(dia) == 1 or len(dia) == 2) and (len(mes) == 1 or len (mes) == 2):
    fecha_correcta = '/'.join([dia,mes,año])
    print (fecha_correcta)
else:
    error_formato = input("**ERROR** El formato introducido no es correcto, introduzca su fecha de nacimiento en formato dd/mm/aaaa o d/m/aaaa: ")
    partes_error = error_formato.split("/")
    dia_error = partes_error [0]
    mes_error = partes_error [1]
    año_error = partes_error [2]
    fecha_corregida = '/'.join([dia_error,mes_error,año_error])
    print(fecha_corregida)

    ##INTENTAR CON BUCLE