# lista1 = [1, 2, 3, 4]
# print(*lista)
# lista2 = [5, 6]

# combinada = [*lista1, *lista2]
# combinada = ["hola", *lista1, "Chanchito", *lista2, "feliz"] listas con un *

# print(combinada)

# ** para diccionarios
punto1 = {"x": 19}
punto2 = {"y": 22}


nuevopunto = {**punto1, "lala": "hola mundo", **punto2, "z": "Mundo"}
print(nuevopunto)
