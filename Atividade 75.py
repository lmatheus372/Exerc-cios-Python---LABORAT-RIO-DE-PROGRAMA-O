def conectar_api():
    raise ConnectionError


def conexao():

    for tentativa in range(1, 4):
        try:
            conectar_api()
            print("Conexão feita!")
            return
        except ConnectionError:
            print(f"Falha na tentativa {tentativa}.")

    print("Limite de tentativas atingido.")


conexao()