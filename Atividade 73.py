precos = [91, 20, 85]


for preco in precos:
    try:
        valor = float(preco)
    except ValueError:
        print("Valor inválido. Digite novamente.")

    else:
        desconto = valor * 0.10
        valor_final = valor - desconto
        print(valor_final)
