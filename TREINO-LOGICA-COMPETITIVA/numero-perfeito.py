#Problema: Verificar se um número é perfeito (soma dos divisores próprios é igual ao número).

num = int(input("Digite um número: "))
soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i
print("É perfeito." if soma == num else "Não é perfeito.")