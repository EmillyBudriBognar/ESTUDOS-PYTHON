#Problema: Calcular a transposta de uma matriz 2x2.

matriz = [[1, 2], [3, 4]]
transposta = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        transposta[j][i] = matriz[i][j]
print(f"Transposta: {transposta}")