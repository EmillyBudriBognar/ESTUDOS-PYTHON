#Problema: Calcular o fatorial de um número usando while.

n = int(input("Digite um número: "))
fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i += 1

print(f"O fatorial de {n} é {fatorial}.")