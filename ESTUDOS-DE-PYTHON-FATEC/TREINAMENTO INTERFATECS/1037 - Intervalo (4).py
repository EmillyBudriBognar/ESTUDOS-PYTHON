x = float(input())

if 0 <= x and x <= 100:
    if 0 <= x <= 25:
        print('Intervalo [0,25]')
    elif 25 < x <= 50:
        print('Intervalo (25,50]')
    elif 50 < x <= 75:
        print('Intervalo (50,75]')
    else:
        print('Intervalo (75,100]')
else:
    print('Fora de intervalo') 
