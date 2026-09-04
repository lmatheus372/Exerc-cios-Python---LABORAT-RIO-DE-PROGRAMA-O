nota = float(input("Informe uma nota de satisfação (0-10) ou digite 0 para sair: "))
soma = 0

while nota != 0:
    soma = soma + nota
    nota = float(input("Informe uma nota de satisfação (0-10) ou digite 0 para sair: "))

print(f"A soma das notas é: {soma}")
