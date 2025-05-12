#Problema: Verificar se um número é primo.

num = int(input("Digite um número: "))
primo = True

if num <= 1:
    primo = False
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            primo = False
            break
        i += 1

print(f"{num} é primo." if primo else f"{num} não é primo.")