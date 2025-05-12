#Problema: Converter um número decimal para hexadecimal.

decimal = int(input("Digite um número decimal: "))
hexadecimal = hex(decimal).upper().replace("0X", "")
print(f"Hexadecimal: {hexadecimal}")