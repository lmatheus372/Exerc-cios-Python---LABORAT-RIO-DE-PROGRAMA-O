import random

numero = int(input("Digite um número de 1 a 10: "))
sorteio = random.randint(1, 11)

if numero == sorteio:
    print("Parabéns! Você acertou o número sorteado!")
else:
    print(f"Você errou! O número sorteado foi: {sorteio}")

