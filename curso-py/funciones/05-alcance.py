saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola Mundo"


def SaludaChanchito():
    saludo = "Hola Chanchito"


print(saludo)
saludar()
print(saludo)
SaludaChanchito()
