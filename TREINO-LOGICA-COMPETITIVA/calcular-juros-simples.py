#Problema: Calcular juros simples (J = P * i * t).

principal = float(input("Capital inicial (P): "))
taxa = float(input("Taxa de juros (i): "))
tempo = float(input("Tempo (t): "))
juros = principal * taxa * tempo
print(f"Juros simples: {juros:.2f}")