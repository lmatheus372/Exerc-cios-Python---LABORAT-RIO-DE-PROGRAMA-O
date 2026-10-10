import traceback


def processar(dados):

    for valor in dados:
        try:
            numero = float(valor)
            print(f"Processando o número: {numero}")
        except (TypeError, ValueError):
            print(f"Erro ao processar o valor: {valor}")
            traceback.print_exc()

dados = ["10", "20", "30", "abc", "50"]

processar(dados)
    