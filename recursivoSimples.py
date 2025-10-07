# Usa apenas recursão simples -> sem memorização.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menorNumeroDeOperacoes(num: int):
    # Caso base
    if num == 1:
        return 0, []

    menorNumOp = num
    melhorCaminho = []

    # Decremento de 1
    operacoes, caminho = menorNumeroDeOperacoes(num - 1)
    if operacoes < menorNumOp:
        menorNumOp = operacoes
        melhorCaminho = ["-1"] + caminho

    # Divisão por 2
    if num % 2 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(num // 2)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/2"] + caminho

    # Divisão por 3
    if num % 3 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(num // 3)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/3"] + caminho

    return 1 + menorNumOp, melhorCaminho
