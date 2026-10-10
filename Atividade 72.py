


def parse_cpf():
    cpf = input("Digite seu CPF:")
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido. Digite novamente.")
    return cpf




def main():
    try:
        cpf = parse_cpf()
        print(f"CPF válido: {cpf}")
    except ValueError:
        print("CPF inválido. Digite novamente.")

main()