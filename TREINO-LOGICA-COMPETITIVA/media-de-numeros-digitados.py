#Problema: Calcular a média de números até o usuário digitar 0.

soma = 0
contador = 0
num = float(input("Digite um número (0 para parar): "))

while num != 0:
    soma += num
    contador += 1
    num = float(input("Digite outro número (0 para parar): "))

if contador > 0:
    print(f"Média: {soma / contador}")
else:
    print("Nenhum número foi digitado.")