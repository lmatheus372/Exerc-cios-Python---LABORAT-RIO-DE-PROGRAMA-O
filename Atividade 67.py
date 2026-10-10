

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade invalida. A idade não deve ser menor que zero.")
        else:
            print("Valor válido!")
            break
    except ValueError:
        print("Idade inválida. Digite apenas números!")
