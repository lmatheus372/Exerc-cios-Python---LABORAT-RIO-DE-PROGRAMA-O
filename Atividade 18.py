total_faturamento = 0

for i in range(1, 6):
    faturamento = float(input("Digite o valor das vendas do dia: "))
    total_faturamento = total_faturamento + faturamento

print(f"O total faturado foi: {total_faturamento:.2f}")