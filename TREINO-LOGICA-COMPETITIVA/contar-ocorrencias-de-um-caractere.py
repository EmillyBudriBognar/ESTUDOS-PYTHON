#Problema: Contar quantas vezes um caractere aparece em uma string.

texto = input("Digite um texto: ")
caractere = input("Digite o caractere a contar: ")
contador = texto.count(caractere)
print(f"O caractere '{caractere}' aparece {contador} vezes.")