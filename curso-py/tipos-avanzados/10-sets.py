# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

primer.add(5)
primer.remove(1)

print(primer)
print(segundo)

# union
print(primer | segundo)

# interserccion
print(primer & segundo)

# diferencia
print(primer - segundo)

# difecencia simetrica
print(primer ^ segundo)
