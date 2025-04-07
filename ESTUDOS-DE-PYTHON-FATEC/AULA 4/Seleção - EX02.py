a = int(input('a? '))
b = int(input('b? '))
resto = a - (a // b * b)
if resto == 0:
    print('divisível')
else:
    print('não divisível')
