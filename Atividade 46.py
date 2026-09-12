matriz = [[30,50,5], 
          [25,10,85], 
          [42,15,92]
        ]
soma = 0

for i in range(len(matriz)):
    soma = matriz[i][i] + soma

print(soma)