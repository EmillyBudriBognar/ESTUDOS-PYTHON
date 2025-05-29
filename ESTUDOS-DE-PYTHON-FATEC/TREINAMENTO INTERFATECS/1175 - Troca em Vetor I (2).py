def gera_lista(qtd):
    L = []
    for i in range(qtd):
        L.append(int(input()))
    return L

def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def inverte(L, qtd):
    i = 0
    j = qtd-1
    while i < j:
        troca(L, i, j)
        i += 1
        j -= 1

def exibe_lista(L, qtd):
    for i in range(qtd):
        print(f'N[{i}] = {L[i]}')

def main():
    L = gera_lista(20)
    inverte(L, 20)
    exibe_lista(L, 20)

main()
