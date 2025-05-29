def quanto_vale(dm): 
    soma = 0
    for simbolo in dm:
        if simbolo == '-':
            soma += 5
        elif simbolo == '.':
            soma += 1
    return soma

def decimal(nm):
    soma = 0
    expoente = 0
    for dm in reversed(nm):
        soma += quanto_vale(dm) * 20**expoente
        expoente += 1
    return soma

def main():
    nm = input()
    while nm != '*':
        nm = nm.split()
        print(decimal(nm))
        nm = input()
    print(0)

main()
