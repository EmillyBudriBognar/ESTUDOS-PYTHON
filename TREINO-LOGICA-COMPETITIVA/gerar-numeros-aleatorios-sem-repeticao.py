#Problema: Gerar N números aleatórios únicos entre 1 e 100.

import random
n = int(input("Quantos números aleatórios? "))
numeros = random.sample(range(1, 101), n)
print(f"Números aleatórios: {numeros}")