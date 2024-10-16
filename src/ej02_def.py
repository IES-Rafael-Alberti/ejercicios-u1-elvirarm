#
#   - ej02 => recibe horas y coste y retorna el importe total.
#

def recibir_horas(horas):
    horas= int(input("Introduzca las horas de trabajo realizadas: "))
    return horas

def recibir_precio(precio):
    precio = int (input("Introduzca el precio de las horas trabajadas: "))
    return precio

def total_precio_horas (total):
    horas = recibir_horas(horas)
    precio = recibir_precio(precio)
    total = (horas * precio)
    return total

def main():
    horas = recibir_horas(horas)
    precio = recibir_precio(precio)
    total = total_precio_horas
print(total) #TERMINAR

print (main)
if __name__ == "__main__":
    main()