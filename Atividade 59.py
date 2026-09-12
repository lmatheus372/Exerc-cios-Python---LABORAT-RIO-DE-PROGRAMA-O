def verificar(a, b):
    numero = [a, b]

    if a % 2 != 0 or b % 2 != 0:
        return min(numero)
    else:
        return max(numero)


print(verificar(4, 10))