from random import randint as aleatorio

def cria_matriz(linhas, colunas):
    M = []
    for i in range(linhas):
        M.append(colunas * [None])
    return M

def exibe_matriz(M, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            print(M[i][j], end='')
            if j < colunas-1:
                print(' ', end='')
            else:
                print()

def preenche_matriz(M, linhas, colunas, tipo):
    for i in range(linhas):
        for j in range(colunas):
            M[i][j] = tipo(input(f'M[{i}][{j}]? '))
        print()

def soma_matriz(M, linhas, colunas):
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            soma += M[i][j]
    return soma

def media_matriz(M, linhas, colunas):
    return soma_matriz(M, linhas, colunas) / (linhas * colunas)

def preenche_aleatorio(M, linhas, colunas, tipo):
    for i in range(linhas):
        for j in range(colunas):
            M[i][j] = tipo(aleatorio(10, 99))

def item_minimo(M, linhas, colunas):
    minimo = M[0][0]
    for i in range(linhas):
        for j in range(colunas):
            if M[i][j] < minimo:
                minimo = M[i][j]
    return minimo

def item_maximo(M, linhas, colunas):
    maximo = M[0][0]
    for i in range(linhas):
        for j in range(colunas):
            if M[i][j] > maximo:
                maximo = M[i][j]
    return maximo

def exibe_colunas(M, linhas, colunas):
    for j in range(colunas):
        for i in range(linhas):
            print(M[i][j], end='')
            if i < linhas-1:
                print(' ', end='')
            else:
                print()

def main():
    linhas = int(input('Quantas linhas? '))
    colunas = int(input('Quantas colunas? '))
    M = cria_matriz(linhas, colunas)
    exibe_matriz(M, linhas, colunas)
    preenche_matriz(M, linhas, colunas, int)
    exibe_matriz(M, linhas, colunas)
    print(f'Soma = {soma_matriz(M, linhas, colunas)}')
    print(f'Média = {media_matriz(M, linhas, colunas)}')
    preenche_aleatorio(M, linhas, colunas, int)
    exibe_matriz(M, linhas, colunas)
    print(f'Ítem mínimo = {item_minimo(M, linhas, colunas)}')
    print(f'Ítem máximo = {item_maximo(M, linhas, colunas)}')
    exibe_colunas(M, linhas, colunas)

main()
