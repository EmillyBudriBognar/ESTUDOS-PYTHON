#Problema: Contar quantos dígitos um número tem.

num = int(input("Digite um número: "))
contador = 0

while num != 0:
    num = num // 10
    contador += 1

print(f"O número tem {contador} dígitos.")