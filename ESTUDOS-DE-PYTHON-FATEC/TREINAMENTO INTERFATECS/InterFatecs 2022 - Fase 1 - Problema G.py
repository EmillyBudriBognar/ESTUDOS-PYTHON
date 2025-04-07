tara_prato = float(input())
peso_prato = float(input())
preco_quilo = float(input())

peso_comida = peso_prato - tara_prato
preco = peso_comida * preco_quilo

print(f'{preco:.2f}')
