# Usa apenas recursão simples -> sem memorização.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menorNumeroDeOperacoes(n: int):
    # Caso base
    if n == 1:
        return 0, []

    menorNumOp = n
    melhorCaminho = []

    # Decremento de 1
    operacoes, caminho = menorNumeroDeOperacoes(n - 1)
    if operacoes < menorNumOp:
        menorNumOp = operacoes
        melhorCaminho = ["-1"] + caminho

    # Divisão por 2
    if n % 2 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(n // 2)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/2"] + caminho

    # Divisão por 3
    if n % 3 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(n // 3)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/3"] + caminho

    return 1 + menorNumOp, melhorCaminho
