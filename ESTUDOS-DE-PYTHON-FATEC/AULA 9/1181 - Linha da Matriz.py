def cria_matriz(L, C):
    """
    A função retornará uma matriz de float.
    L: Quantidade de linhas na matriz.
    C: Quantidade de colunas na matriz.
    """
    M = []
    for i in range(L):
        linha = C * [0.0]
        M.append(linha)
    return M

def preenche(M, L, C):
    """
    M: Matriz que será preenchida.
    L: Quantidade de linhas da matriz.
    C: Quantidade de colunas da matriz.
    """
    for i in range(L):
        for j in range(C):
            M[i][j] = float(input())

def resultado(operacao, M, L, C):
    soma = 0
    for i in range(C):
        soma += M[L][i]
    if operacao == 'S':
        return soma
    else:
        return soma / C

def main():
    linha_operacao = int(input())
    operacao = input()
    M = cria_matriz(12, 12)
    preenche(M, 12, 12)
    resp = resultado(operacao, M, linha_operacao, 12)
    print(f'{resp:.1f}')

main()
