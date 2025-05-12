#Problema: Calcular o Índice de Massa Corporal (IMC).

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")