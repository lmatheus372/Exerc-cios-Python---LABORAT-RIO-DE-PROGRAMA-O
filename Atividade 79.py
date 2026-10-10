def cadastrar_produto(nome, preco, quantidade):
    if nome == "":
        raise ValueError("Nome invalido.")
    if preco <= 0:
        raise ValueError("Preco invalido.")
    if quantidade < 0:
        raise ValueError("Quantidade invalida.")

    return "Produto cadastrado com sucesso!"

try:
    print(cadastrar_produto("Arroz", 5.99, 10))

except ValueError:
    print("Erro ao cadastrar produto, verifique os dados informados.")