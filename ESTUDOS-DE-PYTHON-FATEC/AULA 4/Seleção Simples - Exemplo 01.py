prod = float(input('Preço? R$ '))
qtd = int(input('Quantidade? '))
total = prod * qtd

if total >= 150.00:
    desconto = 0.15 * total
    total -= desconto

print(f'Total = R$ {total:.2f}')
