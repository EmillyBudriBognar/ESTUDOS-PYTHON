#Problema: Converter um número decimal para binário.

decimal = int(input("Digite um número decimal: "))
binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal //= 2
print(f"Binário: {binario if binario else '0'}")