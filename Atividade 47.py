matriz = [[5, -8, 10],
          [-15, 9, -2],
          [-10, 60, 1]

          ]
contador = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            contador= contador + 1

print(f"A quantidade de números positivos são: {contador}")

