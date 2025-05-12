#Problema: Remover todas as vogais de uma string.

texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
texto_sem_vogais = "".join([c for c in texto if c not in vogais])
print(f"Texto sem vogais: {texto_sem_vogais}")