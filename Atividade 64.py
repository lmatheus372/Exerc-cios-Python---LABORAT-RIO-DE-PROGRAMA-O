def numeros(a, b, c):
    soma = a + b + c
    if soma > 21 and (a == 11 or b == 11 or c == 11):
        soma = soma - 10
    if soma <= 21:
        return soma
    else:
        return -1

print(numeros(10, 1, 5))


