numero = 7
usuario = 0

while usuario != numero:
    usuario = int(input("Cual es el numero?"))
    if usuario > numero:
        print("digita un numero menor")
    elif usuario < numero:
        print("digia un numero menor")
    else:
        print("correcto")