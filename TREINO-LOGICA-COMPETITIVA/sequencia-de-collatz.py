#Problema: Gerar a sequência de Collatz para um número N (se N é par, divide por 2; se ímpar, multiplica por 3 e soma 1).

n = int(input("Digite um número: "))
sequencia = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequencia.append(n)
print(f"Sequência de Collatz: {sequencia}")