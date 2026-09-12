matriz = [[8, 9], [25, 70]]
soma = 0

for numero in matriz:
    for valor in numero:
        soma = soma + valor

print(f"A de todos os valores é: {soma}")