#Problema: Inverter os dígitos de um número (ex: 123 → 321).

num = int(input("Digite um número: "))
invertido = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(f"Número invertido: {invertido}")