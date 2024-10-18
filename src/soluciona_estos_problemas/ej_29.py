#
#Realiza un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#

nombre = input("Introduce tu nombre:") or None

vacio = None


while nombre == None:
    print("**ERROR** Debes introducir un nombre.")
    nombre = input("Introduce tu nombre:") or None

edad = input("Introduce tu edad:") or None

while edad == None:
    print ("**ERROR** Debes introducir una edad.")
    edad = input("Introduce tu edad:") or None


edad = int(edad)

while (edad < 0) or (edad > 125):
    print ("**ERROR** Debes introducir una edad comprendida entre 0 y 125 años")
    edad = input("Introduce tu edad:") or -1
    edad = int(edad)


if edad == (edad > 0) or (edad < 125):
    for i in range (0,125):
        edad_por_cumplir = 125 - edad
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {edad_por_cumplir} años por cumplir.")