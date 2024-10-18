#
#ej11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.
#
def recibe_numero():
    numero = int(input("Introduce un número: "))
    return numero
    

def formula(n):
    sumaNumeros = 0
    for i in range (1, n+1):
        sumaNumeros += i
    return sumaNumeros
    
def resultado(final):
    frase = f"El resultado es: {final}"
    return frase


def main():
    n = recibe_numero()
    cuenta = formula(n)
    final = resultado(cuenta)
    print (final)

if __name__ == "__main__":
    main()
