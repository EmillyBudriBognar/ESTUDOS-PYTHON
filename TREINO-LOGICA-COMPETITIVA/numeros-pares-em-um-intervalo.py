#Problema: Imprimir números pares entre A e B.

a = int(input("Digite A: "))
b = int(input("Digite B: "))

i = a
while i <= b:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1