from math import sqrt as raiz

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b - raiz(delta)) / (2*a)
    x2 = (-b + raiz(delta)) / (2*a)
    print(f'x1 = {x1:.2f} | x2 = {x2:.2f}')
else:
    print('Nao existem raízes reais')
