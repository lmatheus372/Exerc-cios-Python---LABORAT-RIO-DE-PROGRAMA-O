
def permissao(perfil, chave, indice):
    try:
        return perfil[chave][indice]
    except KeyError:
        return "acesso_restrito"
    except IndexError:
        return "acesso_restrito"



perfil = {
    "admin": ["Ler", "Escrever", "Editar", "Excluir"],
    "usuario": ["Ler", "Escrever"],
}


print(permissao(perfil, "admin", 0))
