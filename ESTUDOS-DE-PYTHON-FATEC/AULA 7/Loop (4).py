# Crie um programa que exiba ao usuário
# os n primeiros números naturais pares.
# Obs.: Considere que n será um número
#       dado pelo usuário no começo do
#       programa.

qtd = int(input('Quantidade? '))
i = 0

while qtd > 0:
    print(i)
    qtd -= 1
    i += 2

print('Fim!')
