# Crie um programa que exiba todos os
# segundos de todos os minutos de todas
# as horas de todos os dias
# "Para todo o sempre" (Disney).
# Só que decrescente.
# Exiba no formato hh:mm:ss.
# Faça com que cada segundo gaste um
# segundo para ser exibido.

from time import sleep

while True:
    h = 23
    while h >= 0:
        m = 59
        while m >= 0:
            s = 59
            while s >= 0:
                print(f'{h:02}:{m:02}:{s:02}')
                s -= 1
                #sleep(0.1)
            m -= 1
        h -= 1
