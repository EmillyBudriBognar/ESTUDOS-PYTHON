def gera_lista(qtd):
    L = []
    for i in range(qtd):
        L.append(int(input()))
    return L

def exibe_lista(L, qtd):
    i = qtd - 1
    j = 0
    while i >= 0:
        print(f'N[{j}] = {L[i]}')
        i -= 1
        j += 1

def main():
    L = gera_lista(20)
    exibe_lista(L, 20)

main()
