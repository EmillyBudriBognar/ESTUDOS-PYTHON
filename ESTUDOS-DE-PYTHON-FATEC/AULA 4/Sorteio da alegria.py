from random import choice, randint
from time import sleep

frase = 'SORTEIO DA ALEGRIA!!!'

print('-' * 50)
for letra in frase:
    print(letra, end='')
    sleep(randint(1, 3) / 10)
print()
print('-' * 50)

alunos = [
    'Coleguinha 1',
    'Coleguinha 2',
    'Coleguinha 3',
    'Coleguinha 4',
    'Coleguinha 5',
    'Coleguinha 6',
    'Coleguinha 7']

sorteados = []
chances = randint(1, min(5, len(alunos)))
while chances > 0:
    sortudo = choice(alunos)
    print(sortudo)
    sorteados.append(sortudo)
    alunos.remove(sortudo)
    sleep(randint(2, 4))
    if chances > 1:
        print('(Poderia ser você... 😬)')
    else:
        print('(Eu escolho você! 😮)')
        sleep(randint(2, 5))
        if choice([True, False]):
            print('(Brincadeira! 👻👻👻)')
            sleep(2)
            print(f'\nNa verdade...\nEu escolho você! {choice(sorteados)}')
    print('-' * 30)
    sleep(randint(2, 5))
    chances -= 1
