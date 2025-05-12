#Problema: Verificar se um número ou palavra é palíndromo.

texto = input("Digite um número ou palavra: ")
invertido = texto[::-1]

if texto == invertido:
    print(f"{texto} é palíndromo.")
else:
    print(f"{texto} não é palíndromo.")