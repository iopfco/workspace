numeros = [2, 4, 1, 45, 22, 106, 12]

# numeros.sort()
# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)


# usuarios = [[4, "chanchito"], [1, "amelie"], [5, "Pulga"]]
usuarios = [["chanchito", 4], ["amelie", 1], ["Pulga", 5]]


# def ordena(elemento):
#     return elemento[1]


usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)
