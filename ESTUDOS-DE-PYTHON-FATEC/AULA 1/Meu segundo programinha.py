# Crie um programa que solicite ao usuário um
# salário e, ao final, exiba o mesmo salário
# acrescido de 10%.
# Exemplo: 1500.00 (entrada)
#          1650.00 (saída)

salario = float(input('Salário? R$ '))
aumento = salario * 0.10
novo = salario + aumento
print('Novo salário: R$', novo)
