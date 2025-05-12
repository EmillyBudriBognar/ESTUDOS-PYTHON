#Problema: Imprimir todos os primos entre A e B.

a = int(input("Digite A: "))
b = int(input("Digite B: "))

print(f"Primos entre {a} e {b}:")
for num in range(a, b + 1):
    if num > 1:
        primo = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                primo = False
                break
            i += 1
        if primo:
            print(num, end=" ")