# Versão while

#     j
#     0     1    2
M = [[5.5, 7.0, 8.7], # 0 i
     [8.0, 6.0, 9.2], # 1 
     [7.8, 8.3, 8.5], # 2 
     [0.0, 9.9, 9.1]] # 3 

i = 0
while i < 4:
    j = 0
    while j < 3:
        print(M[i][j], end=' ')
        j += 1
    print()
    i += 1









##print(M[0][1]) # 7.0
##print(M[0][2]) # 8.0
##print(M[3][0]) # 0.0
##print(M[2][0]) # 7.8
##print(M[3][2]) # 9.1
##print(M[0][0]) # 5.5
##print(M[1][1]) # 6.0
##print(M[2][3]) # erro!
