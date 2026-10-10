def calcular_media(n1, n2, n3):
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        raise ValueError("Notas invalida.")
    media = (n1 + n2 + n3) / 3
    return media

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das notas é: {media:.2f}")
    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

except ValueError:
    print("Notas invalidas, digite valores entre 0 e 10.")
