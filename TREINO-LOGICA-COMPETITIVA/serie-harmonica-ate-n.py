#Problema: Calcular a soma da série harmônica (1 + 1/2 + 1/3 + ... + 1/N).

n = int(input("Digite N: "))
soma = 0.0
i = 1

while i <= n:
    soma += 1 / i
    i += 1

print(f"Soma harmônica: {soma:.2f}")