def maximo(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input('Número? '))
y = int(input('Número? '))
m = maximo(x, y)
print(f'Máximo: {m}')
    
