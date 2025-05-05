# Crie um programa que exiba todos os
# segundos de todos os minutos de todas
# as horas de um dia.
# Exiba no formato hh:mm:ss.
# Faça com que cada segundo gaste um
# segundo para ser exibido.

from time import sleep

h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            s += 1
            #sleep(0.1)
        m += 1
    h += 1
