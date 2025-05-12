#Problema: Calcular juros compostos (M = P * (1 + i)^t).

principal = float(input("Capital inicial (P): "))
taxa = float(input("Taxa de juros (i): "))
tempo = float(input("Tempo (t): "))
montante = principal * (1 + taxa) ** tempo
print(f"Montante: {montante:.2f}")