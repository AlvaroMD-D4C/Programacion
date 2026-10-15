mario_kart = {"Ana", "Luis", "Pedro", "Marta", "Hugo"}
minecraft = {"Luis", "Marta", "Sara", "David"}
rocket_league = {"Pedro", "Marta", "David", }

opcion = ""

while opcion != "9":
    print("---- Gestión de Torneos ----")
    print("1. Mostrar todos los participantes")
    print("2. Participantes comunes a Mario Kart y Minecraft")
    print("3. Participantes inscritos en los tres torneos")
    print("4. Participantes de Mario Kart que no están en Minecraft")
    print("5. Participantes de Minecraft o Rocket League, pero no en ambos")
    print("6. Añadir un participante a un torneo")
    print("7. Eliminar un participante de un torneo")
    print("8. Consultar en qué torneos está una persona")
    print("9. Terminar el programa")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        participantes = mario_kart, minecraft, rocket_league
        print("Todos los participantes:", participantes)

    elif opcion == "2":
        comunes = mario_kart and minecraft
        print("Participantes comunes:", comunes)

    elif opcion == "3":
        comunes = mario_kart and minecraft and rocket_league
        print("Participantes de los tres toneos:", sorted(comunes))

    elif opcion == "4":
        exclusivos = mario_kart - minecraft
        print("PArticipantes de Mario Kart que no están en Minecraft:", sorted(exclusivos))

    elif opcion == "5":
        exclusivos = minecraft ^ rocket_league
        print("Participantes de Mario Kart o Rocket League, pero no en ambos:", sorted(exclusivos))

    elif opcion == "6":
        print("\n1. Mario Kart")
        print("2. Minecraft")
        print("3. Rocket League")

        torneo = input("Selecciona el torneo: ")
        nombre = input("Nombre del participante: ").strip()

        if torneo == "1":
            mario_kart.add(nombre)
            print("Participante añadido a Mario Kart.")

        elif torneo == "2":
            minecraft.add(nombre)
            print("Participante añadido a Minecraft.")

        elif torneo == "3":
            rocket_league.add(nombre)
            print("Participante añadido a Rocket League.")

        else:
            print("Opción de torneo no válida.")

    elif opcion == "7":
        print("\n1. Mario Kart")
        print("2. Minecraft")
        print("3. Rocket League")

        torneo = input("Selecciona el torneo: ")
        nombre = input("Nombre del participante que quieres eliminar: ").strip()

        if torneo == "1":
            if nombre in mario_kart:
                mario_kart.remove(nombre)
                print("Participante eliminado de Mario Kart.")
            else:
                print("El participante no está en Mario Kart.")

        elif torneo == "2":
            if nombre in minecraft:
                minecraft.remove(nombre)
                print("Participante eliminado de Minecraft.")
            else:
                print("El participante no está en Minecraft.")

        elif torneo == "3":
            if nombre in rocket_league:
                rocket_league.remove(nombre)
                print("Participante eliminado de Rocket League.")
            else:
                print("El participante no está en Rocket League.")

        else:
            print("Opción de torneo no válida.")

    elif opcion == "8":
        nombre = input("Introduce el nombre del participante: ").strip()
        encontrado = False

        if nombre in mario_kart:
            print("Está inscrito en Mario Kart.")
            encontrado = True

        if nombre in minecraft:
            print("Está inscrito en Minecraft.")
            encontrado = True

        if nombre in rocket_league:
            print("Está inscrito en Rocket League.")
            encontrado = True

        if encontrado == False:
            print("No está inscrito en ningún torneo.")

    elif opcion == "9":
        print("Programa finalizado.")

    else:
        print("Opción no válida. Elige un número del 1 al 9.")