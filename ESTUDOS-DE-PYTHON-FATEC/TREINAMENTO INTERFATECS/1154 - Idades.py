soma = 0
qtd = 0

idade = int(input())

while idade >= 0:
    soma += idade
    qtd += 1
    idade = int(input())

print(f'{soma / qtd:.2f}')
