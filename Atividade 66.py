def animais(cabecas, pernas):

    coelhos = (pernas - 2 * cabecas) // 2
    galinhas = cabecas - coelhos

    print(f"Coelhos: {coelhos}, Galinhas: {galinhas}")


animais(35, 94)