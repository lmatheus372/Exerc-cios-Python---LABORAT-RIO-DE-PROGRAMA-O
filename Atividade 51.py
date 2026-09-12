print("Informe a temperatira da estufa dos últimos 5 dias")
lista = [] 
for i in range(5):
    print(int(input("Temperatura: ")))
    lista = [i]

media = lista / 5

if media >= 18 and media <= 28:
    print("Está dentro da faixa ideal de cultivo")
else:
    print("Não está dentro da ffaixa ideal de cultivo")