d = int(input('Dia? '))

if d >= 1 and d <= 7:
    if d == 1:
        print('domingo')
    elif d == 2:
        print('segunda')
    elif d == 3:
        print('terça')
    elif d == 4:
        print('quarta')
    elif d == 5:
        print('quinta')
    elif d == 6:
        print('sexta')
    else:
        print('sábado')
else:
    print('dia inválido')

