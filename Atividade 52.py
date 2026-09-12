medicamentos = {}

for i in range(5):
    nome = input("Informe o nome do medicamento: ")
    quantidade = int(input("Quantidade em estoque: "))
    medicamentos[nome] = quantidade

consulta = input("Qual o medicamento você deseja consultar ?\n ")

print(f"Quantidade em estoque: {medicamentos[consulta]}")
