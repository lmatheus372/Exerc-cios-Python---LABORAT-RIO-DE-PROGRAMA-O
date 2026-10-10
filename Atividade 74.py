produtos = {
    1: "Arroz",
    2: "Feijão",
    3: "Macarrão"
}


def produto(id):
    try:
        nome = produtos[id]
        return nome, 200
    except KeyError:
        return "Produto não encontrado", 404
    except Exception:
        return "Erro do servidor.", 500

print(produto(1))