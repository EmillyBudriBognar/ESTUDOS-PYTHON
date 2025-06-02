def exibe_tabela1(T, L, C):
    i = 0
    while i < L:
        j = 0
        while j < C:
            print(T[i][j])
            j += 1 
        print()
        i += 1

def exibe_tabela2(T, L, C):
    for i in range(L):
        for j in range(C):
            print(T[i][j])
        print()

def exibe_tabela3(T):
    for i in range(len(T)):
        for j in range(len(T[i])):
            print(T[i][j])
        print()

#       tipo      estoque  preço  importado
#        0           1       2      3
T = [['smartphone', 100, 1199.00, True ], # 0 i
     ['televisão',    5, 2599.00, False], # 1
     ['notebook',    20, 4500.00, True ]] # 2

# print(T[0])
# print(T[1])
# print(T[2])
#print(T[1][0])
##i = 0
##if T[i][3]:
##    print(f'{T[i][0]} importado!')
##else:
##    print(f'{T[i][0]} nacional!')
