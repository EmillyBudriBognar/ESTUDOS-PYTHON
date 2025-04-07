def par(n):
    return n % 2 == 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

qtd_pares = 0

if par(a):
    qtd_pares += 1

if par(b):
    qtd_pares += 1

if par(c):
    qtd_pares += 1
    
if par(d):
    qtd_pares += 1

if par(e):
    qtd_pares += 1

print(f'{qtd_pares} valores pares')
