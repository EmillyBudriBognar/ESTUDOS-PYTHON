a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

print('Triângulo', end=' ')

if a == b and b == c:
    print('Equilátero')
else:
    if a == b or b == c or a == c:
        print('Isósceles')
    else:
        print('Escaleno')
        
