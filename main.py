# T1 de Projeto e Otimização de Algoritmos - Caroline de Lima

from recursivoSimples import menorNumeroDeOperacoes as recursivoSimples
from recursivoMemorizado import menorNumeroDeOperacoes as recursivoMemorizado
from iterativo import menorNumeroDeOperacoes as iterativo

def exibirMenu():
    print("\n======== Opções de execução ========")
    print("1 - Versão recursiva simples")
    print("2 - Versão recursiva com memorização")
    print("3 - Versão iterativa (sem recursão)")
    print("0 - Sair")

def main():
    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ").strip()

        if not opcao.isdigit():
            print("Opção inválida! Digite um número entre 1 e 3 ou 0 para sair.")
            continue

        opcao = int(opcao)

        if opcao == 0:
            print("Bye bye honey...")
            break

        if opcao not in [1, 2, 3]:
            print("Opção inválida! Digite um número entre 1 e 3 ou 0 para sair.")
            continue

        try:
            n = int(input("Digite o número: ").strip())
            if n < 1:
                print("O número deve ser maior ou igual a 1.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if opcao == 1:
            resultado, caminho = recursivoSimples(n)
        elif opcao == 2:
            resultado, caminho = recursivoMemorizado(n)
        else:
            resultado, caminho = iterativo(n)

        print(f"\nMenor número de operações: {resultado}")
        print("Caminho das operações:", " ".join(caminho))

if __name__ == "__main__":
    main()
