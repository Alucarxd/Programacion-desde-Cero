usuario = "gabi"
clave = "123"
saldo = 1200


def validaUsuario(u, c):
    if u == usuario and c == clave:
        return True
    return False


def login():
    print("Bienvido")
    usuario = input("Digite usuario ")
    clave = input("digite contrasena ")
    return validaUsuario(usuario, clave)


def retirar(valor):
    if valor > saldo:
        return False, saldo

    return True, saldo - valor


def depositar(valor):
    return True, saldo + valor


def accion(opcion):
    if opcion == 1:
        valor = int(input("Digite el valor a depositar: "))
        return depositar(valor)
    if opcion == 2:
        valor = int(input("Digite el valor a retirar: "))
        return retirar(valor)
    return False, saldo


def ejecutar():
    if not login():
        print("usuario o contrasena invalido")
        return

    print("Que desea hacer?")
    opcion = int(input("1. depositar o 2. retirar: "))

    ok, saldo = accion(opcion)
    if not ok:
        print("no se realizo la accion, saldo: ", saldo)
    else:
        print("accion realizada correctamente, salgo: ", saldo)


ejecutar()
