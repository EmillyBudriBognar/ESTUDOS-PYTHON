#Problema: Contar quantas vogais existem em uma palavra.

palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
contador = 0
i = 0

while i < len(palavra):
    if palavra[i] in vogais:
        contador += 1
    i += 1

print(f"A palavra tem {contador} vogais.")