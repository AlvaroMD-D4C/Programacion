numeroMaleta = int(input("Introduzca el numero de maletas: "))
precioTotal = int()

for i in range (numeroMaleta, 0, -1):
    pesoMaleta = float(input("Introduzca el peso de la maleta (individualmente): "))
    if pesoMaleta <= 10:
        print("Equipaje de mano, es gratuito.")
    elif pesoMaleta == 10 or pesoMaleta <= 20:
        print("Debe facturarse, cuesta 20€")
        precioTotal = precioTotal + 20
    else:
        print("Cuesta 20€ más 5€ por cada kg que supere los 20kg")
        añadidoExtra = (pesoMaleta - 20) * 5
        añadidoTotal = añadidoExtra + 20
        precioTotal = precioTotal + añadidoTotal
print("El importe total es:", precioTotal)