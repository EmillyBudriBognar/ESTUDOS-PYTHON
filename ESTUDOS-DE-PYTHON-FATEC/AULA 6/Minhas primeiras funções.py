def educada(nome):
    print(f'Bom dia {nome}!')

def exibe_media(n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma / 3)

def retorna_media(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma / 3

educada('Joãozinho')

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

r1 = retorna_media(a, b, c)
print(f'r1 = {r1}')

r2 = exibe_media(a, b, c)
print(f'r2 = {r2}')
