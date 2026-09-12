tupla = ("Matemática", "Português")

alunos = {"Matheus" : [10, 9.7],
          "Juninho" : [2.9, 4.0],
          }
soma = 0

soma_matheus = alunos["Matheus"][0] + alunos["Matheus"][1]
media_matheus = soma_matheus / 2

soma_juninho = alunos["Juninho"][0] + alunos["Juninho"][1]
media_juninho = soma_juninho / 2

if media_matheus >= 7:
    print("Matheus está aprovado")
else:
    print("Matheus está reprovado")



if media_juninho >= 7:
    print("Juninho está aprovado")
else:
    print("Juninho está reprovado")

print(f"Disciplinas cadastradas: {tupla}")
