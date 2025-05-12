#Problema: Imprimir a sequência de Fibonacci até o N-ésimo termo.

n = int(input("Digite o valor de N: "))
a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1