# Crie um programa que exiba todos os
# segundos do primeiro minuto.
# Exiba no formato hh:mm:ss.
# Faça com que cada segundo gaste um
# segundo para ser exibido.

from time import sleep

s = 0

while s < 60:
    print(f'00:00:{s:02}')
    s += 1
    sleep(1)
