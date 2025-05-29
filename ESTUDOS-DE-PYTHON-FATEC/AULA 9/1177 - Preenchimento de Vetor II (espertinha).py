# Versão espertinha.

def exibe(L, n):
    for posicao, item in enumerate(L[:n]):
        print(f'N[{posicao}] = {item}')

def preenche(L, n, t):
    for i in range(n):
        L[i] = i % t

def main():
    t = int(input())
    tamanho = 1000
    L = tamanho * [0]
    preenche(L, tamanho, t)
    exibe(L, tamanho)

main()
