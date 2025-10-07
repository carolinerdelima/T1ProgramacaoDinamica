# Usa programação dinâmica iterativa -> bottom-up.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menorNumeroDeOperacoes(num: int):
    operacoes = [0] * (num + 1)
    anterior = [0] * (num + 1)
    opUsada = [""] * (num + 1)

    # Caso base
    operacoes[1] = 0

    for i in range(2, num + 1):
        # Decremento de 1
        menorNumOp = operacoes[i - 1] + 1
        anterior[i] = i - 1
        opUsada[i] = "-1"

        # Divisão por 2 (se possível)
        if i % 2 == 0 and operacoes[i // 2] + 1 < menorNumOp:
            menorNumOp = operacoes[i // 2] + 1
            anterior[i] = i // 2
            opUsada[i] = "/2"

        # Divisão por 3 (se possível)
        if i % 3 == 0 and operacoes[i // 3] + 1 < menorNumOp:
            menorNumOp = operacoes[i // 3] + 1
            anterior[i] = i // 3
            opUsada[i] = "/3"

        operacoes[i] = menorNumOp

    # Reconstrói o caminho percorrido a partir de num até 1
    caminho = []
    atual = num
    while atual != 1:
        caminho.append(opUsada[atual])
        atual = anterior[atual]

    return operacoes[num], caminho
