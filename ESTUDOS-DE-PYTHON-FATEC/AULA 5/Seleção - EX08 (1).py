# Leia: 
# https://www.todamateria.com.br/condicao-de-existencia-de-um-triangulo/

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

if a < b+c and b < a+c and c < a+b:
    print('formam')
else:
    print('não formam')
