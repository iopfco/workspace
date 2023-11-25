n1 = int(input("Ingresa Primer número:"))
n2 = int(input("Ingresa Segundo número:"))

suma = n1+n2
resta = n1-n2
multi = n1*n2
divi = n1/n2

"""
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multi)
print("La división es:", divi)
"""
mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicación es {multi},
el resultado de la división es {divi}
"""
print(mensaje)
