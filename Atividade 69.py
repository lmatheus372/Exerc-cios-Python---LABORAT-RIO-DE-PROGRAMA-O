try:
    arquivo  = open("relatorio_vendas.txt", "r")

    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: arquivo não encontrado")

finally:
    print("Finalizada a execução")