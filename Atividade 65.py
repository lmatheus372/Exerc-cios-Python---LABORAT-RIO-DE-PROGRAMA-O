def calcularCubo(numero):
    parametro = numero ** 3
    return parametro


def calcularDivisaoCubo(numero):
    parametro = numero % 3
    if parametro == 0:
        return  calcularCubo(numero)
    else:
        return False


print(calcularCubo(10))
print(calcularDivisaoCubo(10))