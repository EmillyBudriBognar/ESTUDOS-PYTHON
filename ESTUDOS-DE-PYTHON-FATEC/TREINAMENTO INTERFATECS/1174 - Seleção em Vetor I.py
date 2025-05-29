def gera_lista(qtd):
    A = []
    for i in range(qtd):
        A.append(float(input()))
    return A

def exibe_lista(A):
    for i in range(len(A)):
        if A[i] <= 10:
            print(f'A[{i}] = {A[i]:.1f}')

def main():
    A = gera_lista(100)
    exibe_lista(A)

main()
