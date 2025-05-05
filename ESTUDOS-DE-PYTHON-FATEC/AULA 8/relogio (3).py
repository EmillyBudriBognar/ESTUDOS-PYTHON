# Crie um programa que exiba todos os
# segundos de todos os minutos da primeira
# hora.
# Exiba no formato hh:mm:ss.
# Faça com que cada segundo gaste um
# segundo para ser exibido.

from time import sleep

m = 0
while m < 60:
    s = 0
    while s < 60:
        print(f'00:{m:02}:{s:02}')
        s += 1
        sleep(0.1)
    m += 1

