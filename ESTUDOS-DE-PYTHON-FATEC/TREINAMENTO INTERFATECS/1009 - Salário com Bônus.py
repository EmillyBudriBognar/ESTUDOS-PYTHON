def pagamento(salario_fixo, vendas):
    return salario_fixo + 0.15*vendas

nome = input()
salario_fixo = float(input())
vendas = float(input())
 
print(f'TOTAL = R$ {pagamento(salario_fixo, vendas):.2f}')
