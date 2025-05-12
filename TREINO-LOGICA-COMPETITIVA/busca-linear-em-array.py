#Problema: Verificar se um número está em um array.

array = [4, 7, 2, 9, 5]
alvo = int(input("Digite o número a buscar: "))
encontrado = False
for num in array:
    if num == alvo:
        encontrado = True
        break
print(f"O número {alvo} está no array." if encontrado else "Não está no array.")