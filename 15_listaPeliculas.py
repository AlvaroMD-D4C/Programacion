peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

# 1. Indica qué tipo de estructura es peliculas y qué tipo de estructura representa cada película.
print(type(peliculas))
print(type(peliculas[0]))

# 2. Recorre peliculas con un bucle y muestra el título y la duración de cada película.
print("-- Mostrar las peliculas actuales en la lista.")
for pelicula in peliculas:
    print(pelicula[0], pelicula[1])

# 3. Añade la película ("Los Increíbles", 115) utilizando append().
print("-- Adición de la pelicula \"Los Increíbles\".")
print(" Lo haremos con: \'peliculas.append((\"Los Increíbles\", 115))\'")
peliculas.append(("Los Increíbles", 115))

# 4. Vuelve a mostrar las películas para comprobar que se ha añadido.
print("-- Muestra ahora con la adición de Los Increíbles.")
for pelicula in peliculas:
    print(pelicula[0], pelicula[1])

# 5. Intenta cambiar la duración de Shrek ejecutando esta instrucción: peliculas[0][1] = 95
print("-- Intentamos modificar la duración de la pelicula \"Shrek\"")
print("El comando que usariamos sería: \'peliculas[0][1] = 95\'")
print("Esta instrucción daría un error porque la película es una tupla.")

# 7. Explica por qué puedes añadir una película a la lista, pero no puedes modificar directamente la duración dentro de una tupla.
print("-- Explicación de porque podemos añadir peliculas pero no modificar la duracion dentro de una tupla.")
print("Podemos añadir una película a la lista porque las listas son estructuras de datos mutables.")
print("Sin embargo, no podemos modificar directamente la duración de una película porque cada película está representada mediante una tupla, las cuales son estructuras inmutables")