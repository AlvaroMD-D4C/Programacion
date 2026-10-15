cadena = input("Introduce una palabra o frase: ")
final = len(cadena)-1
for i in range(final, -1, -1):
    print(cadena[i], end="")