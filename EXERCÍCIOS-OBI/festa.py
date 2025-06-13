E = int(input())
S = int(input())
L = int(input())

distancia = abs(S - E) + abs(L - S) + abs(E - L)
print(distancia)
