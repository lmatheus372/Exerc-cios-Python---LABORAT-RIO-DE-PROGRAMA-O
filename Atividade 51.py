print("Informe a temperatira da estufa dos últimos 5 dias")
lista = []
soma = 0

for i in range(5):
    temperatura = float(input("Temperatura: "))
    lista.append(temperatura)
    soma = soma + temperatura

media = soma / 5

if media >= 18 and media <= 28:
    print("Está dentro da faixa ideal de cultivo (entre 18°C e 28°C).")
else:
    print("Não está dentro da ffaixa ideal de cultivo (entre 18°C e 28°C).")

print(f"Segue todas as temperaturas cadastradas: {lista}")