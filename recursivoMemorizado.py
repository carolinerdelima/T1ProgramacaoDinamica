# Usa recursão com memorização.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menorNumeroDeOperacoes(n: int, memo = None):
    # Caso base
    if n == 1:
        return 0, []

    menorNumOp = n
    melhorCaminho = []

    # Inicializa o dicionário de memorização
    if memo is None:
        memo = {}

    # Se já estiver calculado, apenas retorna
    if n in memo:
        return memo[n]

    # Decremento de 1
    operacoes, caminho = menorNumeroDeOperacoes(n - 1, memo)
    if operacoes < menorNumOp:
        menorNumOp = operacoes
        melhorCaminho = ["-1"] + caminho

    # Divisão por 2
    if n % 2 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(n // 2, memo)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/2"] + caminho

    # Divisão por 3
    if n % 3 == 0:
        operacoes, caminho = menorNumeroDeOperacoes(n // 3, memo)
        if operacoes < menorNumOp:
            menorNumOp = operacoes
            melhorCaminho = ["/3"] + caminho

    memo[n] = (1 + menorNumOp, melhorCaminho)
    return memo[n]
