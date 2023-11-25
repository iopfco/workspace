def hola(nombre, apellido="valor por defecto"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("francisco", "Lizama")
hola("Francisco")


hola(apellido="Lizama", nombre="Francisco")
