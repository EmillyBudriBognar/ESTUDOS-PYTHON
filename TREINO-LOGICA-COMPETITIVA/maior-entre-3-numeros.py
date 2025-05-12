#Problema: Encontrar o maior entre três números.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O maior número é {maior}.")