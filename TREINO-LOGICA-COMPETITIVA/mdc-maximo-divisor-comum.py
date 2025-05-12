#Problema: Calcular o MDC entre dois números.

a = int(input("Digite A: "))
b = int(input("Digite B: "))

while b != 0:
    a, b = b, a % b

print(f"MDC: {a}")