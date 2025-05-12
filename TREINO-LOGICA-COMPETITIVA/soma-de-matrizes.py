#Problema: Somar duas matrizes 2x2.

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]
print(f"Soma das matrizes: {resultado}")