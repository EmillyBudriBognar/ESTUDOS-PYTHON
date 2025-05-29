def gera_lista(v, qtd):
    L = [v]
    for i in range(1, qtd):
        L.append(2 * L[i-1])
    return L

def exibe_lista(L, qtd):
    i = 0
    while i < qtd:
        print(f'N[{i}] = {L[i]}')
        i += 1

def main():
    v = int(input())
    L = gera_lista(v, 10)
    exibe_lista(L, 10)

main()
