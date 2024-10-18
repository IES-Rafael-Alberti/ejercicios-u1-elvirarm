def comprobar_entero(cadena: str) -> bool:
    cadena = cadena.strip() #Si la queremos usar tenemos que igualarle el valor para usarlo
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit()) #Nos comprueba si es número. Las funciones llevan parentesis siempre.


def dame_entero() -> int:
    cadena = input("Dame un entero: ")
    while not comprobar_entero(cadena):
        cadena = input("**ERROR** no es un entero!!\n\n Dame un entero de verdad:")
    
    return int(cadena)

def main():
    num = dame_entero()
    print(f"Escribiste el número {num}")

if __name__ == "__main__":
    main()