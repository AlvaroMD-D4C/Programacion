numeroMaleta = int(input("Introduzca el numero de maletas: "))

precioTotal = 0
equipajes = []

for i in range(numeroMaleta):
    pesoMaleta = float(input("Introduzca el peso de la maleta (individualmente): "))
    if pesoMaleta <= 10:
        precio = 0
        print("Equipaje de mano, es gratuito.")
    elif pesoMaleta <= 20:
        precio = 20
        print("Debe facturarse, cuesta 20€")
    else:
        añadidoExtra = (pesoMaleta - 20) * 5
        precio = 20 + añadidoExtra
        print("Cuesta 20€ más 5€ por cada kg que supere los 20kg")
    
    maleta = {
        "peso": pesoMaleta,
        "precio": precio
    }

    equipajes.append(maleta)
    precioTotal = precioTotal + precio
print("\n--- EQUIPAJES ---")

for maleta in equipajes:
    print("Peso:", maleta["peso"], "kg")
    print("Precio:", maleta["precio"], "€")
    print()

print("El importe total es:", precioTotal, "€")