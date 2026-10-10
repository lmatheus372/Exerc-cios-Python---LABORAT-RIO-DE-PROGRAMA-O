

while True:
    try:
        acionistas = int(input("Digite o número de acionistas: "))
        lucros = float(input("Digite o lucro total da empresa: "))
        calculculo = lucros / acionistas
        print(f"O lucro por acionista é: {calculculo}")
        break
    except ZeroDivisionError:
        print("Erro: O número de acionistas não pode ser zero.")
    except ValueError:
        print("Valores inválidos. Digite apenas números!")