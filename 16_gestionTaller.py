talleres = [
    (
        "Fotografía",
        ["Ana", "Luis"],
        {"aula": 12, "plazas": 4},
        {"cámara", "tarjeta de memoria"}
    ),
    (
        "Robótica",
        ["Marta"],
        {"aula": 15, "plazas": 3},
        {"portátil", "cable USB"}
    ),
    (
        "Pintura",
        [],
        {"aula": 8, "plazas": 5},
        {"pinceles", "acuarelas", "papel"}
    )
]

opcion = 0

while opcion != 6:
    print("\n--- GESTIÓN DE TALLERES ---")
    print("1. Mostrar talleres")
    print("2. Inscribir a un alumno")
    print("3. Cancelar una inscripción")
    print("4. Cambiar el aula")
    print("5. Añadir un material")
    print("6. Terminar")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        for taller in talleres:
            print("\nTaller:", taller[0])
            print("Aula:", taller[2]["aula"])
            print("Alumnos inscritos:", taller[1])

            plazas_libres = taller[2]["plazas"] - len(taller[1])

            print("Plazas libres:", plazas_libres)
            print("Materiales:", taller[3])

    elif opcion == 2:
        nombre_taller = input("Nombre del taller: ")
        nombre_alumno = input("Nombre del alumno: ")

        encontrado = False

        for taller in talleres:
            if taller[0].lower() == nombre_taller.lower():
                encontrado = True

                if len(taller[1]) < taller[2]["plazas"]:
                    taller[1].append(nombre_alumno)
                    print("Alumno inscrito correctamente")
                else:
                    print("No quedan plazas libres")

        if encontrado == False:
            print("El taller no existe")

    elif opcion == 3:
        nombre_taller = input("Nombre del taller: ")
        nombre_alumno = input("Nombre del alumno: ")

        encontrado = False

        for taller in talleres:
            if taller[0].lower() == nombre_taller.lower():
                encontrado = True

                if nombre_alumno in taller[1]:
                    taller[1].remove(nombre_alumno)
                    print("Inscripción cancelada")
                else:
                    print("Ese alumno no está inscrito")

        if encontrado == False:
            print("El taller no existe")

    elif opcion == 4:
        nombre_taller = input("Nombre del taller: ")
        encontrado = False

        for taller in talleres:
            if taller[0].lower() == nombre_taller.lower():
                encontrado = True

                nueva_aula = int(input("Nuevo número de aula: "))
                taller[2]["aula"] = nueva_aula

                print("Aula cambiada correctamente")

        if encontrado == False:
            print("El taller no existe")

    elif opcion == 5:
        nombre_taller = input("Nombre del taller: ")
        nombre_material = input("Nombre del material: ")

        encontrado = False

        for taller in talleres:
            if taller[0].lower() == nombre_taller.lower():
                encontrado = True

                if nombre_material not in taller[3]:
                    taller[3].add(nombre_material)
                    print("Material añadido correctamente")
                else:
                    print("Ese material ya existe")

        if encontrado == False:
            print("El taller no existe")

    elif opcion == 6:
        print("Programa terminado")

    else:
        print("Opción no válida")