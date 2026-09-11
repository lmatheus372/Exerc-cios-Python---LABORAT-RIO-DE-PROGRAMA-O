import random

numero = random.randint(1, 10)

tentativa = int(input("Advinhe o número de 1 a 10: "))

while tentativa != numero:
    if  tentativa < numero:
        print("O valor correto é maior")
    else:
        print("O número correto é menor")

    tentativa = int(input("Tente de novo: "))

print("Você acertou !!!!")



