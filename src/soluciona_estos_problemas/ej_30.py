#
#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
#

num = int(input("Dame un número: "))
incremento = int(input("Introduce el valor en el que quieres incrementar el número: "))
total = int(input("Introduce el total de la serie:"))

while incremento <= 0:
    print("**ERROR** El número debe ser mayor de 0")
    incremento = int(input("Introduce otro número:"))

while total <= 0:
    print("**ERROR** El número debe ser mayor de 0")
    total = int(input("Introduce otro número:"))

##SIN TERMINAR##