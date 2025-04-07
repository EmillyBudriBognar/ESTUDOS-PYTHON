a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a >= b and a >= c:
    print(f'{a} eh o maior')
else:
    if b >= a and b >= c:
        print(f'{b} eh o maior')
    else:
        print(f'{c} eh o maior')
