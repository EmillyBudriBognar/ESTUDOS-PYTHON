def media(a, b, c):
    return (a + b + c) / 3

x = float(input('Número? '))
y = float(input('Número? '))
z = float(input('Número? '))

m = media(x, y, z)

print(f'Média: {m:.2f}')
