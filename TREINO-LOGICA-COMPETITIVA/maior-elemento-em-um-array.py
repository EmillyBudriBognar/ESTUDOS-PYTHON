#Problema: Encontrar o maior elemento em um array.

array = [10, 5, 20, 8, 15]
maior = array[0]
for num in array:
    if num > maior:
        maior = num
print(f"Maior elemento: {maior}")