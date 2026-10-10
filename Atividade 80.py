class ProdutoInvalidoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

def registrar_venda(produto, preco, quantidade):
    if produto == "":
        raise ProdutoInvalidoError("Produto invalido.")
    if preco <= 0:
        raise ValorInvalidoError("Preco invalido.")
    if quantidade <= 0:
        raise QuantidadeInvalidaError("Quantidade invalida.")

    total = preco * quantidade

    venda ={
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }
    return venda

def gerar_relatorio(vendas):
    if len(vendas) == 0:
        print("Nenhuma venda registrada.")
        return

    faturamento = 0
    produtos = {}

    for venda in vendas:
        faturamento += venda["total"]
        produto = venda["produto"]
        quantidade = venda["quantidade"]

        if produto in produtos:
            produtos[produto] += quantidade
        else:
            produtos[produto] = quantidade

    maior_quantidade = 0
    mais_vendido = ""

    for produto in produtos:
        if produtos[produto] > maior_quantidade:
            maior_quantidade = produtos[produto]
            mais_vendido = produto

    ticket_medio = faturamento / len(vendas)

    print("Relatório de Vendas:")
    print(f"Quantidade de vendas: {len(vendas)}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Produto mais vendido: {mais_vendido}")

vendas = []
while True:
        produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
        if produto == "fim":
            break
        try:
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade: "))
            venda = registrar_venda(produto, preco, quantidade)
        except ProdutoInvalidoError:
            print("Produto invalido.")
        except ValorInvalidoError:
            print("Preco invalido.")
        except QuantidadeInvalidaError:
            print("Quantidade invalida.")
        except ValueError:
            print("Informe apenas números.")
        else:
            vendas.append(venda)
        finally:
            print("Fim da tentativa.\n")    

gerar_relatorio(vendas)


