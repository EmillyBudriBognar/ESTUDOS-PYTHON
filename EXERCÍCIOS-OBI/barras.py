N = int(input())

valores = list(map(int, input().split()))

H = max(valores)

for linha in range(H):
    for i in range(N):
        if valores[i] >= H - linha:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print() 
