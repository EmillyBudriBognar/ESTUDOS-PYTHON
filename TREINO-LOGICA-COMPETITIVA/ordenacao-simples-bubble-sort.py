#Problema: Ordenar um array em ordem crescente usando Bubble Sort.

array = [5, 3, 8, 1, 2]
n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(f"Array ordenado: {array}")