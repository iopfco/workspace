# def suma(a, b):
#     print(a+b)


# suma(2, 5)

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(5, 6, 8)
