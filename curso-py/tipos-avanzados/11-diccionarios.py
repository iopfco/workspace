punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

if "lala" in punto:
    print("Encontré lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [{"id": 1, "nombre": "chanchito"}, {"id": 2, "nombre": "feliz"}, {
    "id": 3, "nombre": "francisco"}, {"id": 4, "nombre": "lizama"}]

print(usuarios)

for ususario in usuarios:
    print(ususario["nombre"])
