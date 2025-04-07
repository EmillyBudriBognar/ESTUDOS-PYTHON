a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

print('Maior número:', end=' ')

if a > b and a > c:
    print(a)
else:
    if b > a and b > c:
        print(b)
    else:
        print(c)
