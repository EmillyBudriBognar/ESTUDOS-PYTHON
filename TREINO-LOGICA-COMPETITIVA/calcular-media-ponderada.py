#Problema: Calcular a média ponderada de 3 notas com pesos 2, 3 e 5.

nota1 = float(input("Nota 1 (peso 2): "))
nota2 = float(input("Nota 2 (peso 3): "))
nota3 = float(input("Nota 3 (peso 5): "))
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print(f"Média ponderada: {media:.2f}")