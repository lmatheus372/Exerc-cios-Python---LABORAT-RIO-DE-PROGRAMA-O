matriz = [[1, 0, 1],
          [1, 1, 0],
          [0, 1, 1]]

contador = 0
contador2 = 0

for linha in matriz:
    for valor in linha:
        if valor == 0:
            contador= contador + 1
        else:
            contador2 = contador2 + 1

print(f"Vagas ocupadas: {contador2}")
print(f"Vagas livres: {contador}")