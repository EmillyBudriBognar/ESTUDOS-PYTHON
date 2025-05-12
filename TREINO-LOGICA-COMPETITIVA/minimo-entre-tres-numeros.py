#Problema: Encontrar o menor entre três números.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
menor = a if a < b and a < c else (b if b < c else c)
print(f"Menor: {menor}")