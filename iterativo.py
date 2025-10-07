# Usa programação dinâmica iterativa -> bottom-up.
# Retorna uma tupla -> número mínimo de operações, lista de operações.

def menor_numero_de_operacoes(n: int):
    operacoes = [0] * (n + 1)
    anterior = [0] * (n + 1)
    op_usada = [""] * (n + 1)

    # Caso base
    operacoes[1] = 0

    # Calcula de 2 até n
    for i in range(2, n + 1):
        # Decremento de 1
        menor_custo = operacoes[i - 1] + 1
        anterior[i] = i - 1
        op_usada[i] = "-1"

        # Divisão por 2 (se possível)
        if i % 2 == 0 and operacoes[i // 2] + 1 < menor_custo:
            menor_custo = operacoes[i // 2] + 1
            anterior[i] = i // 2
            op_usada[i] = "/2"

        # Divisão por 3 (se possível)
        if i % 3 == 0 and operacoes[i // 3] + 1 < menor_custo:
            menor_custo = operacoes[i // 3] + 1
            anterior[i] = i // 3
            op_usada[i] = "/3"

        operacoes[i] = menor_custo

    # Reconstrói o caminho percorrido a partir de n até 1
    caminho = []
    atual = n
    while atual != 1:
        caminho.append(op_usada[atual])
        atual = anterior[atual]

    return operacoes[n], caminho
