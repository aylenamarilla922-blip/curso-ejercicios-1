pin_correcto = 4321
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    pin_ingresado = int(input("ingrese su pin"))
    if pin_ingresado == pin_correcto:
        print("acceso concedido")
        break
    else:
        print("pin incorrecto")
        intentos += 1
if intentos == max_intentos:
    print("tarjeta bloqueada")