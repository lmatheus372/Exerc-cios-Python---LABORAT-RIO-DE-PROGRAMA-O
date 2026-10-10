def realizar_saque(valor, valor_saque):
    if valor_saque <= 0:
        raise ValueError("Valor invalido.")
    if valor_saque > valor:
        raise Exception("Saldo insuficiente.")

    novo_saldo = saldo - valor_saque
    return novo_saldo

try: 
    saldo = 5461
    valor = float(input("Digite o valor do saque: "))
    saldo = realizar_saque(saldo, valor)
    print(f"Novo saldo: {saldo}")
except ValueError:
    print("Valor invalido, ou saldo insuficiente.")
except Exception:
    print("Erro ao realizar o saque.")