class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")

    saldo -= valor
    return saldo

try:
    print(sacar(100, 150))
    
except SaldoInsuficienteError:
    print("Erro: Saldo insuficiente para efetuar o saque.")