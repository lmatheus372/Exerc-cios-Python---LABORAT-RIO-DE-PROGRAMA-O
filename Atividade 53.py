import random

grupo = ["Ana", "Carlos", "Pedro", "Beatriz" , "Maria"]

numero = random.randint(0, 4)
sorteio = grupo[numero]

print(f"O membro escolhido para ser lider é: {sorteio}")