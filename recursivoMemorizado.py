# Usa recursão com memorização.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menorNumeroDeOperacoes(num: int, memo = None):
    # Caso base
    if num == 1:
        return 0, []

    menorNumOp = num
    melhorCaminho = []

    # Inicializa o dicionário de memorização
    if memo is None:
        memo = {}

    # Se já estiver calculado, apenas retorna
    if num in memo:
        return memo[num]

    # Decremento de 1
    operacoes, caminho = menorNumeroDeOperacoes(num - 1, memo)
    if operacoes < menorNumOp:
        menorNumOp = operacoes
        melhorCaminho = ["-1"] + caminho

    # Divisão por 2
    if num % 2 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(num // 2, memo)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/2"] + caminho

    # Divisão por 3
    if num % 3 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(num // 3, memo)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/3"] + caminho

    memo[num] = (1 + menorNumOp, melhorCaminho)
    return memo[num]
