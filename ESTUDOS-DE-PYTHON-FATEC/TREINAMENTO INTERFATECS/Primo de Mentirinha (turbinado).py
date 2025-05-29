from time import time

def tempo(f, *a):
    inicio = time()
    r = f(*a)
    return (r, time() - inicio)

def gera_lista(limite):
    L = []
    for n in range(1, limite+1):
        if mentirinha(n):
            L.append(n)
    return L

def mentirinha(n):
    qtd_divisores = 0
    metade = n // 2
    for pd in range(2, metade+1):
        if n % pd == 0:
            qtd_divisores += 1
            if qtd_divisores == 2:
                return False
    return qtd_divisores == 1

def main():
    limite = int(input('Limite? '))
    L, t = tempo(gera_lista, limite)
    print(f'Tempo: {t:.2f}seg')
    print(f'L = {L}')

main()
