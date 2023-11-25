print("Bienvenido a la calculadora \nLas operaciones son suma, multi, div y resta\nPara salir escribe Salir")
n1 = int(input("Ingrese el Primer Número:"))
while True:
    op = input("ingrese la operación:")
    n2 = int(input("Ingrese el Segundo Número:"))
    if op.lower() == "suma":
        print(f"La suma de {n1}+{n2} es:", n1+n2)
        n1 = n1+n2
    elif op.lower() == "multi":
        print(f"La multiplicación de {n1}+{n2} es:", n1*n2)
        n1 = n1*n2
    elif op.lower() == "div":
        print(f"La división de {n1}+{n2} es:", n1/n2)
        n1 = n1/n2
    elif op.lower() == "resta":
        print(f"La resta de {n1}+{n2} es:", n1-n2)
        n1 = n1-n2
    elif op.lower() == "salir":
        print("Se cerró la calculadora")
        break
    else:
        print("Ingrese un operador válido")
