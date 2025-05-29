while True:
    try:
        a, b = input().split()
        a, b = int(a), int(b)
        print(f'{a} + {b} = {a + b}')
    except (EOFError, KeyboardInterrupt):
        break
