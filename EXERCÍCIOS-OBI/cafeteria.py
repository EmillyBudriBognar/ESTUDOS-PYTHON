A = int(input())
B = int(input())
C = int(input())
D = int(input())

for i in range(1, C // D + 1):
    cafe = i * D
    leite = C - cafe
    if A <= leite <= B:
        print('S')
        break
else:
    print('N')
