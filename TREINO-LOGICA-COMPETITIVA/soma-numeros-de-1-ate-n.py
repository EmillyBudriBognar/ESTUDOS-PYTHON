#Problema: Calcular a soma de 1 até N.

n = int(input("Digite N: "))
soma = 0
i = 1

while i <= n:
    soma += i
    i += 1

print(f"A soma de 1 até {n} é {soma}.")