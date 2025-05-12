#Problema: Verificar se duas palavras são anagramas.

palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()
print("São anagramas." if sorted(palavra1) == sorted(palavra2) else "Não são anagramas.")