#Problema: Calcular a área de um círculo dado o raio.

import math
raio = float(input("Digite o raio: "))
area = math.pi * raio ** 2
print(f"Área: {area:.2f}")