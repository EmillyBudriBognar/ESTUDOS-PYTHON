def se_par(n):
    return n % 2 == 0

x = int(input('Número? '))

if se_par(x):
    print('é par')
else:
    print('não é par')
