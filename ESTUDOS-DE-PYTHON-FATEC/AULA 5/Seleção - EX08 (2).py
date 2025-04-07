# Leia: 
# https://www.todamateria.com.br/condicao-de-existencia-de-um-triangulo/

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a >= b+c or b >= a+c or c >= a+b:
    print('não formam')
else:
    print('formam')
