preco = float(input('Preço? R$ '))
qtd = int(input('Quantidade? '))
total = preco * qtd
desconto = total * 0.10
final = total - desconto
print('Total a pagar: R$', final)
