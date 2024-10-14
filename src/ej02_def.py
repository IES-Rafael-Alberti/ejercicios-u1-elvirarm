#
#   - ej02 => recibe horas y coste y retorna el importe total.
#

def main():
    horas = int (input ("Introduzca las horas de trabajo:"))
    coste = int(input ("Introduzca el precio de las horas:"))
    total = (horas * coste)
    return total

print (main)
