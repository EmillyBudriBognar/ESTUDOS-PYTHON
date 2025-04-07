a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a > b and a > c:
    print('Maior número:', a)
else:
    if b > a and b > c:
        print('Maior número:', b)
    else:
        print('Maior número:', c)
