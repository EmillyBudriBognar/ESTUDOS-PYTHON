#Problema: Calcular o fatorial de um número usando recursão.

def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)

num = int(input("Digite um número: "))
print(f"Fatorial de {num}: {fatorial(num)}")