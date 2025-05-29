def mentirinha(n):
    qtd_divisores = 0
    for pd in range(1, n+1):
        if n % pd == 0:
            qtd_divisores += 1
    return qtd_divisores == 3

n = int(input('n? '))

if mentirinha(n):
    print('sim')
else:
    print('nao')
