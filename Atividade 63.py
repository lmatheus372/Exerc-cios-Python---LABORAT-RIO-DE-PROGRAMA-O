def informar_numeros():
    numeros = []
    for i in range(5):
        numero = float(input("Informe o número: \n"))
        numeros.append(numero)
    return numeros

def maior(numeros):
    return max(numeros)


def menor(numeros):
    return min(numeros)

numeros = informar_numeros()

print(f"Maior número: {maior(numeros)}")
print(f"Menor número: {menor(numeros)}")

