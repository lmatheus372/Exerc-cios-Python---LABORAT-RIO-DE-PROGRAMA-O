def perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i

    if soma == numero:
        print("Número Perfeito!!!!")
    else:
        print("Número imperfeito!")

perfeito(6)